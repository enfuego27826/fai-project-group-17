"""Suit blocker: the adversary blocks a suit, so only the suit needs hiding (Milestone 5).

Rules, in order:

1. Chance deals a card X = (suit, rank) uniformly from ``suits`` x ``ranks``
   cards to teammate 0. Card id = suit * ranks + rank.
2. (Added by ``games.augment``: key node if s > 0, then one message round
   right after the deal. The adversary sees the messages iff rho = pub.)
3. The adversary (player 2) blocks a suit b.
4. Teammate 1 names a card g without seeing b.

The team utility is u_T = 1 if g = X and suit(X) != b, else 0; the adversary
gets -u_T. Returns are [u_T/2, u_T/2, -u_T], as in the card blocker.

The adversary's payoff depends on X only through its suit, so on a public
channel only the suit needs hiding; the rank can be sent in clear.
"""

import numpy as np
import pyspiel

_NUM_PLAYERS = 3
_MAX_CARDS = 64

_GAME_TYPE = pyspiel.GameType(
    short_name="suit_blocker",
    long_name="Card Guessing with a Suit-Blocking Adversary (team game)",
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
    parameter_specification={"suits": 2, "ranks": 2},
)


class SuitBlockerGame(pyspiel.Game):
    """Card guessing where the adversary blocks one suit before the guess."""

    def __init__(self, params=None):
        params = params or {}
        self.suits = int(params.get("suits", 2))
        self.ranks = int(params.get("ranks", 2))
        if self.suits < 2 or self.ranks < 1 or self.suits * self.ranks > _MAX_CARDS:
            raise ValueError("need suits >= 2, ranks >= 1, suits * ranks <= 64")
        n = self.suits * self.ranks
        game_info = pyspiel.GameInfo(
            num_distinct_actions=n,
            max_chance_outcomes=n,
            num_players=_NUM_PLAYERS,
            min_utility=-1.0,
            max_utility=0.5,
            utility_sum=0.0,
            max_game_length=3,
        )
        super().__init__(_GAME_TYPE, game_info, params)

    def new_initial_state(self):
        """Initial state: chance is about to deal teammate 0's card."""
        return SuitBlockerState(self)

    def make_py_observer(self, iig_obs_type=None, params=None):
        """Observer giving perfect-recall information state strings."""
        return SuitBlockerObserver()


class SuitBlockerState(pyspiel.State):
    """State: the card X, the blocked suit b and the guess g, as far as chosen."""

    def __init__(self, game):
        super().__init__(game)
        self.suits = game.suits
        self.ranks = game.ranks
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
        return list(range(self.suits)) if player == 2 else list(range(self.suits * self.ranks))

    def chance_outcomes(self):
        n = self.suits * self.ranks
        return [(c, 1.0 / n) for c in range(n)]

    def _apply_action(self, action):
        if self.card is None:
            self.card = action
        elif self.block is None:
            self.block = action
        else:
            self.guess = action

    def _action_to_string(self, player, action):
        if player == pyspiel.PlayerId.CHANCE:
            return f"Deal:{divmod(action, self.ranks)}"
        return f"BlockSuit:{action}" if player == 2 else f"Guess:{divmod(action, self.ranks)}"

    def is_terminal(self):
        return self.guess is not None

    def returns(self):
        if self.guess is None:
            return [0.0, 0.0, 0.0]
        u = 1.0 if (self.guess == self.card and self.block != self.card // self.ranks) else 0.0
        return [u / 2, u / 2, 0.0 - u]

    def __str__(self):
        return f"card={self.card} block={self.block} guess={self.guess}"


class SuitBlockerObserver:
    """Teammate 0 sees its card as 'card:suit,rank'; nobody else sees anything private."""

    def __init__(self):
        self.tensor = np.zeros(0, np.float32)
        self.dict = {}

    def set_from(self, state, player):
        pass

    def string_from(self, state, player):
        if player == 0 and state.card is not None:
            suit, rank = divmod(state.card, state.ranks)
            return f"card:{suit},{rank}"
        return ""


pyspiel.register_game(_GAME_TYPE, SuitBlockerGame)


def suit_phi(x):
    """phi(X) for the exploitable leakage I(M; phi(X)): the suit of teammate 0's card.

    ``x`` is the leakage label ``AugmentedState.team_private_info()``: per round,
    the teammates' base information states ('card:suit,rank' for teammate 0).
    """
    return tuple(tuple(part.split(":")[1].split(",")[0] if part else "" for part in rnd)
                 for rnd in x)
