"""Tests for the LP backends, sequence form helpers and the TMECor solvers."""

import numpy as np
import pyspiel
import pytest

import games  # noqa: F401
from games.augment import make_augmented_game
from games.tree import build_tree
from eval.best_response import guaranteed_value
from eval.sequence_form import realization_plan
from solvers.backends import resolve_backend, solve
from solvers.seqform import (count_reduced_plans, enumerate_reduced_plans,
                             plan_from_realization, sequence_form_constraints)
from solvers.tmecor_cg import solve_tmecor
from solvers.tmecor_enum import solve_tmecor_enum

BACKENDS = ["highs"] + (["gurobi"] if resolve_backend("auto") == "gurobi" else [])


@pytest.mark.parametrize("backend", BACKENDS)
def test_dual_convention(backend):
    """dual = d(objective)/d(rhs), checked by finite differences."""
    A, b = np.array([[1.0, 2.0], [3.0, 1.0]]), np.array([4.0, 6.0])
    base = solve([1, 1], A_ub=A, b_ub=b, maximize=True, backend=backend)
    for i in range(2):
        bumped = solve([1, 1], A_ub=A, b_ub=b + 1e-4 * np.eye(2)[i], maximize=True,
                       backend=backend)
        assert base.dual_ub[i] == pytest.approx((bumped.obj - base.obj) / 1e-4, abs=1e-6)


def test_reduced_plans_of_kuhn():
    tree = build_tree(pyspiel.load_game("kuhn_poker(players=3)"))
    assert count_reduced_plans(tree.players[0]) == 9 ** 4  # bet, or check + 3 binary replies
    X = enumerate_reduced_plans(tree.players[0], 10 ** 4)
    F, f = sequence_form_constraints(tree.players[0])
    assert X.shape == (6561, 33)
    assert np.abs(X @ F.T - f).max() == 0
    assert len({row.tobytes() for row in X}) == 6561
    # Round trip: realization -> pure plan -> realization.
    plan = plan_from_realization(tree.players[0], X[123])
    assert np.array_equal(realization_plan(tree.players[0], plan), X[123])


def _aug_tree(base, k, rho):
    return build_tree(make_augmented_game(base, k=k, s="inf", rho=rho))


@pytest.mark.parametrize("rho", ["priv", "pub"])
@pytest.mark.parametrize("k,expected", [(0, 0.25), (1, 0.5), (2, 1.0)])
def test_card_guessing_values(k, expected, rho):
    """Example 1: V(0) = 1/4, V(1) = 1/2, V(2) = 1 with n = 4 cards, one round."""
    tree = _aug_tree("card_guessing(num_cards=4)", k, rho)
    res = solve_tmecor(tree)
    assert res.value == pytest.approx(expected, abs=1e-9)
    assert abs(res.value - guaranteed_value(tree, res.support)) <= 1e-6


@pytest.mark.parametrize("game", ["card_guessing(num_cards=4)", "kuhn_poker(players=3)"])
@pytest.mark.parametrize("rho", ["priv", "pub"])
def test_v0_equals_independent_tmecor(game, rho):
    """Proposition 1(2): V(0, inf, rho) = V_Cor of the base game, by two different solvers."""
    cg = solve_tmecor(_aug_tree(game, 0, rho))
    enum = solve_tmecor_enum(build_tree(pyspiel.load_game(game)))
    assert cg.value == pytest.approx(enum.value, abs=1e-8)


@pytest.mark.parametrize("backend", BACKENDS)
def test_backends_agree_on_kuhn_k0(backend):
    res = solve_tmecor(_aug_tree("kuhn_poker(players=3)", 0, "priv"), backend=backend)
    assert res.value == pytest.approx(-1 / 24, abs=1e-8)


def test_solver_output_has_zero_exploitability_kuhn_k0():
    tree = _aug_tree("kuhn_poker(players=3)", 0, "pub")
    res = solve_tmecor(tree)
    assert abs(res.value - guaranteed_value(tree, res.support)) <= 1e-6
    assert sum(w for w, _ in res.support) == pytest.approx(1.0)


def test_milp_pricing_matches_enumeration():
    """Force MILP pricing on a game where enumeration also works."""
    tree = _aug_tree("card_guessing(num_cards=4)", 1, "priv")
    a = solve_tmecor(tree, enum_limit=10 ** 6)
    b = solve_tmecor(tree, enum_limit=0)
    assert a.pricing == "enumerate" and b.pricing == "milp"
    assert a.value == pytest.approx(b.value, abs=1e-9)
    tree = _aug_tree("kuhn_poker(players=3)", 0, "priv")
    res = solve_tmecor(tree, enum_limit=0)
    assert res.converged and res.upper_bound == pytest.approx(res.value, abs=1e-8)
    assert res.value == pytest.approx(-1 / 24, abs=1e-8)


def test_time_limited_pricing_gives_valid_bounds():
    """With a tiny MILP time limit the solver returns lower <= V <= upper."""
    tree = _aug_tree("kuhn_poker(players=3)", 0, "priv")
    res = solve_tmecor(tree, enum_limit=0, pricing_time_limit=0.01)
    v = -1 / 24
    assert res.value <= v + 1e-8 and res.upper_bound >= v - 1e-8
    assert guaranteed_value(tree, res.support) == pytest.approx(res.value, abs=1e-6)
    if res.converged:
        assert res.value == pytest.approx(v, abs=1e-8)


# Guaranteed team utilities of an approximate TMECor strategy for 3-player Kuhn
# with 4 ranks (K4), opponent in seat 1, 2, 3 (1-indexed): Farina, Celli, Gatti
# and Sandholm (NeurIPS 2018), supplementary Table 4. They are lower bounds on
# the TMECor value. Zhang, Farina and Sandholm (ICML 2023), Table 1, row
# "3K4 {3}" (312 leaves): team value -0.042 with the opponent in seat 3.
FARINA18_TABLE4_K4 = {0: 0.0369, 1: 0.0215, 2: -0.0474}


@pytest.mark.parametrize("adversary,expected", [(0, 5 / 132), (1, 7 / 264), (2, -1 / 24)])
def test_kuhn_tmecor_all_seatings(adversary, expected):
    """V_Cor of 3-player Kuhn for every adversary seat, against published values."""
    team = tuple(p for p in range(3) if p != adversary)
    tree = build_tree(pyspiel.load_game("kuhn_poker(players=3)"), team=team, adversary=adversary)
    # Team utility is the sum of the two teammates' returns.
    assert np.allclose(tree.term_u, tree.term_returns[:, list(team)].sum(axis=1))
    value = solve_tmecor_enum(tree).value
    assert value == pytest.approx(expected, abs=1e-8)
    assert value >= FARINA18_TABLE4_K4[adversary]
    if adversary == 2:
        assert tree.num_terminals == 312 and round(value, 3) == -0.042


def test_known_upper_stops_early():
    """Column generation stops once the master reaches an externally proved upper bound."""
    tree = _aug_tree("card_guessing(num_cards=4)", 1, "priv")
    res = solve_tmecor(tree, known_upper=0.5)
    assert res.reached_known_upper and not res.converged
    assert res.value == pytest.approx(0.5) and res.upper_bound == 0.5
    assert solve_tmecor(tree).reached_known_upper is False
