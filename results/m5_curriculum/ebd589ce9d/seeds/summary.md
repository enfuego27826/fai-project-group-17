| method | game | k | s | ρ | exact V | g(π_T) mean ± 95% CI | gap | I(M;X) | I(M;φ(X)) | cost of leak | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| warm_priv/avg | blocker4 | 1 | 0 | pub | 1/4 | 0.250 ± 0.000 | 0.000 | 1.00 | 1.00 | 0.125 | quiet or coarse | 10 / 10 | 2.5s |
| warm_priv/avg | blocker4 | 2 | 0 | pub | 1/4 | 0.000 ± 0.000 | 0.250 | 2.00 | 2.00 | 0.750 |  |  | 4.0s |
| warm_priv/avg | blocker4 | 2 | 1 | pub | 1/2 | 0.150 ± 0.135 | 0.350 | 1.64 | 1.64 | 0.581 |  |  | 6.3s |
| warm_priv/avg | attack2x2 | 1 | 1 | pub | 1/2 | 0.317 ± 0.166 | 0.183 | 1.25 | 1.25 | 0.400 |  |  | 6.1s |
| warm_priv/last | blocker4 | 1 | 0 | pub | 1/4 | 0.219 ± 0.006 | 0.031 | 1.00 | 1.00 | 0.138 | quiet or coarse | 1 / 10 | 2.5s |
| warm_priv/last | blocker4 | 2 | 0 | pub | 1/4 | 0.000 ± 0.000 | 0.250 | 2.00 | 2.00 | 0.750 |  |  | 4.0s |
| warm_priv/last | blocker4 | 2 | 1 | pub | 1/2 | 0.235 ± 0.171 | 0.265 | 1.50 | 1.50 | 0.495 |  |  | 6.3s |
| warm_priv/last | attack2x2 | 1 | 1 | pub | 1/2 | 0.325 ± 0.170 | 0.175 | 1.28 | 1.28 | 0.400 |  |  | 6.1s |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 1/4 | 0.187 ± 0.000 | 0.063 | 0.01 | 0.01 | 0.001 | quiet or coarse | 0 / 10 | 1.3s |
| scratch10k/avg | blocker4 | 2 | 0 | pub | 1/4 | 0.189 ± 0.004 | 0.061 | 0.04 | 0.04 | 0.005 |  |  | 2.2s |
| scratch10k/avg | blocker4 | 2 | 1 | pub | 1/2 | 0.374 ± 0.000 | 0.126 | 0.00 | 0.00 | 0.000 |  |  | 3.3s |
| scratch10k/avg | attack2x2 | 1 | 1 | pub | 1/2 | 0.387 ± 0.028 | 0.113 | 0.10 | 0.10 | 0.025 |  |  | 3.0s |
| scratch10k/last | blocker4 | 1 | 0 | pub | 1/4 | 0.178 ± 0.003 | 0.072 | 0.02 | 0.02 | 0.004 | quiet or coarse | 0 / 10 | 1.3s |
| scratch10k/last | blocker4 | 2 | 0 | pub | 1/4 | 0.189 ± 0.009 | 0.061 | 0.16 | 0.16 | 0.019 |  |  | 2.2s |
| scratch10k/last | blocker4 | 2 | 1 | pub | 1/2 | 0.358 ± 0.004 | 0.142 | 0.00 | 0.00 | 0.004 |  |  | 3.3s |
| scratch10k/last | attack2x2 | 1 | 1 | pub | 1/2 | 0.375 ± 0.032 | 0.125 | 0.10 | 0.10 | 0.030 |  |  | 3.0s |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 1/4 | 0.186 ± 0.001 | 0.064 | 0.02 | 0.02 | 0.002 | quiet or coarse | 0 / 10 | 2.5s |
| scratch20k/avg | blocker4 | 2 | 0 | pub | 1/4 | 0.194 ± 0.009 | 0.056 | 0.12 | 0.12 | 0.014 |  |  | 4.4s |
| scratch20k/avg | blocker4 | 2 | 1 | pub | 1/2 | 0.375 ± 0.000 | 0.125 | 0.00 | 0.00 | 0.000 |  |  | 6.6s |
| scratch20k/avg | attack2x2 | 1 | 1 | pub | 1/2 | 0.387 ± 0.028 | 0.113 | 0.10 | 0.10 | 0.025 |  |  | 6.1s |
| scratch20k/last | blocker4 | 1 | 0 | pub | 1/4 | 0.179 ± 0.004 | 0.071 | 0.05 | 0.05 | 0.006 | quiet or coarse | 0 / 10 | 2.5s |
| scratch20k/last | blocker4 | 2 | 0 | pub | 1/4 | 0.196 ± 0.009 | 0.054 | 0.31 | 0.31 | 0.032 |  |  | 4.4s |
| scratch20k/last | blocker4 | 2 | 1 | pub | 1/2 | 0.362 ± 0.002 | 0.138 | 0.00 | 0.00 | 0.004 |  |  | 6.6s |
| scratch20k/last | attack2x2 | 1 | 1 | pub | 1/2 | 0.375 ± 0.032 | 0.125 | 0.10 | 0.10 | 0.029 |  |  | 6.1s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| warm_priv/avg | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| warm_priv/avg | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | yes | g=0.249 vs V=0.250; messages carry 1.00 bits |
| warm_priv/avg | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| warm_priv/avg | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| warm_priv/avg | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| warm_priv/avg | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| warm_priv/avg | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | yes | g=0.249 vs V=0.250; messages carry 1.00 bits |
| warm_priv/avg | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| warm_priv/avg | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | yes | g=0.249 vs V=0.250; messages carry 1.00 bits |
| warm_priv/avg | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | yes | g=0.239 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.210 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.225 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.209 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.217 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.213 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.223 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.216 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.216 vs V=0.250; messages carry 1.00 bits |
| warm_priv/last | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.221 vs V=0.250; messages carry 1.00 bits |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry 0.11 bits |
| scratch10k/avg | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch10k/last | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.176 vs V=0.250; messages carry no information (quiet) |
| scratch10k/last | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.178 vs V=0.250; messages carry no information (quiet) |
| scratch10k/last | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.181 vs V=0.250; messages carry no information (quiet) |
| scratch10k/last | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.181 vs V=0.250; messages carry no information (quiet) |
| scratch10k/last | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.174 vs V=0.250; messages carry no information (quiet) |
| scratch10k/last | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.181 vs V=0.250; messages carry no information (quiet) |
| scratch10k/last | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.167 vs V=0.250; messages carry no information (quiet) |
| scratch10k/last | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.181 vs V=0.250; messages carry no information (quiet) |
| scratch10k/last | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.181 vs V=0.250; messages carry 0.20 bits |
| scratch10k/last | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.182 vs V=0.250; messages carry no information (quiet) |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.184 vs V=0.250; messages carry no information (quiet) |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.185 vs V=0.250; messages carry no information (quiet) |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.185 vs V=0.250; messages carry no information (quiet) |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry 0.12 bits |
| scratch20k/avg | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| scratch20k/last | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.182 vs V=0.250; messages carry no information (quiet) |
| scratch20k/last | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.183 vs V=0.250; messages carry no information (quiet) |
| scratch20k/last | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.185 vs V=0.250; messages carry 0.09 bits |
| scratch20k/last | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.180 vs V=0.250; messages carry no information (quiet) |
| scratch20k/last | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.180 vs V=0.250; messages carry no information (quiet) |
| scratch20k/last | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.184 vs V=0.250; messages carry 0.12 bits |
| scratch20k/last | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.178 vs V=0.250; messages carry 0.17 bits |
| scratch20k/last | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.178 vs V=0.250; messages carry no information (quiet) |
| scratch20k/last | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.165 vs V=0.250; messages carry 0.15 bits |
| scratch20k/last | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.180 vs V=0.250; messages carry no information (quiet) |

wall time 82 s for 120 runs
