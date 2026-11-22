"""Exact evaluation of one-round signaling games without building the tree (Milestone 6).

The blocker, suit blocker and coordinated attack games with one message round
right after the deal share one structure, which this module evaluates with
small dense arrays instead of the explicit tree of ``games.tree``:

1. chance deals x0 to teammate 0 and x1 to teammate 1 (uniform, independent;
   x1 has one value in the blockers), and a key K uniform over 2^s values;
2. teammate i sends m_i ~ pi_i^msg(. | K, x_i), simultaneously (k bits each);
3. the adversary picks b, seeing (m0, m1) iff rho = pub;
4. teammate i acts a_i ~ pi_i^act(. | K, x_i, m0, m1) without seeing b
   (teammate 0 has no action in the blockers).

The team wins (u_T = 1) iff every acting teammate plays the target tau(x) and
b != c(x), where c(x) is the class the adversary blocks (the card, the suit,
or the target). Payoffs are team-perspective, as everywhere else.

``g`` is the guaranteed value g(pi_T) against the exact best response of the
adversary (Problem Formulation), and ``leakage`` the exact I(M; X), I(M; c(X))
and I(M; c(X) | K). ``tests/test_onestep.py`` checks both against the tree
evaluators (eval.best_response, eval.leakage) on small instances.
"""

from dataclasses import dataclass

import numpy as np


@dataclass
class OneStepGame:
    name: str
    n0: int                 # values of x0 (teammate 0's private information)
    n1: int                 # values of x1 (1 if teammate 1 has none)
    n_act0: int             # teammate 0's actions after the round (1 = no action)
    n_act1: int             # teammate 1's actions
    n_block: int            # adversary actions (classes it can block)
    target0: np.ndarray     # (n0, n1): the action teammate 0 must play (0 if it has none)
    target1: np.ndarray     # (n0, n1): the action teammate 1 must play
    cls: np.ndarray         # (n0, n1): the class c(x) the adversary must avoid blocking


def card_blocker(n):
    x = np.arange(n)[:, None]
    return OneStepGame(f"blocker{n}", n, 1, 1, n, n, np.zeros((n, 1), int), x.copy(), x.copy())


def suit_blocker(suits, ranks):
    n = suits * ranks
    x = np.arange(n)[:, None]
    return OneStepGame(f"suit{suits}x{ranks}", n, 1, 1, n, suits, np.zeros((n, 1), int),
                       x.copy(), x // ranks)


def coordinated_attack(rows, cols):
    t = np.arange(rows)[:, None] * cols + np.arange(cols)[None, :]
    n = rows * cols
    return OneStepGame(f"attack{rows}x{cols}", rows, cols, n, n, n, t.copy(), t.copy(), t.copy())


@dataclass
class TeamPolicy:
    """Behavioral team policy as dense tables (probabilities; rows sum to 1)."""
    msg0: np.ndarray        # (nK, n0, M)
    msg1: np.ndarray        # (nK, n1, M)
    act0: np.ndarray        # (nK, n0, M, M, n_act0)
    act1: np.ndarray        # (nK, n1, M, M, n_act1)


def success_mass(game, pol):
    """A[x0, x1, m0, m1] = P(x, m, every acting teammate plays tau(x)) (chance included)."""
    nK = pol.msg0.shape[0]
    hit0 = _hit(pol.act0, game.target0, own=0)
    hit1 = _hit(pol.act1, game.target1, own=1)
    pm = (pol.msg0[:, :, None, :, None] * pol.msg1[:, None, :, None, :]) / (nK * game.n0 * game.n1)
    return (pm * hit0 * hit1).sum(axis=0)


def _hit(act, target, own):
    """P(teammate plays target[x0, x1] | K, own x, m0, m1) as (nK, n0, n1, M, M)."""
    n0, n1 = target.shape
    x = (np.arange(n0)[:, None] * np.ones((1, n1), int) if own == 0
         else np.ones((n0, 1), int) * np.arange(n1)[None, :])
    return act[:, x, :, :, target].transpose(2, 0, 1, 3, 4)


def class_mass(game, A):
    """C[m0, m1, c] = P(m, team plays tau(x), c(x) = c)."""
    C = np.zeros(A.shape[2:] + (game.n_block,))
    flat = A.reshape(game.n0 * game.n1, *A.shape[2:])
    np.add.at(C, (slice(None), slice(None), game.cls.reshape(-1)), np.moveaxis(flat, 0, -1))
    return C


def guaranteed_value(game, pol, rho):
    """g(pi_T) and the adversary's best response (pub: a block per (m0, m1); priv: one block)."""
    A = success_mass(game, pol)
    C = class_mass(game, A)
    total = A.sum()
    if rho == "pub":
        br = C.argmax(axis=-1)
        return float(total - C.max(axis=-1).sum()), br
    per_class = C.sum(axis=(0, 1))
    b = int(per_class.argmax())
    return float(total - per_class[b]), np.full(C.shape[:2], b)


def _mi(joint):
    joint = joint / joint.sum()
    pa, pb = joint.sum(1, keepdims=True), joint.sum(0, keepdims=True)
    nz = joint > 0
    return max(0.0, float((joint[nz] * np.log2(joint[nz] / (pa @ pb)[nz])).sum()))


def leakage(game, pol):
    """(I(M; X), I(M; c(X)), I(M; c(X) | K)) in bits, M = (m0, m1), X = (x0, x1)."""
    nK = pol.msg0.shape[0]
    M = pol.msg0.shape[-1]
    pm = (pol.msg0[:, :, None, :, None] * pol.msg1[:, None, :, None, :]) / (nK * game.n0 * game.n1)
    pxm = pm.sum(0).reshape(game.n0 * game.n1, M * M)
    cls = game.cls.reshape(-1)

    def by_class(p):
        out = np.zeros((game.n_block, p.shape[1]))
        np.add.at(out, cls, p)
        return out

    i_x = _mi(pxm)
    i_c = _mi(by_class(pxm))
    i_ck = sum(_mi(by_class(pm[K].reshape(game.n0 * game.n1, M * M))) / nK for K in range(nK))
    return i_x, i_c, i_ck
