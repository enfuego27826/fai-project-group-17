"""The transformation Gamma -> Gamma(k, s, rho) of Definition 1 in the report.

``AugmentedGame`` wraps any OpenSpiel game with a two-player team and one
adversary and adds, following Definition 1:

1. Key. If ``s`` is finite and positive, chance draws K uniformly from {0,1}^s
   at the root. Both teammates observe K, the adversary does not. For s = 0
   there is no key node. For s = infinity there is no key node either: the
   correlation device mu of TMECor is not part of the game tree and is handled
   by the solver (``solvers.tmecor_cg`` solves the s = infinity game by mixing
   over joint pure plans of Gamma(k, 0, rho)).
2. Messages. Communication rounds happen at the histories H_r. Here H_r is
   specified generically by chance phases of the base game: ``rounds="phase0"``
   (Python helper: ``rounds=(0,)``) means "one round the first time play leaves chance phase 0", which for
   Kuhn poker and card guessing is right after the deal, before any other
   move. In each round teammate team[0] picks m_0 in {0,1}^k, then teammate
   team[1] picks m_1 in {0,1}^k, and both messages are revealed to both
   teammates at the end of the round. With ``simultaneous=True`` (default)
   team[1] does not see m_0 when it picks m_1; with ``simultaneous=False`` it
   does. For k = 0 the message set has one element, so rounds are skipped.
3. Visibility. If rho = "pub" the adversary also observes the messages at the
   end of each round; if rho = "priv" it does not.

Information sets. A player's information state string is the base game's
string followed by what the player observed from the augmentation, in order:
the key (teammates only) and, for each finished round r, the player's base
information state at the start of the round followed by the revealed messages.
Recording the base information state at the round makes the interleaving of
messages and base-game observations explicit, so perfect recall carries over
from the base game. ``eval.perfect_recall`` checks this on concrete instances.

The game is registered as ``augmented_team_game``; ``make_augmented_game`` is
the convenience constructor.
"""

from dataclasses import dataclass

import numpy as np
import pyspiel

INF = -1  # encoding of s = infinity in game parameters

_GAME_TYPE = pyspiel.GameType(
    short_name="augmented_team_game",
    long_name="Team game with a k-bit channel, s-bit key and visibility rho",
    dynamics=pyspiel.GameType.Dynamics.SEQUENTIAL,
    chance_mode=pyspiel.GameType.ChanceMode.EXPLICIT_STOCHASTIC,
    information=pyspiel.GameType.Information.IMPERFECT_INFORMATION,
    utility=pyspiel.GameType.Utility.ZERO_SUM,
    reward_model=pyspiel.GameType.RewardModel.TERMINAL,
    max_num_players=10,
    min_num_players=3,
    provides_information_state_string=True,
    provides_information_state_tensor=False,
    provides_observation_string=False,
    provides_observation_tensor=False,
    parameter_specification={
        "base_game": {"name": "kuhn_poker", "players": 3},
        "team0": 0,
        "team1": 1,
        "adversary": 2,
        "k": 1,
        "s": INF,
        "rho": "priv",
        "rounds": "phase0",
        "simultaneous": True,
    },
)


def _parse_rounds(text):
    """Parse "phase0+phase2" into (0, 2); "" or "none" means no rounds.

    Plain numbers are avoided in string parameters because OpenSpiel re-parses
    them as ints when a game is deserialized.
    """
    text = str(text).strip()
    if text in ("", "none"):
        return ()
    phases = []
    for part in text.split("+"):
        if not part.startswith("phase"):
            raise ValueError(f"bad rounds spec {text!r}; use e.g. 'phase0+phase1'")
        phases.append(int(part[len("phase"):]))
    return tuple(phases)


def _format_rounds(phases):
    return "+".join(f"phase{int(r)}" for r in phases) or "none"


@dataclass(frozen=True)
class AugmentConfig:
    """Parameters of Gamma(k, s, rho) that states need (plain data, cheap to copy)."""

    team: tuple
    adversary: int
    k: int
    s: int
    rho: str
    rounds: tuple
    simultaneous: bool
    num_players: int

    @property
    def num_messages(self):
        return 2 ** self.k

    @property
    def has_key(self):
        return self.s not in (0, INF)

    @property
    def num_keys(self):
        return 2 ** self.s if self.has_key else 1

    @property
    def active_rounds(self):
        return self.rounds if self.k > 0 else ()


class AugmentedGame(pyspiel.Game):
    """Gamma(k, s, rho) built from a base game Gamma (Definition 1)."""

    def __init__(self, params=None):
        spec = dict(_GAME_TYPE.parameter_specification)
        spec.update(params or {})
        base = dict(spec["base_game"])
        self.base_game = pyspiel.load_game(base.pop("name"), base)
        self.team = (int(spec["team0"]), int(spec["team1"]))
        self.adversary = int(spec["adversary"])
        self.k = int(spec["k"])
        self.s = int(spec["s"])
        self.rho = str(spec["rho"])
        self.rounds = _parse_rounds(spec["rounds"])
        self.simultaneous = bool(spec["simultaneous"])
        self._validate()

        self.cfg = AugmentConfig(self.team, self.adversary, self.k, self.s, self.rho,
                                 self.rounds, self.simultaneous,
                                 self.base_game.num_players())
        cfg = self.cfg

        base = self.base_game
        game_info = pyspiel.GameInfo(
            num_distinct_actions=max(base.num_distinct_actions(), cfg.num_messages),
            max_chance_outcomes=max(base.max_chance_outcomes(), cfg.num_keys),
            num_players=base.num_players(),
            min_utility=base.min_utility(),
            max_utility=base.max_utility(),
            utility_sum=0.0,
            max_game_length=(base.max_game_length() + 2 * len(cfg.active_rounds)
                             + int(cfg.has_key)),
        )
        super().__init__(_GAME_TYPE, game_info, spec)

    def _validate(self):
        n = self.base_game.num_players()
        players = set(self.team) | {self.adversary}
        if len(self.team) != 2 or len(players) != 3 or not players <= set(range(n)):
            raise ValueError(f"need two distinct teammates and one adversary among "
                             f"{n} players, got team={self.team} adversary={self.adversary}")
        if n != 3:
            raise ValueError("only 3-player base games (2 teammates + adversary) are supported")
        if self.base_game.get_type().utility != pyspiel.GameType.Utility.ZERO_SUM:
            raise ValueError("base game must be zero-sum")
        if self.k < 0 or self.s < INF:
            raise ValueError("k must be >= 0 and s >= 0 or INF (-1)")
        if self.rho not in ("priv", "pub"):
            raise ValueError("rho must be 'priv' or 'pub'")

    def new_initial_state(self):
        """Root of Gamma(k, s, rho): the key node if s is finite and positive."""
        return AugmentedState(self)

    def make_py_observer(self, iig_obs_type=None, params=None):
        """Observer giving the augmented information state strings."""
        return AugmentedObserver()


class AugmentedState(pyspiel.State):
    """State of Gamma(k, s, rho): a base state plus key and message log."""

    def __init__(self, game):
        super().__init__(game)
        self.g = game.cfg
        self.inner = game.base_game.new_initial_state()
        self.key = None
        self.chance_phases_done = 0
        self.round_log = []        # finished rounds: dict(index, x, msgs)
        self.pending = None        # current round: dict(index, x, msgs)
        self._maybe_start_round(prev_was_chance=False)

    # ------------------------------------------------------------------ dynamics

    def _key_pending(self):
        return self.g.has_key and self.key is None

    def current_player(self):
        if self._key_pending():
            return pyspiel.PlayerId.CHANCE
        if self.pending is not None:
            return self.g.team[len(self.pending["msgs"])]
        if self.inner.is_terminal():
            return pyspiel.PlayerId.TERMINAL
        if self.inner.is_chance_node():
            return pyspiel.PlayerId.CHANCE
        return self.inner.current_player()

    def _legal_actions(self, player):
        if self.pending is not None:
            return list(range(self.g.num_messages))
        return self.inner.legal_actions(player)

    def chance_outcomes(self):
        if self._key_pending():
            p = 1.0 / self.g.num_keys
            return [(key, p) for key in range(self.g.num_keys)]
        return self.inner.chance_outcomes()

    def _apply_action(self, action):
        if self._key_pending():
            self.key = action
            return
        if self.pending is not None:
            self.pending["msgs"].append(action)
            if len(self.pending["msgs"]) == 2:
                self.round_log.append(self.pending)
                self.pending = None
            return
        was_chance = self.inner.is_chance_node()
        self.inner.apply_action(action)
        self._maybe_start_round(prev_was_chance=was_chance)

    def _maybe_start_round(self, prev_was_chance):
        """Start a round if play just left one of the chance phases in H_r."""
        inner = self.inner
        if not prev_was_chance or inner.is_chance_node():
            return
        phase = self.chance_phases_done
        self.chance_phases_done += 1
        if phase in self.g.active_rounds and not inner.is_terminal():
            x = tuple(inner.information_state_string(p) for p in range(self.g.num_players))
            self.pending = {"index": phase, "x": x, "msgs": []}

    def is_terminal(self):
        return self.pending is None and not self._key_pending() and self.inner.is_terminal()

    def returns(self):
        return self.inner.returns() if self.is_terminal() else [0.0] * self.g.num_players

    def _action_to_string(self, player, action):
        if player == pyspiel.PlayerId.CHANCE and self._key_pending():
            return f"Key:{action:0{self.g.s}b}"
        if self.pending is not None:
            return f"Msg:{self._fmt(action)}"
        return self.inner.action_to_string(player, action)

    # ------------------------------------------------------------- observations

    def _fmt(self, m):
        return format(m, f"0{self.g.k}b")

    def information_state(self, player):
        """Information state string of ``player`` in Gamma(k, s, rho)."""
        g = self.g
        parts = [self.inner.information_state_string(player)]
        is_team = player in g.team
        if is_team and g.has_key and self.key is not None:
            parts.append(f"key={self.key:0{g.s}b}")
        sees_messages = is_team or g.rho == "pub"
        if sees_messages:
            for rnd in self.round_log:
                msgs = ",".join(self._fmt(m) for m in rnd["msgs"])
                parts.append(f"r{rnd['index']}@{rnd['x'][player]}:{msgs}")
        if is_team and self.pending is not None:
            rnd = self.pending
            own = g.team.index(player)
            if g.simultaneous:
                visible = rnd["msgs"][own:own + 1] if len(rnd["msgs"]) > own else []
            else:
                visible = rnd["msgs"]
            msgs = ",".join(self._fmt(m) for m in visible)
            parts.append(f"r{rnd['index']}@{rnd['x'][player]}:{msgs}?")
        return "|".join(parts)

    def messages(self):
        """All messages sent so far, as a tuple of (m_0, m_1) per finished round."""
        return tuple(tuple(r["msgs"]) for r in self.round_log)

    def adversary_messages(self):
        """The messages M the adversary observes (empty when rho = priv)."""
        return self.messages() if self.g.rho == "pub" else ()

    def team_private_info(self):
        """Teammates' base information states at the start of each finished round.

        This is the default X in the leakage I(M; X): what each teammate knew
        when it sent its messages. For a round right after the deal it is the
        teammates' private cards.
        """
        return tuple(tuple(r["x"][p] for p in self.g.team) for r in self.round_log)

    def __str__(self):
        key = "" if self.key is None else f"key={self.key} "
        return f"{key}msgs={self.messages()} base=[{self.inner}]"


class AugmentedObserver:
    """Observer returning ``AugmentedState.information_state`` strings."""

    def __init__(self):
        self.tensor = np.zeros(0, np.float32)
        self.dict = {}

    def set_from(self, state, player):
        pass

    def string_from(self, state, player):
        return state.information_state(player)


pyspiel.register_game(_GAME_TYPE, AugmentedGame)


def game_parameter(game):
    """OpenSpiel game-typed parameter (a dict with "name") for a game or game string."""
    if isinstance(game, str):
        game = pyspiel.load_game(game)
    return {"name": game.get_type().short_name, **game.get_parameters()}


def make_augmented_game(base_game, k, s, rho, team=(0, 1), adversary=2,
                        rounds=(0,), simultaneous=True):
    """Build Gamma(k, s, rho) (Definition 1) from a base game string.

    ``base_game`` is a game string such as "kuhn_poker(players=3)" or a loaded
    game. ``s`` may be an int or ``float('inf')`` / ``"inf"``; infinity means no key
    node (the solver supplies the correlation device). ``rounds`` lists the
    chance phases after which a communication round happens.
    """
    if s in (float("inf"), "inf", None):
        s = INF
    params = {
        "base_game": game_parameter(base_game),
        "team0": int(team[0]),
        "team1": int(team[1]),
        "adversary": int(adversary),
        "k": int(k),
        "s": int(s),
        "rho": rho,
        "rounds": _format_rounds(rounds),
        "simultaneous": bool(simultaneous),
    }
    return pyspiel.load_game("augmented_team_game", params)
