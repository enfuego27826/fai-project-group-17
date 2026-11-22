| method | game | k | s | ρ | exact V | g(π_T) mean ± 95% CI | gap to V (upper) | leak bits | cost of leak | seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline/avg | attack2x2 | 1 | 1 | pub | 1/2 | 0.399 ± 0.069 | 0.101 | 0.20 | 0.050 | 5 | 3.4s |
| baseline/avg | attack2x2 | 1 | 1 | priv | 3/4 | 0.672 ± 0.126 | 0.078 | 1.08 |  | 5 | 3.3s |
| baseline/avg | blocker4 | 2 | 1 | pub | 1/2 | 0.374 ± 0.000 | 0.126 | 0.00 | 0.000 | 5 | 3.6s |
| baseline/avg | blocker4 | 1 | 0 | pub | 1/4 | 0.187 ± 0.000 | 0.063 | 0.00 | 0.000 | 5 | 1.4s |
| baseline/avg | blocker4 | 2 | 0 | pub | 1/4 | 0.187 ± 0.001 | 0.063 | 0.00 | 0.001 | 5 | 2.4s |
| baseline/last | attack2x2 | 1 | 1 | pub | 1/2 | 0.392 ± 0.076 | 0.108 | 0.20 | 0.053 | 5 | 3.4s |
| baseline/last | attack2x2 | 1 | 1 | priv | 3/4 | 0.670 ± 0.135 | 0.080 | 1.09 |  | 5 | 3.3s |
| baseline/last | blocker4 | 2 | 1 | pub | 1/2 | 0.358 ± 0.005 | 0.142 | 0.00 | 0.003 | 5 | 3.6s |
| baseline/last | blocker4 | 1 | 0 | pub | 1/4 | 0.178 ± 0.004 | 0.072 | 0.00 | 0.002 | 5 | 1.4s |
| baseline/last | blocker4 | 2 | 0 | pub | 1/4 | 0.185 ± 0.014 | 0.065 | 0.08 | 0.011 | 5 | 2.4s |
| decay/avg | attack2x2 | 1 | 1 | pub | 1/2 | 0.301 ± 0.031 | 0.199 | 0.00 | 0.000 | 5 | 3.4s |
| decay/avg | attack2x2 | 1 | 1 | priv | 3/4 | 0.678 ± 0.035 | 0.072 | 1.18 |  | 5 | 3.3s |
| decay/avg | blocker4 | 2 | 1 | pub | 1/2 | 0.223 ± 0.012 | 0.277 | 0.00 | 0.000 | 5 | 3.7s |
| decay/avg | blocker4 | 1 | 0 | pub | 1/4 | 0.187 ± 0.000 | 0.063 | 0.00 | 0.000 | 5 | 1.4s |
| decay/avg | blocker4 | 2 | 0 | pub | 1/4 | 0.187 ± 0.000 | 0.063 | 0.00 | 0.000 | 5 | 2.4s |
| decay/last | attack2x2 | 1 | 1 | pub | 1/2 | 0.349 ± 0.008 | 0.151 | 0.00 | 0.000 | 5 | 3.4s |
| decay/last | attack2x2 | 1 | 1 | priv | 3/4 | 0.731 ± 0.003 | 0.019 | 1.35 |  | 5 | 3.3s |
| decay/last | blocker4 | 2 | 1 | pub | 1/2 | 0.274 ± 0.018 | 0.226 | 0.00 | 0.000 | 5 | 3.7s |
| decay/last | blocker4 | 1 | 0 | pub | 1/4 | 0.187 ± 0.000 | 0.063 | 0.00 | 0.000 | 5 | 1.4s |
| decay/last | blocker4 | 2 | 0 | pub | 1/4 | 0.187 ± 0.000 | 0.063 | 0.00 | 0.000 | 5 | 2.4s |
| entropy/avg | attack2x2 | 1 | 1 | pub | 1/2 | 0.132 ± 0.004 | 0.368 | 0.00 | 0.000 | 5 | 4.8s |
| entropy/avg | attack2x2 | 1 | 1 | priv | 3/4 | 0.260 ± 0.047 | 0.490 | 0.23 |  | 5 | 4.7s |
| entropy/avg | blocker4 | 2 | 1 | pub | 1/2 | 0.204 ± 0.002 | 0.296 | 0.00 | 0.000 | 5 | 5.2s |
| entropy/avg | blocker4 | 1 | 0 | pub | 1/4 | 0.187 ± 0.000 | 0.063 | 0.00 | 0.000 | 5 | 1.7s |
| entropy/avg | blocker4 | 2 | 0 | pub | 1/4 | 0.187 ± 0.000 | 0.063 | 0.00 | 0.000 | 5 | 3.2s |
| entropy/last | attack2x2 | 1 | 1 | pub | 1/2 | 0.357 ± 0.005 | 0.143 | 0.00 | 0.003 | 5 | 4.8s |
| entropy/last | attack2x2 | 1 | 1 | priv | 3/4 | 0.710 ± 0.108 | 0.040 | 1.16 |  | 5 | 4.7s |
| entropy/last | blocker4 | 2 | 1 | pub | 1/2 | 0.359 ± 0.007 | 0.141 | 0.00 | 0.005 | 5 | 5.2s |
| entropy/last | blocker4 | 1 | 0 | pub | 1/4 | 0.180 ± 0.003 | 0.070 | 0.00 | 0.006 | 5 | 1.7s |
| entropy/last | blocker4 | 2 | 0 | pub | 1/4 | 0.181 ± 0.002 | 0.069 | 0.00 | 0.005 | 5 | 3.2s |

| method | game | k | s | ρ | check | yes / seeds |
|---|---|---|---|---|---|---|
| baseline/avg | blocker4 | 1 | 0 | pub | quiet or coarse | 0 / 5 |
| baseline/last | blocker4 | 1 | 0 | pub | quiet or coarse | 0 / 5 |
| decay/avg | blocker4 | 1 | 0 | pub | quiet or coarse | 0 / 5 |
| decay/last | blocker4 | 1 | 0 | pub | quiet or coarse | 0 / 5 |
| entropy/avg | blocker4 | 1 | 0 | pub | quiet or coarse | 0 / 5 |
| entropy/last | blocker4 | 1 | 0 | pub | quiet or coarse | 0 / 5 |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| baseline/avg | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| baseline/avg | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| baseline/avg | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| baseline/avg | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| baseline/avg | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| baseline/last | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.176 vs V=0.250; messages carry no information (quiet) |
| baseline/last | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.178 vs V=0.250; messages carry no information (quiet) |
| baseline/last | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.181 vs V=0.250; messages carry no information (quiet) |
| baseline/last | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.181 vs V=0.250; messages carry no information (quiet) |
| baseline/last | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.174 vs V=0.250; messages carry no information (quiet) |
| decay/avg | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| decay/avg | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| decay/avg | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| decay/avg | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| decay/avg | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| decay/last | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| decay/last | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| decay/last | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| decay/last | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| decay/last | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| entropy/avg | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| entropy/avg | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| entropy/avg | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| entropy/avg | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| entropy/avg | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| entropy/last | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.182 vs V=0.250; messages carry no information (quiet) |
| entropy/last | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.181 vs V=0.250; messages carry no information (quiet) |
| entropy/last | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.176 vs V=0.250; messages carry no information (quiet) |
| entropy/last | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.179 vs V=0.250; messages carry no information (quiet) |
| entropy/last | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.180 vs V=0.250; messages carry no information (quiet) |

wall time 31 s for 75 runs
