"""Certified finite construction for the nonlinear degree-two example.

Default replay uses only Python's standard library and exact rational arithmetic.
--discover optionally uses SciPy to propose A; every accepted proposal is then
checked with Fraction arithmetic, including the feature-cover error budget.
The example has a Lipschitz-certified paired-cover argument and an independent
exact Bernstein polynomial certificate. These finite checks do not formally
verify the general theorems in paper/converse.tex.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]
MATRIX_FILE = ROOT / "evidence" / "nonlinear_comparison_matrix.json"
REPORT_FILE = ROOT / "evidence" / "constructive_converse_report.json"
R, EPS = Q(3, 5), Q(1, 20)
XI_S, XI_T, ETA = Q(3, 160), Q(1, 80), Q(1, 100)
ROW_CAP = Q(1)
NORMALS = [(Q(1), Q(0)), (Q(0), Q(1)),
           (Q(-1), Q(0)), (Q(0), Q(-1))]
for a, b in ((Q(3, 5), Q(4, 5)), (Q(4, 5), Q(3, 5))):
    NORMALS += [(sa*a, sb*b) for sa, sb in product((1, -1), repeat=2)]
NODES = [Q(-1) + Q(k, 80) for k in range(161)]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def f(x):
    return x/2 + x*x/4


def phi(x):
    return (x, x*x)


def beta(z):
    return [dot(a, z)-R for a in NORMALS]


def poly_vertices():
    """All vertices; the four axis inequalities certify boundedness."""
    result = set()
    for a, b in combinations(NORMALS, 2):
        determinant = a[0]*b[1]-a[1]*b[0]
        if not determinant:
            continue
        z = (R*(b[1]-a[1])/determinant,
             R*(a[0]-b[0])/determinant)
        if all(v <= 0 for v in beta(z)):
            result.add(z)
    return sorted(result)


def validate_matrix(matrix, xi_s=XI_S, xi_t=XI_T, eta=ETA):
    """Validate finite LP inequalities; reject any altered error budget."""
    require(xi_s >= XI_S and xi_t >= XI_T,
            "Feature error budget is below the certified cover radii")
    require(eta > 0, "Propagation margin must be positive")
    require(len(matrix) == len(NORMALS), "Wrong matrix dimension")
    slacks = []
    row_sums = []
    for i, row in enumerate(matrix):
        require(len(row) == len(NORMALS), "Wrong matrix dimension")
        require(all(a >= 0 for a in row), "Matrix must be nonnegative")
        row_sum = sum(row, Q(0))
        require(row_sum <= ROW_CAP, "Row-sum cap exceeded")
        row_sums.append(row_sum)
        for x in NODES:
            residual = beta(phi(f(x)))[i] - dot(row, beta(phi(x)))
            slack = -eta - residual - xi_t - xi_s*row_sum
            require(slack >= 0, "Finite LP inequality failed")
            slacks.append(slack)
    # At the exact node x=0, all source and successor facets equal -R.
    spectral_bound = (R-xi_t-eta)/(R+xi_s)
    require(max(row_sums) <= spectral_bound < 1,
            "Schur row-sum bound failed")
    return {"minimum_exact_lp_slack": str(min(slacks)),
            "maximum_row_sum": str(max(row_sums)),
            "certified_spectral_radius_upper_bound": str(spectral_bound)}



def verify_global_polynomials(matrix, eta=ETA):
    """Independent continuum proof in a degree-four Bernstein basis.

    Each row expands (AB)_i-B_i(f(x)) directly; no cover nodes, Lipschitz
    constants, or floating-point operations enter this check.
    Bernstein basis weights are nonnegative and sum to one on [-1,1].
    """
    require(eta > 0, "Propagation margin must be positive")
    require(len(matrix) == len(NORMALS)
            and all(len(row) == len(NORMALS) for row in matrix),
            "Wrong matrix dimension")
    require(all(a >= 0 for row in matrix for a in row),
            "Matrix must be nonnegative")
    all_bernstein = []
    endpoints = []
    for i, row in enumerate(matrix):
        u, v = NORMALS[i]
        # f=x/2+x^2/4 and f^2=x^2/4+x^3/4+x^4/16.
        coefficients = [
            R*(1-sum(row, Q(0))),
            sum((a*n[0] for a, n in zip(row, NORMALS)), Q(0))-u/2,
            sum((a*n[1] for a, n in zip(row, NORMALS)), Q(0))-u/4-v/4,
            -v/4, -v/16,
        ]
        # Substitute x=2t-1, then convert the power basis to degree-4
        # Bernstein coefficients on 0<=t<=1.
        transformed = [
            2**j*sum((coefficients[k]*comb(k,j)*(-1)**(k-j)
                      for k in range(j,5)), Q(0))
            for j in range(5)
        ]
        bernstein_values = [
            sum((transformed[j]*Q(comb(k,j),comb(4,j))
                 for j in range(k+1)), Q(0))
            for k in range(5)
        ]
        require(min(bernstein_values) >= eta,
                "Global polynomial propagation certificate failed")
        all_bernstein.append(bernstein_values)
        for x in (Q(-1), Q(1)):
            value = sum((a*x**k for k,a in enumerate(coefficients)), Q(0))
            endpoints.append((value, i+1, x))
    lower = min(min(row) for row in all_bernstein)
    attained, component, state = min(endpoints)
    return {
        "basis": "degree-four Bernstein on [-1,1]",
        "componentwise_coefficients": [[str(v) for v in row]
                                      for row in all_bernstein],
        "requested_propagation_margin": str(eta),
        "certified_uniform_propagation_margin": str(lower),
        "minimum_bernstein_slack_at_requested_margin": str(lower-eta),
        "smallest_endpoint_residual": str(attained),
        "sharp_for_fixed_certificate": lower == attained,
        "endpoint_witness": {"component_one_based": component,
                             "state": str(state), "residual": str(attained)},
        "scope": "This is a second, cover-independent continuum proof for the committed B and A, not an optimal margin over all certificates.",
    }


def verify_geometry():
    require(all(dot(a, a) == 1 for a in NORMALS), "Normals must be unit")
    vertices = poly_vertices()
    max_norm_sq = max(dot(z, z) for z in vertices)
    require(len(vertices) == 12, "Unexpected polygon vertices")
    require(max_norm_sq == Q(2, 5) < (R+EPS)**2,
            "Polygon is outside the certified source tube")
    # For every convexified pair t1=s1/2+s2/4 and
    # 0 <= t2 <= (9/16)s2. Cauchy--Schwarz yields the Frobenius bound.
    q = Q(13, 16)
    require(Q(1, 2)**2+Q(1, 4)**2+Q(9, 16)**2 == Q(161, 256)
            <= q*q, "Convexified contraction bound failed")
    initial_norm_bound = Q(1, 4)+Q(1, 16)
    require(initial_norm_bound+EPS < R, "Initial tube not contained")
    robust_successor_bound = q*(R+EPS)+EPS
    require(robust_successor_bound == Q(37, 64) < R,
            "Robust body inclusion failed")
    require(XI_T+ROW_CAP*XI_S == Q(1, 32) < EPS,
            "Source/successor error budget failed")
    # Mesh spacing 1/80, nearest-node distance <= 1/160.
    require(NODES[0] == -1 and NODES[-1] == 1
            and all(y-x == Q(1, 80) for x, y in zip(NODES, NODES[1:])),
            "State cover failed")
    require(Q(5) <= 3**2 and Q(13, 4) <= 2**2,
            "Derivative bounds failed")
    # The derivative bounds are ||phi'||^2<=5 and
    # ||(phi o f)'||^2 <= 1*(1+4*(3/4)^2)=13/4 on [-1,1].
    require(XI_S == 3*Q(1, 160) and XI_T == 2*Q(1, 160),
            "Feature cover radii failed")
    # Generic sphere-packing component bound for r=2 and alpha=0.
    scale = 32*R/EPS
    generic_bound = 1+(1+scale)**2-(scale-1)**2
    require(generic_bound == 1537, "Generic component bound failed")
    # Projection construction: delta_s^2=R*EPS/4, alpha<=EPS/16.
    projection_spacing_sq = R*EPS/4
    projection_support_error = EPS/16
    projection_error_bound = projection_spacing_sq/(2*R)+6*projection_support_error
    require(projection_spacing_sq <= R*R/4
            and projection_error_bound == EPS/2,
            "Projection approximation error budget failed")
    # For r=2 the packing expression is 32*sqrt(R/EPS);
    # certify its ceiling as 111 without floating-point square roots.
    require(Q(110)**2 < 1024*R/EPS < Q(111)**2,
            "Projection component ceiling failed")
    return {
        "convexified_relation_contraction_bound": str(q),
        "initial_feature_norm_bound": str(initial_norm_bound),
        "robust_body_radius": str(R),
        "feature_robustness_radius": str(EPS),
        "robust_successor_norm_bound": str(robust_successor_bound),
        "robust_inclusion_gap": str(R-robust_successor_bound),
        "generic_component_upper_bound": int(generic_bound),
        "projection_component_upper_bound": 112,
        "projection_support_error_cap": str(projection_support_error),
        "projection_outer_error_bound": str(projection_error_bound),
        "used_components": len(NORMALS),
        "polygon_vertex_count": len(vertices),
        "maximum_polygon_vertex_squared_norm": str(max_norm_sq),
        "polygon_vertices": [[str(v) for v in z] for z in vertices],
        "state_cover_nodes": len(NODES),
        "state_cover_radius": "1/160",
        "source_feature_error_bound": str(XI_S),
        "successor_feature_error_bound": str(XI_T),
        "row_sum_cap": str(ROW_CAP),
        "combined_feature_error_budget": str(XI_T+ROW_CAP*XI_S),
    }


def verify_scope_examples():
    # Physical robust safety for f=x^2, despite an unsafe fixed point.
    require(Q(1, 2)**2+Q(1, 8) == Q(3, 8) <= Q(1, 2),
            "Physical invariant bound failed")
    require(-Q(1, 8) >= -Q(1, 2), "Physical lower bound failed")
    require(Q(1, 4)**2-Q(1, 2) == -Q(7, 16), "Initial margin failed")
    require(Q(3, 4)**2-Q(1, 2) == Q(1, 16), "Unsafe margin failed")
    require(Q(1)**2 == 1, "Unsafe fixed point failed")
    # Nonlinear positive example is not globally one-step unsafe-avoiding.
    require(f(Q(1)) == Q(3, 4) and Q(7, 10) <= f(Q(1)) <= Q(4, 5),
            "Unsafe transient failed")
    require(f(f(Q(1))) == Q(33, 64) < Q(7, 10),
            "Uniform two-step unsafe avoidance upper bound failed")
    return {
        "physical_counterexample": {
            "map": "x^2", "physical_disturbance_radius": "1/8",
            "invariant_interval": ["-1/2", "1/2"],
            "disturbed_image_interval": ["-1/8", "3/8"],
            "ordinary_comparison_matrix": [["1"]],
            "initial_margin": "7/16", "unsafe_anchor_margin": "1/16",
            "unsafe_fixed_point": "1",
            "strict_class_exclusion": "all degrees and finite component counts; analytic corollary",
        },
        "nonlinear_positive_example": {
            "unsafe_first_successor_of_one": "3/4",
            "largest_second_successor_on_domain": "33/64",
        },
    }


def replay(matrix):
    geometry = verify_geometry()
    lp = validate_matrix(matrix)
    global_polynomial = verify_global_polynomials(matrix)
    return {
        "status": "EXACT_CONSTRUCTIVE_EVIDENCE_VERIFIED",
        "arithmetic": "fractions.Fraction; no floating point in replay",
        "example": {"X": ["-1", "1"], "X0": ["-1/4", "1/4"],
                    "Xu": ["7/10", "4/5"], "map": "x/2 + x^2/4",
                    "features": ["x", "x^2"], "degree_bound": 2},
        "geometry": geometry, "finite_lp": lp,
        "independent_global_polynomial_certificate": global_polynomial,
        "certificate_margins": {"initial_lower_bound": "23/80",
                                "unsafe_anchor_lower_bound": "1/10",
                                "global_propagation_lower_bound": str(ETA)},
        "scope_examples": verify_scope_examples(),
        "limit": "The example has both a proved Lipschitz paired-cover argument and an independent exact Bernstein polynomial certificate. Affinity extends the graph inequalities to convex mixtures. General theorems are not machine-checked.",
    }


def discover():
    import numpy as np
    from scipy.optimize import linprog
    discovery_margin = Q(1, 80)
    sources = [beta(phi(x)) for x in NODES]
    successors = [beta(phi(f(x))) for x in NODES]
    constraints = [[float(XI_S-v) for v in s] for s in sources]
    constraints.append([1.0]*len(NORMALS))
    matrix = []
    for i in range(len(NORMALS)):
        rhs = [float(-discovery_margin-XI_T-t[i]) for t in successors]
        result = linprog(np.ones(len(NORMALS)), A_ub=np.array(constraints),
                         b_ub=np.array(rhs+[float(ROW_CAP)]),
                         bounds=(0, None), method="highs")
        require(result.success, f"LP discovery failed for row {i}")
        row = [Q(float(v)).limit_denominator(1000000) for v in result.x]
        matrix.append(row)
    # Floating-point solver output is never accepted without exact checks.
    replay(matrix)
    return matrix


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true",
                        help="Propose A with SciPy, exactly validate, then save")
    args = parser.parse_args()
    if args.discover:
        matrix = discover()
        payload = {"construction": "12 unit supporting directions, offset 3/5",
                   "normals": [[str(v) for v in a] for a in NORMALS],
                   "A": [[str(v) for v in row] for row in matrix]}
        MATRIX_FILE.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
    else:
        payload = json.loads(MATRIX_FILE.read_text(encoding="utf-8"))
        require(payload["normals"] == [[str(v) for v in a] for a in NORMALS],
                "Committed normal ordering changed")
        matrix = [[Q(v) for v in row] for row in payload["A"]]
    report = replay(matrix)
    REPORT_FILE.write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
