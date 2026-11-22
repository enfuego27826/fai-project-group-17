"""What does the learned k = 1 bit encode on Kuhn? (Milestone 4, task 3)

    .venv/bin/python scripts/describe_learned_bit.py results/m4_kuhn/<hash>/seeds > results/m4_kuhn/<hash>/seeds/learned_bits.txt

For every k = 1 run, prints per key value and teammate which cards send bit 1
(a card counts if it sends 1 with probability > 0.9, 0 if < 0.1, "mixed"
otherwise) and classifies the partition. The solver's codes (Milestone 2)
were "low (J, Q) vs high (K, A)" and "I hold the K".
"""

import json
import sys
from collections import Counter
from pathlib import Path

CARDS = "JQKA"


def partition(bits):
    ones = frozenset(c for c, b in bits.items() if b == 1)
    if any(b == "mixed" for b in bits.values()):
        return "mixed"
    zeros = frozenset(CARDS) - ones
    for a, b in ((ones, zeros), (zeros, ones)):
        if a == frozenset("JQ"):
            return "high/low (J,Q | K,A)"
        if a == frozenset("K"):
            return "I hold the K"
        if a == frozenset("A"):
            return "I hold the A"
        if a == frozenset("KA") or a == frozenset("JQ"):
            return "high/low (J,Q | K,A)"
    if not ones or not zeros:
        return "constant (no information)"
    small = min(ones, zeros, key=lambda x: (len(x), sorted(x, key=CARDS.index)))
    if len(small) == 1:
        return f"I hold the {next(iter(small))}"
    return "{" + ",".join(sorted(small, key=CARDS.index)) + "} vs rest"


def describe(run):
    rows = []
    for p in ("0", "1"):
        msgs = {}
        for key, probs in run["policies"][p].items():
            if not key.endswith("?"):
                continue
            parts = key.split("|")
            card = CARDS[int(parts[0])]
            kv = next((x[4:] for x in parts if x.startswith("key=")), "-")
            p1 = probs.get("1", probs.get(1, 0.0))
            msgs.setdefault(kv, {})[card] = 1 if p1 > 0.9 else 0 if p1 < 0.1 else "mixed"
        for kv, bits in sorted(msgs.items()):
            rows.append((p, kv, "".join(str(bits[c]) if bits[c] != "mixed" else "?" for c in CARDS),
                         partition(bits)))
    return rows


def main():
    root = Path(sys.argv[1])
    kinds = Counter()
    for f in sorted(root.glob("runs/*_kuhn3_k1_*.json")):
        run = json.loads(f.read_text())
        print(f"{run['method']:16s} s={run['s']} seed {run['seed']}  g={run['g']:+.4f}")
        for p, kv, code, kind in describe(run):
            print(f"    teammate {p} key {kv}: bit for J,Q,K,A = {code}  -> {kind}")
            kinds[(run["method"], kind)] += 1
    print("\ncodes used by all k = 1 runs (counted per teammate and key value):")
    for (m, kind), n in sorted(kinds.items()):
        print(f"  {m:16s} {kind:30s} {n}")


if __name__ == "__main__":
    main()
