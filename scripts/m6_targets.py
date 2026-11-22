"""Milestone 6, task 3: targets for the larger games (blocker n = 16, suit blocker 4 x 4, attack 4 x 4).

Usage:
    .venv/bin/python scripts/m6_targets.py            # prints the table, writes results/m6_targets/targets.md

Each cell gets a lower and an upper bound and a label:
* lower: g(pi_T) of an explicit team strategy (``codes`` below), evaluated exactly
  against the adversary's best response by ``eval.onestep``;
* upper: the smallest of
  - uniform block: the adversary blocks a uniformly random class, so V <= 1 - 1/#classes
    (1 - 1/n, 1 - 1/S, 1 - 1/n^2);
  - Lemma 1 (blocker and coordinated attack, public channel, one round):
    V <= 1/4 at s = 0 and V <= 1 - 2^-s at s >= 1;
  - V(k, s, pub) <= V(k, inf, priv) (Proposition 1), with V(k, inf, priv) from the
    column-generation solver (results/m6_values) where it finished in 10 minutes.
"exact" when the bounds meet (the label names the upper bound used), "bound" otherwise.
The strategies are hand codes, so the lower bounds are not claimed to be optimal.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np  # noqa: E402

from eval import onestep  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def empty(game, k, s):
    M, nK = 2 ** k, 2 ** s
    return onestep.TeamPolicy(
        msg0=np.zeros((nK, game.n0, M)), msg1=np.zeros((nK, game.n1, M)),
        act0=np.full((nK, game.n0, M, M, game.n_act0), 1.0 / game.n_act0),
        act1=np.full((nK, game.n1, M, M, game.n_act1), 1.0 / game.n_act1))


def blocker_code(n, k, s, group):
    """Send the group x // group (log2(n/group) <= k bits), XOR its low s bits with the key;
    the guesser decodes and guesses uniformly inside the group. Teammate 1 sends 0."""
    game = onestep.card_blocker(n)
    pol = empty(game, k, s)
    pol.msg1[:, :, 0] = 1.0
    for K in range(2 ** s):
        for x in range(n):
            pol.msg0[K, x, (x // group) ^ K] = 1.0
        for m in range(n // group):
            pol.act1[K, 0, m, :, :] = 0.0
            g = m ^ K
            pol.act1[K, 0, m, :, g * group:(g + 1) * group] = 1.0 / group
    return game, pol


def suit_code(S, R, k, s, rank_bits):
    """Send (suit XOR key, top ``rank_bits`` of the rank); guess uniformly among the
    ranks consistent with the message. Teammate 1 sends 0."""
    game = onestep.suit_blocker(S, R)
    pol = empty(game, k, s)
    pol.msg1[:, :, 0] = 1.0
    rb = int(np.log2(R))
    for K in range(2 ** s):
        for x in range(S * R):
            su, ra = divmod(x, R)
            pol.msg0[K, x, ((su ^ K) << rank_bits) | (ra >> (rb - rank_bits))] = 1.0
        for su_m in range(S):
            for r_m in range(2 ** rank_bits):
                m = (su_m << rank_bits) | r_m
                su = su_m ^ K
                ranks = [r for r in range(R) if r >> (rb - rank_bits) == r_m]
                pol.act1[K, 0, m, :, :] = 0.0
                for r in ranks:
                    pol.act1[K, 0, m, :, su * R + r] = 1.0 / len(ranks)
    return game, pol


def attack_pad(n, k, s, pad0, pad1):
    """Each teammate sends its coordinate (k = log2 n bits), the low ``pad0`` / ``pad1`` bits
    XORed with its own part of the key; both decode and attack the weak target."""
    game = onestep.coordinated_attack(n, n)
    pol = empty(game, k, s)
    pol.act0[:] = 0.0
    pol.act1[:] = 0.0
    for K in range(2 ** s):
        K0, K1 = K & (2 ** pad0 - 1), (K >> pad0) & (2 ** pad1 - 1)
        for i in range(n):
            pol.msg0[K, i, i ^ K0] = 1.0
            pol.msg1[K, i, i ^ K1] = 1.0
        for m0 in range(n):
            for m1 in range(n):
                t = (m0 ^ K0) * n + (m1 ^ K1)
                pol.act0[K, m0 ^ K0, m0, m1, t] = 1.0
                pol.act1[K, m1 ^ K1, m0, m1, t] = 1.0
        # unreachable (own x inconsistent with own message): attack anything
        for p in (pol.act0, pol.act1):
            dead = p[K].sum(-1) == 0
            p[K][dead] = 1.0 / game.n_act0
    return game, pol


def attack_half(n):
    """s = 0: teammate 0 sends its row, teammate 1 only the top bit of its column; teammate 1
    then knows the target, teammate 0 attacks one of the two candidates at random."""
    k = int(np.log2(n))
    game = onestep.coordinated_attack(n, n)
    pol = empty(game, k, 0)
    pol.act0[:] = 1.0 / game.n_act0
    pol.act1[:] = 1.0 / game.n_act1
    half = n // 2
    for i in range(n):
        pol.msg0[0, i, i] = 1.0
    for j in range(n):
        pol.msg1[0, j, j // half] = 1.0
    for m0 in range(n):
        for m1 in range(2):
            pol.act0[0, m0, m0, m1, :] = 0.0
            for j in range(m1 * half, (m1 + 1) * half):
                pol.act0[0, m0, m0, m1, m0 * n + j] = 1.0 / half
            for j in range(m1 * half, (m1 + 1) * half):
                pol.act1[0, j, m0, m1, :] = 0.0
                pol.act1[0, j, m0, m1, m0 * n + j] = 1.0
    return game, pol


def lemma(s):
    return 0.25 if s == 0 else 1 - 2.0 ** -s


# V(k, inf, priv) from the column-generation solver (configs/m6_values.yaml, scripts/m6_values.sh,
# results/m6_values/*/0/summary.md; each solve finished in under 10 s and matches the closed form)
SOLVER = {("blocker16", 0): 0.05859375, ("blocker16", 1): 0.1171875, ("blocker16", 2): 0.234375,
          ("blocker16", 4): 0.9375, ("suit4x4", 0): 0.046875, ("suit4x4", 1): 0.09375,
          ("suit4x4", 2): 0.1875, ("suit4x4", 4): 0.75, ("attack4x4", 0): 0.234375,
          ("attack4x4", 1): 0.46875, ("attack4x4", 2): 0.9375}

# (game, k, s, rho): (strategy builder, description)
CELLS = [
    ("blocker16", 2, 2, "pub", lambda: blocker_code(16, 2, 2, 4), "groups of 4, both bits padded"),
    ("blocker16", 2, 1, "pub", lambda: blocker_code(16, 2, 1, 4), "groups of 4, one bit padded"),
    ("blocker16", 2, 0, "pub", lambda: blocker_code(16, 2, 0, 4), "groups of 4 in clear"),
    ("blocker16", 4, 4, "pub", lambda: blocker_code(16, 4, 4, 1), "card, all 4 bits padded"),
    ("blocker16", 4, 2, "pub", lambda: blocker_code(16, 4, 2, 1), "card, 2 bits padded"),
    ("blocker16", 4, 1, "pub", lambda: blocker_code(16, 4, 1, 1), "card, 1 bit padded"),
    ("blocker16", 4, 0, "pub", lambda: blocker_code(16, 4, 0, 2), "pair in clear, guess 50/50"),
    ("blocker16", 4, 0, "priv", lambda: blocker_code(16, 4, 0, 1), "card in clear"),
    ("suit4x4", 4, 4, "pub", lambda: suit_code(4, 4, 4, 2, 2), "suit padded, rank in clear"),
    ("suit4x4", 4, 2, "pub", lambda: suit_code(4, 4, 4, 2, 2), "suit padded, rank in clear"),
    ("suit4x4", 4, 1, "pub", lambda: suit_code(4, 4, 4, 1, 2), "one suit bit padded, rank in clear"),
    ("suit4x4", 2, 2, "pub", lambda: suit_code(4, 4, 2, 2, 0), "suit padded, no rank"),
    ("suit4x4", 4, 0, "priv", lambda: suit_code(4, 4, 4, 0, 2), "card in clear"),
    ("attack4x4", 2, 4, "pub", lambda: attack_pad(4, 2, 4, 2, 2), "both coordinates padded"),
    ("attack4x4", 2, 2, "pub", lambda: attack_pad(4, 2, 2, 1, 1), "one bit of each padded"),
    ("attack4x4", 2, 1, "pub", lambda: attack_pad(4, 2, 1, 1, 0), "one bit of the row padded"),
    ("attack4x4", 2, 0, "pub", lambda: attack_half(4), "row in clear, half the column"),
    ("attack4x4", 2, 0, "priv", lambda: attack_pad(4, 2, 0, 0, 0), "both coordinates in clear"),
]


def bounds(name, game, k, s, rho, lower):
    ups = [(1.0 - 1.0 / game.n_block, "uniform block")]
    if rho == "pub" and not name.startswith("suit"):
        ups.append((lemma(s), "Lemma 1"))
    if (name, k) in SOLVER:
        ups.append((SOLVER[(name, k)], "solver V(k,inf,priv)"))
    hi, why = min(ups, key=lambda u: u[0])
    exact = abs(hi - lower) < 1e-9
    return hi, ("exact (code + " + why + ")") if exact else f"bound (upper: {why})"


def targets():
    rows = []
    for name, k, s, rho, build, desc in CELLS:
        game, pol = build()
        lo, _ = onestep.guaranteed_value(game, pol, rho)
        hi, label = bounds(name, game, k, s, rho, lo)
        rows.append({"game": name, "k": k, "s": s, "rho": rho, "lo": lo, "hi": hi,
                     "label": label, "code": desc})
    return rows


def main():
    rows = targets()
    lines = ["| game | k | s | ρ | lower (code, exact BR) | upper | label | code |",
             "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['game']} | {r['k']} | {r['s']} | {r['rho']} | {r['lo']:.4f} | "
                     f"{r['hi']:.4f} | {r['label']} | {r['code']} |")
    text = "\n".join(lines)
    print(text)
    out = ROOT / "results" / "m6_targets"
    out.mkdir(parents=True, exist_ok=True)
    (out / "targets.md").write_text("# Milestone 6 targets (scripts/m6_targets.py)\n\n" + text + "\n")
    return rows


if __name__ == "__main__":
    main()
