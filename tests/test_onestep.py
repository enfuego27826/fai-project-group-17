"""eval.onestep (vectorized exact evaluator, Milestone 6) agrees with the tree evaluators."""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import games  # noqa: E402,F401
from eval import onestep  # noqa: E402
from eval.best_response import guaranteed_value  # noqa: E402
from eval.leakage import mutual_information  # noqa: E402
from games.suit_blocker import suit_phi  # noqa: E402
from run_marl import tree_of  # noqa: E402

GAMES = {
    "blocker4": ({"name": "blocker4", "base_game": "card_blocker(num_cards=4)", "team": [0, 1],
                  "adversary": 2, "rounds": [0]}, onestep.card_blocker(4)),
    "suit2x2": ({"name": "suit2x2", "base_game": "suit_blocker(suits=2,ranks=2)", "team": [0, 1],
                 "adversary": 2, "rounds": [0]}, onestep.suit_blocker(2, 2)),
    "attack2x2": ({"name": "attack2x2", "base_game": "coordinated_attack(rows=2,cols=2)",
                   "team": [0, 1], "adversary": 2, "rounds": [0]}, onestep.coordinated_attack(2, 2)),
}


def _private(text, game):
    """x index from the base part of an information state ("card:3", "card:1,0", "row:1", "")."""
    if not text:
        return 0
    val = text.split(":")[1]
    if "," in val:                       # suit blocker card "suit,rank"
        su, ra = map(int, val.split(","))
        return su * (game.n0 // game.n_block) + ra
    return int(val)


def random_tables(tree, game, k, s, rng):
    """A random behavioral team policy as tree policies and as onestep tables."""
    M, nK = 2 ** k, 2 ** s
    tables = onestep.TeamPolicy(
        msg0=np.zeros((nK, game.n0, M)), msg1=np.zeros((nK, game.n1, M)),
        act0=np.full((nK, game.n0, M, M, game.n_act0), 1.0 / game.n_act0),
        act1=np.full((nK, game.n1, M, M, game.n_act1), 1.0 / game.n_act1))
    policies = {}
    for t in tree.team:
        info = tree.players[t]
        pol = {}
        for I, key in enumerate(info.infoset_keys):
            acts = list(info.infoset_actions[I])
            p = rng.dirichlet(np.full(len(acts), 0.5))
            pol[key] = {int(a): float(q) for a, q in zip(acts, p)}
            parts = key.split("|")
            x = _private(parts[0], game)
            K = next((int(q[4:], 2) for q in parts if q.startswith("key=")), 0)
            msgs = parts[-1].rsplit(":", 1)[1]
            if msgs == "?":
                (tables.msg0 if t == 0 else tables.msg1)[K, x, acts] = p
            else:
                m0, m1 = (int(v, 2) for v in msgs.split(","))
                (tables.act0 if t == 0 else tables.act1)[K, x, m0, m1, acts] = p
        policies[t] = pol
    return policies, tables


@pytest.mark.parametrize("name", list(GAMES))
@pytest.mark.parametrize("k,s", [(1, 0), (1, 1), (2, 1)])
@pytest.mark.parametrize("rho", ["priv", "pub"])
def test_matches_tree(name, k, s, rho):
    g_cfg, game = GAMES[name]
    tree = tree_of(g_cfg, k, s, rho)
    rng = np.random.default_rng(100 * k + 10 * s + (rho == "pub"))
    for _ in range(3):
        policies, tables = random_tables(tree, game, k, s, rng)
        strategy = [(1.0, policies)]
        g_tree = guaranteed_value(tree, strategy)
        g_vec, _ = onestep.guaranteed_value(game, tables, rho)
        assert abs(g_tree - g_vec) < 1e-10
        i_x, i_c, i_ck = onestep.leakage(game, tables)
        assert abs(i_x - mutual_information(tree, strategy, channel="all")) < 1e-9
        phi = suit_phi if name == "suit2x2" else None
        assert abs(i_c - mutual_information(tree, strategy, channel="all", phi=phi)) < 1e-9
        assert abs(i_ck - mutual_information(tree, strategy, channel="all", phi=phi,
                                             given_key=True)) < 1e-9


def test_closed_forms():
    """Hand codes: blocker private value (1 - 1/n) 2^k / n, and the one-time pad."""
    n, k = 16, 2
    game = onestep.card_blocker(n)
    M = 2 ** k
    pol = onestep.TeamPolicy(msg0=np.zeros((1, n, M)), msg1=np.full((1, 1, M), 1.0 / M),
                             act0=np.ones((1, n, M, M, 1)), act1=np.zeros((1, 1, M, M, n)))
    for x in range(n):
        pol.msg0[0, x, x % M] = 1.0
        pol.act1[0, 0, x % M, :, x] = 1.0 / (n // M)
    g, _ = onestep.guaranteed_value(game, pol, "priv")
    assert abs(g - (1 - 1 / n) * M / n) < 1e-12
    # pad the class with a 2-bit key: public value equals the private one, leakage 0
    nK = 4
    pad = onestep.TeamPolicy(msg0=np.zeros((nK, n, M)), msg1=np.full((nK, 1, M), 1.0 / M),
                             act0=np.ones((nK, n, M, M, 1)), act1=np.zeros((nK, 1, M, M, n)))
    for K in range(nK):
        for x in range(n):
            pad.msg0[K, x, (x % M) ^ K] = 1.0
            pad.act1[K, 0, (x % M) ^ K, :, x] = 1.0 / (n // M)
    g, _ = onestep.guaranteed_value(game, pad, "pub")
    assert abs(g - (1 - 1 / n) * M / n) < 1e-12
    assert onestep.leakage(game, pad)[0] < 1e-12
