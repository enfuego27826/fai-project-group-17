"""Independent exact TMECor value V_Cor by a single LP (for checking V(0, inf, .)).

Proposition 1(2) of the report says V(0, inf, rho) = V_Cor of the base game.
This module computes V_Cor without column generation, so the two solvers can
be compared.

Enumerate the reduced pure plans sigma_e of one teammate e (the one with fewer
plans). A correlation device mu over (sigma_e, sigma_f) is the same as weights
lambda(sigma_e) together with, for each sigma_e, a conditional mixed strategy
of the other teammate f, which (f having perfect recall) is a realization plan
z_{sigma_e} scaled by lambda(sigma_e). Dualizing the adversary's best response
as in ``solvers.tmecor_cg`` gives one LP:

    max v_0  s.t.  F_o^T v <= sum_{sigma_e} A_{sigma_e} z_{sigma_e},
                   F_f z_{sigma_e} = lambda(sigma_e) e_0,   sum lambda = 1,
                   z, lambda >= 0.

Only feasible when one teammate has few reduced plans (base 3-player Kuhn:
6561 for teammate 0).
"""

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp

from solvers.backends import resolve_backend, solve
from solvers.seqform import count_reduced_plans, enumerate_reduced_plans, sequence_form_constraints


@dataclass
class EnumResult:
    value: float          # V_Cor
    enumerated: int       # teammate whose plans were enumerated
    num_plans: int
    num_variables: int
    num_constraints: int
    seconds: float
    backend: str


def solve_tmecor_enum(tree, backend="auto", plan_limit=50000):
    """V_Cor of the game in ``tree`` by enumerating one teammate's reduced plans."""
    backend = resolve_backend(backend)
    counts = [count_reduced_plans(tree.players[p]) for p in tree.team]
    e_idx = int(np.argmin(counts))
    e, f = tree.team[e_idx], tree.team[1 - e_idx]
    info_e, info_f, adv = tree.players[e], tree.players[f], tree.players[tree.adversary]
    X = enumerate_reduced_plans(info_e, plan_limit)          # (P, S_e)
    P, S_f = X.shape[0], info_f.num_seqs
    F_o, _ = sequence_form_constraints(adv)
    F_f, _ = sequence_form_constraints(info_f)
    n_v, n_seq_o = F_o.shape[0], adv.num_seqs

    coef = tree.term_chance * tree.term_u
    se, sf, so = tree.term_seq[:, e], tree.term_seq[:, f], tree.term_seq[:, tree.adversary]
    # Payoff block: rows = adversary sequences, cols = (plan p, sequence of f).
    plan_idx, term_idx = np.nonzero(X[:, se])           # terminals each plan reaches
    rows = so[term_idx]
    cols = plan_idx * S_f + sf[term_idx]
    A = sp.csr_matrix((coef[term_idx], (rows, cols)), shape=(n_seq_o, P * S_f))

    # Variables: [v (n_v), z (P * S_f), lambda (P)].
    n = n_v + P * S_f + P
    c = np.zeros(n)
    c[0] = 1.0
    A_ub = sp.hstack([F_o.T, -A, sp.csr_matrix((n_seq_o, P))]).tocsr()
    b_ub = np.zeros(n_seq_o)
    # F_f z_p - lambda_p e_0 = 0 for every plan p, and sum lambda = 1.
    rows_f = F_f.shape[0]
    lam_link = sp.csr_matrix((-np.ones(P), (np.arange(P) * rows_f, np.arange(P))),
                             shape=(P * rows_f, P))
    A_eq = sp.vstack([
        sp.hstack([sp.csr_matrix((P * rows_f, n_v)), sp.kron(sp.eye(P), F_f), lam_link]),
        sp.hstack([sp.csr_matrix((1, n_v + P * S_f)), sp.csr_matrix(np.ones((1, P)))]),
    ]).tocsr()
    b_eq = np.zeros(A_eq.shape[0])
    b_eq[-1] = 1.0
    lb = np.concatenate([np.full(n_v, -np.inf), np.zeros(P * S_f + P)])
    res = solve(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, lb=lb, ub=np.inf,
                maximize=True, backend=backend)
    return EnumResult(value=float(res.obj), enumerated=e, num_plans=P, num_variables=n,
                      num_constraints=A_ub.shape[0] + A_eq.shape[0], seconds=res.seconds,
                      backend=res.backend)
