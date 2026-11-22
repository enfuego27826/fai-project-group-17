| cell | runs | Spearman(early r, final leakage) [95% CI] | Spearman(early r, final g) [95% CI] | within-type control [95% CI] |
|---|---|---|---|---|
| attack (1, 2, pub) | 100 | +0.80 [+0.70, +0.88] | -0.84 [-0.90, -0.75] | +0.46 [+0.21, +0.61] |
| blocker (1, 2, pub) | 100 | +0.47 [+0.27, +0.63] | -0.92 [-0.95, -0.87] | +0.23 [+0.02, +0.42] |
| blocker (2, 2, pub) | 100 | +0.87 [+0.81, +0.92] | -0.84 [-0.89, -0.75] | +0.66 [+0.47, +0.76] |
| attack (1, 0, pub) | 100 | +0.50 [+0.31, +0.65] | -0.39 [-0.58, -0.18] | +0.23 [-0.00, +0.42] |

Within-type Spearman per adversary type (10 runs each; n/a = constant input):

| cell | exact_br | noisy_e0.25 | noisy_e0.5 | noisy_e0.75 | noisy_e1 | model_N2048_T1 | model_N2048_T10 | model_N32_T10 | reinforce_s1 | reinforce_s4 |
|---|---|---|---|---|---|---|---|---|---|---|
| attack (1, 2, pub) | n/a | +0.52 | +0.62 | +0.68 | +0.85 | +0.15 | -0.08 | +0.56 | +0.58 | +0.49 |
| blocker (1, 2, pub) | n/a | -0.08 | -0.44 | +0.67 | +0.72 | +0.15 | -0.04 | +0.39 | +0.25 | +0.55 |
| blocker (2, 2, pub) | n/a | +0.68 | +0.78 | +0.98 | +0.95 | +0.44 | +0.66 | +0.66 | +0.42 | +0.72 |
| attack (1, 0, pub) | n/a | -0.48 | +0.18 | +0.77 | +0.78 | +0.15 | +0.67 | -0.05 | +0.13 | +0.05 |

Lagged, within run:

| cell | adversary | Δ = 500: mean corr ± 95% (runs) | Δ = 2000: mean corr ± 95% (runs) |
|---|---|---|---|
| attack (1, 2, pub) | exact_br | undefined (r_t constant) | undefined (r_t constant) |
| attack (1, 2, pub) | noisy_e0.25 | -0.61 ± 0.08 (10) | -0.81 ± 0.08 (10) |
| attack (1, 2, pub) | noisy_e0.5 | -0.48 ± 0.17 (10) | -0.62 ± 0.21 (10) |
| attack (1, 2, pub) | noisy_e0.75 | -0.56 ± 0.29 (10) | -0.69 ± 0.33 (10) |
| attack (1, 2, pub) | noisy_e1 | -0.89 ± 0.09 (10) | -0.89 ± 0.16 (10) |
| attack (1, 2, pub) | model_N2048_T1 | -0.20 ± 0.06 (10) | -0.22 ± 0.08 (10) |
| attack (1, 2, pub) | model_N2048_T10 | -0.08 ± 0.13 (10) | -0.13 ± 0.16 (10) |
| attack (1, 2, pub) | model_N32_T10 | -0.06 ± 0.21 (10) | -0.14 ± 0.34 (10) |
| attack (1, 2, pub) | reinforce_s1 | -0.10 ± 0.36 (10) | -0.15 ± 0.47 (10) |
| attack (1, 2, pub) | reinforce_s4 | -0.37 ± 0.24 (10) | -0.51 ± 0.26 (10) |
| blocker (1, 2, pub) | exact_br | undefined (r_t constant) | undefined (r_t constant) |
| blocker (1, 2, pub) | noisy_e0.25 | -0.05 ± 0.17 (10) | -0.07 ± 0.35 (10) |
| blocker (1, 2, pub) | noisy_e0.5 | +0.04 ± 0.16 (10) | +0.05 ± 0.30 (10) |
| blocker (1, 2, pub) | noisy_e0.75 | +0.08 ± 0.16 (10) | +0.10 ± 0.28 (10) |
| blocker (1, 2, pub) | noisy_e1 | -0.17 ± 0.17 (10) | -0.16 ± 0.30 (10) |
| blocker (1, 2, pub) | model_N2048_T1 | -0.01 ± 0.08 (10) | +0.03 ± 0.25 (10) |
| blocker (1, 2, pub) | model_N2048_T10 | -0.13 ± 0.07 (10) | -0.07 ± 0.14 (10) |
| blocker (1, 2, pub) | model_N32_T10 | -0.00 ± 0.08 (10) | +0.01 ± 0.11 (10) |
| blocker (1, 2, pub) | reinforce_s1 | -0.26 ± 0.08 (10) | -0.27 ± 0.08 (10) |
| blocker (1, 2, pub) | reinforce_s4 | -0.17 ± 0.10 (10) | -0.24 ± 0.18 (10) |
| blocker (2, 2, pub) | exact_br | undefined (r_t constant) | undefined (r_t constant) |
| blocker (2, 2, pub) | noisy_e0.25 | -0.56 ± 0.23 (10) | -0.72 ± 0.21 (10) |
| blocker (2, 2, pub) | noisy_e0.5 | -0.62 ± 0.22 (10) | -0.81 ± 0.13 (10) |
| blocker (2, 2, pub) | noisy_e0.75 | -0.72 ± 0.23 (10) | -0.66 ± 0.36 (10) |
| blocker (2, 2, pub) | noisy_e1 | -0.98 ± 0.01 (10) | -0.99 ± 0.02 (10) |
| blocker (2, 2, pub) | model_N2048_T1 | -0.04 ± 0.13 (10) | -0.16 ± 0.14 (10) |
| blocker (2, 2, pub) | model_N2048_T10 | -0.07 ± 0.14 (10) | -0.05 ± 0.17 (10) |
| blocker (2, 2, pub) | model_N32_T10 | +0.00 ± 0.09 (10) | -0.07 ± 0.10 (10) |
| blocker (2, 2, pub) | reinforce_s1 | -0.23 ± 0.20 (10) | -0.42 ± 0.21 (10) |
| blocker (2, 2, pub) | reinforce_s4 | -0.27 ± 0.20 (10) | -0.41 ± 0.28 (10) |
| attack (1, 0, pub) | exact_br | undefined (r_t constant) | undefined (r_t constant) |
| attack (1, 0, pub) | noisy_e0.25 | +0.15 ± 0.04 (10) | +0.30 ± 0.12 (10) |
| attack (1, 0, pub) | noisy_e0.5 | +0.20 ± 0.13 (10) | +0.34 ± 0.22 (10) |
| attack (1, 0, pub) | noisy_e0.75 | -0.04 ± 0.27 (10) | +0.07 ± 0.35 (10) |
| attack (1, 0, pub) | noisy_e1 | -0.88 ± 0.17 (10) | -0.91 ± 0.18 (10) |
| attack (1, 0, pub) | model_N2048_T1 | -0.03 ± 0.09 (10) | -0.14 ± 0.11 (10) |
| attack (1, 0, pub) | model_N2048_T10 | -0.08 ± 0.08 (10) | -0.11 ± 0.07 (10) |
| attack (1, 0, pub) | model_N32_T10 | +0.33 ± 0.06 (10) | +0.34 ± 0.09 (10) |
| attack (1, 0, pub) | reinforce_s1 | +0.48 ± 0.31 (10) | +0.36 ± 0.36 (10) |
| attack (1, 0, pub) | reinforce_s4 | +0.19 ± 0.26 (10) | +0.05 ± 0.39 (10) |

Decision rule: supports (4 of 4 cells positive with the interval above 0)
