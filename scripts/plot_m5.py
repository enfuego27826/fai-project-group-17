"""Milestone 5 plots from a run_m5.py results folder.

Usage:
    .venv/bin/python scripts/plot_m5.py dose results/m5_dose/<hash>/seeds results/m5_dose/dose.png

``dose``: pad rate and quiet rate (left) and mean leakage I(M; X) (right) against
the adversary's noise epsilon. Error bars are 95% intervals (Wilson for rates,
Student t for leakage) over seeds.
"""

import json
import sys
from pathlib import Path

import numpy as np
from scipy import stats

BLUE, ORANGE, INK, MUTED, SURFACE = "#2a78d6", "#eb6834", "#0b0b0b", "#52514e", "#fcfcfb"


def wilson(k, n, z=1.96):
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return p, c - h, c + h


def dose(folder, png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    runs = [json.loads(f.read_text()) for f in Path(folder, "runs").glob("*.json")]
    checks = json.loads(Path(folder, "metrics.json").read_text())["checks"]
    eps = sorted({float(r["method"].split("/")[0][3:]) for r in runs})
    groups = {"key as pad (3 cells, 30 seeds)": ("key as pad", BLUE, "o"),
              "quiet (attack (1, 0, pub), 10 seeds)": ("quiet or coarse", ORANGE, "D")}
    plt.rcParams.update({"font.size": 10, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                         "xtick.color": MUTED, "ytick.color": MUTED})
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.6), facecolor=SURFACE)
    for ax in axes:
        ax.set_facecolor(SURFACE)
        ax.grid(True, color="#e4e3df", lw=0.8)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        ax.set_xlabel("adversary noise ε (P(uniform) per episode)")
        ax.set_xticks(eps)
        ax.set_xticklabels([f"{e:g}" for e in eps])
    for label, (check, color, marker) in groups.items():
        rate, lo, hi, leak, lh = [], [], [], [], []
        for e in eps:
            name = f"eps{e:g}/last"
            oks = [c[7] for c in checks if c[0] == name and c[6] == check]
            p, a, b = wilson(sum(oks), len(oks))
            rate.append(p), lo.append(a), hi.append(b)
            cells = {(c[1], c[2], c[3], c[4]) for c in checks if c[0] == name and c[6] == check}
            ls = np.array([r["leak_bits"] for r in runs if r["method"] == name
                           and (r["game"], r["k"], r["s"], r["rho"]) in cells])
            leak.append(ls.mean())
            lh.append(stats.t.ppf(0.975, len(ls) - 1) * ls.std(ddof=1) / np.sqrt(len(ls)))
        rate, lo, hi = map(np.array, (rate, lo, hi))
        axes[0].errorbar(eps, rate, yerr=[rate - lo, hi - rate], color=color, marker=marker,
                         ms=6, lw=2, capsize=3, label=label)
        axes[1].errorbar(eps, leak, yerr=lh, color=color, marker=marker, ms=6, lw=2, capsize=3,
                         label=label)
    axes[0].set_ylabel("fraction of seeds passing the check")
    axes[0].set_ylim(-0.03, 1.03)
    axes[1].set_ylabel("leakage I(M; X), bits (mean)")
    axes[1].set_ylim(bottom=0)
    h, l = axes[0].get_legend_handles_labels()
    fig.legend(h, l, loc="lower center", ncol=2, frameon=False, bbox_to_anchor=(0.5, -0.01))
    fig.suptitle("Learned secrecy against an ε-noisy exact best response (PG, M3 hyperparameters)",
                 color=INK, fontsize=11)
    fig.tight_layout(rect=(0, 0.08, 1, 0.95))
    fig.savefig(png, dpi=150, facecolor=SURFACE)
    print("wrote", png)


if __name__ == "__main__":
    {"dose": dose}[sys.argv[1]](sys.argv[2], sys.argv[3])
