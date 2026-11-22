"""Values and bounds of V(k, s, rho) for finite and infinite s (Milestone 2).

Usage:
    nice -n 19 .venv/bin/python scripts/run_bounds.py --config configs/m2_values.yaml --seed 0

Uses at most FAI_THREADS threads (default 2). Run one at a time.

For every game and cell (k, s, rho) in the config:

* s = inf: V(k, inf, rho) by TMECor column generation (``solvers.tmecor_cg``).
* finite s: the lower bound L(k, s, rho) over key-indexed joint pure plans
  (``solvers.finite_s.solve_key_pure``; it leaves out private randomization)
  and, where enabled, the exact bilinear solve (``solve_bilinear``), which
  returns the value of its best strategy and a proven upper bound.

Bounds are then combined across cells with Propositions 1 and 2 of the
report, using only what their proofs give: V nondecreasing in k and s,
V(pub) <= V(priv), V(k, inf, pub) = V(k, inf, priv), and
V(k, s, pub) >= V(k, s - 2kR, priv) (one k-bit pad per teammate per round).
Upper bounds proved by hand can be listed in the config.

Each cell is labelled "exact" (a solver proved the value for this cell),
"theorem" (lower and upper bounds meet only after using the propositions
or a hand proof) or "bound". Leakage I(M; X) (bits, all messages, X = the
teammates' private information at the round) is reported for the strategy
that attains the cell's best solver lower bound.

Writes results/<experiment>/<config-hash>/<seed>/ (config, run info,
metrics.json, solutions/, summary.md) and prints the table.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from solvers.threads import limit_threads  # noqa: E402

limit_threads()  # before NumPy/SciPy load BLAS

import argparse  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import platform  # noqa: E402
import random  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import pyspiel  # noqa: E402
import yaml  # noqa: E402

import games  # noqa: E402,F401
from eval.best_response import guaranteed_value  # noqa: E402
from eval.leakage import leakage_labels, mutual_information  # noqa: E402
from games.augment import make_augmented_game  # noqa: E402
from games.merged import MergedTeamGame  # noqa: E402
from games.tree import build_tree  # noqa: E402
from run_values import config_hash, git_info, parse_s  # noqa: E402
from solvers.backends import resolve_backend  # noqa: E402
from solvers.finite_s import solve_bilinear, solve_key_pure  # noqa: E402
from solvers.threads import num_threads  # noqa: E402
from solvers.tmecor_cg import solve_tmecor  # noqa: E402
from solvers.zero_sum_lp import solve_zero_sum  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
INF = math.inf
EPS = 1e-9


def s_value(s):
    return INF if s == "inf" else s


def s_label(s):
    return "inf" if s in (INF, "inf") else str(s)


def v_com_of(g, backend):
    """V_Com of the game: the team merged into one player (games.merged), sequence-form LP."""
    team, adversary = tuple(g["team"]), int(g["adversary"])
    tree = build_tree(MergedTeamGame(g["base_game"], team, adversary), team=(0,), adversary=1)
    return solve_zero_sum(tree, backend=backend).value


def solve_cell(g, k, s, rho, cfg, backend, seed, verbose, v_com=None):
    """Run the solvers configured for one cell; returns (row, solutions)."""
    solver = cfg.get("solver", {})
    team, adversary = tuple(g["team"]), int(g["adversary"])
    t0 = time.perf_counter()
    game = make_augmented_game(g["base_game"], k=k, s=s, rho=rho, team=team,
                               adversary=adversary, rounds=g["rounds"],
                               simultaneous=cfg.get("simultaneous", True))
    tree = build_tree(game, team, adversary, label_fn=leakage_labels)
    row = {
        "game": g["name"], "k": k, "s": s_label(s), "rho": rho,
        "team_infosets": [tree.num_infosets(p) for p in team],
        "adversary_infosets": tree.num_infosets(adversary),
        "terminals": tree.num_terminals,
        "build_seconds": time.perf_counter() - t0,
        "lower": -INF, "upper": INF, "lower_from": None, "upper_from": None,
        "solver_exact": False, "solves": {},
    }
    candidates = []   # (guaranteed value, name, team strategy) for leakage
    solutions = {}

    def lower(value, source, strategy):
        candidates.append((value, source, strategy))
        if value > row["lower"] + EPS:
            row["lower"], row["lower_from"] = value, source

    def upper(value, source):
        if value < row["upper"] - EPS:
            row["upper"], row["upper_from"] = value, source

    if s == "inf":
        res = solve_tmecor(tree, backend=backend, enum_limit=solver.get("enum_limit", 20000),
                           tol=solver.get("tol", 1e-9),
                           pricing_time_limit=solver.get("pricing_time_limit"),
                           seed=seed, verbose=verbose,
                           known_upper=v_com if g.get("stop_at_v_com") else None)
        g_val = guaranteed_value(tree, res.support)
        lower(g_val, "tmecor", res.support)
        if not res.reached_known_upper:
            upper(res.upper_bound, "tmecor")
        row["solver_exact"] = res.converged
        row["solves"]["tmecor"] = {"value": res.value, "upper": res.upper_bound,
                                   "converged": res.converged, "g": g_val,
                                   "support_size": len(res.support),
                                   "iterations": res.iterations,
                                   "seconds": res.master_seconds + res.pricing_seconds}
        solutions["tmecor"] = {"support": res.support, "adversary_policy": res.adversary_policy}
    else:
        tl = g.get("time_limit")
        if g.get("lower_bound"):
            res = solve_key_pure(tree, backend=backend,
                                 enum_limit=solver.get("key_pure_enum_limit", 2_000_000),
                                 time_limit=tl)
            lower(res.value, "L", [(1.0, res.profile)])
            row["solves"]["L"] = {"value": res.value, "bound_on_L": res.bound,
                                  "optimal": res.optimal, "method": res.method,
                                  "seconds": res.seconds}
            solutions["L"] = {"profile": res.profile}
        # exact_cells: [k, s, rho] or [k, s, rho, seconds] (per-cell time limit).
        exact_cells = {tuple(c[:3]): (c[3] if len(c) > 3 else tl)
                       for c in g.get("exact_cells", [])}
        if g.get("exact") or (k, s, rho) in exact_cells:
            res = solve_bilinear(tree, time_limit=exact_cells.get((k, s, rho), tl))
            lower(res.value, "bilinear", [(1.0, res.profile)])
            upper(res.bound, "bilinear")
            row["solver_exact"] = res.optimal
            row["solves"]["bilinear"] = {"value": res.value, "bound": res.bound,
                                         "optimal": res.optimal, "seconds": res.seconds}
            solutions["bilinear"] = {"profile": res.profile}

    if v_com is not None:
        upper(v_com, "V_Com (Prop1)")

    # Leakage of the best strategy found for this cell.
    best = max(candidates, key=lambda c: c[0])
    row["leak_strategy"] = best[1]
    row["leak_bits"] = mutual_information(tree, best[2], channel="all")
    if g.get("phi") == "suit_blocker":      # Milestone 5: exploitable leakage I(M; suit)
        from games.suit_blocker import suit_phi
        row["leak_exploitable"] = mutual_information(tree, best[2], channel="all", phi=suit_phi)
    row["seconds"] = time.perf_counter() - t0
    for name, sol in solutions.items():
        if "profile" in sol and name in row["solves"]:
            row["solves"][name]["leak_bits"] = mutual_information(
                tree, [(1.0, sol["profile"])], channel="all")
    return row, solutions


def propagate(rows, rounds, hand):
    """Tighten bounds across cells with Propositions 1 and 2 (and hand-proved bounds)."""
    cell = {(r["k"], s_value(parse_s(r["s"])), r["rho"]): r for r in rows}
    for (k, s, rho), r in cell.items():
        for h in hand:
            if (h["k"], s_value(parse_s(h["s"])), h["rho"]) == (k, s, rho) \
                    and h["upper"] < r["upper"] - EPS:
                r["upper"], r["upper_from"] = h["upper"], f"hand ({h['ref']})"

    def improve(r, lo=None, hi=None, why=""):
        changed = False
        if lo is not None and lo > r["lower"] + EPS:
            r["lower"], r["lower_from"], changed = lo, why, True
        if hi is not None and hi < r["upper"] - EPS:
            r["upper"], r["upper_from"], changed = hi, why, True
        return changed

    changed = True
    while changed:
        changed = False
        for (k, s, rho), r in cell.items():
            for (k2, s2, rho2), q in cell.items():
                if (k2, s2, rho2) == (k, s, rho):
                    continue
                # Prop. 1(1): monotone in s and in k (same rho).
                if rho2 == rho and k2 == k and s2 < s:
                    changed |= improve(r, lo=q["lower"], why=f"Prop1 s (from s={s_label(s2)})")
                    changed |= improve(q, hi=r["upper"], why=f"Prop1 s (from s={s_label(s)})")
                if rho2 == rho and s2 == s and k2 < k:
                    changed |= improve(r, lo=q["lower"], why=f"Prop1 k (from k={k2})")
                    changed |= improve(q, hi=r["upper"], why=f"Prop1 k (from k={k})")
                # Prop. 1(1): pub <= priv.
                if k2 == k and s2 == s and rho == "pub" and rho2 == "priv":
                    changed |= improve(r, hi=q["upper"], why="Prop1 pub<=priv")
                    changed |= improve(q, lo=r["lower"], why="Prop1 pub<=priv")
                # Prop. 2: one-time pad (2kR key bits: one k-bit pad per teammate per round).
                if rho == "pub" and rho2 == "priv" and k2 == k and \
                        (s2 == s - 2 * k * rounds or (s == INF and s2 == INF)):
                    changed |= improve(r, lo=q["lower"], why=f"Prop2 (from priv s={s_label(s2)})")
    for r in rows:
        r["certified"] = r["upper"] - r["lower"] <= 1e-7
        r["status"] = ("exact" if r["certified"] and r["solver_exact"]
                       else "theorem" if r["certified"] else "bound")


def fmt_value(r):
    if r["certified"]:
        return f"{r['lower']:+.6f}"
    return f"[{r['lower']:+.6f}, {r['upper']:+.6f}]"


def format_table(rows):
    head = ("| game | k | s | rho | V or [lower, upper] | status | lower from | upper from "
            "| L (pure) | leak (bits) | time (s) | team infosets | adv infosets |")
    lines = [head, "|" + "---|" * 13]
    for r in rows:
        L = r["solves"].get("L", {})
        L_txt = "" if not L else (f"{L['value']:+.6f}" + ("" if L["optimal"] else
                                  f" (<= {L['bound_on_L']:+.6f})"))
        lines.append(
            f"| {r['game']} | {r['k']} | {r['s']} | {r['rho']} | {fmt_value(r)} | {r['status']} "
            f"| {r['lower_from']} | {r['upper_from']} | {L_txt} | {r['leak_bits']:.3f}"
            + (f" / {r['leak_exploitable']:.3f}" if "leak_exploitable" in r else "") + " "
            f"| {r['seconds']:.1f} | {r['team_infosets'][0]} + {r['team_infosets'][1]} "
            f"| {r['adversary_infosets']} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--config", required=True)
    ap.add_argument("--seed", type=int, default=None, help="overrides the config seed")
    ap.add_argument("--games", nargs="*", help="only these game names")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    if args.seed is not None:
        cfg["seed"] = args.seed
    if args.games:
        cfg["games"] = [g for g in cfg["games"] if g["name"] in args.games]
    seed = int(cfg["seed"])
    random.seed(seed)
    np.random.seed(seed)  # computations are deterministic; seeded for the convention

    backend = resolve_backend(cfg.get("backend", "auto"))
    out = ROOT / "results" / cfg["experiment"] / config_hash(cfg) / str(seed)
    (out / "solutions").mkdir(parents=True, exist_ok=True)
    (out / "config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    run_info = {**git_info(), "python": platform.python_version(),
                "open_spiel": getattr(pyspiel, "__version__", None), "backend": backend,
                "threads": num_threads(), "started": time.strftime("%Y-%m-%d %H:%M:%S"),
                "argv": sys.argv}
    (out / "run_info.json").write_text(json.dumps(run_info, indent=2))

    all_rows, v_coms = [], {}
    for g in cfg["games"]:
        rows = []
        v_com = None
        if g.get("v_com"):
            t0 = time.perf_counter()
            v_com = v_com_of(g, backend)
            v_coms[g["name"]] = v_com
            print(f"{g['name']:9s} V_Com = {v_com:+.6f} ({time.perf_counter() - t0:.1f}s)",
                  flush=True)
        for k in g["k"]:
            for s in map(parse_s, g["s"]):
                for rho in g["rho"]:
                    row, sols = solve_cell(g, k, s, rho, cfg, backend, seed, args.verbose, v_com)
                    rows.append(row)
                    print(f"{g['name']:9s} k={k} s={s_label(s):3s} {rho:4s} "
                          f"[{row['lower']:+.6f}, {row['upper']:+.6f}] "
                          f"leak={row['leak_bits']:.3f} ({row['seconds']:.1f}s)", flush=True)
                    name = f"{g['name']}_k{k}_s{s_label(s)}_{rho}.json"
                    (out / "solutions" / name).write_text(json.dumps(sols))
        hand = [h for h in cfg.get("hand_upper_bounds", []) if h["game"] == g["name"]]
        propagate(rows, len(g["rounds"]), hand)
        all_rows.extend(rows)
        (out / "metrics.json").write_text(json.dumps(all_rows, indent=2, default=str))
        (out / "v_com.json").write_text(json.dumps(v_coms, indent=2))

    table = format_table(all_rows)
    if v_coms:
        table += "\n\n| game | V_Com (merged team, exact LP) |\n|---|---|\n" + "\n".join(
            f"| {name} | {v:+.6f} |" for name, v in v_coms.items())
    print()
    print(table)
    (out / "summary.md").write_text(table + "\n")
    print(f"\nresults in {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
