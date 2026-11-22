"""Export one row per training run (seed) of every learning experiment to results/<exp>/<hash>/seeds/runs.csv.

Usage:
    .venv/bin/python scripts/export_runs_csv.py            # all results/*/*/seeds/runs folders

The per-run JSON files (policies, curves) are large and stay local; these CSVs keep what the report
counts over seeds (g(pi_T) from the exact best response, I(M; X), I(M; c(X)), I(M; c(X) | K)).
They are written by the runners' outputs only; nothing is recomputed.
"""

import csv
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ["method", "game", "k", "s", "rho", "seed", "g", "leak_bits", "leak_exploitable",
          "leak_decodable", "g_same_policy_priv", "episodes", "seconds"]


def main():
    for run_dir in sorted(glob.glob(str(ROOT / "results/*/*/seeds/runs"))):
        rows = []
        for f in sorted(glob.glob(f"{run_dir}/*.json")):
            r = json.loads(Path(f).read_text())
            rows.append({k: r.get(k) for k in FIELDS})
        rows.sort(key=lambda r: (r["method"], r["game"], r["k"], str(r["s"]), r["rho"], r["seed"]))
        out = Path(run_dir).parent / "runs.csv"
        with out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=FIELDS)
            w.writeheader()
            w.writerows(rows)
        print(f"{out.relative_to(ROOT)}: {len(rows)} runs")


if __name__ == "__main__":
    main()
