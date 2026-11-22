"""Strategies as sequence-form realization plans, and exact best responses.

Policy formats accepted everywhere in ``eval``:

* behavioral policy of player p: ``{information state string: {action: prob}}``
  (a list/array of probabilities aligned with the legal actions also works);
* pure plan: ``{information state string: action}``;
* team strategy: a list of ``(weight, {player: policy})`` pairs, i.e. a
  distribution mu over joint team profiles. A single behavioral profile is
  ``[(1.0, {0: pi_0, 1: pi_1})]``; the TMECor solver returns a distribution
  over joint pure plans. Information sets missing from a policy are allowed
  only if the policy never reaches them.
"""

import numpy as np


def _action_probs(info, infoset, choice):
    actions = info.infoset_actions[infoset]
    if isinstance(choice, dict):
        probs = np.array([choice.get(a, 0.0) for a in actions], dtype=np.float64)
    elif np.isscalar(choice):  # pure plan
        if choice not in actions:
            raise ValueError(f"illegal action {choice} at {info.infoset_keys[infoset]!r}")
        probs = np.array([1.0 if a == choice else 0.0 for a in actions])
    else:
        probs = np.asarray(choice, dtype=np.float64)
    if probs.shape != (len(actions),) or abs(probs.sum() - 1.0) > 1e-9 or probs.min() < -1e-12:
        raise ValueError(f"not a distribution over legal actions at {info.infoset_keys[infoset]!r}")
    return probs


def realization_plan(info, policy):
    """Sequence-form realization plan r_p(sigma) of ``policy`` for player ``info.player``.

    r_p(empty) = 1 and r_p(I, a) = r_p(parent(I)) * pi_p(a | I): the probability
    that player p's own choices are consistent with reaching sequence sigma.
    """
    r = np.zeros(info.num_seqs)
    r[0] = 1.0
    for infoset in range(info.num_infosets):  # parents come first
        parent = r[info.infoset_parent_seq[infoset]]
        key = info.infoset_keys[infoset]
        if key not in policy:
            if parent > 0:
                raise KeyError(f"policy of player {info.player} misses reachable infoset {key!r}")
            continue
        first = info.infoset_first_seq[infoset]
        r[first:first + info.infoset_num_actions[infoset]] = parent * _action_probs(
            info, infoset, policy[key])
    return r


def uniform_policy(info):
    """Uniform behavioral policy of player ``info.player`` (used as a default opponent)."""
    return {key: {a: 1.0 / len(acts) for a in acts}
            for key, acts in zip(info.infoset_keys, info.infoset_actions)}


def team_terminal_weights(tree, team_strategy):
    """w(z) = p_c(z) * sum_j mu_j prod_{i in team} r_i^j(z): team-and-chance reach of each terminal."""
    w = np.zeros(tree.num_terminals)
    for weight, profile in team_strategy:
        if weight == 0:
            continue
        reach = np.full(tree.num_terminals, float(weight))
        for p in tree.team:
            r = realization_plan(tree.players[p], profile[p])
            reach *= r[tree.term_seq[:, p]]
        w += reach
    return w * tree.term_chance


def leaf_values(tree, player, terminal_values):
    """Sum ``terminal_values`` (shape (Z,) or (Z, B)) into player's last sequences."""
    n = tree.players[player].num_seqs
    shape = (n,) + np.shape(terminal_values)[1:]
    out = np.zeros(shape)
    np.add.at(out, tree.term_seq[:, player], terminal_values)
    return out


def best_response(info, leaf, maximize):
    """Exact best response of one perfect-recall player by a bottom-up pass.

    ``leaf[sigma]`` is the value collected at histories whose last own sequence
    is sigma, already weighted by everyone else's reach (shape (S,) or (S, B)
    for B independent problems). Returns ``(value, choice)`` where ``value`` is
    the optimal total (shape () or (B,)) and ``choice[I]`` the index of the
    optimal action at information set I (shape (num_infosets,) or
    (num_infosets, B)).
    """
    vals = np.array(leaf, dtype=np.float64, copy=True)
    choice = np.zeros((info.num_infosets,) + vals.shape[1:], dtype=np.int64)
    pick = np.argmax if maximize else np.argmin
    for infoset in range(info.num_infosets - 1, -1, -1):  # children before parents
        first = info.infoset_first_seq[infoset]
        block = vals[first:first + info.infoset_num_actions[infoset]]
        best = pick(block, axis=0)
        choice[infoset] = best
        vals[info.infoset_parent_seq[infoset]] += np.take_along_axis(
            block, best[None, ...], axis=0)[0] if block.ndim > 1 else block[best]
    return vals[0], choice


def choice_to_plan(info, choice):
    """Pure plan {information state: action} from best-response action indices."""
    return {key: info.infoset_actions[i][int(choice[i])]
            for i, key in enumerate(info.infoset_keys)}
