"""Tests for exact evaluation: best response, g(pi_T), exploitability inputs, leakage."""

import math

import numpy as np
import pyspiel
import pytest
from open_spiel.python import policy as os_policy
from open_spiel.python.algorithms import best_response as os_br

import games  # noqa: F401
from games.augment import make_augmented_game
from games.tree import build_tree
from eval.best_response import adversary_best_response, expected_team_utility
from eval.leakage import leakage_labels, mutual_information
from eval.sequence_form import realization_plan, uniform_policy


def _random_tabular(game, seed):
    pol = os_policy.TabularPolicy(game)
    rng = np.random.default_rng(seed)
    probs = rng.random(pol.action_probability_array.shape) * pol.legal_actions_mask
    pol.action_probability_array = probs / probs.sum(axis=1, keepdims=True)
    return pol


def _to_dict(tab, tree, player):
    out = {}
    for key, acts in zip(tree.players[player].infoset_keys, tree.players[player].infoset_actions):
        row = tab.action_probability_array[tab.state_lookup[key]]
        out[key] = {a: float(row[a]) for a in acts}
    return out


@pytest.mark.parametrize("game_string,seed", [
    ("kuhn_poker(players=3)", 0),
    ("kuhn_poker(players=3)", 1),
    ("augmented", 2),
])
def test_adversary_br_matches_openspiel(game_string, seed):
    if game_string == "augmented":
        game = make_augmented_game("kuhn_poker(players=3)", k=1, s=1, rho="pub")
    else:
        game = pyspiel.load_game(game_string)
    tree = build_tree(game)
    tab = _random_tabular(game, seed)
    team = [(1.0, {p: _to_dict(tab, tree, p) for p in (0, 1)})]
    ours = adversary_best_response(tree, team)

    br = os_br.BestResponsePolicy(game, 2, tab)
    theirs = br.value(game.new_initial_state())  # adversary's expected return
    assert ours.value == pytest.approx(-theirs, abs=1e-10)
    # The returned adversary plan attains g(pi_T).
    assert expected_team_utility(tree, team, ours.policy) == pytest.approx(ours.value, abs=1e-10)


def test_expected_utility_matches_openspiel():
    from open_spiel.python.algorithms import expected_game_score
    game = pyspiel.load_game("kuhn_poker(players=3)")
    tree = build_tree(game)
    tab = _random_tabular(game, 7)
    team = [(1.0, {p: _to_dict(tab, tree, p) for p in (0, 1)})]
    ours = expected_team_utility(tree, team, _to_dict(tab, tree, 2))
    vals = expected_game_score.policy_value(game.new_initial_state(), [tab] * 3)
    assert ours == pytest.approx(-vals[2], abs=1e-10)


def test_mixture_of_profiles_is_linear():
    game = pyspiel.load_game("kuhn_poker(players=3)")
    tree = build_tree(game)
    a = {p: _to_dict(_random_tabular(game, 3), tree, p) for p in (0, 1)}
    b = {p: _to_dict(_random_tabular(game, 4), tree, p) for p in (0, 1)}
    adv = uniform_policy(tree.players[2])
    mix = expected_team_utility(tree, [(0.3, a), (0.7, b)], adv)
    assert mix == pytest.approx(0.3 * expected_team_utility(tree, [(1, a)], adv)
                                + 0.7 * expected_team_utility(tree, [(1, b)], adv))


def test_realization_plan_rejects_missing_reachable_infoset():
    tree = build_tree(pyspiel.load_game("kuhn_poker(players=3)"))
    with pytest.raises(KeyError):
        realization_plan(tree.players[0], {})


def _card_tree(k, rho="pub", s="inf"):
    game = make_augmented_game("card_guessing(num_cards=4)", k=k, s=s, rho=rho)
    return build_tree(game, label_fn=leakage_labels)


def _card_identity_code(tree, k):
    """Teammate 0 sends its card (mod 2^k); teammate 1 sends 0 and guesses accordingly."""
    p0 = {key: int(key.split("card:")[1].split("|")[0]) % 2 ** k
          for key in tree.players[0].infoset_keys}
    p1 = {}
    for key, acts in zip(tree.players[1].infoset_keys, tree.players[1].infoset_actions):
        if key.endswith("?"):
            p1[key] = 0
        else:
            m0 = int(key.split(":")[-1].split(",")[0], 2)
            p1[key] = m0
    return [(1.0, {0: p0, 1: p1})]


def test_leakage_identity_code():
    tree = _card_tree(k=2)
    team = _card_identity_code(tree, 2)
    assert mutual_information(tree, team) == pytest.approx(2.0)
    assert adversary_best_response(tree, team).value == pytest.approx(1.0)
    tree1 = _card_tree(k=1)
    assert mutual_information(tree1, _card_identity_code(tree1, 1)) == pytest.approx(1.0)


def test_leakage_zero_for_uniform_messages_and_k0():
    tree = _card_tree(k=2)
    team = [(1.0, {p: uniform_policy(tree.players[p]) for p in (0, 1)})]
    assert mutual_information(tree, team) == pytest.approx(0.0, abs=1e-12)
    tree0 = _card_tree(k=0)
    team0 = [(1.0, {1: uniform_policy(tree0.players[1]), 0: {}})]
    assert mutual_information(tree0, team0) == pytest.approx(0.0, abs=1e-12)


def test_leakage_channel_priv_is_zero():
    tree = _card_tree(k=2, rho="priv")
    team = _card_identity_code(tree, 2)
    assert mutual_information(tree, team, channel="adversary") == 0.0
    assert mutual_information(tree, team, channel="all") == pytest.approx(2.0)


def test_one_time_pad_hides_messages():
    """Teammate 0 sends card XOR key (s = k = 2): M is independent of X, value stays 1."""
    game = make_augmented_game("card_guessing(num_cards=4)", k=2, s=2, rho="pub")
    tree = build_tree(game, label_fn=leakage_labels)
    p0 = {}
    for key in tree.players[0].infoset_keys:
        card = int(key.split("card:")[1].split("|")[0])
        k_bits = int(key.split("key=")[1].split("|")[0], 2)
        p0[key] = card ^ k_bits
    p1 = {}
    for key in tree.players[1].infoset_keys:
        if key.endswith("?"):
            p1[key] = 0
        else:
            k_bits = int(key.split("key=")[1].split("|")[0], 2)
            p1[key] = int(key.split(":")[-1].split(",")[0], 2) ^ k_bits
    team = [(1.0, {0: p0, 1: p1})]
    assert mutual_information(tree, team) == pytest.approx(0.0, abs=1e-12)
    assert adversary_best_response(tree, team).value == pytest.approx(1.0)
    assert math.isclose(tree.term_chance.sum(), 64.0)  # 16 message pairs x 4 guesses
