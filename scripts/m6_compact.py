"""Milestone 6, task 3: compact per-cell table (one row per cell, one column per training setup).

Usage:
    .venv/bin/python scripts/m6_compact.py results/m6_neural/<hash>/seeds/metrics.json
Prints g(pi_T) mean ± 95% CI, the check count and the mean leakage per method.
"""

import json
import sys
from pathlib import Path


def fmt_t(lo, hi):
    return f"{lo:.4f}" if abs(hi - lo) < 1e-9 else f"[{lo:.4f}, {hi:.4f}]"


def main():
    m = json.loads(Path(sys.argv[1]).read_text())
    methods, cells = [], {}
    for r in m["cells"]:
        if r["method"] not in methods:
            methods.append(r["method"])
        cells.setdefault((r["game"], r["k"], r["s"], r["rho"]), {})[r["method"]] = r
    head = "| cell | target | label | check | " + " | ".join(methods) + " |"
    lines = [head, "|" + "---|" * (4 + len(methods))]
    for (game, k, s, rho), by in cells.items():
        r0 = next(iter(by.values()))
        vals = []
        for meth in methods:
            r = by.get(meth)
            vals.append("" if r is None else
                        f"{r['g_mean']:.3f} ± {r['g_ci95']:.3f}, {r['check_yes']}/{r['seeds']}, "
                        f"{r['leak_mean']:.2f} / {r['leak_ex_mean']:.2f} b")
        lines.append(f"| {game} ({k}, {s}, {rho}) | {fmt_t(r0['V_lo'], r0['V_hi'])} | {r0['label']} "
                     f"| {r0['check']} | " + " | ".join(vals) + " |")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
