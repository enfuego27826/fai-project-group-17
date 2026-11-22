"""Team Liar's Dice (games.team_liars_dice): rules, payoffs and the augmented game."""

import numpy as np
import pyspiel
import pytest

import games  # noqa: F401
from games.augment import make_augmented_game
from games.merged import MergedTeamGame
from games.tree import build_tree
from eval.perfect_recall import has_perfect_recall
from solvers.zero_sum_lp import solve_zero_sum

GAME = "team_liars_dice"
LIAR = 9  # 3 dice x 3 faces


def rolled(dice=(1, 2, 3), **params):
    """State after the roll; dice are faces 1..F for players 0, 1, 2."""
    state = pyspiel.load_game(GAME, params).new_initial_state()
    for d in dice:
        state.apply_action(d - 1)
    return state


def bid(q, f, faces=3):
    return (q - 1) * faces + (f - 1)


def test_bid_ordering_and_legal_actions():
    state = rolled()
    assert state.current_player() == 0
    assert state.legal_actions() == list(range(9))        # no "liar" before the first bid
    state.apply_action(bid(1, 3))
    assert state.current_player() == 1
    assert state.legal_actions() == list(range(bid(2, 1), 9)) + [LIAR]  # strictly higher
    state.apply_action(bid(3, 3))                         # highest bid
    assert state.legal_actions() == [LIAR]                # forced call
    assert state.current_player() == 2


@pytest.mark.parametrize("dice,bids,expected", [
    # Bid holds: the caller loses. Adversary (2) calls a true bid of teammate 1.
    ((2, 2, 1), [bid(1, 1), bid(2, 2)], [0.5, 0.5, -1.0]),
    # Bid fails: the bidder loses. Adversary calls teammate 1's false bid.
    ((1, 2, 3), [bid(1, 1), bid(2, 2)], [0.0, -1.0, 1.0]),
    # Teammate 0 calls the adversary's false bid.
    ((1, 2, 3), [bid(1, 1), bid(1, 2), bid(2, 3)], [0.5, 0.5, -1.0]),
    # Teammate 1 calls teammate 0's true bid: the team loses either way.
    ((3, 3, 3), [bid(3, 3)], [0.0, -1.0, 1.0]),
])
def test_payoffs(dice, bids, expected):
    state = rolled(dice)
    for a in bids:
        state.apply_action(a)
    state.apply_action(LIAR)
    assert state.is_terminal()
    assert state.returns() == expected
    assert sum(state.returns()) == 0.0


def test_information_states():
    state = rolled((3, 1, 2))
    assert state.information_state_string(0) == "dice:3|bids:"
    assert state.information_state_string(1) == "dice:1|bids:"
    state.apply_action(bid(1, 2))
    assert state.information_state_string(2) == "dice:2|bids:1"


def test_wild_ones():
    state = rolled((1, 1, 3), wild=True)
    assert state.count(3) == 3 and state.count(1) == 2
    assert rolled((1, 1, 3)).count(3) == 1


def test_adversary_seat_changes_payoff_split():
    state = rolled((1, 2, 3), adversary=0)
    state.apply_action(bid(2, 1))     # player 0 (adversary) bids a false bid
    state.apply_action(LIAR)          # player 1 calls
    assert state.returns() == [-1.0, 0.5, 0.5]


def test_tree_zero_sum_and_team_utility():
    tree = build_tree(pyspiel.load_game(GAME))
    assert tree.num_terminals == 27 * 511
    assert np.abs(tree.term_returns.sum(axis=1)).max() == 0.0
    assert set(tree.term_u) == {-1.0, 1.0}
    assert np.allclose(tree.term_u, tree.term_returns[:, 0] + tree.term_returns[:, 1])


@pytest.mark.parametrize("k,s,rho", [(0, 0, "priv"), (1, "inf", "priv"), (1, "inf", "pub"),
                                     (1, 1, "pub"), (2, "inf", "pub")])
def test_perfect_recall_augmented(k, s, rho):
    tree = build_tree(make_augmented_game(GAME, k=k, s=s, rho=rho))
    assert has_perfect_recall(tree)
    # Each teammate: one message information set per die value (3), and every base
    # decision information set split by the 4^k message pairs; times 2^s key values.
    base = build_tree(pyspiel.load_game(GAME))
    keys = 2 ** s if s != "inf" else 1
    for p in (0, 1):
        expected = base.num_infosets(p) if k == 0 else 3 + 4 ** k * base.num_infosets(p)
        assert tree.num_infosets(p) == keys * expected
    assert tree.num_infosets(2) == base.num_infosets(2) * (4 ** k if rho == "pub" else 1)


def test_v_com():
    tree = build_tree(MergedTeamGame(GAME), team=(0,), adversary=1)
    assert solve_zero_sum(tree).value == pytest.approx(1 / 9, abs=1e-9)


@pytest.mark.slow
def test_v0_equals_v_com():
    """Kill-criterion result: V(0, inf) = V_Com = 1/9 (D = 1, F = 3), so V(k, inf, .) = 1/9 for all k.

    The column generation is stopped once its master value reaches V_Com
    (``known_upper``); the returned correlation device must guarantee 1/9.
    """
    from eval.best_response import guaranteed_value
    from solvers.tmecor_cg import solve_tmecor

    v_com = solve_zero_sum(build_tree(MergedTeamGame(GAME), team=(0,), adversary=1)).value
    tree = build_tree(make_augmented_game(GAME, k=0, s="inf", rho="priv"))
    res = solve_tmecor(tree, known_upper=v_com)
    assert res.reached_known_upper
    assert guaranteed_value(tree, res.support) == pytest.approx(v_com, abs=1e-9)
