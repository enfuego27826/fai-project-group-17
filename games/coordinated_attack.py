"""Coordinated attack: both teammates hold private information and must talk.

Rules, in order (Milestone 2.5):

1. Targets form an ``rows x cols`` grid. Chance picks the weak target (i, j)
   uniformly. Teammate 0 observes only the row i, teammate 1 only the column j.
2. (Added by ``games.augment``: key node if s > 0, then one message round
   right after the deal. The adversary sees the messages iff rho = pub.)
3. The adversary (player 2) chooses a target d to defend.
4. Teammate 0, then teammate 1, each choose a target to attack, without
   seeing d or each other's choice.

The team utility is u_T = 1 if both attack (i, j) and d != (i, j), else 0;
the adversary gets -u_T. Returns are [u_T/2, u_T/2, -u_T] as in card guessing.
Targets are numbered t = i * cols + j.
"""

import numpy as np
import pyspiel

_NUM_PLAYERS = 3

_GAME_TYPE = pyspiel.GameType(
    short_name="coordinated_attack",
    long_name="Coordinated Attack (team game)",
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
    parameter_specification={"rows": 2, "cols": 2},
)


class CoordinatedAttackGame(pyspiel.Game):
    """Coordinated attack on a ``rows x cols`` grid of targets."""

    def __init__(self, params=None):
        params = params or {}
        self.rows = int(params.get("rows", 2))
        self.cols = int(params.get("cols", 2))
        if self.rows < 1 or self.cols < 1 or self.rows * self.cols < 2:
            raise ValueError("need at least two targets")
        n = self.rows * self.cols
        game_info = pyspiel.GameInfo(
            num_distinct_actions=n,
            max_chance_outcomes=n,
            num_players=_NUM_PLAYERS,
            min_utility=-1.0,
            max_utility=0.5,
            utility_sum=0.0,
            max_game_length=4,
        )
        super().__init__(_GAME_TYPE, game_info, params)

    def new_initial_state(self):
        """Initial state: chance is about to pick the weak target."""
        return CoordinatedAttackState(self)

    def make_py_observer(self, iig_obs_type=None, params=None):
        """Observer giving perfect-recall information state strings."""
        return CoordinatedAttackObserver()


class CoordinatedAttackState(pyspiel.State):
    """State: weak target, defended target and the two attacks, as far as chosen."""

    def __init__(self, game):
        super().__init__(game)
        self.rows, self.cols = game.rows, game.cols
        self.weak = None
        self.defend = None
        self.attacks = []

    def current_player(self):
        if self.weak is None:
            return pyspiel.PlayerId.CHANCE
        if self.defend is None:
            return 2
        if len(self.attacks) < 2:
            return len(self.attacks)
        return pyspiel.PlayerId.TERMINAL

    def _legal_actions(self, player):
        return list(range(self.rows * self.cols))

    def chance_outcomes(self):
        n = self.rows * self.cols
        return [(t, 1.0 / n) for t in range(n)]

    def _apply_action(self, action):
        if self.weak is None:
            self.weak = action
        elif self.defend is None:
            self.defend = action
        else:
            self.attacks.append(action)

    def _action_to_string(self, player, action):
        i, j = divmod(action, self.cols)
        if player == pyspiel.PlayerId.CHANCE:
            return f"Weak:({i},{j})"
        return f"Defend:({i},{j})" if player == 2 else f"Attack:({i},{j})"

    def is_terminal(self):
        return len(self.attacks) == 2

    def returns(self):
        if not self.is_terminal():
            return [0.0, 0.0, 0.0]
        win = self.attacks[0] == self.weak == self.attacks[1] and self.defend != self.weak
        u = 1.0 if win else 0.0
        return [u / 2, u / 2, 0.0 - u]

    def __str__(self):
        return f"weak={self.weak} defend={self.defend} attacks={self.attacks}"


class CoordinatedAttackObserver:
    """Teammate 0 sees the row, teammate 1 the column, the adversary nothing."""

    def __init__(self):
        self.tensor = np.zeros(0, np.float32)
        self.dict = {}

    def set_from(self, state, player):
        pass

    def string_from(self, state, player):
        if state.weak is None or player == 2:
            return ""
        i, j = divmod(state.weak, state.cols)
        return f"row:{i}" if player == 0 else f"col:{j}"


pyspiel.register_game(_GAME_TYPE, CoordinatedAttackGame)
