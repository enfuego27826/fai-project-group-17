"""Explicit game tree in sequence form, extracted once from an OpenSpiel game.

Solvers and exact evaluators work on this structure instead of OpenSpiel
states, because they need many passes over the tree. Learning code should keep
using the OpenSpiel game itself.

Sequences. For player p, sequence 0 is the empty sequence and every other
sequence is a pair (information set I, action a). Information sets get ids in
depth-first discovery order, so the parent sequence of an information set
always belongs to an information set with a smaller id (or is empty). Walking
information sets in decreasing id order is therefore a valid bottom-up order.
"""

from dataclasses import dataclass, field

import numpy as np
import pyspiel


@dataclass
class PlayerSeqs:
    """Information sets and sequences of one player."""

    player: int
    infoset_keys: list = field(default_factory=list)       # information state strings
    infoset_index: dict = field(default_factory=dict)      # key -> infoset id
    infoset_actions: list = field(default_factory=list)    # legal actions per infoset
    infoset_parent_seq: list = field(default_factory=list)  # parent sequence per infoset
    infoset_first_seq: list = field(default_factory=list)  # seqs of I: first .. first+|A|-1
    seq_infoset: list = field(default_factory=lambda: [-1])
    seq_action: list = field(default_factory=lambda: [-1])
    recall_violations: list = field(default_factory=list)  # (key, reason)

    @property
    def num_infosets(self):
        return len(self.infoset_keys)

    @property
    def num_seqs(self):
        return len(self.seq_infoset)

    def _infoset(self, key, actions, parent_seq):
        idx = self.infoset_index.get(key)
        if idx is None:
            idx = self.num_infosets
            self.infoset_index[key] = idx
            self.infoset_keys.append(key)
            self.infoset_actions.append(list(actions))
            self.infoset_parent_seq.append(parent_seq)
            self.infoset_first_seq.append(self.num_seqs)
            self.seq_infoset.extend([idx] * len(actions))
            self.seq_action.extend(actions)
            return idx
        if self.infoset_parent_seq[idx] != parent_seq:
            self.recall_violations.append((key, "different own action/observation history"))
        if self.infoset_actions[idx] != list(actions):
            self.recall_violations.append((key, "different legal actions"))
        return idx

    def finalize(self):
        """Convert list fields to numpy arrays once the tree is complete."""
        self.infoset_parent_seq = np.asarray(self.infoset_parent_seq, dtype=np.int64)
        self.infoset_first_seq = np.asarray(self.infoset_first_seq, dtype=np.int64)
        self.infoset_num_actions = np.asarray(
            [len(a) for a in self.infoset_actions], dtype=np.int64)
        self.seq_infoset = np.asarray(self.seq_infoset, dtype=np.int64)
        self.seq_action = np.asarray(self.seq_action, dtype=np.int64)

    def seqs_of(self, infoset):
        """Sequence ids (I, a) for all actions a at information set ``infoset``."""
        first = self.infoset_first_seq[infoset]
        return range(first, first + len(self.infoset_actions[infoset]))


@dataclass
class GameTree:
    """Terminal histories with chance reach, team utility and per-player sequences.

    ``term_u`` is the team utility u_T(z), defined as minus the adversary's
    return (for 3-player Kuhn this equals the sum of the teammates' returns).
    """

    num_players: int
    team: tuple
    adversary: int
    players: list
    term_seq: np.ndarray       # (Z, num_players) last sequence of each player
    term_chance: np.ndarray    # (Z,) chance reach probability p_c(z)
    term_returns: np.ndarray   # (Z, num_players)
    term_u: np.ndarray         # (Z,) team utility u_T(z)
    term_labels: list          # optional per-terminal labels (see build_tree)
    num_nodes: int

    @property
    def num_terminals(self):
        return len(self.term_u)

    def num_infosets(self, player):
        """Number of information sets of ``player`` (all decision points, incl. messages)."""
        return self.players[player].num_infosets


def build_tree(game, team=(0, 1), adversary=2, label_fn=None):
    """Extract the explicit sequence-form tree of ``game``.

    ``label_fn(state)``, if given, is called at each terminal state and its
    result stored in ``term_labels`` (used e.g. for leakage, which needs the
    messages and private information along each terminal history).
    Perfect recall is not enforced here; violations are recorded per player
    and checked by ``eval.perfect_recall``.
    """
    n = game.num_players()
    players = [PlayerSeqs(p) for p in range(n)]
    term_seq, term_chance, term_returns, labels = [], [], [], []
    num_nodes = 0

    # Iterative DFS. The last child reuses the parent state to save a clone.
    stack = [(game.new_initial_state(), 1.0, (0,) * n)]
    while stack:
        state, reach, seqs = stack.pop()
        num_nodes += 1
        if state.is_terminal():
            term_seq.append(seqs)
            term_chance.append(reach)
            term_returns.append(state.returns())
            if label_fn is not None:
                labels.append(label_fn(state))
            continue
        if state.is_chance_node():
            branches = [(a, reach * p, seqs) for a, p in state.chance_outcomes() if p > 0]
        else:
            p = state.current_player()
            actions = state.legal_actions(p)
            info = players[p]
            idx = info._infoset(state.information_state_string(p), actions, seqs[p])
            first = info.infoset_first_seq[idx]
            branches = []
            for j, a in enumerate(actions):
                child_seqs = seqs[:p] + (first + j,) + seqs[p + 1:]
                branches.append((a, reach, child_seqs))
        # Push in reverse so children are expanded in action order (stable infoset ids).
        for i, (a, r, s) in enumerate(reversed(branches)):
            child = state if i == len(branches) - 1 else state.clone()
            child.apply_action(a)
            stack.append((child, r, s))

    for info in players:
        info.finalize()
    term_returns = np.asarray(term_returns, dtype=np.float64)
    return GameTree(
        num_players=n,
        team=tuple(team),
        adversary=adversary,
        players=players,
        term_seq=np.asarray(term_seq, dtype=np.int64).reshape(-1, n),
        term_chance=np.asarray(term_chance, dtype=np.float64),
        term_returns=term_returns,
        term_u=-term_returns[:, adversary],
        term_labels=labels if label_fn is not None else None,
        num_nodes=num_nodes,
    )
