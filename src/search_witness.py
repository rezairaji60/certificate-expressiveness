"""Finite-support LP discovery followed by exact rational reconstruction.

LP infeasibility says only that this support grid has no witness. LP feasibility
is not a proof until rational replay succeeds. Requires numpy/scipy for discovery.
"""
from fractions import Fraction as F
import json
from pathlib import Path
from exact_verify import validate_witness


def exact_linear_solution(M, rhs):
    """Rational RREF; free variables set to zero, followed by residual replay."""
    n = len(M[0])
    rows = [list(map(F,row))+[F(b)] for row,b in zip(M,rhs)]
    pivot_columns = []
    at = 0
    for col in range(n):
        pivot = next((i for i in range(at,len(rows)) if rows[i][col]),None)
        if pivot is None:
            continue
        rows[at],rows[pivot] = rows[pivot],rows[at]
        divisor = rows[at][col]
        rows[at] = [x/divisor for x in rows[at]]
        for i in range(len(rows)):
            if i != at and rows[i][col]:
                factor = rows[i][col]
                rows[i] = [x-factor*y for x,y in zip(rows[i],rows[at])]
        pivot_columns.append(col)
        at += 1
    if any(not any(row[:n]) and row[n] for row in rows):
        raise ValueError("No exact solution on numerical active support")
    out = [F(0)]*n
    for i,col in enumerate(pivot_columns):
        out[col] = rows[i][-1]
    if any(sum((a*x for a,x in zip(row,out)),F(0)) != b for row,b in zip(M,rhs)):
        raise ValueError("Exact reconstruction residual failed")
    return out


def discover(degree=3):
    import numpy as np
    from scipy.optimize import linprog
    a,t,u,v = F(12,25),F(3,4),F(1641,3200),F(103,200)
    f = lambda x: x*(1+F(1,2)*(x*x-F(1,4))*(1-x*x))
    source = [F(-1),-t,F(0),t,F(1)]
    initial = [-a,F(0),a]
    unsafe = [-v,-u,u,v]
    ns,ni,nu = len(source),len(initial),len(unsafe)
    M, rhs = [],[]
    for start,size in [(0,ns),(ns,ni),(ns+ni,nu)]:
        M.append([F(int(start <= j < start+size)) for j in range(ns+ni+nu)])
        rhs.append(F(1))
    for k in range(1,degree+1):
        M.append([x**k for x in source]+[-x**k for x in initial]+[F(0)]*nu)
        rhs.append(F(0))
        M.append([f(x)**k for x in source]+[F(0)]*ni+[-x**k for x in unsafe])
        rhs.append(F(0))
    result = linprog(np.zeros(ns+ni+nu),A_eq=np.array(M,dtype=float),
                     b_eq=np.array(rhs,dtype=float),bounds=(0,None),method="highs")
    if not result.success:
        return {"degree":degree,"status":"NO_VERIFIED_WITNESS_ON_THIS_GRID",
                "solver_status":int(result.status),"solver_message":result.message,
                "interpretation":"No conclusion about certificate existence or other supports."}
    active = [i for i,w in enumerate(result.x) if w > 1e-9]
    try:
        weights = exact_linear_solution([[row[i] for i in active] for row in M],rhs)
        if any(w < 0 for w in weights):
            raise ValueError("Rational reconstruction has negative weight")
        full = [F(0)]*(ns+ni+nu)
        for i,w in zip(active,weights):
            full[i] = w
        mu = [(x,w) for x,w in zip(source,full[:ns]) if w]
        mu0 = [(x,w) for x,w in zip(initial,full[ns:ns+ni]) if w]
        nu_atoms = [(x,w) for x,w in zip(unsafe,full[ns+ni:]) if w]
        validate_witness(mu,mu0,nu_atoms,f,degree,a,u,v)
    except ValueError as exc:
        return {"degree":degree,"status":"NUMERICAL_CANDIDATE_NOT_VERIFIED","reason":str(exc)}
    return {"degree":degree,"status":"EXACT_ATOMIC_WITNESS_VERIFIED",
            "atoms":{name:[[str(x),str(w)] for x,w in atoms]
                     for name,atoms in [("mu",mu),("mu0",mu0),("nu",nu_atoms)]}}


if __name__ == "__main__":
    results = [discover(d) for d in [1,2,3,4]]
    path = Path(__file__).resolve().parents[1]/"evidence"/"lp_discovery.json"
    path.write_text(json.dumps(results,indent=2)+"\n")
    print(json.dumps(results,indent=2))
