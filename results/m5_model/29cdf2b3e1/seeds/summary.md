| method | game | k | s | ρ | exact V | g(π_T) mean ± 95% CI | gap | I(M;X) | I(M;φ(X)) | cost of leak | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exact_br/last | attack2x2 | 1 | 2 | pub | 3/4 | 0.730 ± 0.044 | 0.020 | 0.05 | 0.05 | 0.009 | key as pad | 9 / 10 | 5.3s |
| exact_br/last | attack2x2 | 1 | 0 | pub | 1/4 | 0.234 ± 0.023 | 0.016 | 0.00 | 0.00 | 0.000 | quiet or coarse | 8 / 10 | 1.8s |
| exact_br/last | blocker4 | 1 | 2 | pub | 3/8 | 0.375 ± 0.000 | 0.000 | 0.04 | 0.04 | 0.000 | key as pad | 9 / 10 | 2.7s |
| exact_br/last | blocker4 | 2 | 2 | pub | 3/4 | 0.725 ± 0.031 | 0.025 | 0.03 | 0.03 | 0.000 | key as pad | 7 / 10 | 5.6s |
| exact_br/last | suit2x2 | 2 | 1 | pub | 1/2 | 0.472 ± 0.062 | 0.028 | 1.00 | 0.00 | 0.002 | pad suit only | 9 / 10 | 3.1s |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 3/4 | 0.709 ± 0.062 | 0.041 | 0.07 | 0.07 | 0.017 | key as pad | 8 / 10 | 5.4s |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 1/4 | 0.148 ± 0.079 | 0.102 | 0.50 | 0.50 | 0.106 | quiet or coarse | 5 / 10 | 1.8s |
| model_N2048/last | blocker4 | 1 | 2 | pub | 3/8 | 0.375 ± 0.000 | 0.000 | 0.04 | 0.04 | 0.000 | key as pad | 8 / 10 | 2.7s |
| model_N2048/last | blocker4 | 2 | 2 | pub | 3/4 | 0.670 ± 0.056 | 0.080 | 0.13 | 0.13 | 0.018 | key as pad | 4 / 10 | 5.5s |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 1/2 | 0.500 ± 0.000 | 0.000 | 1.00 | 0.00 | 0.000 | pad suit only | 10 / 10 | 3.0s |
| model_N512/last | attack2x2 | 1 | 2 | pub | 3/4 | 0.727 ± 0.051 | 0.023 | 0.05 | 0.05 | 0.011 | key as pad | 9 / 10 | 5.3s |
| model_N512/last | attack2x2 | 1 | 0 | pub | 1/4 | 0.165 ± 0.065 | 0.085 | 0.50 | 0.50 | 0.093 | quiet or coarse | 5 / 10 | 1.7s |
| model_N512/last | blocker4 | 1 | 2 | pub | 3/8 | 0.374 ± 0.000 | 0.001 | 0.05 | 0.05 | 0.000 | key as pad | 8 / 10 | 2.7s |
| model_N512/last | blocker4 | 2 | 2 | pub | 3/4 | 0.724 ± 0.031 | 0.026 | 0.04 | 0.04 | 0.007 | key as pad | 7 / 10 | 5.5s |
| model_N512/last | suit2x2 | 2 | 1 | pub | 1/2 | 0.462 ± 0.043 | 0.038 | 1.02 | 0.03 | 0.000 | pad suit only | 7 / 10 | 3.0s |
| model_N128/last | attack2x2 | 1 | 2 | pub | 3/4 | 0.685 ± 0.074 | 0.065 | 0.12 | 0.12 | 0.029 | key as pad | 7 / 10 | 5.4s |
| model_N128/last | attack2x2 | 1 | 0 | pub | 1/4 | 0.137 ± 0.078 | 0.113 | 0.59 | 0.59 | 0.162 | quiet or coarse | 4 / 10 | 1.7s |
| model_N128/last | blocker4 | 1 | 2 | pub | 3/8 | 0.371 ± 0.001 | 0.004 | 0.06 | 0.06 | 0.001 | key as pad | 9 / 10 | 2.7s |
| model_N128/last | blocker4 | 2 | 2 | pub | 3/4 | 0.673 ± 0.059 | 0.077 | 0.18 | 0.18 | 0.056 | key as pad | 4 / 10 | 5.5s |
| model_N128/last | suit2x2 | 2 | 1 | pub | 1/2 | 0.499 ± 0.000 | 0.001 | 1.00 | 0.00 | 0.000 | pad suit only | 10 / 10 | 3.0s |
| model_N32/last | attack2x2 | 1 | 2 | pub | 3/4 | 0.562 ± 0.096 | 0.188 | 0.34 | 0.34 | 0.169 | key as pad | 3 / 10 | 5.3s |
| model_N32/last | attack2x2 | 1 | 0 | pub | 1/4 | 0.104 ± 0.080 | 0.146 | 0.95 | 0.95 | 0.325 | quiet or coarse | 3 / 10 | 1.7s |
| model_N32/last | blocker4 | 1 | 2 | pub | 3/8 | 0.349 ± 0.012 | 0.026 | 0.09 | 0.09 | 0.007 | key as pad | 2 / 10 | 2.6s |
| model_N32/last | blocker4 | 2 | 2 | pub | 3/4 | 0.546 ± 0.071 | 0.204 | 0.43 | 0.43 | 0.177 | key as pad | 0 / 10 | 5.5s |
| model_N32/last | suit2x2 | 2 | 1 | pub | 1/2 | 0.452 ± 0.105 | 0.048 | 1.05 | 0.06 | 0.018 | pad suit only | 9 / 10 | 2.9s |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 3/4 | 0.624 ± 0.094 | 0.126 | 0.28 | 0.28 | 0.085 | key as pad | 5 / 10 | 5.3s |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 1/4 | 0.025 ± 0.057 | 0.225 | 1.69 | 1.69 | 0.624 | quiet or coarse | 1 / 10 | 1.9s |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 3/8 | 0.255 ± 0.041 | 0.120 | 0.23 | 0.23 | 0.058 | key as pad | 1 / 10 | 2.8s |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 3/4 | 0.572 ± 0.094 | 0.178 | 0.41 | 0.41 | 0.147 | key as pad | 2 / 10 | 6.0s |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 1/2 | 0.387 ± 0.122 | 0.113 | 1.08 | 0.11 | 0.074 | pad suit only | 6 / 10 | 3.4s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| exact_br/last | attack2x2 | 1 | 2 | pub | 0 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | attack2x2 | 1 | 2 | pub | 1 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | attack2x2 | 1 | 2 | pub | 2 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | attack2x2 | 1 | 2 | pub | 3 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | attack2x2 | 1 | 2 | pub | 4 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | attack2x2 | 1 | 2 | pub | 5 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | attack2x2 | 1 | 2 | pub | 6 | key as pad | no | g=0.557 vs V_priv=0.750; leak=0.453 bits |
| exact_br/last | attack2x2 | 1 | 2 | pub | 7 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | attack2x2 | 1 | 2 | pub | 8 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | attack2x2 | 1 | 2 | pub | 9 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | attack2x2 | 1 | 0 | pub | 0 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | attack2x2 | 1 | 0 | pub | 1 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | attack2x2 | 1 | 0 | pub | 2 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | attack2x2 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.173 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | attack2x2 | 1 | 0 | pub | 4 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | attack2x2 | 1 | 0 | pub | 5 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | attack2x2 | 1 | 0 | pub | 6 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | attack2x2 | 1 | 0 | pub | 7 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | attack2x2 | 1 | 0 | pub | 8 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | attack2x2 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.173 vs V=0.250; messages carry no information (quiet) |
| exact_br/last | blocker4 | 1 | 2 | pub | 0 | key as pad | no | g=0.375 vs V_priv=0.375; leak=0.105 bits |
| exact_br/last | blocker4 | 1 | 2 | pub | 1 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.054 bits |
| exact_br/last | blocker4 | 1 | 2 | pub | 2 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.027 bits |
| exact_br/last | blocker4 | 1 | 2 | pub | 3 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.029 bits |
| exact_br/last | blocker4 | 1 | 2 | pub | 4 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.086 bits |
| exact_br/last | blocker4 | 1 | 2 | pub | 5 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.066 bits |
| exact_br/last | blocker4 | 1 | 2 | pub | 6 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.034 bits |
| exact_br/last | blocker4 | 1 | 2 | pub | 7 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.018 bits |
| exact_br/last | blocker4 | 1 | 2 | pub | 8 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.000 bits |
| exact_br/last | blocker4 | 1 | 2 | pub | 9 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.010 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 0 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 1 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 2 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 3 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 4 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 5 | key as pad | no | g=0.687 vs V_priv=0.750; leak=0.101 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 6 | key as pad | no | g=0.625 vs V_priv=0.750; leak=0.101 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 7 | key as pad | no | g=0.687 vs V_priv=0.750; leak=0.101 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 8 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | blocker4 | 2 | 2 | pub | 9 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| exact_br/last | suit2x2 | 2 | 1 | pub | 0 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| exact_br/last | suit2x2 | 2 | 1 | pub | 1 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| exact_br/last | suit2x2 | 2 | 1 | pub | 2 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| exact_br/last | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| exact_br/last | suit2x2 | 2 | 1 | pub | 4 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| exact_br/last | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| exact_br/last | suit2x2 | 2 | 1 | pub | 6 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| exact_br/last | suit2x2 | 2 | 1 | pub | 7 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| exact_br/last | suit2x2 | 2 | 1 | pub | 8 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| exact_br/last | suit2x2 | 2 | 1 | pub | 9 | pad suit only | no | g=0.224 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 0 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 1 | key as pad | no | g=0.528 vs V_priv=0.750; leak=0.453 bits |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 2 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 3 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 4 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 5 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 6 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 7 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 8 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | attack2x2 | 1 | 2 | pub | 9 | key as pad | no | g=0.562 vs V_priv=0.750; leak=0.254 bits |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.126 vs V=0.250; messages carry 1.00 bits |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.033 vs V=0.250; messages carry 1.00 bits |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.033 vs V=0.250; messages carry 1.00 bits |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.018 vs V=0.250; messages carry 1.00 bits |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.023 vs V=0.250; messages carry 1.00 bits |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 5 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 6 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 7 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 8 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048/last | attack2x2 | 1 | 0 | pub | 9 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N2048/last | blocker4 | 1 | 2 | pub | 0 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.031 bits |
| model_N2048/last | blocker4 | 1 | 2 | pub | 1 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.039 bits |
| model_N2048/last | blocker4 | 1 | 2 | pub | 2 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.043 bits |
| model_N2048/last | blocker4 | 1 | 2 | pub | 3 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.028 bits |
| model_N2048/last | blocker4 | 1 | 2 | pub | 4 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.052 bits |
| model_N2048/last | blocker4 | 1 | 2 | pub | 5 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.000 bits |
| model_N2048/last | blocker4 | 1 | 2 | pub | 6 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.002 bits |
| model_N2048/last | blocker4 | 1 | 2 | pub | 7 | key as pad | no | g=0.375 vs V_priv=0.375; leak=0.109 bits |
| model_N2048/last | blocker4 | 1 | 2 | pub | 8 | key as pad | no | g=0.375 vs V_priv=0.375; leak=0.106 bits |
| model_N2048/last | blocker4 | 1 | 2 | pub | 9 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.000 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.625 vs V_priv=0.750; leak=0.101 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 1 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.624 vs V_priv=0.750; leak=0.175 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 3 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 4 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 5 | key as pad | no | g=0.624 vs V_priv=0.750; leak=0.171 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 6 | key as pad | no | g=0.625 vs V_priv=0.750; leak=0.219 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 7 | key as pad | yes | g=0.750 vs V_priv=0.750; leak=0.000 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 8 | key as pad | no | g=0.687 vs V_priv=0.750; leak=0.099 bits |
| model_N2048/last | blocker4 | 2 | 2 | pub | 9 | key as pad | no | g=0.521 vs V_priv=0.750; leak=0.557 bits |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 0 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 1 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 2 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 4 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 6 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 7 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 8 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N2048/last | suit2x2 | 2 | 1 | pub | 9 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N512/last | attack2x2 | 1 | 2 | pub | 0 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | attack2x2 | 1 | 2 | pub | 1 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | attack2x2 | 1 | 2 | pub | 2 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | attack2x2 | 1 | 2 | pub | 3 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | attack2x2 | 1 | 2 | pub | 4 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | attack2x2 | 1 | 2 | pub | 5 | key as pad | no | g=0.524 vs V_priv=0.750; leak=0.452 bits |
| model_N512/last | attack2x2 | 1 | 2 | pub | 6 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | attack2x2 | 1 | 2 | pub | 7 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | attack2x2 | 1 | 2 | pub | 8 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | attack2x2 | 1 | 2 | pub | 9 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | attack2x2 | 1 | 0 | pub | 0 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| model_N512/last | attack2x2 | 1 | 0 | pub | 1 | quiet or coarse | yes | g=0.249 vs V=0.250; messages carry no information (quiet) |
| model_N512/last | attack2x2 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.103 vs V=0.250; messages carry 1.00 bits |
| model_N512/last | attack2x2 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.104 vs V=0.250; messages carry 1.00 bits |
| model_N512/last | attack2x2 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.095 vs V=0.250; messages carry 1.00 bits |
| model_N512/last | attack2x2 | 1 | 0 | pub | 5 | quiet or coarse | yes | g=0.249 vs V=0.250; messages carry no information (quiet) |
| model_N512/last | attack2x2 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.066 vs V=0.250; messages carry 1.00 bits |
| model_N512/last | attack2x2 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.037 vs V=0.250; messages carry 1.01 bits |
| model_N512/last | attack2x2 | 1 | 0 | pub | 8 | quiet or coarse | yes | g=0.249 vs V=0.250; messages carry no information (quiet) |
| model_N512/last | attack2x2 | 1 | 0 | pub | 9 | quiet or coarse | yes | g=0.249 vs V=0.250; messages carry no information (quiet) |
| model_N512/last | blocker4 | 1 | 2 | pub | 0 | key as pad | yes | g=0.374 vs V_priv=0.375; leak=0.032 bits |
| model_N512/last | blocker4 | 1 | 2 | pub | 1 | key as pad | yes | g=0.374 vs V_priv=0.375; leak=0.001 bits |
| model_N512/last | blocker4 | 1 | 2 | pub | 2 | key as pad | yes | g=0.374 vs V_priv=0.375; leak=0.034 bits |
| model_N512/last | blocker4 | 1 | 2 | pub | 3 | key as pad | yes | g=0.374 vs V_priv=0.375; leak=0.000 bits |
| model_N512/last | blocker4 | 1 | 2 | pub | 4 | key as pad | yes | g=0.374 vs V_priv=0.375; leak=0.020 bits |
| model_N512/last | blocker4 | 1 | 2 | pub | 5 | key as pad | yes | g=0.374 vs V_priv=0.375; leak=0.042 bits |
| model_N512/last | blocker4 | 1 | 2 | pub | 6 | key as pad | yes | g=0.374 vs V_priv=0.375; leak=0.073 bits |
| model_N512/last | blocker4 | 1 | 2 | pub | 7 | key as pad | no | g=0.374 vs V_priv=0.375; leak=0.114 bits |
| model_N512/last | blocker4 | 1 | 2 | pub | 8 | key as pad | no | g=0.375 vs V_priv=0.375; leak=0.120 bits |
| model_N512/last | blocker4 | 1 | 2 | pub | 9 | key as pad | yes | g=0.374 vs V_priv=0.375; leak=0.047 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 0 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.687 vs V_priv=0.750; leak=0.102 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 2 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 3 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 4 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 5 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 6 | key as pad | no | g=0.687 vs V_priv=0.750; leak=0.102 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 7 | key as pad | no | g=0.625 vs V_priv=0.750; leak=0.218 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 8 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | blocker4 | 2 | 2 | pub | 9 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N512/last | suit2x2 | 2 | 1 | pub | 0 | pad suit only | no | g=0.374 vs V=0.500; suit padded, rank in clear; I(M;X)=1.05, I(M;suit)=0.07 |
| model_N512/last | suit2x2 | 2 | 1 | pub | 1 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N512/last | suit2x2 | 2 | 1 | pub | 2 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N512/last | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N512/last | suit2x2 | 2 | 1 | pub | 4 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N512/last | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N512/last | suit2x2 | 2 | 1 | pub | 6 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N512/last | suit2x2 | 2 | 1 | pub | 7 | pad suit only | no | g=0.374 vs V=0.500; suit leaks; I(M;X)=1.11, I(M;suit)=0.12 |
| model_N512/last | suit2x2 | 2 | 1 | pub | 8 | pad suit only | no | g=0.374 vs V=0.500; suit leaks; I(M;X)=1.07, I(M;suit)=0.10 |
| model_N512/last | suit2x2 | 2 | 1 | pub | 9 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N128/last | attack2x2 | 1 | 2 | pub | 0 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | attack2x2 | 1 | 2 | pub | 1 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | attack2x2 | 1 | 2 | pub | 2 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | attack2x2 | 1 | 2 | pub | 3 | key as pad | yes | g=0.748 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | attack2x2 | 1 | 2 | pub | 4 | key as pad | no | g=0.510 vs V_priv=0.750; leak=0.448 bits |
| model_N128/last | attack2x2 | 1 | 2 | pub | 5 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | attack2x2 | 1 | 2 | pub | 6 | key as pad | no | g=0.558 vs V_priv=0.750; leak=0.263 bits |
| model_N128/last | attack2x2 | 1 | 2 | pub | 7 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | attack2x2 | 1 | 2 | pub | 8 | key as pad | no | g=0.539 vs V_priv=0.750; leak=0.453 bits |
| model_N128/last | attack2x2 | 1 | 2 | pub | 9 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | attack2x2 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.030 vs V=0.250; messages carry 1.05 bits |
| model_N128/last | attack2x2 | 1 | 0 | pub | 1 | quiet or coarse | yes | g=0.246 vs V=0.250; messages carry no information (quiet) |
| model_N128/last | attack2x2 | 1 | 0 | pub | 2 | quiet or coarse | yes | g=0.242 vs V=0.250; messages carry no information (quiet) |
| model_N128/last | attack2x2 | 1 | 0 | pub | 3 | quiet or coarse | yes | g=0.245 vs V=0.250; messages carry no information (quiet) |
| model_N128/last | attack2x2 | 1 | 0 | pub | 4 | quiet or coarse | yes | g=0.246 vs V=0.250; messages carry no information (quiet) |
| model_N128/last | attack2x2 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.075 vs V=0.250; messages carry 1.05 bits |
| model_N128/last | attack2x2 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.027 vs V=0.250; messages carry 1.01 bits |
| model_N128/last | attack2x2 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.212 vs V=0.250; messages carry 0.06 bits |
| model_N128/last | attack2x2 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.014 vs V=0.250; messages carry 1.59 bits |
| model_N128/last | attack2x2 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.028 vs V=0.250; messages carry 1.01 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 0 | key as pad | yes | g=0.368 vs V_priv=0.375; leak=0.050 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 1 | key as pad | yes | g=0.372 vs V_priv=0.375; leak=0.042 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 2 | key as pad | yes | g=0.371 vs V_priv=0.375; leak=0.028 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 3 | key as pad | yes | g=0.370 vs V_priv=0.375; leak=0.045 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 4 | key as pad | no | g=0.372 vs V_priv=0.375; leak=0.103 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 5 | key as pad | yes | g=0.370 vs V_priv=0.375; leak=0.086 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 6 | key as pad | yes | g=0.373 vs V_priv=0.375; leak=0.046 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 7 | key as pad | yes | g=0.374 vs V_priv=0.375; leak=0.040 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 8 | key as pad | yes | g=0.372 vs V_priv=0.375; leak=0.032 bits |
| model_N128/last | blocker4 | 1 | 2 | pub | 9 | key as pad | yes | g=0.371 vs V_priv=0.375; leak=0.086 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.686 vs V_priv=0.750; leak=0.099 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 1 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.624 vs V_priv=0.750; leak=0.497 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 3 | key as pad | no | g=0.500 vs V_priv=0.750; leak=0.640 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 4 | key as pad | no | g=0.686 vs V_priv=0.750; leak=0.100 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 5 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 6 | key as pad | no | g=0.622 vs V_priv=0.750; leak=0.246 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 7 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 8 | key as pad | no | g=0.621 vs V_priv=0.750; leak=0.197 bits |
| model_N128/last | blocker4 | 2 | 2 | pub | 9 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N128/last | suit2x2 | 2 | 1 | pub | 0 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N128/last | suit2x2 | 2 | 1 | pub | 1 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N128/last | suit2x2 | 2 | 1 | pub | 2 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N128/last | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N128/last | suit2x2 | 2 | 1 | pub | 4 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N128/last | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N128/last | suit2x2 | 2 | 1 | pub | 6 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N128/last | suit2x2 | 2 | 1 | pub | 7 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N128/last | suit2x2 | 2 | 1 | pub | 8 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N128/last | suit2x2 | 2 | 1 | pub | 9 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| model_N32/last | attack2x2 | 1 | 2 | pub | 0 | key as pad | no | g=0.500 vs V_priv=0.750; leak=0.491 bits |
| model_N32/last | attack2x2 | 1 | 2 | pub | 1 | key as pad | no | g=0.502 vs V_priv=0.750; leak=0.485 bits |
| model_N32/last | attack2x2 | 1 | 2 | pub | 2 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32/last | attack2x2 | 1 | 2 | pub | 3 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32/last | attack2x2 | 1 | 2 | pub | 4 | key as pad | no | g=0.500 vs V_priv=0.750; leak=0.493 bits |
| model_N32/last | attack2x2 | 1 | 2 | pub | 5 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| model_N32/last | attack2x2 | 1 | 2 | pub | 6 | key as pad | no | g=0.500 vs V_priv=0.750; leak=0.498 bits |
| model_N32/last | attack2x2 | 1 | 2 | pub | 7 | key as pad | no | g=0.500 vs V_priv=0.750; leak=0.488 bits |
| model_N32/last | attack2x2 | 1 | 2 | pub | 8 | key as pad | no | g=0.375 vs V_priv=0.750; leak=0.449 bits |
| model_N32/last | attack2x2 | 1 | 2 | pub | 9 | key as pad | no | g=0.500 vs V_priv=0.750; leak=0.492 bits |
| model_N32/last | attack2x2 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.002 vs V=0.250; messages carry 1.90 bits |
| model_N32/last | attack2x2 | 1 | 0 | pub | 1 | quiet or coarse | yes | g=0.230 vs V=0.250; messages carry no information (quiet) |
| model_N32/last | attack2x2 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.013 vs V=0.250; messages carry 1.58 bits |
| model_N32/last | attack2x2 | 1 | 0 | pub | 3 | quiet or coarse | yes | g=0.246 vs V=0.250; messages carry no information (quiet) |
| model_N32/last | attack2x2 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 1.92 bits |
| model_N32/last | attack2x2 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.208 vs V=0.250; messages carry 0.12 bits |
| model_N32/last | attack2x2 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.074 vs V=0.250; messages carry 1.04 bits |
| model_N32/last | attack2x2 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.025 vs V=0.250; messages carry 1.01 bits |
| model_N32/last | attack2x2 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.001 vs V=0.250; messages carry 1.89 bits |
| model_N32/last | attack2x2 | 1 | 0 | pub | 9 | quiet or coarse | yes | g=0.236 vs V=0.250; messages carry no information (quiet) |
| model_N32/last | blocker4 | 1 | 2 | pub | 0 | key as pad | yes | g=0.361 vs V_priv=0.375; leak=0.093 bits |
| model_N32/last | blocker4 | 1 | 2 | pub | 1 | key as pad | no | g=0.347 vs V_priv=0.375; leak=0.113 bits |
| model_N32/last | blocker4 | 1 | 2 | pub | 2 | key as pad | no | g=0.310 vs V_priv=0.375; leak=0.274 bits |
| model_N32/last | blocker4 | 1 | 2 | pub | 3 | key as pad | no | g=0.364 vs V_priv=0.375; leak=0.141 bits |
| model_N32/last | blocker4 | 1 | 2 | pub | 4 | key as pad | yes | g=0.360 vs V_priv=0.375; leak=0.032 bits |
| model_N32/last | blocker4 | 1 | 2 | pub | 5 | key as pad | no | g=0.349 vs V_priv=0.375; leak=0.045 bits |
| model_N32/last | blocker4 | 1 | 2 | pub | 6 | key as pad | no | g=0.354 vs V_priv=0.375; leak=0.002 bits |
| model_N32/last | blocker4 | 1 | 2 | pub | 7 | key as pad | no | g=0.363 vs V_priv=0.375; leak=0.130 bits |
| model_N32/last | blocker4 | 1 | 2 | pub | 8 | key as pad | no | g=0.336 vs V_priv=0.375; leak=0.049 bits |
| model_N32/last | blocker4 | 1 | 2 | pub | 9 | key as pad | no | g=0.350 vs V_priv=0.375; leak=0.002 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.619 vs V_priv=0.750; leak=0.260 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.588 vs V_priv=0.750; leak=0.367 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.547 vs V_priv=0.750; leak=0.536 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 3 | key as pad | no | g=0.555 vs V_priv=0.750; leak=0.411 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 4 | key as pad | no | g=0.677 vs V_priv=0.750; leak=0.101 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 5 | key as pad | no | g=0.517 vs V_priv=0.750; leak=0.545 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 6 | key as pad | no | g=0.312 vs V_priv=0.750; leak=0.884 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 7 | key as pad | no | g=0.482 vs V_priv=0.750; leak=0.512 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 8 | key as pad | no | g=0.552 vs V_priv=0.750; leak=0.422 bits |
| model_N32/last | blocker4 | 2 | 2 | pub | 9 | key as pad | no | g=0.614 vs V_priv=0.750; leak=0.278 bits |
| model_N32/last | suit2x2 | 2 | 1 | pub | 0 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N32/last | suit2x2 | 2 | 1 | pub | 1 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N32/last | suit2x2 | 2 | 1 | pub | 2 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N32/last | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N32/last | suit2x2 | 2 | 1 | pub | 4 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N32/last | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N32/last | suit2x2 | 2 | 1 | pub | 6 | pad suit only | no | g=0.035 vs V=0.500; suit leaks; I(M;X)=1.60, I(M;suit)=0.62 |
| model_N32/last | suit2x2 | 2 | 1 | pub | 7 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N32/last | suit2x2 | 2 | 1 | pub | 8 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| model_N32/last | suit2x2 | 2 | 1 | pub | 9 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 0 | key as pad | no | g=0.499 vs V_priv=0.750; leak=0.453 bits |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 1 | key as pad | no | g=0.498 vs V_priv=0.750; leak=0.452 bits |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 2 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 3 | key as pad | no | g=0.499 vs V_priv=0.750; leak=0.998 bits |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 4 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 5 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 6 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 7 | key as pad | no | g=0.498 vs V_priv=0.750; leak=0.453 bits |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 8 | key as pad | no | g=0.500 vs V_priv=0.750; leak=0.493 bits |
| reinforce_adv/last | attack2x2 | 1 | 2 | pub | 9 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 2.00 bits |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 1.00 bits |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 2.00 bits |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 1.99 bits |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 4 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry no information (quiet) |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 1.99 bits |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 2.00 bits |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 2.00 bits |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 2.00 bits |
| reinforce_adv/last | attack2x2 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.000 vs V=0.250; messages carry 1.97 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 0 | key as pad | no | g=0.249 vs V_priv=0.375; leak=0.406 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 1 | key as pad | no | g=0.251 vs V_priv=0.375; leak=0.002 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 2 | key as pad | no | g=0.251 vs V_priv=0.375; leak=0.035 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 3 | key as pad | no | g=0.170 vs V_priv=0.375; leak=0.444 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 4 | key as pad | no | g=0.250 vs V_priv=0.375; leak=0.479 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 5 | key as pad | no | g=0.190 vs V_priv=0.375; leak=0.481 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 6 | key as pad | no | g=0.313 vs V_priv=0.375; leak=0.048 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 7 | key as pad | no | g=0.250 vs V_priv=0.375; leak=0.247 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 8 | key as pad | no | g=0.250 vs V_priv=0.375; leak=0.100 bits |
| reinforce_adv/last | blocker4 | 1 | 2 | pub | 9 | key as pad | yes | g=0.375 vs V_priv=0.375; leak=0.048 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.549 vs V_priv=0.750; leak=0.437 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 1 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.561 vs V_priv=0.750; leak=0.492 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 3 | key as pad | no | g=0.625 vs V_priv=0.750; leak=0.248 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 4 | key as pad | yes | g=0.748 vs V_priv=0.750; leak=0.000 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 5 | key as pad | no | g=0.562 vs V_priv=0.750; leak=0.366 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 6 | key as pad | no | g=0.312 vs V_priv=0.750; leak=1.021 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 7 | key as pad | no | g=0.559 vs V_priv=0.750; leak=0.341 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 8 | key as pad | no | g=0.621 vs V_priv=0.750; leak=0.239 bits |
| reinforce_adv/last | blocker4 | 2 | 2 | pub | 9 | key as pad | no | g=0.437 vs V_priv=0.750; leak=0.918 bits |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 0 | pad suit only | no | g=0.374 vs V=0.500; suit leaks; I(M;X)=0.87, I(M;suit)=0.14 |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 1 | pad suit only | no | g=0.253 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 2 | pad suit only | no | g=0.251 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 4 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00 |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 6 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 7 | pad suit only | no | g=0.002 vs V=0.500; suit leaks; I(M;X)=1.98, I(M;suit)=0.98 |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 8 | pad suit only | yes | g=0.498 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |
| reinforce_adv/last | suit2x2 | 2 | 1 | pub | 9 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00 |

wall time 279 s for 300 runs
