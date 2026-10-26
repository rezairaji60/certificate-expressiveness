# Schur-stable converse and certified finite construction

The October 25, 2026 revision is [paper/converse.pdf](../paper/converse.pdf).
Its self-contained [LaTeX source](../paper/converse.tex) compiles with pdfLaTeX
and can replace the main file in Overleaf.

## Exact class and assumptions

Fix total degree at most d. X is compact, f: X -> X is continuous,
and the nonempty compact initial and unsafe sets are disjoint.
The designated first component is positive on **every** unsafe state;
all components are strictly negative on the initial set.
The comparison matrix is constant and entrywise nonnegative.

The feature map contains all nonconstant monomials through d; affine offsets
represent constants. The graph of paired source/successor features is convexified,
and reachable feature sets are convexified at every iteration. Source and
successor errors are independent balls in the relative affine feature space,
and may leave the realizable monomial variety.

Theorem 1 proves equivalence of:

1. Positive-radius robust separation of that convexified feature closure.
2. A finite degree-bounded forward fixed-anchor VBC with a uniform strict
   global propagation margin.
3. An ordinary VBC in the same class with a Schur-stable matrix, ρ(A) < 1.

Every ordinary certificate under these compact-domain and strict-initial
assumptions has ρ(A) ≤ 1. The neutral boundary ρ(A) = 1 is not characterized
by the robust converse. Constant shifting interconverts items 2 and 3 without
changing the degree or number of functions.

## Stronger dynamical restriction

The strict class forces all trajectories from the entire verification domain
to become uniformly negative in the certificate functions after a common
finite time. Ordinary Schur-stable certificates have this property after
the constant shift, not necessarily in their original functions.
An unsafe periodic point or onto map excludes this entire class at all degrees
and finite component counts.

The original nonlinear degree-separation map is onto. Its ordinary quartic
certificate remains valid with A=[1], while no strict or Schur-stable certificate
exists at any degree. The new converse therefore does not explain quartic recovery.

Physical robust safety is different. For f=x², the initial interval [-1/4,1/4]
is safe against state disturbances of size 1/8 within [-1/2,1/2], yet the unsafe
fixed point 1 excludes the feature-robust/Schur-stable class at every degree.

## Quantitative and finite construction

Theorems 2 and 3 start with a **certified chosen convex body**, a feature
robustness radius epsilon, a fixed unit unsafe separator of margin gamma,
and geometry/support information. A sphere-net volume estimate gives

m <= 1 + ceil[(1+32 R/epsilon)^r - (32 R/epsilon-1)^r],

where r is the affine feature dimension and the body lies within radius R.
Support overestimation alpha <= min(epsilon/8, gamma/2) preserves the
unsafe margin and keeps the polyhedron in a source-error tube.

Section 4.1 adds a sharper projection construction. For exact Euclidean projections and support errors alpha <= min(epsilon/16,
gamma/2), it yields

m <= 1 + ceil[(1+8 sqrt(R/epsilon))^r - (8 sqrt(R/epsilon)-1)^r],

of order O_r((R/epsilon)^((r-1)/2)). This is an application of classical Dudley
geometry, with an explicit error proof; it is not a new approximation exponent.
The worked example's a priori bound improves from 1,537 to 112 with certified projection data. Feasible inexact projection points also suffice
when their supporting-normal gap sigma satisfies sigma+alpha<=epsilon/16. The twelve-component construction is unchanged.

A finite LP then extracts the nonnegative comparison rows. A certified paired
cover of exact graph nodes has errors xi_s and xi_t; the row-sum cap Lambda
charges xi_t + Lambda*xi_s against the propagation margin.
The LP is provably feasible under that budget, and its accepted matrix certifies
the entire continuum and full convexified relation. No numerical spectral
constraint is required; Schur stability follows analytically.

The note specifies support/cover/decision oracles and an admissible semialgebraic
representation. Compactness and continuity alone do not constitute an executable
algorithm. The procedure does not automatically find the body C.
Approximate node evaluations require additional certified errors; the stated
feasibility proof uses exact graph nodes.

## Nonlinear certificate and exact replay

For f=x/2+x²/4 on [-1,1], degree-two features contract on the **full**
convexified relation by a certified norm factor 13/16. The feature ball
C=(3/5)B with independent errors epsilon=1/20 has successor norm at most 37/64.
Twelve rational supporting directions meet the source-tube condition.

A 161-node exact paired cover uses source error 3/160 and successor error 1/80.
A sparse rational 12-by-12 matrix passes all finite LP inequalities with
minimum slack 1/400 at target propagation margin 1/100.
The initial margin is at least 23/80, unsafe-anchor margin at least 1/10,
and maximum row sum is 58/125 < 1. This supplied-body extraction example is not a function-count benefit: b=x-3/5, A=1/2 is a scalar affine certificate with margins 7/20, 1/10, 1/20. Its propagation margin exceeds 73/2500.

The replay additionally converts every global residual (AB)_i-B_i(f) into the
degree-four Bernstein basis on [-1,1], using exact rational arithmetic and no
cover nodes or Lipschitz bounds. The minimum of all 60 coefficients is 73/2500.
The first component at x=1 attains this value, proving the exact largest uniform
propagation margin for this fixed B,A. This second proof is independent of the
finite cover. The LP target remains 1/100 after accounting for cover errors.

From the repository root:

```sh
python src/exact_verify.py
python src/exact_verify_converse.py
python src/constructive_converse.py
python -m unittest discover -s tests -v
```

All replays use only the standard library. Do not run the older assertion-based
scripts with -O. There are 20 tests, including rejection of an erased anchor row,
negative matrix entries, and understated source or successor cover errors.
The new replay uses explicit exceptions and does not depend on assertions.
Tests also verify the sharp Bernstein margin and reject a margin just above
the exact endpoint value.

Optional discovery:

```sh
python -m pip install -r requirements-optional.txt
python src/constructive_converse.py --discover
```

SciPy proposes a matrix; rational reconstruction is accepted only after exact
verification. Solver status is not proof. Committed reports are deterministic.

## A nonlinear function-count and degree tradeoff

On the unit disk with initial radius 1/4 and unsafe point (3/4,0), any continuous
map f=(9/10)Rx+e with sup||e||<=delta<1/20 has no scalar affine certificate
for any nonnegative multiplier. At x_*=R^T*a/||a||, every possible affine
separator is negative while its successor value is positive.
Four affine functions +/-x_j-1/2 succeed with A=(9/10)Pi and strict margin
1/20-delta. This is an analytic proof over all scalar affine functions.

The cubic family f_theta=(9/10-theta*(1-||x||²))Rx, 0<theta<=1/40,
satisfies that assumption. The same four functions have uniform margin 1/40;
a scalar quadratic ||x||²-1/4 has multiplier 81/100 and margin 19/400.
Thus the minimum forward scalar comparison degree is exactly two and the
minimum finite-vector degree exactly one. The minimum vector count is not
proved; it lies between two and four.

All convexified pairs obey t=(9/10)Rs+e_bar with ||e_bar||<=1/40.
The square C=[-1/2,1/2]² has robust successor infinity norm <=247/500
for independent feature errors 1/100. Exact multivariate polynomial
coefficient/factor identities verify continuum propagation, without a grid.

## Literature and remaining questions

The revision explicitly compares HST Theorem 3.10 / Remark 3.11,
Liu Section IV / Theorem 30, Alessio et al. Theorem 4 and its subsequent
ellipsoidal construction, and Berger–Sankaranarayanan's finite LP synthesis
of polyhedral Lyapunov functions, including its Section 9 discrete-time extension discussion.
Theorem-specific comparisons now also cover the HSCC 2024 polynomial-cone
positive-system framework (Theorem 3.5, Corollary 5.2, Algorithms 2–6). The sharper projection count explicitly cites
Har-Peled–Jones, arXiv:1912.01977v3, for the classical Dudley mechanism.
Multiplier arguments, approximation within
a dynamical margin, and finite LP synthesis are established mechanisms.

Novelty of the combined fixed-feature equivalence and certified extraction
still requires assessment. A general converse at ρ(A)=1, effective discovery
of a suitable body, and useful sharper complexity bounds remain open here.
General theorem proofs and priority have not been independently or formally
verified.

The consolidated outline in MANUSCRIPT_OUTLINE.md organizes the established results for drafting. As Majid requested, the general neutral-class converse is not a prerequisite for drafting this paper.
