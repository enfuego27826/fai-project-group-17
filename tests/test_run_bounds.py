"""Bound propagation and labels in scripts/run_bounds.py (Propositions 1 and 2)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import math  # noqa: E402

from run_bounds import propagate  # noqa: E402


def row(k, s, rho, lo, hi, exact=False):
    return {"k": k, "s": s, "rho": rho, "lower": lo, "upper": hi, "lower_from": "solver",
            "upper_from": "solver", "solver_exact": exact}


def test_propagation_and_labels():
    rows = [
        row(1, "inf", "priv", 0.375, 0.375, exact=True),
        row(1, "inf", "pub", 0.375, 0.375, exact=True),
        row(1, "0", "priv", 0.25, math.inf),            # only a lower bound from L
        row(1, "0", "pub", 0.0, math.inf),
        row(1, "2", "pub", 0.0, math.inf),
        row(2, "0", "pub", 0.0, 0.4),
    ]
    propagate(rows, rounds=1, hand=[{"k": 2, "s": 0, "rho": "pub", "upper": 0.25, "ref": "C1"}])
    by = {(r["k"], r["s"], r["rho"]): r for r in rows}
    # Upper bounds from s = inf (Prop. 1, monotone in s).
    assert by[(1, "0", "priv")]["upper"] == 0.375
    assert by[(1, "0", "priv")]["status"] == "bound"
    # Prop. 2 with 2kR = 2 key bits: V(1, 2, pub) >= V(1, 0, priv) >= 0.25.
    assert by[(1, "2", "pub")]["lower"] == 0.25
    # Hand bound, and the k-monotone lower bound does not exceed it.
    assert by[(2, "0", "pub")]["upper"] == 0.25
    assert by[(1, "inf", "priv")]["status"] == "exact"


def test_theorem_label_when_bounds_meet_only_via_propositions():
    rows = [row(0, "inf", "priv", 0.1875, 0.1875, exact=True),
            row(0, "1", "priv", 0.1875, math.inf)]
    propagate(rows, rounds=1, hand=[])
    assert rows[1]["certified"] and rows[1]["status"] == "theorem"
