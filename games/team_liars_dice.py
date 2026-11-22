"""Team Liar's Dice: three players, a two-player team against one adversary.

OpenSpiel's ``liars_dice`` supports only two players, so this is our own
implementation (Milestone 2.5).

Rules.

1. Chance rolls ``dice_per_player`` dice with ``faces`` faces for every
   player, player 0's dice first. Each player sees only its own dice.
2. (Added by ``games.augment``: key node if s > 0, then one message round
   right after the roll, ``rounds: [0]``.)
3. Players act in turn order 0, 1, 2, 0, ... A bid (q, f) claims that at least
   q dice among *all* dice show face f. Each bid must be strictly higher than
   the previous one, quantity first, then face. Instead of bidding, a player
   may call "liar" on the previous bid (not possible before the first bid;
   forced after the highest bid).
4. On a call the bid is checked against all dice. If it holds, the caller
   loses; otherwise the bidder loses.

With ``wild=True`` face 1 is wild: it counts towards bids on every other
face (bids on face 1 count only ones). Default off.

Payoffs. The team utility is u_T = +1 if the adversary loses and -1 if a
team member loses. Returns are split so that teammates' returns sum to u_T
and the game is zero-sum: if the adversary loses, it gets -1 and each
teammate +1/2; if a teammate loses, it gets -1, the adversary +1 and the
other teammate 0. This needs to know the adversary's seat (``adversary``,
default 2), which must match the seating used by ``games.augment``.

Actions. Bid (q, f) with q in 1..N (N = total dice) and f in 1..F has id
(q - 1) * F + (f - 1), so larger ids are higher bids. "Liar" is id N * F.
"""

from dataclasses import dataclass

import numpy as np
import pyspiel

_NUM_PLAYERS = 3

_GAME_TYPE = pyspiel.GameType(
    short_name="team_liars_dice",
    long_name="Team Liar's Dice (2 vs 1)",
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
    parameter_specification={"dice_per_player": 1, "faces": 3, "wild": False, "adversary": 2},
)


@dataclass(frozen=True)
class DiceConfig:
    """Rules of one Team Liar's Dice instance (plain data, so states can copy it)."""

    dice: int
    faces: int
    wild: bool
    adversary: int

    @property
    def total_dice(self):
        return _NUM_PLAYERS * self.dice

    @property
    def num_bids(self):
        return self.total_dice * self.faces

    def bid(self, action):
        """(quantity, face) of a bid action, faces numbered from 1."""
        q, f = divmod(action, self.faces)
        return q + 1, f + 1


class TeamLiarsDiceGame(pyspiel.Game):
    """Liar's Dice for a team {0, 1, 2} minus ``adversary`` against ``adversary``."""

    def __init__(self, params=None):
        params = params or {}
        self.dice = int(params.get("dice_per_player", 1))
        self.faces = int(params.get("faces", 3))
        self.wild = bool(params.get("wild", False))
        self.adversary = int(params.get("adversary", 2))
        if self.dice < 1 or self.faces < 2 or self.adversary not in range(_NUM_PLAYERS):
            raise ValueError("need dice_per_player >= 1, faces >= 2, adversary in {0, 1, 2}")
        self.cfg = DiceConfig(self.dice, self.faces, self.wild, self.adversary)
        self.total_dice = self.cfg.total_dice
        self.num_bids = self.cfg.num_bids
        game_info = pyspiel.GameInfo(
            num_distinct_actions=self.num_bids + 1,
            max_chance_outcomes=self.faces,
            num_players=_NUM_PLAYERS,
            min_utility=-1.0,
            max_utility=1.0,
            utility_sum=0.0,
            max_game_length=self.total_dice + self.num_bids + 1,
        )
        super().__init__(_GAME_TYPE, game_info, params)

    def new_initial_state(self):
        """Initial state: chance rolls player 0's first die."""
        return TeamLiarsDiceState(self)

    def make_py_observer(self, iig_obs_type=None, params=None):
        """Observer giving perfect-recall information state strings."""
        return TeamLiarsDiceObserver()

class TeamLiarsDiceState(pyspiel.State):
    """Dice of every player, the bid history and the caller, if any."""

    def __init__(self, game):
        super().__init__(game)
        self.g = game.cfg
        self.dice = [[] for _ in range(_NUM_PLAYERS)]
        self.bids = []          # (player, bid action) in order
        self.caller = None

    def _rolling(self):
        return sum(len(d) for d in self.dice) < self.g.total_dice

    def current_player(self):
        if self._rolling():
            return pyspiel.PlayerId.CHANCE
        if self.caller is not None:
            return pyspiel.PlayerId.TERMINAL
        return len(self.bids) % _NUM_PLAYERS

    def _legal_actions(self, player):
        last = self.bids[-1][1] if self.bids else -1
        actions = list(range(last + 1, self.g.num_bids))
        if self.bids:
            actions.append(self.g.num_bids)
        return actions

    def chance_outcomes(self):
        p = 1.0 / self.g.faces
        return [(f, p) for f in range(self.g.faces)]

    def _apply_action(self, action):
        if self._rolling():
            p = next(i for i in range(_NUM_PLAYERS) if len(self.dice[i]) < self.g.dice)
            self.dice[p].append(action + 1)
        elif action == self.g.num_bids:
            self.caller = self.current_player()
        else:
            self.bids.append((self.current_player(), action))

    def _action_to_string(self, player, action):
        if player == pyspiel.PlayerId.CHANCE:
            return f"Roll:{action + 1}"
        if action == self.g.num_bids:
            return "Liar"
        q, f = self.g.bid(action)
        return f"Bid:{q}x{f}"

    def is_terminal(self):
        return self.caller is not None

    def count(self, face):
        """Number of dice that count towards a bid on ``face``."""
        all_dice = [d for hand in self.dice for d in hand]
        if self.g.wild and face != 1:
            return sum(1 for d in all_dice if d == face or d == 1)
        return sum(1 for d in all_dice if d == face)

    def loser(self):
        """The player who loses the call (None before the game ends)."""
        if self.caller is None:
            return None
        bidder, action = self.bids[-1]
        q, f = self.g.bid(action)
        return self.caller if self.count(f) >= q else bidder

    def returns(self):
        loser = self.loser()
        if loser is None:
            return [0.0] * _NUM_PLAYERS
        adv = self.g.adversary
        r = [0.0] * _NUM_PLAYERS
        if loser == adv:
            for p in range(_NUM_PLAYERS):
                r[p] = -1.0 if p == adv else 0.5
        else:
            r[loser], r[adv] = -1.0, 1.0
        return r

    def __str__(self):
        bids = " ".join(f"{p}:{'%dx%d' % self.g.bid(a)}" for p, a in self.bids)
        return f"dice={self.dice} bids=[{bids}] caller={self.caller}"


class TeamLiarsDiceObserver:
    """Own dice (sorted) and the public bid history."""

    def __init__(self):
        self.tensor = np.zeros(0, np.float32)
        self.dict = {}

    def set_from(self, state, player):
        pass

    def string_from(self, state, player):
        own = "".join(str(d) for d in sorted(state.dice[player]))
        bids = ",".join(str(a) for _, a in state.bids)
        call = "|liar" if state.caller is not None else ""
        return f"dice:{own}|bids:{bids}{call}"


pyspiel.register_game(_GAME_TYPE, TeamLiarsDiceGame)
