| method | game | k | s | ρ | target | label | g(π_T) mean ± 95% CI | gap to lower | I(M;X) | I(M;c(X)) | I(M;c(X)\|K) | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 0.7500 | exact (code + uniform block) | 0.631 ± 0.077 | 0.119 | 3.66 | 1.72 | 1.72 | reaches best known | 3 / 10 | 924s |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.500 ± 0.070 | 0.438 | 3.50 | 3.50 | 3.50 | reaches best known | 0 / 10 | 818s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 0 | reaches best known | no | g=0.500 vs 0.750; I(M;X)=3.66 |
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 1 | reaches best known | no | g=0.687 vs 0.750; I(M;X)=3.81 |
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 2 | reaches best known | no | g=0.500 vs 0.750; I(M;X)=3.15 |
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 3 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=4.00 |
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 4 | reaches best known | no | g=0.625 vs 0.750; I(M;X)=3.61 |
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 5 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=4.00 |
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 6 | reaches best known | no | g=0.562 vs 0.750; I(M;X)=3.39 |
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 7 | reaches best known | no | g=0.500 vs 0.750; I(M;X)=3.16 |
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 8 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=4.00 |
| ppo_hidden256 | suit4x4 | 4 | 0 | priv | 9 | reaches best known | no | g=0.687 vs 0.750; I(M;X)=3.87 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 0 | reaches best known | no | g=0.500 vs 0.938; I(M;X)=3.50 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 1 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=3.00 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 2 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=3.00 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 3 | reaches best known | no | g=0.625 vs 0.938; I(M;X)=4.00 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 4 | reaches best known | no | g=0.625 vs 0.938; I(M;X)=3.50 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 5 | reaches best known | no | g=0.500 vs 0.938; I(M;X)=4.00 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 6 | reaches best known | no | g=0.625 vs 0.938; I(M;X)=3.50 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 7 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=3.00 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 8 | reaches best known | no | g=0.500 vs 0.938; I(M;X)=4.00 |
| ppo_hidden256 | attack4x4 | 2 | 0 | priv | 9 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=3.50 |

wall time 2616 s for 20 runs
