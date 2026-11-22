"""Team policy gradient against an exact best-responding adversary (Milestone 3).

Each teammate has an independent tabular softmax policy over its own
information states of Gamma(k, s, rho); these include the key and the
messages the teammate has seen, so execution is decentralized. There is no
correlation device: finite s only.

One iteration:
1. compute the adversary's exact best response to the current team policy
   (``eval.sequence_form.best_response``: one bottom-up pass), which also
   gives the guaranteed value g(pi_T) of the current policy;
2. sample a batch of episodes of Gamma(k, s, rho) with the team policy, chance
   and the best-responding adversary;
3. update both teammates with REINFORCE on the team payoff u_T, with the batch
   mean as baseline: theta += lr * mean_b[(u_b - mean u) * grad log pi_T(z_b)].

This is a stochastic subgradient method on g(pi_T) (Danskin): the gradient of
u_T(pi_T, BR(pi_T)) with the best response held fixed is a subgradient of g.

``opponent="learning"`` is the self-play baseline: the adversary is a tabular
softmax policy too and is updated by REINFORCE on -u_T from the same episodes;
the team never sees a best response during training. g(pi_T) is still computed
exactly (for the learning curve and the final evaluation), never the reward
against the training adversary.

Milestone 5 adds two opt-in adversaries (the defaults are unchanged):
* ``opponent="noisy_br"``: in each episode the adversary plays the exact best
  response with probability 1 - epsilon and the uniform policy otherwise
  (realization plan (1 - eps) y_BR + eps y_uniform). epsilon = 0 is the main
  method, bit for bit.
* ``opponent="model"``: an opponent-model adversary. Every ``model_every``
  team iterations it estimates the team's behavioral policy at every team
  information state from the last ``model_window`` sampled episodes and plays
  the exact best response to that estimate until the next refit. It assumes
  everything private is revealed when an episode ends (as at a poker
  showdown), so each episode shows the actions taken at the team information
  states it passed through, key included. Unvisited information states are
  modelled as uniform. It never sees the team's true policy.

Milestone 6 adds two more opt-in modes (the defaults are unchanged):
* two-timescale self-play (``opponent="learning"``): the adversary's step size
  is ``adv_lr_mult`` times the team's, and it makes ``adv_steps`` updates per
  team update. The extra ``adv_steps - 1`` updates come first, each on a fresh
  batch played by the current team and adversary, and touch only the
  adversary; the last batch updates both sides as before.
* ``exact_gradient=True`` (``opponent="best_response"``): the sampled
  REINFORCE step is replaced by its expectation over the exact terminal
  distribution, sum_z p(z) (u(z) - E u) grad log pi_T(z), which is the exact
  gradient of u_T(pi_T, BR(pi_T)) with the best response held fixed, i.e. a
  subgradient of g(pi_T) (Danskin). No episodes are sampled.

Milestone 8 adds opt-in logging (``resp_every`` > 0, evaluation only, no random
numbers drawn, so the training trajectory is unchanged): every ``resp_every``
iterations, the responsiveness gap r_t = u_T(pi_T^t, pi_o^t) - g(pi_T^t), where
pi_o^t is the realization plan the training adversary actually plays in that
iteration (for the noisy best response, the mixture), and the exact leakage
I(M; X) of the current team policy.

Episodes are sampled from the exact terminal distribution of the explicit
tree (``games.tree``), which is the same distribution as playing the game out.
Learning code uses only the game tree and the evaluator, never solver code.
"""

from dataclasses import dataclass, field

import numpy as np

from eval.sequence_form import best_response


@dataclass
class PGConfig:
    iterations: int = 3000
    batch: int = 256
    lr: float = 0.5
    log_every: int = 25
    init_scale: float = 0.0       # std of initial logits (0 = uniform policy)
    lr_decay: str = "const"       # "const" or "sqrt": lr_t = lr / sqrt(t + 1)
    entropy: float = 0.0          # entropy bonus beta_0, annealed linearly to 0 over the run
    track_g: bool = True          # compute g(pi_T) for the learning curve (evaluation only)
    epsilon: float = 0.0          # opponent="noisy_br": P(adversary plays uniform instead of BR)
    model_window: int = 512       # opponent="model": episodes N used to estimate the team policy
    model_every: int = 10         # opponent="model": refit the model every T team iterations
    adv_lr_mult: float = 1.0      # opponent="learning": adversary step size = adv_lr_mult * lr
    adv_steps: int = 1            # opponent="learning": adversary updates per team update
    exact_gradient: bool = False  # opponent="best_response": exact subgradient of g, no sampling
    resp_every: int = 0           # > 0: log responsiveness gap and leakage every this many iterations


@dataclass
class PGResult:
    policies: dict                 # {teammate: {information state: {action: prob}}}
    curve: list = field(default_factory=list)   # (iteration, episodes, g(pi_T))
    final_g: float = None          # g(pi_T) of the final policy (learner's own computation)
    episodes: int = 0
    avg_policies: dict = None      # linearly averaged policy (per teammate, in sequence form)
    avg_curve: list = field(default_factory=list)  # (iteration, episodes, g(average policy))
    theta: list = None             # final logits per teammate (for warm starts)
    resp_log: list = None          # (iteration, r_t, leakage_t, g_t) if cfg.resp_every > 0


class _Player:
    """Tabular softmax policy of one teammate, stored per sequence (I, a)."""

    def __init__(self, info, rng, init_scale):
        self.info = info
        self.theta = np.zeros(info.num_seqs)
        if init_scale > 0:
            self.theta[1:] = rng.normal(0.0, init_scale, info.num_seqs - 1)
        self.first = info.infoset_first_seq
        self.nact = info.infoset_num_actions
        # infoset of every sequence (-1 for the empty sequence)
        self.seq_infoset = info.seq_infoset

    def probs(self):
        """pi(a | I) for every sequence (I, a); entry 0 (empty sequence) is 1."""
        p = np.ones(self.info.num_seqs)
        for I in range(self.info.num_infosets):
            sl = slice(self.first[I], self.first[I] + self.nact[I])
            z = self.theta[sl] - self.theta[sl].max()
            e = np.exp(z)
            p[sl] = e / e.sum()
        return p

    def realization(self, p):
        r = np.zeros(self.info.num_seqs)
        r[0] = 1.0
        for I in range(self.info.num_infosets):  # parents come first
            sl = slice(self.first[I], self.first[I] + self.nact[I])
            r[sl] = r[self.info.infoset_parent_seq[I]] * p[sl]
        return r

    def entropy_grad(self, p):
        """Gradient of sum_I H(pi(. | I)) with respect to the logits."""
        g = np.zeros_like(self.theta)
        logp = np.log(np.maximum(p, 1e-300))
        for I in range(self.info.num_infosets):
            sl = slice(self.first[I], self.first[I] + self.nact[I])
            h = -(p[sl] * logp[sl]).sum()
            g[sl] = -p[sl] * (logp[sl] + h)
        return g

    def policy_dict(self, p):
        out = {}
        for I, key in enumerate(self.info.infoset_keys):
            acts = self.info.infoset_actions[I]
            out[key] = {int(a): float(p[self.first[I] + j]) for j, a in enumerate(acts)}
        return out


def _paths(tree, player):
    """(Z, D) array of the player's sequences on the path to each terminal (-1 padded)."""
    info = tree.players[player]
    seqs = []
    for s in tree.term_seq[:, player]:
        path = []
        while s != 0:
            path.append(s)
            s = info.infoset_parent_seq[info.seq_infoset[s]]
        seqs.append(path)
    depth = max(1, max(len(p) for p in seqs))
    out = np.full((len(seqs), depth), -1, dtype=np.int64)
    for z, p in enumerate(seqs):
        out[z, :len(p)] = p
    return out


def _pure_realization(info, choice):
    x = np.zeros(info.num_seqs)
    x[0] = 1.0
    for I in range(info.num_infosets):
        x[info.infoset_first_seq[I] + choice[I]] = x[info.infoset_parent_seq[I]]
    return x


def guaranteed_value_and_br(tree, r0, r1):
    """g(pi_T) and the adversary's best-response realization plan, from team realization plans."""
    t0, t1 = tree.team
    adv = tree.players[tree.adversary]
    w = tree.term_chance * tree.term_u * r0[tree.term_seq[:, t0]] * r1[tree.term_seq[:, t1]]
    leaf = np.bincount(tree.term_seq[:, tree.adversary], weights=w, minlength=adv.num_seqs)
    value, choice = best_response(adv, leaf, maximize=False)
    return float(value), _pure_realization(adv, choice)


def _update(pl, p, path, zs, weights, lr):
    """REINFORCE step theta += lr * sum_b w_b grad log pi(path of z_b)."""
    P = path[zs]                                   # (B, D)
    mask = P >= 0
    seqs = P[mask]
    a = np.broadcast_to(weights[:, None], P.shape)[mask]
    grad = np.zeros_like(pl.theta)
    np.add.at(grad, seqs, a)                       # + e_a
    per_infoset = np.zeros(pl.info.num_infosets)
    np.add.at(per_infoset, pl.seq_infoset[seqs], a)
    grad[1:] -= per_infoset[pl.seq_infoset[1:]] * p[1:]   # - pi(. | I) on the path
    pl.theta += lr * grad


def behavioral_from_realization(info, r):
    """pi(a | I) = r(I, a) / r(parent(I)), uniform where the parent has zero mass."""
    p = np.ones(info.num_seqs)
    for I in range(info.num_infosets):
        first, n = info.infoset_first_seq[I], info.infoset_num_actions[I]
        tot = r[first:first + n].sum()
        p[first:first + n] = r[first:first + n] / tot if tot > 1e-300 else 1.0 / n
    return p


def uniform_realization(info):
    """Realization plan of the uniform behavioral policy."""
    r = np.zeros(info.num_seqs)
    r[0] = 1.0
    for I in range(info.num_infosets):
        first, n = info.infoset_first_seq[I], info.infoset_num_actions[I]
        r[first:first + n] = r[info.infoset_parent_seq[I]] / n
    return r


def realization_from_counts(info, path, zs):
    """Realization plan of the empirical behavioral policy seen in episodes ``zs``.

    pi_hat(a | I) = #(episodes taking a at I) / #(episodes reaching I), uniform at
    information states no episode reached. ``path`` is ``_paths(tree, player)``.
    """
    counts = np.zeros(info.num_seqs)
    if len(zs):
        P = path[zs]
        np.add.at(counts, P[P >= 0], 1.0)
    p = np.ones(info.num_seqs)
    for I in range(info.num_infosets):
        first, n = info.infoset_first_seq[I], info.infoset_num_actions[I]
        tot = counts[first:first + n].sum()
        p[first:first + n] = counts[first:first + n] / tot if tot > 0 else 1.0 / n
    r = np.zeros(info.num_seqs)
    r[0] = 1.0
    for I in range(info.num_infosets):
        sl = slice(info.infoset_first_seq[I], info.infoset_first_seq[I] + info.infoset_num_actions[I])
        r[sl] = r[info.infoset_parent_seq[I]] * p[sl]
    return r


def train(tree, cfg, seed, opponent="best_response", fixed_y=None, init_theta=None):
    """Train both teammates of ``tree`` (Gamma(k, s, rho), finite s).

    ``opponent``: "best_response" (main method, exact BR each iteration),
    "learning" (self-play: the adversary learns by policy gradient as well), or
    "fixed" (the adversary plays the fixed realization plan ``fixed_y``, e.g. a
    PSRO meta-mixture; no best response is used in training).

    Besides the last iterate, the result holds the linearly averaged policy
    (weights proportional to t): each teammate's realization plans are averaged
    separately and converted back to behavioral form. Averaging each teammate on
    its own keeps the team uncorrelated, as finite s requires; averaging joint
    profiles would need a correlation device.
    """
    if opponent not in ("best_response", "learning", "fixed", "noisy_br", "model"):
        raise ValueError(opponent)
    rng = np.random.default_rng(seed)
    t0, t1 = tree.team
    players = [_Player(tree.players[t], rng, cfg.init_scale) for t in (t0, t1)]
    if init_theta is not None:
        for pl, th in zip(players, init_theta):
            pl.theta = th.copy()
    paths = [_paths(tree, t) for t in (t0, t1)]
    adv = _Player(tree.players[tree.adversary], rng, cfg.init_scale)
    adv_path = _paths(tree, tree.adversary)
    s_team = [tree.term_seq[:, t] for t in (t0, t1)]
    so = tree.term_seq[:, tree.adversary]
    curve, avg_curve = [], []
    episodes = 0
    avg_r = [np.zeros(pl.info.num_seqs) for pl in players]
    avg_w = 0.0
    if opponent == "noisy_br":
        y_unif = uniform_realization(tree.players[tree.adversary])
    if opponent == "model":
        window = np.zeros(0, dtype=np.int64)        # terminals of the last N episodes
    if cfg.exact_gradient:
        all_z = np.arange(len(tree.term_u))
    resp_log = None
    if cfg.resp_every > 0:
        from eval.leakage import LeakageIndex
        leak_index, resp_log = LeakageIndex(tree), []
    for it in range(cfg.iterations + 1):
        probs = [pl.probs() for pl in players]
        reals = [pl.realization(p) for pl, p in zip(players, probs)]
        w_it = it + 1.0                              # linear averaging weights
        for acc, r in zip(avg_r, reals):
            acc += w_it * r
        avg_w += w_it
        log_now = it % cfg.log_every == 0 or it == cfg.iterations
        if opponent in ("best_response", "noisy_br") or (cfg.track_g and log_now):
            g, y_br = guaranteed_value_and_br(tree, *reals)
        if cfg.track_g and log_now:
            curve.append((it, episodes, g))
            g_avg, _ = guaranteed_value_and_br(tree, *(acc / avg_w for acc in avg_r))
            avg_curve.append((it, episodes, g_avg))
        if it == cfg.iterations:
            break
        if opponent == "best_response":
            y = y_br
        elif opponent == "learning":
            adv_p = adv.probs()
            y = adv.realization(adv_p)
        elif opponent == "noisy_br":
            y = y_br if cfg.epsilon == 0 else (1.0 - cfg.epsilon) * y_br + cfg.epsilon * y_unif
        elif opponent == "model":
            if it % cfg.model_every == 0:
                est = [realization_from_counts(tree.players[t], path, window)
                       for t, path in zip((t0, t1), paths)]
                _, y_model = guaranteed_value_and_br(tree, *est)
            y = y_model
        else:
            y = fixed_y
        if opponent == "learning" and cfg.adv_steps > 1:
            adv_lr = cfg.adv_lr_mult * (cfg.lr if cfg.lr_decay == "const" else cfg.lr / np.sqrt(it + 1.0))
            for _ in range(cfg.adv_steps - 1):     # adversary-only updates on fresh batches
                pz = tree.term_chance * reals[0][s_team[0]] * reals[1][s_team[1]] * y[so]
                pz = np.maximum(pz, 0.0)
                pz /= pz.sum()
                zs = rng.choice(len(pz), size=cfg.batch, p=pz)
                episodes += cfg.batch
                u = tree.term_u[zs]
                _update(adv, adv_p, adv_path, zs, -(u - u.mean()) / cfg.batch, adv_lr)
                adv_p = adv.probs()
                y = adv.realization(adv_p)
        if resp_log is not None and it % cfg.resp_every == 0:
            g_t, _ = guaranteed_value_and_br(tree, *reals)
            u_t = float((tree.term_chance * tree.term_u * reals[0][s_team[0]]
                         * reals[1][s_team[1]] * y[so]).sum())
            resp_log.append((it, u_t - g_t, leak_index.mi(*reals), g_t))
        if cfg.exact_gradient:
            if opponent != "best_response":
                raise ValueError("exact_gradient needs opponent='best_response'")
            pz = tree.term_chance * reals[0][s_team[0]] * reals[1][s_team[1]] * y[so]
            u = tree.term_u
            weights = pz * (u - (pz * u).sum())
            lr = cfg.lr if cfg.lr_decay == "const" else cfg.lr / np.sqrt(it + 1.0)
            for pl, p, path in zip(players, probs, paths):
                _update(pl, p, path, all_z, weights, lr)
            continue
        # Episodes against the adversary (exact best response, learning adversary, or fixed).
        pz = tree.term_chance * reals[0][s_team[0]] * reals[1][s_team[1]] * y[so]
        pz = np.maximum(pz, 0.0)
        pz /= pz.sum()
        zs = rng.choice(len(pz), size=cfg.batch, p=pz)
        episodes += cfg.batch
        if opponent == "model":
            window = np.concatenate([window, zs])[-cfg.model_window:]
        u = tree.term_u[zs]
        adv_w = (u - u.mean()) / cfg.batch
        lr = cfg.lr if cfg.lr_decay == "const" else cfg.lr / np.sqrt(it + 1.0)
        beta = cfg.entropy * (1.0 - it / cfg.iterations)
        for pl, p, path in zip(players, probs, paths):
            _update(pl, p, path, zs, adv_w, lr)
            if beta > 0:
                pl.theta += lr * beta * pl.entropy_grad(p)
        if opponent == "learning":
            _update(adv, adv_p, adv_path, zs, -adv_w, cfg.adv_lr_mult * lr)
            if beta > 0:
                adv.theta += lr * beta * adv.entropy_grad(adv_p)
    if resp_log is not None:                         # final policy: leakage and g, no adversary
        g_t, _ = guaranteed_value_and_br(tree, *reals)
        resp_log.append((cfg.iterations, None, leak_index.mi(*reals), g_t))
    probs = [pl.probs() for pl in players]
    policies = {t: pl.policy_dict(p) for t, pl, p in zip((t0, t1), players, probs)}
    avg_policies = {t: pl.policy_dict(behavioral_from_realization(pl.info, acc / avg_w))
                    for t, pl, acc in zip((t0, t1), players, avg_r)}
    return PGResult(policies=policies, curve=curve,
                    final_g=curve[-1][2] if curve else None, episodes=episodes,
                    avg_policies=avg_policies, avg_curve=avg_curve,
                    theta=[pl.theta.copy() for pl in players], resp_log=resp_log)


def train_adversary(tree, cfg, seed, team_weight):
    """Adversary best response by REINFORCE against a fixed team strategy (for PSRO).

    ``team_weight[z]`` is the team's reach probability of terminal z (for example
    a meta-mixture of team policies). Returns the adversary's realization plan
    and behavioral policy. No exact best response is used.
    """
    rng = np.random.default_rng(seed)
    adv = _Player(tree.players[tree.adversary], rng, cfg.init_scale)
    path = _paths(tree, tree.adversary)
    so = tree.term_seq[:, tree.adversary]
    base = tree.term_chance * team_weight
    for it in range(cfg.iterations):
        p = adv.probs()
        y = adv.realization(p)
        pz = np.maximum(base * y[so], 0.0)
        pz /= pz.sum()
        zs = rng.choice(len(pz), size=cfg.batch, p=pz)
        u = -tree.term_u[zs]
        lr = cfg.lr if cfg.lr_decay == "const" else cfg.lr / np.sqrt(it + 1.0)
        _update(adv, p, path, zs, (u - u.mean()) / cfg.batch, lr)
    p = adv.probs()
    return adv.realization(p), adv.policy_dict(p)
