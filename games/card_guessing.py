"""Card guessing, the base game of Example 1 in the report.

Players: teammate 0 (sees the card), teammate 1 (names a card), adversary 2.
Chance deals teammate 0 a card uniformly from ``num_cards``. Teammate 1 then
names a card, and the team wins if the guess is right.

Payoffs. The team utility is u_T = 1 for a correct guess and 0 otherwise, and
the adversary gets -u_T. OpenSpiel returns are per player, so we split u_T
evenly between the two teammates: returns = [u_T/2, u_T/2, -u_T]. This keeps
the game zero-sum and matches 3-player Kuhn poker, where the team utility is
the sum of the teammates' returns, i.e. minus the adversary's return.

Communication is not part of this game. It is added by the transformation in
``games.augment``, with one round right after the deal.
"""

import numpy as np
import pyspiel

_NUM_PLAYERS = 3
_MAX_CARDS = 64

_GAME_TYPE = pyspiel.GameType(
    short_name="card_guessing",
    long_name="Card Guessing (team game)",
    dynamics=pyspiel.GameType.Dynamics.SEQUENTIAL,
    chance_mode=pyspiel.GameType.ChanceMode.EXPLICIT_STOCHASTIC,
    information=pyspiel.GameType.Information.IMPERFECT_INFORMATION,
    utility=pyspiel.GameType.Utility.ZERO_SUM,
    reward_model=pyspiel.GameType.RewardModel.TERMINAL,
    max_num_players=_NUM_PLAYERS,
    min_num_players=_NUM_PLAYERS,
    provides_information_state_string=True,
    provides_information_state_tensor=False,
    provides_observation_string=False,
    provides_observation_tensor=False,
    parameter_specification={"num_cards": 4, "adversary_acts": False},
)


class CardGuessingGame(pyspiel.Game):
    """Card guessing with ``num_cards`` cards (passive adversary only, for now).

    Active adversary (``adversary_acts=True``) is a stub, rules to be decided by
    the team. Candidate rules, all keeping the game small and zero-sum:

    1. Blocking. After the deal and before the guess, the adversary removes one
       card label from the set teammate 1 may name (without seeing the card). If
       the true card is removed the team scores 0. This makes the adversary's
       choice depend on what it can infer about the card, so on a public channel
       messages become exploitable.
    2. Betting. After the guess, the adversary (seeing only public messages if
       rho = pub) chooses to "challenge" or "pass"; a challenge doubles the
       stake. The team then wants messages that are informative to teammate 1
       but not to the adversary.
    3. Decoy card. The adversary also holds a card, and the team scores only if
       the guess matches teammate 0's card and differs from the adversary's.

    Option 1 is the simplest candidate for an increasing delta(k) with an acting
    adversary (Question 2 in the report). It is implemented, as specified in
    Milestone 2, as the separate game ``card_blocker`` (games/card_blocker.py).
    """

    def __init__(self, params=None):
        params = params or {}
        self.num_cards = int(params.get("num_cards", 4))
        self.adversary_acts = bool(params.get("adversary_acts", False))
        if not 1 <= self.num_cards <= _MAX_CARDS:
            raise ValueError(f"num_cards must be in [1, {_MAX_CARDS}]")
        if self.adversary_acts:
            raise NotImplementedError(
                "Active-adversary card guessing is not designed yet; see the "
                "class docstring for candidate rules.")
        game_info = pyspiel.GameInfo(
            num_distinct_actions=self.num_cards,
            max_chance_outcomes=self.num_cards,
            num_players=_NUM_PLAYERS,
            min_utility=-1.0,
            max_utility=0.5,
            utility_sum=0.0,
            max_game_length=2,
        )
        super().__init__(_GAME_TYPE, game_info, params)

    def new_initial_state(self):
        """Initial state: chance is about to deal teammate 0's card."""
        return CardGuessingState(self)

    def make_py_observer(self, iig_obs_type=None, params=None):
        """Observer giving perfect-recall information state strings."""
        return CardGuessingObserver()


class CardGuessingState(pyspiel.State):
    """State of passive card guessing: the card and the guess, if made."""

    def __init__(self, game):
        super().__init__(game)
        self.num_cards = game.num_cards
        self.card = None
        self.guess = None

    def current_player(self):
        if self.guess is not None:
            return pyspiel.PlayerId.TERMINAL
        if self.card is None:
            return pyspiel.PlayerId.CHANCE
        return 1

    def _legal_actions(self, player):
        assert player == 1
        return list(range(self.num_cards))

    def chance_outcomes(self):
        p = 1.0 / self.num_cards
        return [(c, p) for c in range(self.num_cards)]

    def _apply_action(self, action):
        if self.card is None:
            self.card = action
        else:
            self.guess = action

    def _action_to_string(self, player, action):
        if player == pyspiel.PlayerId.CHANCE:
            return f"Deal:{action}"
        return f"Guess:{action}"

    def is_terminal(self):
        return self.guess is not None

    def returns(self):
        if self.guess is None:
            return [0.0, 0.0, 0.0]
        u = 1.0 if self.guess == self.card else 0.0
        return [u / 2, u / 2, 0.0 - u]

    def __str__(self):
        return f"card={self.card} guess={self.guess}"


class CardGuessingObserver:
    """Information state strings: teammate 0 sees its card, nobody else sees anything."""

    def __init__(self):
        self.tensor = np.zeros(0, np.float32)
        self.dict = {}

    def set_from(self, state, player):
        pass

    def string_from(self, state, player):
        if player == 0 and state.card is not None:
            return f"card:{state.card}"
        return ""


pyspiel.register_game(_GAME_TYPE, CardGuessingGame)
