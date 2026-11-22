| method | game | k | s | ρ | exact V | g(π_T) mean ± 95% CI | gap | I(M;X) | I(M;φ(X)) | cost of leak | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exact_uniform/avg | blocker4 | 1 | 0 | pub | 1/4 | 0.187 ± nan | 0.063 | 0.00 | 0.00 | -0.000 | quiet or coarse | 0 / 1 | 0.9s |
| exact_uniform/avg | blocker4 | 2 | 0 | pub | 1/4 | 0.187 ± nan | 0.063 | 0.00 | 0.00 | -0.000 |  |  | 1.9s |
| exact_uniform/avg | blocker4 | 2 | 1 | pub | 1/2 | 0.187 ± nan | 0.313 | 0.00 | 0.00 | -0.000 |  |  | 3.3s |
| exact_uniform/avg | attack2x2 | 1 | 1 | pub | 1/2 | 0.187 ± nan | 0.313 | 0.00 | 0.00 | 0.000 |  |  | 3.4s |
| exact_uniform/last | blocker4 | 1 | 0 | pub | 1/4 | 0.183 ± nan | 0.067 | 0.00 | 0.00 | 0.000 | quiet or coarse | 0 / 1 | 0.9s |
| exact_uniform/last | blocker4 | 2 | 0 | pub | 1/4 | 0.187 ± nan | 0.063 | 0.00 | 0.00 | -0.000 |  |  | 1.9s |
| exact_uniform/last | blocker4 | 2 | 1 | pub | 1/2 | 0.187 ± nan | 0.313 | 0.00 | 0.00 | 0.000 |  |  | 3.3s |
| exact_uniform/last | attack2x2 | 1 | 1 | pub | 1/2 | 0.187 ± nan | 0.313 | 0.00 | 0.00 | 0.000 |  |  | 3.4s |
| exact_random/avg | blocker4 | 1 | 0 | pub | 1/4 | 0.208 ± 0.021 | 0.042 | 0.43 | 0.43 | 0.043 | quiet or coarse | 3 / 10 | 0.9s |
| exact_random/avg | blocker4 | 2 | 0 | pub | 1/4 | 0.212 ± 0.008 | 0.038 | 0.39 | 0.39 | 0.018 |  |  | 1.9s |
| exact_random/avg | blocker4 | 2 | 1 | pub | 1/2 | 0.417 ± 0.022 | 0.083 | 0.52 | 0.52 | 0.082 |  |  | 3.2s |
| exact_random/avg | attack2x2 | 1 | 1 | pub | 1/2 | 0.340 ± 0.022 | 0.160 | 0.11 | 0.11 | 0.000 |  |  | 3.4s |
| exact_random/last | blocker4 | 1 | 0 | pub | 1/4 | 0.189 ± 0.009 | 0.061 | 0.43 | 0.43 | 0.050 | quiet or coarse | 0 / 10 | 0.9s |
| exact_random/last | blocker4 | 2 | 0 | pub | 1/4 | 0.196 ± 0.008 | 0.054 | 0.40 | 0.40 | 0.033 |  |  | 1.9s |
| exact_random/last | blocker4 | 2 | 1 | pub | 1/2 | 0.408 ± 0.024 | 0.092 | 0.52 | 0.52 | 0.088 |  |  | 3.2s |
| exact_random/last | attack2x2 | 1 | 1 | pub | 1/2 | 0.335 ± 0.027 | 0.165 | 0.12 | 0.12 | 0.003 |  |  | 3.4s |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 1/4 | 0.201 ± 0.018 | 0.049 | 0.44 | 0.44 | 0.044 | quiet or coarse | 2 / 10 | 1.2s |
| sampled_random/avg | blocker4 | 2 | 0 | pub | 1/4 | 0.226 ± 0.006 | 0.024 | 0.52 | 0.52 | 0.043 |  |  | 2.1s |
| sampled_random/avg | blocker4 | 2 | 1 | pub | 1/2 | 0.425 ± 0.032 | 0.075 | 0.59 | 0.59 | 0.116 |  |  | 3.1s |
| sampled_random/avg | attack2x2 | 1 | 1 | pub | 1/2 | 0.356 ± 0.042 | 0.144 | 0.23 | 0.23 | 0.031 |  |  | 2.8s |
| sampled_random/last | blocker4 | 1 | 0 | pub | 1/4 | 0.191 ± 0.009 | 0.059 | 0.50 | 0.50 | 0.051 | quiet or coarse | 0 / 10 | 1.2s |
| sampled_random/last | blocker4 | 2 | 0 | pub | 1/4 | 0.204 ± 0.009 | 0.046 | 0.53 | 0.53 | 0.063 |  |  | 2.1s |
| sampled_random/last | blocker4 | 2 | 1 | pub | 1/2 | 0.426 ± 0.040 | 0.074 | 0.61 | 0.61 | 0.126 |  |  | 3.1s |
| sampled_random/last | attack2x2 | 1 | 1 | pub | 1/2 | 0.350 ± 0.046 | 0.150 | 0.23 | 0.23 | 0.038 |  |  | 2.8s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| exact_uniform/avg | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| exact_uniform/last | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.183 vs V=0.250; messages carry no information (quiet) |
| exact_random/avg | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.190 vs V=0.250; messages carry 0.11 bits |
| exact_random/avg | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| exact_random/avg | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.193 vs V=0.250; messages carry 0.50 bits |
| exact_random/avg | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| exact_random/avg | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| exact_random/avg | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.190 vs V=0.250; messages carry 0.11 bits |
| exact_random/avg | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| exact_random/avg | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.190 vs V=0.250; messages carry 0.11 bits |
| exact_random/avg | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.187 vs V=0.250; messages carry no information (quiet) |
| exact_random/avg | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.190 vs V=0.250; messages carry 0.50 bits |
| exact_random/last | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.188 vs V=0.250; messages carry 0.11 bits |
| exact_random/last | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.177 vs V=0.250; messages carry no information (quiet) |
| exact_random/last | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.192 vs V=0.250; messages carry 0.50 bits |
| exact_random/last | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.198 vs V=0.250; messages carry 1.00 bits |
| exact_random/last | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.189 vs V=0.250; messages carry 1.00 bits |
| exact_random/last | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.179 vs V=0.250; messages carry 0.11 bits |
| exact_random/last | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.219 vs V=0.250; messages carry 1.00 bits |
| exact_random/last | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.183 vs V=0.250; messages carry 0.11 bits |
| exact_random/last | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.184 vs V=0.250; messages carry no information (quiet) |
| exact_random/last | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.183 vs V=0.250; messages carry 0.50 bits |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.189 vs V=0.250; messages carry 0.12 bits |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.184 vs V=0.250; messages carry 0.37 bits |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.193 vs V=0.250; messages carry 0.50 bits |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.198 vs V=0.250; messages carry 0.65 bits |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | yes | g=0.249 vs V=0.250; messages carry 1.00 bits |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.189 vs V=0.250; messages carry 0.12 bits |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | yes | g=0.250 vs V=0.250; messages carry 1.00 bits |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.189 vs V=0.250; messages carry 0.12 bits |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.185 vs V=0.250; messages carry no information (quiet) |
| sampled_random/avg | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.189 vs V=0.250; messages carry 0.50 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 0 | quiet or coarse | no | g=0.175 vs V=0.250; messages carry 0.10 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 1 | quiet or coarse | no | g=0.188 vs V=0.250; messages carry 0.50 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 2 | quiet or coarse | no | g=0.190 vs V=0.250; messages carry 0.50 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 3 | quiet or coarse | no | g=0.193 vs V=0.250; messages carry 1.00 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 4 | quiet or coarse | no | g=0.209 vs V=0.250; messages carry 1.00 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 5 | quiet or coarse | no | g=0.183 vs V=0.250; messages carry 0.13 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 6 | quiet or coarse | no | g=0.217 vs V=0.250; messages carry 1.00 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 7 | quiet or coarse | no | g=0.183 vs V=0.250; messages carry 0.14 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 8 | quiet or coarse | no | g=0.184 vs V=0.250; messages carry 0.09 bits |
| sampled_random/last | blocker4 | 1 | 0 | pub | 9 | quiet or coarse | no | g=0.185 vs V=0.250; messages carry 0.50 bits |

wall time 34 s for 84 runs
