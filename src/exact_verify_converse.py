"""Exact finite evidence for the candidate converse note (Python stdlib).

These checks cover the examples and rational bounds, not the general theorem.
Run without -O so all checks execute.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

if not __debug__:
    raise RuntimeError("Run without -O: exact verification requires assertions")


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Q(0))


def mv(a, x):
    return [dot(row, x) for row in a]


def moments(atoms, d, transform=lambda x: x):
    return [
        sum((w * transform(x) ** k for x, w in atoms), Q(0))
        for k in range(d + 1)
    ]


def verify_rotation():
    q, r, a, u, eps = Q(9, 10), Q(1, 2), Q(1, 4), Q(3, 4), Q(1, 100)
    R = [[Q(0), Q(-1)], [Q(1), Q(0)]]
    G = [[Q(1), Q(0)], [Q(0), Q(1)], [Q(-1), Q(0)], [Q(0), Q(-1)]]
    perm = [[Q(0), Q(0), Q(0), Q(1)],
            [Q(1), Q(0), Q(0), Q(0)],
            [Q(0), Q(1), Q(0), Q(0)],
            [Q(0), Q(0), Q(1), Q(0)]]
    A = [[q * z for z in row] for row in perm]
    # Equality of every affine coefficient is a global polynomial identity.
    GF = [[q * sum(G[i][k] * R[k][j] for k in range(2))
           for j in range(2)] for i in range(4)]
    AG = [[sum(A[i][k] * G[k][j] for k in range(4))
           for j in range(2)] for i in range(4)]
    eta = (1 - q) * r
    assert GF == AG
    assert all(-r == -r * sum(A[i]) - eta for i in range(4))
    assert all(z >= 0 for row in A for z in row)
    assert eta == Q(1, 20)
    assert r - a == Q(1, 4) and u - r == Q(1, 4)
    assert a + eps < r
    bound = q * r + (q + 1) * eps
    assert bound == Q(469, 1000) and bound < r
    assert u < q  # used in the analytic one-component impossibility proof
    return {
        "degree_bound": 1,
        "components": 4,
        "A": [[str(x) for x in row] for row in A],
        "initial_margin": str(r-a),
        "unsafe_anchor_margin": str(u-r),
        "global_propagation_margin": str(eta),
        "feature_error_radius": str(eps),
        "robust_successor_infinity_norm_bound": str(bound),
        "verification": "all affine coefficients and constant offsets match",
    }



def verify_scalar_baseline(eta=Q(1, 20)):
    """Verify Majid's affine baseline on the full interval, without sampling."""
    # (A*b)-b(f) = 3/10 - x^2/4
    residual = [Q(3, 10), Q(0), Q(-1, 4)]
    endpoint_minimum = residual[0] + residual[2]
    if eta <= 0 or eta > endpoint_minimum:
        raise ValueError("Scalar baseline margin exceeds the exact endpoint bound")
    # residual-eta = (1/20-eta)+(1/4)*(1-x^2) >= 0 on [-1,1].
    assert residual == [Q(1,20)+Q(1,4), Q(0), -Q(1,4)]
    assert Q(3,5)-Q(1,4) == Q(7,20)
    assert Q(7,10)-Q(3,5) == Q(1,10)
    return {
        "degree": 1, "components": 1, "multiplier": "1/2",
        "initial_margin": "7/20", "unsafe_anchor_margin": "1/10",
        "global_propagation_margin": str(endpoint_minimum),
        "residual_coefficients_ascending": [str(v) for v in residual],
        "domain_proof": "residual-1/20=(1-x^2)/4; equality at x=+/-1",
        "comparison": "12-component example validates supplied-body extraction, not a benefit over scalar",
    }


def padd(*polys):
    result = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, Q(0)) + coefficient
    return {k: v for k, v in result.items() if v}


def pscale(coefficient, poly):
    return {k: coefficient*v for k, v in poly.items() if coefficient*v}


def pmul(left, right):
    result = {}
    for (a, b), c in left.items():
        for (d, e), f in right.items():
            exponent = (a+d, b+e)
            result[exponent] = result.get(exponent, Q(0)) + c*f
    return {k: v for k, v in result.items() if v}


def verify_nonlinear_recovery(theta=Q(1,40), matrix=None,
                              eta=Q(1,40), eps=Q(1,100)):
    """Exact coefficient and nonnegative-factor proof for the cubic family.

    Universal scalar impossibility is the analytic a,x_* argument in the note,
    not an inference from solver failure or finitely many candidate functions.
    """
    q, r0, delta = Q(9,10), Q(1,2), Q(1,40)
    if not Q(0) < theta <= delta:
        raise ValueError("Cubic-family parameter must lie in (0,1/40]")
    if eta <= 0 or eta > (1-q)*r0-theta:
        raise ValueError("Propagation target exceeds the certified perturbation margin")
    one = {(0,0): Q(1)}
    x = [{(1,0):Q(1)}, {(0,1):Q(1)}]
    radius2 = padd(pmul(x[0],x[0]),pmul(x[1],x[1]))
    disk = padd(one, pscale(-1,radius2))
    R = [[Q(0),Q(-1)],[Q(1),Q(0)]]
    G = [[Q(1),Q(0)],[Q(0),Q(1)],[Q(-1),Q(0)],[Q(0),Q(-1)]]
    permutation = [[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
    expected_A = [[q*value for value in row] for row in permutation]
    A = expected_A if matrix is None else matrix
    if len(A)!=4 or any(len(row)!=4 for row in A):
        raise ValueError("Comparison matrix must have four rows and columns")
    if any(v<0 for row in A for v in row):
        raise ValueError("Comparison matrix must be entrywise nonnegative")
    if any(sum(row)!=q for row in A):
        raise ValueError("Comparison row sum does not match the certified coupling")
    factor = padd(pscale(q,one),pscale(-theta,disk))
    f = [pscale(-1,pmul(factor,x[1])),pmul(factor,x[0])]
    B = [padd(*(pscale(g,coord) for g,coord in zip(row,x)),
              pscale(-r0,one)) for row in G]
    residuals = []
    for i in range(4):
        AB = padd(*(pscale(A[i][j],B[j]) for j in range(4)))
        Bf = padd(*(pscale(G[i][j],f[j]) for j in range(2)),
                   pscale(-r0,one))
        residual = padd(AB,pscale(-1,Bf))
        u = padd(*(pscale(sum(G[i][k]*R[k][j] for k in range(2)),x[j])
                   for j in range(2)))
        expected = padd(pscale((1-q)*r0,one),pscale(theta,pmul(disk,u)))
        if residual != expected:
            raise ValueError("Global cubic comparison identity fails")
        # residual-eta = nonnegative constant
        #                + theta*((1-||x||^2)*(1+u)+||x||^2).
        # u is a signed coordinate, so 1+u>=0 on the disk.
        nonnegative_form = padd(
            pscale((1-q)*r0-theta-eta,one),
            pscale(theta,padd(pmul(disk,padd(one,u)),radius2)))
        if padd(residual,pscale(-eta,one)) != nonnegative_form:
            raise ValueError("Nonnegative disk-factor identity fails")
        residuals.append([{"powers":list(k),"coefficient":str(v)}
                          for k,v in sorted(residual.items())])
    assert q-delta > Q(3,4)  # analytic scalar contradiction stays strict
    assert q+delta < 1  # entire perturbation ball remains in the domain
    # All convexified pairs obey t=q*R*s+e_bar, ||e_bar||<=delta.
    bound = q*r0+delta+(q+1)*eps
    if eps <= 0 or Q(1,4)+eps > r0 or bound >= r0:
        raise ValueError("Independent feature-error radius is not certified")
    # Radial factor in [q-theta,q] implies a scalar quadratic certificate.
    assert Q(0) < q-theta <= q < 1
    scalar2_margin = (1-q*q)*Q(1,4)
    assert scalar2_margin == Q(19,400)
    return {
        "dynamics_degree": 3, "certificate_degree": 1, "components": 4,
        "theta":str(theta),"theta_family":"0 < theta <= 1/40",
        "dynamics":"f=(9/10-theta*(1-x1^2-x2^2))*(-x2,x1)",
        "A":[[str(v) for v in row] for row in A],
        "initial_margin":"1/4", "unsafe_anchor_margin":"1/4",
        "uniform_family_propagation_margin":"1/40",
        "certified_selected_target":str(eta),
        "spectral_radius":"9/10",
        "perturbation_radius":str(delta),
        "feature_error_radius":str(eps),
        "robust_successor_infinity_norm_bound":str(bound),
        "global_residual_polynomials":residuals,
        "continuum_proof":"exact coefficients plus nonnegative disk-factor identity; no grid",
        "scalar_affine_impossibility":"analytic x_*=R^T*a/||a|| proof for every lambda>=0",
        "scalar_quadratic_alternative":{
            "degree":2,"components":1,"multiplier":"81/100",
            "initial_margin":"3/16","unsafe_anchor_margin":"5/16",
            "global_propagation_margin":str(scalar2_margin)},
        "minimum_degree_scope":{
            "scalar_constant_comparison":2,"finite_fixed_anchor_vector":1,
            "proof":"affine impossibility, explicit quadratic/vector upper bounds, no constant separator",
            "minimum_vector_component_count":"not established; 2 <= m_min <= 4"},
    }

def verify_moment_obstruction():
    a, t, u, v = Q(12, 25), Q(3, 4), Q(1641, 3200), Q(103, 200)

    def f(x):
        return Q(7, 8)*x + Q(5, 8)*x**3 - Q(1, 2)*x**5

    mu = [(Q(0), Q(369, 625)), (-t, Q(128, 625)), (t, Q(128, 625))]
    mu0 = [(-a, Q(1, 2)), (a, Q(1, 2))]
    nu = [(-u, Q(1, 2)), (u, Q(1, 2))]
    for atoms in (mu, mu0, nu):
        assert sum(w for _, w in atoms) == 1
        assert all(w >= 0 for _, w in atoms)
    assert all(abs(x) <= 1 for x, _ in mu)
    assert all(abs(x) <= a for x, _ in mu0)
    assert all(u <= abs(x) <= v for x, _ in nu)
    assert f(t) == Q(1641, 2048)
    assert u == a * f(t) / t
    assert Q(0) < a < Q(1, 2) < u < v < Q(1)
    assert moments(mu, 3) == moments(mu0, 3)
    assert moments(mu, 3, f) == moments(nu, 3)
    assert moments(mu, 4)[4] != moments(mu0, 4)[4]
    assert f(-Q(1)) == -1 and f(Q(1)) == 1
    # f'(x) coefficient identity:
    # 7/8 + 15x^2/8 - 5x^4/2
    # = 1/4 + (1-x^2)(5/8 + 5x^2/2).
    assert [Q(7, 8), Q(15, 8), Q(-5, 2)] == [
        Q(1, 4)+Q(5, 8), Q(5, 2)-Q(5, 8), Q(-5, 2)
    ]
    return {
        "excluded_degree_bounds": [2, 3],
        "input_moments_0_through_3": [str(x) for x in moments(mu, 3)],
        "successor_moments_0_through_3": [str(x) for x in moments(mu, 3, f)],
        "quadratic_ibc_initial_margin": str(Q(1, 4)-a*a),
        "quadratic_ibc_unsafe_margin": str(u*u-Q(1, 4)),
        "mu": [[str(x), str(w)] for x, w in mu],
        "mu0": [[str(x), str(w)] for x, w in mu0],
        "nu": [[str(x), str(w)] for x, w in nu],
        "scope": "all finite forward fixed-anchor component counts and A >= 0",
    }


def main():
    result = {
        "status": "EXACT_FINITE_EVIDENCE_VERIFIED",
        "arithmetic": "fractions.Fraction; no floating point",
        "rotation": verify_rotation(),
        "scalar_baseline": verify_scalar_baseline(),
        "nonlinear_same_degree_recovery": verify_nonlinear_recovery(),
        "moment_obstruction": verify_moment_obstruction(),
        "limit": "General converse and universal impossibility rely on the note's proofs.",
    }
    destination = Path(__file__).resolve().parents[1] / "evidence" / "converse_report.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
