"""Print the k = 1 message strategy of the TMECor solution of Kuhn (Milestone 2, task 1).

For each joint pure plan in the support of the correlation device, prints the
bit each teammate sends for each card, and the on-path betting actions as a
function of the teammate's own card and the partner's bit (two letters:
the action if the partner sent 0, then if it sent 1; P = pass/fold, B = bet/call).

    nice -n 19 .venv/bin/python scripts/describe_kuhn_bit.py
"""

from solvers.threads import limit_threads

limit_threads()

import games  # noqa: E402,F401
from games.augment import make_augmented_game  # noqa: E402
from games.tree import build_tree  # noqa: E402
from eval.best_response import guaranteed_value  # noqa: E402
from solvers.tmecor_cg import solve_tmecor  # noqa: E402

CARDS = "JQKA"
HISTORIES = {0: ["", "ppb", "pbb", "pbp"], 1: ["p", "b", "ppbb", "ppbp"]}


def main():
    tree = build_tree(make_augmented_game("kuhn_poker(players=3)", k=1, s="inf", rho="priv"))
    res = solve_tmecor(tree)
    print(f"V(1, inf, priv) = {res.value:.6f} (converged: {res.converged}), "
          f"{len(res.support)} joint plans in the support")
    for weight, prof in res.support:
        alone = guaranteed_value(tree, [(1.0, prof)])
        print(f"\nplan with weight {weight:.3f} (g of this plan alone: {alone:.4f})")
        bits = [{c: prof[p][f"{c}|r0@{c}:?"] for c in range(4)} for p in (0, 1)]
        for p in (0, 1):
            print(f"  bit of teammate {p}: " + " ".join(f"{CARDS[c]}->{b}" for c, b in bits[p].items()))
        for p in (0, 1):
            for h in HISTORIES[p]:
                cells = []
                for c in range(4):
                    acts = ""
                    for partner in (0, 1):
                        m = (bits[0][c], partner) if p == 0 else (partner, bits[1][c])
                        key = f"{c}{h}|r0@{c}:{m[0]},{m[1]}"
                        acts += "PB"[prof[p][key]] if key in prof[p] else "-"
                    cells.append(f"{CARDS[c]}:{acts}")
                print(f"  teammate {p} after '{h or '(start)'}': " + " ".join(cells))


if __name__ == "__main__":
    main()
