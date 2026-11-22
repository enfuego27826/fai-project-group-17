"""CPU limits for solver runs (keep laptops cool).

``FAI_THREADS`` (default 2) caps Gurobi threads and BLAS/OpenMP threads.
``limit_threads()`` must run before NumPy/SciPy are imported to affect BLAS,
so scripts and tests/conftest.py call it first.
"""

import os

DEFAULT_THREADS = 2


def num_threads():
    """Thread budget for one solver process, from FAI_THREADS (default 2)."""
    return max(1, int(os.environ.get("FAI_THREADS", DEFAULT_THREADS)))


def limit_threads():
    """Set BLAS/OpenMP thread limits (no effect on libraries already loaded)."""
    n = str(num_threads())
    for var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                "NUMEXPR_NUM_THREADS"):
        os.environ.setdefault(var, n)
