"""TMECor value V(k, infinity, rho) by column generation.

With s = infinity the team's key is replaced by a correlation device mu over
joint pure plans (Definition 1), so

    V(k, inf, rho) = max_{mu in Delta(Sigma_1 x Sigma_2)} min_{pi_o} E_mu[u_T]

on the game Gamma(k, 0, rho), which has no key node. We solve it by column
generation over joint team pure plans (as in Farina et al. 2018):

* Master LP. Given columns j = (sigma_1^j, sigma_2^j), write
  a_j(tau) = sum_{z : tau_o(z) = tau} p_c(z) u_T(z) 1[sigma^j reaches z]
  for adversary sequences tau, and dualize the adversary's sequence-form
  minimization:

      max  v_0   s.t.  F_o^T v <= sum_j lambda_j a_j,   sum_j lambda_j = 1,
                       lambda >= 0, v free.

  The duals of the first constraints are a realization plan y of the
  adversary that minimizes max_j a_j^T y.
* Pricing. Find the joint pure plan maximizing
  sum_z p_c(z) u_T(z) y(tau_o(z)) x_1(sigma_1(z)) x_2(sigma_2(z)). Either by
  enumerating one teammate's reduced plans and best-responding with the other
  (exact, used when the smaller plan count is at most ``enum_limit``), or by a
  MILP over binary sequence-form vectors x_1, x_2 with McCormick product
  variables, one per pair of team sequences that ends a terminal history.
  In MILP mode each iteration first tries a cheap alternating best response
  (fix one teammate's plan, best-respond with the other, repeat) started from
  every column found so far; the MILP is only called when that finds no
  improving column, so the final certificate of optimality is always exact.
* Stop when the best new column does not beat the master value by more than
  ``tol``; then the master value is V(k, inf, rho).
"""

from dataclasses import dataclass, field
import time

import numpy as np
import scipy.sparse as sp

from eval.sequence_form import best_response
from solvers.backends import resolve_backend, solve
from solvers.seqform import (behavioral_from_realization, count_reduced_plans,
                             enumerate_reduced_plans, plan_from_realization,
                             sequence_form_constraints)


@dataclass
class TMECorResult:
    value: float                 # V(k, inf, rho) if converged, else the lower bound
    support: list                # [(weight, {player: pure plan})], the correlation device mu
    adversary_policy: dict       # adversary's equilibrium behavioral strategy
    iterations: int
    num_columns: int
    converged: bool              # False if exact pricing hit its time limit
    upper_bound: float           # proven upper bound on V (= value when converged)
    pricing: str                 # "enumerate" or "milp"
    backend: str
    master_seconds: float = 0.0
    pricing_seconds: float = 0.0
    log: list = field(default_factory=list)  # (iteration, master, pricing value, exact?)
    reached_known_upper: bool = False  # stopped because the master reached ``known_upper``


class _Pricer:
    """Best joint team pure plan against an adversary realization plan y."""

    def __init__(self, tree, backend, enum_limit, seed=0):
        self.tree = tree
        self.backend = backend
        t0, t1 = tree.team
        self.infos = (tree.players[t0], tree.players[t1])
        self.coef = tree.term_chance * tree.term_u
        self.rng = np.random.default_rng(seed)
        self.s0 = tree.term_seq[:, t0]
        self.s1 = tree.term_seq[:, t1]
        self.so = tree.term_seq[:, tree.adversary]
        counts = [count_reduced_plans(info) for info in self.infos]
        self.enum_side = int(np.argmin(counts))
        self.mode = "enumerate" if counts[self.enum_side] <= enum_limit else "milp"
        if self.mode == "enumerate":
            self.plans = enumerate_reduced_plans(self.infos[self.enum_side], enum_limit)
        else:
            self._setup_milp()

    def _pair_matrix(self, y):
        """Q[sigma_0, sigma_1] = sum of p_c u_T y over terminals ending in that pair."""
        q = self.coef * y[self.so]
        n0, n1 = self.infos[0].num_seqs, self.infos[1].num_seqs
        return sp.csr_matrix((q, (self.s0, self.s1)), shape=(n0, n1))

    def __call__(self, y, threshold, starts=(), time_limit=None):
        """Return (value, x_0, x_1, exact, upper) for a good joint pure plan against y.

        If ``exact`` is False the plan comes from the heuristic and has value
        above ``threshold``. Otherwise exact pricing ran and ``upper`` is a
        proven upper bound on the best plan's value: equal to ``value`` when
        solved to optimality, at most ``threshold`` when the MILP proved that no
        plan beats it, or the MILP's bound when it hit ``time_limit``.
        """
        Q = self._pair_matrix(y)
        if self.mode == "enumerate":
            value, x0, x1 = self._enumerate(Q)
            return value, x0, x1, True, value
        if starts:
            value, x0, x1 = self._alternating(Q, starts)
            if value > threshold:
                return value, x0, x1, False, None
        value, x0, x1, upper = self._milp(Q, threshold, time_limit)
        return value, x0, x1, True, upper

    def _alternating(self, Q, starts, rounds=10):
        """Alternating best responses from the given (x0, x1) starts, batched."""
        info0, info1 = self.infos
        X1 = np.stack([x1 for _, x1 in starts] + self._random_plans(info1), axis=1)
        best = (-np.inf, None, None)
        for _ in range(rounds):
            v0, c0 = best_response(info0, np.asarray(Q @ X1), maximize=True)
            X0 = _pure_realization(info0, c0)
            v1, c1 = best_response(info1, np.asarray(Q.T @ X0), maximize=True)
            X1_new = _pure_realization(info1, c1)
            j = int(np.argmax(v1))
            if v1[j] > best[0] + 1e-12:
                best = (float(v1[j]), X0[:, j].copy(), X1_new[:, j].copy())
            if np.array_equal(X1_new, X1):
                break
            X1 = X1_new
        return best

    def _enumerate(self, Q):
        e = self.enum_side
        other = self.infos[1 - e]
        # Leaf values of the other teammate for every plan of the enumerated one.
        leaf = (Q.T @ self.plans.T) if e == 0 else (Q @ self.plans.T)  # (S_other, P)
        values, choice = best_response(other, np.asarray(leaf), maximize=True)
        best = int(np.argmax(values))
        x_other = _pure_realization(other, choice[:, best])
        x_e = self.plans[best]
        x0, x1 = (x_e, x_other) if e == 0 else (x_other, x_e)
        return float(values[best]), x0, x1

    def _random_plans(self, info, count=32):
        """Random pure plans of one teammate, as extra heuristic starts."""
        if info.num_infosets == 0:
            return []
        choice = np.stack([self.rng.integers(0, n, size=count) for n in info.infoset_num_actions])
        X = _pure_realization(info, choice.reshape(info.num_infosets, count))
        return [X[:, j] for j in range(count)]

    def _setup_milp(self):
        pairs = np.unique(np.stack([self.s0, self.s1], axis=1), axis=0)
        self.pairs = pairs
        n0, n1, npair = self.infos[0].num_seqs, self.infos[1].num_seqs, len(pairs)
        self.n = n0 + n1 + npair
        F0, f0 = sequence_form_constraints(self.infos[0])
        F1, f1 = sequence_form_constraints(self.infos[1])
        self.A_eq = sp.block_diag([F0, F1, sp.csr_matrix((0, npair))]).tocsr()
        self.b_eq = np.concatenate([f0, f1])
        # McCormick for w = x0 * x1 on binaries: w <= x0, w <= x1, w >= x0 + x1 - 1.
        r = np.arange(npair)
        w = n0 + n1 + r
        i0 = pairs[:, 0]
        i1 = n0 + pairs[:, 1]
        rows = np.concatenate([r, r, npair + r, npair + r, 2 * npair + r, 2 * npair + r,
                               2 * npair + r])
        cols = np.concatenate([w, i0, w, i1, i0, i1, w])
        vals = np.concatenate([np.ones(npair), -np.ones(npair), np.ones(npair), -np.ones(npair),
                               np.ones(npair), np.ones(npair), -np.ones(npair)])
        self.A_ub = sp.csr_matrix((vals, (rows, cols)), shape=(3 * npair, self.n))
        self.b_ub = np.concatenate([np.zeros(2 * npair), np.ones(npair)])
        self.integrality = np.concatenate([np.ones(n0 + n1), np.zeros(npair)])
        self.ub = np.ones(self.n)

    def _milp(self, Q, threshold, time_limit=None):
        n0, n1 = self.infos[0].num_seqs, self.infos[1].num_seqs
        c = np.zeros(self.n)
        c[n0 + n1:] = np.asarray(Q[self.pairs[:, 0], self.pairs[:, 1]]).ravel()
        res = solve(c, A_ub=self.A_ub, b_ub=self.b_ub, A_eq=self.A_eq, b_eq=self.b_eq,
                    lb=0.0, ub=self.ub, integrality=self.integrality, maximize=True,
                    backend=self.backend, bound_stop=threshold, time_limit=time_limit)
        upper = res.bound if res.bound is not None else res.obj
        if res.x is None:  # stopped before finding any plan
            return -np.inf, None, None, upper
        x0 = np.round(res.x[:n0])
        x1 = np.round(res.x[n0:n0 + n1])
        # Recompute the objective exactly from the rounded plans.
        value = float(x0 @ (Q @ x1))
        return value, x0, x1, max(upper, value) if res.status == "optimal" else upper


def _pure_realization(info, choice):
    """0/1 realization plan(s) from best-response action indices at every infoset.

    ``choice`` has shape (num_infosets,) or (num_infosets, B); the result has
    shape (num_seqs,) or (num_seqs, B).
    """
    choice = np.asarray(choice, dtype=np.int64)
    x = np.zeros((info.num_seqs,) + choice.shape[1:])
    x[0] = 1.0
    for infoset in range(info.num_infosets):
        on = x[info.infoset_parent_seq[infoset]]
        seq = info.infoset_first_seq[infoset] + choice[infoset]
        if choice.ndim == 1:
            x[seq] = on
        else:
            x[seq, np.arange(choice.shape[1])] = on
    return x


def _first_action_plan(info):
    return _pure_realization(info, np.zeros(info.num_infosets, dtype=np.int64))


def solve_tmecor(tree, backend="auto", enum_limit=20000, tol=1e-9, max_iters=10000,
                 pricing_time_limit=None, seed=0, verbose=False, known_upper=None):
    """V(k, inf, rho): TMECor value of the game in ``tree`` by column generation.

    ``tree`` must have no key node (build it from Gamma(k, 0, rho) or with
    s = infinity). Returns the value, the correlation device (support over
    joint pure plans), the adversary's equilibrium strategy, and solver stats.

    If an exact (MILP) pricing call hits ``pricing_time_limit`` seconds
    without finding an improving column, the solve stops with
    ``converged=False``: then ``value`` (the master value, attained by the
    returned support) is a lower bound on V and ``upper_bound`` (the MILP's
    bound against the master's adversary strategy) is an upper bound.

    ``known_upper`` is an upper bound on V proved elsewhere (e.g. V_Com, by
    Proposition 1). If the master value reaches it, the solve stops with
    ``reached_known_upper=True``, ``converged=False`` and
    ``upper_bound=known_upper``: V equals the value by that external bound,
    not by this solver's own pricing.
    """
    backend = resolve_backend(backend)
    t0, t1 = tree.team
    adv = tree.players[tree.adversary]
    F_o, _ = sequence_form_constraints(adv)
    n_rows = F_o.shape[0]           # dual variables v (root + one per adversary infoset)
    n_seq_o = adv.num_seqs
    coef = tree.term_chance * tree.term_u
    so = tree.term_seq[:, tree.adversary]
    pricer = _Pricer(tree, backend, enum_limit, seed)

    def column(x0, x1):
        reach = coef * x0[tree.term_seq[:, t0]] * x1[tree.term_seq[:, t1]]
        return np.bincount(so, weights=reach, minlength=n_seq_o)

    infos = (tree.players[t0], tree.players[t1])
    plans = [(_first_action_plan(infos[0]), _first_action_plan(infos[1]))]
    cols = [column(*plans[0])]
    seen = {(plans[0][0].tobytes(), plans[0][1].tobytes())}
    log = []
    master_time = pricing_time = 0.0

    for it in range(1, max_iters + 1):
        J = len(cols)
        A = np.stack(cols, axis=1)  # (n_seq_o, J)
        # Variables: [v (n_rows), lambda (J)]. Maximize v_0.
        c = np.zeros(n_rows + J)
        c[0] = 1.0
        A_ub = sp.hstack([F_o.T, sp.csr_matrix(-A)]).tocsr()
        A_eq = sp.csr_matrix(np.concatenate([np.zeros(n_rows), np.ones(J)])[None, :])
        lb = np.concatenate([np.full(n_rows, -np.inf), np.zeros(J)])
        t_start = time.perf_counter()
        master = solve(c, A_ub=A_ub, b_ub=np.zeros(n_seq_o), A_eq=A_eq, b_eq=[1.0],
                       lb=lb, ub=np.inf, maximize=True, backend=backend)
        master_time += time.perf_counter() - t_start
        y = np.maximum(master.dual_ub, 0.0)

        threshold = master.obj + tol * max(1.0, abs(master.obj))
        if known_upper is not None and threshold >= known_upper:
            converged, upper_bound, reached = False, float(known_upper), True
            log.append((it, master.obj, None, False))
            break
        t_start = time.perf_counter()
        price, x0, x1, exact, upper = pricer(y, threshold, starts=plans,
                                             time_limit=pricing_time_limit)
        pricing_time += time.perf_counter() - t_start
        log.append((it, master.obj, price, exact))
        if verbose:
            kind = "exact" if exact else "heur"
            bound = "" if upper is None else f"  bound {upper:.10f}"
            print(f"  iter {it:4d}  master {master.obj:.10f}  pricing {price:.10f} ({kind})"
                  f"{bound}  cols {J}", flush=True)
        if price <= threshold:
            converged = upper <= threshold
            upper_bound = master.obj if converged else upper
            reached = False
            break
        key = (x0.tobytes(), x1.tobytes())
        if key in seen:
            raise RuntimeError(f"pricing returned an existing column with value {price} > "
                               f"master {master.obj}; numerical trouble")
        seen.add(key)
        plans.append((x0, x1))
        cols.append(column(x0, x1))
    else:
        raise RuntimeError(f"column generation did not converge in {max_iters} iterations")

    lam = master.x[n_rows:]
    support = []
    for weight, (x0, x1) in zip(lam, plans):
        if weight > 1e-12:
            support.append((float(weight), {t0: plan_from_realization(infos[0], x0),
                                            t1: plan_from_realization(infos[1], x1)}))
    total = sum(w for w, _ in support)
    support = [(w / total, prof) for w, prof in support]
    return TMECorResult(
        value=float(master.obj),
        support=support,
        adversary_policy=behavioral_from_realization(adv, y),
        iterations=it,
        num_columns=len(cols),
        converged=converged,
        upper_bound=float(upper_bound),
        pricing=pricer.mode,
        backend=backend,
        master_seconds=master_time,
        pricing_seconds=pricing_time,
        log=log,
        reached_known_upper=reached,
    )
