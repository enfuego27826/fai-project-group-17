"""Sequence-form constraint matrices and reduced pure plans (Koller et al. 1996).

For a perfect-recall player with sequences S and information sets I, a
realization plan x in R^S satisfies F x = f, x >= 0 with

    x[empty] = 1,   sum_{a in A(I)} x[(I, a)] - x[parent(I)] = 0   for all I.

A reduced pure plan is a 0/1 realization plan: it picks one action at every
information set its own earlier choices reach, and nothing elsewhere.
"""

import itertools

import numpy as np
import scipy.sparse as sp


def sequence_form_constraints(info):
    """(F, f): the sequence-form polytope {x >= 0 : F x = f} of one player."""
    rows, cols, vals = [0], [0], [1.0]
    for infoset in range(info.num_infosets):
        r = infoset + 1
        for seq in info.seqs_of(infoset):
            rows.append(r), cols.append(seq), vals.append(1.0)
        rows.append(r), cols.append(info.infoset_parent_seq[infoset]), vals.append(-1.0)
    F = sp.csr_matrix((vals, (rows, cols)), shape=(info.num_infosets + 1, info.num_seqs))
    f = np.zeros(info.num_infosets + 1)
    f[0] = 1.0
    return F, f


def child_infosets(info):
    """children[sigma] = information sets whose parent sequence is sigma."""
    children = [[] for _ in range(info.num_seqs)]
    for infoset in range(info.num_infosets):
        children[info.infoset_parent_seq[infoset]].append(infoset)
    return children


def count_reduced_plans(info):
    """Number of reduced pure plans of one player (may be astronomically large)."""
    count = [1] * info.num_seqs  # plans below each sequence (Python ints, no overflow)
    for infoset in range(info.num_infosets - 1, -1, -1):
        count[info.infoset_parent_seq[infoset]] *= sum(count[s] for s in info.seqs_of(infoset))
    return count[0]


def enumerate_reduced_plans(info, limit):
    """All reduced pure plans as a 0/1 matrix of shape (num_plans, num_seqs).

    Raises ValueError if there are more than ``limit`` plans.
    """
    n = count_reduced_plans(info)
    if n > limit:
        raise ValueError(f"{n} reduced plans exceed the limit {limit}")
    children = child_infosets(info)

    def below(seq):
        """List of frozensets: sequences switched on under ``seq`` (excluded)."""
        options_per_child = []
        for infoset in children[seq]:
            opts = []
            for s in info.seqs_of(infoset):
                for rest in below(s):
                    opts.append(rest | {s})
            options_per_child.append(opts)
        return [frozenset().union(*combo) for combo in itertools.product(*options_per_child)]

    plans = below(0)
    X = np.zeros((len(plans), info.num_seqs), dtype=np.float64)
    X[:, 0] = 1.0
    for i, plan in enumerate(plans):
        X[i, list(plan)] = 1.0
    return X


def plan_from_realization(info, x, tol=0.5):
    """Pure plan {information state: action} from a 0/1 realization plan.

    Information sets the plan does not reach get the first legal action; this
    does not change outcomes but gives a complete policy.
    """
    plan = {}
    for infoset, key in enumerate(info.infoset_keys):
        seqs = list(info.seqs_of(infoset))
        on = [j for j, s in enumerate(seqs) if x[s] > tol]
        plan[key] = info.infoset_actions[infoset][on[0] if on else 0]
    return plan


def behavioral_from_realization(info, y, tol=1e-12):
    """Behavioral policy pi(a | I) = y(I, a) / y(parent(I)) (uniform where y(parent) = 0).

    Normalizes by sum_a y(I, a), which equals y(parent(I)) for a feasible plan.
    """
    policy = {}
    for infoset, key in enumerate(info.infoset_keys):
        seqs = list(info.seqs_of(infoset))
        acts = info.infoset_actions[infoset]
        vals = np.maximum(np.asarray([y[s] for s in seqs]), 0.0)
        total = vals.sum()
        if total <= tol:
            policy[key] = {a: 1.0 / len(acts) for a in acts}
        else:
            policy[key] = {a: float(v / total) for a, v in zip(acts, vals)}
    return policy
