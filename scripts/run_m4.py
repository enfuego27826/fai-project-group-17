"""Milestone 4 experiments: several learners, iterate averaging, PSRO, more seeds, Kuhn.

Usage:
    nice -n 19 .venv/bin/python scripts/run_m4.py --config configs/m4_selfplay.yaml

Generalizes scripts/run_marl.py (which is kept unchanged for Milestone 3):
* ``methods`` is a list of learner specs, e.g.
  {name, trainer: pg, opponent: best_response | learning, lr, lr_decay, entropy,
   outputs: [last, avg]} or {name, trainer: psro, ...}. Each output variant
  (last iterate, averaged policy, PSRO's chosen policy) is evaluated and
  reported as its own row "name/output".
* ``exact_values`` may be numbers or [lower, upper] intervals (for cells that
  are only bounded); ``exact_values_from`` loads them from another config.
* a game may list ``cells: [[k, s, rho], ...]`` instead of the k x s x rho grid.
Every value is g(pi_T) from the exact best response; 95% confidence intervals
use Student's t over seeds. The run stops if any g exceeds the upper end of
its cell's exact value (a bug).
"""

import os
import sys
from pathlib import Path

os.environ["FAI_THREADS"] = "1"
for var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[var] = "1"
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import argparse  # noqa: E402
import json  # noqa: E402
import platform  # noqa: E402
import time  # noqa: E402
from multiprocessing import Pool  # noqa: E402

import numpy as np  # noqa: E402
import yaml  # noqa: E402
from scipy import stats  # noqa: E402

import games  # noqa: E402,F401
from eval.best_response import guaranteed_value  # noqa: E402
from eval.leakage import mutual_information  # noqa: E402
from learning.psro import PSROConfig, train_psro  # noqa: E402
from learning.tabular_pg import PGConfig, train  # noqa: E402
from run_marl import behavior, frac, tree_of  # noqa: E402
from run_values import config_hash, git_info  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CFG = None


def _init(cfg):
    global CFG
    CFG = cfg


def cells_of(g):
    if "cells" in g:
        return [tuple(c) for c in g["cells"]]
    return [(k, s, rho) for k in g["k"] for s in g["s"] for rho in g["rho"]]


def v_range(cfg, game, k, s, rho):
    v = cfg["exact_values"][game][f"{k},{s},{rho}"]
    return (float(v[0]), float(v[1])) if isinstance(v, (list, tuple)) else (float(v), float(v))


def run_one(task):
    mi, gi, k, s, rho, seed = task
    m, g = CFG["methods"][mi], CFG["games"][gi]
    tree = tree_of(g, k, s, rho)
    t0 = time.perf_counter()
    outputs = {}
    if m["trainer"] == "pg":
        res = train(tree, PGConfig(iterations=m["iterations"], batch=m["batch"], lr=m["lr"],
                                   log_every=m.get("log_every", 50),
                                   lr_decay=m.get("lr_decay", "const"),
                                   entropy=m.get("entropy", 0.0)),
                    seed=seed, opponent=m["opponent"])
        if "last" in m["outputs"]:
            outputs["last"] = (res.policies, res.curve)
        if "avg" in m["outputs"]:
            outputs["avg"] = (res.avg_policies, res.avg_curve)
        episodes = res.episodes
    elif m["trainer"] == "psro":
        res = train_psro(tree, PSROConfig(iterations=m["iterations"],
                                          br_iterations=m["br_iterations"], batch=m["batch"],
                                          lr=m["lr"]), seed=seed)
        outputs["single"] = (res.policies, res.curve)
        episodes = res.episodes
    else:
        raise ValueError(m["trainer"])
    seconds = time.perf_counter() - t0
    out = []
    for oname, (pol, curve) in outputs.items():
        strategy = [(1.0, pol)]
        g_val = guaranteed_value(tree, strategy)
        leak = mutual_information(tree, strategy, channel="all")
        g_priv = guaranteed_value(tree_of(g, k, s, "priv"), strategy) if rho == "pub" else g_val
        out.append({"method": f"{m['name']}/{oname}", "game": g["name"], "k": k, "s": s,
                    "rho": rho, "seed": seed, "g": g_val, "leak_bits": leak,
                    "g_same_policy_priv": g_priv, "seconds": seconds, "episodes": episodes,
                    "curve": curve, "policies": {str(p): v for p, v in pol.items()}})
    return out


def summarize(cfg, runs):
    cells = {}
    for r in runs:
        cells.setdefault((r["method"], r["game"], r["k"], r["s"], r["rho"]), []).append(r)
    rows, checks = [], []
    for (method, game, k, s, rho), rs in cells.items():
        lo, hi = v_range(cfg, game, k, s, rho)
        gs = np.array([r["g"] for r in rs])
        n = len(gs)
        half = stats.t.ppf(0.975, n - 1) * gs.std(ddof=1) / np.sqrt(n) if n > 1 else float("nan")
        leaks = np.array([r["leak_bits"] for r in rs])
        cost = np.array([r["g_same_policy_priv"] - r["g"] for r in rs])
        rows.append({"method": method, "game": game, "k": k, "s": s, "rho": rho, "V_lo": lo,
                     "V_hi": hi, "g_mean": gs.mean(), "g_ci95": half, "g_std": gs.std(ddof=1)
                     if n > 1 else 0.0, "gap_mean": hi - gs.mean(), "leak_mean": leaks.mean(),
                     "cost_mean": cost.mean(), "seeds": n,
                     "seconds": float(np.mean([r["seconds"] for r in rs]))})
        if lo == hi and game in ("attack2x2", "blocker4"):
            v_priv = v_range(cfg, game, k, s, "priv")[0]
            for r in sorted(rs, key=lambda r: r["seed"]):
                b = behavior(r, lo, v_priv)
                if b:
                    checks.append((method, game, k, s, rho, r["seed"], *b))
    return rows, checks


def fmt_v(lo, hi):
    return frac(lo) if lo == hi else f"[{frac(lo)}, {frac(hi)}]"


def format_tables(rows, checks):
    lines = ["| method | game | k | s | ρ | exact V | g(π_T) mean ± 95% CI | gap to V (upper) | "
             "leak bits | cost of leak | seeds | time/run |", "|" + "---|" * 12]
    for r in rows:
        cost = f"{r['cost_mean']:.3f}" if r["rho"] == "pub" else ""
        lines.append(
            f"| {r['method']} | {r['game']} | {r['k']} | {r['s']} | {r['rho']} "
            f"| {fmt_v(r['V_lo'], r['V_hi'])} | {r['g_mean']:.3f} ± {r['g_ci95']:.3f} "
            f"| {r['gap_mean']:.3f} | {r['leak_mean']:.2f} | {cost} | {r['seeds']} "
            f"| {r['seconds']:.1f}s |")
    if checks:
        tally = {}
        for method, game, k, s, rho, seed, name, ok, desc in checks:
            key = (method, game, k, s, rho, name)
            tally.setdefault(key, []).append(ok)
        lines += ["", "| method | game | k | s | ρ | check | yes / seeds |", "|" + "---|" * 7]
        for (method, game, k, s, rho, name), oks in tally.items():
            lines.append(f"| {method} | {game} | {k} | {s} | {rho} | {name} | {sum(oks)} / {len(oks)} |")
        lines += ["", "| method | game | k | s | ρ | seed | check | yes/no | what the policy does |",
                  "|" + "---|" * 9]
        for method, game, k, s, rho, seed, name, ok, desc in checks:
            lines.append(f"| {method} | {game} | {k} | {s} | {rho} | {seed} | {name} "
                         f"| {'yes' if ok else 'no'} | {desc} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    if "exact_values_from" in cfg:
        src = yaml.safe_load((ROOT / cfg["exact_values_from"]).read_text())["exact_values"]
        cfg["exact_values"] = {**src, **cfg.get("exact_values", {})}
    out = ROOT / "results" / cfg["experiment"] / config_hash(cfg) / "seeds"
    (out / "runs").mkdir(parents=True, exist_ok=True)
    (out / "config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    (out / "run_info.json").write_text(json.dumps({
        **git_info(), "python": platform.python_version(), "workers": cfg["workers"],
        "threads_per_worker": 1, "started": time.strftime("%Y-%m-%d %H:%M:%S"),
        "argv": sys.argv}, indent=2))
    tasks = [(mi, gi, k, s, rho, seed) for mi in range(len(cfg["methods"]))
             for gi, g in enumerate(cfg["games"]) for (k, s, rho) in cells_of(g)
             for seed in cfg["seeds"]]
    # Longest tasks first keeps the workers busy.
    tasks.sort(key=lambda t: -(cfg["methods"][t[0]]["trainer"] == "psro") - t[2] - t[3])
    t0 = time.perf_counter()
    runs = []
    with Pool(cfg["workers"], initializer=_init, initargs=(cfg,)) as pool:
        for outs in pool.imap_unordered(run_one, tasks):
            for r in outs:
                lo, hi = v_range(cfg, r["game"], r["k"], r["s"], r["rho"])
                if r["g"] > hi + 1e-6:
                    pool.terminate()
                    raise RuntimeError(f"g = {r['g']} exceeds V <= {hi} in {r['game']} k={r['k']} "
                                       f"s={r['s']} {r['rho']} seed {r['seed']} ({r['method']}): bug")
                name = (f"{r['method'].replace('/', '-')}_{r['game']}_k{r['k']}_s{r['s']}_"
                        f"{r['rho']}_seed{r['seed']}.json")
                (out / "runs" / name).write_text(json.dumps(r))
                runs.append(r)
                print(f"{r['method']:22s} {r['game']:9s} k={r['k']} s={r['s']} {r['rho']:4s} "
                      f"seed {r['seed']:2d}  g={r['g']:+.4f}  V<={hi:+.4f}  "
                      f"leak={r['leak_bits']:.3f}  ({r['seconds']:.1f}s)", flush=True)
    wall = time.perf_counter() - t0
    morder = {m["name"]: i for i, m in enumerate(cfg["methods"])}
    corder = {(g["name"], *c): i for i, (g, c) in enumerate(
        (g, c) for g in cfg["games"] for c in cells_of(g))}
    runs.sort(key=lambda r: (morder[r["method"].split("/")[0]], r["method"],
                             corder[(r["game"], r["k"], r["s"], r["rho"])], r["seed"]))
    rows, checks = summarize(cfg, runs)
    table = format_tables(rows, checks)
    (out / "metrics.json").write_text(json.dumps(
        {"cells": rows, "checks": checks, "wall_seconds": wall}, indent=2, default=float))
    (out / "summary.md").write_text(table + f"\n\nwall time {wall:.0f} s for {len(tasks)} runs\n")
    print()
    print(table)
    print(f"\nwall time {wall:.0f} s for {len(tasks)} runs; results in {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
