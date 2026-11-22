"""Draw the report figures from the committed results files (no hand-typed numbers).

Usage:
    .venv/bin/python scripts/make_report_figures.py          # writes report/figures/*.{pdf,png}

Figures (each read from the results named here, written by the configs and scripts listed in
README.md):
* fig_exact_values      exact V(k, s, rho) against k, blocker n = 4 (results/m2_values) and
                        coordinated attack 2 x 2 (results/m25_values); private s = 2 and public
                        s = 0, 1, 2. Intervals (cells not closed by the solver) are drawn as bars.
* fig_learning_vs_exact the 12 public cells of results/m4_seeds (PG vs BR, last iterate, 20 seeds):
                        exact V as a black bar, learned g(pi_T) mean +- 95% CI as a point.
* fig_dose              results/m5_dose: (a) pad rate (three pad cells, 30 runs) and quiet rate
                        (10 runs) against epsilon, (b) mean leakage on the pad cells and the quiet cell.
* fig_responsiveness    results/m8_resp/runs_summary.csv: mean r_t over the first half of training
                        against final leakage, one panel per cell, colored by training adversary.
"""

import csv
import glob
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "report" / "figures"
BLUE, ORANGE, BLACK = "#2a78d6", "#eb6834", "#000000"

plt.rcParams.update({
    "font.family": "serif", "font.size": 8, "axes.titlesize": 8, "axes.labelsize": 8,
    "legend.fontsize": 6.5, "xtick.labelsize": 7, "ytick.labelsize": 7,
    "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42,
})


def one(pattern):
    files = sorted(glob.glob(str(ROOT / pattern)))
    if len(files) != 1:
        raise FileNotFoundError(f"expected one file for {pattern}, found {files}")
    return json.loads(Path(files[0]).read_text())


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    for ext in ("pdf", "png"):
        meta = {"CreationDate": None} if ext == "pdf" else {}   # byte-identical reruns
        fig.savefig(OUT / f"{name}.{ext}", dpi=200, bbox_inches="tight", metadata=meta)
    plt.close(fig)
    print(f"wrote report/figures/{name}.pdf and .png")


def exact_rows():
    rows = one("results/m2_values/*/0/metrics.json") + one("results/m25_values/*/0/metrics.json")
    return {(r["game"], r["k"], str(r["s"]), r["rho"]): (r["lower"], r["upper"]) for r in rows}


def fig_exact_values():
    V = exact_rows()
    series = [("2", "priv", "private, s = 2", BLACK, "-", "o"),
              ("0", "pub", "public, s = 0", ORANGE, ":", "v"),
              ("1", "pub", "public, s = 1", BLUE, "--", "s"),
              ("2", "pub", "public, s = 2", BLUE, "-", "^")]
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5))
    for ax, (game, ks, title) in zip(axes, [("blocker4", [0, 1, 2], "(a) blocker, n = 4"),
                                            ("attack2x2", [0, 1], "(b) coordinated attack, 2 × 2")]):
        for s, rho, label, color, ls, mk in series:
            lo = [V[(game, k, s, rho)][0] for k in ks]
            hi = [V[(game, k, s, rho)][1] for k in ks]
            mid = [(a + b) / 2 for a, b in zip(lo, hi)]
            under = rho == "priv"                 # equal to public s = 2 here; draw it underneath
            ax.plot(ks, mid, ls=ls, marker=mk, color=color, label=label, ms=7 if under else 4,
                    lw=3 if under else 1.2, alpha=0.35 if under else 1.0, zorder=1 if under else 2)
            for k, a, b in zip(ks, lo, hi):
                if b - a > 1e-6:
                    ax.vlines(k, a, b, color=color, lw=2)
        ax.set_xticks(ks)
        ax.set_xlabel("channel bits k")
        ax.set_title(title)
        ax.set_ylim(0, 0.85)
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("team value V(k, s, ρ)")
    axes[0].legend(frameon=False, loc="upper left")
    fig.tight_layout()
    save(fig, "fig_exact_values")


def fig_learning_vs_exact():
    m = one("results/m4_seeds/*/seeds/metrics.json")
    cells = {(c["game"], c["k"], c["s"]): c for c in m["cells"]
             if c["rho"] == "pub" and c["method"] == "pg_vs_br/last"}
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5))
    for ax, (game, ks, title) in zip(axes, [("attack2x2", [0, 1], "(a) coordinated attack, 2 × 2"),
                                            ("blocker4", [1, 2], "(b) blocker, n = 4")]):
        keys = [(game, k, s) for k in ks for s in (0, 1, 2)]
        x = list(range(len(keys)))
        ax.scatter(x, [cells[c]["V_hi"] for c in keys], marker="_", s=260, color=BLACK, lw=2,
                   label="exact V", zorder=2)
        ax.errorbar(x, [cells[c]["g_mean"] for c in keys], yerr=[cells[c]["g_ci95"] for c in keys],
                    fmt="o", color=BLUE, ms=4, capsize=2, label="learned g(π_T), 95% CI", zorder=3)
        ax.set_xticks(x, [f"({k},{s})" for _, k, s in keys])
        ax.set_xlabel("public cell (k, s)")
        ax.set_title(title)
        ax.set_ylim(0, 0.85)
        ax.grid(alpha=0.3, axis="y")
    axes[0].set_ylabel("value")
    axes[0].legend(frameon=False, loc="upper left")
    fig.tight_layout()
    save(fig, "fig_learning_vs_exact")


def dose_series():
    m = one("results/m5_dose/*/seeds/metrics.json")
    by = {}
    for c in m["cells"]:
        eps = float(c["method"].split("/")[0][3:])
        by.setdefault(eps, []).append(c)
    pad_cells = {("attack2x2", 1, 2), ("blocker4", 1, 2), ("blocker4", 2, 2)}
    out = []
    for eps in sorted(by):
        pads = [c for c in by[eps] if (c["game"], c["k"], c["s"]) in pad_cells]
        quiet = [c for c in by[eps] if (c["game"], c["k"], c["s"]) == ("attack2x2", 1, 0)][0]
        out.append({"eps": eps, "pad": sum(c["check_yes"] for c in pads),
                    "pad_n": sum(c["seeds"] for c in pads), "quiet": quiet["check_yes"],
                    "quiet_n": quiet["seeds"], "leak_pad": sum(c["leak_mean"] for c in pads) / 3,
                    "leak_quiet": quiet["leak_mean"]})
    return out


def fig_dose():
    d = dose_series()
    eps = [r["eps"] for r in d]
    fig, axes = plt.subplots(1, 2, figsize=(6.6, 2.5))
    ax = axes[0]
    ax.plot(eps, [r["pad"] / r["pad_n"] for r in d], "-o", color=BLUE, ms=4,
            label="key used as pad (30 runs)")
    ax.plot(eps, [r["quiet"] / r["quiet_n"] for r in d], "-s", color=ORANGE, ms=4,
            label="quiet when overheard (10 runs)")
    ax.set_ylim(-0.03, 1.05)
    ax.set_ylabel("fraction of runs")
    ax.set_title("(a) secrecy behaviors")
    ax.legend(frameon=False, loc="lower left")
    ax = axes[1]
    ax.plot(eps, [r["leak_pad"] for r in d], "-o", color=BLUE, ms=4, label="pad cells (mean)")
    ax.plot(eps, [r["leak_quiet"] for r in d], "-s", color=ORANGE, ms=4, label="quiet cell")
    ax.set_ylabel("leakage I(M; X), bits")
    ax.set_title("(b) leakage")
    ax.legend(frameon=False, loc="upper left")
    for ax in axes:
        ax.set_xticks(eps, [f"{e:g}".lstrip("0") if e not in (0, 1) else f"{e:g}" for e in eps])
        ax.set_xlabel("adversary noise ε (uniform play with prob. ε)")
        ax.grid(alpha=0.3)
    fig.tight_layout()
    save(fig, "fig_dose")


ADV = [("exact_br", "exact BR", BLACK, "o", 1.0),
       ("noisy_e0.25", "noisy BR ε = .25", BLUE, "o", 0.35),
       ("noisy_e0.5", "noisy BR ε = .5", BLUE, "o", 0.55),
       ("noisy_e0.75", "noisy BR ε = .75", BLUE, "o", 0.75),
       ("noisy_e1", "noisy BR ε = 1", BLUE, "o", 1.0),
       ("model_N2048_T1", "model N=2048, T=1", ORANGE, "s", 0.45),
       ("model_N2048_T10", "model N=2048, T=10", ORANGE, "s", 0.7),
       ("model_N32_T10", "model N=32, T=10", ORANGE, "s", 1.0),
       ("reinforce_s1", "REINFORCE, 1 update", "#666666", "x", 0.6),
       ("reinforce_s4", "REINFORCE, 4 updates", "#666666", "x", 1.0)]
RESP_CELLS = [(("attack2x2", 1, 2), "attack (1, 2, pub)"), (("blocker4", 1, 2), "blocker (1, 2, pub)"),
              (("blocker4", 2, 2), "blocker (2, 2, pub)"), (("attack2x2", 1, 0), "attack (1, 0, pub)")]


def fig_responsiveness():
    path = ROOT / "results" / "m8_resp" / "runs_summary.csv"
    rows = list(csv.DictReader(path.open()))
    fig, axes = plt.subplots(1, 4, figsize=(6.6, 2.5))
    for ax, ((game, k, s), title) in zip(axes, RESP_CELLS):
        for name, label, color, mk, alpha in ADV:
            rs = [r for r in rows if (r["game"], int(r["k"]), int(r["s"]), r["adversary"])
                  == (game, k, s, name)]
            ax.scatter([float(r["early_r"]) for r in rs], [float(r["final_leakage"]) for r in rs],
                       s=9, marker=mk, color=color, alpha=alpha, label=label,
                       linewidths=0.8 if mk == "x" else 0)
        ax.set_title(title)
        ax.set_xlabel("early mean r_t")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("final leakage I(M; X), bits")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=5, frameon=False,
               bbox_to_anchor=(0.5, -0.17))
    fig.tight_layout()
    save(fig, "fig_responsiveness")


def main():
    fig_exact_values()
    fig_learning_vs_exact()
    fig_dose()
    fig_responsiveness()


if __name__ == "__main__":
    main()
