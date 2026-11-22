| method | game | k | s | ρ | exact V | g(π_T) mean ± 95% CI | gap to V (upper) | leak bits | cost of leak | seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|
| self_play_lr0.5/avg | blocker4 | 2 | 2 | pub | 3/4 | 0.342 ± 0.106 | 0.408 | 0.13 | 0.074 | 3 | 6.6s |
| self_play_lr0.5/last | blocker4 | 2 | 2 | pub | 3/4 | 0.501 ± 0.236 | 0.249 | 0.45 | 0.171 | 3 | 6.6s |
| self_play_lr1/avg | blocker4 | 2 | 2 | pub | 3/4 | 0.556 ± 0.185 | 0.194 | 0.12 | 0.058 | 3 | 6.6s |
| self_play_lr1/last | blocker4 | 2 | 2 | pub | 3/4 | 0.578 ± 0.374 | 0.172 | 0.24 | 0.107 | 3 | 6.6s |
| self_play_lr2/avg | blocker4 | 2 | 2 | pub | 3/4 | 0.548 ± 0.116 | 0.202 | 0.30 | 0.104 | 3 | 6.5s |
| self_play_lr2/last | blocker4 | 2 | 2 | pub | 3/4 | 0.517 ± 0.194 | 0.233 | 0.55 | 0.175 | 3 | 6.5s |
| self_play_lr4/avg | blocker4 | 2 | 2 | pub | 3/4 | 0.540 ± 0.157 | 0.210 | 0.38 | 0.143 | 3 | 6.5s |
| self_play_lr4/last | blocker4 | 2 | 2 | pub | 3/4 | 0.422 ± 0.054 | 0.328 | 0.94 | 0.268 | 3 | 6.5s |
| self_play_lr8/avg | blocker4 | 2 | 2 | pub | 3/4 | 0.618 ± 0.272 | 0.132 | 0.32 | 0.101 | 3 | 6.5s |
| self_play_lr8/last | blocker4 | 2 | 2 | pub | 3/4 | 0.620 ± 0.279 | 0.130 | 0.31 | 0.103 | 3 | 6.5s |

| method | game | k | s | ρ | check | yes / seeds |
|---|---|---|---|---|---|---|
| self_play_lr0.5/avg | blocker4 | 2 | 2 | pub | key as pad | 0 / 3 |
| self_play_lr0.5/last | blocker4 | 2 | 2 | pub | key as pad | 0 / 3 |
| self_play_lr1/avg | blocker4 | 2 | 2 | pub | key as pad | 0 / 3 |
| self_play_lr1/last | blocker4 | 2 | 2 | pub | key as pad | 1 / 3 |
| self_play_lr2/avg | blocker4 | 2 | 2 | pub | key as pad | 0 / 3 |
| self_play_lr2/last | blocker4 | 2 | 2 | pub | key as pad | 0 / 3 |
| self_play_lr4/avg | blocker4 | 2 | 2 | pub | key as pad | 0 / 3 |
| self_play_lr4/last | blocker4 | 2 | 2 | pub | key as pad | 0 / 3 |
| self_play_lr8/avg | blocker4 | 2 | 2 | pub | key as pad | 1 / 3 |
| self_play_lr8/last | blocker4 | 2 | 2 | pub | key as pad | 1 / 3 |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| self_play_lr0.5/avg | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.310 vs V_priv=0.750; leak=0.159 bits |
| self_play_lr0.5/avg | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.326 vs V_priv=0.750; leak=0.159 bits |
| self_play_lr0.5/avg | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.391 vs V_priv=0.750; leak=0.087 bits |
| self_play_lr0.5/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.476 vs V_priv=0.750; leak=0.633 bits |
| self_play_lr0.5/last | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.421 vs V_priv=0.750; leak=0.503 bits |
| self_play_lr0.5/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.606 vs V_priv=0.750; leak=0.213 bits |
| self_play_lr1/avg | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.558 vs V_priv=0.750; leak=0.198 bits |
| self_play_lr1/avg | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.480 vs V_priv=0.750; leak=0.153 bits |
| self_play_lr1/avg | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.629 vs V_priv=0.750; leak=0.004 bits |
| self_play_lr1/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.453 vs V_priv=0.750; leak=0.560 bits |
| self_play_lr1/last | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.536 vs V_priv=0.750; leak=0.167 bits |
| self_play_lr1/last | blocker4 | 2 | 2 | pub | 2 | key as pad | yes | g=0.745 vs V_priv=0.750; leak=0.000 bits |
| self_play_lr2/avg | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.600 vs V_priv=0.750; leak=0.229 bits |
| self_play_lr2/avg | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.531 vs V_priv=0.750; leak=0.127 bits |
| self_play_lr2/avg | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.512 vs V_priv=0.750; leak=0.534 bits |
| self_play_lr2/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.605 vs V_priv=0.750; leak=0.273 bits |
| self_play_lr2/last | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.494 vs V_priv=0.750; leak=0.649 bits |
| self_play_lr2/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.453 vs V_priv=0.750; leak=0.727 bits |
| self_play_lr4/avg | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.475 vs V_priv=0.750; leak=0.555 bits |
| self_play_lr4/avg | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.601 vs V_priv=0.750; leak=0.218 bits |
| self_play_lr4/avg | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.544 vs V_priv=0.750; leak=0.366 bits |
| self_play_lr4/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.397 vs V_priv=0.750; leak=0.828 bits |
| self_play_lr4/last | blocker4 | 2 | 2 | pub | 1 | key as pad | no | g=0.431 vs V_priv=0.750; leak=0.976 bits |
| self_play_lr4/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.438 vs V_priv=0.750; leak=1.020 bits |
| self_play_lr8/avg | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.556 vs V_priv=0.750; leak=0.457 bits |
| self_play_lr8/avg | blocker4 | 2 | 2 | pub | 1 | key as pad | yes | g=0.744 vs V_priv=0.750; leak=0.002 bits |
| self_play_lr8/avg | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.553 vs V_priv=0.750; leak=0.503 bits |
| self_play_lr8/last | blocker4 | 2 | 2 | pub | 0 | key as pad | no | g=0.549 vs V_priv=0.750; leak=0.437 bits |
| self_play_lr8/last | blocker4 | 2 | 2 | pub | 1 | key as pad | yes | g=0.749 vs V_priv=0.750; leak=0.000 bits |
| self_play_lr8/last | blocker4 | 2 | 2 | pub | 2 | key as pad | no | g=0.561 vs V_priv=0.750; leak=0.492 bits |

wall time 14 s for 15 runs
