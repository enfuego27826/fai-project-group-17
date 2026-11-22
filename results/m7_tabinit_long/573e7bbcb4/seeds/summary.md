| method | game | k | s | ρ | target | label | g(π_T) mean ± 95% CI | gap to lower | I(M;X) | I(M;c(X)) | I(M;c(X)\|K) | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.708 ± 0.024 | 0.230 | 1.40 | 1.40 | 3.69 | key as pad | 0 / 10 | 78s |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.561 ± 0.073 | 0.189 | 2.15 | 2.15 | 3.61 | reaches best known | 0 / 10 | 28s |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 0.7500 | exact (code + uniform block) | 0.576 ± 0.013 | 0.174 | 1.62 | 0.21 | 1.63 | pad suit only | 0 / 10 | 85s |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 0.7500 | exact (code + uniform block) | 0.544 ± 0.058 | 0.206 | 2.27 | 0.39 | 1.63 | pad suit only | 0 / 10 | 25s |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.428 ± 0.021 | 0.510 | 0.65 | 0.65 | 2.88 | key as pad | 0 / 10 | 22s |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.339 ± 0.018 | 0.411 | 1.57 | 1.57 | 2.64 | reaches best known | 0 / 10 | 15s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 0 | key as pad | no | g=0.717 vs 0.938; I(M;X)=1.41 |
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 1 | key as pad | no | g=0.668 vs 0.938; I(M;X)=1.59 |
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 2 | key as pad | no | g=0.694 vs 0.938; I(M;X)=1.37 |
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 3 | key as pad | no | g=0.740 vs 0.938; I(M;X)=1.24 |
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 4 | key as pad | no | g=0.725 vs 0.938; I(M;X)=1.52 |
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 5 | key as pad | no | g=0.669 vs 0.938; I(M;X)=1.65 |
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 6 | key as pad | no | g=0.758 vs 0.938; I(M;X)=0.90 |
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 7 | key as pad | no | g=0.697 vs 0.938; I(M;X)=1.52 |
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 8 | key as pad | no | g=0.665 vs 0.938; I(M;X)=1.62 |
| tabular_sigma1_40k | blocker16 | 4 | 4 | pub | 9 | key as pad | no | g=0.743 vs 0.938; I(M;X)=1.17 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 0 | reaches best known | no | g=0.430 vs 0.750; I(M;X)=2.25 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 1 | reaches best known | no | g=0.443 vs 0.750; I(M;X)=2.34 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 2 | reaches best known | no | g=0.625 vs 0.750; I(M;X)=1.93 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 3 | reaches best known | no | g=0.656 vs 0.750; I(M;X)=1.98 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 4 | reaches best known | no | g=0.703 vs 0.750; I(M;X)=1.96 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 5 | reaches best known | no | g=0.648 vs 0.750; I(M;X)=1.93 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 6 | reaches best known | no | g=0.480 vs 0.750; I(M;X)=2.42 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 7 | reaches best known | no | g=0.487 vs 0.750; I(M;X)=2.38 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 8 | reaches best known | no | g=0.640 vs 0.750; I(M;X)=1.86 |
| tabular_sigma1_40k | blocker16 | 4 | 2 | pub | 9 | reaches best known | no | g=0.495 vs 0.750; I(M;X)=2.40 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 0 | pad suit only | no | g=0.556 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.79, I(M;suit)=0.27, I(M;suit|K)=1.59 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 1 | pad suit only | no | g=0.549 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.84, I(M;suit)=0.26, I(M;suit|K)=1.59 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 2 | pad suit only | no | g=0.579 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.57, I(M;suit)=0.17, I(M;suit|K)=1.65 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 3 | pad suit only | no | g=0.588 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.49, I(M;suit)=0.18, I(M;suit|K)=1.64 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 4 | pad suit only | no | g=0.595 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.45, I(M;suit)=0.16, I(M;suit|K)=1.64 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 5 | pad suit only | no | g=0.591 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.31, I(M;suit)=0.17, I(M;suit|K)=1.66 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 6 | pad suit only | no | g=0.571 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.72, I(M;suit)=0.25, I(M;suit|K)=1.66 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 7 | pad suit only | no | g=0.585 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.89, I(M;suit)=0.25, I(M;suit|K)=1.70 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 8 | pad suit only | no | g=0.551 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.79, I(M;suit)=0.25, I(M;suit|K)=1.59 |
| tabular_sigma1_40k | suit4x4 | 4 | 4 | pub | 9 | pad suit only | no | g=0.591 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.31, I(M;suit)=0.12, I(M;suit|K)=1.63 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 0 | pad suit only | no | g=0.511 vs 0.750; suit leaks, rank in clear; I(M;X)=2.47, I(M;suit)=0.54, I(M;suit|K)=1.59 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 1 | pad suit only | no | g=0.496 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.40, I(M;suit)=0.51, I(M;suit|K)=1.53 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 2 | pad suit only | no | g=0.577 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.01, I(M;suit)=0.28, I(M;suit|K)=1.70 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 3 | pad suit only | no | g=0.609 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.03, I(M;suit)=0.24, I(M;suit|K)=1.75 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 4 | pad suit only | no | g=0.416 vs 0.750; suit leaks, rank in clear; I(M;X)=2.63, I(M;suit)=0.65, I(M;suit|K)=1.50 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 5 | pad suit only | no | g=0.687 vs 0.750; suit partly padded, rank partly sent; I(M;X)=1.93, I(M;suit)=0.08, I(M;suit|K)=1.85 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 6 | pad suit only | no | g=0.503 vs 0.750; suit leaks, rank in clear; I(M;X)=2.45, I(M;suit)=0.49, I(M;suit|K)=1.57 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 7 | pad suit only | no | g=0.493 vs 0.750; suit leaks, rank in clear; I(M;X)=2.31, I(M;suit)=0.41, I(M;suit|K)=1.46 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 8 | pad suit only | no | g=0.512 vs 0.750; suit leaks, rank in clear; I(M;X)=2.47, I(M;suit)=0.54, I(M;suit|K)=1.59 |
| tabular_sigma1_40k | suit4x4 | 4 | 2 | pub | 9 | pad suit only | no | g=0.632 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.04, I(M;suit)=0.18, I(M;suit|K)=1.76 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 0 | key as pad | no | g=0.426 vs 0.938; I(M;X)=0.66 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 1 | key as pad | no | g=0.415 vs 0.938; I(M;X)=0.69 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 2 | key as pad | no | g=0.371 vs 0.938; I(M;X)=0.70 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 3 | key as pad | no | g=0.395 vs 0.938; I(M;X)=0.66 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 4 | key as pad | no | g=0.445 vs 0.938; I(M;X)=0.54 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 5 | key as pad | no | g=0.463 vs 0.938; I(M;X)=0.65 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 6 | key as pad | no | g=0.454 vs 0.938; I(M;X)=0.59 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 7 | key as pad | no | g=0.414 vs 0.938; I(M;X)=0.62 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 8 | key as pad | no | g=0.455 vs 0.938; I(M;X)=0.64 |
| tabular_sigma1_40k | attack4x4 | 2 | 4 | pub | 9 | key as pad | no | g=0.437 vs 0.938; I(M;X)=0.74 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 0 | reaches best known | no | g=0.359 vs 0.750; I(M;X)=1.50 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 1 | reaches best known | no | g=0.343 vs 0.750; I(M;X)=1.71 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 2 | reaches best known | no | g=0.304 vs 0.750; I(M;X)=1.80 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 3 | reaches best known | no | g=0.343 vs 0.750; I(M;X)=1.49 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 4 | reaches best known | no | g=0.335 vs 0.750; I(M;X)=1.31 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 5 | reaches best known | no | g=0.374 vs 0.750; I(M;X)=1.74 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 6 | reaches best known | no | g=0.359 vs 0.750; I(M;X)=1.55 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 7 | reaches best known | no | g=0.312 vs 0.750; I(M;X)=1.78 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 8 | reaches best known | no | g=0.301 vs 0.750; I(M;X)=1.29 |
| tabular_sigma1_40k | attack4x4 | 2 | 2 | pub | 9 | reaches best known | no | g=0.359 vs 0.750; I(M;X)=1.54 |

wall time 850 s for 60 runs
