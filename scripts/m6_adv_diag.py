"""Milestone 6, task 1 diagnostic: can a REINFORCE adversary read messages when the team holds still?

Usage:
    nice -n 19 .venv/bin/python scripts/m6_adv_diag.py

For every final team policy of two self-play settings of configs/m6_timescale.yaml
(adv_m1_s1 = Milestone 5's self-play, adv_m1_s4 = the best two-timescale setting),
freeze the team and train a fresh tabular REINFORCE adversary against it alone
(learning.tabular_pg.train_adversary: lr 8, batch 256, 10,000 iterations, the
Milestone 3 to 5 hyperparameters). Report the team's payoff against a uniform
adversary, against the trained adversary, and against the exact best response
g(pi_T), and the fraction of the best response's exploitation the trained
adversary achieves: (u_uniform - u_trained) / (u_uniform - g).
If the fraction is near 1, a policy-gradient adversary can learn to condition on
the messages of a fixed team, and self-play fails because the team moves.
"""

import os
import sys
from pathlib import Path

for var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[var] = "1"
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import glob  # noqa: E402
import json  # noqa: E402

import numpy as np  # noqa: E402
import yaml  # noqa: E402

import games  # noqa: E402,F401
from eval.sequence_form import realization_plan, uniform_policy  # noqa: E402
from learning.tabular_pg import PGConfig, guaranteed_value_and_br, train_adversary  # noqa: E402
from run_marl import tree_of  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def main():
    cfg = yaml.safe_load((ROOT / "configs" / "m6_timescale.yaml").read_text())
    gcfg = {g["name"]: g for g in cfg["games"]}
    run_dir = sorted(glob.glob(str(ROOT / "results" / "m6_timescale" / "*" / "seeds" / "runs")))[-1]
    adv_cfg = PGConfig(iterations=10000, batch=256, lr=8.0)
    rows = {}
    per_run = ["self_play_setting,game,k,s,seed,u_uniform,u_trained_adversary,g_exact_br"]
    for method in ("adv_m1_s1", "adv_m1_s4"):
        for f in sorted(glob.glob(f"{run_dir}/{method}-last_*.json")):
            r = json.load(open(f))
            tree = tree_of(gcfg[r["game"]], r["k"], r["s"], r["rho"])
            t0, t1 = tree.team
            pol = {int(p): {I: {int(a): v for a, v in d.items()} for I, d in P.items()}
                   for p, P in r["policies"].items()}
            r0 = realization_plan(tree.players[t0], pol[t0])
            r1 = realization_plan(tree.players[t1], pol[t1])
            team_w = r0[tree.term_seq[:, t0]] * r1[tree.term_seq[:, t1]]
            so = tree.term_seq[:, tree.adversary]
            g, _ = guaranteed_value_and_br(tree, r0, r1)
            y, _ = train_adversary(tree, adv_cfg, 1000 + r["seed"], team_w)
            y_u = realization_plan(tree.players[tree.adversary], uniform_policy(tree.players[tree.adversary]))
            base = tree.term_chance * tree.term_u * team_w
            u_tr, u_un = float((base * y[so]).sum()), float((base * y_u[so]).sum())
            frac = (u_un - u_tr) / (u_un - g) if u_un - g > 1e-6 else float("nan")
            rows.setdefault((method, r["game"], r["k"], r["s"]), []).append((u_un, u_tr, g, frac))
            per_run.append(f"{method},{r['game']},{r['k']},{r['s']},{r['seed']},{u_un!r},{u_tr!r},{g!r}")
            print(f"{method} {r['game']} k={r['k']} s={r['s']} seed {r['seed']}: u_unif={u_un:.3f} "
                  f"u_trained={u_tr:.3f} g={g:.3f} frac={frac:.2f}", flush=True)
    lines = ["| self-play setting | game | k | s | u vs uniform | u vs trained PG adversary | g (exact BR) "
             "| share of BR exploitation (median) |", "|---|---|---|---|---|---|---|---|"]
    for (method, game, k, s), vals in rows.items():
        a = np.array(vals)
        lines.append(f"| {method} | {game} | {k} | {s} | {a[:, 0].mean():.3f} | {a[:, 1].mean():.3f} "
                     f"| {a[:, 2].mean():.3f} | {np.nanmedian(a[:, 3]):.2f} |")
    text = "\n".join(lines)
    print(text)
    out = ROOT / "results" / "m6_adv_diag"
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.md").write_text(text + "\n")
    (out / "runs.csv").write_text("\n".join(per_run) + "\n")


if __name__ == "__main__":
    main()
