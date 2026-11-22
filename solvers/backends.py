"""LP / MILP backends: Gurobi (primary) and HiGHS via SciPy (fallback, no licence).

Both backends take the same sparse-matrix problem

    optimize  c^T x   s.t.  A_ub x <= b_ub,  A_eq x = b_eq,  lb <= x <= ub

and report duals with one convention: ``dual_ub[i] = d(objective)/d(b_ub[i])``
and likewise for ``dual_eq``, with the objective in the requested sense.

``backend="auto"`` uses Gurobi if a licence can be started (the Gurobi WLS
licence needs internet), otherwise HiGHS. A size-limited (restricted) Gurobi
licence that rejects a model also falls back to HiGHS.

Gurobi uses at most ``solvers.threads.num_threads()`` threads (FAI_THREADS,
default 2).
"""

import os
from dataclasses import dataclass
import time
import warnings

import numpy as np
import scipy.sparse as sp

from solvers.threads import num_threads

_GUROBI_ENV = None
_GUROBI_ERROR = None

TOL = 1e-9


@dataclass
class Result:
    x: np.ndarray
    obj: float
    dual_ub: np.ndarray = None
    dual_eq: np.ndarray = None
    backend: str = ""
    seconds: float = 0.0
    status: str = "optimal"     # "optimal", "bound_stop" or "time_limit" (MILP only)
    bound: float = None         # MILP: best proven bound on the optimum


def _gurobi_env():
    """Start one shared Gurobi environment, or return None if unavailable."""
    global _GUROBI_ENV, _GUROBI_ERROR
    if _GUROBI_ENV is None and _GUROBI_ERROR is None:
        try:
            import gurobipy as gp
            env = gp.Env(empty=True)
            env.setParam("OutputFlag", 0)
            env.setParam("Threads", num_threads())
            mem = os.environ.get("FAI_GUROBI_MEM_GB")   # opt-in memory cap (laptop has no swap)
            if mem:
                env.setParam("SoftMemLimit", float(mem))        # stop cleanly (status MEM_LIMIT)
                env.setParam("NodefileStart", float(mem) / 2)   # spill B&B nodes to disk first
            env.start()
            _GUROBI_ENV = env
        except Exception as e:  # missing package, no licence, no network
            _GUROBI_ERROR = e
    return _GUROBI_ENV


def resolve_backend(backend="auto"):
    """Return "gurobi" or "highs" for a requested backend name."""
    if backend == "auto":
        return "gurobi" if _gurobi_env() is not None else "highs"
    if backend == "gurobi" and _gurobi_env() is None:
        raise RuntimeError(f"Gurobi requested but unavailable: {_GUROBI_ERROR}")
    if backend not in ("gurobi", "highs"):
        raise ValueError(f"unknown backend {backend!r}")
    return backend


def _csr(A, n):
    return sp.csr_matrix((0, n)) if A is None else sp.csr_matrix(A)


def solve(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, lb=0.0, ub=np.inf,
          integrality=None, maximize=False, backend="auto", time_limit=None, bound_stop=None):
    """Solve an LP (``integrality is None``) or MILP; integer variables are marked 1.

    ``bound_stop`` (MILP, maximization): the solver may stop as soon as its
    best bound proves the optimum is at most this value. The returned x is
    then the best solution found, which is enough when the caller only needs
    to know that nothing beats ``bound_stop``.
    """
    c = np.asarray(c, dtype=np.float64)
    n = len(c)
    A_ub = _csr(A_ub, n)
    A_eq = _csr(A_eq, n)
    b_ub = np.zeros(0) if b_ub is None else np.asarray(b_ub, dtype=np.float64)
    b_eq = np.zeros(0) if b_eq is None else np.asarray(b_eq, dtype=np.float64)
    lb = np.broadcast_to(np.asarray(lb, dtype=np.float64), (n,))
    ub = np.broadcast_to(np.asarray(ub, dtype=np.float64), (n,))
    name = resolve_backend(backend)
    start = time.perf_counter()
    if name == "gurobi":
        try:
            res = _solve_gurobi(c, A_ub, b_ub, A_eq, b_eq, lb, ub, integrality, maximize,
                                time_limit, bound_stop)
        except _size_limit_error() as e:
            if backend == "gurobi" or getattr(e, "errno", None) != 10010:
                raise
            warnings.warn("Gurobi licence is size-limited; falling back to HiGHS")
            name = "highs"
    if name == "highs":
        res = _solve_highs(c, A_ub, b_ub, A_eq, b_eq, lb, ub, integrality, maximize, time_limit)
    res.backend = name
    res.seconds = time.perf_counter() - start
    return res


def _size_limit_error():
    try:
        import gurobipy as gp
        return gp.GurobiError
    except ImportError:
        return ()


def _solve_gurobi(c, A_ub, b_ub, A_eq, b_eq, lb, ub, integrality, maximize, time_limit,
                  bound_stop=None):
    import gurobipy as gp
    from gurobipy import GRB

    m = gp.Model(env=_gurobi_env())
    m.Params.FeasibilityTol = TOL
    m.Params.OptimalityTol = TOL
    if integrality is not None:
        m.Params.MIPGap = 1e-10
        m.Params.MIPGapAbs = 1e-10
        m.Params.IntFeasTol = 1e-9
    if time_limit:
        m.Params.TimeLimit = time_limit
    if bound_stop is not None and integrality is not None:
        m.Params.BestBdStop = bound_stop  # in the model's own objective sense
    vtype = GRB.CONTINUOUS
    if integrality is not None:
        vtype = np.where(np.asarray(integrality) > 0, GRB.INTEGER, GRB.CONTINUOUS)
    x = m.addMVar(len(c), lb=lb, ub=ub, vtype=vtype)
    cu = m.addMConstr(A_ub, x, "<", b_ub) if A_ub.shape[0] else None
    ce = m.addMConstr(A_eq, x, "=", b_eq) if A_eq.shape[0] else None
    m.setObjective(c @ x, GRB.MAXIMIZE if maximize else GRB.MINIMIZE)
    m.optimize()
    status = {GRB.OPTIMAL: "optimal", GRB.USER_OBJ_LIMIT: "bound_stop",
              GRB.TIME_LIMIT: "time_limit"}.get(m.Status)
    if status is None or (status == "time_limit" and integrality is None):
        raise RuntimeError(f"Gurobi status {m.Status}")
    worst = -np.inf if maximize else np.inf
    if m.SolCount == 0:  # stopped (bound or time) before finding any solution
        return Result(x=None, obj=worst, status=status, bound=float(m.ObjBound))
    res = Result(x=np.array(x.X), obj=float(m.ObjVal), status=status)
    if integrality is not None:
        res.bound = float(m.ObjBound)
    else:
        res.dual_ub = np.array(cu.Pi) if cu is not None else np.zeros(0)
        res.dual_eq = np.array(ce.Pi) if ce is not None else np.zeros(0)
    return res


def _solve_highs(c, A_ub, b_ub, A_eq, b_eq, lb, ub, integrality, maximize, time_limit):
    from scipy.optimize import Bounds, LinearConstraint, linprog, milp

    sign = -1.0 if maximize else 1.0
    if integrality is None:
        out = linprog(sign * c,
                      A_ub=A_ub if A_ub.shape[0] else None, b_ub=b_ub if A_ub.shape[0] else None,
                      A_eq=A_eq if A_eq.shape[0] else None, b_eq=b_eq if A_eq.shape[0] else None,
                      bounds=np.column_stack([lb, ub]), method="highs",
                      options={"primal_feasibility_tolerance": TOL,
                               "dual_feasibility_tolerance": TOL,
                               **({"time_limit": time_limit} if time_limit else {})})
        if out.status != 0:
            raise RuntimeError(f"HiGHS LP failed: {out.message}")
        res = Result(x=out.x, obj=sign * out.fun)
        res.dual_ub = sign * out.ineqlin.marginals if A_ub.shape[0] else np.zeros(0)
        res.dual_eq = sign * out.eqlin.marginals if A_eq.shape[0] else np.zeros(0)
        return res
    cons = []
    if A_ub.shape[0]:
        cons.append(LinearConstraint(A_ub, -np.inf, b_ub))
    if A_eq.shape[0]:
        cons.append(LinearConstraint(A_eq, b_eq, b_eq))
    options = {"mip_rel_gap": 1e-10}
    if time_limit:
        options["time_limit"] = time_limit
    out = milp(sign * c, integrality=np.asarray(integrality), bounds=Bounds(lb, ub),
               constraints=cons, options=options)
    bound = getattr(out, "mip_dual_bound", None)
    bound = None if bound is None else sign * bound
    if out.status == 1:  # time or iteration limit
        if out.x is None:
            return Result(x=None, obj=-np.inf if maximize else np.inf, status="time_limit",
                          bound=bound)
        return Result(x=out.x, obj=sign * out.fun, status="time_limit", bound=bound)
    if out.status != 0:
        raise RuntimeError(f"HiGHS MILP failed: {out.message}")
    return Result(x=out.x, obj=sign * out.fun, bound=bound)
