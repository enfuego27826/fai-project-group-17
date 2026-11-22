| method | game | k | s | ρ | target | label | g(π_T) mean ± 95% CI | gap to lower | I(M;X) | I(M;c(X)) | I(M;c(X)\|K) | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ppo_entropy | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.854 ± 0.090 | 0.083 | 3.82 | 3.82 | 3.82 | reaches best known | 0 / 3 | 113s |
| ppo_batch1024 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.770 ± 0.179 | 0.167 | 3.66 | 3.66 | 3.66 | reaches best known | 0 / 3 | 668s |
| ppo_value | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.458 ± 0.237 | 0.479 | 2.78 | 2.78 | 2.78 | reaches best known | 0 / 3 | 155s |
| ppo_hidden256 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.917 ± 0.090 | 0.021 | 3.99 | 3.99 | 3.99 | reaches best known | 2 / 3 | 707s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| ppo_entropy | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.875 vs 0.938; I(M;X)=3.87 |
| ppo_entropy | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.812 vs 0.938; I(M;X)=3.70 |
| ppo_entropy | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.875 vs 0.938; I(M;X)=3.87 |
| ppo_batch1024 | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.812 vs 0.938; I(M;X)=3.73 |
| ppo_batch1024 | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.687 vs 0.938; I(M;X)=3.56 |
| ppo_batch1024 | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.812 vs 0.938; I(M;X)=3.70 |
| ppo_value | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.40 |
| ppo_value | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=2.73 |
| ppo_value | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.562 vs 0.938; I(M;X)=3.20 |
| ppo_hidden256 | blocker16 | 4 | 0 | priv | 0 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| ppo_hidden256 | blocker16 | 4 | 0 | priv | 1 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| ppo_hidden256 | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.875 vs 0.938; I(M;X)=3.96 |

wall time 1283 s for 12 runs
