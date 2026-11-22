"""Card guessing with a blocker (games.card_blocker) and its values at s = infinity."""

import pyspiel
import pytest

import games  # noqa: F401
from games.augment import make_augmented_game
from games.tree import build_tree
from eval.best_response import guaranteed_value
from eval.perfect_recall import has_perfect_recall
from solvers.tmecor_cg import solve_tmecor


def play(actions, **params):
    state = pyspiel.load_game("card_blocker", {"num_cards": 4, **params}).new_initial_state()
    for a in actions:
        state.apply_action(a)
    return state


def test_order_and_payoffs():
    state = play([2])
    assert state.current_player() == 2          # adversary blocks before the guess
    state.apply_action(0)
    assert state.current_player() == 1
    state.apply_action(2)
    assert state.returns() == [0.5, 0.5, -1.0]  # g = X, b != X
    assert play([2, 2, 2]).returns() == [0.0, 0.0, 0.0]  # true card blocked
    assert play([2, 0, 1]).returns() == [0.0, 0.0, 0.0]  # wrong guess


def test_information_states():
    state = play([3, 1])
    assert state.information_state_string(0) == "card:3"
    assert state.information_state_string(1) == ""        # does not see the block
    assert state.information_state_string(2) == ""
    seen = play([3, 1], guesser_sees_block=True)
    assert seen.information_state_string(1) == "block:1"


@pytest.mark.parametrize("sees", [False, True])
@pytest.mark.parametrize("s", [0, 1, "inf"])
@pytest.mark.parametrize("rho", ["priv", "pub"])
@pytest.mark.parametrize("k", [0, 1, 2])
def test_perfect_recall(k, rho, s, sees):
    game = make_augmented_game(f"card_blocker(num_cards=4,guesser_sees_block={sees})",
                               k=k, s=s, rho=rho)
    assert has_perfect_recall(build_tree(game))


def blocker_value(n, k, rho):
    tree = build_tree(make_augmented_game(f"card_blocker(num_cards={n})", k=k, s="inf", rho=rho))
    res = solve_tmecor(tree)
    assert res.converged
    assert abs(res.value - guaranteed_value(tree, res.support)) <= 1e-6
    return res.value


@pytest.mark.parametrize("rho", ["priv", "pub"])
@pytest.mark.parametrize("k,expected", [(0, 3 / 16), (1, 3 / 8), (2, 3 / 4)])
def test_values_n4(k, expected, rho):
    """Hand-derived V(k, inf, priv) for n = 4; pub equals priv at s = inf (Proposition 2)."""
    assert blocker_value(4, k, rho) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("k", [0, 1, 2, 3])
def test_values_n8_formula(k):
    """V(k, inf, priv) = (1 - 1/n) 2^k / n for 2^k <= n."""
    assert blocker_value(8, k, "priv") == pytest.approx((1 - 1 / 8) * 2 ** k / 8, abs=1e-9)
