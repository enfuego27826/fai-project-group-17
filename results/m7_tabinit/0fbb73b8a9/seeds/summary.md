| method | game | k | s | ρ | target | label | g(π_T) mean ± 95% CI | gap to lower | I(M;X) | I(M;c(X)) | I(M;c(X)\|K) | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 0.2344 | exact (code + solver V(k,inf,priv)) | 0.199 ± 0.005 | 0.036 | 0.49 | 0.49 | 1.33 | key as pad | 0 / 10 | 3s |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | [0.2188, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.192 ± 0.005 | 0.027 | 0.83 | 0.83 | 1.54 | reaches best known | 1 / 10 | 3s |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | [0.1875, 0.2344] | bound (upper: solver V(k,inf,priv)) | 0.170 ± 0.004 | 0.017 | 1.82 | 1.82 | 1.82 | reaches best known | 6 / 10 | 3s |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.538 ± 0.030 | 0.400 | 0.94 | 0.94 | 2.81 | key as pad | 0 / 10 | 19s |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.536 ± 0.074 | 0.214 | 2.05 | 2.05 | 3.48 | reaches best known | 0 / 10 | 7s |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.379 ± 0.017 | 0.121 | 2.36 | 2.36 | 3.21 | reaches best known | 0 / 10 | 5s |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.220 ± 0.005 | 0.030 | 2.70 | 2.70 | 2.70 | reaches best known | 0 / 10 | 4s |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.906 ± 0.024 | 0.032 | 3.92 | 3.92 | 3.92 | reaches best known | 5 / 10 | 4s |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 0.7500 | exact (code + uniform block) | 0.408 ± 0.020 | 0.342 | 0.96 | 0.10 | 0.98 | pad suit only | 0 / 10 | 19s |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 0.7500 | exact (code + uniform block) | 0.521 ± 0.060 | 0.229 | 2.17 | 0.36 | 1.52 | pad suit only | 0 / 10 | 7s |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | [0.5000, 0.7500] | bound (upper: uniform block) | 0.394 ± 0.017 | 0.106 | 2.62 | 0.65 | 1.41 | reaches best known | 0 / 10 | 5s |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 0.1875 | exact (code + solver V(k,inf,priv)) | 0.182 ± 0.005 | 0.005 | 0.51 | 0.04 | 0.23 | pad suit only | 0 / 10 | 3s |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 0.7500 | exact (code + uniform block) | 0.702 ± 0.025 | 0.048 | 3.89 | 1.89 | 1.89 | reaches best known | 3 / 10 | 4s |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 0.9375 | exact (code + uniform block) | 0.182 ± 0.013 | 0.755 | 0.36 | 0.36 | 2.15 | key as pad | 0 / 10 | 6s |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 0.7500 | exact (code + Lemma 1) | 0.300 ± 0.024 | 0.450 | 1.54 | 1.54 | 2.59 | reaches best known | 0 / 10 | 4s |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 0.5000 | exact (code + Lemma 1) | 0.236 ± 0.033 | 0.264 | 1.71 | 1.71 | 2.28 | reaches best known | 0 / 10 | 4s |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 0.2500 | exact (code + Lemma 1) | 0.177 ± 0.025 | 0.073 | 1.61 | 1.61 | 1.61 | reaches best known | 1 / 10 | 4s |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 0.9375 | exact (code + uniform block) | 0.500 ± 0.073 | 0.438 | 2.94 | 2.94 | 2.94 | reaches best known | 0 / 10 | 3s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 0 | key as pad | no | g=0.198 vs 0.234; I(M;X)=0.79 |
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 1 | key as pad | no | g=0.198 vs 0.234; I(M;X)=0.81 |
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 2 | key as pad | no | g=0.187 vs 0.234; I(M;X)=0.19 |
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 3 | key as pad | no | g=0.209 vs 0.234; I(M;X)=0.37 |
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 4 | key as pad | no | g=0.195 vs 0.234; I(M;X)=0.37 |
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 5 | key as pad | no | g=0.202 vs 0.234; I(M;X)=0.29 |
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 6 | key as pad | no | g=0.198 vs 0.234; I(M;X)=0.26 |
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 7 | key as pad | no | g=0.207 vs 0.234; I(M;X)=0.30 |
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 8 | key as pad | no | g=0.192 vs 0.234; I(M;X)=0.72 |
| tabular_sigma1 | blocker16 | 2 | 2 | pub | 9 | key as pad | no | g=0.200 vs 0.234; I(M;X)=0.77 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 0 | reaches best known | no | g=0.180 vs 0.219; I(M;X)=0.68 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 1 | reaches best known | no | g=0.195 vs 0.219; I(M;X)=0.88 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 2 | reaches best known | no | g=0.190 vs 0.219; I(M;X)=0.77 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 3 | reaches best known | no | g=0.192 vs 0.219; I(M;X)=0.95 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 4 | reaches best known | no | g=0.196 vs 0.219; I(M;X)=0.87 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 5 | reaches best known | yes | g=0.199 vs 0.219; I(M;X)=0.88 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 6 | reaches best known | no | g=0.180 vs 0.219; I(M;X)=0.64 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 7 | reaches best known | no | g=0.196 vs 0.219; I(M;X)=0.87 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 8 | reaches best known | no | g=0.195 vs 0.219; I(M;X)=0.91 |
| tabular_sigma1 | blocker16 | 2 | 1 | pub | 9 | reaches best known | no | g=0.195 vs 0.219; I(M;X)=0.85 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 0 | reaches best known | yes | g=0.168 vs 0.188; I(M;X)=1.77 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 1 | reaches best known | yes | g=0.174 vs 0.188; I(M;X)=1.92 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 2 | reaches best known | no | g=0.161 vs 0.188; I(M;X)=1.74 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 3 | reaches best known | yes | g=0.177 vs 0.188; I(M;X)=1.96 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 4 | reaches best known | no | g=0.165 vs 0.188; I(M;X)=1.70 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 5 | reaches best known | yes | g=0.177 vs 0.188; I(M;X)=1.88 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 6 | reaches best known | no | g=0.166 vs 0.188; I(M;X)=1.67 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 7 | reaches best known | yes | g=0.174 vs 0.188; I(M;X)=1.87 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 8 | reaches best known | no | g=0.165 vs 0.188; I(M;X)=1.79 |
| tabular_sigma1 | blocker16 | 2 | 0 | pub | 9 | reaches best known | yes | g=0.177 vs 0.188; I(M;X)=1.92 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 0 | key as pad | no | g=0.553 vs 0.938; I(M;X)=0.98 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 1 | key as pad | no | g=0.474 vs 0.938; I(M;X)=1.00 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 2 | key as pad | no | g=0.565 vs 0.938; I(M;X)=0.96 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 3 | key as pad | no | g=0.588 vs 0.938; I(M;X)=0.87 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 4 | key as pad | no | g=0.573 vs 0.938; I(M;X)=1.11 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 5 | key as pad | no | g=0.483 vs 0.938; I(M;X)=1.04 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 6 | key as pad | no | g=0.580 vs 0.938; I(M;X)=0.54 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 7 | key as pad | no | g=0.543 vs 0.938; I(M;X)=1.14 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 8 | key as pad | no | g=0.498 vs 0.938; I(M;X)=1.04 |
| tabular_sigma1 | blocker16 | 4 | 4 | pub | 9 | key as pad | no | g=0.520 vs 0.938; I(M;X)=0.68 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 0 | reaches best known | no | g=0.395 vs 0.750; I(M;X)=2.08 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 1 | reaches best known | no | g=0.430 vs 0.750; I(M;X)=2.36 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 2 | reaches best known | no | g=0.608 vs 0.750; I(M;X)=1.90 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 3 | reaches best known | no | g=0.623 vs 0.750; I(M;X)=1.95 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 4 | reaches best known | no | g=0.654 vs 0.750; I(M;X)=1.79 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 5 | reaches best known | no | g=0.646 vs 0.750; I(M;X)=1.90 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 6 | reaches best known | no | g=0.467 vs 0.750; I(M;X)=2.34 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 7 | reaches best known | no | g=0.463 vs 0.750; I(M;X)=2.23 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 8 | reaches best known | no | g=0.623 vs 0.750; I(M;X)=1.75 |
| tabular_sigma1 | blocker16 | 4 | 2 | pub | 9 | reaches best known | no | g=0.447 vs 0.750; I(M;X)=2.23 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 0 | reaches best known | no | g=0.355 vs 0.500; I(M;X)=2.16 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 1 | reaches best known | no | g=0.380 vs 0.500; I(M;X)=2.39 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 2 | reaches best known | no | g=0.396 vs 0.500; I(M;X)=2.51 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 3 | reaches best known | no | g=0.361 vs 0.500; I(M;X)=2.18 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 4 | reaches best known | no | g=0.437 vs 0.500; I(M;X)=2.63 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 5 | reaches best known | no | g=0.372 vs 0.500; I(M;X)=2.26 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 6 | reaches best known | no | g=0.361 vs 0.500; I(M;X)=2.28 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 7 | reaches best known | no | g=0.369 vs 0.500; I(M;X)=2.36 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 8 | reaches best known | no | g=0.366 vs 0.500; I(M;X)=2.35 |
| tabular_sigma1 | blocker16 | 4 | 1 | pub | 9 | reaches best known | no | g=0.390 vs 0.500; I(M;X)=2.50 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 0 | reaches best known | no | g=0.225 vs 0.250; I(M;X)=2.90 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 1 | reaches best known | no | g=0.225 vs 0.250; I(M;X)=2.77 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 2 | reaches best known | no | g=0.207 vs 0.250; I(M;X)=2.50 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 3 | reaches best known | no | g=0.217 vs 0.250; I(M;X)=2.68 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 4 | reaches best known | no | g=0.228 vs 0.250; I(M;X)=2.77 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 5 | reaches best known | no | g=0.222 vs 0.250; I(M;X)=2.68 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 6 | reaches best known | no | g=0.224 vs 0.250; I(M;X)=2.77 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 7 | reaches best known | no | g=0.220 vs 0.250; I(M;X)=2.68 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 8 | reaches best known | no | g=0.223 vs 0.250; I(M;X)=2.77 |
| tabular_sigma1 | blocker16 | 4 | 0 | pub | 9 | reaches best known | no | g=0.210 vs 0.250; I(M;X)=2.43 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 0 | reaches best known | no | g=0.875 vs 0.938; I(M;X)=3.86 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 1 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 2 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 3 | reaches best known | no | g=0.875 vs 0.938; I(M;X)=3.84 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 4 | reaches best known | no | g=0.875 vs 0.938; I(M;X)=3.82 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 5 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 6 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 7 | reaches best known | no | g=0.875 vs 0.938; I(M;X)=3.86 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 8 | reaches best known | no | g=0.874 vs 0.938; I(M;X)=3.87 |
| tabular_sigma1 | blocker16 | 4 | 0 | priv | 9 | reaches best known | yes | g=0.937 vs 0.938; I(M;X)=4.00 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 0 | pad suit only | no | g=0.405 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.14, I(M;suit)=0.15, I(M;suit|K)=1.01 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 1 | pad suit only | no | g=0.373 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.05, I(M;suit)=0.12, I(M;suit|K)=0.92 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 2 | pad suit only | no | g=0.426 vs 0.750; suit partly padded, rank partly sent; I(M;X)=0.98, I(M;suit)=0.10, I(M;suit|K)=1.06 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 3 | pad suit only | no | g=0.447 vs 0.750; suit leaks, rank partly sent; I(M;X)=0.98, I(M;suit)=0.11, I(M;suit|K)=1.08 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 4 | pad suit only | no | g=0.419 vs 0.750; suit partly padded, rank partly sent; I(M;X)=0.84, I(M;suit)=0.08, I(M;suit|K)=0.96 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 5 | pad suit only | no | g=0.405 vs 0.750; suit partly padded, rank partly sent; I(M;X)=0.68, I(M;suit)=0.04, I(M;suit|K)=0.93 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 6 | pad suit only | no | g=0.389 vs 0.750; suit partly padded, rank partly sent; I(M;X)=0.94, I(M;suit)=0.10, I(M;suit|K)=0.93 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 7 | pad suit only | no | g=0.409 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.22, I(M;suit)=0.16, I(M;suit|K)=1.02 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 8 | pad suit only | no | g=0.363 vs 0.750; suit leaks, rank partly sent; I(M;X)=0.97, I(M;suit)=0.10, I(M;suit|K)=0.85 |
| tabular_sigma1 | suit4x4 | 4 | 4 | pub | 9 | pad suit only | no | g=0.444 vs 0.750; suit partly padded, rank partly sent; I(M;X)=0.76, I(M;suit)=0.06, I(M;suit|K)=1.04 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 0 | pad suit only | no | g=0.466 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.26, I(M;suit)=0.45, I(M;suit|K)=1.37 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 1 | pad suit only | no | g=0.478 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.35, I(M;suit)=0.51, I(M;suit|K)=1.47 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 2 | pad suit only | no | g=0.560 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.93, I(M;suit)=0.26, I(M;suit|K)=1.59 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 3 | pad suit only | no | g=0.576 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.94, I(M;suit)=0.21, I(M;suit|K)=1.62 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 4 | pad suit only | no | g=0.389 vs 0.750; suit leaks, rank in clear; I(M;X)=2.55, I(M;suit)=0.64, I(M;suit|K)=1.39 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 5 | pad suit only | no | g=0.686 vs 0.750; suit partly padded, rank partly sent; I(M;X)=1.90, I(M;suit)=0.08, I(M;suit|K)=1.84 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 6 | pad suit only | no | g=0.471 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.28, I(M;suit)=0.45, I(M;suit|K)=1.39 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 7 | pad suit only | no | g=0.492 vs 0.750; suit leaks, rank partly sent; I(M;X)=2.30, I(M;suit)=0.40, I(M;suit|K)=1.44 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 8 | pad suit only | no | g=0.500 vs 0.750; suit leaks, rank in clear; I(M;X)=2.42, I(M;suit)=0.48, I(M;suit|K)=1.53 |
| tabular_sigma1 | suit4x4 | 4 | 2 | pub | 9 | pad suit only | no | g=0.592 vs 0.750; suit leaks, rank partly sent; I(M;X)=1.82, I(M;suit)=0.14, I(M;suit|K)=1.53 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 0 | reaches best known | no | g=0.382 vs 0.500; I(M;X)=2.49 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 1 | reaches best known | no | g=0.371 vs 0.500; I(M;X)=2.65 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 2 | reaches best known | no | g=0.410 vs 0.500; I(M;X)=2.66 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 3 | reaches best known | no | g=0.371 vs 0.500; I(M;X)=2.48 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 4 | reaches best known | no | g=0.429 vs 0.500; I(M;X)=2.76 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 5 | reaches best known | no | g=0.382 vs 0.500; I(M;X)=2.54 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 6 | reaches best known | no | g=0.427 vs 0.500; I(M;X)=2.64 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 7 | reaches best known | no | g=0.364 vs 0.500; I(M;X)=2.62 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 8 | reaches best known | no | g=0.408 vs 0.500; I(M;X)=2.68 |
| tabular_sigma1 | suit4x4 | 4 | 1 | pub | 9 | reaches best known | no | g=0.397 vs 0.500; I(M;X)=2.70 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 0 | pad suit only | no | g=0.169 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.66, I(M;suit)=0.07, I(M;suit|K)=0.18 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 1 | pad suit only | no | g=0.187 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.36, I(M;suit)=0.03, I(M;suit|K)=0.20 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 2 | pad suit only | no | g=0.175 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.70, I(M;suit)=0.06, I(M;suit|K)=0.18 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 3 | pad suit only | no | g=0.183 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.84, I(M;suit)=0.04, I(M;suit|K)=0.27 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 4 | pad suit only | no | g=0.187 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.38, I(M;suit)=0.01, I(M;suit|K)=0.15 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 5 | pad suit only | no | g=0.176 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.59, I(M;suit)=0.05, I(M;suit|K)=0.27 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 6 | pad suit only | no | g=0.187 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.28, I(M;suit)=0.03, I(M;suit|K)=0.22 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 7 | pad suit only | no | g=0.187 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.28, I(M;suit)=0.01, I(M;suit|K)=0.27 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 8 | pad suit only | no | g=0.187 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.28, I(M;suit)=0.03, I(M;suit|K)=0.24 |
| tabular_sigma1 | suit4x4 | 2 | 2 | pub | 9 | pad suit only | no | g=0.182 vs 0.188; suit partly padded, rank partly sent; I(M;X)=0.70, I(M;suit)=0.04, I(M;suit|K)=0.28 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 0 | reaches best known | no | g=0.687 vs 0.750; I(M;X)=3.87 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 1 | reaches best known | no | g=0.687 vs 0.750; I(M;X)=3.83 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 2 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=4.00 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 3 | reaches best known | yes | g=0.750 vs 0.750; I(M;X)=4.00 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 4 | reaches best known | no | g=0.687 vs 0.750; I(M;X)=3.86 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 5 | reaches best known | yes | g=0.749 vs 0.750; I(M;X)=3.99 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 6 | reaches best known | no | g=0.687 vs 0.750; I(M;X)=3.87 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 7 | reaches best known | no | g=0.687 vs 0.750; I(M;X)=3.87 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 8 | reaches best known | no | g=0.651 vs 0.750; I(M;X)=3.74 |
| tabular_sigma1 | suit4x4 | 4 | 0 | priv | 9 | reaches best known | no | g=0.687 vs 0.750; I(M;X)=3.87 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 0 | key as pad | no | g=0.195 vs 0.938; I(M;X)=0.39 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 1 | key as pad | no | g=0.160 vs 0.938; I(M;X)=0.36 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 2 | key as pad | no | g=0.163 vs 0.938; I(M;X)=0.37 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 3 | key as pad | no | g=0.185 vs 0.938; I(M;X)=0.33 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 4 | key as pad | no | g=0.184 vs 0.938; I(M;X)=0.35 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 5 | key as pad | no | g=0.189 vs 0.938; I(M;X)=0.35 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 6 | key as pad | no | g=0.168 vs 0.938; I(M;X)=0.33 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 7 | key as pad | no | g=0.188 vs 0.938; I(M;X)=0.34 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 8 | key as pad | no | g=0.221 vs 0.938; I(M;X)=0.40 |
| tabular_sigma1 | attack4x4 | 2 | 4 | pub | 9 | key as pad | no | g=0.171 vs 0.938; I(M;X)=0.37 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 0 | reaches best known | no | g=0.335 vs 0.750; I(M;X)=1.49 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 1 | reaches best known | no | g=0.288 vs 0.750; I(M;X)=1.70 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 2 | reaches best known | no | g=0.287 vs 0.750; I(M;X)=1.74 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 3 | reaches best known | no | g=0.318 vs 0.750; I(M;X)=1.48 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 4 | reaches best known | no | g=0.303 vs 0.750; I(M;X)=1.26 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 5 | reaches best known | no | g=0.349 vs 0.750; I(M;X)=1.73 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 6 | reaches best known | no | g=0.280 vs 0.750; I(M;X)=1.68 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 7 | reaches best known | no | g=0.264 vs 0.750; I(M;X)=1.61 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 8 | reaches best known | no | g=0.244 vs 0.750; I(M;X)=1.21 |
| tabular_sigma1 | attack4x4 | 2 | 2 | pub | 9 | reaches best known | no | g=0.333 vs 0.750; I(M;X)=1.53 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 0 | reaches best known | no | g=0.296 vs 0.500; I(M;X)=1.94 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 1 | reaches best known | no | g=0.253 vs 0.500; I(M;X)=1.35 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 2 | reaches best known | no | g=0.186 vs 0.500; I(M;X)=1.66 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 3 | reaches best known | no | g=0.199 vs 0.500; I(M;X)=1.88 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 4 | reaches best known | no | g=0.294 vs 0.500; I(M;X)=1.65 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 5 | reaches best known | no | g=0.202 vs 0.500; I(M;X)=1.48 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 6 | reaches best known | no | g=0.202 vs 0.500; I(M;X)=1.48 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 7 | reaches best known | no | g=0.186 vs 0.500; I(M;X)=2.02 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 8 | reaches best known | no | g=0.248 vs 0.500; I(M;X)=1.55 |
| tabular_sigma1 | attack4x4 | 2 | 1 | pub | 9 | reaches best known | no | g=0.296 vs 0.500; I(M;X)=2.06 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 0 | reaches best known | no | g=0.165 vs 0.250; I(M;X)=0.81 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 1 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=1.62 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 2 | reaches best known | no | g=0.187 vs 0.250; I(M;X)=1.89 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 3 | reaches best known | no | g=0.212 vs 0.250; I(M;X)=2.50 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 4 | reaches best known | no | g=0.135 vs 0.250; I(M;X)=0.81 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 5 | reaches best known | no | g=0.153 vs 0.250; I(M;X)=0.81 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 6 | reaches best known | yes | g=0.250 vs 0.250; I(M;X)=2.00 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 7 | reaches best known | no | g=0.140 vs 0.250; I(M;X)=2.63 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 8 | reaches best known | no | g=0.185 vs 0.250; I(M;X)=2.00 |
| tabular_sigma1 | attack4x4 | 2 | 0 | pub | 9 | reaches best known | no | g=0.154 vs 0.250; I(M;X)=0.99 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 0 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.31 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 1 | reaches best known | no | g=0.500 vs 0.938; I(M;X)=3.00 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 2 | reaches best known | no | g=0.500 vs 0.938; I(M;X)=3.00 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 3 | reaches best known | no | g=0.375 vs 0.938; I(M;X)=2.31 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 4 | reaches best known | no | g=0.625 vs 0.938; I(M;X)=3.50 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 5 | reaches best known | no | g=0.500 vs 0.938; I(M;X)=3.00 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 6 | reaches best known | no | g=0.562 vs 0.938; I(M;X)=3.00 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 7 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=2.81 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 8 | reaches best known | no | g=0.437 vs 0.938; I(M;X)=3.00 |
| tabular_sigma1 | attack4x4 | 2 | 0 | priv | 9 | reaches best known | no | g=0.687 vs 0.938; I(M;X)=3.50 |

wall time 355 s for 180 runs
