"""Exact rational replay for the proposed degree separation. Python stdlib only.

This checks finite evidence and polynomial identities. The universal quantifiers
over component count and comparison matrices are justified in paper/note.tex.
"""
if not __debug__:
    raise RuntimeError("Exact verification requires Python without -O")

from fractions import Fraction as F
from math import comb
import json
from pathlib import Path


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else F(0)) +
                 (q[i] if i < len(q) else F(0))
                 for i in range(max(len(p), len(q)))])


def scale(p, c):
    return trim([c * x for x in p])


def mul(p, q):
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def power(p, n):
    out = [F(1)]
    for _ in range(n):
        out = mul(out, p)
    return out


def compose(p, q):
    out = [F(0)]
    for c in reversed(p):
        out = add(mul(out, q), [c])
    return out


def derivative(p):
    return trim([i * p[i] for i in range(1, len(p))] or [0])


def divide_exact(p, q):
    rem = trim(p)
    out = [F(0)] * max(1, len(p) - len(q) + 1)
    while len(rem) >= len(q) and any(rem):
        j, c = len(rem) - len(q), rem[-1] / q[-1]
        out[j] += c
        rem = add(rem, [F(0)] * j + scale(q, -c))
    if any(rem):
        raise ValueError("Nonzero remainder in exact polynomial division")
    return trim(out)


def evaluate(p, x):
    out = F(0)
    for c in reversed(p):
        out = out * x + c
    return out


def bernstein(p, lo=F(0), hi=F(1)):
    """Exact coefficients on [lo,hi]; nonnegative coefficients prove positivity."""
    q = compose(p, [lo, hi - lo])
    n = len(q) - 1
    return [sum((q[j] * F(comb(k, j), comb(n, j))
                 for j in range(k + 1)), F(0)) for k in range(n + 1)]


def moments(atoms, degree, transform=lambda x: x):
    return [sum((w * transform(x) ** k for x, w in atoms), F(0))
            for k in range(degree + 1)]


def validate_witness(mu, mu0, nu, f, degree, a, u, v):
    for atoms in (mu, mu0, nu):
        if not atoms or any(w < 0 for _, w in atoms):
            raise ValueError("Witness weights must be nonnegative")
        if sum((w for _, w in atoms), F(0)) != 1:
            raise ValueError("Witness must have unit mass")
    if any(abs(x) > 1 for x, _ in mu):
        raise ValueError("Source support outside X")
    if any(abs(x) > a for x, _ in mu0):
        raise ValueError("Initial support outside X0")
    if any(not u <= abs(x) <= v for x, _ in nu):
        raise ValueError("Unsafe support outside Xu")
    if moments(mu, degree) != moments(mu0, degree):
        raise ValueError("Initial moments do not match")
    if moments(mu, degree, f) != moments(nu, degree):
        raise ValueError("Successor moments do not match")
    return True


def verify():
    r, c, a, t, v, kappa = F(1, 2), F(1, 2), F(12, 25), F(3, 4), F(103, 200), F(3, 10000)
    z, one_minus_z, z_minus_r2 = [0, 1], [1, -1], [-r*r, 1]
    hz = add([1], scale(mul(z_minus_r2, one_minus_z), c))
    fx = mul([0, 1], compose(hz, [0, 0, 1]))
    f = lambda x: evaluate(fx, x)
    u = a * f(t) / t
    theta = a*a/(t*t)
    mu = [(F(0), 1-theta), (-t, theta/2), (t, theta/2)]
    mu0 = [(-a, F(1, 2)), (a, F(1, 2))]
    nu = [(-u, F(1, 2)), (u, F(1, 2))]
    validate_witness(mu, mu0, nu, f, 3, a, u, v)
    # Show the witness is degree-limited, rather than claiming a degree-4 obstruction.
    assert moments(mu, 4)[4] != moments(mu0, 4)[4]
    assert 0 < a < r < u < v < 1
    # Domain proof: f' = 1/4 + (1-z)(5/8 + 5z/2) >= 1/4 on X.
    derivative_z = add([F(1, 4)], mul(one_minus_z, [F(5, 8), F(5, 2)]))
    assert derivative(fx) == compose(derivative_z, [0, 0, 1])
    assert f(-F(1)) == -1 and f(F(1)) == 1
    # h >= 7/8, and h-1 has sign z-r^2. Together these prove interval IBC invariance.
    assert min(bernstein(hz)) >= F(7, 8)
    assert add(hz, [-1]) == scale(mul(z_minus_r2, one_minus_z), c)
    ibc_initial, ibc_unsafe = r*r-a*a, u*u-r*r
    assert ibc_initial > 0 and ibc_unsafe > 0
    # Quartic p(z)=kappa-(z-r^2)^2.
    pz = add([kappa], scale(power(z_minus_r2, 2), -1))
    f_squared_z = mul(z, power(hz, 2))
    Q = add(divide_exact(add(f_squared_z, [-r*r]), z_minus_r2), [1])
    assert min(bernstein(Q)) > 0
    # p(x)-p(f(x))=c*z*(z-r^2)^2*(1-z)*(h+1)*Q >= 0 on X.
    product = scale(mul(mul(mul(mul(z, power(z_minus_r2, 2)), one_minus_z),
                            add(hz, [1])), Q), c)
    assert add(pz, scale(compose(pz, f_squared_z), -1)) == product
    vbc_initial = (r*r-a*a)**2-kappa
    vbc_unsafe = kappa-(v*v-r*r)**2
    assert vbc_initial > 0 and vbc_unsafe > 0
    # Fixed-B convexification violation, with B=x^2-r^2.
    assert moments(mu, 2)[2]-r*r < 0
    assert moments(mu, 2, f)[2]-r*r > 0
    return {
        "status": "EXACT_EVIDENCE_VERIFIED",
        "arithmetic": "Python fractions.Fraction; no floating-point proof steps",
        "parameters": {name: str(value) for name, value in
                       [("r", r), ("c", c), ("a", a), ("t", t), ("u", u), ("v", v), ("kappa", kappa)]},
        "witness": {name: [[str(x), str(w)] for x, w in atoms]
                    for name, atoms in [("mu", mu), ("mu0", mu0), ("nu", nu)]},
        "input_moments_0_to_3": list(map(str, moments(mu, 3))),
        "output_moments_0_to_3": list(map(str, moments(mu, 3, f))),
        "ibc_margins": {"initial": str(ibc_initial), "unsafe": str(ibc_unsafe)},
        "quartic_vbc_margins": {"initial": str(vbc_initial), "unsafe": str(vbc_unsafe)},
        "Q_power_coefficients": list(map(str, Q)),
        "Q_bernstein_coefficients_on_0_1": list(map(str, bernstein(Q))),
        "claims": {
            "implication_ibc_minimum_degree": 2,
            "fixed_anchor_constant_comparison_vbc_minimum_degree_either_direction": 4,
            "nonexistence_scope": "all finite m, all constant entrywise nonnegative A, degree <= 3",
            "novelty": "requires coauthor review and additional literature checking",
            "analytical_proofs": "paper/note.tex",
        },
    }


if __name__ == "__main__":
    report = verify()
    target = Path(__file__).resolve().parents[1]/"evidence"/"exact_report.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
