"""Finite key length: the lower bound L(k, s, rho) and the exact bilinear solver.

L is the best key-indexed joint pure team plan (no private randomization),
so it may be strictly below V(k, s, rho). U(k, s, rho) = V(k, inf, rho).
"""

import itertools

import pytest

import games  # noqa: F401
from games.augment import make_augmented_game
from games.tree import build_tree
from eval.best_response import guaranteed_value
from solvers.backends import resolve_backend
from solvers.finite_s import solve_bilinear, solve_key_pure
from solvers.tmecor_cg import solve_tmecor

BLOCKER = "card_blocker(num_cards=4)"
KS, SS, RHOS = (0, 1, 2), (0, 1, 2), ("priv", "pub")
TOL = 1e-9
needs_gurobi = pytest.mark.skipif(resolve_backend("auto") != "gurobi",
                                  reason="bilinear solver needs Gurobi")


def tree_of(k, s, rho, base=BLOCKER):
    return build_tree(make_augmented_game(base, k=k, s=s, rho=rho))


@pytest.fixture(scope="module")
def blocker_L():
    return {(k, s, rho): solve_key_pure(tree_of(k, s, rho))
            for k, s, rho in itertools.product(KS, SS, RHOS)}


@pytest.fixture(scope="module")
def blocker_U():
    return {(k, rho): solve_tmecor(tree_of(k, "inf", rho)).value
            for k, rho in itertools.product(KS, RHOS)}


def test_L_is_optimal_and_attained(blocker_L):
    for (k, s, rho), res in blocker_L.items():
        assert res.optimal
        g = guaranteed_value(tree_of(k, s, rho), [(1.0, res.profile)])
        assert g == pytest.approx(res.value, abs=1e-9)


def test_L_below_U(blocker_L, blocker_U):
    for (k, s, rho), res in blocker_L.items():
        assert res.value <= blocker_U[(k, rho)] + TOL


def test_L_monotone(blocker_L):
    for k, s, rho in itertools.product(KS, SS, RHOS):
        L = blocker_L[(k, s, rho)].value
        if s + 1 in SS:
            assert L <= blocker_L[(k, s + 1, rho)].value + TOL
        if k + 1 in KS:
            assert L <= blocker_L[(k + 1, s, rho)].value + TOL
        if rho == "pub":
            assert L <= blocker_L[(k, s, "priv")].value + TOL


def test_L_known_cells(blocker_L):
    """No key and no private randomization: a pure guess is always blocked."""
    assert blocker_L[(0, 0, "priv")].value == pytest.approx(0.0)
    assert blocker_L[(1, 0, "pub")].value == pytest.approx(0.0)
    # Two key bits are enough to reach V(1, inf) = 3/8 with pure plans.
    assert blocker_L[(1, 2, "pub")].value == pytest.approx(3 / 8)


def test_L_milp_matches_enumeration():
    for k, s, rho in [(1, 0, "pub"), (1, 1, "pub"), (0, 2, "priv"), (2, 0, "priv")]:
        tree = tree_of(k, s, rho)
        a = solve_key_pure(tree)
        b = solve_key_pure(tree, enum_limit=0)
        assert a.method == "enumerate" and b.method == "milp"
        assert a.value == pytest.approx(b.value, abs=1e-9)


@needs_gurobi
@pytest.mark.parametrize("k,s,rho,expected", [
    (0, 0, "priv", 3 / 16), (0, 0, "pub", 3 / 16),
    (1, 0, "priv", 3 / 8), (1, 0, "pub", 1 / 4),
    (1, 1, "pub", 3 / 8), (2, 2, "pub", 3 / 4),
])
def test_bilinear_exact_blocker(k, s, rho, expected):
    """Exact V(k, s, rho) with private randomization. V(1, 0, pub) = 1/4 is the hand-derived value."""
    tree = tree_of(k, s, rho)
    res = solve_bilinear(tree, time_limit=60)
    assert res.optimal
    assert res.value == pytest.approx(expected, abs=1e-6)
    assert res.bound == pytest.approx(expected, abs=1e-6)
    assert res.value >= solve_key_pure(tree).value - 1e-7  # V >= L


@needs_gurobi
def test_bilinear_time_limit_gives_valid_bounds():
    """V(2, 0, pub) = 1/4 (Lemma 1 of report/main.tex); a short solve brackets it."""
    res = solve_bilinear(tree_of(2, 0, "pub"), time_limit=2)
    assert res.value <= 0.25 + 1e-7 <= res.bound + 2e-7


def test_kuhn_one_key_bit_reaches_tmecor():
    """L(0, 1, .) on Kuhn equals V_Cor = -1/24: two equally likely joint pure plans suffice."""
    res = solve_key_pure(tree_of(0, 1, "priv", base="kuhn_poker(players=3)"), time_limit=120)
    assert res.optimal and res.value == pytest.approx(-1 / 24, abs=1e-9)


@pytest.mark.slow
@needs_gurobi
@pytest.mark.parametrize("n,k,s", [(3, 1, 0), (4, 1, 0), (5, 2, 0), (4, 1, 1), (3, 1, 1)])
def test_claim1_public_blocker_bound(n, k, s):
    """Claim 1 (implied by Lemma 1 of report/main.tex): V(k, s, pub) <= 2^s / 4 on the blocker game, any n, k."""
    tree = tree_of(k, s, "pub", base=f"card_blocker(num_cards={n})")
    res = solve_bilinear(tree, time_limit=30)
    assert res.value <= 2 ** s / 4 + 1e-7
    if res.optimal:
        assert res.bound <= 2 ** s / 4 + 1e-7


def test_claim1_holds_for_L(blocker_L):
    for (k, s, rho), res in blocker_L.items():
        if rho == "pub":
            assert res.value <= 2 ** s / 4 + 1e-9
