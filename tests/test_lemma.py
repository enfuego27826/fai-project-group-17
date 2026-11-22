"""Public-channel cap (Lemma 1 of report/main.tex): V(k, s, pub) <= 1/4 at s = 0 and 1 - 2^-s at s >= 1.

Checked against every value recorded in the committed result summaries of
Milestones 2 and 2.5 (exact values and lower bounds must respect it; upper
bounds may be looser), and against fresh solver values on small instances.
"""

import re
from pathlib import Path

import pytest

import games  # noqa: F401
from games.augment import make_augmented_game
from games.tree import build_tree
from solvers.backends import resolve_backend
from solvers.finite_s import solve_bilinear, solve_key_pure

ROOT = Path(__file__).resolve().parents[1]
GAMES = ("blocker4", "blocker8", "attack2x2", "attack3x3")


def cap(s):
    return 0.25 if s == 0 else 1 - 2.0 ** -s


def recorded_public_cells():
    """(source, game, k, s, lower) for finite-s public cells in the committed summaries."""
    cells = []
    for summary in sorted(ROOT.glob("results/m2*_values/*/0/summary.md")):
        for line in summary.read_text().splitlines():
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) < 5 or parts[0] not in GAMES or parts[3] != "pub" or parts[2] == "inf":
                continue
            lower = float(re.findall(r"[-+]?\d*\.\d+", parts[4])[0])
            cells.append((summary.parent.parent.name, parts[0], int(parts[1]), int(parts[2]), lower))
    return cells


def test_summaries_exist():
    assert len(recorded_public_cells()) >= 30


@pytest.mark.parametrize("cell", recorded_public_cells(), ids=lambda c: f"{c[1]}-k{c[2]}-s{c[3]}")
def test_recorded_values_respect_cap(cell):
    _, _, _, s, lower = cell
    assert lower <= cap(s) + 1e-7


@pytest.mark.skipif(resolve_backend("auto") != "gurobi", reason="bilinear solver needs Gurobi")
@pytest.mark.parametrize("base,k,s", [("card_blocker(num_cards=4)", 2, 2),
                                      ("card_blocker(num_cards=3)", 1, 2),
                                      ("coordinated_attack(rows=2,cols=2)", 1, 2),
                                      ("coordinated_attack(rows=2,cols=3)", 1, 2)])
def test_fresh_values_respect_cap(base, k, s):
    tree = build_tree(make_augmented_game(base, k=k, s=s, rho="pub"))
    L = solve_key_pure(tree, time_limit=30)
    res = solve_bilinear(tree, time_limit=20)
    assert max(L.value, res.value) <= cap(s) + 1e-7
    if res.optimal:
        assert res.bound <= cap(s) + 1e-7
