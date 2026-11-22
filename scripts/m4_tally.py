"""Per-method summary of a run_m4.py result: mean gap, cells within 0.005, check tallies."""
import json
import sys
from collections import defaultdict

d = json.load(open(sys.argv[1]))
by = defaultdict(list)
for r in d["cells"]:
    by[r["method"]].append(r)
for m, rs in by.items():
    gaps = [r["gap_mean"] for r in rs]
    print(f"{m:24s} cells {len(rs):3d}  mean gap {sum(gaps)/len(gaps):.4f}  "
          f"within 0.005: {sum(g < 0.005 for g in gaps):2d}  worst {max(gaps):.3f}")
tally = defaultdict(lambda: [0, 0])
for c in d["checks"]:
    method, game, k, s, rho, seed, name, ok, _ = c
    key = (method, name, f"{game}({k},{s},{rho})")
    tally[key][0] += bool(ok)
    tally[key][1] += 1
for (m, name, cell), (y, n) in sorted(tally.items()):
    print(f"  {m:24s} {name:16s} {cell:22s} {y}/{n}")
