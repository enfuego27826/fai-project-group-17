"""Team-PSRO-lite: populations of team and adversary policies, all learned (Milestone 4).

No exact best response is used in training. Each PSRO iteration:
1. evaluate the meta-game M[i, j] = u_T(team_i, adversary_j) (exact expected
   utility of two fixed policies; this is evaluation, not a best response);
2. solve the zero-sum meta-game by a small LP (team maximizes);
3. train a team best response by REINFORCE (both teammates, independent
   tabular softmax policies) against the adversary meta-mixture, and an
   adversary best response by REINFORCE against the team meta-mixture;
4. add both to their populations.

Output. The team meta-mixture is a distribution over joint team policies, i.e.
a correlation device, which finite s does not allow. The reported team
strategy is therefore a single population member: the one with the highest
worst-case payoff against the learned adversary population,
argmax_i min_j M[i, j]. This choice uses only learned opponents. The exact
best response is used afterwards, only to evaluate it.
"""

from dataclasses import dataclass, field

import numpy as np
from scipy.optimize import linprog

from learning.tabular_pg import PGConfig, guaranteed_value_and_br, train, train_adversary


@dataclass
class PSROConfig:
    iterations: int = 10          # PSRO iterations (population grows by one per side each)
    br_iterations: int = 1500     # REINFORCE iterations per best response
    batch: int = 256
    lr: float = 8.0
    track_g: bool = True          # exact g of the chosen output after each iteration (evaluation only)


@dataclass
class PSROResult:
    policies: dict                # chosen single team policy {teammate: {infoset: {a: p}}}
    meta_team: list               # meta-mixture weights over the team population
    curve: list = field(default_factory=list)   # (psro iteration, episodes, exact g of output)
    episodes: int = 0
    population: int = 0


def solve_matrix_game(M):
    """Max-min mixed strategies of the zero-sum matrix game M (row player maximizes)."""
    n, m = M.shape
    shift = M.min() - 1.0
    A = M - shift                                   # positive entries
    # Row player: max v s.t. A^T x >= v, sum x = 1  <=> standard LP in (x, v)
    c = np.zeros(n + 1)
    c[-1] = -1.0
    A_ub = np.hstack([-A.T, np.ones((m, 1))])
    res = linprog(c, A_ub=A_ub, b_ub=np.zeros(m), A_eq=[[1.0] * n + [0.0]], b_eq=[1.0],
                  bounds=[(0, None)] * n + [(None, None)], method="highs")
    x = np.maximum(res.x[:n], 0)
    c2 = np.zeros(m + 1)
    c2[-1] = 1.0
    A_ub2 = np.hstack([A, -np.ones((n, 1))])
    res2 = linprog(c2, A_ub=A_ub2, b_ub=np.zeros(n), A_eq=[[1.0] * m + [0.0]], b_eq=[1.0],
                   bounds=[(0, None)] * m + [(None, None)], method="highs")
    y = np.maximum(res2.x[:m], 0)
    return x / x.sum(), y / y.sum()


def _uniform_team(tree):
    out = []
    for t in tree.team:
        info = tree.players[t]
        r = np.zeros(info.num_seqs)
        r[0] = 1.0
        for I in range(info.num_infosets):
            first, n = info.infoset_first_seq[I], info.infoset_num_actions[I]
            r[first:first + n] = r[info.infoset_parent_seq[I]] / n
        out.append(r)
    return out


def _uniform_adv(tree):
    info = tree.players[tree.adversary]
    r = np.zeros(info.num_seqs)
    r[0] = 1.0
    for I in range(info.num_infosets):
        first, n = info.infoset_first_seq[I], info.infoset_num_actions[I]
        r[first:first + n] = r[info.infoset_parent_seq[I]] / n
    return r


def _uniform_policies(tree):
    return {t: {key: {int(a): 1.0 / len(acts) for a in acts}
                for key, acts in zip(tree.players[t].infoset_keys, tree.players[t].infoset_actions)}
            for t in tree.team}


def train_psro(tree, cfg, seed):
    """Team-PSRO-lite on ``tree`` (Gamma(k, s, rho), finite s)."""
    rng = np.random.default_rng(seed)
    t0, t1 = tree.team
    s0, s1 = tree.term_seq[:, t0], tree.term_seq[:, t1]
    so = tree.term_seq[:, tree.adversary]
    coef = tree.term_chance * tree.term_u

    team_pop = [(_uniform_team(tree), _uniform_policies(tree))]   # (realizations, policies)
    adv_pop = [_uniform_adv(tree)]

    def payoff(team, y):
        r0, r1 = team[0]
        return float(np.sum(coef * r0[s0] * r1[s1] * y[so]))

    M = np.array([[payoff(team_pop[0], adv_pop[0])]])
    br_cfg = PGConfig(iterations=cfg.br_iterations, batch=cfg.batch, lr=cfg.lr, track_g=False)
    curve, episodes = [], 0

    def chosen():
        return int(np.argmax(M.min(axis=1)))

    for it in range(cfg.iterations + 1):
        if cfg.track_g:
            g, _ = guaranteed_value_and_br(tree, *team_pop[chosen()][0])
            curve.append((it, episodes, g))
        if it == cfg.iterations:
            break
        x, y_meta = solve_matrix_game(M)
        y_mix = sum(w * y for w, y in zip(y_meta, adv_pop))
        team_w = sum(w * r0[s0] * r1[s1] for w, ((r0, r1), _) in zip(x, team_pop))
        res = train(tree, br_cfg, int(rng.integers(2 ** 31)), opponent="fixed", fixed_y=y_mix)
        new_team = ([_realization(tree.players[t], res.policies[t]) for t in (t0, t1)],
                    res.policies)
        y_new, _ = train_adversary(tree, br_cfg, int(rng.integers(2 ** 31)), team_w)
        episodes += 2 * cfg.br_iterations * cfg.batch
        team_pop.append(new_team)
        adv_pop.append(y_new)
        n, m = len(team_pop), len(adv_pop)
        M2 = np.zeros((n, m))
        M2[:n - 1, :m - 1] = M
        for i in range(n):
            M2[i, m - 1] = payoff(team_pop[i], adv_pop[m - 1])
        for j in range(m - 1):
            M2[n - 1, j] = payoff(team_pop[n - 1], adv_pop[j])
        M = M2
    x, _ = solve_matrix_game(M)
    return PSROResult(policies=team_pop[chosen()][1], meta_team=[float(v) for v in x],
                      curve=curve, episodes=episodes, population=len(team_pop))


def _realization(info, policy):
    r = np.zeros(info.num_seqs)
    r[0] = 1.0
    for I, key in enumerate(info.infoset_keys):
        first = info.infoset_first_seq[I]
        for j, a in enumerate(info.infoset_actions[I]):
            r[first + j] = r[info.infoset_parent_seq[I]] * policy[key][a]
    return r
