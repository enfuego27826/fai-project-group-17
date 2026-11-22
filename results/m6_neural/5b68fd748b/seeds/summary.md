| method | game | k | s | ρ | target | label | g(π_T) mean ± 95% CI | gap to lower | I(M;X) | I(M;c(X)) | I(M;c(X)\|K) | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| exact_br | blocker16 | 2 | 2 | pub | 0.2344 | exact (code + solver V(k,inf,priv)) | 0.100 ± 0.019 | 0.135 | 0.78 | 0.78 | 0.80 | key as pad | 0 / 10 | 17s |
| exact_br | blocker16 | 2 | 1 | pub | [0.2188, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.102 ± 0.019 | 0.117 | 0.84 | 0.84 | 0.84 | reaches best known | 0 / 10 | 16s |
| exact_br | blocker16 | 2 | 0 | pub | [0.1875, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.093 ± 0.017 | 0.095 | 0.68 | 0.68 | 0.68 | reaches best known | 0 / 10 | 16s |
| exact_br | blocker16 | 4 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.123 ± 0.012 | 0.815 | 1.18 | 1.18 | 1.18 | key as pad | 0 / 10 | 83s |
| exact_br | blocker16 | 4 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.113 ± 0.018 | 0.637 | 1.03 | 1.03 | 1.03 | reaches best known | 0 / 10 | 36s |
| exact_br | blocker16 | 4 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.117 ± 0.020 | 0.383 | 1.07 | 1.07 | 1.07 | reaches best known | 0 / 10 | 25s |
| exact_br | blocker16 | 4 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.093 ± 0.020 | 0.157 | 0.67 | 0.67 | 0.67 | reaches best known | 0 / 10 | 22s |
| exact_br | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.331 ± 0.047 | 0.606 | 2.29 | 2.29 | 2.29 | reaches best known | 0 / 10 | 22s |
| exact_br | suit4x4 | 4 | 4 | pub | 0.7500 | exact (code + uniform block) | 0.155 ± 0.015 | 0.595 | 1.69 | 0.07 | 0.07 | pad suit only | 0 / 10 | 86s |
| exact_br | suit4x4 | 4 | 2 | pub | 0.7500 | exact (code + uniform block) | 0.149 ± 0.012 | 0.601 | 1.67 | 0.09 | 0.09 | pad suit only | 0 / 10 | 37s |
| exact_br | suit4x4 | 4 | 1 | pub | [0.5000, 0.7500] | bound (upper: uniform block) | 0.153 ± 0.014 | 0.347 | 1.64 | 0.04 | 0.07 | reaches best known | 0 / 10 | 25s |
| exact_br | suit4x4 | 2 | 2 | pub | 0.1875 | exact (code + solver V(k,inf,priv)) | 0.136 ± 0.002 | 0.051 | 1.50 | 0.07 | 0.07 | pad suit only | 0 / 10 | 17s |
| exact_br | suit4x4 | 4 | 0 | priv | 0.7500 | exact (code + uniform block) | 0.303 ± 0.050 | 0.447 | 2.24 | 0.79 | 0.79 | reaches best known | 0 / 10 | 22s |
| exact_br | attack4x4 | 2 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.178 ± 0.021 | 0.760 | 0.34 | 0.34 | 0.36 | key as pad | 0 / 10 | 41s |
| exact_br | attack4x4 | 2 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.170 ± 0.015 | 0.580 | 0.55 | 0.55 | 0.72 | reaches best known | 0 / 10 | 20s |
| exact_br | attack4x4 | 2 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.184 ± 0.007 | 0.316 | 0.54 | 0.54 | 0.58 | reaches best known | 0 / 10 | 18s |
| exact_br | attack4x4 | 2 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.166 ± 0.024 | 0.084 | 0.29 | 0.29 | 0.29 | reaches best known | 0 / 10 | 17s |
| exact_br | attack4x4 | 2 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.269 ± 0.060 | 0.669 | 2.91 | 2.91 | 2.91 | reaches best known | 0 / 10 | 17s |
| model_N2048 | blocker16 | 2 | 2 | pub | 0.2344 | exact (code + solver V(k,inf,priv)) | 0.120 ± 0.013 | 0.115 | 1.15 | 1.15 | 1.16 | key as pad | 0 / 10 | 18s |
| model_N2048 | blocker16 | 2 | 1 | pub | [0.2188, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.130 ± 0.013 | 0.089 | 1.32 | 1.32 | 1.32 | reaches best known | 0 / 10 | 17s |
| model_N2048 | blocker16 | 2 | 0 | pub | [0.1875, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.141 ± 0.011 | 0.046 | 1.51 | 1.51 | 1.51 | reaches best known | 1 / 10 | 17s |
| model_N2048 | blocker16 | 4 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.148 ± 0.022 | 0.790 | 1.58 | 1.58 | 1.60 | key as pad | 0 / 10 | 93s |
| model_N2048 | blocker16 | 4 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.162 ± 0.014 | 0.588 | 1.83 | 1.83 | 1.83 | reaches best known | 0 / 10 | 42s |
| model_N2048 | blocker16 | 4 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.145 ± 0.011 | 0.355 | 1.57 | 1.57 | 1.57 | reaches best known | 0 / 10 | 26s |
| model_N2048 | blocker16 | 4 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.148 ± 0.013 | 0.102 | 1.65 | 1.65 | 1.65 | reaches best known | 0 / 10 | 23s |
| model_N2048 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.331 ± 0.060 | 0.606 | 2.33 | 2.33 | 2.33 | reaches best known | 0 / 10 | 23s |
| model_N2048 | suit4x4 | 4 | 4 | pub | 0.7500 | exact (code + uniform block) | 0.177 ± 0.014 | 0.573 | 2.07 | 0.30 | 0.33 | pad suit only | 0 / 10 | 98s |
| model_N2048 | suit4x4 | 4 | 2 | pub | 0.7500 | exact (code + uniform block) | 0.153 ± 0.015 | 0.597 | 1.79 | 0.19 | 0.19 | pad suit only | 0 / 10 | 43s |
| model_N2048 | suit4x4 | 4 | 1 | pub | [0.5000, 0.7500] | bound (upper: uniform block) | 0.160 ± 0.013 | 0.340 | 1.94 | 0.27 | 0.27 | reaches best known | 0 / 10 | 26s |
| model_N2048 | suit4x4 | 2 | 2 | pub | 0.1875 | exact (code + solver V(k,inf,priv)) | 0.138 ± 0.016 | 0.050 | 1.57 | 0.13 | 0.13 | pad suit only | 0 / 10 | 18s |
| model_N2048 | suit4x4 | 4 | 0 | priv | 0.7500 | exact (code + uniform block) | 0.295 ± 0.040 | 0.455 | 2.30 | 0.87 | 0.87 | reaches best known | 0 / 10 | 23s |
| model_N2048 | attack4x4 | 2 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.148 ± 0.036 | 0.789 | 0.24 | 0.24 | 0.32 | key as pad | 0 / 10 | 45s |
| model_N2048 | attack4x4 | 2 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.144 ± 0.036 | 0.606 | 0.25 | 0.25 | 0.29 | reaches best known | 0 / 10 | 21s |
| model_N2048 | attack4x4 | 2 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.160 ± 0.023 | 0.340 | 0.46 | 0.46 | 0.61 | reaches best known | 0 / 10 | 19s |
| model_N2048 | attack4x4 | 2 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.169 ± 0.017 | 0.081 | 0.41 | 0.41 | 0.41 | reaches best known | 0 / 10 | 18s |
| model_N2048 | attack4x4 | 2 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.212 ± 0.043 | 0.725 | 2.55 | 2.55 | 2.55 | reaches best known | 0 / 10 | 18s |
| reinforce_adv | blocker16 | 2 | 2 | pub | 0.2344 | exact (code + solver V(k,inf,priv)) | 0.000 ± 0.000 | 0.234 | 1.46 | 1.46 | 1.53 | key as pad | 0 / 10 | 36s |
| reinforce_adv | blocker16 | 2 | 1 | pub | [0.2188, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.001 ± 0.002 | 0.218 | 1.43 | 1.43 | 1.43 | reaches best known | 0 / 10 | 36s |
| reinforce_adv | blocker16 | 2 | 0 | pub | [0.1875, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.000 ± 0.000 | 0.187 | 1.47 | 1.47 | 1.47 | reaches best known | 0 / 10 | 35s |
| reinforce_adv | blocker16 | 4 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.003 ± 0.004 | 0.935 | 1.69 | 1.69 | 1.73 | key as pad | 0 / 10 | 119s |
| reinforce_adv | blocker16 | 4 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.001 ± 0.002 | 0.749 | 1.65 | 1.65 | 1.69 | reaches best known | 0 / 10 | 71s |
| reinforce_adv | blocker16 | 4 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.000 ± 0.000 | 0.500 | 1.75 | 1.75 | 1.75 | reaches best known | 0 / 10 | 51s |
| reinforce_adv | blocker16 | 4 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.000 ± 0.001 | 0.250 | 2.05 | 2.05 | 2.05 | reaches best known | 0 / 10 | 48s |
| reinforce_adv | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.250 ± 0.042 | 0.688 | 2.01 | 2.01 | 2.01 | reaches best known | 0 / 10 | 47s |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 0.7500 | exact (code + uniform block) | 0.000 ± 0.000 | 0.750 | 1.30 | 0.39 | 0.42 | pad suit only | 0 / 10 | 115s |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 0.7500 | exact (code + uniform block) | 0.000 ± 0.000 | 0.750 | 1.47 | 0.39 | 0.40 | pad suit only | 0 / 10 | 62s |
| reinforce_adv | suit4x4 | 4 | 1 | pub | [0.5000, 0.7500] | bound (upper: uniform block) | 0.000 ± 0.000 | 0.500 | 1.79 | 0.35 | 0.37 | reaches best known | 0 / 10 | 49s |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 0.1875 | exact (code + solver V(k,inf,priv)) | 0.000 ± 0.000 | 0.187 | 1.18 | 0.26 | 0.27 | pad suit only | 0 / 10 | 35s |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 0.7500 | exact (code + uniform block) | 0.175 ± 0.046 | 0.575 | 1.77 | 0.54 | 0.54 | reaches best known | 0 / 10 | 45s |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.013 ± 0.019 | 0.924 | 0.44 | 0.44 | 0.47 | key as pad | 0 / 10 | 52s |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.021 ± 0.021 | 0.729 | 1.31 | 1.31 | 1.35 | reaches best known | 0 / 10 | 40s |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.001 ± 0.001 | 0.499 | 1.94 | 1.94 | 1.94 | reaches best known | 0 / 10 | 38s |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.000 ± 0.000 | 0.250 | 2.00 | 2.00 | 2.00 | reaches best known | 0 / 10 | 37s |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.125 ± 0.030 | 0.812 | 2.34 | 2.34 | 2.34 | reaches best known | 0 / 10 | 37s |
| tabular_br | blocker16 | 2 | 2 | pub | 0.2344 | exact (code + solver V(k,inf,priv)) | 0.207 ± 0.007 | 0.028 | 0.47 | 0.47 | 1.49 | key as pad | 0 / 10 | 3s |
| tabular_br | blocker16 | 2 | 1 | pub | [0.2188, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.201 ± 0.011 | 0.017 | 0.97 | 0.97 | 1.80 | reaches best known | 9 / 10 | 3s |
| tabular_br | blocker16 | 2 | 0 | pub | [0.1875, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.165 ± 0.011 | 0.023 | 1.78 | 1.78 | 1.78 | reaches best known | 6 / 10 | 2s |
| tabular_br | blocker16 | 4 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.059 ± 0.000 | 0.879 | 0.00 | 0.00 | 0.02 | key as pad | 0 / 10 | 20s |
| tabular_br | blocker16 | 4 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.120 ± 0.072 | 0.630 | 0.27 | 0.27 | 0.58 | reaches best known | 0 / 10 | 5s |
| tabular_br | blocker16 | 4 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.282 ± 0.068 | 0.218 | 1.97 | 1.97 | 2.53 | reaches best known | 0 / 10 | 5s |
| tabular_br | blocker16 | 4 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.187 ± 0.008 | 0.063 | 2.08 | 2.08 | 2.08 | reaches best known | 0 / 10 | 4s |
| tabular_br | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.931 ± 0.014 | 0.007 | 3.98 | 3.98 | 3.98 | reaches best known | 9 / 10 | 4s |
| tabular_br | suit4x4 | 4 | 4 | pub | 0.7500 | exact (code + uniform block) | 0.047 ± 0.000 | 0.703 | 0.00 | 0.00 | 0.00 | pad suit only | 0 / 10 | 18s |
| tabular_br | suit4x4 | 4 | 2 | pub | 0.7500 | exact (code + uniform block) | 0.151 ± 0.056 | 0.599 | 1.02 | 0.10 | 0.25 | pad suit only | 0 / 10 | 5s |
| tabular_br | suit4x4 | 4 | 1 | pub | [0.5000, 0.7500] | bound (upper: uniform block) | 0.243 ± 0.043 | 0.257 | 2.35 | 0.40 | 0.57 | reaches best known | 0 / 10 | 4s |
| tabular_br | suit4x4 | 2 | 2 | pub | 0.1875 | exact (code + solver V(k,inf,priv)) | 0.180 ± 0.002 | 0.007 | 0.96 | 0.04 | 0.16 | pad suit only | 0 / 10 | 3s |
| tabular_br | suit4x4 | 4 | 0 | priv | 0.7500 | exact (code + uniform block) | 0.743 ± 0.014 | 0.007 | 3.98 | 1.98 | 1.98 | reaches best known | 9 / 10 | 4s |
| tabular_br | attack4x4 | 2 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.004 ± 0.000 | 0.933 | 0.00 | 0.00 | 0.03 | key as pad | 0 / 10 | 5s |
| tabular_br | attack4x4 | 2 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.088 ± 0.044 | 0.662 | 0.40 | 0.40 | 1.28 | reaches best known | 0 / 10 | 4s |
| tabular_br | attack4x4 | 2 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.284 ± 0.037 | 0.216 | 1.53 | 1.53 | 2.26 | reaches best known | 0 / 10 | 3s |
| tabular_br | attack4x4 | 2 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.172 ± 0.016 | 0.078 | 1.08 | 1.08 | 1.08 | reaches best known | 0 / 10 | 3s |
| tabular_br | attack4x4 | 2 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.687 ± 0.133 | 0.250 | 3.35 | 3.35 | 3.35 | reaches best known | 3 / 10 | 3s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| exact_br | blocker16 | 2 | 2 | pub | 0 | key as pad | no | g=0.108 vs 0.234; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 2 | pub | 1 | key as pad | no | g=0.108 vs 0.234; I(M;X)=1.00 |
| exact_br | blocker16 | 2 | 2 | pub | 2 | key as pad | no | g=0.108 vs 0.234; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 2 | pub | 3 | key as pad | no | g=0.058 vs 0.234; I(M;X)=0.00 |
| exact_br | blocker16 | 2 | 2 | pub | 4 | key as pad | no | g=0.108 vs 0.234; I(M;X)=1.00 |
| exact_br | blocker16 | 2 | 2 | pub | 5 | key as pad | no | g=0.108 vs 0.234; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 2 | pub | 6 | key as pad | no | g=0.058 vs 0.234; I(M;X)=0.00 |
| exact_br | blocker16 | 2 | 2 | pub | 7 | key as pad | no | g=0.085 vs 0.234; I(M;X)=0.29 |
| exact_br | blocker16 | 2 | 2 | pub | 8 | key as pad | no | g=0.150 vs 0.234; I(M;X)=1.58 |
| exact_br | blocker16 | 2 | 2 | pub | 9 | key as pad | no | g=0.107 vs 0.234; I(M;X)=0.95 |
| exact_br | blocker16 | 2 | 1 | pub | 0 | reaches best known | no | g=0.148 vs 0.219; I(M;X)=1.54 |
| exact_br | blocker16 | 2 | 1 | pub | 1 | reaches best known | no | g=0.058 vs 0.219; I(M;X)=0.00 |
| exact_br | blocker16 | 2 | 1 | pub | 2 | reaches best known | no | g=0.106 vs 0.219; I(M;X)=0.90 |
| exact_br | blocker16 | 2 | 1 | pub | 3 | reaches best known | no | g=0.108 vs 0.219; I(M;X)=1.00 |
| exact_br | blocker16 | 2 | 1 | pub | 4 | reaches best known | no | g=0.108 vs 0.219; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 1 | pub | 5 | reaches best known | no | g=0.108 vs 0.219; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 1 | pub | 6 | reaches best known | no | g=0.058 vs 0.219; I(M;X)=0.00 |
| exact_br | blocker16 | 2 | 1 | pub | 7 | reaches best known | no | g=0.108 vs 0.219; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 1 | pub | 8 | reaches best known | no | g=0.106 vs 0.219; I(M;X)=0.95 |
| exact_br | blocker16 | 2 | 1 | pub | 9 | reaches best known | no | g=0.108 vs 0.219; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 0 | pub | 0 | reaches best known | no | g=0.108 vs 0.188; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 0 | pub | 1 | reaches best known | no | g=0.107 vs 0.188; I(M;X)=0.95 |
| exact_br | blocker16 | 2 | 0 | pub | 2 | reaches best known | no | g=0.106 vs 0.188; I(M;X)=0.90 |
| exact_br | blocker16 | 2 | 0 | pub | 3 | reaches best known | no | g=0.108 vs 0.188; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 0 | pub | 4 | reaches best known | no | g=0.108 vs 0.188; I(M;X)=1.00 |
| exact_br | blocker16 | 2 | 0 | pub | 5 | reaches best known | no | g=0.058 vs 0.188; I(M;X)=0.00 |
| exact_br | blocker16 | 2 | 0 | pub | 6 | reaches best known | no | g=0.058 vs 0.188; I(M;X)=0.00 |
| exact_br | blocker16 | 2 | 0 | pub | 7 | reaches best known | no | g=0.108 vs 0.188; I(M;X)=0.99 |
| exact_br | blocker16 | 2 | 0 | pub | 8 | reaches best known | no | g=0.108 vs 0.188; I(M;X)=1.00 |
| exact_br | blocker16 | 2 | 0 | pub | 9 | reaches best known | no | g=0.058 vs 0.188; I(M;X)=0.00 |
| exact_br | blocker16 | 4 | 4 | pub | 0 | key as pad | no | g=0.136 vs 0.938; I(M;X)=1.42 |
| exact_br | blocker16 | 4 | 4 | pub | 1 | key as pad | no | g=0.108 vs 0.938; I(M;X)=0.99 |
| exact_br | blocker16 | 4 | 4 | pub | 2 | key as pad | no | g=0.149 vs 0.938; I(M;X)=1.55 |
| exact_br | blocker16 | 4 | 4 | pub | 3 | key as pad | no | g=0.137 vs 0.938; I(M;X)=1.40 |
| exact_br | blocker16 | 4 | 4 | pub | 4 | key as pad | no | g=0.135 vs 0.938; I(M;X)=1.37 |
| exact_br | blocker16 | 4 | 4 | pub | 5 | key as pad | no | g=0.106 vs 0.938; I(M;X)=0.90 |
| exact_br | blocker16 | 4 | 4 | pub | 6 | key as pad | no | g=0.105 vs 0.938; I(M;X)=0.90 |
| exact_br | blocker16 | 4 | 4 | pub | 7 | key as pad | no | g=0.133 vs 0.938; I(M;X)=1.30 |
| exact_br | blocker16 | 4 | 4 | pub | 8 | key as pad | no | g=0.108 vs 0.938; I(M;X)=1.00 |
| exact_br | blocker16 | 4 | 4 | pub | 9 | key as pad | no | g=0.107 vs 0.938; I(M;X)=0.99 |
| exact_br | blocker16 | 4 | 2 | pub | 0 | reaches best known | no | g=0.108 vs 0.750; I(M;X)=1.00 |
| exact_br | blocker16 | 4 | 2 | pub | 1 | reaches best known | no | g=0.107 vs 0.750; I(M;X)=0.95 |
| exact_br | blocker16 | 4 | 2 | pub | 2 | reaches best known | no | g=0.058 vs 0.750; I(M;X)=0.00 |
| exact_br | blocker16 | 4 | 2 | pub | 3 | reaches best known | no | g=0.106 vs 0.750; I(M;X)=0.90 |
| exact_br | blocker16 | 4 | 2 | pub | 4 | reaches best known | no | g=0.137 vs 0.750; I(M;X)=1.42 |
| exact_br | blocker16 | 4 | 2 | pub | 5 | reaches best known | no | g=0.108 vs 0.750; I(M;X)=1.00 |
| exact_br | blocker16 | 4 | 2 | pub | 6 | reaches best known | no | g=0.146 vs 0.750; I(M;X)=1.50 |
| exact_br | blocker16 | 4 | 2 | pub | 7 | reaches best known | no | g=0.108 vs 0.750; I(M;X)=0.99 |
| exact_br | blocker16 | 4 | 2 | pub | 8 | reaches best known | no | g=0.148 vs 0.750; I(M;X)=1.54 |
| exact_br | blocker16 | 4 | 2 | pub | 9 | reaches best known | no | g=0.107 vs 0.750; I(M;X)=0.95 |
| exact_br | blocker16 | 4 | 1 | pub | 0 | reaches best known | no | g=0.132 vs 0.500; I(M;X)=1.24 |
| exact_br | blocker16 | 4 | 1 | pub | 1 | reaches best known | no | g=0.108 vs 0.500; I(M;X)=0.99 |
| exact_br | blocker16 | 4 | 1 | pub | 2 | reaches best known | no | g=0.151 vs 0.500; I(M;X)=1.58 |
| exact_br | blocker16 | 4 | 1 | pub | 3 | reaches best known | no | g=0.058 vs 0.500; I(M;X)=0.00 |
| exact_br | blocker16 | 4 | 1 | pub | 4 | reaches best known | no | g=0.108 vs 0.500; I(M;X)=0.95 |
| exact_br | blocker16 | 4 | 1 | pub | 5 | reaches best known | no | g=0.148 vs 0.500; I(M;X)=1.55 |
| exact_br | blocker16 | 4 | 1 | pub | 6 | reaches best known | no | g=0.107 vs 0.500; I(M;X)=0.95 |
| exact_br | blocker16 | 4 | 1 | pub | 7 | reaches best known | no | g=0.108 vs 0.500; I(M;X)=1.00 |
| exact_br | blocker16 | 4 | 1 | pub | 8 | reaches best known | no | g=0.107 vs 0.500; I(M;X)=0.95 |
| exact_br | blocker16 | 4 | 1 | pub | 9 | reaches best known | no | g=0.146 vs 0.500; I(M;X)=1.51 |
| exact_br | blocker16 | 4 | 0 | pub | 0 | reaches best known | no | g=0.108 vs 0.250; I(M;X)=0.99 |
| exact_br | blocker16 | 4 | 0 | pub | 1 | reaches best known | no | g=0.108 vs 0.250; I(M;X)=0.99 |
| exact_br | blocker16 | 4 | 0 | pub | 2 | reaches best known | no | g=0.106 vs 0.250; I(M;X)=0.90 |
| exact_br | blocker16 | 4 | 0 | pub | 3 | reaches best known | no | g=0.108 vs 0.250; I(M;X)=0.99 |
| exact_br | blocker16 | 4 | 0 | pub | 4 | reaches best known | no | g=0.059 vs 0.250; I(M;X)=0.00 |
| exact_br | blocker16 | 4 | 0 | pub | 5 | reaches best known | no | g=0.058 vs 0.250; I(M;X)=0.00 |
| exact_br | blocker16 | 4 | 0 | pub | 6 | reaches best known | no | g=0.136 vs 0.250; I(M;X)=1.41 |
| exact_br | blocker16 | 4 | 0 | pub | 7 | reaches best known | no | g=0.078 vs 0.250; I(M;X)=0.44 |
| exact_br | blocker16 | 4 | 0 | pub | 8 | reaches best known | no | g=0.058 vs 0.250; I(M;X)=0.00 |
| exact_br | blocker16 | 4 | 0 | pub | 9 | reaches best known | no | g=0.108 vs 0.250; I(M;X)=0.99 |
| exact_br | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.15 |
| exact_br | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.60 |
| exact_br | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.01 |
| exact_br | blocker16 | 4 | 0 | priv | 3 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=1.88 |
| exact_br | blocker16 | 4 | 0 | priv | 4 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.41 |
| exact_br | blocker16 | 4 | 0 | priv | 5 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=1.77 |
| exact_br | blocker16 | 4 | 0 | priv | 6 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.43 |
| exact_br | blocker16 | 4 | 0 | priv | 7 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.52 |
| exact_br | blocker16 | 4 | 0 | priv | 8 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.41 |
| exact_br | blocker16 | 4 | 0 | priv | 9 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=2.73 |
| exact_br | suit4x4 | 4 | 4 | pub | 0 | pad suit only | no | g=0.140 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.47, I(M;suit)=0.05, I(M;suit|K)=0.07 |
| exact_br | suit4x4 | 4 | 4 | pub | 1 | pad suit only | no | g=0.139 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.56, I(M;suit)=0.06, I(M;suit|K)=0.06 |
| exact_br | suit4x4 | 4 | 4 | pub | 2 | pad suit only | no | g=0.171 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.92, I(M;suit)=0.17, I(M;suit|K)=0.17 |
| exact_br | suit4x4 | 4 | 4 | pub | 3 | pad suit only | no | g=0.180 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.98, I(M;suit)=0.10, I(M;suit|K)=0.10 |
| exact_br | suit4x4 | 4 | 4 | pub | 4 | pad suit only | no | g=0.185 vs 0.750; suit not sent, rank in clear; I(M;X)=2.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| exact_br | suit4x4 | 4 | 4 | pub | 5 | pad suit only | no | g=0.140 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.52, I(M;suit)=0.06, I(M;suit|K)=0.07 |
| exact_br | suit4x4 | 4 | 4 | pub | 6 | pad suit only | no | g=0.133 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.48, I(M;suit)=0.10, I(M;suit|K)=0.10 |
| exact_br | suit4x4 | 4 | 4 | pub | 7 | pad suit only | no | g=0.180 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.98, I(M;suit)=0.10, I(M;suit|K)=0.10 |
| exact_br | suit4x4 | 4 | 4 | pub | 8 | pad suit only | no | g=0.139 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.51, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| exact_br | suit4x4 | 4 | 4 | pub | 9 | pad suit only | no | g=0.138 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.50, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| exact_br | suit4x4 | 4 | 2 | pub | 0 | pad suit only | no | g=0.180 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.98, I(M;suit)=0.10, I(M;suit|K)=0.10 |
| exact_br | suit4x4 | 4 | 2 | pub | 1 | pad suit only | no | g=0.139 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.55, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| exact_br | suit4x4 | 4 | 2 | pub | 2 | pad suit only | no | g=0.138 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.55, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| exact_br | suit4x4 | 4 | 2 | pub | 3 | pad suit only | no | g=0.170 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.92, I(M;suit)=0.17, I(M;suit|K)=0.17 |
| exact_br | suit4x4 | 4 | 2 | pub | 4 | pad suit only | no | g=0.139 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.56, I(M;suit)=0.06, I(M;suit|K)=0.06 |
| exact_br | suit4x4 | 4 | 2 | pub | 5 | pad suit only | no | g=0.134 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.51, I(M;suit)=0.21, I(M;suit|K)=0.22 |
| exact_br | suit4x4 | 4 | 2 | pub | 6 | pad suit only | no | g=0.139 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.50, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| exact_br | suit4x4 | 4 | 2 | pub | 7 | pad suit only | no | g=0.139 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.58, I(M;suit)=0.08, I(M;suit|K)=0.08 |
| exact_br | suit4x4 | 4 | 2 | pub | 8 | pad suit only | no | g=0.140 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.55, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| exact_br | suit4x4 | 4 | 2 | pub | 9 | pad suit only | no | g=0.171 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.98, I(M;suit)=0.10, I(M;suit|K)=0.10 |
| exact_br | suit4x4 | 4 | 1 | pub | 0 | reaches best known | no | g=0.155 vs 0.500; I(M;X)=1.55 |
| exact_br | suit4x4 | 4 | 1 | pub | 1 | reaches best known | no | g=0.164 vs 0.500; I(M;X)=1.69 |
| exact_br | suit4x4 | 4 | 1 | pub | 2 | reaches best known | no | g=0.139 vs 0.500; I(M;X)=1.52 |
| exact_br | suit4x4 | 4 | 1 | pub | 3 | reaches best known | no | g=0.139 vs 0.500; I(M;X)=1.55 |
| exact_br | suit4x4 | 4 | 1 | pub | 4 | reaches best known | no | g=0.139 vs 0.500; I(M;X)=1.50 |
| exact_br | suit4x4 | 4 | 1 | pub | 5 | reaches best known | no | g=0.140 vs 0.500; I(M;X)=1.55 |
| exact_br | suit4x4 | 4 | 1 | pub | 6 | reaches best known | no | g=0.186 vs 0.500; I(M;X)=2.00 |
| exact_br | suit4x4 | 4 | 1 | pub | 7 | reaches best known | no | g=0.185 vs 0.500; I(M;X)=2.00 |
| exact_br | suit4x4 | 4 | 1 | pub | 8 | reaches best known | no | g=0.140 vs 0.500; I(M;X)=1.52 |
| exact_br | suit4x4 | 4 | 1 | pub | 9 | reaches best known | no | g=0.140 vs 0.500; I(M;X)=1.56 |
| exact_br | suit4x4 | 2 | 2 | pub | 0 | pad suit only | no | g=0.139 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.55, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| exact_br | suit4x4 | 2 | 2 | pub | 1 | pad suit only | no | g=0.138 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.55, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| exact_br | suit4x4 | 2 | 2 | pub | 2 | pad suit only | no | g=0.134 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.42, I(M;suit)=0.09, I(M;suit|K)=0.09 |
| exact_br | suit4x4 | 2 | 2 | pub | 3 | pad suit only | no | g=0.134 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.42, I(M;suit)=0.09, I(M;suit|K)=0.09 |
| exact_br | suit4x4 | 2 | 2 | pub | 4 | pad suit only | no | g=0.138 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.56, I(M;suit)=0.06, I(M;suit|K)=0.06 |
| exact_br | suit4x4 | 2 | 2 | pub | 5 | pad suit only | no | g=0.140 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.56, I(M;suit)=0.06, I(M;suit|K)=0.06 |
| exact_br | suit4x4 | 2 | 2 | pub | 6 | pad suit only | no | g=0.134 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.51, I(M;suit)=0.18, I(M;suit|K)=0.18 |
| exact_br | suit4x4 | 2 | 2 | pub | 7 | pad suit only | no | g=0.134 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.46, I(M;suit)=0.02, I(M;suit|K)=0.03 |
| exact_br | suit4x4 | 2 | 2 | pub | 8 | pad suit only | no | g=0.134 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.42, I(M;suit)=0.09, I(M;suit|K)=0.09 |
| exact_br | suit4x4 | 2 | 2 | pub | 9 | pad suit only | no | g=0.139 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.55, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| exact_br | suit4x4 | 4 | 0 | priv | 0 | reaches best known | no | g=0.375 vs 0.750; I(M;X)=2.22 |
| exact_br | suit4x4 | 4 | 0 | priv | 1 | reaches best known | no | g=0.280 vs 0.750; I(M;X)=2.36 |
| exact_br | suit4x4 | 4 | 0 | priv | 2 | reaches best known | no | g=0.312 vs 0.750; I(M;X)=2.48 |
| exact_br | suit4x4 | 4 | 0 | priv | 3 | reaches best known | no | g=0.375 vs 0.750; I(M;X)=2.89 |
| exact_br | suit4x4 | 4 | 0 | priv | 4 | reaches best known | no | g=0.233 vs 0.750; I(M;X)=1.50 |
| exact_br | suit4x4 | 4 | 0 | priv | 5 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=1.95 |
| exact_br | suit4x4 | 4 | 0 | priv | 6 | reaches best known | no | g=0.375 vs 0.750; I(M;X)=2.73 |
| exact_br | suit4x4 | 4 | 0 | priv | 7 | reaches best known | no | g=0.234 vs 0.750; I(M;X)=1.79 |
| exact_br | suit4x4 | 4 | 0 | priv | 8 | reaches best known | no | g=0.281 vs 0.750; I(M;X)=1.98 |
| exact_br | suit4x4 | 4 | 0 | priv | 9 | reaches best known | no | g=0.375 vs 0.750; I(M;X)=2.47 |
| exact_br | attack4x4 | 2 | 4 | pub | 0 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 4 | pub | 1 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 4 | pub | 2 | key as pad | no | g=0.093 vs 0.938; I(M;X)=0.28 |
| exact_br | attack4x4 | 2 | 4 | pub | 3 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 4 | pub | 4 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 4 | pub | 5 | key as pad | no | g=0.187 vs 0.938; I(M;X)=1.07 |
| exact_br | attack4x4 | 2 | 4 | pub | 6 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 4 | pub | 7 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 4 | pub | 8 | key as pad | no | g=0.186 vs 0.938; I(M;X)=1.09 |
| exact_br | attack4x4 | 2 | 4 | pub | 9 | key as pad | no | g=0.187 vs 0.938; I(M;X)=1.01 |
| exact_br | attack4x4 | 2 | 2 | pub | 0 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=1.08 |
| exact_br | attack4x4 | 2 | 2 | pub | 1 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 2 | pub | 2 | reaches best known | no | g=0.125 vs 0.750; I(M;X)=0.81 |
| exact_br | attack4x4 | 2 | 2 | pub | 3 | reaches best known | no | g=0.156 vs 0.750; I(M;X)=0.20 |
| exact_br | attack4x4 | 2 | 2 | pub | 4 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 2 | pub | 5 | reaches best known | no | g=0.156 vs 0.750; I(M;X)=0.54 |
| exact_br | attack4x4 | 2 | 2 | pub | 6 | reaches best known | no | g=0.171 vs 0.750; I(M;X)=0.94 |
| exact_br | attack4x4 | 2 | 2 | pub | 7 | reaches best known | no | g=0.156 vs 0.750; I(M;X)=0.84 |
| exact_br | attack4x4 | 2 | 2 | pub | 8 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 2 | pub | 9 | reaches best known | no | g=0.186 vs 0.750; I(M;X)=1.07 |
| exact_br | attack4x4 | 2 | 1 | pub | 0 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 1 | pub | 1 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 1 | pub | 2 | reaches best known | no | g=0.186 vs 0.500; I(M;X)=1.05 |
| exact_br | attack4x4 | 2 | 1 | pub | 3 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 1 | pub | 4 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=1.07 |
| exact_br | attack4x4 | 2 | 1 | pub | 5 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 1 | pub | 6 | reaches best known | no | g=0.186 vs 0.500; I(M;X)=1.02 |
| exact_br | attack4x4 | 2 | 1 | pub | 7 | reaches best known | no | g=0.156 vs 0.500; I(M;X)=1.17 |
| exact_br | attack4x4 | 2 | 1 | pub | 8 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=1.07 |
| exact_br | attack4x4 | 2 | 1 | pub | 9 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 0 | pub | 0 | reaches best known | no | g=0.195 vs 0.250; I(M;X)=1.08 |
| exact_br | attack4x4 | 2 | 0 | pub | 1 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 0 | pub | 2 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 0 | pub | 3 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 0 | pub | 4 | reaches best known | no | g=0.093 vs 0.250; I(M;X)=0.01 |
| exact_br | attack4x4 | 2 | 0 | pub | 5 | reaches best known | no | g=0.145 vs 0.250; I(M;X)=0.26 |
| exact_br | attack4x4 | 2 | 0 | pub | 6 | reaches best known | no | g=0.186 vs 0.250; I(M;X)=1.07 |
| exact_br | attack4x4 | 2 | 0 | pub | 7 | reaches best known | no | g=0.144 vs 0.250; I(M;X)=0.24 |
| exact_br | attack4x4 | 2 | 0 | pub | 8 | reaches best known | no | g=0.145 vs 0.250; I(M;X)=0.25 |
| exact_br | attack4x4 | 2 | 0 | pub | 9 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=0.00 |
| exact_br | attack4x4 | 2 | 0 | priv | 0 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.50 |
| exact_br | attack4x4 | 2 | 0 | priv | 1 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=2.80 |
| exact_br | attack4x4 | 2 | 0 | priv | 2 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=3.49 |
| exact_br | attack4x4 | 2 | 0 | priv | 3 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=3.00 |
| exact_br | attack4x4 | 2 | 0 | priv | 4 | reaches best known | no | g=0.125 vs 0.938; I(M;X)=2.28 |
| exact_br | attack4x4 | 2 | 0 | priv | 5 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=3.01 |
| exact_br | attack4x4 | 2 | 0 | priv | 6 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=3.50 |
| exact_br | attack4x4 | 2 | 0 | priv | 7 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=3.00 |
| exact_br | attack4x4 | 2 | 0 | priv | 8 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=3.00 |
| exact_br | attack4x4 | 2 | 0 | priv | 9 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.50 |
| model_N2048 | blocker16 | 2 | 2 | pub | 0 | key as pad | no | g=0.138 vs 0.234; I(M;X)=1.48 |
| model_N2048 | blocker16 | 2 | 2 | pub | 1 | key as pad | no | g=0.139 vs 0.234; I(M;X)=1.51 |
| model_N2048 | blocker16 | 2 | 2 | pub | 2 | key as pad | no | g=0.141 vs 0.234; I(M;X)=1.48 |
| model_N2048 | blocker16 | 2 | 2 | pub | 3 | key as pad | no | g=0.109 vs 0.234; I(M;X)=0.95 |
| model_N2048 | blocker16 | 2 | 2 | pub | 4 | key as pad | no | g=0.097 vs 0.234; I(M;X)=0.70 |
| model_N2048 | blocker16 | 2 | 2 | pub | 5 | key as pad | no | g=0.106 vs 0.234; I(M;X)=0.95 |
| model_N2048 | blocker16 | 2 | 2 | pub | 6 | key as pad | no | g=0.103 vs 0.234; I(M;X)=0.90 |
| model_N2048 | blocker16 | 2 | 2 | pub | 7 | key as pad | no | g=0.130 vs 0.234; I(M;X)=1.30 |
| model_N2048 | blocker16 | 2 | 2 | pub | 8 | key as pad | no | g=0.130 vs 0.234; I(M;X)=1.37 |
| model_N2048 | blocker16 | 2 | 2 | pub | 9 | key as pad | no | g=0.103 vs 0.234; I(M;X)=0.90 |
| model_N2048 | blocker16 | 2 | 1 | pub | 0 | reaches best known | no | g=0.140 vs 0.219; I(M;X)=1.42 |
| model_N2048 | blocker16 | 2 | 1 | pub | 1 | reaches best known | no | g=0.143 vs 0.219; I(M;X)=1.51 |
| model_N2048 | blocker16 | 2 | 1 | pub | 2 | reaches best known | no | g=0.146 vs 0.219; I(M;X)=1.58 |
| model_N2048 | blocker16 | 2 | 1 | pub | 3 | reaches best known | no | g=0.103 vs 0.219; I(M;X)=0.95 |
| model_N2048 | blocker16 | 2 | 1 | pub | 4 | reaches best known | no | g=0.141 vs 0.219; I(M;X)=1.48 |
| model_N2048 | blocker16 | 2 | 1 | pub | 5 | reaches best known | no | g=0.130 vs 0.219; I(M;X)=1.42 |
| model_N2048 | blocker16 | 2 | 1 | pub | 6 | reaches best known | no | g=0.106 vs 0.219; I(M;X)=0.96 |
| model_N2048 | blocker16 | 2 | 1 | pub | 7 | reaches best known | no | g=0.144 vs 0.219; I(M;X)=1.50 |
| model_N2048 | blocker16 | 2 | 1 | pub | 8 | reaches best known | no | g=0.140 vs 0.219; I(M;X)=1.48 |
| model_N2048 | blocker16 | 2 | 1 | pub | 9 | reaches best known | no | g=0.105 vs 0.219; I(M;X)=0.95 |
| model_N2048 | blocker16 | 2 | 0 | pub | 0 | reaches best known | no | g=0.145 vs 0.188; I(M;X)=1.58 |
| model_N2048 | blocker16 | 2 | 0 | pub | 1 | reaches best known | no | g=0.105 vs 0.188; I(M;X)=0.99 |
| model_N2048 | blocker16 | 2 | 0 | pub | 2 | reaches best known | yes | g=0.168 vs 0.188; I(M;X)=1.88 |
| model_N2048 | blocker16 | 2 | 0 | pub | 3 | reaches best known | no | g=0.141 vs 0.188; I(M;X)=1.51 |
| model_N2048 | blocker16 | 2 | 0 | pub | 4 | reaches best known | no | g=0.139 vs 0.188; I(M;X)=1.51 |
| model_N2048 | blocker16 | 2 | 0 | pub | 5 | reaches best known | no | g=0.144 vs 0.188; I(M;X)=1.55 |
| model_N2048 | blocker16 | 2 | 0 | pub | 6 | reaches best known | no | g=0.140 vs 0.188; I(M;X)=1.50 |
| model_N2048 | blocker16 | 2 | 0 | pub | 7 | reaches best known | no | g=0.149 vs 0.188; I(M;X)=1.58 |
| model_N2048 | blocker16 | 2 | 0 | pub | 8 | reaches best known | no | g=0.133 vs 0.188; I(M;X)=1.42 |
| model_N2048 | blocker16 | 2 | 0 | pub | 9 | reaches best known | no | g=0.147 vs 0.188; I(M;X)=1.56 |
| model_N2048 | blocker16 | 4 | 4 | pub | 0 | key as pad | no | g=0.125 vs 0.938; I(M;X)=1.20 |
| model_N2048 | blocker16 | 4 | 4 | pub | 1 | key as pad | no | g=0.137 vs 0.938; I(M;X)=1.42 |
| model_N2048 | blocker16 | 4 | 4 | pub | 2 | key as pad | no | g=0.169 vs 0.938; I(M;X)=1.95 |
| model_N2048 | blocker16 | 4 | 4 | pub | 3 | key as pad | no | g=0.158 vs 0.938; I(M;X)=1.77 |
| model_N2048 | blocker16 | 4 | 4 | pub | 4 | key as pad | no | g=0.084 vs 0.938; I(M;X)=0.54 |
| model_N2048 | blocker16 | 4 | 4 | pub | 5 | key as pad | no | g=0.162 vs 0.938; I(M;X)=1.91 |
| model_N2048 | blocker16 | 4 | 4 | pub | 6 | key as pad | no | g=0.188 vs 0.938; I(M;X)=2.23 |
| model_N2048 | blocker16 | 4 | 4 | pub | 7 | key as pad | no | g=0.165 vs 0.938; I(M;X)=1.90 |
| model_N2048 | blocker16 | 4 | 4 | pub | 8 | key as pad | no | g=0.167 vs 0.938; I(M;X)=1.90 |
| model_N2048 | blocker16 | 4 | 4 | pub | 9 | key as pad | no | g=0.122 vs 0.938; I(M;X)=1.02 |
| model_N2048 | blocker16 | 4 | 2 | pub | 0 | reaches best known | no | g=0.161 vs 0.750; I(M;X)=1.81 |
| model_N2048 | blocker16 | 4 | 2 | pub | 1 | reaches best known | no | g=0.168 vs 0.750; I(M;X)=1.88 |
| model_N2048 | blocker16 | 4 | 2 | pub | 2 | reaches best known | no | g=0.150 vs 0.750; I(M;X)=1.67 |
| model_N2048 | blocker16 | 4 | 2 | pub | 3 | reaches best known | no | g=0.173 vs 0.750; I(M;X)=2.00 |
| model_N2048 | blocker16 | 4 | 2 | pub | 4 | reaches best known | no | g=0.154 vs 0.750; I(M;X)=1.79 |
| model_N2048 | blocker16 | 4 | 2 | pub | 5 | reaches best known | no | g=0.179 vs 0.750; I(M;X)=2.23 |
| model_N2048 | blocker16 | 4 | 2 | pub | 6 | reaches best known | no | g=0.172 vs 0.750; I(M;X)=1.88 |
| model_N2048 | blocker16 | 4 | 2 | pub | 7 | reaches best known | no | g=0.131 vs 0.750; I(M;X)=1.37 |
| model_N2048 | blocker16 | 4 | 2 | pub | 8 | reaches best known | no | g=0.192 vs 0.750; I(M;X)=2.22 |
| model_N2048 | blocker16 | 4 | 2 | pub | 9 | reaches best known | no | g=0.136 vs 0.750; I(M;X)=1.42 |
| model_N2048 | blocker16 | 4 | 1 | pub | 0 | reaches best known | no | g=0.138 vs 0.500; I(M;X)=1.50 |
| model_N2048 | blocker16 | 4 | 1 | pub | 1 | reaches best known | no | g=0.169 vs 0.500; I(M;X)=1.90 |
| model_N2048 | blocker16 | 4 | 1 | pub | 2 | reaches best known | no | g=0.140 vs 0.500; I(M;X)=1.48 |
| model_N2048 | blocker16 | 4 | 1 | pub | 3 | reaches best known | no | g=0.113 vs 0.500; I(M;X)=1.06 |
| model_N2048 | blocker16 | 4 | 1 | pub | 4 | reaches best known | no | g=0.140 vs 0.500; I(M;X)=1.50 |
| model_N2048 | blocker16 | 4 | 1 | pub | 5 | reaches best known | no | g=0.157 vs 0.500; I(M;X)=1.83 |
| model_N2048 | blocker16 | 4 | 1 | pub | 6 | reaches best known | no | g=0.140 vs 0.500; I(M;X)=1.48 |
| model_N2048 | blocker16 | 4 | 1 | pub | 7 | reaches best known | no | g=0.164 vs 0.500; I(M;X)=1.85 |
| model_N2048 | blocker16 | 4 | 1 | pub | 8 | reaches best known | no | g=0.144 vs 0.500; I(M;X)=1.55 |
| model_N2048 | blocker16 | 4 | 1 | pub | 9 | reaches best known | no | g=0.141 vs 0.500; I(M;X)=1.51 |
| model_N2048 | blocker16 | 4 | 0 | pub | 0 | reaches best known | no | g=0.164 vs 0.250; I(M;X)=1.88 |
| model_N2048 | blocker16 | 4 | 0 | pub | 1 | reaches best known | no | g=0.142 vs 0.250; I(M;X)=1.55 |
| model_N2048 | blocker16 | 4 | 0 | pub | 2 | reaches best known | no | g=0.132 vs 0.250; I(M;X)=1.40 |
| model_N2048 | blocker16 | 4 | 0 | pub | 3 | reaches best known | no | g=0.177 vs 0.250; I(M;X)=1.98 |
| model_N2048 | blocker16 | 4 | 0 | pub | 4 | reaches best known | no | g=0.130 vs 0.250; I(M;X)=1.36 |
| model_N2048 | blocker16 | 4 | 0 | pub | 5 | reaches best known | no | g=0.140 vs 0.250; I(M;X)=1.74 |
| model_N2048 | blocker16 | 4 | 0 | pub | 6 | reaches best known | no | g=0.161 vs 0.250; I(M;X)=1.88 |
| model_N2048 | blocker16 | 4 | 0 | pub | 7 | reaches best known | no | g=0.141 vs 0.250; I(M;X)=1.50 |
| model_N2048 | blocker16 | 4 | 0 | pub | 8 | reaches best known | no | g=0.126 vs 0.250; I(M;X)=1.30 |
| model_N2048 | blocker16 | 4 | 0 | pub | 9 | reaches best known | no | g=0.164 vs 0.250; I(M;X)=1.88 |
| model_N2048 | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.48 |
| model_N2048 | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.28 |
| model_N2048 | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.11 |
| model_N2048 | blocker16 | 4 | 0 | priv | 3 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.02 |
| model_N2048 | blocker16 | 4 | 0 | priv | 4 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.27 |
| model_N2048 | blocker16 | 4 | 0 | priv | 5 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=2.61 |
| model_N2048 | blocker16 | 4 | 0 | priv | 6 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.55 |
| model_N2048 | blocker16 | 4 | 0 | priv | 7 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=1.53 |
| model_N2048 | blocker16 | 4 | 0 | priv | 8 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=2.83 |
| model_N2048 | blocker16 | 4 | 0 | priv | 9 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.66 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 0 | pad suit only | no | g=0.182 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.03, I(M;suit)=0.28, I(M;suit|K)=0.40 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 1 | pad suit only | no | g=0.186 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.28, I(M;suit)=0.40, I(M;suit|K)=0.40 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 2 | pad suit only | no | g=0.176 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.19, I(M;suit)=0.44, I(M;suit|K)=0.44 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 3 | pad suit only | no | g=0.175 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.98, I(M;suit)=0.10, I(M;suit|K)=0.10 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 4 | pad suit only | no | g=0.169 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.93, I(M;suit)=0.19, I(M;suit|K)=0.19 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 5 | pad suit only | no | g=0.191 vs 0.750; suit leaks, rank in clear; I(M;X)=2.25, I(M;suit)=0.25, I(M;suit|K)=0.25 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 6 | pad suit only | no | g=0.139 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.77, I(M;suit)=0.29, I(M;suit|K)=0.29 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 7 | pad suit only | no | g=0.178 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.23, I(M;suit)=0.48, I(M;suit|K)=0.48 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 8 | pad suit only | no | g=0.211 vs 0.750; suit leaks, rank in clear; I(M;X)=2.25, I(M;suit)=0.34, I(M;suit|K)=0.50 |
| model_N2048 | suit4x4 | 4 | 4 | pub | 9 | pad suit only | no | g=0.159 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.85, I(M;suit)=0.22, I(M;suit|K)=0.22 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 0 | pad suit only | no | g=0.165 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.95, I(M;suit)=0.20, I(M;suit|K)=0.20 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 1 | pad suit only | no | g=0.129 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.55, I(M;suit)=0.22, I(M;suit|K)=0.22 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 2 | pad suit only | no | g=0.175 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.98, I(M;suit)=0.10, I(M;suit|K)=0.10 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 3 | pad suit only | no | g=0.159 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.85, I(M;suit)=0.22, I(M;suit|K)=0.22 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 4 | pad suit only | no | g=0.129 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.42, I(M;suit)=0.09, I(M;suit|K)=0.09 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 5 | pad suit only | no | g=0.152 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.75, I(M;suit)=0.25, I(M;suit|K)=0.25 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 6 | pad suit only | no | g=0.183 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.23, I(M;suit)=0.35, I(M;suit|K)=0.35 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 7 | pad suit only | no | g=0.176 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.15, I(M;suit)=0.40, I(M;suit|K)=0.40 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 8 | pad suit only | no | g=0.134 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.50, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| model_N2048 | suit4x4 | 4 | 2 | pub | 9 | pad suit only | no | g=0.134 vs 0.750; suit not sent, rank partly sent; I(M;X)=1.56, I(M;suit)=0.06, I(M;suit|K)=0.06 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 0 | reaches best known | no | g=0.147 vs 0.500; I(M;X)=1.75 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 1 | reaches best known | no | g=0.152 vs 0.500; I(M;X)=1.96 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 2 | reaches best known | no | g=0.160 vs 0.500; I(M;X)=1.92 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 3 | reaches best known | no | g=0.144 vs 0.500; I(M;X)=1.81 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 4 | reaches best known | no | g=0.194 vs 0.500; I(M;X)=2.28 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 5 | reaches best known | no | g=0.148 vs 0.500; I(M;X)=1.78 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 6 | reaches best known | no | g=0.173 vs 0.500; I(M;X)=1.98 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 7 | reaches best known | no | g=0.160 vs 0.500; I(M;X)=1.91 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 8 | reaches best known | no | g=0.142 vs 0.500; I(M;X)=1.75 |
| model_N2048 | suit4x4 | 4 | 1 | pub | 9 | reaches best known | no | g=0.184 vs 0.500; I(M;X)=2.22 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 0 | pad suit only | no | g=0.136 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.55, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 1 | pad suit only | no | g=0.172 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.98, I(M;suit)=0.10, I(M;suit|K)=0.10 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 2 | pad suit only | no | g=0.161 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.88, I(M;suit)=0.26, I(M;suit|K)=0.26 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 3 | pad suit only | no | g=0.091 vs 0.188; suit not sent, rank partly sent; I(M;X)=0.90, I(M;suit)=0.04, I(M;suit|K)=0.04 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 4 | pad suit only | no | g=0.135 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.56, I(M;suit)=0.06, I(M;suit|K)=0.06 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 5 | pad suit only | no | g=0.137 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.55, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 6 | pad suit only | no | g=0.135 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.50, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 7 | pad suit only | no | g=0.126 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.48, I(M;suit)=0.32, I(M;suit|K)=0.32 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 8 | pad suit only | no | g=0.158 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.88, I(M;suit)=0.26, I(M;suit|K)=0.26 |
| model_N2048 | suit4x4 | 2 | 2 | pub | 9 | pad suit only | no | g=0.126 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.48, I(M;suit)=0.15, I(M;suit|K)=0.15 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 0 | reaches best known | no | g=0.375 vs 0.750; I(M;X)=2.67 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 1 | reaches best known | no | g=0.375 vs 0.750; I(M;X)=2.81 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 2 | reaches best known | no | g=0.231 vs 0.750; I(M;X)=1.77 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 3 | reaches best known | no | g=0.250 vs 0.750; I(M;X)=2.20 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 4 | reaches best known | no | g=0.312 vs 0.750; I(M;X)=2.52 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 5 | reaches best known | no | g=0.312 vs 0.750; I(M;X)=2.44 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 6 | reaches best known | no | g=0.233 vs 0.750; I(M;X)=1.50 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 7 | reaches best known | no | g=0.312 vs 0.750; I(M;X)=2.53 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 8 | reaches best known | no | g=0.312 vs 0.750; I(M;X)=2.60 |
| model_N2048 | suit4x4 | 4 | 0 | priv | 9 | reaches best known | no | g=0.233 vs 0.750; I(M;X)=1.97 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 0 | key as pad | no | g=0.178 vs 0.938; I(M;X)=1.00 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 1 | key as pad | no | g=0.092 vs 0.938; I(M;X)=0.42 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 2 | key as pad | no | g=0.062 vs 0.938; I(M;X)=0.20 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 3 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 4 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 5 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 6 | key as pad | no | g=0.186 vs 0.938; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 7 | key as pad | no | g=0.125 vs 0.938; I(M;X)=0.79 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 8 | key as pad | no | g=0.187 vs 0.938; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 4 | pub | 9 | key as pad | no | g=0.091 vs 0.938; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 0 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 1 | reaches best known | no | g=0.186 vs 0.750; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 2 | reaches best known | no | g=0.060 vs 0.750; I(M;X)=0.01 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 3 | reaches best known | no | g=0.176 vs 0.750; I(M;X)=1.00 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 4 | reaches best known | no | g=0.125 vs 0.750; I(M;X)=0.02 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 5 | reaches best known | no | g=0.156 vs 0.750; I(M;X)=0.20 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 6 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 7 | reaches best known | no | g=0.094 vs 0.750; I(M;X)=0.20 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 8 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 2 | pub | 9 | reaches best known | no | g=0.077 vs 0.750; I(M;X)=1.10 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 0 | reaches best known | no | g=0.125 vs 0.500; I(M;X)=0.79 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 1 | reaches best known | no | g=0.177 vs 0.500; I(M;X)=1.02 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 2 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 3 | reaches best known | no | g=0.155 vs 0.500; I(M;X)=0.30 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 4 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 5 | reaches best known | no | g=0.156 vs 0.500; I(M;X)=0.85 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 6 | reaches best known | no | g=0.156 vs 0.500; I(M;X)=0.54 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 7 | reaches best known | no | g=0.180 vs 0.500; I(M;X)=1.04 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 8 | reaches best known | no | g=0.087 vs 0.500; I(M;X)=0.06 |
| model_N2048 | attack4x4 | 2 | 1 | pub | 9 | reaches best known | no | g=0.187 vs 0.500; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 0 | reaches best known | no | g=0.175 vs 0.250; I(M;X)=1.00 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 1 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 2 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 3 | reaches best known | no | g=0.176 vs 0.250; I(M;X)=1.01 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 4 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 5 | reaches best known | no | g=0.142 vs 0.250; I(M;X)=0.24 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 6 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 7 | reaches best known | no | g=0.125 vs 0.250; I(M;X)=1.62 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 8 | reaches best known | no | g=0.140 vs 0.250; I(M;X)=0.27 |
| model_N2048 | attack4x4 | 2 | 0 | pub | 9 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=0.00 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 0 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.47 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 1 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.97 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 2 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=2.95 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 3 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=1.81 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 4 | reaches best known | no | g=0.125 vs 0.938; I(M;X)=2.69 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 5 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=2.50 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 6 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=2.83 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 7 | reaches best known | no | g=0.125 vs 0.938; I(M;X)=2.49 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 8 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=1.81 |
| model_N2048 | attack4x4 | 2 | 0 | priv | 9 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.99 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 0 | key as pad | no | g=0.000 vs 0.234; I(M;X)=1.42 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 1 | key as pad | no | g=0.000 vs 0.234; I(M;X)=1.56 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 2 | key as pad | no | g=0.000 vs 0.234; I(M;X)=1.48 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 3 | key as pad | no | g=0.000 vs 0.234; I(M;X)=0.67 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 4 | key as pad | no | g=0.000 vs 0.234; I(M;X)=1.56 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 5 | key as pad | no | g=0.000 vs 0.234; I(M;X)=1.51 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 6 | key as pad | no | g=0.000 vs 0.234; I(M;X)=1.78 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 7 | key as pad | no | g=0.000 vs 0.234; I(M;X)=1.54 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 8 | key as pad | no | g=0.000 vs 0.234; I(M;X)=1.48 |
| reinforce_adv | blocker16 | 2 | 2 | pub | 9 | key as pad | no | g=0.000 vs 0.234; I(M;X)=1.64 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 0 | reaches best known | no | g=0.000 vs 0.219; I(M;X)=1.58 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 1 | reaches best known | no | g=0.000 vs 0.219; I(M;X)=1.41 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 2 | reaches best known | no | g=0.007 vs 0.219; I(M;X)=1.58 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 3 | reaches best known | no | g=0.000 vs 0.219; I(M;X)=1.49 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 4 | reaches best known | no | g=0.000 vs 0.219; I(M;X)=1.62 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 5 | reaches best known | no | g=0.000 vs 0.219; I(M;X)=0.91 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 6 | reaches best known | no | g=0.000 vs 0.219; I(M;X)=1.68 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 7 | reaches best known | no | g=0.000 vs 0.219; I(M;X)=0.34 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 8 | reaches best known | no | g=0.000 vs 0.219; I(M;X)=1.85 |
| reinforce_adv | blocker16 | 2 | 1 | pub | 9 | reaches best known | no | g=0.000 vs 0.219; I(M;X)=1.82 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 0 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=1.37 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 1 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=1.20 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 2 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=0.70 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 3 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=1.90 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 4 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=1.85 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 5 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=1.65 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 6 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=1.76 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 7 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=1.76 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 8 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=1.59 |
| reinforce_adv | blocker16 | 2 | 0 | pub | 9 | reaches best known | no | g=0.000 vs 0.188; I(M;X)=0.87 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 0 | key as pad | no | g=0.000 vs 0.938; I(M;X)=1.66 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 1 | key as pad | no | g=0.000 vs 0.938; I(M;X)=1.62 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 2 | key as pad | no | g=0.000 vs 0.938; I(M;X)=1.80 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 3 | key as pad | no | g=0.000 vs 0.938; I(M;X)=1.76 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 4 | key as pad | no | g=0.000 vs 0.938; I(M;X)=2.11 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 5 | key as pad | no | g=0.008 vs 0.938; I(M;X)=1.54 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 6 | key as pad | no | g=0.000 vs 0.938; I(M;X)=1.80 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 7 | key as pad | no | g=0.000 vs 0.938; I(M;X)=1.62 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 8 | key as pad | no | g=0.000 vs 0.938; I(M;X)=1.30 |
| reinforce_adv | blocker16 | 4 | 4 | pub | 9 | key as pad | no | g=0.017 vs 0.938; I(M;X)=1.71 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 0 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.89 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 1 | reaches best known | no | g=0.007 vs 0.750; I(M;X)=1.74 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 2 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=2.39 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 3 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.60 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 4 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.75 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 5 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.62 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 6 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=0.54 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 7 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.20 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 8 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.57 |
| reinforce_adv | blocker16 | 4 | 2 | pub | 9 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=2.17 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 0 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=0.67 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 1 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.47 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 2 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.62 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 3 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=2.01 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 4 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.91 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 5 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.76 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 6 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.92 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 7 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=2.45 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 8 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.67 |
| reinforce_adv | blocker16 | 4 | 1 | pub | 9 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=2.00 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 0 | reaches best known | no | g=0.002 vs 0.250; I(M;X)=2.65 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 1 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=2.22 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 2 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=2.60 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 3 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=1.81 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 4 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=1.66 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 5 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=1.95 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 6 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=1.67 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 7 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=2.02 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 8 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=1.50 |
| reinforce_adv | blocker16 | 4 | 0 | pub | 9 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=2.40 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=2.19 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 1 | reaches best known | no | g=0.250 vs 0.938; I(M;X)=2.01 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 2 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.15 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 3 | reaches best known | no | g=0.248 vs 0.938; I(M;X)=1.49 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 4 | reaches best known | no | g=0.188 vs 0.938; I(M;X)=1.31 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 5 | reaches best known | no | g=0.311 vs 0.938; I(M;X)=2.28 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 6 | reaches best known | no | g=0.188 vs 0.938; I(M;X)=2.04 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 7 | reaches best known | no | g=0.311 vs 0.938; I(M;X)=2.58 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 8 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=2.02 |
| reinforce_adv | blocker16 | 4 | 0 | priv | 9 | reaches best known | no | g=0.312 vs 0.938; I(M;X)=2.05 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 0 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.91, I(M;suit)=0.42, I(M;suit|K)=0.42 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 1 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=0.87, I(M;suit)=0.23, I(M;suit|K)=0.25 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 2 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=0.49, I(M;suit)=0.18, I(M;suit|K)=0.20 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 3 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.31, I(M;suit)=0.45, I(M;suit|K)=0.46 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 4 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.28, I(M;suit)=0.61, I(M;suit|K)=0.68 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 5 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.42, I(M;suit)=0.47, I(M;suit|K)=0.52 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 6 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.20, I(M;suit)=0.22, I(M;suit|K)=0.22 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 7 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.29, I(M;suit)=0.38, I(M;suit|K)=0.45 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 8 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.70, I(M;suit)=0.60, I(M;suit|K)=0.61 |
| reinforce_adv | suit4x4 | 4 | 4 | pub | 9 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.50, I(M;suit)=0.33, I(M;suit|K)=0.35 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 0 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.25, I(M;suit)=0.63, I(M;suit|K)=0.63 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 1 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.45, I(M;suit)=0.24, I(M;suit|K)=0.26 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 2 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.65, I(M;suit)=0.45, I(M;suit|K)=0.45 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 3 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.89, I(M;suit)=0.44, I(M;suit|K)=0.48 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 4 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.05, I(M;suit)=0.26, I(M;suit|K)=0.27 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 5 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=0.87, I(M;suit)=0.29, I(M;suit|K)=0.30 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 6 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=0.60, I(M;suit)=0.14, I(M;suit|K)=0.19 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 7 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.09, I(M;suit)=0.72, I(M;suit|K)=0.72 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 8 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.95, I(M;suit)=0.45, I(M;suit|K)=0.45 |
| reinforce_adv | suit4x4 | 4 | 2 | pub | 9 | pad suit only | no | g=0.000 vs 0.750; suit leaks, rank partly sent; I(M;X)=0.88, I(M;suit)=0.23, I(M;suit|K)=0.25 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 0 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.16 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 1 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.93 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 2 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.98 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 3 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=2.05 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 4 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.70 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 5 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=2.23 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 6 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.68 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 7 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=2.17 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 8 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.19 |
| reinforce_adv | suit4x4 | 4 | 1 | pub | 9 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.80 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 0 | pad suit only | no | g=0.000 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.58, I(M;suit)=0.43, I(M;suit|K)=0.43 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 1 | pad suit only | no | g=0.000 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.55, I(M;suit)=0.39, I(M;suit|K)=0.39 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 2 | pad suit only | no | g=0.000 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.49, I(M;suit)=0.34, I(M;suit|K)=0.34 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 3 | pad suit only | no | g=0.000 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.75, I(M;suit)=0.42, I(M;suit|K)=0.42 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 4 | pad suit only | no | g=0.000 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.32, I(M;suit)=0.20, I(M;suit|K)=0.21 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 5 | pad suit only | no | g=0.000 vs 0.188; suit leaks, rank partly sent; I(M;X)=0.64, I(M;suit)=0.29, I(M;suit|K)=0.32 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 6 | pad suit only | no | g=0.000 vs 0.188; suit leaks, rank partly sent; I(M;X)=0.62, I(M;suit)=0.16, I(M;suit|K)=0.16 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 7 | pad suit only | no | g=0.000 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.55, I(M;suit)=0.22, I(M;suit|K)=0.28 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 8 | pad suit only | no | g=0.000 vs 0.188; suit leaks, rank partly sent; I(M;X)=1.28, I(M;suit)=0.12, I(M;suit|K)=0.18 |
| reinforce_adv | suit4x4 | 2 | 2 | pub | 9 | pad suit only | no | g=0.000 vs 0.188; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 0 | reaches best known | no | g=0.125 vs 0.750; I(M;X)=1.99 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 1 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=1.77 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 2 | reaches best known | no | g=0.250 vs 0.750; I(M;X)=2.24 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 3 | reaches best known | no | g=0.250 vs 0.750; I(M;X)=1.62 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 4 | reaches best known | no | g=0.125 vs 0.750; I(M;X)=1.37 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 5 | reaches best known | no | g=0.250 vs 0.750; I(M;X)=2.18 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 6 | reaches best known | no | g=0.125 vs 0.750; I(M;X)=1.70 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 7 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=1.68 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 8 | reaches best known | no | g=0.187 vs 0.750; I(M;X)=1.50 |
| reinforce_adv | suit4x4 | 4 | 0 | priv | 9 | reaches best known | no | g=0.063 vs 0.750; I(M;X)=1.64 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 0 | key as pad | no | g=0.000 vs 0.938; I(M;X)=0.10 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 1 | key as pad | no | g=0.008 vs 0.938; I(M;X)=1.89 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 2 | key as pad | no | g=0.062 vs 0.938; I(M;X)=0.00 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 3 | key as pad | no | g=0.000 vs 0.938; I(M;X)=0.00 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 4 | key as pad | no | g=0.062 vs 0.938; I(M;X)=0.13 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 5 | key as pad | no | g=0.000 vs 0.938; I(M;X)=1.73 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 6 | key as pad | no | g=0.000 vs 0.938; I(M;X)=0.16 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 7 | key as pad | no | g=0.000 vs 0.938; I(M;X)=0.22 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 8 | key as pad | no | g=0.000 vs 0.938; I(M;X)=0.12 |
| reinforce_adv | attack4x4 | 2 | 4 | pub | 9 | key as pad | no | g=0.000 vs 0.938; I(M;X)=0.05 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 0 | reaches best known | no | g=0.062 vs 0.750; I(M;X)=0.36 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 1 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.31 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 2 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.25 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 3 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=2.41 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 4 | reaches best known | no | g=0.062 vs 0.750; I(M;X)=1.00 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 5 | reaches best known | no | g=0.062 vs 0.750; I(M;X)=1.59 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 6 | reaches best known | no | g=0.021 vs 0.750; I(M;X)=0.93 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 7 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=0.97 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 8 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.51 |
| reinforce_adv | attack4x4 | 2 | 2 | pub | 9 | reaches best known | no | g=0.000 vs 0.750; I(M;X)=1.74 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 0 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=0.32 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 1 | reaches best known | no | g=0.005 vs 0.500; I(M;X)=1.17 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 2 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=2.30 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 3 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.66 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 4 | reaches best known | no | g=0.003 vs 0.500; I(M;X)=2.89 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 5 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.98 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 6 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.47 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 7 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=2.96 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 8 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=1.82 |
| reinforce_adv | attack4x4 | 2 | 1 | pub | 9 | reaches best known | no | g=0.000 vs 0.500; I(M;X)=2.83 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 0 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=2.49 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 1 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=2.27 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 2 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=1.81 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 3 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=1.98 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 4 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=1.40 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 5 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=1.77 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 6 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=2.31 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 7 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=2.58 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 8 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=2.46 |
| reinforce_adv | attack4x4 | 2 | 0 | pub | 9 | reaches best known | no | g=0.000 vs 0.250; I(M;X)=0.91 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 0 | reaches best known | no | g=0.125 vs 0.938; I(M;X)=2.25 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 1 | reaches best known | no | g=0.062 vs 0.938; I(M;X)=1.79 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 2 | reaches best known | no | g=0.125 vs 0.938; I(M;X)=2.23 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 3 | reaches best known | no | g=0.125 vs 0.938; I(M;X)=2.95 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 4 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=2.47 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 5 | reaches best known | no | g=0.062 vs 0.938; I(M;X)=2.16 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 6 | reaches best known | no | g=0.125 vs 0.938; I(M;X)=2.67 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 7 | reaches best known | no | g=0.125 vs 0.938; I(M;X)=1.01 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 8 | reaches best known | no | g=0.187 vs 0.938; I(M;X)=3.46 |
| reinforce_adv | attack4x4 | 2 | 0 | priv | 9 | reaches best known | no | g=0.125 vs 0.938; I(M;X)=2.40 |
| tabular_br | blocker16 | 2 | 2 | pub | 0 | key as pad | no | g=0.193 vs 0.234; I(M;X)=1.16 |
| tabular_br | blocker16 | 2 | 2 | pub | 1 | key as pad | no | g=0.194 vs 0.234; I(M;X)=0.63 |
| tabular_br | blocker16 | 2 | 2 | pub | 2 | key as pad | no | g=0.216 vs 0.234; I(M;X)=0.17 |
| tabular_br | blocker16 | 2 | 2 | pub | 3 | key as pad | no | g=0.208 vs 0.234; I(M;X)=0.15 |
| tabular_br | blocker16 | 2 | 2 | pub | 4 | key as pad | no | g=0.217 vs 0.234; I(M;X)=0.22 |
| tabular_br | blocker16 | 2 | 2 | pub | 5 | key as pad | no | g=0.205 vs 0.234; I(M;X)=0.65 |
| tabular_br | blocker16 | 2 | 2 | pub | 6 | key as pad | no | g=0.198 vs 0.234; I(M;X)=0.71 |
| tabular_br | blocker16 | 2 | 2 | pub | 7 | key as pad | no | g=0.216 vs 0.234; I(M;X)=0.26 |
| tabular_br | blocker16 | 2 | 2 | pub | 8 | key as pad | no | g=0.216 vs 0.234; I(M;X)=0.11 |
| tabular_br | blocker16 | 2 | 2 | pub | 9 | key as pad | no | g=0.203 vs 0.234; I(M;X)=0.64 |
| tabular_br | blocker16 | 2 | 1 | pub | 0 | reaches best known | yes | g=0.208 vs 0.219; I(M;X)=0.98 |
| tabular_br | blocker16 | 2 | 1 | pub | 1 | reaches best known | yes | g=0.209 vs 0.219; I(M;X)=0.92 |
| tabular_br | blocker16 | 2 | 1 | pub | 2 | reaches best known | yes | g=0.208 vs 0.219; I(M;X)=0.84 |
| tabular_br | blocker16 | 2 | 1 | pub | 3 | reaches best known | yes | g=0.205 vs 0.219; I(M;X)=0.91 |
| tabular_br | blocker16 | 2 | 1 | pub | 4 | reaches best known | yes | g=0.203 vs 0.219; I(M;X)=0.83 |
| tabular_br | blocker16 | 2 | 1 | pub | 5 | reaches best known | yes | g=0.208 vs 0.219; I(M;X)=0.91 |
| tabular_br | blocker16 | 2 | 1 | pub | 6 | reaches best known | yes | g=0.206 vs 0.219; I(M;X)=0.87 |
| tabular_br | blocker16 | 2 | 1 | pub | 7 | reaches best known | no | g=0.158 vs 0.219; I(M;X)=1.70 |
| tabular_br | blocker16 | 2 | 1 | pub | 8 | reaches best known | yes | g=0.206 vs 0.219; I(M;X)=0.86 |
| tabular_br | blocker16 | 2 | 1 | pub | 9 | reaches best known | yes | g=0.202 vs 0.219; I(M;X)=0.86 |
| tabular_br | blocker16 | 2 | 0 | pub | 0 | reaches best known | yes | g=0.183 vs 0.188; I(M;X)=1.99 |
| tabular_br | blocker16 | 2 | 0 | pub | 1 | reaches best known | yes | g=0.170 vs 0.188; I(M;X)=1.87 |
| tabular_br | blocker16 | 2 | 0 | pub | 2 | reaches best known | no | g=0.146 vs 0.188; I(M;X)=1.54 |
| tabular_br | blocker16 | 2 | 0 | pub | 3 | reaches best known | yes | g=0.171 vs 0.188; I(M;X)=1.87 |
| tabular_br | blocker16 | 2 | 0 | pub | 4 | reaches best known | no | g=0.149 vs 0.188; I(M;X)=1.57 |
| tabular_br | blocker16 | 2 | 0 | pub | 5 | reaches best known | no | g=0.149 vs 0.188; I(M;X)=1.57 |
| tabular_br | blocker16 | 2 | 0 | pub | 6 | reaches best known | yes | g=0.173 vs 0.188; I(M;X)=1.91 |
| tabular_br | blocker16 | 2 | 0 | pub | 7 | reaches best known | no | g=0.147 vs 0.188; I(M;X)=1.55 |
| tabular_br | blocker16 | 2 | 0 | pub | 8 | reaches best known | yes | g=0.180 vs 0.188; I(M;X)=1.97 |
| tabular_br | blocker16 | 2 | 0 | pub | 9 | reaches best known | yes | g=0.178 vs 0.188; I(M;X)=1.94 |
| tabular_br | blocker16 | 4 | 4 | pub | 0 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 4 | pub | 1 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 4 | pub | 2 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 4 | pub | 3 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 4 | pub | 4 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 4 | pub | 5 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 4 | pub | 6 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 4 | pub | 7 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 4 | pub | 8 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 4 | pub | 9 | key as pad | no | g=0.059 vs 0.938; I(M;X)=0.00 |
| tabular_br | blocker16 | 4 | 2 | pub | 0 | reaches best known | no | g=0.064 vs 0.750; I(M;X)=0.04 |
| tabular_br | blocker16 | 4 | 2 | pub | 1 | reaches best known | no | g=0.188 vs 0.750; I(M;X)=0.72 |
| tabular_br | blocker16 | 4 | 2 | pub | 2 | reaches best known | no | g=0.059 vs 0.750; I(M;X)=0.02 |
| tabular_br | blocker16 | 4 | 2 | pub | 3 | reaches best known | no | g=0.246 vs 0.750; I(M;X)=0.72 |
| tabular_br | blocker16 | 4 | 2 | pub | 4 | reaches best known | no | g=0.061 vs 0.750; I(M;X)=0.03 |
| tabular_br | blocker16 | 4 | 2 | pub | 5 | reaches best known | no | g=0.061 vs 0.750; I(M;X)=0.02 |
| tabular_br | blocker16 | 4 | 2 | pub | 6 | reaches best known | no | g=0.335 vs 0.750; I(M;X)=1.04 |
| tabular_br | blocker16 | 4 | 2 | pub | 7 | reaches best known | no | g=0.064 vs 0.750; I(M;X)=0.03 |
| tabular_br | blocker16 | 4 | 2 | pub | 8 | reaches best known | no | g=0.060 vs 0.750; I(M;X)=0.01 |
| tabular_br | blocker16 | 4 | 2 | pub | 9 | reaches best known | no | g=0.059 vs 0.750; I(M;X)=0.01 |
| tabular_br | blocker16 | 4 | 1 | pub | 0 | reaches best known | no | g=0.115 vs 0.500; I(M;X)=1.03 |
| tabular_br | blocker16 | 4 | 1 | pub | 1 | reaches best known | no | g=0.369 vs 0.500; I(M;X)=2.12 |
| tabular_br | blocker16 | 4 | 1 | pub | 2 | reaches best known | no | g=0.196 vs 0.500; I(M;X)=2.17 |
| tabular_br | blocker16 | 4 | 1 | pub | 3 | reaches best known | no | g=0.373 vs 0.500; I(M;X)=2.15 |
| tabular_br | blocker16 | 4 | 1 | pub | 4 | reaches best known | no | g=0.338 vs 0.500; I(M;X)=1.95 |
| tabular_br | blocker16 | 4 | 1 | pub | 5 | reaches best known | no | g=0.201 vs 0.500; I(M;X)=2.24 |
| tabular_br | blocker16 | 4 | 1 | pub | 6 | reaches best known | no | g=0.190 vs 0.500; I(M;X)=2.10 |
| tabular_br | blocker16 | 4 | 1 | pub | 7 | reaches best known | no | g=0.337 vs 0.500; I(M;X)=1.95 |
| tabular_br | blocker16 | 4 | 1 | pub | 8 | reaches best known | no | g=0.342 vs 0.500; I(M;X)=1.94 |
| tabular_br | blocker16 | 4 | 1 | pub | 9 | reaches best known | no | g=0.360 vs 0.500; I(M;X)=2.04 |
| tabular_br | blocker16 | 4 | 0 | pub | 0 | reaches best known | no | g=0.194 vs 0.250; I(M;X)=2.22 |
| tabular_br | blocker16 | 4 | 0 | pub | 1 | reaches best known | no | g=0.167 vs 0.250; I(M;X)=1.84 |
| tabular_br | blocker16 | 4 | 0 | pub | 2 | reaches best known | no | g=0.198 vs 0.250; I(M;X)=2.25 |
| tabular_br | blocker16 | 4 | 0 | pub | 3 | reaches best known | no | g=0.198 vs 0.250; I(M;X)=2.22 |
| tabular_br | blocker16 | 4 | 0 | pub | 4 | reaches best known | no | g=0.179 vs 0.250; I(M;X)=1.99 |
| tabular_br | blocker16 | 4 | 0 | pub | 5 | reaches best known | no | g=0.189 vs 0.250; I(M;X)=2.11 |
| tabular_br | blocker16 | 4 | 0 | pub | 6 | reaches best known | no | g=0.201 vs 0.250; I(M;X)=2.27 |
| tabular_br | blocker16 | 4 | 0 | pub | 7 | reaches best known | no | g=0.184 vs 0.250; I(M;X)=1.99 |
| tabular_br | blocker16 | 4 | 0 | pub | 8 | reaches best known | no | g=0.183 vs 0.250; I(M;X)=1.99 |
| tabular_br | blocker16 | 4 | 0 | pub | 9 | reaches best known | no | g=0.176 vs 0.250; I(M;X)=1.97 |
| tabular_br | blocker16 | 4 | 0 | priv | 0 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | blocker16 | 4 | 0 | priv | 1 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | blocker16 | 4 | 0 | priv | 2 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | blocker16 | 4 | 0 | priv | 3 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | blocker16 | 4 | 0 | priv | 4 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | blocker16 | 4 | 0 | priv | 5 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | blocker16 | 4 | 0 | priv | 6 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | blocker16 | 4 | 0 | priv | 7 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | blocker16 | 4 | 0 | priv | 8 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | blocker16 | 4 | 0 | priv | 9 | reaches best known | no | g=0.875 vs 0.938; I(M;X)=3.87 |
| tabular_br | suit4x4 | 4 | 4 | pub | 0 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 4 | pub | 1 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 4 | pub | 2 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 4 | pub | 3 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 4 | pub | 4 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 4 | pub | 5 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 4 | pub | 6 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 4 | pub | 7 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 4 | pub | 8 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 4 | pub | 9 | pad suit only | no | g=0.047 vs 0.750; suit not sent, no rank; I(M;X)=0.00, I(M;suit)=0.00, I(M;suit|K)=0.00 |
| tabular_br | suit4x4 | 4 | 2 | pub | 0 | pad suit only | no | g=0.126 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.24, I(M;suit)=0.10, I(M;suit|K)=0.10 |
| tabular_br | suit4x4 | 4 | 2 | pub | 1 | pad suit only | no | g=0.210 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.21, I(M;suit)=0.15, I(M;suit|K)=0.54 |
| tabular_br | suit4x4 | 4 | 2 | pub | 2 | pad suit only | no | g=0.095 vs 0.750; suit not sent, rank partly sent; I(M;X)=0.74, I(M;suit)=0.06, I(M;suit|K)=0.06 |
| tabular_br | suit4x4 | 4 | 2 | pub | 3 | pad suit only | no | g=0.145 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.17, I(M;suit)=0.14, I(M;suit|K)=0.20 |
| tabular_br | suit4x4 | 4 | 2 | pub | 4 | pad suit only | no | g=0.136 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.37, I(M;suit)=0.11, I(M;suit|K)=0.11 |
| tabular_br | suit4x4 | 4 | 2 | pub | 5 | pad suit only | no | g=0.093 vs 0.750; suit not sent, rank partly sent; I(M;X)=0.47, I(M;suit)=0.01, I(M;suit|K)=0.06 |
| tabular_br | suit4x4 | 4 | 2 | pub | 6 | pad suit only | no | g=0.179 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.08, I(M;suit)=0.11, I(M;suit|K)=0.38 |
| tabular_br | suit4x4 | 4 | 2 | pub | 7 | pad suit only | no | g=0.100 vs 0.750; suit not sent, rank partly sent; I(M;X)=0.78, I(M;suit)=0.09, I(M;suit|K)=0.09 |
| tabular_br | suit4x4 | 4 | 2 | pub | 8 | pad suit only | no | g=0.344 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.48, I(M;suit)=0.16, I(M;suit|K)=0.92 |
| tabular_br | suit4x4 | 4 | 2 | pub | 9 | pad suit only | no | g=0.086 vs 0.750; suit not sent, rank partly sent; I(M;X)=0.63, I(M;suit)=0.05, I(M;suit|K)=0.05 |
| tabular_br | suit4x4 | 4 | 1 | pub | 0 | reaches best known | no | g=0.216 vs 0.500; I(M;X)=2.49 |
| tabular_br | suit4x4 | 4 | 1 | pub | 1 | reaches best known | no | g=0.215 vs 0.500; I(M;X)=2.47 |
| tabular_br | suit4x4 | 4 | 1 | pub | 2 | reaches best known | no | g=0.207 vs 0.500; I(M;X)=2.33 |
| tabular_br | suit4x4 | 4 | 1 | pub | 3 | reaches best known | no | g=0.205 vs 0.500; I(M;X)=2.27 |
| tabular_br | suit4x4 | 4 | 1 | pub | 4 | reaches best known | no | g=0.205 vs 0.500; I(M;X)=2.39 |
| tabular_br | suit4x4 | 4 | 1 | pub | 5 | reaches best known | no | g=0.220 vs 0.500; I(M;X)=2.53 |
| tabular_br | suit4x4 | 4 | 1 | pub | 6 | reaches best known | no | g=0.303 vs 0.500; I(M;X)=2.23 |
| tabular_br | suit4x4 | 4 | 1 | pub | 7 | reaches best known | no | g=0.265 vs 0.500; I(M;X)=2.09 |
| tabular_br | suit4x4 | 4 | 1 | pub | 8 | reaches best known | no | g=0.208 vs 0.500; I(M;X)=2.37 |
| tabular_br | suit4x4 | 4 | 1 | pub | 9 | reaches best known | no | g=0.387 vs 0.500; I(M;X)=2.36 |
| tabular_br | suit4x4 | 2 | 2 | pub | 0 | pad suit only | no | g=0.182 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.70, I(M;suit)=0.02, I(M;suit|K)=0.21 |
| tabular_br | suit4x4 | 2 | 2 | pub | 1 | pad suit only | no | g=0.177 vs 0.188; suit not sent, rank partly sent; I(M;X)=1.84, I(M;suit)=0.04, I(M;suit|K)=0.04 |
| tabular_br | suit4x4 | 2 | 2 | pub | 2 | pad suit only | no | g=0.180 vs 0.188; suit partly padded, rank partly sent; I(M;X)=1.29, I(M;suit)=0.04, I(M;suit|K)=0.14 |
| tabular_br | suit4x4 | 2 | 2 | pub | 3 | pad suit only | no | g=0.180 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.83, I(M;suit)=0.03, I(M;suit|K)=0.13 |
| tabular_br | suit4x4 | 2 | 2 | pub | 4 | pad suit only | no | g=0.177 vs 0.188; suit partly padded, rank partly sent; I(M;X)=1.23, I(M;suit)=0.07, I(M;suit|K)=0.13 |
| tabular_br | suit4x4 | 2 | 2 | pub | 5 | pad suit only | no | g=0.179 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.79, I(M;suit)=0.02, I(M;suit|K)=0.15 |
| tabular_br | suit4x4 | 2 | 2 | pub | 6 | pad suit only | no | g=0.185 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.76, I(M;suit)=0.05, I(M;suit|K)=0.22 |
| tabular_br | suit4x4 | 2 | 2 | pub | 7 | pad suit only | no | g=0.185 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.75, I(M;suit)=0.06, I(M;suit|K)=0.21 |
| tabular_br | suit4x4 | 2 | 2 | pub | 8 | pad suit only | no | g=0.182 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.76, I(M;suit)=0.04, I(M;suit|K)=0.21 |
| tabular_br | suit4x4 | 2 | 2 | pub | 9 | pad suit only | no | g=0.176 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.69, I(M;suit)=0.03, I(M;suit|K)=0.15 |
| tabular_br | suit4x4 | 4 | 0 | priv | 0 | reaches best known | yes | g=0.749 vs 0.750; I(M;X)=3.99 |
| tabular_br | suit4x4 | 4 | 0 | priv | 1 | reaches best known | yes | g=0.749 vs 0.750; I(M;X)=3.99 |
| tabular_br | suit4x4 | 4 | 0 | priv | 2 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=3.99 |
| tabular_br | suit4x4 | 4 | 0 | priv | 3 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=3.99 |
| tabular_br | suit4x4 | 4 | 0 | priv | 4 | reaches best known | no | g=0.687 vs 0.750; I(M;X)=3.86 |
| tabular_br | suit4x4 | 4 | 0 | priv | 5 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=3.99 |
| tabular_br | suit4x4 | 4 | 0 | priv | 6 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=3.99 |
| tabular_br | suit4x4 | 4 | 0 | priv | 7 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=3.99 |
| tabular_br | suit4x4 | 4 | 0 | priv | 8 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=3.99 |
| tabular_br | suit4x4 | 4 | 0 | priv | 9 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=3.99 |
| tabular_br | attack4x4 | 2 | 4 | pub | 0 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 4 | pub | 1 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 4 | pub | 2 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 4 | pub | 3 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 4 | pub | 4 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 4 | pub | 5 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 4 | pub | 6 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 4 | pub | 7 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 4 | pub | 8 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 4 | pub | 9 | key as pad | no | g=0.004 vs 0.938; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 2 | pub | 0 | reaches best known | no | g=0.150 vs 0.750; I(M;X)=0.64 |
| tabular_br | attack4x4 | 2 | 2 | pub | 1 | reaches best known | no | g=0.080 vs 0.750; I(M;X)=0.29 |
| tabular_br | attack4x4 | 2 | 2 | pub | 2 | reaches best known | no | g=0.058 vs 0.750; I(M;X)=0.34 |
| tabular_br | attack4x4 | 2 | 2 | pub | 3 | reaches best known | no | g=0.203 vs 0.750; I(M;X)=0.88 |
| tabular_br | attack4x4 | 2 | 2 | pub | 4 | reaches best known | no | g=0.064 vs 0.750; I(M;X)=0.34 |
| tabular_br | attack4x4 | 2 | 2 | pub | 5 | reaches best known | no | g=0.048 vs 0.750; I(M;X)=0.11 |
| tabular_br | attack4x4 | 2 | 2 | pub | 6 | reaches best known | no | g=0.035 vs 0.750; I(M;X)=0.22 |
| tabular_br | attack4x4 | 2 | 2 | pub | 7 | reaches best known | no | g=0.013 vs 0.750; I(M;X)=0.12 |
| tabular_br | attack4x4 | 2 | 2 | pub | 8 | reaches best known | no | g=0.071 vs 0.750; I(M;X)=0.47 |
| tabular_br | attack4x4 | 2 | 2 | pub | 9 | reaches best known | no | g=0.159 vs 0.750; I(M;X)=0.64 |
| tabular_br | attack4x4 | 2 | 1 | pub | 0 | reaches best known | no | g=0.211 vs 0.500; I(M;X)=1.66 |
| tabular_br | attack4x4 | 2 | 1 | pub | 1 | reaches best known | no | g=0.253 vs 0.500; I(M;X)=1.30 |
| tabular_br | attack4x4 | 2 | 1 | pub | 2 | reaches best known | no | g=0.342 vs 0.500; I(M;X)=2.11 |
| tabular_br | attack4x4 | 2 | 1 | pub | 3 | reaches best known | no | g=0.280 vs 0.500; I(M;X)=0.96 |
| tabular_br | attack4x4 | 2 | 1 | pub | 4 | reaches best known | no | g=0.341 vs 0.500; I(M;X)=1.55 |
| tabular_br | attack4x4 | 2 | 1 | pub | 5 | reaches best known | no | g=0.324 vs 0.500; I(M;X)=1.88 |
| tabular_br | attack4x4 | 2 | 1 | pub | 6 | reaches best known | no | g=0.227 vs 0.500; I(M;X)=1.41 |
| tabular_br | attack4x4 | 2 | 1 | pub | 7 | reaches best known | no | g=0.341 vs 0.500; I(M;X)=1.55 |
| tabular_br | attack4x4 | 2 | 1 | pub | 8 | reaches best known | no | g=0.229 vs 0.500; I(M;X)=1.42 |
| tabular_br | attack4x4 | 2 | 1 | pub | 9 | reaches best known | no | g=0.292 vs 0.500; I(M;X)=1.50 |
| tabular_br | attack4x4 | 2 | 0 | pub | 0 | reaches best known | no | g=0.181 vs 0.250; I(M;X)=1.00 |
| tabular_br | attack4x4 | 2 | 0 | pub | 1 | reaches best known | no | g=0.145 vs 0.250; I(M;X)=0.27 |
| tabular_br | attack4x4 | 2 | 0 | pub | 2 | reaches best known | no | g=0.202 vs 0.250; I(M;X)=1.62 |
| tabular_br | attack4x4 | 2 | 0 | pub | 3 | reaches best known | no | g=0.171 vs 0.250; I(M;X)=0.81 |
| tabular_br | attack4x4 | 2 | 0 | pub | 4 | reaches best known | no | g=0.183 vs 0.250; I(M;X)=1.81 |
| tabular_br | attack4x4 | 2 | 0 | pub | 5 | reaches best known | no | g=0.183 vs 0.250; I(M;X)=1.81 |
| tabular_br | attack4x4 | 2 | 0 | pub | 6 | reaches best known | no | g=0.176 vs 0.250; I(M;X)=0.84 |
| tabular_br | attack4x4 | 2 | 0 | pub | 7 | reaches best known | no | g=0.125 vs 0.250; I(M;X)=0.00 |
| tabular_br | attack4x4 | 2 | 0 | pub | 8 | reaches best known | no | g=0.169 vs 0.250; I(M;X)=0.81 |
| tabular_br | attack4x4 | 2 | 0 | pub | 9 | reaches best known | no | g=0.182 vs 0.250; I(M;X)=1.80 |
| tabular_br | attack4x4 | 2 | 0 | priv | 0 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | attack4x4 | 2 | 0 | priv | 1 | reaches best known | no | g=0.562 vs 0.938; I(M;X)=3.00 |
| tabular_br | attack4x4 | 2 | 0 | priv | 2 | reaches best known | no | g=0.687 vs 0.938; I(M;X)=3.49 |
| tabular_br | attack4x4 | 2 | 0 | priv | 3 | reaches best known | no | g=0.562 vs 0.938; I(M;X)=3.00 |
| tabular_br | attack4x4 | 2 | 0 | priv | 4 | reaches best known | no | g=0.562 vs 0.938; I(M;X)=3.00 |
| tabular_br | attack4x4 | 2 | 0 | priv | 5 | reaches best known | no | g=0.687 vs 0.938; I(M;X)=3.50 |
| tabular_br | attack4x4 | 2 | 0 | priv | 6 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | attack4x4 | 2 | 0 | priv | 7 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_br | attack4x4 | 2 | 0 | priv | 8 | reaches best known | no | g=0.562 vs 0.938; I(M;X)=3.00 |
| tabular_br | attack4x4 | 2 | 0 | priv | 9 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=2.50 |

wall time 3631 s for 720 runs
