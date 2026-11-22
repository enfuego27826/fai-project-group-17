"""Print the report's tables (and the numbers quoted around them) from the committed results.

Usage:
    .venv/bin/python scripts/report_tables.py            # all tables
    .venv/bin/python scripts/report_tables.py 1 2 3      # only these tables ("facts" = inline numbers)

Every value is read from results/*/metrics.json (or summary/analysis files) written by the
configs named in README.md; nothing is typed in. report/NUMBERS.md maps each report number to
the line of this output (or other results file) it comes from.

Table 1 and Table 2 apply the report's theorems as extra upper bounds on public cells:
Lemma 1 (V(k, 0, pub) <= 1/4, V(k, s, pub) <= 1 - 2^-s) and V(k, s, pub) <= V(k, s, priv)
(Proposition 1). Cells whose bounds then meet are marked with a dagger (certified by a theorem).
"""

import glob
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOL = 1e-7


def one(pattern):
    files = sorted(glob.glob(str(ROOT / pattern)))
    if len(files) != 1:
        raise FileNotFoundError(f"expected one file for {pattern}, found {files}")
    return json.loads(Path(files[0]).read_text())


def frac(x, digits=3):
    f = Fraction(x).limit_denominator(100)
    return str(f) if abs(float(f) - x) < 1e-6 else f"{x:.{digits}f}"


def lemma(s):
    return 0.25 if s == 0 else 1 - 2.0 ** -s


def exact_table(rows, lemma_games):
    """{(game, k, s, rho): (lo, hi, certified_by_theorem)} with s an int or 'inf'."""
    V = {}
    for r in rows:
        s = r["s"] if r["s"] == "inf" else int(r["s"])
        V[(r["game"], r["k"], s, r["rho"])] = [r["lower"], r["upper"], False]
    for (g, k, s, rho), v in V.items():
        if rho == "pub" and s != "inf" and g in lemma_games and lemma(s) < v[1] - TOL:
            v[1], v[2] = lemma(s), True
        priv = V.get((g, k, s, "priv"))
        if rho == "pub" and priv and priv[1] < v[1] - TOL:
            v[1], v[2] = priv[1], True
    return V


def fmt_cell(lo, hi, cert=False):
    mark = "†" if cert and hi - lo < TOL else ""
    return (frac(lo) + mark) if hi - lo < TOL else f"[{lo:.4f}, {hi:.4f}]"


def table1():
    rows = one("results/m2_values/*/0/metrics.json") + one("results/m25_values/*/0/metrics.json")
    V = exact_table(rows, {"blocker4", "blocker8", "attack2x2", "attack3x3"})
    print("Table 1: price of eavesdropping PoE(k, s) = V(k,s,priv) - V(k,s,pub); public value in "
          "parentheses (results/m2_values, results/m25_values; † = closed with Lemma 1 / Prop. 1)")
    print(f"{'game':14s} {'k':>2s}  {'s=0':>28s}  {'s=1':>28s}  {'s=2':>28s}  smallest s (of 0..2) with PoE = 0")
    for g, label, ks in [("blocker4", "blocker n=4", [1, 2]), ("blocker8", "blocker n=8", [3]),
                         ("attack2x2", "attack 2x2", [1]), ("attack3x3", "attack 3x3", [1, 2])]:
        for k in ks:
            cells, zero = [], None
            for s in (0, 1, 2):
                pr, pu = V[(g, k, s, "priv")], V[(g, k, s, "pub")]
                lo, hi = pr[0] - pu[1], pr[1] - pu[0]
                poe = frac(lo) if hi - lo < TOL else f"[{lo:.3f}, {hi:.3f}]"
                cells.append(f"{poe} ({fmt_cell(pu[0], pu[1], pu[2])})")
                if zero is None and hi < TOL:
                    zero = s
            print(f"{label:14s} {k:>2d}  " + "  ".join(f"{c:>28s}" for c in cells)
                  + f"  {zero if zero is not None else '> 2 (see Lemma 1, Prop. 2)'}")
    print("other values quoted in Section 5:")
    for key in [("attack2x2", 0, "inf", "priv"), ("attack3x3", 1, "inf", "priv"),
                ("attack3x3", 2, "inf", "priv"), ("attack3x3", 2, 0, "pub"), ("attack3x3", 1, 0, "priv")]:
        lo, hi, _ = V[key]
        print(f"  V{key} = [{lo:.9f}, {hi:.9f}]  ({frac(lo)})")
    kuhn = one("results/m2_values/*/0/metrics.json")
    for r in kuhn:
        if r["game"] == "kuhn3" and (str(r["s"]), r["rho"]) in (("inf", "priv"), ("inf", "pub"), ("0", "priv")) and r["k"] in (0, 1, 2):
            print(f"  kuhn3 k={r['k']} s={r['s']} {r['rho']}: [{r['lower']:+.10f}, {r['upper']:+.10f}] "
                  f"{r['status']}, leak {r.get('leak_bits')}")


def table2():
    rows = []
    for f in sorted(glob.glob(str(ROOT / "results/m5_suit_values/*/0/metrics.json"))):
        rows += json.loads(Path(f).read_text())
    V = exact_table(rows, {"suit2x2", "suit2x4", "suit4x2"})
    print("Table 2: suit blocker (results/m5_suit_values; † = closed with Lemma 1 / Prop. 1)")
    print(f"{'S x R':6s} {'k':>2s} {'V(k,inf,priv)':>14s} {'V(k,0,pub)':>12s} {'V(k,1,pub)':>12s} "
          f"{'V(k,2,pub)':>12s}  smallest s with PoE = 0   leak of the solver's (k,s*,pub) strategy")
    leak = {(r["game"], r["k"], str(r["s"]), r["rho"]): r.get("leak_bits") for r in rows}
    for g, label, k in [("suit2x2", "2x2", 2), ("suit2x4", "2x4", 2), ("suit2x4", "2x4", 3),
                        ("suit4x2", "4x2", 2), ("suit4x2", "4x2", 3)]:
        pv = V[(g, k, "inf", "priv")]
        pubs = [V[(g, k, s, "pub")] for s in (0, 1, 2)]
        zero = next((s for s, p in zip((0, 1, 2), pubs) if pv[0] - p[1] < TOL and p[0] > pv[1] - TOL), None)
        print(f"{label:6s} {k:>2d} {fmt_cell(pv[0], pv[1]):>14s} "
              + " ".join(f"{fmt_cell(*p):>12s}" for p in pubs)
              + f"  {zero}   {leak.get((g, k, str(zero), 'pub'))}")


def method_rows(cells, checks, method):
    cs = [c for c in cells if c["method"] == method]
    chk = [c for c in checks if c[0] == method]
    pad = [c for c in chk if c[6] == "key as pad"]
    quiet = [c for c in chk if c[6] == "quiet or coarse" and (c[1], c[2], c[3], c[4]) == ("attack2x2", 1, 0, "pub")]
    return {"gap": sum(c["gap_mean"] for c in cs) / len(cs), "n": len(cs),
            "within": sum(c["gap_mean"] <= 0.005 for c in cs),
            "pad": (sum(c[7] for c in pad), len(pad)), "quiet": (sum(c[7] for c in quiet), len(quiet))}


def table3():
    seeds = one("results/m4_seeds/*/seeds/metrics.json")
    sp = one("results/m4_selfplay/*/seeds/metrics.json")
    ps = one("results/m4_psro/*/seeds/metrics.json")
    ku = one("results/m4_kuhn/*/seeds/metrics.json")
    print("Table 3: methods over the 30 toy cells and the 9 Kuhn cells (results/m4_seeds, "
          "m4_selfplay, m4_psro, m4_kuhn)")
    print(f"{'method':28s} {'mean gap':>9s} {'cells within 0.005':>19s} {'pad':>7s} {'quiet':>7s} {'Kuhn mean gap':>14s}")
    for label, src, method, kmethod in [
            ("PG vs BR, last (20 seeds)", seeds, "pg_vs_br/last", "pg_vs_br/last"),
            ("PG vs BR, averaged", sp, "pg_vs_br/avg", "pg_vs_br/avg"),
            ("self-play, last", sp, "self_play/last", "self_play/last"),
            ("self-play, averaged", sp, "self_play/avg", "self_play/avg"),
            ("Team-PSRO-lite", ps, "psro/single", "psro/single")]:
        r = method_rows(src["cells"], src["checks"], method)
        kc = [c for c in ku["cells"] if c["method"] == kmethod]
        kg = sum(c["gap_mean"] for c in kc) / len(kc)
        print(f"{label:28s} {r['gap']:9.3f} {r['within']:>12d}/{r['n']:<6d} "
              f"{r['pad'][0]:>3d}/{r['pad'][1]:<3d} {r['quiet'][0]:>3d}/{r['quiet'][1]:<3d} {kg:14.3f}"
              f"   (Kuhn cells: {len(kc)})")
    print("Kuhn PG vs BR last, g per cell:", ", ".join(
        f"({c['k']},{c['s']}) {c['g_mean']:+.3f}±{c['g_ci95']:.3f}" for c in ku["cells"] if c["method"] == "pg_vs_br/last"))


def table4():
    m = one("results/m4_seeds/*/seeds/metrics.json")
    print("Table 4: public cells, PG vs BR last iterate, 20 seeds (results/m4_seeds)")
    print(f"{'game':9s} {'k':>2s} {'s':>2s} {'V':>5s} {'g mean ± 95% CI':>18s} {'leak':>6s}   private-cell leak")
    priv = {(c["game"], c["k"], c["s"]): c["leak_mean"] for c in m["cells"] if c["rho"] == "priv"}
    for c in m["cells"]:
        if c["rho"] == "pub":
            print(f"{c['game']:9s} {c['k']:>2d} {c['s']:>2d} {frac(c['V_hi']):>5s} "
                  f"{c['g_mean']:.3f} ± {c['g_ci95']:.3f}    {c['leak_mean']:.2f}   "
                  f"{priv[(c['game'], c['k'], c['s'])]:.2f}")


def table5():
    model = one("results/m5_model/*/seeds/metrics.json")
    t1 = one("results/m5_model_t1/*/seeds/metrics.json")
    ts = one("results/m6_timescale/*/seeds/metrics.json")
    print("Table 5: same team learner, different training adversaries, 10 seeds "
          "(results/m5_model, m5_model_t1, m6_timescale)")
    print(f"{'training adversary':44s} {'pad':>6s} {'quiet':>6s} {'suit':>6s} {'leak quiet':>11s} {'mean gap':>9s}")
    for label, src, method in [("exact best response", model, "exact_br/last"),
                               ("team model, N = 2048, refit every iteration", t1, "model_N2048_T1/last"),
                               ("team model, N = 32, refit every iteration", t1, "model_N32_T1/last"),
                               ("team model, N = 2048, refit every 10", model, "model_N2048/last"),
                               ("team model, N = 32, refit every 10", model, "model_N32/last"),
                               ("REINFORCE adversary (self-play)", model, "reinforce_adv/last"),
                               ("REINFORCE adversary, 4 updates per team update", ts, "adv_m1_s4/last")]:
        cs = [c for c in src["cells"] if c["method"] == method]
        pad = sum(c["check_yes"] for c in cs if c["check"] == "key as pad")
        quiet = [c for c in cs if c["check"] == "quiet or coarse"][0]
        suit = [c for c in cs if c["check"] == "pad suit only"][0]
        gap = sum(c["gap_mean"] for c in cs) / len(cs)
        print(f"{label:44s} {pad:>3d}/30 {quiet['check_yes']:>3d}/10 {suit['check_yes']:>3d}/10 "
              f"{quiet['leak_mean']:11.2f} {gap:9.3f}")


def figure1():
    m = one("results/m5_dose/*/seeds/metrics.json")
    print("Figure 1 data (results/m5_dose): eps, pad / 30, quiet / 10, mean leakage on pad cells, quiet cell")
    by = {}
    for c in m["cells"]:
        by.setdefault(float(c["method"].split("/")[0][3:]), []).append(c)
    for eps in sorted(by):
        cs = by[eps]
        pads = [c for c in cs if c["check"] == "key as pad"]
        q = [c for c in cs if c["check"] == "quiet or coarse"][0]
        print(f"  eps={eps:<5g} pad {sum(c['check_yes'] for c in pads):>2d}/30  quiet {q['check_yes']:>2d}/10  "
              f"leak pad {sum(c['leak_mean'] for c in pads) / 3:.2f}  leak quiet {q['leak_mean']:.2f}")


def facts():
    print("Inline numbers (Sections 6.1 to 6.3 and Appendix B):")
    cur = one("results/m5_curriculum/*/seeds/metrics.json")
    for c in cur["cells"]:
        if c["method"] in ("warm_priv/avg", "warm_priv/last", "scratch10k/last"):
            print(f"  curriculum {c['method']:16s} {c['game']} ({c['k']},{c['s']},pub) g {c['g_mean']:.3f} "
                  f"check_yes {c.get('check_yes')}")
    eg = one("results/m6_exactgrad/*/seeds/metrics.json")
    print("  exact-gradient diagnostic (results/m6_exactgrad): see summary.md; reach counts:")
    import collections
    for (meth, n) in sorted(collections.Counter(
            c["method"] for c in eg["cells"]).items()):
        cs = [c for c in eg["cells"] if c["method"] == meth]
        print(f"    {meth:20s} g by cell: " + ", ".join(f"{c['game']}({c['k']},{c['s']}) {c['g_mean']:.3f}" for c in cs))
    diag = (ROOT / "results/m6_adv_diag/summary.md").read_text().splitlines()
    print("  frozen-team REINFORCE adversary (results/m6_adv_diag/summary.md):", len(diag) - 2, "rows")
    an = json.loads((ROOT / "results/m8_resp/analysis.json").read_text())
    for cell, v in an["cells"].items():
        print(f"  responsiveness {cell}: rho {v['rho']:+.2f} [{v['ci'][0]:+.2f}, {v['ci'][1]:+.2f}], "
              f"g {v['rho_g']:+.2f}, within-type {v['within']:+.2f} [{v['within_ci'][0]:+.2f}, {v['within_ci'][1]:+.2f}]")
    su = one("results/m5_suit/*/seeds/metrics.json")
    for c in su["cells"]:
        if c["method"] == "pg_vs_br/last":
            print(f"  suit learning {c['game']} ({c['k']},{c['s']},pub): g {c['g_mean']:.3f}, V {frac(c['V_hi'])}, "
                  f"I(M;X) {c['leak_mean']:.2f}, I(M;suit) {c['leak_ex_mean']:.2f}, check {c['check_yes']}/{c['seeds']}")
    nn = one("results/m6_neural/*/seeds/metrics.json")
    mlp = [c for c in nn["cells"] if c["method"] != "tabular_br"]
    print(f"  neural (results/m6_neural): {sum(c['check_yes'] for c in mlp)} of "
          f"{sum(c['seeds'] for c in mlp)} MLP runs reach the target; private cells: " + ", ".join(
              f"{c['method']} {c['game']} {c['g_mean']:.3f}" for c in nn["cells"] if c["rho"] == "priv"))
    print("  wall times (metrics.json wall_seconds):")
    for exp in ["m4_seeds", "m4_selfplay", "m4_psro", "m5_dose", "m5_model", "m6_timescale",
                "m5_curriculum", "m6_neural", "m8_resp", "m7_tabinit", "m7_neural_diag",
                "m7_neural_combo", "m7_neural_gate"]:
        m = one(f"results/{exp}/*/seeds/metrics.json")
        secs = [c["seconds"] for c in m["cells"]]
        n = sum(c["seeds"] for c in m["cells"])
        print(f"    {exp:16s} {m['wall_seconds']:7.0f} s for {n} runs; per run {min(secs):.0f} to {max(secs):.0f} s")


def runs(pattern):
    import csv
    files = sorted(glob.glob(str(ROOT / pattern)))
    if len(files) != 1:
        raise FileNotFoundError(f"expected one file for {pattern}, found {files}")
    return list(csv.DictReader(open(files[0])))


def counts():
    """Counts over seeds quoted in Sections 6.1 to 6.3 (from results/*/runs.csv)."""
    print("Counts over seeds (results/*/*/seeds/runs.csv):")
    V = {("blocker4", 1, 0): 0.25, ("blocker4", 2, 0): 0.25, ("blocker4", 2, 1): 0.5, ("attack2x2", 1, 1): 0.5}
    for meth in ("exact_random/last", "sampled_random/last", "exact_random/avg", "sampled_random/avg"):
        rs = [r for r in runs("results/m6_exactgrad/*/seeds/runs.csv") if r["method"] == meth]
        hit = sum(float(r["g"]) >= V[(r["game"], int(r["k"]), int(r["s"]))] - 0.02 for r in rs)
        print(f"  exact-gradient diagnostic {meth:20s} reach V (within 0.02): {hit} of {len(rs)}")
    for meth in ("warm_priv/last", "warm_priv/avg", "scratch10k/last", "scratch20k/last"):
        rs = [r for r in runs("results/m5_curriculum/*/seeds/runs.csv") if r["method"] == meth]
        for cell in V:
            cr = [r for r in rs if (r["game"], int(r["k"]), int(r["s"])) == cell]
            at_v = sum(float(r["g"]) >= V[cell] - 0.02 for r in cr)
            at_0 = sum(float(r["g"]) < 0.01 for r in cr)
            print(f"  curriculum {meth:16s} {cell}: at V {at_v}/{len(cr)}, at 0 {at_0}/{len(cr)}")
    seeds = runs("results/m4_seeds/*/seeds/runs.csv")
    for cell in [("blocker4", 1, 0), ("blocker4", 2, 0), ("blocker4", 2, 1)]:
        gs = [float(r["g"]) for r in seeds if (r["game"], int(r["k"]), int(r["s"])) == cell and r["rho"] == "pub"]
        print(f"  PG vs BR from scratch (m4_seeds, 20 seeds) {cell} pub: max g {max(gs):.3f}")
    m = one("results/m4_seeds/*/seeds/metrics.json")
    import re
    fail = [float(re.search(r"leak=([\d.]+)", c[8]).group(1)) for c in m["checks"]
            if c[6] == "key as pad" and not c[7]]
    print(f"  m4_seeds pad check: {len(fail)} failing runs, their mean leakage {sum(fail) / len(fail):.3f} bits")
    diag = runs("results/m6_adv_diag/runs.csv")
    close = sum(float(r["u_trained_adversary"]) - float(r["g_exact_br"]) <= 0.002 for r in diag)
    print(f"  frozen-team REINFORCE adversary within 0.002 of the exact BR value: {close} of {len(diag)}")
    nn = runs("results/m6_neural/*/seeds/runs.csv")
    print(f"  m6_neural MLP public cells, g max vs REINFORCE adversary: "
          f"{max(float(r['g']) for r in nn if r['method'] == 'reinforce_adv' and r['rho'] == 'pub'):.3f}")
    for exp in ("m7_neural_combo", "m7_neural_gate", "m7_tabinit"):
        rs = runs(f"results/{exp}/*/seeds/runs.csv")
        by = {}
        for r in rs:
            by.setdefault((r["method"], r["game"], r["k"], r["s"], r["rho"]), []).append(float(r["g"]))
        for key, gs in sorted(by.items()):
            if key[4] == "priv":
                print(f"  {exp} {key}: g per seed " + ", ".join(f"{g:.3f}" for g in gs))
    ku = one("results/m4_kuhn/*/seeds/metrics.json")
    for meth in ("pg_vs_br/last", "pg_vs_br/avg"):
        cs = [c for c in ku["cells"] if c["method"] == meth]
        k1 = [c["g_mean"] for c in cs if c["k"] >= 1]
        beat = [(c["k"], c["s"]) for c in cs if c["g_mean"] - c["g_ci95"] > -1 / 24]
        print(f"  Kuhn {meth}: k >= 1 from {max(k1):+.3f} to {min(k1):+.3f}; k = 0 "
              + ", ".join(f"{c['g_mean']:+.3f}" for c in cs if c["k"] == 0) + f"; beat -1/24 at 95%: {beat}")
    for name, pat in (("self-play", "results/m4_selfplay/*/seeds/metrics.json"), ("PSRO", "results/m4_psro/*/seeds/metrics.json")):
        mm = one(pat)
        for meth in sorted({c["method"] for c in mm["cells"]} - {"pg_vs_br/last", "pg_vs_br/avg"}):
            cs = [c for c in mm["cells"] if c["method"] == meth and c["rho"] == "pub"]
            print(f"  {name} {meth}: public cells mean leakage {sum(c['leak_mean'] for c in cs) / len(cs):.2f}, "
                  f"max {max(c['leak_mean'] for c in cs):.2f} bits; max cost of leak {max(c['cost_mean'] for c in cs):.2f}")


TABLES = {"1": table1, "2": table2, "3": table3, "4": table4, "5": table5, "fig1": figure1, "facts": facts,
          "counts": counts}


def main():
    which = sys.argv[1:] or list(TABLES)
    for w in which:
        TABLES[w]()
        print()


if __name__ == "__main__":
    main()
