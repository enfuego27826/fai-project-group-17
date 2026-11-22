"""Tests for the transformation Gamma -> Gamma(k, s, rho) (Definition 1)."""

import pyspiel
import pytest

import games  # noqa: F401  (registers games)
from games.augment import make_augmented_game
from games.tree import build_tree
from eval.perfect_recall import perfect_recall_violations

KUHN = "kuhn_poker(players=3)"
CARDS = "card_guessing(num_cards=4)"


def _tree(base, **kw):
    return build_tree(make_augmented_game(base, **kw))


@pytest.mark.parametrize("base", [KUHN, CARDS])
@pytest.mark.parametrize("k", [0, 1, 2])
@pytest.mark.parametrize("s", [0, 1, "inf"])
@pytest.mark.parametrize("rho", ["priv", "pub"])
@pytest.mark.parametrize("simultaneous", [True, False])
def test_perfect_recall(base, k, s, rho, simultaneous):
    tree = _tree(base, k=k, s=s, rho=rho, simultaneous=simultaneous)
    assert perfect_recall_violations(tree) == {}


def _expected_kuhn_counts(k, s, rho, simultaneous):
    """Information sets of 3-player Kuhn with one round after the deal.

    Base game: 16 information sets per player, all after the deal. Each
    teammate has one message information set per own card (4), teammate 1
    also per m_0 when messages are sequential. Every later team information set
    is refined by the 2^(2k) message pairs (x 2^{2kR}); the key multiplies all
    team information sets by 2^s. The adversary's sets are refined by the
    message pairs only when rho = pub.
    """
    keys = 2 ** s if isinstance(s, int) and s > 0 else 1
    pairs = 4 ** k
    if k == 0:
        team = [16 * keys, 16 * keys]
    else:
        msg0 = 4
        msg1 = 4 * (1 if simultaneous else 2 ** k)
        team = [(msg0 + 16 * pairs) * keys, (msg1 + 16 * pairs) * keys]
    adv = 16 * (pairs if rho == "pub" else 1)
    return team + [adv]


@pytest.mark.parametrize("k", [0, 1, 2])
@pytest.mark.parametrize("s", [0, 2, "inf"])
@pytest.mark.parametrize("rho", ["priv", "pub"])
@pytest.mark.parametrize("simultaneous", [True, False])
def test_kuhn_infoset_counts(k, s, rho, simultaneous):
    tree = _tree(KUHN, k=k, s=s, rho=rho, simultaneous=simultaneous)
    got = [tree.num_infosets(p) for p in range(3)]
    assert got == _expected_kuhn_counts(k, s, rho, simultaneous)
    keys = 2 ** s if isinstance(s, int) and s > 0 else 1
    assert tree.num_terminals == 312 * 4 ** k * keys


@pytest.mark.parametrize("k", [0, 1, 2, 3])
@pytest.mark.parametrize("simultaneous", [True, False])
def test_card_guessing_infoset_counts(k, simultaneous):
    tree = _tree(CARDS, k=k, s="inf", rho="priv", simultaneous=simultaneous)
    msg0 = 4 if k > 0 else 0
    msg1 = (1 if simultaneous else 2 ** k) if k > 0 else 0
    assert tree.num_infosets(0) == msg0
    assert tree.num_infosets(1) == msg1 + 4 ** k  # guesses refined by 2^(2k) pairs
    assert tree.num_infosets(2) == 0


def test_k0_is_the_base_game():
    base = build_tree(pyspiel.load_game(KUHN))
    aug = _tree(KUHN, k=0, s=0, rho="pub")
    assert aug.num_terminals == base.num_terminals
    assert [aug.num_infosets(p) for p in range(3)] == [base.num_infosets(p) for p in range(3)]
    assert sorted(aug.term_u) == pytest.approx(sorted(base.term_u))


def _play(game, actions):
    state = game.new_initial_state()
    for a in actions:
        state.apply_action(a)
    return state


def test_information_states_follow_definition_1():
    # key=10, deal 0,1,2, then m_0=1, m_1=0 (k=1).
    pub = make_augmented_game(KUHN, k=1, s=2, rho="pub")
    priv = make_augmented_game(KUHN, k=1, s=2, rho="priv")

    # Teammate 1 picks m_1 without seeing m_0 (simultaneous round).
    st = _play(pub, [2, 0, 1, 2, 1])
    assert st.current_player() == 1
    assert st.information_state_string(1) == _play(pub, [2, 0, 1, 2, 0]).information_state_string(1)

    # After the round both teammates see both messages and the key.
    st = _play(pub, [2, 0, 1, 2, 1, 0])
    assert "key=10" in st.information_state_string(0)
    assert st.information_state_string(0).endswith("1,0")
    assert st.information_state_string(1).endswith("1,0")
    # The adversary never sees the key; it sees the messages only if public.
    st_pub = _play(pub, [2, 0, 1, 2, 1, 0, 0, 1])
    st_priv = _play(priv, [2, 0, 1, 2, 1, 0, 0, 1])
    assert st_pub.current_player() == 2
    assert "key" not in st_pub.information_state_string(2)
    assert st_pub.information_state_string(2).endswith("1,0")
    assert st_priv.information_state_string(2) == pyspiel.load_game(KUHN).new_initial_state().child(0).child(1).child(2).child(0).child(1).information_state_string(2)


def test_sequential_messages_reveal_m0():
    seq = make_augmented_game(CARDS, k=1, s=0, rho="priv", simultaneous=False)
    a = _play(seq, [3, 1]).information_state_string(1)
    b = _play(seq, [3, 0]).information_state_string(1)
    assert a != b


def test_key_is_uniform_and_game_roundtrips():
    game = make_augmented_game(KUHN, k=1, s=3, rho="pub")
    root = game.new_initial_state()
    assert root.chance_outcomes() == [(i, 1 / 8) for i in range(8)]
    again = pyspiel.load_game(str(game))
    assert again.cfg == game.cfg
    state = _play(game, [5, 0, 1, 2, 1])
    clone = state.clone()
    clone.apply_action(1)
    assert state.current_player() == 1 and clone.current_player() == 0
