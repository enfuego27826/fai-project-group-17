"""Milestone 5 experiments: adversary strength, exploitable leakage, opponent models, curricula.

Usage:
    nice -n 19 .venv/bin/python scripts/run_m5.py --config configs/m5_<dose|suit|model|curriculum>.yaml

Like scripts/run_m4.py (unchanged), with these opt-in additions:
* method fields ``opponent: noisy_br`` + ``epsilon`` (Task 1) and
  ``opponent: model`` + ``model_window`` / ``model_every`` (Task 3), passed to
  ``learning.tabular_pg.train``;
* ``warm_start: priv`` (Task 4): train ``iterations`` on the private channel of
  the same cell, then continue on the cell itself for ``iterations`` more from
  the private run's logits (team information states are identical in both);
* exploitable leakage I(M; phi(X)) next to I(M; X), where phi(X) is the part of
  the private information the adversary's payoff depends on (``PHI`` below:
  the suit in the suit blocker; X itself in the card blocker and coordinated
  attack, so there the two coincide);
* the behavior checks of Milestone 3 plus a suit-blocker classification.
Milestone 6 adds the method fields ``adv_lr_mult`` / ``adv_steps`` (two-timescale
self-play), ``exact_gradient`` and ``init_scale`` (exact-gradient diagnostic), and
a per-method ``seeds`` list; all default to the Milestone 5 behavior. Milestone 8 adds
``resp_every`` (log the responsiveness gap and leakage; evaluation only).
Every value is g(pi_T) from the exact best response. The run stops if any g
exceeds the upper end of its cell's exact value (a bug).
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
import math  # noqa: E402
import platform  # noqa: E402
import time  # noqa: E402
from multiprocessing import Pool  # noqa: E402

import numpy as np  # noqa: E402
import yaml  # noqa: E402
from scipy import stats  # noqa: E402

import games  # noqa: E402,F401
from eval.best_response import guaranteed_value  # noqa: E402
from eval.leakage import mutual_information  # noqa: E402
from games.suit_blocker import suit_phi  # noqa: E402
from learning.tabular_pg import PGConfig, train  # noqa: E402
from run_m4 import cells_of, fmt_v, v_range  # noqa: E402
from run_marl import behavior, tree_of  # noqa: E402
from run_values import config_hash, git_info  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CFG = None


PHI = {"suit_blocker": suit_phi}


def _init(cfg):
    global CFG
    CFG = cfg


def pg_config(m):
    return PGConfig(iterations=m["iterations"], batch=m["batch"], lr=m["lr"],
                    log_every=m.get("log_every", 50), lr_decay=m.get("lr_decay", "const"),
                    entropy=m.get("entropy", 0.0), epsilon=m.get("epsilon", 0.0),
                    model_window=m.get("model_window", 512), model_every=m.get("model_every", 10),
                    init_scale=m.get("init_scale", 0.0), adv_lr_mult=m.get("adv_lr_mult", 1.0),
                    adv_steps=m.get("adv_steps", 1), exact_gradient=m.get("exact_gradient", False),
                    resp_every=m.get("resp_every", 0))


def m_seeds(cfg, mi):
    """Seeds of method ``mi``: its own ``seeds`` field if set (Milestone 6), else the config's."""
    return cfg["methods"][mi].get("seeds", cfg["seeds"])


def transfer_theta(src_tree, dst_tree, theta):
    """Map each teammate's logits from ``src_tree`` to ``dst_tree`` by information-state key."""
    out = []
    for t, th in zip(src_tree.team, theta):
        src, dst = src_tree.players[t], dst_tree.players[t]
        index = {key: I for I, key in enumerate(src.infoset_keys)}
        new = np.zeros(dst.num_seqs)
        for J, key in enumerate(dst.infoset_keys):
            I = index[key]
            assert list(src.infoset_actions[I]) == list(dst.infoset_actions[J])
            n = dst.infoset_num_actions[J]
            new[dst.infoset_first_seq[J]:dst.infoset_first_seq[J] + n] = \
                th[src.infoset_first_seq[I]:src.infoset_first_seq[I] + n]
        out.append(new)
    return out


def suit_check(r, V, game_cfg):
    """Suit blocker, public cells: what the message does with the suit and the rank.

    I(M; suit) is what the adversary learns about the suit, I(M; suit | K) what
    the key-holding guesser learns; a padded suit has the first near 0 and the
    second near log2 S. The rank information is I(M; X) - I(M; suit).
    """
    R = int(game_cfg.get("ranks", 2))
    ex, tot, gv = r["leak_exploitable"], r["leak_bits"], r["g"]
    dec = r.get("leak_decodable")
    rank = tot - ex
    rank_txt = ("rank in clear" if rank > math.log2(R) - 0.1 else
                "no rank" if rank < 0.1 else "rank partly sent")
    if ex >= 0.1:
        suit_txt = "suit leaks"
    elif dec is not None and dec > 0.9:
        suit_txt = "suit padded"
    elif dec is not None and dec < 0.1:
        suit_txt = "suit not sent"
    else:
        suit_txt = "suit partly padded"
    what = f"{suit_txt}, {rank_txt}"
    ok = what == "suit padded, rank in clear" and gv >= V - 0.02
    return "pad suit only", ok, (f"g={gv:.3f} vs V={V:.3f}; {what}; I(M;X)={tot:.2f}, "
                                 f"I(M;suit)={ex:.2f}, I(M;suit|K)={dec if dec is None else round(dec, 2)}")


def run_one(task):
    mi, gi, k, s, rho, seed = task
    m, g = CFG["methods"][mi], CFG["games"][gi]
    tree = tree_of(g, k, s, rho)
    cfg = pg_config(m)
    t0 = time.perf_counter()
    init_theta, pre_episodes = None, 0
    if m.get("warm_start") == "priv":
        src = tree_of(g, k, s, "priv")
        pre = train(src, cfg, seed=seed, opponent=m["opponent"])
        init_theta = transfer_theta(src, tree, pre.theta)
        pre_episodes = pre.episodes
    res = train(tree, cfg, seed=seed, opponent=m["opponent"], init_theta=init_theta)
    seconds = time.perf_counter() - t0
    outputs = {}
    if "last" in m["outputs"]:
        outputs["last"] = (res.policies, res.curve)
    if "avg" in m["outputs"]:
        outputs["avg"] = (res.avg_policies, res.avg_curve)
    phi = PHI.get(g.get("phi"))
    out = []
    for oname, (pol, curve) in outputs.items():
        strategy = [(1.0, pol)]
        g_val = guaranteed_value(tree, strategy)
        leak = mutual_information(tree, strategy, channel="all")
        leak_ex = mutual_information(tree, strategy, channel="all", phi=phi) if phi else leak
        leak_dec = (mutual_information(tree, strategy, channel="all", phi=phi, given_key=True)
                    if phi else None)
        g_priv = guaranteed_value(tree_of(g, k, s, "priv"), strategy) if rho == "pub" else g_val
        out.append({"method": f"{m['name']}/{oname}", "game": g["name"], "k": k, "s": s,
                    "rho": rho, "seed": seed, "g": g_val, "leak_bits": leak,
                    "leak_exploitable": leak_ex, "leak_decodable": leak_dec,
                    "g_same_policy_priv": g_priv,
                    "seconds": seconds, "episodes": res.episodes + pre_episodes,
                    "curve": curve, "policies": {str(p): v for p, v in pol.items()},
                    **({"resp_log": res.resp_log} if res.resp_log is not None else {})})
    return out


def checks_of(cfg, r):
    lo, hi = v_range(cfg, r["game"], r["k"], r["s"], r["rho"])
    g = next(g for g in cfg["games"] if g["name"] == r["game"])
    if g.get("phi") == "suit_blocker":
        return suit_check(r, hi, g) if r["rho"] == "pub" else None
    if lo == hi and r["game"] in ("attack2x2", "blocker4"):
        return behavior(r, lo, v_range(cfg, r["game"], r["k"], r["s"], "priv")[0])
    return None


def summarize(cfg, runs):
    cells = {}
    for r in runs:
        cells.setdefault((r["method"], r["game"], r["k"], r["s"], r["rho"]), []).append(r)
    rows, checks = [], []
    for (method, game, k, s, rho), rs in cells.items():
        lo, hi = v_range(cfg, game, k, s, rho)
        gs = np.array([r["g"] for r in rs])
        n = len(gs)
        half = stats.t.ppf(0.975, n - 1) * gs.std(ddof=1) / np.sqrt(n) if n > 1 else float("nan")
        rs_sorted = sorted(rs, key=lambda r: r["seed"])
        found = [c for r in rs_sorted if (c := checks_of(cfg, r))]
        for r, c in zip([r for r in rs_sorted if checks_of(cfg, r)], found):
            checks.append((method, game, k, s, rho, r["seed"], *c))
        rows.append({"method": method, "game": game, "k": k, "s": s, "rho": rho, "V_lo": lo,
                     "V_hi": hi, "g_mean": gs.mean(), "g_ci95": half,
                     "gap_mean": hi - gs.mean(),
                     "leak_mean": float(np.mean([r["leak_bits"] for r in rs])),
                     "leak_ex_mean": float(np.mean([r["leak_exploitable"] for r in rs])),
                     "leak_dec_mean": (float(np.mean([r["leak_decodable"] for r in rs]))
                                       if rs[0].get("leak_decodable") is not None else None),
                     "cost_mean": float(np.mean([r["g_same_policy_priv"] - r["g"] for r in rs])),
                     "check": found[0][0] if found else "",
                     "check_yes": sum(c[1] for c in found), "seeds": n,
                     "seconds": float(np.mean([r["seconds"] for r in rs]))})
    return rows, checks


def format_tables(rows, checks):
    lines = ["| method | game | k | s | ρ | exact V | g(π_T) mean ± 95% CI | gap | I(M;X) | "
             "I(M;φ(X)) | cost of leak | check | yes / seeds | time/run |", "|" + "---|" * 14]
    for r in rows:
        cost = f"{r['cost_mean']:.3f}" if r["rho"] == "pub" else ""
        yes = f"{r['check_yes']} / {r['seeds']}" if r["check"] else ""
        lines.append(
            f"| {r['method']} | {r['game']} | {r['k']} | {r['s']} | {r['rho']} "
            f"| {fmt_v(r['V_lo'], r['V_hi'])} | {r['g_mean']:.3f} ± {r['g_ci95']:.3f} "
            f"| {r['gap_mean']:.3f} | {r['leak_mean']:.2f} | {r['leak_ex_mean']:.2f} | {cost} "
            f"| {r['check']} | {yes} | {r['seconds']:.1f}s |")
    if checks:
        lines += ["", "| method | game | k | s | ρ | seed | check | yes/no | what the policy does |",
                  "|" + "---|" * 9]
        for method, game, k, s, rho, seed, name, ok, desc in checks:
            lines.append(f"| {method} | {game} | {k} | {s} | {rho} | {seed} | {name} "
                         f"| {'yes' if ok else 'no'} | {desc} |")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    if "exact_values_from" in cfg:
        merged = {}
        for src in np.atleast_1d(cfg["exact_values_from"]):
            merged.update(yaml.safe_load((ROOT / src).read_text())["exact_values"])
        cfg["exact_values"] = {**merged, **cfg.get("exact_values", {})}
    out = ROOT / "results" / cfg["experiment"] / config_hash(cfg) / "seeds"
    (out / "runs").mkdir(parents=True, exist_ok=True)
    (out / "config.yaml").write_text(yaml.safe_dump(cfg, sort_keys=False))
    (out / "run_info.json").write_text(json.dumps({
        **git_info(), "python": platform.python_version(), "workers": cfg["workers"],
        "threads_per_worker": 1, "started": time.strftime("%Y-%m-%d %H:%M:%S"),
        "argv": sys.argv}, indent=2))
    tasks = [(mi, gi, k, s, rho, seed) for mi in range(len(cfg["methods"]))
             for gi, g in enumerate(cfg["games"]) for (k, s, rho) in cells_of(g)
             for seed in m_seeds(cfg, mi)]
    tasks.sort(key=lambda t: -t[2] - t[3] - 2 * (cfg["methods"][t[0]].get("warm_start") is not None))
    t0 = time.perf_counter()
    runs = []
    with Pool(cfg["workers"], initializer=_init, initargs=(cfg,)) as pool:
        for outs in pool.imap_unordered(run_one, tasks):
            for r in outs:
                lo, hi = v_range(cfg, r["game"], r["k"], r["s"], r["rho"])
                if r["g"] > hi + 1e-6:
                    pool.terminate()
                    raise RuntimeError(f"g = {r['g']} exceeds V <= {hi} in {r['game']} k={r['k']} "
                                       f"s={r['s']} {r['rho']} seed {r['seed']} ({r['method']}): bug")
                name = (f"{r['method'].replace('/', '-')}_{r['game']}_k{r['k']}_s{r['s']}_"
                        f"{r['rho']}_seed{r['seed']}.json")
                (out / "runs" / name).write_text(json.dumps(r))
                runs.append(r)
                print(f"{r['method']:22s} {r['game']:9s} k={r['k']} s={r['s']} {r['rho']:4s} "
                      f"seed {r['seed']:2d}  g={r['g']:+.4f}  V<={hi:+.4f}  "
                      f"leak={r['leak_bits']:.3f}/{r['leak_exploitable']:.3f}  "
                      f"({r['seconds']:.1f}s)", flush=True)
    wall = time.perf_counter() - t0
    morder = {m["name"]: i for i, m in enumerate(cfg["methods"])}
    corder = {(g["name"], *c): i for i, (g, c) in enumerate(
        (g, c) for g in cfg["games"] for c in cells_of(g))}
    runs.sort(key=lambda r: (morder[r["method"].split("/")[0]], r["method"],
                             corder[(r["game"], r["k"], r["s"], r["rho"])], r["seed"]))
    rows, checks = summarize(cfg, runs)
    table = format_tables(rows, checks)
    (out / "metrics.json").write_text(json.dumps(
        {"cells": rows, "checks": checks, "wall_seconds": wall}, indent=2, default=float))
    (out / "summary.md").write_text(table + f"\n\nwall time {wall:.0f} s for {len(tasks)} runs\n")
    print()
    print(table)
    print(f"\nwall time {wall:.0f} s for {len(tasks)} runs; results in {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
