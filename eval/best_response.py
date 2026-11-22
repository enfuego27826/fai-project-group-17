"""Exact adversary best response, guaranteed value g(pi_T) and exploitability.

These are the headline metrics of the report (Preliminaries, "Best responses
and exploitability"): for a team strategy pi_T,

    g(pi_T)    = min_{pi_o} u_T(pi_T, pi_o)
    expl(pi_T) = V(k, s, rho) - g(pi_T).

The adversary is a single perfect-recall player, so the minimum is computed
exactly in one bottom-up pass over its information sets.
"""

from dataclasses import dataclass

import numpy as np

from eval.sequence_form import (best_response, choice_to_plan, leaf_values,
                                realization_plan, team_terminal_weights)


@dataclass
class AdversaryBestResponse:
    value: float   # g(pi_T): team utility when the adversary best-responds
    policy: dict   # adversary pure plan {information state: action}


def adversary_best_response(tree, team_strategy):
    """Exact adversary best response to ``team_strategy`` and the value g(pi_T).

    ``team_strategy`` is a list of (weight, {player: policy}) pairs (see
    ``eval.sequence_form``), so both behavioral team policies and TMECor
    distributions over joint pure plans are supported.
    """
    w = team_terminal_weights(tree, team_strategy)
    adv = tree.players[tree.adversary]
    leaf = leaf_values(tree, tree.adversary, w * tree.term_u)
    value, choice = best_response(adv, leaf, maximize=False)
    return AdversaryBestResponse(float(value), choice_to_plan(adv, choice))


def guaranteed_value(tree, team_strategy):
    """g(pi_T) = min over adversary policies of the team's expected utility u_T."""
    return adversary_best_response(tree, team_strategy).value


def exploitability(tree, team_strategy, value):
    """expl(pi_T) = V - g(pi_T), with V = V(k, s, rho) of the game ``tree``."""
    return value - guaranteed_value(tree, team_strategy)


def expected_team_utility(tree, team_strategy, adversary_policy):
    """u_T(pi_T, pi_o): expected team utility against a given adversary policy."""
    w = team_terminal_weights(tree, team_strategy)
    r = realization_plan(tree.players[tree.adversary], adversary_policy)
    return float(np.sum(w * r[tree.term_seq[:, tree.adversary]] * tree.term_u))
