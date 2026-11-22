"""Milestone 8: does adversary responsiveness predict leakage? (analysis of results/m8_resp)

Usage:
    .venv/bin/python scripts/m8_analyze.py [results/m8_resp/<hash>/seeds]

Fixed before looking at any result (the prompt's definitions; the choices it leaves open are
marked "choice"):
* r_t = u_T(pi_T^t, pi_o^t) - g(pi_T^t), logged every 100 team iterations, t = 0 .. 9,900;
  l_t = I(M; X) exact, at the same steps and at t = 10,000 (final policy).
  Both are rounded to 1e-12 before ranking (choice), so that floating-point noise in an
  exact best response's r_t (about 1e-17) does not create a spurious order.
* Run level: x = mean of r_t over the first half, t < 5,000 (50 points); y = l_final, and
  separately g_final. Spearman rank correlation over all runs of the cell (100 runs = 10
  adversary settings x 10 seeds), 95% percentile bootstrap interval from 2,000 resamples of
  runs (choice: numpy seed 0; resamples with a constant x or y are dropped and counted).
* Within run, lagged: for each run, Spearman between r_t and l_{t+D} - l_t over all t with
  t + D <= 10,000, D in {500, 2000} (choice: Spearman, as at run level). Undefined (constant
  input, e.g. r_t = 0 for the exact best response) runs are excluded and counted. Mean over runs
  of each adversary type, 95% Student t interval over runs.
* Control: run-level correlation within adversary types only. Ranks of x and y are taken within
  each type and centred by the type mean, then pooled over the types of the cell and correlated
  (Pearson on the centred within-type ranks, i.e. a pooled within-type Spearman); the bootstrap
  resamples runs within each type (choice). Per-type Spearman values over 10 runs are listed too.
* Decision rule: supports if the run-level interval is above 0 in >= 3 of the 4 cells;
  contradicts if the correlation is negative or its interval contains 0 in >= 3 cells; else mixed.
"""

import glob
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
CELLS = [("attack2x2", 1, 2), ("blocker4", 1, 2), ("blocker4", 2, 2), ("attack2x2", 1, 0)]
CELL_NAME = {("attack2x2", 1, 2): "attack (1, 2, pub)", ("blocker4", 1, 2): "blocker (1, 2, pub)",
             ("blocker4", 2, 2): "blocker (2, 2, pub)", ("attack2x2", 1, 0): "attack (1, 0, pub)"}
TYPES = ["exact_br", "noisy_e0.25", "noisy_e0.5", "noisy_e0.75", "noisy_e1", "model_N2048_T1",
         "model_N2048_T10", "model_N32_T10", "reinforce_s1", "reinforce_s4"]
B = 2000


def rnd(v):
    return np.round(np.asarray(v, dtype=float), 12)


def spearman(x, y):
    x, y = rnd(x), rnd(y)
    if np.ptp(x) == 0 or np.ptp(y) == 0:
        return float("nan")
    return float(stats.spearmanr(x, y)[0])


def boot(fn, idx_groups, rng):
    """Percentile 95% interval of fn(indices) over resamples (within each group)."""
    vals, dropped = [], 0
    for _ in range(B):
        idx = np.concatenate([rng.choice(g, size=len(g), replace=True) for g in idx_groups])
        v = fn(idx)
        if np.isnan(v):
            dropped += 1
        else:
            vals.append(v)
    lo, hi = np.percentile(vals, [2.5, 97.5]) if vals else (float("nan"), float("nan"))
    return float(lo), float(hi), dropped


def within_type(x, y, types):
    """Pooled within-type rank correlation: centred within-type ranks, then Pearson."""
    xs, ys = [], []
    for t in np.unique(types):
        m = types == t
        if m.sum() < 2:
            continue
        rx = stats.rankdata(rnd(x[m]))
        ry = stats.rankdata(rnd(y[m]))
        xs.append(rx - rx.mean())
        ys.append(ry - ry.mean())
    xs, ys = np.concatenate(xs), np.concatenate(ys)
    if not xs.any() or not ys.any():
        return float("nan")
    return float(np.corrcoef(xs, ys)[0, 1])


def tci(v):
    v = np.asarray([a for a in v if not np.isnan(a)])
    if len(v) < 2:
        return (float(v.mean()) if len(v) else float("nan")), float("nan"), len(v)
    h = stats.t.ppf(0.975, len(v) - 1) * v.std(ddof=1) / np.sqrt(len(v))
    return float(v.mean()), float(h), len(v)


def load(run_dir):
    runs = defaultdict(list)
    for f in glob.glob(f"{run_dir}/runs/*.json"):
        r = json.load(open(f))
        log = r["resp_log"]
        it = np.array([e[0] for e in log])
        rt = np.array([np.nan if e[1] is None else e[1] for e in log])
        lt = np.array([e[2] for e in log])
        runs[(r["game"], r["k"], r["s"])].append({
            "type": r["method"].split("/")[0], "seed": r["seed"], "it": it, "r": rt, "l": lt,
            "early_r": float(np.mean(rt[(it < 5000)])), "l_final": float(lt[it == 10000][0]),
            "g_final": r["g"]})
    return runs


def lagged(run, D):
    it, r, l = run["it"], run["r"], run["l"]
    pos = {t: i for i, t in enumerate(it)}
    xs, ys = [], []
    for i, t in enumerate(it):
        if np.isnan(r[i]) or t + D not in pos:
            continue
        xs.append(r[i])
        ys.append(l[pos[t + D]] - l[i])
    return spearman(xs, ys)


def main():
    run_dir = sys.argv[1] if len(sys.argv) > 1 else sorted(glob.glob(str(ROOT / "results/m8_resp/*/seeds")))[-1]
    runs = load(run_dir)
    rng = np.random.default_rng(0)
    out = {"cells": {}}
    lines = ["| cell | runs | Spearman(early r, final leakage) [95% CI] | Spearman(early r, final g) [95% CI] "
             "| within-type control [95% CI] |", "|---|---|---|---|---|"]
    lag_lines = ["| cell | adversary | Δ = 500: mean corr ± 95% (runs) | Δ = 2000: mean corr ± 95% (runs) |",
                 "|---|---|---|---|"]
    type_lines = ["| cell | " + " | ".join(TYPES) + " |", "|" + "---|" * (len(TYPES) + 1)]
    verdicts = []
    for cell in CELLS:
        rs = sorted(runs[cell], key=lambda r: (TYPES.index(r["type"]), r["seed"]))
        x = np.array([r["early_r"] for r in rs])
        y = np.array([r["l_final"] for r in rs])
        gf = np.array([r["g_final"] for r in rs])
        types = np.array([r["type"] for r in rs])
        all_idx = [np.arange(len(rs))]
        rho = spearman(x, y)
        lo, hi, d1 = boot(lambda i: spearman(x[i], y[i]), all_idx, rng)
        rho_g = spearman(x, gf)
        lo_g, hi_g, d2 = boot(lambda i: spearman(x[i], gf[i]), all_idx, rng)
        groups = [np.where(types == t)[0] for t in TYPES if (types == t).any()]
        wt = within_type(x, y, types)
        wlo, whi, d3 = boot(lambda i: within_type(x[i], y[i], types[i]), groups, rng)
        per_type = {t: spearman(x[types == t], y[types == t]) for t in TYPES}
        verdict = ("positive" if lo > 0 else "negative" if rho < 0 else "indistinguishable from 0")
        verdicts.append(lo > 0)
        name = CELL_NAME[cell]
        lines.append(f"| {name} | {len(rs)} | {rho:+.2f} [{lo:+.2f}, {hi:+.2f}] | {rho_g:+.2f} "
                     f"[{lo_g:+.2f}, {hi_g:+.2f}] | {wt:+.2f} [{wlo:+.2f}, {whi:+.2f}] |")
        type_lines.append(f"| {name} | " + " | ".join(
            "n/a" if np.isnan(v) else f"{v:+.2f}" for v in per_type.values()) + " |")
        lag = {}
        for t in TYPES:
            trs = [r for r in rs if r["type"] == t]
            cells_txt = []
            for D in (500, 2000):
                m, h, n = tci([lagged(r, D) for r in trs])
                lag[(t, D)] = (m, h, n)
                cells_txt.append("undefined (r_t constant)" if n == 0 else
                                 f"{m:+.2f} ± {h:.2f} ({n})" if n > 1 else f"{m:+.2f} ({n})")
            lag_lines.append(f"| {name} | {t} | " + " | ".join(cells_txt) + " |")
        out["cells"][name] = {"rho": rho, "ci": [lo, hi], "rho_g": rho_g, "ci_g": [lo_g, hi_g],
                              "within": wt, "within_ci": [wlo, whi], "per_type": per_type,
                              "dropped": [d1, d2, d3], "verdict": verdict,
                              "lagged": {f"{t} {D}": v for (t, D), v in lag.items()},
                              "spread": {t: [float(x[types == t].min()), float(x[types == t].max()),
                                             float(y[types == t].min()), float(y[types == t].max())]
                                         for t in TYPES}}
    n_pos = sum(verdicts)
    n_neg_or_zero = sum(1 for v in out["cells"].values() if v["verdict"] != "positive")
    outcome = ("supports" if n_pos >= 3 else "contradicts" if n_neg_or_zero >= 3 else "mixed")
    out["outcome"] = outcome
    text = ("\n".join(lines) + "\n\nWithin-type Spearman per adversary type (10 runs each; n/a = "
            "constant input):\n\n" + "\n".join(type_lines) + "\n\nLagged, within run:\n\n"
            + "\n".join(lag_lines) + f"\n\nDecision rule: {outcome} ({n_pos} of 4 cells positive "
            "with the interval above 0)\n")
    print(text)
    res = ROOT / "results" / "m8_resp"
    (res / "analysis.md").write_text(text)
    (res / "analysis.json").write_text(json.dumps(out, indent=2, default=float))
    write_csv(runs, res / "runs_summary.csv")
    figure(runs)


def write_csv(runs, path):
    """One row per run: what the report figure and the run-level correlations are built from."""
    lines = ["game,k,s,adversary,seed,early_r,final_leakage,final_g"]
    for (game, k, s), rs in sorted(runs.items()):
        for r in sorted(rs, key=lambda r: (TYPES.index(r["type"]), r["seed"])):
            lines.append(f"{game},{k},{s},{r['type']},{r['seed']},{r['early_r']!r},"
                         f"{r['l_final']!r},{r['g_final']!r}")
    path.write_text("\n".join(lines) + "\n")


def figure(runs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    colors = {"exact_br": "#000000", "noisy_e0.25": "#9ecae1", "noisy_e0.5": "#4292c6",
              "noisy_e0.75": "#2171b5", "noisy_e1": "#08306b", "model_N2048_T1": "#a1d99b",
              "model_N2048_T10": "#41ab5d", "model_N32_T10": "#00441b",
              "reinforce_s1": "#fd8d3c", "reinforce_s4": "#d94801"}
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.2), sharey=False)
    for ax, cell in zip(axes, CELLS):
        for t in TYPES:
            rs = [r for r in runs[cell] if r["type"] == t]
            ax.scatter([r["early_r"] for r in rs], [r["l_final"] for r in rs], s=22, alpha=0.8,
                       color=colors[t], label=t, edgecolors="none")
        ax.set_title(CELL_NAME[cell])
        ax.set_xlabel("mean responsiveness gap r_t, t < 5000")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("final leakage I(M; X) (bits)")
    axes[-1].legend(fontsize=7, loc="upper left", bbox_to_anchor=(1.02, 1.0))
    fig.tight_layout()
    for ext in ("png", "pdf"):
        fig.savefig(ROOT / "results" / "m8_resp" / f"responsiveness.{ext}", dpi=150,
                    bbox_inches="tight")


if __name__ == "__main__":
    main()
