# Where every number in the report comes from

Checked against the compiled report `main.pdf` (build of 22 Nov 2026, 14:06, 12 pages). The LaTeX source was not in this repository when the check was made, so the corrections below are listed for the authors to apply in `report/main.tex`. The PDF has not been changed.

All commands are run from the repository root with the project environment (see `README.md`). `T` stands for `python scripts/report_tables.py`, which prints every table and the inline counts from the committed results files without any solver or training. `F` stands for `python scripts/make_report_figures.py`.

## Corrections needed in `report/main.tex`

| # | where | old | new | source |
|---|---|---|---|---|
| 1 | §6.1, "Question 4, optimality gap" | "so no run trained from scratch gets above about 0.19" | "about 0.21" (max over 20 seeds: 0.188 at k = 1, **0.211** at k = 2, blocker s = 0 public) | `T counts`, line "PG vs BR from scratch (m4_seeds, 20 seeds)"; `results/m4_seeds/10b86067ad/seeds/runs.csv` |
| 2 | §6.1, "Kuhn poker" | "PG vs BR ends between −0.023 and −0.036 when k ≥ 1" | "between −0.023 and −0.046" (last iterate: (2,1) −0.023 … (2,0) −0.046; the averaged policy gives −0.024 … −0.036) | `T 3`, line "Kuhn PG vs BR last, g per cell"; `T counts`, "Kuhn pg_vs_br/last"; `results/m4_kuhn/21de4dc484/seeds/metrics.json` |
| 3 | §6.2, "first look" | "and still leak only about 0.03 bits on average" (the 15 runs that fail the pad check) | "about 0.1 bits" (mean 0.107 over the 15 failing runs; 0.03 is the mean over all 60 pad-cell runs) | `T counts`, line "m4_seeds pad check: 15 failing runs, their mean leakage 0.107 bits" |
| 4 | §6.2, "Protecting only the exploitable part" | "On 4 × 2 the teams leak 0.3 bits of the suit" | "0.4 bits" (last iterate I(M; suit) = 0.355; the averaged policy has 0.32) | `T facts`, "suit learning suit4x2"; `results/m5_suit/70447f85c5/seeds/metrics.json` |
| 5 | Appendix B, Table 6, row "Neural fixes" | "12 to 19 min per run" | "0.5 to 15 min per run" (single changes 30 s to 3.5 min, PPO pairs 2 to 13 min, decision-rule runs 14 to 15.4 min) | `T facts`, wall times of `m7_neural_diag`, `m7_neural_combo`, `m7_neural_gate` |

Remarks, not number changes (wording left as is):
- §6.1 Kuhn: "for (k, s) = (1, 2) and (2, 1) the learned team beats −1/24 with 95% confidence". This is true. With the last iterate (2, 2) also clears it, by 0.0006 (`T counts`).
- §5 and §6.2 say that on coordinated attack with k = 1, s = 0 the team "uses the diagonal trick". With s = 0 there is no shared key, so the policy found is the fixed diagonal (each teammate attacks the diagonal cell of its own row or column), not the key-switched trick of the s ≥ 1 cells. The value 1/4 is correct.

## Unsupported numbers

| where | number | status |
|---|---|---|
| Appendix B, Table 6, PG vs BR | "SGD step 8 (chosen from {1, 2, 4, 8} on one cell)" | The tuning run (blocker n = 4, (2, 2, pub), 3 seeds) predates the results layout. Its only record is the comment in `configs/m3_marl.yaml`, and there is no config or results folder for it. We did not regenerate it, because that would be a new run. Every other step-size choice in Table 6 has a results folder (`m4_tune_selfplay`, `m6_neural_tune`, `m7_tabinit_tune`). |

Everything else listed below matches the results to the digits shown.

## Abstract and Introduction

| number | source | command |
|---|---|---|
| 2kR (not kR) key bits; 1/4 and 1 − 2^−s caps; "three small games"; "16 messages" | Proposition 2, Lemma 1 (theorems in the report); Table 1 (attack 2 × 2, kR = 1 is not enough); game definitions in `games/` | `T 1` |
| "half of the episodes", "refits … at every step" | Figure 1 (ε = 0.5: 23/30 pad, 10/10 quiet); Table 5 | `T fig1`, `T 5` |
| "even exact gradient ascent stops" | 0 of 40 runs reach V | `T counts` |

## Section 5, exact values

| number | source | command |
|---|---|---|
| Kuhn V_Cor = −1/24 (312 leaves); k⋆ = 1; V_Com = 0; one key bit reaches V_Cor; one bit + one key bit reaches V_Com | `results/m1_values/c0c43b42ec/0/metrics.json` (terminals 312), `results/m2_values/e9111a924c/0/metrics.json` (kuhn3 rows) | `T 1` ("kuhn3" lines); solver: `python scripts/run_values.py --config configs/m1_values.yaml --seed 0`, `python scripts/run_bounds.py --config configs/m2_values.yaml --seed 0` |
| V(0, ∞) = 3/8 on 2 × 2; 3 × 3: k⋆ = 2, V(1, ∞, priv) = 40/81, V_Com = 8/9 | `results/m25_values/f987c5a37c/0/metrics.json` | `T 1` ("other values"); solver: `python scripts/run_bounds.py --config configs/m25_values.yaml --seed 0` |
| **Table 1**, every cell | `results/m2_values/*/0/metrics.json`, `results/m25_values/*/0/metrics.json`, with Lemma 1 and Proposition 1 applied as upper bounds († in the printout) | `T 1` |
| Table 1, "smallest s": 1 and 2 (blocker n = 4), 2 = 2kR (attack 2 × 2) | computed cells s ≤ 2 | `T 1` |
| Table 1, "smallest s": 3 (blocker n = 8), ≥ 2 (attack 3 × 3, k = 1), 4 = 2kR (attack 3 × 3, k = 2) | theorem: Proposition 2 gives the upper end (kR = 3 for the blocker, one informative message; 2kR = 4 for attack), Lemma 1 rules out smaller s (1 − 2^−s < V(k, ∞, priv)); the computed s ≤ 2 cells give PoE > 0 or an open interval | `T 1` |
| "1 − 2^−3 < 8/9" | arithmetic, V_Com = 8/9 from `results/m25_values` | `T 1` |
| Liar's Dice V_Cor = V_Com = 1/9 | `results/m25_values/f987c5a37c/0/v_com.json`, `summary.md` (liars_dice rows) | solver as above |
| **Table 2**, every cell; "2 × 4, k = 3 … leaks 2 bits about the card" | `results/m5_suit_values/*/0/metrics.json` (leak column of the (3, 1, pub) strategy: 2.0 bits) | `T 2`; solver: `FAI_THREADS=2 FAI_GUROBI_MEM_GB=2 python scripts/run_bounds.py --config configs/m5_suit_values.yaml` |
| "(S, R) ∈ {(2,2), (2,4), (4,2), (4,4)}, construction equals V(k, ∞, priv)" | `results/m5_suit_values`, `results/m6_values/*/0/summary.md` (4 × 4) | `T 2`; `python scripts/m6_targets.py` |
| Example 1: 3/16, 3/8, 3/4 | `results/m2_values` (blocker4, s = ∞) | `T 1` |

## Section 6, learning

| number | source | command |
|---|---|---|
| "30 cells", "9 Kuhn cells", 256 episodes, step 8 | `configs/m4_seeds.yaml`, `configs/m4_kuhn.yaml`, `configs/m3_marl.yaml` | config files |
| Self-play step "tuned … from {0.5, 1, 2, 4, 8} and picked the same value" | `results/m4_tune_selfplay/b4d266138c/seeds/summary.md` (lr 8 best: 0.620 last, 0.618 avg) | `python scripts/run_m4.py --config configs/m4_tune_selfplay.yaml` |
| **Table 3**, every entry | `results/m4_seeds`, `m4_selfplay`, `m4_psro`, `m4_kuhn` (`metrics.json`) | `T 3` |
| **Table 4**, every entry | `results/m4_seeds/10b86067ad/seeds/metrics.json` | `T 4` |
| §6.1: mean gap 0.023, 18 of 30 within 0.005 (averaged), self-play 0.093 → 0.040 | Table 3 | `T 3` |
| §6.1: 3/16 "the value of saying nothing" | Table 1 / `results/m2_values` (blocker4 k = 0) | `T 1` |
| §6.1: "no run gets above 3/8 against 1/2" (blocker k = 2, s = 1) | max 0.365 over 20 seeds | `T counts` |
| §6.1: exact gradient "none of 40", sampled "4 of 40" | `results/m6_exactgrad/1167292757/seeds/runs.csv` | `T counts` |
| §6.1: warm start 10 of 10 (averaged), 0 of 30 from scratch (20 in m4_seeds + 10 in m5_curriculum); 4 and 6 of 10 vs 0 and 1; 3 or 4 collapse to 0; k = 2, s = 0 all at 0 | `results/m5_curriculum/ebd589ce9d/seeds/runs.csv`, `results/m4_seeds/.../runs.csv` | `T counts` |
| §6.1 Kuhn: about −0.05 at k = 0; mean gaps 0.06 to 0.15 for self-play and PSRO | `results/m4_kuhn` | `T 3`, `T counts` |
| §6.1 Kuhn: codes (high/low, "I hold the J"), "one case in six" without information (11 of 70) | `results/m4_kuhn/21de4dc484/seeds/learned_bits.txt` | `python scripts/describe_learned_bit.py results/m4_kuhn/21de4dc484/seeds` (needs the per-run files, i.e. a rerun of `configs/m4_kuhn.yaml`) |
| §6.2: 0 to 0.18 bits public, 1 to 2 bits private (s = 0 cells), 16 of 20 quiet, 45 of 60 pad | Table 4 (private-cell column of the printout), Table 3 | `T 4`, `T 3` |
| §6.2: self-play and PSRO leak 0.4 to 1.6 bits (mean 0.42 to 0.53, max 1.60), BR takes up to 0.6, pad 3 to 5 of 15 | `results/m4_selfplay`, `results/m4_psro` | `T counts`, `T 3` |
| **Figure 1** and its text (23 to 25 of 30 up to ε = 0.5, 17 at 0.75, 1 at 1; leakage < 0.1 up to 0.5, 0.9 and 1.8 at 1; quiet 10/10 vs 8/10) | `results/m5_dose/9741c729f4/seeds/metrics.json` | `T fig1`; `F` writes `report/figures/fig_dose.{pdf,png}` |
| **Table 5**, every entry; text (26 of 30, 9 of 10, 0.016 vs 0.018; 5 of 30; 8 of 30) | `results/m5_model`, `results/m5_model_t1`, `results/m6_timescale` | `T 5` |
| "100 of 100 runs" (frozen team) | `results/m6_adv_diag/runs.csv` | `T counts`; `python scripts/m6_adv_diag.py` (needs the per-run files of `configs/m6_timescale.yaml`) |
| "8 to 14 of 30", "halves the mean gap", "at most 2 of 10" | Table 5 rows; `results/m6_timescale/9cdf74e4e5/seeds/summary.md` (all six settings) | `T 5` |
| Responsiveness: ten adversaries, 400 runs, Spearman +0.47 to +0.87 (intervals above 0), −0.39 to −0.92 with final g, within type +0.23 to +0.66 (interval above 0 in three of four), lagged sign | `results/m8_resp/analysis.json`, `analysis.md`, `runs_summary.csv` | `T facts`; `python scripts/m8_analyze.py results/m8_resp/fdce74d282/seeds` (needs the per-run logs); `F` writes `report/figures/fig_responsiveness.*` |
| Suit learning: 9 of 10, 1 bit, 1/2 (2 × 2); 8 of 10, about 1/4 (2 × 4); 0.31 and 1/2 (4 × 2) | `results/m5_suit/70447f85c5/seeds/metrics.json` and `summary.md` (per-seed classification) | `T facts` |
| §6.3: 15 of 18 cells exact | `results/m6_targets/targets.md` | `python scripts/m6_targets.py` |
| §6.3: 1 of 540; 0.33 vs 0.94; tabular 9, 9 and 3 of 10; g ≤ 0.021; 0.09 to 0.18; 21 of 30 | `results/m6_neural/5b68fd748b/seeds/metrics.json`, `summary.md`, `runs.csv` | `T facts`, `python scripts/m6_compact.py results/m6_neural/5b68fd748b/seeds/metrics.json` |
| §6.3: PPO + wider network 2 of 3 (blocker), 3 of 10 (suit), none (attack) | `results/m7_neural_combo`, `results/m7_neural_gate` | `T counts` |
| §6.3: 0.71 of 0.94 after 40,000 iterations; 0 of 50 pad and suit pad; 5 instead of 9 of 10 | `results/m7_tabinit`, `results/m7_tabinit_long`, `results/m6_neural` | `python scripts/m6_compact.py results/m7_tabinit*/*/seeds/metrics.json` |

## Section 7 and appendices

| number | source | command |
|---|---|---|
| Kuhn public optimum leaks 0.085 bits | `results/m2_values` (kuhn3, k = 1, s = ∞, pub: 0.0848) | `T 1` |
| Appendix A: tolerances 10^−7 and 10^−9, time limits 300 to 1200 s | `configs/m2_values.yaml`, `configs/m25_values.yaml`, `configs/m5_suit_values.yaml`, `solvers/` | config files |
| Appendix A: [0.2499997, 1/4] (attack 3 × 3, k = 2, s = 0, pub); 8 · 10^−9 (k = 1, s = 0, priv); Kuhn V_TME within 4.5 · 10^−10 | `results/m25_values`, `results/m2_values` | `T 1` |
| Appendix A: list of cells closed by theorems | `status` and `upper_from` columns of `results/m2_values`, `m25_values`, `m5_suit_values` `summary.md`, plus Lemma 1 († in `T 1`, `T 2`) | `T 1`, `T 2` |
| Table 6: 1 to 7 s per run; 166 s for 150; 117 s for 240; 279 s for 300; 265 s for 300; 82 s for 120; about 1 h for 720; 245 s for 400 | `wall_seconds` and `seconds` in each `metrics.json` (the "runs" count of the printout counts last and averaged outputs separately) | `T facts` |
