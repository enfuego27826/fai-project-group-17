"""Coordinated attack (games.coordinated_attack): rules and exact values on the 2 x 2 grid.

Note on V(0, inf). The milestone prompt's hand-derived value was 3/16. The
solver gives 3/8, and the strategy is checked here directly: the correlation
device picks the diagonal or the anti-diagonal; teammate 0 with row i attacks
the target of row i on it, teammate 1 with column j attacks the target of
column j on it. They coordinate whenever (i, j) lies on the chosen line
(probability 1/2), and the attacked target is uniform, so the defender stops
it with probability 1/4: 1/2 * 3/4 = 3/8. Reported in results/m25_values.
"""

import pyspiel
import pytest

import games  # noqa: F401
from games.augment import make_augmented_game
from games.merged import MergedTeamGame
from games.tree import build_tree
from eval.best_response import guaranteed_value
from eval.perfect_recall import has_perfect_recall
from solvers.backends import resolve_backend
from solvers.finite_s import solve_bilinear
from solvers.tmecor_cg import solve_tmecor
from solvers.zero_sum_lp import solve_zero_sum

needs_gurobi = pytest.mark.skipif(resolve_backend("auto") != "gurobi",
                                  reason="bilinear solver needs Gurobi")


def play(actions, rows=2, cols=2):
    state = pyspiel.load_game("coordinated_attack", {"rows": rows, "cols": cols}).new_initial_state()
    for a in actions:
        state.apply_action(a)
    return state


def test_order_information_and_payoffs():
    state = play([3])                       # weak target (1, 1)
    assert state.current_player() == 2
    assert state.information_state_string(0) == "row:1"
    assert state.information_state_string(1) == "col:1"
    assert state.information_state_string(2) == ""
    state.apply_action(0)                   # defend (0, 0)
    assert state.current_player() == 0
    state.apply_action(3)
    assert state.current_player() == 1
    assert state.information_state_string(1) == "col:1"  # does not see the attack or defence
    state.apply_action(3)
    assert state.returns() == [0.5, 0.5, -1.0]
    assert play([3, 3, 3, 3]).returns() == [0.0, 0.0, 0.0]  # defended
    assert play([3, 0, 3, 2]).returns() == [0.0, 0.0, 0.0]  # miscoordinated
    assert play([5, 0], rows=2, cols=3).information_state_string(1) == "col:2"


@pytest.mark.parametrize("grid", [(2, 2), (3, 3)])
@pytest.mark.parametrize("s", [0, 1, "inf"])
@pytest.mark.parametrize("rho", ["priv", "pub"])
@pytest.mark.parametrize("k", [0, 1])
def test_perfect_recall(grid, s, rho, k):
    base = f"coordinated_attack(rows={grid[0]},cols={grid[1]})"
    assert has_perfect_recall(build_tree(make_augmented_game(base, k=k, s=s, rho=rho)))


def value_inf(k, rho):
    tree = build_tree(make_augmented_game("coordinated_attack", k=k, s="inf", rho=rho))
    res = solve_tmecor(tree)
    assert res.converged
    assert abs(res.value - guaranteed_value(tree, res.support)) <= 1e-6
    return res.value, tree


def test_v0_is_three_eighths_with_diagonal_strategy():
    value, tree = value_inf(0, "priv")
    assert value == pytest.approx(3 / 8, abs=1e-9)
    diag = {0: {"row:0": 0, "row:1": 3}, 1: {"col:0": 0, "col:1": 3}}
    anti = {0: {"row:0": 1, "row:1": 2}, 1: {"col:0": 2, "col:1": 1}}
    assert guaranteed_value(tree, [(0.5, diag), (0.5, anti)]) == pytest.approx(3 / 8)


def test_k1_reaches_full_communication():
    v1, _ = value_inf(1, "priv")
    merged = build_tree(MergedTeamGame("coordinated_attack"), team=(0,), adversary=1)
    v_com = solve_zero_sum(merged).value
    assert v1 == pytest.approx(3 / 4, abs=1e-9)
    assert v_com == pytest.approx(v1, abs=1e-9)
    assert value_inf(1, "pub")[0] == pytest.approx(3 / 4, abs=1e-9)  # Prop. 2


@needs_gurobi
@pytest.mark.parametrize("s,expected", [(1, 1 / 2), (2, 3 / 4)])
def test_public_values_need_two_key_bits(s, expected):
    """V(1, 1, pub) = 1/2 < V(1, 1, priv) = 3/4; with s = 2 = 2kR the gap closes."""
    tree = build_tree(make_augmented_game("coordinated_attack", k=1, s=s, rho="pub"))
    res = solve_bilinear(tree, time_limit=120)
    assert res.optimal
    assert res.value == pytest.approx(expected, abs=1e-6)


@pytest.mark.slow
@needs_gurobi
@pytest.mark.parametrize("grid,k,s", [((2, 2), 1, 0), ((2, 3), 1, 0), ((3, 3), 1, 0),
                                      ((2, 2), 1, 1), ((2, 3), 1, 1)])
def test_claim2_public_bound(grid, k, s):
    """Claim 2 (implied by Lemma 1 of report/main.tex): V(k, s, pub) <= 2^s / 4 on any grid (attained on 2 x 2)."""
    from solvers.finite_s import solve_key_pure

    base = f"coordinated_attack(rows={grid[0]},cols={grid[1]})"
    tree = build_tree(make_augmented_game(base, k=k, s=s, rho="pub"))
    L = solve_key_pure(tree, time_limit=60)
    res = solve_bilinear(tree, time_limit=10)
    cap = 2 ** s / 4
    assert L.value <= cap + 1e-9 and res.value <= cap + 1e-7
    if grid == (2, 2):
        assert max(L.value, res.value) == pytest.approx(cap, abs=1e-6)
