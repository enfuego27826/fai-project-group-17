| method | game | k | s | ρ | target | label | g(π_T) mean ± 95% CI | gap to lower | I(M;X) | I(M;c(X)) | I(M;c(X)\|K) | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| m6_baseline | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.312 ± 0.155 | 0.625 | 2.25 | 2.25 | 2.25 | reaches best known | 0 / 3 | 30s |
| a_entropy | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.437 ± 0.269 | 0.500 | 1.92 | 1.92 | 1.92 | reaches best known | 0 / 3 | 39s |
| b_batch1024 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.375 ± 0.155 | 0.563 | 2.55 | 2.55 | 2.55 | reaches best known | 0 / 3 | 178s |
| c_value | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.271 ± 0.090 | 0.667 | 2.09 | 2.09 | 2.09 | reaches best known | 0 / 3 | 70s |
| d_hidden256 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.333 ± 0.359 | 0.604 | 2.34 | 2.34 | 2.34 | reaches best known | 0 / 3 | 212s |
| e_ppo4 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.708 ± 0.180 | 0.229 | 3.49 | 3.49 | 3.49 | reaches best known | 0 / 3 | 91s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| m6_baseline | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.15 |
| m6_baseline | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.60 |
| m6_baseline | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.01 |
| a_entropy | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.500 vs 0.938; I(M;X)=2.17 |
| a_entropy | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.500 vs 0.938; I(M;X)=2.16 |
| a_entropy | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=1.44 |
| b_batch1024 | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=2.77 |
| b_batch1024 | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.28 |
| b_batch1024 | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.60 |
| c_value | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.11 |
| c_value | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.02 |
| c_value | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.15 |
| d_hidden256 | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.500 vs 0.938; I(M;X)=2.91 |
| d_hidden256 | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.05 |
| d_hidden256 | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.05 |
| e_ppo4 | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.750 vs 0.938; I(M;X)=3.62 |
| e_ppo4 | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.625 vs 0.938; I(M;X)=3.22 |
| e_ppo4 | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.750 vs 0.938; I(M;X)=3.64 |

wall time 408 s for 18 runs
