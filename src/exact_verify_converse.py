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
        "moment_obstruction": verify_moment_obstruction(),
        "limit": "General converse and universal impossibility rely on the note's proofs.",
    }
    destination = Path(__file__).resolve().parents[1] / "evidence" / "converse_report.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
