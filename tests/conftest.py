from solvers.threads import limit_threads

limit_threads()  # cap BLAS/Gurobi threads in tests (FAI_THREADS, default 2)
