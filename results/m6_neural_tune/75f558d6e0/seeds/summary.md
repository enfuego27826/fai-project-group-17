| method | game | k | s | ρ | target | label | g(π_T) mean ± 95% CI | gap to lower | I(M;X) | I(M;c(X)) | I(M;c(X)\|K) | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| lr1e-3 | blocker16 | 4 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.116 ± 0.037 | 0.821 | 1.09 | 1.09 | 1.09 | key as pad | 0 / 3 | 81s |
| lr3e-3 | blocker16 | 4 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.088 ± 0.064 | 0.850 | 0.59 | 0.59 | 0.59 | key as pad | 0 / 3 | 82s |
| lr1e-2 | blocker16 | 4 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.094 ± 0.116 | 0.844 | 0.94 | 0.94 | 1.12 | key as pad | 0 / 3 | 58s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| lr1e-3 | blocker16 | 4 | 4 | pub | 100 | key as pad | no | g=0.108 vs 0.938; I(M;X)=0.99 |
| lr1e-3 | blocker16 | 4 | 4 | pub | 101 | key as pad | no | g=0.108 vs 0.938; I(M;X)=0.99 |
| lr1e-3 | blocker16 | 4 | 4 | pub | 102 | key as pad | no | g=0.133 vs 0.938; I(M;X)=1.30 |
| lr3e-3 | blocker16 | 4 | 4 | pub | 100 | key as pad | no | g=0.106 vs 0.938; I(M;X)=0.95 |
| lr3e-3 | blocker16 | 4 | 4 | pub | 101 | key as pad | no | g=0.058 vs 0.938; I(M;X)=0.00 |
| lr3e-3 | blocker16 | 4 | 4 | pub | 102 | key as pad | no | g=0.099 vs 0.938; I(M;X)=0.81 |
| lr1e-2 | blocker16 | 4 | 4 | pub | 100 | key as pad | no | g=0.141 vs 0.938; I(M;X)=1.27 |
| lr1e-2 | blocker16 | 4 | 4 | pub | 101 | key as pad | no | g=0.094 vs 0.938; I(M;X)=1.54 |
| lr1e-2 | blocker16 | 4 | 4 | pub | 102 | key as pad | no | g=0.047 vs 0.938; I(M;X)=0.00 |

wall time 139 s for 9 runs
