"""Milestone 3: train teams by policy gradient against an exact best response, evaluate exactly.

Usage:
    nice -n 19 .venv/bin/python scripts/run_marl.py --config configs/m3_marl.yaml

Runs every (game, k, s, rho, seed) in parallel in ``workers`` single-threaded
processes (keep workers <= 8 on the laptop). For every final team policy it
computes, with the exact evaluators in ``eval/``:
  * g(pi_T) and the gap V(k, s, rho) - g(pi_T) (Question 4);
  * leakage I(M; X) (all messages; on public cells this is what the adversary
    sees) and its cost against a best response, g_priv(pi_T) - g_pub(pi_T),
    i.e. the same policy evaluated with a private channel (Question 5);
  * the behavior checks (Questions 5 and 6).
Stops with an error if any g(pi_T) exceeds the exact V of its cell (a bug).

Writes results/m3_marl/<config-hash>/: config, run info, one JSON per run
(final policy, learning curve, metrics), metrics.json, summary.md, and the
plots values_<game>.png and curves.png.
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

import games  # noqa: E402,F401
from eval.best_response import guaranteed_value  # noqa: E402
from eval.leakage import leakage_labels, mutual_information  # noqa: E402
from games.augment import make_augmented_game  # noqa: E402
from games.tree import build_tree  # noqa: E402
from learning.tabular_pg import PGConfig, train  # noqa: E402
from run_values import config_hash, git_info  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
_TREES = {}
CFG = None


def tree_of(g, k, s, rho):
    key = (g["base_game"], k, s, rho)
    if key not in _TREES:
        game = make_augmented_game(g["base_game"], k=k, s=s, rho=rho, team=tuple(g["team"]),
                                   adversary=int(g["adversary"]), rounds=g["rounds"])
        _TREES[key] = build_tree(game, tuple(g["team"]), int(g["adversary"]),
                                 label_fn=leakage_labels)
    return _TREES[key]


def _init(cfg):
    global CFG
    CFG = cfg


METHODS = {"team_pg_vs_exact_br": "best_response", "self_play": "learning"}


def run_one(task):
    """Train one (method, game, k, s, rho, seed) and evaluate the final policy exactly."""
    method, gi, k, s, rho, seed = task
    g = CFG["games"][gi]
    lc = CFG["learner"]
    tree = tree_of(g, k, s, rho)
    t0 = time.perf_counter()
    res = train(tree, PGConfig(iterations=lc["iterations"], batch=lc["batch"], lr=lc["lr"],
                               log_every=lc["log_every"], init_scale=lc["init_scale"]),
                seed=seed, opponent=METHODS[method])
    seconds = time.perf_counter() - t0
    strategy = [(1.0, res.policies)]
    g_val = guaranteed_value(tree, strategy)            # evaluator, independent of the learner
    leak = mutual_information(tree, strategy, channel="all")
    g_priv = guaranteed_value(tree_of(g, k, s, "priv"), strategy) if rho == "pub" else g_val
    return {
        "method": method, "game": g["name"], "k": k, "s": s, "rho": rho, "seed": seed,
        "g": g_val, "g_learner": res.final_g, "leak_bits": leak, "g_same_policy_priv": g_priv,
        "seconds": seconds, "episodes": res.episodes, "curve": res.curve,
        "policies": {str(p): pol for p, pol in res.policies.items()},
    }


# ----------------------------------------------------------------- behavior checks

def _split(key):
    parts = key.split("|")
    k = next((p[4:] for p in parts if p.startswith("key=")), "")
    return parts[0], k


def diagonal_trick(run):
    """Coordinated attack, k = 0: per key, which cells both teammates attack together."""
    att = {0: {}, 1: {}}
    for p in (0, 1):
        for key, probs in run["policies"][str(p)].items():
            inner, kv = _split(key)
            coord = int(inner.split(":")[1])
            att[p][(kv, coord)] = max(probs, key=probs.get)
    keys = sorted({kv for kv, _ in att[0]})
    cells = {}
    for kv in keys:
        cells[kv] = sorted(divmod(t, 2) for i in (0, 1) for j in (0, 1)
                           if (t := att[0][(kv, i)]) == att[1][(kv, j)] and divmod(t, 2) == (i, j))
    lines = {kv: ("diag" if c == [(0, 0), (1, 1)] else "anti" if c == [(0, 1), (1, 0)] else str(c))
             for kv, c in cells.items()}
    found = (all(len(c) == 2 for c in cells.values())
             and {"diag", "anti"} <= set(lines.values()) and run["g"] >= 3 / 8 - 0.01)
    desc = "per key: " + ", ".join(f"K={kv or '-'}:{v}" for kv, v in lines.items())
    return found, desc


def behavior(run, V, V_priv):
    """(check name, yes/no, one-line description) or None for cells without a check."""
    game, k, s, rho = run["game"], run["k"], run["s"], run["rho"]
    leak, gv = run["leak_bits"], run["g"]
    if game == "attack2x2" and k == 0 and s >= 1:
        found, desc = diagonal_trick(run)
        return "diagonal trick", found, f"g={gv:.3f}; {desc}"
    if k == 1 and s == 0 and rho == "pub":
        ok = gv >= V - 0.02
        what = ("messages carry no information (quiet)" if leak < 0.05 else
                f"messages carry {leak:.2f} bits")
        return "quiet or coarse", ok, f"g={gv:.3f} vs V={V:.3f}; {what}"
    if s == 2 and rho == "pub" and k >= 1:
        ok = leak < 0.1 and gv >= V_priv - 0.02
        return "key as pad", ok, f"g={gv:.3f} vs V_priv={V_priv:.3f}; leak={leak:.3f} bits"
    return None


# ----------------------------------------------------------------- reporting

def frac(x):
    from fractions import Fraction
    f = Fraction(x).limit_denominator(64)
    return str(f) if abs(float(f) - x) < 1e-9 else f"{x:.4f}"


def summarize(cfg, runs):
    V = cfg["exact_values"]
    cells = {}
    for r in runs:
        cells.setdefault((r["method"], r["game"], r["k"], r["s"], r["rho"]), []).append(r)
    rows, checks = [], []
    for (method, game, k, s, rho), rs in cells.items():
        v = V[game][f"{k},{s},{rho}"]
        v_priv = V[game][f"{k},{s},priv"]
        gs = np.array([r["g"] for r in rs])
        leaks = np.array([r["leak_bits"] for r in rs])
        cost = np.array([r["g_same_policy_priv"] - r["g"] for r in rs])
        rows.append({"method": method, "game": game, "k": k, "s": s, "rho": rho, "V": v,
                     "g_mean": gs.mean(), "g_std": gs.std(), "gap_mean": v - gs.mean(),
                     "gap_max": (v - gs).max(), "leak_mean": leaks.mean(), "leak_std": leaks.std(),
                     "cost_mean": cost.mean(), "seeds": len(rs),
                     "seconds": float(np.mean([r["seconds"] for r in rs]))})
        for r in sorted(rs, key=lambda r: r["seed"]):
            b = behavior(r, v, v_priv)
            if b:
                checks.append((method, game, k, s, rho, r["seed"], *b))
    return rows, checks


def format_tables(rows, checks):
    lines = ["| method | game | k | s | ρ | exact V | g(π_T) mean ± std | gap (mean / worst) | "
             "leak bits | cost of leak | time/run |",
             "|" + "---|" * 11]
    for r in rows:
        cost = f"{r['cost_mean']:.3f}" if r["rho"] == "pub" else ""
        lines.append(
            f"| {SHORT[r['method']]} | {r['game']} | {r['k']} | {r['s']} | {r['rho']} | {frac(r['V'])} "
            f"| {r['g_mean']:.3f} ± {r['g_std']:.3f} | {r['gap_mean']:.3f} / {r['gap_max']:.3f} "
            f"| {r['leak_mean']:.2f} ± {r['leak_std']:.2f} | {cost} | {r['seconds']:.1f}s |")
    lines += ["", "| method | game | k | s | ρ | seed | check | yes/no | what the policy does |",
              "|" + "---|" * 9]
    for method, game, k, s, rho, seed, name, ok, desc in checks:
        lines.append(f"| {SHORT[method]} | {game} | {k} | {s} | {rho} | {seed} | {name} "
                     f"| {'yes' if ok else 'no'} | {desc} |")
    return "\n".join(lines)


SHORT = {"team_pg_vs_exact_br": "PG vs BR", "self_play": "self-play"}


def plots(cfg, rows, runs, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    BLUE, INK, MUTED, SURFACE = "#2a78d6", "#0b0b0b", "#52514e", "#fcfcfb"
    COLOR = {"team_pg_vs_exact_br": BLUE, "self_play": "#eb6834"}
    MARK = {"team_pg_vs_exact_br": "o", "self_play": "D"}
    methods = cfg["methods"]
    plt.rcParams.update({"font.size": 9, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                         "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False,
                         "axes.spines.right": False, "figure.facecolor": SURFACE,
                         "axes.facecolor": SURFACE})
    for g in cfg["games"]:
        fig, axes = plt.subplots(2, 3, figsize=(9, 5), sharey=True, sharex=True)
        for i, rho in enumerate(("priv", "pub")):
            for j, s in enumerate((0, 1, 2)):
                ax = axes[i, j]
                for mi, m in enumerate(methods):
                    rs = sorted((r for r in rows if r["game"] == g["name"] and r["rho"] == rho
                                 and r["s"] == s and r["method"] == m), key=lambda r: r["k"])
                    ks = [r["k"] for r in rs]
                    if mi == 0:
                        ax.plot(ks, [r["V"] for r in rs], color=MUTED, lw=2, ls="--", marker="s",
                                ms=8, mfc="none", label="exact V")
                    ax.errorbar(ks, [r["g_mean"] for r in rs], yerr=[r["g_std"] for r in rs],
                                color=COLOR[m], lw=2, marker=MARK[m], ms=7, capsize=3,
                                mec=SURFACE, mew=1.5,
                                label=f"g(π_T), {SHORT[m]} (mean ± std, 5 seeds)")
                ax.set_title(f"s = {s}, {'private' if rho == 'priv' else 'public'}", color=INK)
                ax.set_xticks(ks)
                ax.grid(axis="y", color="#e6e5e0", lw=0.8)
                if i == 1:
                    ax.set_xlabel("k (bits per message)")
                if j == 0:
                    ax.set_ylabel("team value")
        axes[0, 0].legend(frameon=False, loc="upper left")
        fig.suptitle(f"{g['name']}: guaranteed value g(π_T) of learned teams vs exact V", color=INK)
        fig.tight_layout()
        fig.savefig(out / f"values_{g['name']}.png", dpi=150)
        plt.close(fig)

    cells = cfg["curve_cells"]
    fig, axes = plt.subplots(1, len(cells), figsize=(3.4 * len(cells), 3.3), sharey=False)
    for ax, (game, k, s, rho) in zip(np.atleast_1d(axes), cells):
        for m in methods:
            rs = [r for r in runs if (r["method"], r["game"], r["k"], r["s"], r["rho"])
                  == (m, game, k, s, rho)]
            ep = np.array([c[1] for c in rs[0]["curve"]]) / 1e6
            G = np.array([[c[2] for c in r["curve"]] for r in rs])
            ax.fill_between(ep, G.min(0), G.max(0), color=COLOR[m], alpha=0.15, lw=0)
            ax.plot(ep, G.mean(0), color=COLOR[m], lw=2, label=f"{SHORT[m]} (mean; band = min–max)")
        v = cfg["exact_values"][game][f"{k},{s},{rho}"]
        ax.axhline(v, color=MUTED, lw=2, ls="--", label="exact V")
        ax.set_title(f"{game} (k={k}, s={s}, {rho}), V = {frac(v)}", color=INK, fontsize=9)
        ax.set_xlabel("episodes (millions)")
        ax.grid(axis="y", color="#e6e5e0", lw=0.8)
    handles, labels = np.atleast_1d(axes)[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False)
    np.atleast_1d(axes)[0].set_ylabel("guaranteed value g(π_T)")
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(out / "curves.png", dpi=150)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    out = ROOT / "results" / cfg["experiment"] / config_hash(cfg) / "seeds"
    (out / "runs").mkdir(parents=True, exist_ok=True)
    (out / "config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    (out / "run_info.json").write_text(json.dumps({
        **git_info(), "python": platform.python_version(), "workers": cfg["workers"],
        "threads_per_worker": 1, "started": time.strftime("%Y-%m-%d %H:%M:%S"),
        "argv": sys.argv}, indent=2))

    tasks = [(m, gi, k, s, rho, seed) for m in cfg["methods"]
             for gi, g in enumerate(cfg["games"]) for k in g["k"]
             for s in g["s"] for rho in g["rho"] for seed in cfg["seeds"]]
    t0 = time.perf_counter()
    runs = []
    with Pool(cfg["workers"], initializer=_init, initargs=(cfg,)) as pool:
        for r in pool.imap_unordered(run_one, tasks):
            v = cfg["exact_values"][r["game"]][f"{r['k']},{r['s']},{r['rho']}"]
            if r["g"] > v + 1e-6:
                pool.terminate()
                raise RuntimeError(f"g(pi_T) = {r['g']} exceeds exact V = {v} in {r['game']} "
                                   f"k={r['k']} s={r['s']} {r['rho']} seed {r['seed']}: bug")
            name = f"{r['method']}_{r['game']}_k{r['k']}_s{r['s']}_{r['rho']}_seed{r['seed']}.json"
            (out / "runs" / name).write_text(json.dumps(r))
            runs.append(r)
            print(f"{SHORT[r['method']]:9s} {r['game']:9s} k={r['k']} s={r['s']} {r['rho']:4s} seed {r['seed']}  "
                  f"g={r['g']:.4f}  V={v:.4f}  leak={r['leak_bits']:.3f}  ({r['seconds']:.1f}s)",
                  flush=True)
    wall = time.perf_counter() - t0
    order = {(m, g["name"], k, s, rho): i for i, (m, g, k, s, rho) in enumerate(
        (m, g, k, s, rho) for m in cfg["methods"] for g in cfg["games"] for k in g["k"]
        for s in g["s"] for rho in g["rho"])}
    runs.sort(key=lambda r: (order[(r["method"], r["game"], r["k"], r["s"], r["rho"])], r["seed"]))
    rows, checks = summarize(cfg, runs)
    table = format_tables(rows, checks)
    (out / "metrics.json").write_text(json.dumps(
        {"cells": rows, "checks": checks, "wall_seconds": wall}, indent=2, default=float))
    (out / "summary.md").write_text(table + f"\n\nwall time {wall:.0f} s for {len(runs)} runs\n")
    plots(cfg, rows, runs, out)
    print()
    print(table)
    print(f"\nwall time {wall:.0f} s for {len(runs)} runs; results in {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
