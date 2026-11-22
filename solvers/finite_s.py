"""Bounds on V(k, s, rho) for finite key length s (Milestone 2, task 4).

Upper bound. U(k, s, rho) = V(k, inf, rho) (Proposition 1: V is nondecreasing
in s), computed by ``solvers.tmecor_cg``.

Lower bound. L(k, s, rho) is the best value over team strategies that assign
one joint pure plan of the team to each of the 2^s equally likely key values,
against an exact adversary best response. In Gamma(k, s, rho) both teammates
observe the key K at the root, so such a strategy is exactly one joint pure
plan (x_1, x_2) of Gamma(k, s, rho) itself, and

    L = max_{x_1, x_2 pure}  min_y  sum_z p_c(z) u_T(z) x_1(z) x_2(z) y(z).

L leaves out the teammates' private randomization (each teammate may also mix
independently given K), so L can be strictly below V(k, s, rho). It is a
valid lower bound because every such strategy is available to the team.

Two exact methods:

* Enumeration of all pairs of reduced pure plans, with an exact adversary best
  response for each pair (used when the number of pairs is at most
  ``enum_limit``).
* MILP. Binary sequence-form vectors x_1, x_2, McCormick product variables w
  for each pair of team sequences that ends a terminal history, and the
  adversary's minimization replaced by the dual of its sequence-form LP:

      max v_0  s.t.  F_o^T v <= B w,   F_i x_i = f_i,   w = x_1 x_2 (McCormick),

  where B[tau, (sigma_1, sigma_2)] = sum of p_c(z) u_T(z) over terminals z
  ending in (sigma_1, sigma_2, tau). On a time limit the MILP returns its
  incumbent (a valid lower bound on L, hence on V) and its proven bound on L.
"""

from dataclasses import dataclass
import time

import numpy as np
import scipy.sparse as sp

from eval.sequence_form import best_response
from solvers.backends import resolve_backend, solve
from solvers.seqform import (count_reduced_plans, enumerate_reduced_plans,
                             plan_from_realization, sequence_form_constraints)


@dataclass
class KeyPureResult:
    value: float          # L(k, s, rho) if optimal, else the incumbent's value (lower bound on L)
    bound: float          # proven upper bound on L (= value when optimal); NOT a bound on V
    optimal: bool
    profile: dict         # {teammate: pure plan of Gamma(k, s, rho)} attaining ``value``
    method: str           # "enumerate" or "milp"
    num_pairs: int        # number of joint reduced pure plans
    seconds: float
    backend: str


def solve_key_pure(tree, backend="auto", enum_limit=2_000_000, time_limit=None):
    """L(k, s, rho): best key-indexed joint pure team plan against an exact best response.

    ``tree`` is Gamma(k, s, rho) with a finite s (key node at the root when
    s > 0). Lower bound on V(k, s, rho); see the module docstring.
    """
    backend = resolve_backend(backend)
    start = time.perf_counter()
    t0, t1 = tree.team
    infos = (tree.players[t0], tree.players[t1])
    counts = [count_reduced_plans(info) for info in infos]
    num_pairs = counts[0] * counts[1]
    if num_pairs <= enum_limit:
        value, x0, x1 = _enumerate(tree, infos)
        bound, optimal, method = value, True, "enumerate"
    else:
        value, bound, optimal, x0, x1 = _milp(tree, infos, backend, time_limit)
        method = "milp"
    profile = {t0: plan_from_realization(infos[0], x0), t1: plan_from_realization(infos[1], x1)}
    return KeyPureResult(value=value, bound=bound, optimal=optimal, profile=profile,
                         method=method, num_pairs=num_pairs,
                         seconds=time.perf_counter() - start, backend=backend)


def _adversary_leaf(tree, coef, x_e, e, f, n_f):
    """B_e[tau, sigma_f] = sum_z coef(z) x_e(z) over terminals ending in (sigma_f, tau)."""
    s_e, s_f = tree.term_seq[:, e], tree.term_seq[:, f]
    so = tree.term_seq[:, tree.adversary]
    w = coef * x_e[s_e]
    on = w != 0
    return sp.csr_matrix((w[on], (so[on], s_f[on])),
                         shape=(tree.players[tree.adversary].num_seqs, n_f))


def _enumerate(tree, infos):
    """Exact L by enumerating joint reduced pure plans (adversary best-responds to each)."""
    t = tree.team
    counts = [count_reduced_plans(info) for info in infos]
    e_idx = int(np.argmin(counts))
    f_idx = 1 - e_idx
    X_e = enumerate_reduced_plans(infos[e_idx], counts[e_idx])
    X_f = enumerate_reduced_plans(infos[f_idx], counts[f_idx])
    adv = tree.players[tree.adversary]
    coef = tree.term_chance * tree.term_u
    best = (-np.inf, None, None)
    for x_e in X_e:
        B = _adversary_leaf(tree, coef, x_e, t[e_idx], t[f_idx], infos[f_idx].num_seqs)
        leaf = np.asarray((B @ X_f.T))                  # (adversary seqs, plans of f)
        values, _ = best_response(adv, leaf, maximize=False)
        j = int(np.argmax(values))
        if values[j] > best[0] + 1e-12:
            best = (float(values[j]), x_e, X_f[j])
    value, x_e, x_f = best
    return (value, x_e, x_f) if e_idx == 0 else (value, x_f, x_e)


def _guaranteed(tree, x0, x1):
    """g of the joint pure plan (x0, x1): exact adversary best response value."""
    coef = tree.term_chance * tree.term_u * x0[tree.term_seq[:, tree.team[0]]] \
        * x1[tree.term_seq[:, tree.team[1]]]
    adv = tree.players[tree.adversary]
    leaf = np.bincount(tree.term_seq[:, tree.adversary], weights=coef, minlength=adv.num_seqs)
    return float(best_response(adv, leaf, maximize=False)[0])


def _milp(tree, infos, backend, time_limit):
    """L by a MILP with the adversary's best response dualized."""
    t0, t1 = tree.team
    s0, s1 = tree.term_seq[:, t0], tree.term_seq[:, t1]
    so = tree.term_seq[:, tree.adversary]
    adv = tree.players[tree.adversary]
    coef = tree.term_chance * tree.term_u

    pairs, pair_of_term = np.unique(np.stack([s0, s1], axis=1), axis=0, return_inverse=True)
    pair_of_term = pair_of_term.ravel()
    n0, n1, npair = infos[0].num_seqs, infos[1].num_seqs, len(pairs)
    F0, f0 = sequence_form_constraints(infos[0])
    F1, f1 = sequence_form_constraints(infos[1])
    F_o, _ = sequence_form_constraints(adv)
    n_v, n_so = F_o.shape[0], adv.num_seqs
    # Variables: [x0 (n0), x1 (n1), w (npair), v (n_v)]; maximize v_0.
    n = n0 + n1 + npair + n_v
    iw, iv = n0 + n1, n0 + n1 + npair
    c = np.zeros(n)
    c[iv] = 1.0

    B = sp.csr_matrix((coef, (so, pair_of_term)), shape=(n_so, npair))
    dual_rows = sp.hstack([sp.csr_matrix((n_so, n0 + n1)), -B, F_o.T]).tocsr()
    r = np.arange(npair)
    w, i0, i1 = iw + r, pairs[:, 0], n0 + pairs[:, 1]
    ones = np.ones(npair)
    mcc = sp.csr_matrix((np.concatenate([ones, -ones, ones, -ones, ones, ones, -ones]),
                         (np.concatenate([r, r, npair + r, npair + r,
                                          2 * npair + r, 2 * npair + r, 2 * npair + r]),
                          np.concatenate([w, i0, w, i1, i0, i1, w]))),
                        shape=(3 * npair, n))
    A_ub = sp.vstack([dual_rows, mcc]).tocsr()
    b_ub = np.concatenate([np.zeros(n_so), np.zeros(2 * npair), ones])
    A_eq = sp.hstack([sp.block_diag([F0, F1]), sp.csr_matrix((F0.shape[0] + F1.shape[0],
                                                               npair + n_v))]).tocsr()
    b_eq = np.concatenate([f0, f1])
    lb = np.concatenate([np.zeros(n0 + n1 + npair), np.full(n_v, -np.inf)])
    ub = np.concatenate([np.ones(n0 + n1 + npair), np.full(n_v, np.inf)])
    integrality = np.concatenate([np.ones(n0 + n1), np.zeros(npair + n_v)])
    res = solve(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, lb=lb, ub=ub,
                integrality=integrality, maximize=True, backend=backend,
                time_limit=time_limit)
    if res.x is None:
        raise RuntimeError("MILP found no team plan within the time limit")
    x0, x1 = np.round(res.x[:n0]), np.round(res.x[n0:n0 + n1])
    value = _guaranteed(tree, x0, x1)  # recomputed exactly from the rounded plans
    optimal = res.status == "optimal"
    bound = float(res.bound) if res.bound is not None else value
    if optimal:
        bound = max(bound, value)
    return value, bound, optimal, x0, x1



@dataclass
class BilinearResult:
    value: float          # best team strategy found: g of it (lower bound on V(k, s, rho))
    bound: float          # proven upper bound on V(k, s, rho) (= value when optimal)
    optimal: bool
    profile: dict         # {teammate: behavioral policy of Gamma(k, s, rho)}
    seconds: float


def solve_bilinear(tree, time_limit=None, rlt_limit=0):
    """V(k, s, rho) exactly, by global optimization of the bilinear team problem (Gurobi only).

    The team plays behavioral strategies of Gamma(k, s, rho) (both teammates
    see the key, and each may randomize privately), so with realization plans
    x_1, x_2 and the adversary's best response dualized,

        V = max v_0  s.t.  F_o^T v <= B w,  F_i x_i = f_i,  x_i >= 0,
                           w_(sigma_1, sigma_2) = x_1(sigma_1) x_2(sigma_2).

    The product constraints make the problem nonconvex (this is the TME
    problem of Gamma(k, s, rho)); Gurobi's spatial branch and bound
    (NonConvex = 2) solves it to global optimality, or returns the incumbent
    and a proven bound on a time limit. Only practical on tiny games.

    If n_1 n_2 <= ``rlt_limit``, a product variable W[sigma_1, sigma_2] is
    added for every pair of team sequences, with the valid linear constraints
    F_1 W = f_1 x_2^T and W F_2^T = x_1 f_2^T (sequence-form constraints of
    one teammate multiplied by the other's variables) and W <= x_i. The
    bilinear constraints are still imposed only where they matter (pairs that
    end a terminal history), so the value is unchanged and the relaxation is
    tighter. Off by default: on the blocker game (k = 2, s = 0, pub) the
    larger model gave a worse bound within the same time limit.
    """
    import gurobipy as gp
    from gurobipy import GRB

    from eval.best_response import guaranteed_value
    from solvers.backends import _gurobi_env
    from solvers.seqform import behavioral_from_realization

    if resolve_backend("auto") != "gurobi":
        raise RuntimeError("solve_bilinear needs Gurobi")
    start = time.perf_counter()
    t0, t1 = tree.team
    infos = (tree.players[t0], tree.players[t1])
    s0, s1 = tree.term_seq[:, t0], tree.term_seq[:, t1]
    so = tree.term_seq[:, tree.adversary]
    adv = tree.players[tree.adversary]
    coef = tree.term_chance * tree.term_u
    pairs, pair_of_term = np.unique(np.stack([s0, s1], axis=1), axis=0, return_inverse=True)
    pair_of_term = pair_of_term.ravel()
    F0, f0 = sequence_form_constraints(infos[0])
    F1, f1 = sequence_form_constraints(infos[1])
    F_o, _ = sequence_form_constraints(adv)
    B = sp.csr_matrix((coef, (so, pair_of_term)), shape=(adv.num_seqs, len(pairs)))

    n0, n1 = infos[0].num_seqs, infos[1].num_seqs
    m = gp.Model(env=_gurobi_env())
    m.Params.NonConvex = 2
    m.Params.FeasibilityTol = 1e-9
    m.Params.MIPGap = 1e-9
    m.Params.MIPGapAbs = 1e-9
    if time_limit:
        m.Params.TimeLimit = time_limit
    x0 = m.addMVar(n0, lb=0.0, ub=1.0)
    x1 = m.addMVar(n1, lb=0.0, ub=1.0)
    v = m.addMVar(F_o.shape[0], lb=-np.inf)
    m.addConstr(F0 @ x0 == f0)
    m.addConstr(F1 @ x1 == f1)
    if n0 * n1 <= rlt_limit:
        W = m.addMVar((n0, n1), lb=0.0, ub=1.0)
        w = W.reshape(-1)[(pairs[:, 0] * n1 + pairs[:, 1]).tolist()]
        for j in range(n1):
            m.addConstr(F0 @ W[:, j] == f0 * x1[j])
        for i in range(n0):
            m.addConstr(F1 @ W[i, :] == f1 * x0[i])
            m.addConstr(W[i, :] <= x1)
        for j in range(n1):
            m.addConstr(W[:, j] <= x0)
    else:
        w = m.addMVar(len(pairs), lb=0.0, ub=1.0)
    m.addConstr(F_o.T @ v - B @ w <= 0)
    for r, (i, j) in enumerate(pairs):
        m.addConstr(w[r] == x0[int(i)] * x1[int(j)])
    m.setObjective(v[0], GRB.MAXIMIZE)
    m.optimize()
    if m.SolCount == 0:
        raise RuntimeError(f"no solution found (Gurobi status {m.Status})")
    profile = {t0: behavioral_from_realization(infos[0], np.maximum(x0.X, 0.0)),
               t1: behavioral_from_realization(infos[1], np.maximum(x1.X, 0.0))}
    value = guaranteed_value(tree, [(1.0, profile)])  # exact g of the returned strategy
    optimal = m.Status == GRB.OPTIMAL
    bound = max(float(m.ObjBound), value) if optimal else float(m.ObjBound)
    return BilinearResult(value=value, bound=bound, optimal=optimal, profile=profile,
                          seconds=time.perf_counter() - start)
