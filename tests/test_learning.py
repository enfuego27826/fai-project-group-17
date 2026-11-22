"""Team policy gradient against an exact best response (learning.tabular_pg)."""

import pytest

import games  # noqa: F401
from games.augment import make_augmented_game
from games.tree import build_tree
from eval.best_response import guaranteed_value
from learning.tabular_pg import PGConfig, train


def test_learner_value_matches_evaluator_and_never_beats_v():
    tree = build_tree(make_augmented_game("coordinated_attack", k=0, s=1, rho="priv"))
    res = train(tree, PGConfig(iterations=300, batch=128, lr=8.0), seed=0)
    g = guaranteed_value(tree, [(1.0, res.policies)])
    assert g == pytest.approx(res.final_g, abs=1e-9)
    assert g <= 3 / 8 + 1e-9
    assert res.curve[0][2] < g                     # learning improves on the uniform policy


def test_learns_card_guessing_code():
    """With 2 private bits the guesser can learn the identity code (V = 1)."""
    tree = build_tree(make_augmented_game("card_guessing(num_cards=4)", k=2, s=0, rho="priv"))
    res = train(tree, PGConfig(iterations=1500, batch=128, lr=8.0), seed=1)
    assert res.final_g > 0.95


def test_reproducible_from_seed():
    tree = build_tree(make_augmented_game("card_blocker(num_cards=4)", k=1, s=1, rho="pub"))
    a = train(tree, PGConfig(iterations=100, batch=64, lr=8.0), seed=3)
    b = train(tree, PGConfig(iterations=100, batch=64, lr=8.0), seed=3)
    assert a.curve == b.curve


def test_self_play_runs_and_respects_v():
    """Self-play baseline: the adversary learns too; g(pi_T) is still exact and <= V."""
    tree = build_tree(make_augmented_game("coordinated_attack", k=1, s=2, rho="pub"))
    res = train(tree, PGConfig(iterations=300, batch=128, lr=8.0), seed=0, opponent="learning")
    g = guaranteed_value(tree, [(1.0, res.policies)])
    assert g == pytest.approx(res.final_g, abs=1e-9) and g <= 0.75 + 1e-9
    with pytest.raises(ValueError):
        train(tree, PGConfig(iterations=1), seed=0, opponent="nobody")


def test_averaged_policy_is_valid_and_evaluated_exactly():
    """Linear iterate averaging: the averaged team strategy is uncorrelated and its g is exact."""
    tree = build_tree(make_augmented_game("card_blocker(num_cards=4)", k=0, s=0, rho="priv"))
    res = train(tree, PGConfig(iterations=400, batch=128, lr=8.0), seed=0)
    g_avg = guaranteed_value(tree, [(1.0, res.avg_policies)])
    assert g_avg == pytest.approx(res.avg_curve[-1][2], abs=1e-9)
    assert g_avg <= 3 / 16 + 1e-9
    for pol in res.avg_policies.values():
        for probs in pol.values():
            assert sum(probs.values()) == pytest.approx(1.0)


def test_decay_and_entropy_options_run():
    tree = build_tree(make_augmented_game("coordinated_attack", k=1, s=1, rho="pub"))
    for cfg in (PGConfig(iterations=200, batch=64, lr=8.0, lr_decay="sqrt"),
                PGConfig(iterations=200, batch=64, lr=8.0, entropy=0.05)):
        res = train(tree, cfg, seed=0)
        assert guaranteed_value(tree, [(1.0, res.policies)]) <= 0.5 + 1e-9


def test_psro_output_is_single_uncorrelated_policy():
    from learning.psro import PSROConfig, solve_matrix_game, train_psro

    x, y = solve_matrix_game(__import__("numpy").array([[1.0, -1.0], [-1.0, 1.0]]))
    assert x == pytest.approx([0.5, 0.5]) and y == pytest.approx([0.5, 0.5])
    tree = build_tree(make_augmented_game("coordinated_attack", k=0, s=1, rho="priv"))
    res = train_psro(tree, PSROConfig(iterations=3, br_iterations=200, batch=64), seed=0)
    assert res.population == 4 and len(res.meta_team) == 4
    g = guaranteed_value(tree, [(1.0, res.policies)])
    assert g <= 3 / 8 + 1e-9 and g == pytest.approx(res.curve[-1][2], abs=1e-9)


def test_noisy_best_response_eps0_is_the_main_method():
    """Milestone 5: epsilon = 0 reproduces PG vs exact BR bit for bit."""
    tree = build_tree(make_augmented_game("card_blocker(num_cards=4)", k=1, s=2, rho="pub"))
    a = train(tree, PGConfig(iterations=100, batch=64, lr=8.0), seed=2)
    b = train(tree, PGConfig(iterations=100, batch=64, lr=8.0, epsilon=0.0), seed=2,
              opponent="noisy_br")
    assert a.curve == b.curve and a.policies == b.policies


@pytest.mark.parametrize("opponent, extra", [("noisy_br", {"epsilon": 0.5}),
                                             ("model", {"model_window": 128, "model_every": 5})])
def test_weaker_adversaries_respect_v(opponent, extra):
    """Noisy-BR and opponent-model adversaries: g(pi_T) is exact and <= V."""
    tree = build_tree(make_augmented_game("coordinated_attack", k=1, s=2, rho="pub"))
    res = train(tree, PGConfig(iterations=200, batch=128, lr=8.0, **extra), seed=0,
                opponent=opponent)
    g = guaranteed_value(tree, [(1.0, res.policies)])
    assert g == pytest.approx(res.final_g, abs=1e-9) and g <= 0.75 + 1e-9


def test_model_from_counts_recovers_policy():
    """The opponent model's estimate converges to the team's true realization plan."""
    import numpy as np
    from learning.tabular_pg import _paths, realization_from_counts
    tree = build_tree(make_augmented_game("card_blocker(num_cards=4)", k=1, s=0, rho="pub"))
    res = train(tree, PGConfig(iterations=50, batch=64, lr=8.0), seed=0)
    from eval.sequence_form import realization_plan
    t0 = tree.team[0]
    r_true = realization_plan(tree.players[t0], res.policies[t0])
    rng = np.random.default_rng(0)
    r1 = realization_plan(tree.players[tree.team[1]], res.policies[tree.team[1]])
    pz = tree.term_chance * r_true[tree.term_seq[:, t0]] * r1[tree.term_seq[:, tree.team[1]]]
    zs = rng.choice(len(pz), size=200_000, p=pz / pz.sum())
    est = realization_from_counts(tree.players[t0], _paths(tree, t0), zs)
    assert np.abs(est - r_true).max() < 0.01


def test_two_timescale_defaults_are_self_play():
    """Milestone 6: adv_lr_mult = 1, adv_steps = 1 is the self-play baseline bit for bit."""
    tree = build_tree(make_augmented_game("card_blocker(num_cards=4)", k=1, s=2, rho="pub"))
    a = train(tree, PGConfig(iterations=100, batch=64, lr=8.0), seed=2, opponent="learning")
    b = train(tree, PGConfig(iterations=100, batch=64, lr=8.0, adv_lr_mult=1.0, adv_steps=1),
              seed=2, opponent="learning")
    assert a.curve == b.curve and a.policies == b.policies
    c = train(tree, PGConfig(iterations=100, batch=64, lr=8.0, adv_lr_mult=4.0, adv_steps=4),
              seed=2, opponent="learning")
    assert c.episodes == 4 * a.episodes and c.final_g <= 3 / 8 + 1e-9


def test_exact_gradient_is_gradient_of_payoff_against_fixed_br():
    """Milestone 6: one exact-gradient step equals lr x the finite-difference gradient of
    u_T(pi_T, y_BR) with the best response y_BR held fixed (Danskin subgradient of g)."""
    import numpy as np
    from learning.tabular_pg import _Player, guaranteed_value_and_br
    tree = build_tree(make_augmented_game("card_blocker(num_cards=4)", k=1, s=1, rho="pub"))
    rng = np.random.default_rng(0)
    players = [_Player(tree.players[t], rng, 1.0) for t in tree.team]
    th0 = [pl.theta.copy() for pl in players]
    reals = [pl.realization(pl.probs()) for pl in players]
    _, y = guaranteed_value_and_br(tree, *reals)
    so, s0, s1 = (tree.term_seq[:, p] for p in (tree.adversary, *tree.team))

    def u(thetas):
        rs = []
        for pl, th in zip(players, thetas):
            pl.theta = th
            rs.append(pl.realization(pl.probs()))
        return float((tree.term_chance * tree.term_u * rs[0][s0] * rs[1][s1] * y[so]).sum())

    lr = 1e-3
    res = train(tree, PGConfig(iterations=1, batch=64, lr=lr, exact_gradient=True,
                               init_scale=1.0, track_g=False), seed=0)
    for i in range(2):
        fd = np.zeros_like(th0[i])
        for j in range(1, len(fd)):
            e = np.zeros_like(fd)
            e[j] = 1e-6
            th_p = [t.copy() for t in th0]
            th_m = [t.copy() for t in th0]
            th_p[i] += e
            th_m[i] -= e
            fd[j] = (u(th_p) - u(th_m)) / 2e-6
        assert np.allclose(res.theta[i] - th0[i], lr * fd, atol=1e-9)
