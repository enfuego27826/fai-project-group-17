"""Neural team policy gradient on one-round signaling games (Milestone 6, Task 3).

Each teammate is one MLP (two hidden layers of 64, tanh) whose input is the
one-hot of its own private information, its key bits (0/1), the one-hot of the
two messages it has seen (zero before the round) and a phase flag. The output
has 2^k message logits and one logit per action; the illegal half is masked.
So the policy must generalize across keys and messages instead of storing a
separate table entry for each information state.

Training is REINFORCE on the team payoff with the batch-mean baseline and Adam,
exactly the Milestone 3 objective with a different policy class. Adversaries:

* ``best_response``: the exact best response to the current team policy
  (``eval.onestep``), recomputed every iteration;
* ``model``: the opponent model of Milestone 5 refit every iteration: the
  empirical team policy of the last ``model_window`` episodes (everything is
  revealed at the end of an episode; unvisited states uniform) and the exact
  best response to it;
* ``learning``: self-play against an MLP adversary (input: one-hot of both
  messages on a public channel, a constant on a private one) trained by
  REINFORCE on -u_T with step ``adv_lr_mult`` x the team's and ``adv_steps``
  updates per team update (Task 1's timescales).

``policy="tabular"`` is a control: the same training loop with a tabular softmax
per information state and plain SGD (the Milestone 3 learner), to separate the
effect of the policy class from the effect of the larger game.

g(pi_T) is always from the exact best response (``eval.onestep``), never the
reward against the training adversary. Learning code imports only evaluators.
"""

from dataclasses import dataclass, field

import numpy as np

from eval import onestep


@dataclass
class NeuralConfig:
    iterations: int = 5000
    batch: int = 256
    lr: float = 3e-3              # Adam step size
    hidden: int = 64
    log_every: int = 100
    policy: str = "mlp"           # "mlp", or "tabular" (control; lr is then the SGD step)
    adv_lr_mult: float = 1.0      # opponent="learning"
    adv_steps: int = 1            # opponent="learning"
    model_window: int = 2048      # opponent="model"
    # Milestone 7 (all opt-in; the defaults are the Milestone 6 learner bit for bit)
    init_scale: float = 0.0       # policy="tabular": initial logits iid N(0, init_scale^2)
    entropy: float = 0.0          # MLP: entropy bonus on the message head, annealed linearly to 0
    value_baseline: bool = False  # MLP: learned state-value baseline (own MLP) instead of batch mean
    ppo_epochs: int = 0           # MLP: > 0 = PPO-style clipped updates, this many epochs per batch
    ppo_clip: float = 0.2
    adv_hidden: int = 0           # opponent="learning": adversary width (0 = same as hidden)


@dataclass
class NeuralResult:
    tables: onestep.TeamPolicy
    curve: list = field(default_factory=list)   # (iteration, episodes, g(pi_T))
    episodes: int = 0


class MLP:
    """x -> tanh(W1 x) -> tanh(W2 h) -> W3 h, trained with Adam (gradient ascent)."""

    def __init__(self, n_in, n_out, hidden, rng, lr):
        def glorot(a, b):
            return rng.normal(0.0, np.sqrt(2.0 / (a + b)), (a, b))
        self.params = [glorot(n_in, hidden), np.zeros(hidden), glorot(hidden, hidden),
                       np.zeros(hidden), np.zeros((hidden, n_out)), np.zeros(n_out)]
        self.m = [np.zeros_like(p) for p in self.params]
        self.v = [np.zeros_like(p) for p in self.params]
        self.t = 0
        self.lr = lr

    def forward(self, x):
        W1, b1, W2, b2, W3, b3 = self.params
        h1 = np.tanh(x @ W1 + b1)
        h2 = np.tanh(h1 @ W2 + b2)
        return h2 @ W3 + b3, (x, h1, h2)

    def grads(self, cache, dout):
        """Gradient of sum(dout * output) with respect to the parameters (backpropagation)."""
        x, h1, h2 = cache
        W1, b1, W2, b2, W3, b3 = self.params
        gW3, gb3 = h2.T @ dout, dout.sum(0)
        d2 = (dout @ W3.T) * (1 - h2 ** 2)
        gW2, gb2 = h1.T @ d2, d2.sum(0)
        d1 = (d2 @ W2.T) * (1 - h1 ** 2)
        gW1, gb1 = x.T @ d1, d1.sum(0)
        return gW1, gb1, gW2, gb2, gW3, gb3

    def ascend(self, cache, dout):
        """One Adam step along d(objective)/d(output) = ``dout`` (rows = inputs in ``cache``)."""
        self.t += 1
        b1c, b2c = 1 - 0.9 ** self.t, 1 - 0.999 ** self.t
        for p, g, m, v in zip(self.params, self.grads(cache, dout), self.m, self.v):
            m *= 0.9
            m += 0.1 * g
            v *= 0.999
            v += 0.001 * g * g
            p += self.lr * (m / b1c) / (np.sqrt(v / b2c) + 1e-8)


def _softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


class Teammate:
    """One MLP; information states are (phase, K, own x, m0, m1)."""

    def __init__(self, n_x, n_act, k, s, hidden, rng, lr, value_baseline=False):
        self.n_x, self.n_act, self.M, self.nK, self.s = n_x, n_act, 2 ** k, 2 ** s, s
        self.n_in = n_x + s + 2 * self.M + 1
        self.net = MLP(self.n_in, self.M + n_act, hidden, rng, lr)
        self.vnet = MLP(self.n_in, 1, hidden, rng, lr) if value_baseline else None
        K = np.arange(self.nK)
        self.key_bits = ((K[:, None] >> np.arange(s)[None, :]) & 1).astype(float)
        # all message-phase inputs (K, x) and action-phase inputs (K, x, m0, m1), row-major
        self.msg_x = self.features(*np.meshgrid(K, np.arange(n_x), indexing="ij"), None, None)
        if n_act > 1:
            grid = np.meshgrid(K, np.arange(n_x), np.arange(self.M), np.arange(self.M), indexing="ij")
            self.act_x = self.features(*grid)

    def features(self, K, x, m0, m1):
        K, x = np.ravel(K), np.ravel(x)
        f = np.zeros((len(K), self.n_in))
        f[np.arange(len(K)), x] = 1.0
        f[:, self.n_x:self.n_x + self.s] = self.key_bits[K]
        if m0 is not None:
            m0, m1 = np.ravel(m0), np.ravel(m1)
            o = self.n_x + self.s
            f[np.arange(len(K)), o + m0] = 1.0
            f[np.arange(len(K)), o + self.M + m1] = 1.0
            f[:, -1] = 1.0
        return f

    def tables(self):
        zm, _ = self.net.forward(self.msg_x)
        msg = _softmax(zm[:, :self.M]).reshape(self.nK, self.n_x, self.M)
        if self.n_act == 1:                       # no action after the round (blocker sender)
            return msg, np.ones((self.nK, self.n_x, self.M, self.M, 1))
        za, _ = self.net.forward(self.act_x)
        act = _softmax(za[:, self.M:]).reshape(self.nK, self.n_x, self.M, self.M, self.n_act)
        return msg, act

    def update(self, K, x, m_own, m0, m1, a, msg_p, act_p, w, u=None, entropy=0.0,
               ppo_epochs=0, ppo_clip=0.2):
        """REINFORCE: ascend sum_b w_b grad log pi(m_own | K, x) pi(a | K, x, m0, m1).

        Milestone 7 options: ``u`` (raw payoffs) with a value network replaces w by
        (u - V(state)) / B at each decision and fits V by least squares; ``entropy``
        adds beta * grad H(pi(. | K, x)) / B on the message head; ``ppo_epochs`` > 0
        replaces the single step by that many clipped-surrogate Adam steps on the batch.
        """
        f = np.concatenate([self.features(K, x, None, None), self.features(K, x, m0, m1)])
        if self.vnet is not None or entropy > 0 or ppo_epochs > 0:
            return self._update_m7(f, K, x, m_own, m0, m1, a, msg_p, act_p, w, u, entropy,
                                   ppo_epochs, ppo_clip)
        _, cache = self.net.forward(f)
        B = len(K)
        d = np.zeros((2 * B, self.M + self.n_act))
        pm = msg_p[K, x]                                  # (B, M)
        d[:B, :self.M] = -pm * w[:, None]
        d[np.arange(B), m_own] += w
        if self.n_act > 1:
            pa = act_p[K, x, m0, m1]                      # (B, n_act)
            d[B:, self.M:] = -pa * w[:, None]
            d[B + np.arange(B), self.M + a] += w
        self.net.ascend(cache, d)


    def _update_m7(self, f, K, x, m_own, m0, m1, a, msg_p, act_p, w, u, entropy, ppo_epochs,
                   ppo_clip):
        B, M = len(K), self.M
        act_rows = self.n_act > 1
        if self.vnet is not None:                # per-decision advantage u - V(state)
            v, vcache = self.vnet.forward(f)
            v = v[:, 0]
            adv = (np.concatenate([u, u]) - v) / B
            self.vnet.ascend(vcache, ((np.concatenate([u, u]) - v) / B)[:, None])
        else:
            adv = np.concatenate([w, w])
        chosen = np.concatenate([m_own, M + a])
        old = np.concatenate([msg_p[K, x][np.arange(B), m_own],
                              act_p[K, x, m0, m1][np.arange(B), a] if act_rows else np.ones(B)])
        for _ in range(max(1, ppo_epochs)):
            z, cache = self.net.forward(f)
            p = np.zeros_like(z)
            p[:B, :M] = _softmax(z[:B, :M])
            p[B:, M:] = _softmax(z[B:, M:])
            onehot = np.zeros_like(z)
            onehot[np.arange(2 * B), chosen] = 1.0
            coef = adv.copy()
            if ppo_epochs > 0:                   # clipped surrogate min(r A, clip(r) A)
                r = p[np.arange(2 * B), chosen] / old
                coef = coef * r
                coef[((adv > 0) & (r > 1 + ppo_clip)) | ((adv < 0) & (r < 1 - ppo_clip))] = 0.0
            d = coef[:, None] * (onehot - p)
            d[:B, M:] = 0.0
            d[B:, :M] = 0.0
            if not act_rows:
                d[B:] = 0.0
            if entropy > 0:                      # + beta * grad H on the message head
                pm = p[:B, :M]
                logp = np.log(np.maximum(pm, 1e-300))
                h = -(pm * logp).sum(1, keepdims=True)
                d[:B, :M] += entropy * (-pm * (logp + h)) / B
            self.net.ascend(cache, d)


class TabularTeammate:
    """Control: a tabular softmax policy over the same information states, plain SGD
    REINFORCE as in Milestones 3 to 5 (no generalization across keys or messages)."""

    def __init__(self, n_x, n_act, k, s, lr, rng=None, init_scale=0.0):
        self.n_act, self.M, self.nK, self.lr = n_act, 2 ** k, 2 ** s, lr
        self.msg = np.zeros((self.nK, n_x, self.M))
        self.act = np.zeros((self.nK, n_x, self.M, self.M, n_act))
        if init_scale > 0:                       # Milestone 7: break the uniform start
            self.msg += rng.normal(0.0, init_scale, self.msg.shape)
            if n_act > 1:
                self.act += rng.normal(0.0, init_scale, self.act.shape)

    def tables(self):
        return _softmax(self.msg), _softmax(self.act)

    def update(self, K, x, m_own, m0, m1, a, msg_p, act_p, w):
        g = -msg_p[K, x] * w[:, None]
        g[np.arange(len(K)), m_own] += w
        np.add.at(self.msg, (K, x), self.lr * g)
        if self.n_act > 1:
            g = -act_p[K, x, m0, m1] * w[:, None]
            g[np.arange(len(K)), a] += w
            np.add.at(self.act, (K, x, m0, m1), self.lr * g)


def _sample(rng, p):
    """One draw per row of the probability array ``p`` (last axis)."""
    c = p.cumsum(axis=-1)
    u = rng.random(p.shape[:-1])[..., None] * c[..., -1:]
    return np.minimum((u > c).sum(axis=-1), p.shape[-1] - 1)


class Adversary:
    """REINFORCE adversary: an MLP over (m0, m1) on a public channel, a constant input otherwise."""

    def __init__(self, game, k, rho, hidden, rng, lr):
        self.M, self.rho, self.n = 2 ** k, rho, game.n_block
        self.n_in = 2 * self.M if rho == "pub" else 1
        self.net = MLP(self.n_in, self.n, hidden, rng, lr)
        m0, m1 = np.meshgrid(np.arange(self.M), np.arange(self.M), indexing="ij")
        self.all_x = self.features(m0.ravel(), m1.ravel())

    def features(self, m0, m1):
        f = np.zeros((len(m0), self.n_in))
        if self.rho == "pub":
            f[np.arange(len(m0)), m0] = 1.0
            f[np.arange(len(m0)), self.M + m1] = 1.0
        else:
            f[:, 0] = 1.0
        return f

    def table(self):
        z, _ = self.net.forward(self.all_x)
        return _softmax(z).reshape(self.M, self.M, self.n)

    def update(self, m0, m1, b, p, w):
        _, cache = self.net.forward(self.features(m0, m1))
        d = -p[m0, m1] * w[:, None]
        d[np.arange(len(b)), b] += w
        self.net.ascend(cache, d)


class _Model:
    """Counts of the team's actions in the last ``window`` episodes (opponent model)."""

    def __init__(self, game, k, s, window):
        M, nK = 2 ** k, 2 ** s
        self.c = [np.zeros((nK, game.n0, M)), np.zeros((nK, game.n1, M)),
                  np.zeros((nK, game.n0, M, M, game.n_act0)),
                  np.zeros((nK, game.n1, M, M, game.n_act1))]
        self.window, self.buf = window, []

    def add(self, ep):
        """Add a batch of episodes and forget everything older than the last ``window``."""
        self.buf.append(ep)
        self._count(ep, 1.0)
        extra = sum(len(e[0]) for e in self.buf) - self.window
        while extra > 0:
            old = self.buf[0]
            drop = min(extra, len(old[0]))
            self._count(tuple(v[:drop] for v in old), -1.0)
            if drop == len(old[0]):
                self.buf.pop(0)
            else:
                self.buf[0] = tuple(v[drop:] for v in old)
            extra -= drop

    def _count(self, ep, sign):
        K, x0, x1, m0, m1, a0, a1 = ep
        np.add.at(self.c[0], (K, x0, m0), sign)
        np.add.at(self.c[1], (K, x1, m1), sign)
        np.add.at(self.c[2], (K, x0, m0, m1, a0), sign)
        np.add.at(self.c[3], (K, x1, m0, m1, a1), sign)

    def policy(self):
        out = []
        for c in self.c:
            tot = c.sum(axis=-1, keepdims=True)
            out.append(np.where(tot > 0, c / np.maximum(tot, 1e-300), 1.0 / c.shape[-1]))
        return onestep.TeamPolicy(*out)


def train(game, k, s, rho, cfg, seed, opponent="best_response"):
    """Train both teammates' MLPs on Gamma(k, s, rho) of ``game`` (finite s, one round)."""
    if opponent not in ("best_response", "model", "learning"):
        raise ValueError(opponent)
    rng = np.random.default_rng(seed)
    if cfg.policy == "tabular":
        t0 = TabularTeammate(game.n0, game.n_act0, k, s, cfg.lr, rng, cfg.init_scale)
        t1 = TabularTeammate(game.n1, game.n_act1, k, s, cfg.lr, rng, cfg.init_scale)
    else:
        t0 = Teammate(game.n0, game.n_act0, k, s, cfg.hidden, rng, cfg.lr, cfg.value_baseline)
        t1 = Teammate(game.n1, game.n_act1, k, s, cfg.hidden, rng, cfg.lr, cfg.value_baseline)
    adv = (Adversary(game, k, rho, cfg.adv_hidden or cfg.hidden, rng, cfg.adv_lr_mult * cfg.lr)
           if opponent == "learning" else None)
    model = _Model(game, k, s, cfg.model_window) if opponent == "model" else None
    nK, B = 2 ** s, cfg.batch
    curve, episodes = [], 0
    for it in range(cfg.iterations + 1):
        msg0, act0 = t0.tables()
        msg1, act1 = t1.tables()
        pol = onestep.TeamPolicy(msg0, msg1, act0, act1)
        if opponent == "best_response" or it % cfg.log_every == 0 or it == cfg.iterations:
            g, br = onestep.guaranteed_value(game, pol, rho)
            if it % cfg.log_every == 0 or it == cfg.iterations:
                curve.append((it, episodes, g))
        if it == cfg.iterations:
            break
        if opponent == "model":
            _, br = onestep.guaranteed_value(game, model.policy(), rho)

        def play(adv_table=None):
            K = rng.integers(nK, size=B)
            x0 = rng.integers(game.n0, size=B)
            x1 = rng.integers(game.n1, size=B)
            m0 = _sample(rng, msg0[K, x0])
            m1 = _sample(rng, msg1[K, x1])
            b = br[m0, m1] if adv_table is None else _sample(rng, adv_table[m0, m1])
            a0 = _sample(rng, act0[K, x0, m0, m1])
            a1 = _sample(rng, act1[K, x1, m0, m1])
            u = ((a0 == game.target0[x0, x1]) & (a1 == game.target1[x0, x1])
                 & (b != game.cls[x0, x1])).astype(float)
            return K, x0, x1, m0, m1, a0, a1, b, u

        adv_table = None
        if opponent == "learning":
            for _ in range(cfg.adv_steps - 1):            # adversary-only updates
                adv_table = adv.table()
                *_, m0, m1, _, _, b, u = play(adv_table)
                episodes += B
                adv.update(m0, m1, b, adv_table, -(u - u.mean()) / B)
            adv_table = adv.table()
        K, x0, x1, m0, m1, a0, a1, b, u = play(adv_table)
        episodes += B
        w = (u - u.mean()) / B
        if cfg.policy == "tabular":
            t0.update(K, x0, m0, m0, m1, a0, msg0, act0, w)
            t1.update(K, x1, m1, m0, m1, a1, msg1, act1, w)
        else:
            beta = cfg.entropy * (1.0 - it / cfg.iterations)
            m7 = dict(u=u, entropy=beta, ppo_epochs=cfg.ppo_epochs, ppo_clip=cfg.ppo_clip)
            t0.update(K, x0, m0, m0, m1, a0, msg0, act0, w, **m7)
            t1.update(K, x1, m1, m0, m1, a1, msg1, act1, w, **m7)
        if opponent == "learning":
            adv.update(m0, m1, b, adv_table, -w)
        if opponent == "model":
            model.add((K, x0, x1, m0, m1, a0, a1))
    return NeuralResult(tables=pol, curve=curve, episodes=episodes)
