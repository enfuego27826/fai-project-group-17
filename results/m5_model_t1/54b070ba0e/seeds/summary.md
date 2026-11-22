| method | game | k | s | ρ | exact V | g(π_T) mean ± 95% CI | gap | I(M;X) | I(M;φ(X)) | cost of leak | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 3/4 | 0.749 ± 0.000 | 0.001 | 0.00 | 0.00 | 0.000 | key as pad | 10 / 10 | 8.6s |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 1/4 | 0.234 ± 0.035 | 0.016 | 0.10 | 0.10 | 0.017 | quiet or coarse | 9 / 10 | 3.3s |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 3/8 | 0.375 ± 0.000 | 0.000 | 0.03 | 0.03 | 0.000 | key as pad | 10 / 10 | 4.3s |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 3/4 | 0.699 ± 0.046 | 0.051 | 0.06 | 0.06 | 0.009 | key as pad | 6 / 10 | 8.9s |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 1/2 | 0.487 ± 0.028 | 0.013 | 1.00 | 0.01 | 0.000 | pad suit only | 9 / 10 | 5.1s |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 3/4 | 0.643 ± 0.103 | 0.107 | 0.19 | 0.19 | 0.081 | key as pad | 6 / 10 | 8.1s |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 1/4 | 0.214 ± 0.035 | 0.036 | 0.34 | 0.34 | 0.071 | quiet or coarse | 7 / 10 | 2.7s |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 3/8 | 0.361 ± 0.004 | 0.014 | 0.04 | 0.04 | 0.004 | key as pad | 10 / 10 | 4.1s |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 3/4 | 0.634 ± 0.065 | 0.116 | 0.22 | 0.22 | 0.101 | key as pad | 3 / 10 | 8.6s |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 1/2 | 0.456 ± 0.049 | 0.044 | 0.99 | 0.03 | 0.005 | pad suit only | 7 / 10 | 4.7s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 0 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 1 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 2 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 3 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 4 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 5 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 6 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 7 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 8 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 2 | pub | 9 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 0 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 1 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 2 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.095 vs V=0.250; messages carry 1.00 bits |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 4 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 5 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 6 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 7 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 8 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048_T1/last | attack2x2 | 1 | 0 | pub | 9 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 0 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.002 bits |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 1 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.060 bits |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 2 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.032 bits |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 3 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.007 bits |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 4 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.002 bits |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 5 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.000 bits |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 6 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.038 bits |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 7 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.042 bits |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 8 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.049 bits |
| model_N2048_T1/last | blocker4 | 1 | 2 | pub | 9 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.033 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 0 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.625 vs V_priv=0.750; leak=0.176 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.624 vs V_priv=0.750; leak=0.092 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 3 | key as pad | no | g=0.624 vs V_priv=0.750; leak=0.213 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 4 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 5 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 6 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 7 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 8 | key as pad | no | g=0.625 vs V_priv=0.750; leak=0.113 bits |
| model_N2048_T1/last | blocker4 | 2 | 2 | pub | 9 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 0 | pad suit only | no | g=0.375 vs V=0.500; suit partly padded, rank in clear; I(M;X)=1.05, I(M;suit)=0.10, I(M;suit|K)=0.68 |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 1 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 2 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 4 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 6 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 7 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 8 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| model_N2048_T1/last | suit2x2 | 2 | 1 | pub | 9 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 0 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 1 | key as pad | no | g=0.500 vs V_priv=0.750; leak=0.490 bits |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 2 | key as pad | no | g=0.556 vs V_priv=0.750; leak=0.212 bits |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 3 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 4 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 5 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 6 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 7 | key as pad | no | g=0.500 vs V_priv=0.750; leak=0.494 bits |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 8 | key as pad | no | g=0.375 vs V_priv=0.750; leak=0.695 bits |
| model_N32_T1/last | attack2x2 | 1 | 2 | pub | 9 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 0 | quiet or coarse | yes | g=0.237 vs V=0.250; messages carry no information (quiet) |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 1 | quiet or coarse | yes | g=0.246 vs V=0.250; messages carry 0.09 bits |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 2 | quiet or coarse | yes | g=0.235 vs V=0.250; messages carry no information (quiet) |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 3 | quiet or coarse | yes | g=0.236 vs V=0.250; messages carry no information (quiet) |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 4 | quiet or coarse | yes | g=0.241 vs V=0.250; messages carry 0.09 bits |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.161 vs V=0.250; messages carry 1.05 bits |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 6 | quiet or coarse | yes | g=0.242 vs V=0.250; messages carry no information (quiet) |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.100 vs V=0.250; messages carry 1.06 bits |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.200 vs V=0.250; messages carry 1.03 bits |
| model_N32_T1/last | attack2x2 | 1 | 0 | pub | 9 | quiet or coarse | yes | g=0.244 vs V=0.250; messages carry no information (quiet) |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 0 | key as pad | yes | g=0.359 vs V_priv=0.375; leak=0.037 bits |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 1 | key as pad | yes | g=0.371 vs V_priv=0.375; leak=0.037 bits |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 2 | key as pad | yes | g=0.362 vs V_priv=0.375; leak=0.000 bits |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 3 | key as pad | yes | g=0.363 vs V_priv=0.375; leak=0.059 bits |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 4 | key as pad | yes | g=0.356 vs V_priv=0.375; leak=0.040 bits |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 5 | key as pad | yes | g=0.356 vs V_priv=0.375; leak=0.030 bits |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 6 | key as pad | yes | g=0.358 vs V_priv=0.375; leak=0.053 bits |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 7 | key as pad | yes | g=0.366 vs V_priv=0.375; leak=0.035 bits |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 8 | key as pad | yes | g=0.364 vs V_priv=0.375; leak=0.002 bits |
| model_N32_T1/last | blocker4 | 1 | 2 | pub | 9 | key as pad | yes | g=0.357 vs V_priv=0.375; leak=0.064 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.625 vs V_priv=0.750; leak=0.101 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 1 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.542 vs V_priv=0.750; leak=0.474 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 3 | key as pad | no | g=0.603 vs V_priv=0.750; leak=0.292 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 4 | key as pad | no | g=0.607 vs V_priv=0.750; leak=0.295 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 5 | key as pad | no | g=0.613 vs V_priv=0.750; leak=0.283 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 6 | key as pad | no | g=0.617 vs V_priv=0.750; leak=0.264 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 7 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 8 | key as pad | no | g=0.481 vs V_priv=0.750; leak=0.520 bits |
| model_N32_T1/last | blocker4 | 2 | 2 | pub | 9 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 0 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 1 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 2 | pad suit only | no | g=0.356 vs V=0.500; suit leaks, rank in clear; I(M;X)=1.13, I(M;suit)=0.15, I(M;suit|K)=0.73 |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 4 | pad suit only | no | g=0.368 vs V=0.500; suit partly padded, rank partly sent; I(M;X)=0.80, I(M;suit)=0.06, I(M;suit|K)=0.74 |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 6 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 7 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 8 | pad suit only | no | g=0.343 vs V=0.500; suit partly padded, rank in clear; I(M;X)=1.02, I(M;suit)=0.06, I(M;suit|K)=0.48 |
| model_N32_T1/last | suit2x2 | 2 | 1 | pub | 9 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.99 |

wall time 148 s for 100 runs
