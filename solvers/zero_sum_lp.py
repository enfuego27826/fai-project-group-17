"""Value of a two-player zero-sum game by the sequence-form LP (Koller et al. 1996).

Used for V_Com: with full communication the team is one perfect-recall player
(``games.merged``), so its max-min value is a single LP

    max_{x, v}  v_0   s.t.  F_o^T v <= A^T x,   F_t x = f_t,   x >= 0,

where A[sigma_t, tau_o] = sum_{z ending in (sigma_t, tau_o)} p_c(z) u_T(z).
"""

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp

from solvers.backends import resolve_backend, solve
from solvers.seqform import behavioral_from_realization, sequence_form_constraints


@dataclass
class ZeroSumResult:
    value: float          # max-min value for player tree.team[0] (here V_Com)
    team_policy: dict     # behavioral strategy of the maximizer
    adversary_policy: dict
    seconds: float
    backend: str


def solve_zero_sum(tree, backend="auto"):
    """Max-min value of the maximizer ``tree.team[0]`` against ``tree.adversary``.

    Applied to the merged-team game this is V_Com, the full-communication value.
    """
    backend = resolve_backend(backend)
    t, o = tree.team[0], tree.adversary
    info_t, info_o = tree.players[t], tree.players[o]
    F_t, f_t = sequence_form_constraints(info_t)
    F_o, _ = sequence_form_constraints(info_o)
    A = sp.csr_matrix((tree.term_chance * tree.term_u,
                       (tree.term_seq[:, t], tree.term_seq[:, o])),
                      shape=(info_t.num_seqs, info_o.num_seqs))
    n_v, n_x = F_o.shape[0], info_t.num_seqs
    # Variables: [v (n_v), x (n_x)].
    c = np.zeros(n_v + n_x)
    c[0] = 1.0
    A_ub = sp.hstack([F_o.T, -A.T]).tocsr()
    A_eq = sp.hstack([sp.csr_matrix((F_t.shape[0], n_v)), F_t]).tocsr()
    lb = np.concatenate([np.full(n_v, -np.inf), np.zeros(n_x)])
    res = solve(c, A_ub=A_ub, b_ub=np.zeros(info_o.num_seqs), A_eq=A_eq, b_eq=f_t,
                lb=lb, ub=np.inf, maximize=True, backend=backend)
    x = res.x[n_v:]
    y = np.maximum(res.dual_ub, 0.0)
    return ZeroSumResult(
        value=float(res.obj),
        team_policy=behavioral_from_realization(info_t, x),
        adversary_policy=behavioral_from_realization(info_o, y),
        seconds=res.seconds,
        backend=backend,
    )
