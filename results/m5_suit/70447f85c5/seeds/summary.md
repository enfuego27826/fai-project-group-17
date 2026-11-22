| method | game | k | s | ρ | exact V | g(π_T) mean ± 95% CI | gap | I(M;X) | I(M;φ(X)) | cost of leak | check | yes / seeds | time/run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 1/2 | 0.474 ± 0.057 | 0.026 | 0.99 | 0.00 | 0.000 | pad suit only | 9 / 10 | 3.1s |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 1/2 | 0.286 ± 0.065 | 0.214 | 1.89 | 0.00 | 0.001 | pad suit only | 0 / 10 | 11.3s |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | [1/2, 3/4] | 0.314 ± 0.066 | 0.436 | 1.28 | 0.32 | 0.038 | pad suit only | 0 / 10 | 14.0s |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 1/2 | 0.472 ± 0.062 | 0.028 | 1.00 | 0.00 | 0.002 | pad suit only | 9 / 10 | 3.1s |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 1/2 | 0.280 ± 0.072 | 0.220 | 1.97 | 0.00 | 0.010 | pad suit only | 1 / 10 | 11.3s |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | [1/2, 3/4] | 0.313 ± 0.067 | 0.437 | 1.35 | 0.36 | 0.045 | pad suit only | 0 / 10 | 14.0s |

| method | game | k | s | ρ | seed | check | yes/no | what the policy does |
|---|---|---|---|---|---|---|---|---|
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 0 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 1 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 2 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 4 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 6 | pad suit only | yes | g=0.495 vs V=0.500; suit padded, rank in clear; I(M;X)=0.98, I(M;suit)=0.00, I(M;suit|K)=0.98 |
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 7 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 8 | pad suit only | yes | g=0.499 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=0.99 |
| pg_vs_br/avg | suit2x2 | 2 | 1 | pub | 9 | pad suit only | no | g=0.249 vs V=0.500; suit not sent, rank in clear; I(M;X)=0.99, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 0 | pad suit only | no | g=0.244 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.94, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 1 | pad suit only | no | g=0.244 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.92, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 2 | pad suit only | no | g=0.237 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.92, I(M;suit)=0.01, I(M;suit|K)=0.01 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 3 | pad suit only | no | g=0.246 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.94, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 4 | pad suit only | no | g=0.243 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.90, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 5 | pad suit only | no | g=0.484 vs V=0.500; suit padded, rank partly sent; I(M;X)=1.89, I(M;suit)=0.00, I(M;suit|K)=0.92 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 6 | pad suit only | no | g=0.428 vs V=0.500; suit partly padded, rank partly sent; I(M;X)=1.65, I(M;suit)=0.01, I(M;suit|K)=0.67 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 7 | pad suit only | no | g=0.245 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.94, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 8 | pad suit only | no | g=0.245 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.93, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/avg | suit2x4 | 3 | 1 | pub | 9 | pad suit only | no | g=0.244 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.91, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 0 | pad suit only | no | g=0.377 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.32, I(M;suit)=0.36, I(M;suit|K)=1.18 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 1 | pad suit only | no | g=0.191 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.06, I(M;suit)=0.11, I(M;suit|K)=0.11 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 2 | pad suit only | no | g=0.386 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.35, I(M;suit)=0.39, I(M;suit|K)=1.23 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 3 | pad suit only | no | g=0.354 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.15, I(M;suit)=0.20, I(M;suit|K)=0.98 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 4 | pad suit only | no | g=0.399 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.29, I(M;suit)=0.31, I(M;suit|K)=1.21 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 5 | pad suit only | no | g=0.212 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.35, I(M;suit)=0.39, I(M;suit|K)=0.4 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 6 | pad suit only | no | g=0.204 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.22, I(M;suit)=0.25, I(M;suit|K)=0.26 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 7 | pad suit only | no | g=0.222 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.48, I(M;suit)=0.51, I(M;suit|K)=0.51 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 8 | pad suit only | no | g=0.397 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.35, I(M;suit)=0.37, I(M;suit|K)=1.28 |
| pg_vs_br/avg | suit4x2 | 3 | 1 | pub | 9 | pad suit only | no | g=0.396 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.27, I(M;suit)=0.31, I(M;suit|K)=1.19 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 0 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 1 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 2 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 3 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 4 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 5 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 6 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 7 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 8 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x2 | 2 | 1 | pub | 9 | pad suit only | no | g=0.224 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.00, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 0 | pad suit only | no | g=0.239 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.99, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 1 | pad suit only | no | g=0.235 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.99, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 2 | pad suit only | no | g=0.229 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.99, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 3 | pad suit only | no | g=0.226 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.99, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 4 | pad suit only | no | g=0.234 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.99, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 5 | pad suit only | yes | g=0.500 vs V=0.500; suit padded, rank in clear; I(M;X)=1.99, I(M;suit)=0.00, I(M;suit|K)=1.0 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 6 | pad suit only | no | g=0.437 vs V=0.500; suit partly padded, rank partly sent; I(M;X)=1.75, I(M;suit)=0.02, I(M;suit|K)=0.74 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 7 | pad suit only | no | g=0.231 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.99, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 8 | pad suit only | no | g=0.231 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.99, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/last | suit2x4 | 3 | 1 | pub | 9 | pad suit only | no | g=0.235 vs V=0.500; suit not sent, rank in clear; I(M;X)=1.99, I(M;suit)=0.00, I(M;suit|K)=0.0 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 0 | pad suit only | no | g=0.380 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.39, I(M;suit)=0.40, I(M;suit|K)=1.27 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 1 | pad suit only | no | g=0.191 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.13, I(M;suit)=0.14, I(M;suit|K)=0.14 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 2 | pad suit only | no | g=0.389 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.42, I(M;suit)=0.42, I(M;suit|K)=1.29 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 3 | pad suit only | no | g=0.353 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.22, I(M;suit)=0.22, I(M;suit|K)=1.04 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 4 | pad suit only | no | g=0.391 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.33, I(M;suit)=0.33, I(M;suit|K)=1.24 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 5 | pad suit only | no | g=0.213 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.49, I(M;suit)=0.49, I(M;suit|K)=0.49 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 6 | pad suit only | no | g=0.200 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.28, I(M;suit)=0.28, I(M;suit|K)=0.28 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 7 | pad suit only | no | g=0.220 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.55, I(M;suit)=0.56, I(M;suit|K)=0.56 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 8 | pad suit only | no | g=0.396 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.38, I(M;suit)=0.38, I(M;suit|K)=1.32 |
| pg_vs_br/last | suit4x2 | 3 | 1 | pub | 9 | pad suit only | no | g=0.396 vs V=0.750; suit leaks, rank in clear; I(M;X)=1.32, I(M;suit)=0.33, I(M;suit|K)=1.24 |

wall time 77 s for 30 runs
