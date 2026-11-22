"""Compute exact team values V(k, inf, rho) for the games, k and rho in a config.

Usage:
    nice -n 19 python scripts/run_values.py --config configs/m1_values.yaml --seed 0

Uses at most FAI_THREADS threads (default 2).

Writes results/<experiment>/<config-hash>/<seed>/ with the config, run info
(git commit, versions, backend), metrics.json (one row per game, k, s, rho)
and the solutions (correlation device support and adversary strategy), and
prints a table of values, solve times and information set counts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solvers.threads import limit_threads  # noqa: E402

limit_threads()  # before NumPy/SciPy load BLAS

import argparse
import hashlib
import json
import platform
import random
import subprocess
import time

import numpy as np
import pyspiel
import yaml

ROOT = Path(__file__).resolve().parents[1]

import games  # noqa: E402,F401
from eval.best_response import guaranteed_value  # noqa: E402
from games.augment import make_augmented_game  # noqa: E402
from games.tree import build_tree  # noqa: E402
from solvers.backends import resolve_backend  # noqa: E402
from solvers.threads import num_threads  # noqa: E402
from solvers.tmecor_cg import solve_tmecor  # noqa: E402
from solvers.tmecor_enum import solve_tmecor_enum  # noqa: E402


def config_hash(cfg):
    blob = json.dumps(cfg, sort_keys=True, default=str).encode()
    return hashlib.sha256(blob).hexdigest()[:10]


def git_info():
    def run(*args):
        try:
            return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                                  check=True).stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None
    commit = run("rev-parse", "HEAD") or "uncommitted"
    status = run("status", "--porcelain")
    return {"commit": commit, "dirty": bool(status) if status is not None else None}


def parse_s(s):
    return "inf" if str(s).lower() in ("inf", "infinity", ".inf") or s == float("inf") else int(s)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--config", required=True)
    ap.add_argument("--seed", type=int, default=None, help="overrides the config seed")
    ap.add_argument("--games", nargs="*", help="only these game names")
    ap.add_argument("--k", nargs="*", type=int, help="only these k")
    ap.add_argument("--rho", nargs="*", choices=["priv", "pub"], help="only these visibilities")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    if args.seed is not None:
        cfg["seed"] = args.seed
    if args.games:
        cfg["games"] = [g for g in cfg["games"] if g["name"] in args.games]
    if args.k:
        cfg["k"] = [k for k in cfg["k"] if k in args.k]
    if args.rho:
        cfg["rho"] = [r for r in cfg["rho"] if r in args.rho]
    seed = int(cfg["seed"])
    random.seed(seed)
    np.random.seed(seed)  # all computations here are deterministic; seeded for the convention

    backend = resolve_backend(cfg.get("backend", "auto"))
    out = ROOT / "results" / cfg["experiment"] / config_hash(cfg) / str(seed)
    (out / "solutions").mkdir(parents=True, exist_ok=True)
    (out / "config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    run_info = {
        **git_info(),
        "python": platform.python_version(),
        "open_spiel": getattr(pyspiel, "__version__", None),
        "backend": backend,
        "threads": num_threads(),
        "started": time.strftime("%Y-%m-%d %H:%M:%S"),
        "argv": sys.argv,
    }
    (out / "run_info.json").write_text(json.dumps(run_info, indent=2))

    solver = cfg.get("solver", {})
    rows = []
    for g in cfg["games"]:
        team, adversary = tuple(g["team"]), int(g["adversary"])
        v_cor = None
        if cfg.get("check_independent_v0"):
            base_tree = build_tree(pyspiel.load_game(g["base_game"]), team, adversary)
            v_cor = solve_tmecor_enum(base_tree, backend=backend).value
        for k in cfg["k"]:
            for s in map(parse_s, cfg["s"]):
                if s != "inf":
                    raise NotImplementedError("finite s is not solved in milestone 1 "
                                              "(see solvers/finite_s.py and scripts/run_bounds.py)")
                for rho in cfg["rho"]:
                    t0 = time.perf_counter()
                    game = make_augmented_game(g["base_game"], k=k, s=s, rho=rho, team=team,
                                               adversary=adversary, rounds=g["rounds"],
                                               simultaneous=cfg.get("simultaneous", True))
                    tree = build_tree(game, team, adversary)
                    t1 = time.perf_counter()
                    res = solve_tmecor(tree, backend=backend,
                                       enum_limit=solver.get("enum_limit", 20000),
                                       tol=solver.get("tol", 1e-9),
                                       pricing_time_limit=solver.get("pricing_time_limit"),
                                       seed=seed, verbose=args.verbose)
                    t2 = time.perf_counter()
                    g_val = guaranteed_value(tree, res.support)
                    row = {
                        "game": g["name"], "k": k, "s": s, "rho": rho,
                        "V": res.value, "converged": res.converged,
                        "V_upper_bound": res.upper_bound, "g_of_solution": g_val,
                        "exploitability": res.value - g_val,
                        "V_cor_base": v_cor,
                        "team_infosets": [tree.num_infosets(p) for p in team],
                        "adversary_infosets": tree.num_infosets(adversary),
                        "terminals": tree.num_terminals,
                        "iterations": res.iterations, "columns": res.num_columns,
                        "support_size": len(res.support),
                        "exact_pricing_calls": sum(1 for entry in res.log if entry[3]),
                        "pricing": res.pricing, "backend": res.backend,
                        "build_seconds": t1 - t0, "solve_seconds": t2 - t1,
                        "master_seconds": res.master_seconds,
                        "pricing_seconds": res.pricing_seconds,
                    }
                    rows.append(row)
                    gap = "" if res.converged else f" (NOT converged, V <= {res.upper_bound:+.6f})"
                    print(f"{g['name']:14s} k={k} s={s} {rho:4s} V={res.value:+.6f}{gap} "
                          f"expl={row['exploitability']:.1e} solve={row['solve_seconds']:.1f}s",
                          flush=True)
                    sol = {"support": res.support, "adversary_policy": res.adversary_policy}
                    (out / "solutions" / f"{g['name']}_k{k}_s{s}_{rho}.json").write_text(
                        json.dumps(sol))
                    (out / "metrics.json").write_text(json.dumps(rows, indent=2))

    print()
    print(format_table(rows))
    (out / "summary.md").write_text(format_table(rows) + "\n")
    print(f"\nresults in {out.relative_to(ROOT)}")


def format_table(rows):
    head = ("| game | k | s | rho | V (or [lower, upper]) | V_Cor(base) | expl | team infosets | adv infosets "
            "| iters | solve s |")
    lines = [head, "|" + "---|" * 11]
    for r in rows:
        vcor = "" if r["V_cor_base"] is None else f"{r['V_cor_base']:+.6f}"
        v = (f"{r['V']:+.6f}" if r["converged"]
             else f"[{r['V']:+.6f}, {r['V_upper_bound']:+.6f}]")
        lines.append(
            f"| {r['game']} | {r['k']} | {r['s']} | {r['rho']} | {v} | {vcor} "
            f"| {r['exploitability']:.1e} | {r['team_infosets'][0]} + {r['team_infosets'][1]} "
            f"| {r['adversary_infosets']} | {r['iterations']} | {r['solve_seconds']:.1f} |")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
