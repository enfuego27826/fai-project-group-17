"""Milestone 6, task 3: neural team policies on larger games, evaluated exactly.

Usage:
    nice -n 19 .venv/bin/python scripts/run_m6.py --config configs/m6_neural.yaml
    nice -n 19 .venv/bin/python scripts/run_m6.py --config configs/m6_neural_tune.yaml

Games are the one-round blocker, suit blocker and coordinated attack at larger
sizes (``eval.onestep``, checked against the tree evaluators in
tests/test_onestep.py). Targets (lower and upper bound, label) come from
scripts/m6_targets.py. Each run trains ``learning.neural_pg`` and reports the
exact g(pi_T), the gap to the target, I(M; X), I(M; c(X)) and I(M; c(X) | K),
and the pad / suit-pad / reaches-target checks. The run stops if any g exceeds
the upper end of its target (a bug). Milestone 7 adds the opt-in method fields
init_scale, entropy, value_baseline, ppo_epochs / ppo_clip, batch and hidden.
"""

import os
import sys
from pathlib import Path

for var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[var] = "1"
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import argparse  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import platform  # noqa: E402
import time  # noqa: E402
from multiprocessing import Pool  # noqa: E402

import numpy as np  # noqa: E402
import yaml  # noqa: E402
from scipy import stats  # noqa: E402

import m6_targets  # noqa: E402
from eval import onestep  # noqa: E402
from learning.neural_pg import NeuralConfig, train  # noqa: E402
from run_values import config_hash, git_info  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CFG = None
TARGETS = None

GAMES = {"blocker16": lambda: onestep.card_blocker(16),
         "suit4x4": lambda: onestep.suit_blocker(4, 4),
         "attack4x4": lambda: onestep.coordinated_attack(4, 4)}


def _init(cfg, targets):
    global CFG, TARGETS
    CFG, TARGETS = cfg, targets


def load_targets():
    return {(r["game"], r["k"], r["s"], r["rho"]): r for r in m6_targets.targets()}


def run_one(task):
    mi, name, k, s, rho, seed = task
    m = CFG["methods"][mi]
    game = GAMES[name]()
    cfg = NeuralConfig(iterations=CFG["iterations"], batch=CFG["batch"], lr=m.get("lr", CFG["lr"]),
                       hidden=CFG["hidden"], log_every=CFG["log_every"],
                       adv_lr_mult=m.get("adv_lr_mult", 1.0), adv_steps=m.get("adv_steps", 1),
                       model_window=m.get("model_window", 2048), policy=m.get("policy", "mlp"),
                       init_scale=m.get("init_scale", 0.0), entropy=m.get("entropy", 0.0),
                       value_baseline=m.get("value_baseline", False),
                       ppo_epochs=m.get("ppo_epochs", 0), ppo_clip=m.get("ppo_clip", 0.2))
    if "batch" in m:
        cfg.batch = m["batch"]
    if "hidden" in m:
        cfg.hidden = m["hidden"]
    if "adv_hidden" in m:
        cfg.adv_hidden = m["adv_hidden"]
    t0 = time.perf_counter()
    res = train(game, k, s, rho, cfg, seed=seed, opponent=m["opponent"])
    seconds = time.perf_counter() - t0
    g, _ = onestep.guaranteed_value(game, res.tables, rho)
    g_priv, _ = onestep.guaranteed_value(game, res.tables, "priv")
    i_x, i_c, i_ck = onestep.leakage(game, res.tables)
    out = ROOT / CFG["_out"] / "policies"
    np.savez_compressed(out / f"{m['name']}_{name}_k{k}_s{s}_{rho}_seed{seed}.npz",
                        **{f: getattr(res.tables, f).astype(np.float32)
                           for f in ("msg0", "msg1", "act0", "act1")})
    return {"method": m["name"], "game": name, "k": k, "s": s, "rho": rho, "seed": seed,
            "g": g, "leak_bits": i_x, "leak_exploitable": i_c, "leak_decodable": i_ck,
            "g_same_policy_priv": g_priv, "seconds": seconds, "episodes": res.episodes,
            "curve": res.curve}


def check(r, t, game):
    """(check name, yes/no, description) for one run, or None."""
    lo, hi = t["lo"], t["hi"]
    g, ix, ic, ick = r["g"], r["leak_bits"], r["leak_exploitable"], r["leak_decodable"]
    reach = g >= lo - 0.02
    kind = t.get("check")
    if kind == "pad":
        ok = ix < 0.1 and reach
        return "key as pad", ok, f"g={g:.3f} vs {lo:.3f}; I(M;X)={ix:.2f}"
    if kind == "suit pad":
        S = game.n_block
        R = game.n0 // S
        rank = ix - ic
        rank_txt = ("rank in clear" if rank > math.log2(R) - 0.1 else
                    "no rank" if rank < 0.1 else "rank partly sent")
        suit_txt = ("suit leaks" if ic >= 0.1 else "suit padded" if ick > math.log2(S) - 0.1
                    else "suit not sent" if ick < 0.1 else "suit partly padded")
        ok = suit_txt == "suit padded" and ic < 0.1 and reach
        return "pad suit only", ok, (f"g={g:.3f} vs {lo:.3f}; {suit_txt}, {rank_txt}; "
                                     f"I(M;X)={ix:.2f}, I(M;suit)={ic:.2f}, I(M;suit|K)={ick:.2f}")
    return "reaches best known", reach, f"g={g:.3f} vs {lo:.3f}; I(M;X)={ix:.2f}"


def summarize(cfg, runs, targets):
    cells = {}
    for r in runs:
        cells.setdefault((r["method"], r["game"], r["k"], r["s"], r["rho"]), []).append(r)
    rows, checks = [], []
    for (method, name, k, s, rho), rs in cells.items():
        t = {**targets[(name, k, s, rho)], **cfg["cell_checks"].get(f"{name} {k},{s},{rho}", {})}
        game = GAMES[name]()
        gs = np.array([r["g"] for r in rs])
        n = len(gs)
        half = stats.t.ppf(0.975, n - 1) * gs.std(ddof=1) / np.sqrt(n) if n > 1 else float("nan")
        found = []
        for r in sorted(rs, key=lambda r: r["seed"]):
            c = check(r, t, game)
            found.append(c)
            checks.append((method, name, k, s, rho, r["seed"], *c))
        rows.append({"method": method, "game": name, "k": k, "s": s, "rho": rho,
                     "V_lo": t["lo"], "V_hi": t["hi"], "label": t["label"],
                     "g_mean": gs.mean(), "g_ci95": half, "gap_mean": t["lo"] - gs.mean(),
                     "leak_mean": float(np.mean([r["leak_bits"] for r in rs])),
                     "leak_ex_mean": float(np.mean([r["leak_exploitable"] for r in rs])),
                     "leak_dec_mean": float(np.mean([r["leak_decodable"] for r in rs])),
                     "cost_mean": float(np.mean([r["g_same_policy_priv"] - r["g"] for r in rs])),
                     "check": found[0][0], "check_yes": sum(c[1] for c in found), "seeds": n,
                     "seconds": float(np.mean([r["seconds"] for r in rs]))})
    return rows, checks


def fmt_t(lo, hi):
    return f"{lo:.4f}" if abs(hi - lo) < 1e-9 else f"[{lo:.4f}, {hi:.4f}]"


def format_tables(rows, checks):
    lines = ["| method | game | k | s | ρ | target | label | g(π_T) mean ± 95% CI | gap to lower "
             "| I(M;X) | I(M;c(X)) | I(M;c(X)\\|K) | check | yes / seeds | time/run |",
             "|" + "---|" * 15]
    for r in rows:
        lines.append(
            f"| {r['method']} | {r['game']} | {r['k']} | {r['s']} | {r['rho']} "
            f"| {fmt_t(r['V_lo'], r['V_hi'])} | {r['label']} | {r['g_mean']:.3f} ± {r['g_ci95']:.3f} "
            f"| {r['gap_mean']:.3f} | {r['leak_mean']:.2f} | {r['leak_ex_mean']:.2f} "
            f"| {r['leak_dec_mean']:.2f} | {r['check']} | {r['check_yes']} / {r['seeds']} "
            f"| {r['seconds']:.0f}s |")
    lines += ["", "| method | game | k | s | ρ | seed | check | yes/no | what the policy does |",
              "|" + "---|" * 9]
    for method, name, k, s, rho, seed, cname, ok, desc in checks:
        lines.append(f"| {method} | {name} | {k} | {s} | {rho} | {seed} | {cname} "
                     f"| {'yes' if ok else 'no'} | {desc} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    cfg.setdefault("cell_checks", {})
    targets = load_targets()
    out = ROOT / "results" / cfg["experiment"] / config_hash(cfg) / "seeds"
    (out / "runs").mkdir(parents=True, exist_ok=True)
    (out / "policies").mkdir(exist_ok=True)
    cfg["_out"] = str(out.relative_to(ROOT))
    (out / "config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    (out / "targets.json").write_text(json.dumps({" ".join(map(str, key)): v
                                                  for key, v in targets.items()}, indent=2))
    (out / "run_info.json").write_text(json.dumps({
        **git_info(), "python": platform.python_version(), "workers": cfg["workers"],
        "threads_per_worker": 1, "started": time.strftime("%Y-%m-%d %H:%M:%S"),
        "argv": sys.argv}, indent=2))
    tasks = [(mi, c[0], c[1], c[2], c[3], seed) for mi in range(len(cfg["methods"]))
             for c in cfg["cells"] for seed in cfg["seeds"]]
    tasks.sort(key=lambda t: -(t[2] + t[3]))
    t0 = time.perf_counter()
    runs = []
    with Pool(cfg["workers"], initializer=_init, initargs=(cfg, targets)) as pool:
        for r in pool.imap_unordered(run_one, tasks):
            t = targets[(r["game"], r["k"], r["s"], r["rho"])]
            if r["g"] > t["hi"] + 1e-6:
                pool.terminate()
                raise RuntimeError(f"g = {r['g']} exceeds the target's upper end {t['hi']} "
                                   f"({t['label']}) in {r}: bug")
            name = f"{r['method']}_{r['game']}_k{r['k']}_s{r['s']}_{r['rho']}_seed{r['seed']}.json"
            (out / "runs" / name).write_text(json.dumps(r))
            runs.append(r)
            print(f"{r['method']:14s} {r['game']:9s} k={r['k']} s={r['s']} {r['rho']:4s} "
                  f"seed {r['seed']:2d}  g={r['g']:+.4f}  target={fmt_t(t['lo'], t['hi'])}  "
                  f"leak={r['leak_bits']:.3f}/{r['leak_exploitable']:.3f}  ({r['seconds']:.0f}s)",
                  flush=True)
    wall = time.perf_counter() - t0
    morder = {m["name"]: i for i, m in enumerate(cfg["methods"])}
    corder = {tuple(c): i for i, c in enumerate(cfg["cells"])}
    runs.sort(key=lambda r: (morder[r["method"]], corder[(r["game"], r["k"], r["s"], r["rho"])],
                             r["seed"]))
    rows, checks = summarize(cfg, runs, targets)
    table = format_tables(rows, checks)
    (out / "metrics.json").write_text(json.dumps(
        {"cells": rows, "checks": checks, "wall_seconds": wall}, indent=2, default=float))
    (out / "summary.md").write_text(table + f"\n\nwall time {wall:.0f} s for {len(tasks)} runs\n")
    print()
    print(table)
    print(f"\nwall time {wall:.0f} s for {len(tasks)} runs; results in {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
