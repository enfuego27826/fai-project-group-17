"""Suit blocker (games.suit_blocker, Milestone 5): hand-derived values for S = R = 2."""

import pytest

import games  # noqa: F401
from eval.best_response import guaranteed_value
from eval.leakage import leakage_labels, mutual_information
from games.augment import make_augmented_game
from games.suit_blocker import suit_phi
from games.tree import build_tree
from solvers.backends import resolve_backend
from solvers.finite_s import solve_bilinear, solve_key_pure
from solvers.tmecor_cg import solve_tmecor

BASE = "suit_blocker(suits=2,ranks=2)"
needs_gurobi = pytest.mark.skipif(resolve_backend("auto") != "gurobi",
                                  reason="exact finite-s solve needs Gurobi")


def tree(k, s, rho):
    return build_tree(make_augmented_game(BASE, k=k, s=s, rho=rho), label_fn=leakage_labels)


@pytest.mark.parametrize("k, expected", [(0, 1 / 8), (1, 1 / 4), (2, 1 / 2)])
def test_private_values(k, expected):
    """V(k, inf, priv) = 1/8, 1/4, 1/2: the guess is right w.p. 2^k / 4, the suit survives w.p. 1/2."""
    assert solve_tmecor(tree(k, "inf", "priv")).value == pytest.approx(expected, abs=1e-7)


def test_pad_the_suit_bit():
    """V(2, 1, pub) = 1/2 = V(2, inf, priv): one key bit pads the suit, the rank goes in clear."""
    assert solve_key_pure(tree(2, 1, "pub")).value == pytest.approx(0.5, abs=1e-7)


@needs_gurobi
def test_public_no_key():
    """V(2, 0, pub) >= 1/4: send the rank in clear and guess the suit at random.

    The hand value is 1/4. The exact bilinear solve finds a strategy worth 1/4
    but does not close the gap within its time limit (upper bound about 0.28
    after 300 s; results/m5_suit_values), so only the lower end is checked.
    """
    res = solve_bilinear(tree(2, 0, "pub"), time_limit=20)
    assert res.value == pytest.approx(0.25, abs=1e-6) and res.bound >= 0.25 - 1e-6


def _code(pad):
    """Teammate 0 sends (suit xor key, rank) if ``pad`` else (suit, rank); teammate 1 decodes."""
    t = tree(2, 1, "pub")
    pol = {0: {}, 1: {}}
    for p in (0, 1):
        info = t.players[p]
        for key, acts in zip(info.infoset_keys, info.infoset_actions):
            kb = int(key.split("key=")[1][0])
            if p == 0 and "card:" in key:
                suit, rank = map(int, key.split("card:")[1].split("|")[0].split(","))
                m = 2 * ((suit ^ kb) if pad else suit) + rank
            elif p == 1 and key.endswith("?"):           # teammate 1's own message: constant
                m = 0
            else:                                        # teammate 1 guesses
                m0 = int(key.split(":")[-1].split(",")[0], 2)    # messages are binary strings
                sb, rank = divmod(m0, 2)
                m = 2 * ((sb ^ kb) if pad else sb) + rank
            pol[p][key] = {int(a): float(a == m) for a in acts}
    return t, [(1.0, pol)]


def test_exploitable_leakage():
    """Padding the suit: I(M; X) = 1 bit (the rank), I(M; suit) = 0, and g = 1/2."""
    t, strat = _code(pad=True)
    assert mutual_information(t, strat) == pytest.approx(1.0, abs=1e-9)
    assert mutual_information(t, strat, phi=suit_phi) == pytest.approx(0.0, abs=1e-9)
    assert guaranteed_value(t, strat) == pytest.approx(0.5, abs=1e-9)
    assert mutual_information(t, strat, phi=suit_phi, given_key=True) == pytest.approx(1.0, abs=1e-9)
    t, strat = _code(pad=False)
    assert mutual_information(t, strat) == pytest.approx(2.0, abs=1e-9)
    assert mutual_information(t, strat, phi=suit_phi) == pytest.approx(1.0, abs=1e-9)
    assert guaranteed_value(t, strat) == pytest.approx(0.0, abs=1e-9)


def _recorded_suit_cells():
    """(game, k, s, lower) for finite-s public cells in the committed Milestone 5 summaries."""
    import re
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    cells = []
    for summary in sorted(root.glob("results/m5_suit_*/*/0/summary.md")):
        for line in summary.read_text().splitlines():
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) < 5 or not parts[0].startswith("suit") or parts[3] != "pub" \
                    or parts[2] == "inf":
                continue
            lower = float(re.findall(r"[-+]?\d*\.\d+", parts[4])[0])
            cells.append((parts[0], int(parts[1]), int(parts[2]), lower))
    return cells


def test_recorded_suit_values_respect_lemma_cap():
    """The Lemma's cap (1/4 at s = 0, 1 - 2^-s at s >= 1) holds for every suit-blocker value found."""
    cells = _recorded_suit_cells()
    assert len(cells) >= 30
    for game, k, s, lower in cells:
        cap = 0.25 if s == 0 else 1 - 2.0 ** -s
        assert lower <= cap + 1e-7, (game, k, s, lower)
