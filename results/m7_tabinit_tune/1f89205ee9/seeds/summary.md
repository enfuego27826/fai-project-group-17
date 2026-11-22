| method | game | k | s | ρ | target | label | g(π_T) mean ± 95% CI | gap to lower | I(M;X) | I(M;c(X)) | I(M;c(X)\|K) | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sigma0.5 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.937 ± 0.000 | 0.000 | 4.00 | 4.00 | 4.00 | reaches best known | 3 / 3 | 4s |
| sigma1 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.937 ± 0.000 | 0.000 | 4.00 | 4.00 | 4.00 | reaches best known | 3 / 3 | 4s |
| sigma2 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.833 ± 0.090 | 0.105 | 3.74 | 3.74 | 3.74 | reaches best known | 0 / 3 | 4s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| sigma0.5 | blocker16 | 4 | 0 | priv | 100 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| sigma0.5 | blocker16 | 4 | 0 | priv | 101 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| sigma0.5 | blocker16 | 4 | 0 | priv | 102 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| sigma1 | blocker16 | 4 | 0 | priv | 100 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| sigma1 | blocker16 | 4 | 0 | priv | 101 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| sigma1 | blocker16 | 4 | 0 | priv | 102 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| sigma2 | blocker16 | 4 | 0 | priv | 100 | reaches best known | no | g=0.812 vs 0.938; I(M;X)=3.74 |
| sigma2 | blocker16 | 4 | 0 | priv | 101 | reaches best known | no | g=0.812 vs 0.938; I(M;X)=3.63 |
| sigma2 | blocker16 | 4 | 0 | priv | 102 | reaches best known | no | g=0.875 vs 0.938; I(M;X)=3.86 |

wall time 12 s for 9 runs
