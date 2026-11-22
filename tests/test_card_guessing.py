import pyspiel
import pytest

import games.card_guessing  # noqa: F401  (registers the game)


@pytest.mark.parametrize("n", [1, 2, 4, 5])
def test_payoffs_and_zero_sum(n):
    game = pyspiel.load_game("card_guessing", {"num_cards": n})
    root = game.new_initial_state()
    assert root.is_chance_node()
    assert sum(p for _, p in root.chance_outcomes()) == pytest.approx(1.0)
    for card, _ in root.chance_outcomes():
        dealt = root.child(card)
        assert dealt.current_player() == 1
        assert dealt.legal_actions() == list(range(n))
        for guess in range(n):
            r = dealt.child(guess).returns()
            assert sum(r) == pytest.approx(0.0)
            assert r[0] + r[1] == (1.0 if guess == card else 0.0)


def test_information_states():
    game = pyspiel.load_game("card_guessing", {"num_cards": 4})
    dealt = game.new_initial_state().child(3)
    assert dealt.information_state_string(0) == "card:3"
    assert dealt.information_state_string(1) == ""
    assert dealt.information_state_string(2) == ""


def test_active_adversary_is_a_stub():
    with pytest.raises(NotImplementedError):
        pyspiel.load_game("card_guessing", {"adversary_acts": True})
