"""Card guessing with a blocker: an active adversary for which eavesdropping helps.

Rules, in order (Milestone 2, option 1 in ``games.card_guessing``):

1. Chance deals X uniformly from ``num_cards`` cards to teammate 0.
2. (Added by ``games.augment``: key node if s > 0, then one message round
   right after the deal. The adversary sees the messages iff rho = pub.)
3. The adversary (player 2) blocks a card b.
4. Teammate 1 names a card g. By default it does not observe b
   (``guesser_sees_block=False``); with ``guesser_sees_block=True`` it does.

The team utility is u_T = 1 if g = X and b != X, else 0; the adversary gets
-u_T. As in card guessing, returns are [u_T/2, u_T/2, -u_T].

With a private channel and s = infinity the value for n cards is
(1 - 1/n) 2^k / n for 2^k <= n: the team spreads X uniformly over 2^k message
classes and guesses uniformly within the class, so whatever the adversary
blocks, the team wins with probability (2^k / n)(1 - 1/n).
"""

import numpy as np
import pyspiel

_NUM_PLAYERS = 3
_MAX_CARDS = 64

_GAME_TYPE = pyspiel.GameType(
    short_name="card_blocker",
    long_name="Card Guessing with a Blocking Adversary (team game)",
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
    parameter_specification={"num_cards": 4, "guesser_sees_block": False},
)


class CardBlockerGame(pyspiel.Game):
    """Card guessing where the adversary blocks one card before the guess."""

    def __init__(self, params=None):
        params = params or {}
        self.num_cards = int(params.get("num_cards", 4))
        self.guesser_sees_block = bool(params.get("guesser_sees_block", False))
        if not 2 <= self.num_cards <= _MAX_CARDS:
            raise ValueError(f"num_cards must be in [2, {_MAX_CARDS}]")
        game_info = pyspiel.GameInfo(
            num_distinct_actions=self.num_cards,
            max_chance_outcomes=self.num_cards,
            num_players=_NUM_PLAYERS,
            min_utility=-1.0,
            max_utility=0.5,
            utility_sum=0.0,
            max_game_length=3,
        )
        super().__init__(_GAME_TYPE, game_info, params)

    def new_initial_state(self):
        """Initial state: chance is about to deal teammate 0's card."""
        return CardBlockerState(self)

    def make_py_observer(self, iig_obs_type=None, params=None):
        """Observer giving perfect-recall information state strings."""
        return CardBlockerObserver()


class CardBlockerState(pyspiel.State):
    """State: the card X, the blocked card b and the guess g, as far as chosen."""

    def __init__(self, game):
        super().__init__(game)
        self.num_cards = game.num_cards
        self.guesser_sees_block = game.guesser_sees_block
        self.card = None
        self.block = None
        self.guess = None

    def current_player(self):
        if self.card is None:
            return pyspiel.PlayerId.CHANCE
        if self.block is None:
            return 2
        if self.guess is None:
            return 1
        return pyspiel.PlayerId.TERMINAL

    def _legal_actions(self, player):
        return list(range(self.num_cards))

    def chance_outcomes(self):
        p = 1.0 / self.num_cards
        return [(c, p) for c in range(self.num_cards)]

    def _apply_action(self, action):
        if self.card is None:
            self.card = action
        elif self.block is None:
            self.block = action
        else:
            self.guess = action

    def _action_to_string(self, player, action):
        if player == pyspiel.PlayerId.CHANCE:
            return f"Deal:{action}"
        return f"Block:{action}" if player == 2 else f"Guess:{action}"

    def is_terminal(self):
        return self.guess is not None

    def returns(self):
        if self.guess is None:
            return [0.0, 0.0, 0.0]
        u = 1.0 if (self.guess == self.card and self.block != self.card) else 0.0
        return [u / 2, u / 2, 0.0 - u]

    def __str__(self):
        return f"card={self.card} block={self.block} guess={self.guess}"


class CardBlockerObserver:
    """Teammate 0 sees its card; teammate 1 sees the block only if configured."""

    def __init__(self):
        self.tensor = np.zeros(0, np.float32)
        self.dict = {}

    def set_from(self, state, player):
        pass

    def string_from(self, state, player):
        if player == 0 and state.card is not None:
            return f"card:{state.card}"
        if player == 1 and state.guesser_sees_block and state.block is not None:
            return f"block:{state.block}"
        return ""


pyspiel.register_game(_GAME_TYPE, CardBlockerGame)
