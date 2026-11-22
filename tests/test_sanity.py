"""Sanity checks on 3-player Kuhn poker (team {0, 1}, adversary 2).

Values are computed once per module. Instances with k >= 1 use MILP pricing
and take tens of seconds each, so they are marked slow (about 2 minutes total).
"""

import pytest

import games  # noqa: F401
from games.augment import make_augmented_game
from games.tree import build_tree
from eval.best_response import guaranteed_value
from solvers.tmecor_cg import solve_tmecor

KUHN = "kuhn_poker(players=3)"
TOL = 1e-7


@pytest.fixture(scope="module")
def kuhn_values():
    cache = {}

    def get(k, rho):
        if (k, rho) not in cache:
            tree = build_tree(make_augmented_game(KUHN, k=k, s="inf", rho=rho,
                                                  team=(0, 1), adversary=2))
            res = solve_tmecor(tree)
            cache[(k, rho)] = (res, tree)
        return cache[(k, rho)]

    return get


def _check_ks(kuhn_values, ks):
    for rho in ("priv", "pub"):
        values = [kuhn_values(k, rho)[0].value for k in ks]
        for lo, hi in zip(values, values[1:]):
            assert lo <= hi + TOL, f"V not nondecreasing in k for rho={rho}: {values}"
    for k in ks:
        assert kuhn_values(k, "pub")[0].value <= kuhn_values(k, "priv")[0].value + TOL
        for rho in ("priv", "pub"):
            res, tree = kuhn_values(k, rho)
            assert res.converged
            assert abs(res.value - guaranteed_value(tree, res.support)) <= 1e-6


@pytest.mark.slow
def test_kuhn_monotone_k01(kuhn_values):
    """Proposition 1(1) on Kuhn for k in {0, 1}; exploitability of solutions ~ 0."""
    _check_ks(kuhn_values, [0, 1])


@pytest.mark.slow
def test_kuhn_monotone_k2_priv(kuhn_values):
    """V(2, inf, priv) >= V(1, inf, priv), certified.

    k = 2 with rho = pub is left out: its MILP pricing does not certify
    optimality within 20 minutes on a laptop (see results/m1_values). Its
    value 0 follows from the solver's lower bound and Proposition 2.
    """
    _check_ks(kuhn_values, [0, 1])
    res, tree = kuhn_values(2, "priv")
    assert res.converged
    assert res.value >= kuhn_values(1, "priv")[0].value - TOL
    assert abs(res.value - guaranteed_value(tree, res.support)) <= 1e-6


@pytest.mark.slow
def test_kuhn_v_com_equals_k2_priv_and_k1(kuhn_values):
    """Proposition 1(3): V_Com = V(2, inf, priv); and V(1, inf, priv) already reaches it (k* = 1)."""
    from games.merged import MergedTeamGame
    from solvers.zero_sum_lp import solve_zero_sum

    merged = build_tree(MergedTeamGame(KUHN, (0, 1), 2), team=(0,), adversary=1)
    v_com = solve_zero_sum(merged).value
    assert abs(kuhn_values(2, "priv")[0].value - v_com) <= TOL
    assert abs(kuhn_values(1, "priv")[0].value - v_com) <= TOL
    assert kuhn_values(0, "priv")[0].value < v_com - 1e-3
