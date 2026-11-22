"""Neural team policy gradient on one-round games (learning.neural_pg, Milestone 6)."""

import numpy as np

from eval import onestep
from learning.neural_pg import MLP, NeuralConfig, _Model, train


def test_backprop_matches_finite_differences():
    rng = np.random.default_rng(0)
    net = MLP(5, 3, 8, rng, 1e-3)
    net.params[4] = rng.normal(size=net.params[4].shape)   # nonzero last layer
    x = rng.normal(size=(4, 5))
    dout = rng.normal(size=(4, 3))
    out, cache = net.forward(x)
    grads = net.grads(cache, dout)
    for p, g in zip(net.params, grads):
        fd = np.zeros_like(p)
        for idx in np.ndindex(p.shape):
            old = p[idx]
            p[idx] = old + 1e-6
            up = (net.forward(x)[0] * dout).sum()
            p[idx] = old - 1e-6
            down = (net.forward(x)[0] * dout).sum()
            p[idx] = old
            fd[idx] = (up - down) / 2e-6
        assert np.allclose(g, fd, atol=1e-6)


def test_model_window_keeps_last_n_episodes():
    game = onestep.card_blocker(4)
    model = _Model(game, 1, 1, window=100)
    rng = np.random.default_rng(0)
    for _ in range(5):
        B = 64
        ep = tuple(rng.integers(n, size=B) for n in (2, 4, 1, 2, 2, 1, 4))
        model.add(ep)
    assert model.c[0].sum() == 100 and model.c[3].sum() == 100
    pol = model.policy()
    assert np.allclose(pol.msg0.sum(-1), 1) and np.allclose(pol.act1.sum(-1), 1)


def test_learners_respect_value_and_tabular_learns_private_code():
    game = onestep.card_blocker(4)
    for opp in ("best_response", "model", "learning"):
        r = train(game, 2, 2, "pub", NeuralConfig(iterations=200, log_every=100), seed=0, opponent=opp)
        g, _ = onestep.guaranteed_value(game, r.tables, "pub")
        assert g <= 0.75 + 1e-9 and abs(g - r.curve[-1][2]) < 1e-12
    r = train(game, 2, 0, "priv", NeuralConfig(iterations=1500, lr=8.0, policy="tabular"), seed=0)
    assert r.curve[-1][2] > 0.7


def test_m7_options_run_and_respect_value():
    """Milestone 7 options: entropy, value baseline, PPO, tabular random init; g exact and <= V."""
    game = onestep.card_blocker(4)
    for kw in (dict(entropy=0.05), dict(value_baseline=True), dict(ppo_epochs=4),
               dict(ppo_epochs=4, entropy=0.05), dict(policy="tabular", lr=8.0, init_scale=1.0)):
        cfg = NeuralConfig(**{**dict(iterations=200, log_every=100), **kw})
        r = train(game, 2, 0, "priv", cfg, seed=0)
        g, _ = onestep.guaranteed_value(game, r.tables, "priv")
        assert g <= 0.75 + 1e-9 and abs(g - r.curve[-1][2]) < 1e-12


def test_ppo_one_epoch_is_reinforce():
    """One PPO epoch starts at ratio 1, so it takes the plain REINFORCE step."""
    game = onestep.card_blocker(4)
    a = train(game, 2, 1, "pub", NeuralConfig(iterations=50, log_every=25), seed=1)
    b = train(game, 2, 1, "pub", NeuralConfig(iterations=50, log_every=25, ppo_epochs=1), seed=1)
    assert np.allclose(a.tables.msg0, b.tables.msg0, atol=1e-10)
    assert np.allclose(a.tables.act1, b.tables.act1, atol=1e-10)
