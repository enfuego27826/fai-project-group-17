"""Perfect recall check for an extracted game tree (Definition 1 requires it)."""


def perfect_recall_violations(tree):
    """Return {player: [(information state, reason), ...]} for players without perfect recall.

    A player has perfect recall if all histories in each of its information
    sets share the same sequence of the player's own (information set, action)
    pairs, and the same legal actions. ``games.tree.build_tree`` records every
    history that breaks this; an empty dict means perfect recall holds.
    """
    return {info.player: list(info.recall_violations)
            for info in tree.players if info.recall_violations}


def has_perfect_recall(tree):
    """True iff every player has perfect recall in ``tree``."""
    return not perfect_recall_violations(tree)
