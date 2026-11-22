"""Full-communication game: the team merged into one player (for V_Com).

V_Com in the report is the team's value when the two teammates can share
everything, i.e. when one player sees both teammates' information and makes
both teammates' moves. This module builds that two-player zero-sum game from
any 3-player base game directly, without the transformation in
``games.augment``, so V_Com is an independent check of the augmented games.

Players of the merged game: 0 = the team (merged), 1 = the adversary. The
team's information state at a team node is the seat that is about to move
together with both teammates' base information states, so the merged player
has perfect recall whenever the base game has. Payoffs: team utility is the
sum of the two teammates' returns, the adversary gets its own return.

Only the small part of the ``pyspiel.State`` interface that ``games.tree``
uses is implemented, which keeps the module free of game registration.
"""

import pyspiel

TEAM, ADVERSARY = 0, 1


class MergedTeamGame:
    """Gamma with teammates ``team`` merged into player 0 and ``adversary`` as player 1."""

    def __init__(self, base_game, team=(0, 1), adversary=2):
        if isinstance(base_game, str):
            base_game = pyspiel.load_game(base_game)
        if base_game.num_players() != 3 or len({*team, adversary}) != 3:
            raise ValueError("need a 3-player base game with two teammates and one adversary")
        self.base_game = base_game
        self.team = tuple(team)
        self.adversary = adversary

    def num_players(self):
        return 2

    def new_initial_state(self):
        return MergedTeamState(self, self.base_game.new_initial_state())


class MergedTeamState:
    """A base-game state seen through the merged team / adversary player split."""

    def __init__(self, game, inner):
        self.game = game
        self.inner = inner

    def clone(self):
        return MergedTeamState(self.game, self.inner.clone())

    def is_terminal(self):
        return self.inner.is_terminal()

    def is_chance_node(self):
        return self.inner.is_chance_node()

    def chance_outcomes(self):
        return self.inner.chance_outcomes()

    def apply_action(self, action):
        self.inner.apply_action(action)

    def current_player(self):
        p = self.inner.current_player()
        if p in self.game.team:
            return TEAM
        if p == self.game.adversary:
            return ADVERSARY
        return p  # chance / terminal ids

    def legal_actions(self, player=None):
        return self.inner.legal_actions()

    def information_state_string(self, player):
        g, inner = self.game, self.inner
        if player == ADVERSARY:
            return inner.information_state_string(g.adversary)
        seat = inner.current_player()
        both = "#".join(inner.information_state_string(p) for p in g.team)
        return f"seat={seat}|{both}"

    def returns(self):
        r = self.inner.returns()
        return [r[self.game.team[0]] + r[self.game.team[1]], r[self.game.adversary]]
