"""Milestone 8: fast leakage index and responsiveness logging."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import games  # noqa: E402,F401
from eval.leakage import LeakageIndex, mutual_information  # noqa: E402
from eval.sequence_form import realization_plan  # noqa: E402
from learning.tabular_pg import PGConfig, train  # noqa: E402
from run_marl import tree_of  # noqa: E402

G = {"name": "attack2x2", "base_game": "coordinated_attack(rows=2,cols=2)", "team": [0, 1],
     "adversary": 2, "rounds": [0]}


def test_index_matches_mutual_information():
    tree = tree_of(G, 1, 1, "pub")
    res = train(tree, PGConfig(iterations=60, batch=64, lr=8.0, init_scale=1.0), seed=0)
    pol = res.policies
    r = [realization_plan(tree.players[t], pol[t]) for t in tree.team]
    assert abs(LeakageIndex(tree).mi(*r) - mutual_information(tree, [(1.0, pol)])) < 1e-10


def test_logging_does_not_change_training_and_gap_is_nonnegative():
    tree = tree_of(G, 1, 2, "pub")
    for opp, extra in [("best_response", {}), ("noisy_br", {"epsilon": 0.5}),
                       ("model", {"model_window": 64, "model_every": 10}),
                       ("learning", {"adv_steps": 4})]:
        a = train(tree, PGConfig(iterations=120, batch=64, lr=8.0, **extra), seed=4, opponent=opp)
        b = train(tree, PGConfig(iterations=120, batch=64, lr=8.0, resp_every=20, **extra),
                  seed=4, opponent=opp)
        assert a.policies == b.policies and a.curve == b.curve
        gaps = [r for _, r, _, _ in b.resp_log if r is not None]
        assert min(gaps) >= -1e-12
        if opp == "best_response":
            assert max(gaps) < 1e-12
