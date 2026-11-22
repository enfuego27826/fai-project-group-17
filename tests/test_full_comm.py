"""V_Com: the full-communication value from the merged-team game (games.merged)."""

import pyspiel
import pytest

from games.merged import MergedTeamGame
from games.tree import build_tree
from eval.perfect_recall import has_perfect_recall
from solvers.zero_sum_lp import solve_zero_sum

KUHN = "kuhn_poker(players=3)"


def v_com(base, team=(0, 1), adversary=2):
    tree = build_tree(MergedTeamGame(base, team, adversary), team=(0,), adversary=1)
    assert has_perfect_recall(tree)
    return solve_zero_sum(tree).value


def test_zero_sum_lp_on_two_player_kuhn():
    """The sequence-form LP gives the known value -1/18 of 2-player Kuhn for player 0."""
    tree = build_tree(pyspiel.load_game("kuhn_poker"), team=(0,), adversary=1)
    assert solve_zero_sum(tree).value == pytest.approx(-1 / 18, abs=1e-9)


def test_merged_team_utility_is_sum_of_teammates():
    game = MergedTeamGame(KUHN)
    tree = build_tree(game, team=(0,), adversary=1)
    base = build_tree(pyspiel.load_game(KUHN))
    assert sorted(tree.term_u) == pytest.approx(
        sorted(base.term_returns[:, 0] + base.term_returns[:, 1]))


def test_card_guessing_v_com_is_one():
    """With full communication the guesser always knows the card."""
    assert v_com("card_guessing(num_cards=4)") == pytest.approx(1.0)


def test_kuhn_v_com_default_seating():
    """Proposition 1(3): 2 bits identify a card among 4, so V_Com = V(2, inf, priv) = 0.

    V(2, inf, priv) = 0 is computed (slowly) in test_sanity.py, which also
    compares it against V_Com directly.
    """
    assert v_com(KUHN) == pytest.approx(0.0, abs=1e-9)
