"""Exact leakage Leak(pi_T) = I(M; X) of a team policy (Problem Formulation).

X = (X_1, X_2) is the teammates' private information and M the messages. By
default (``games.augment``) X is, for every round, each teammate's base-game
information state at the start of the round, i.e. what it knew when it sent
its message; for Kuhn and card guessing with a round after the deal, X is the
teammates' cards. M is either all messages (``channel="all"``: what the
adversary would learn on a public channel) or only what the adversary actually
observes (``channel="adversary"``: empty when rho = priv).

The joint law of (M, X) generally depends on the adversary's policy (messages
in later rounds depend on its earlier moves), so the adversary policy is an
argument; it defaults to uniform. With a single round before any adversary
move it does not matter.
"""

from collections import defaultdict

import numpy as np

from eval.sequence_form import realization_plan, team_terminal_weights, uniform_policy


def leakage_labels(state):
    """Terminal label used by ``mutual_information``: (all messages, adversary's messages, X, key)."""
    return (state.messages(), state.adversary_messages(), state.team_private_info(),
            getattr(state, "key", None))


def _entropy(probs):
    p = np.asarray([v for v in probs if v > 0])
    return float(-(p * np.log2(p)).sum())


def mutual_information(tree, team_strategy, adversary_policy=None, channel="all", phi=None,
                       given_key=False):
    """I(M; X) in bits under ``team_strategy`` and ``adversary_policy``.

    ``tree`` must be built with ``label_fn=eval.leakage.leakage_labels``.
    With ``phi`` (a function of the X label) it returns the exploitable leakage
    I(M; phi(X)) instead, where phi(X) is the part of the private information
    the adversary's payoff depends on (Milestone 5). With ``given_key`` it
    returns the conditional I(M; X | K) (or I(M; phi(X) | K)): what a holder of
    the key learns from the messages, e.g. whether a padded suit is decodable.
    """
    if tree.term_labels is None:
        raise ValueError("build the tree with label_fn=leakage_labels")
    adv = tree.players[tree.adversary]
    adversary_policy = adversary_policy or uniform_policy(adv)
    prob = team_terminal_weights(tree, team_strategy)
    prob = prob * realization_plan(adv, adversary_policy)[tree.term_seq[:, tree.adversary]]

    which = {"all": 0, "adversary": 1}[channel]
    if given_key:
        by_key = defaultdict(lambda: (defaultdict(float), defaultdict(float), defaultdict(float)))
        for p, label in zip(prob, tree.term_labels):
            if p == 0:
                continue
            m, x = label[which], phi(label[2]) if phi is not None else label[2]
            joint, pm, px = by_key[label[3]]
            joint[(m, x)] += p
            pm[m] += p
            px[x] += p
        total = sum(sum(j.values()) for j, _, _ in by_key.values())
        out = 0.0
        for joint, pm, px in by_key.values():
            w = sum(joint.values())
            norm = lambda d: [v / w for v in d.values()]  # noqa: E731
            out += w / total * (_entropy(norm(pm)) + _entropy(norm(px)) - _entropy(norm(joint)))
        return max(0.0, out)
    joint, pm, px = defaultdict(float), defaultdict(float), defaultdict(float)
    for p, label in zip(prob, tree.term_labels):
        if p == 0:
            continue
        m, x = label[which], label[2]
        if phi is not None:
            x = phi(x)
        joint[(m, x)] += p
        pm[m] += p
        px[x] += p
    total = sum(joint.values())
    norm = lambda d: [v / total for v in d.values()]  # noqa: E731
    return max(0.0, _entropy(norm(pm)) + _entropy(norm(px)) - _entropy(norm(joint)))


class LeakageIndex:
    """Fast exact I(M; X) from team realization plans, for logging during training (Milestone 8).

    Same quantity as ``mutual_information(tree, strategy, channel="all")`` with the
    default uniform adversary, but takes the two teammates' realization plans
    directly and aggregates with precomputed integer codes, so it can be called
    every few iterations. ``tests/test_leakage_index.py`` checks the two agree.
    """

    def __init__(self, tree):
        if tree.term_labels is None:
            raise ValueError("build the tree with label_fn=leakage_labels")
        ms, xs = {}, {}
        self.m = np.array([ms.setdefault(lab[0], len(ms)) for lab in tree.term_labels])
        self.x = np.array([xs.setdefault(lab[2], len(xs)) for lab in tree.term_labels])
        self.nm, self.nx = len(ms), len(xs)
        adv = tree.players[tree.adversary]
        y = realization_plan(adv, uniform_policy(adv))
        self.base = tree.term_chance * y[tree.term_seq[:, tree.adversary]]
        self.s0, self.s1 = (tree.term_seq[:, p] for p in tree.team)

    def mi(self, r0, r1):
        prob = self.base * r0[self.s0] * r1[self.s1]
        joint = np.bincount(self.m * self.nx + self.x, weights=prob,
                            minlength=self.nm * self.nx).reshape(self.nm, self.nx)
        joint = joint / joint.sum()
        pm, px = joint.sum(1), joint.sum(0)
        return max(0.0, _entropy(pm) + _entropy(px) - _entropy(joint.ravel()))
