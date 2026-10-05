# Coauthor review and a TAC research program

## What to ask Majid to assess first

The scientific question is whether more functions can overcome the conservatism of global constant-comparison inequalities at fixed polynomial degree. The note gives a finite-dimensional way to identify one intrinsic source of failure: convexified transitions in monomial feature space. Every degree-d vector of polynomials is a linear map of those features, so a valid moment transition is invisible to all choices of its coefficients and all finite vector sizes.

The exact example meets the requested quadratic target and strengthens it to a degree-3 impossibility result. It also closes the upper bound with a scalar quartic VBC. The supplied SCL example established a degree-1 obstruction and a quartic upper bound without claiming quartic minimality. The new example establishes exact minima for its own system and sets; it does not improve the degree bound for the old system by assumption.

Ask for review of:

1. The equivalence between global comparison and convexified orthant preservation, including compactness, continuity, strict feasibility, and attained row multipliers.
2. The scope of the moment obstruction, especially fixed-anchor rather than pointwise unsafe separation.
3. The explicit 2-versus-4 degree gap and the open parameter family.
4. Whether a robust converse for the feature-space relation could be the main TAC theorem.

## Precise result status

| Item | Status in this package | What remains |
| --- | --- | --- |
| Fixed-B comparison characterization | Proof supplied; classical convex-duality mechanism | Independent review and priority comparison |
| Prescribed-degree, arbitrary-component obstruction | Proof supplied for finite atomic measures | Practical extraction for larger examples; characterize its limitations |
| Exact scalar quadratic/cubic separation | Analytical proof and rational replay | Coauthor review |
| Exact VBC minimum degree 4 | Explicit quartic witness plus degree-3 obstruction | Coauthor review |
| Parameter family | Proof supplied with open strict parameter bounds | Test additional families beyond an invariant scalar axis |
| Multi-step lifted obstruction | Proof in the technical note | Efficient support refinement and stopping conditions |
| Unknown-vector completeness | Not established | Robust invariant-polyhedron existence theorem |
| General pointwise-separation VBC exclusion | Not established | A different obstruction or direct proof |
| More implication-IBC frames helping at fixed degree | Not established by this example | Construct an independent memory/frame-count example |
| Switched-system extension | Not established | Address mode quantifiers and graph composition after autonomous results |

## Why the first theorem alone is not enough

The fixed-B theorem is a finite-dimensional convex-alternatives result applied to the convex hull of certificate values. Horvath, Song, and Terlaky already connect invariance with nonnegative multipliers under convexity/concavity assumptions. A reviewer may reasonably view the general fixed-B characterization as an explanatory reformulation rather than the main breakthrough. The more distinctive proposed contribution is the coefficient-independent obstruction to an entire degree-limited certificate class, paired with exact minimum-degree separations and a formulation diagnosis method.

Moment and occupation-measure techniques themselves are established. Do not claim that lifting to moments, using Farkas duality, or comparing certificate structures is new. The proposed novelty must be checked at the intersection of these techniques: fixed polynomial degree, arbitrary finite component count, constant nonnegative global comparison, and exact implications-versus-comparisons separation.

The example uses one implication frame. It is an ordinary invariant barrier with sign implication, represented as an IBC with m=1. It shows that the comparison propagation inequality can impose an unnecessary degree increase. It is not evidence that interpolation chains add expressive power in this example.

## Main theorem target: robust feature-space converse

Let K_d be the convex hull of degree-d monomial feature vectors on X. Let F_d be the convex hull of the lifted transition graph. A finite degree-d vector is a finite collection of affine halfspaces on the constant-coordinate slice of feature space.

The fixed-vector theorem implies: strict initial inclusion, a fixed unsafe separating facet, and invariance of the feature polyhedron under F_d are equivalent to a VBC with those polynomial components. This gives an exact existence reformulation, but not yet a constructive finite algorithm.

The next substantial goal is a theorem that guarantees a finitely faceted invariant feature polyhedron when the abstract relation has a robust safe invariant region. Explicit assumptions would need to address:

- A positive distance from initial feature points to the boundary of the invariant region.
- An unsafe feature set separated by a single affine functional, as required by the anchor definition.
- A stability or contraction property of the relation, or a strict invariance margin sufficient for polyhedral approximation.
- Behavior at fixed points and neutral boundaries: compactness alone does not justify a strict invariance margin.
- Whether row multipliers can be chosen with quantitative bounds when perturbations are considered.

Do not assume such a converse for arbitrary compact polynomial systems. Derive the assumptions and prove them. A useful outcome could be a conditional completeness theorem for refinement in a fixed monomial feature space, together with a witness proving when that refinement cannot succeed.

## Diagnosis algorithm to develop

1. Choose the degree and verification domain before optimizing certificate coefficients.
2. Search for an atomic one-step or multi-step moment obstruction.
3. Use exact support membership and rational identities to accept a discovered obstruction.
4. If accepted, stop increasing the VBC component count at that degree. Try implication propagation, change the model/domain only when justified by the verification task, or increase degree.
5. If no obstruction is discovered, keep the outcome inconclusive and continue synthesis or refine supports.
6. For a candidate B, search for a probability mixture violating expected orthant preservation. This diagnoses its global-comparison gap directly.
7. Report theorem-backed exclusions, exact positive certificates, numerical candidates, and inconclusive searches separately.

Finite-grid LP discovery is implemented. General semialgebraic moment-SOS extraction, an implication-IBC synthesizer, and a complete refinement loop are not implemented in this package.

## Coupled higher-dimensional family to examine

A direct embedding uses x+=f(x), y+=rho*y on [-1,1] times a transverse box, with |rho|<=1. Initial and unsafe sets are products of the scalar sets with transverse boxes containing zero. Any multivariate degree-at-most-3 VBC restricted to the invariant axis y=0 would contradict the scalar obstruction. The scalar quadratic and quartic witnesses lift unchanged.

A more coupled construction uses

    x+ = x[1+c(y)(x^2-r^2)(1-x^2)],   y+ = rho*y,

where c(y) is polynomial, is uniformly positive, lies strictly below both parameter bounds from the scalar family, and c(0)=1/2 when r=1/2. The axis remains invariant, so the scalar nonexistence proof still applies. The same sign and monotonicity arguments establish the quadratic implication and quartic global propagation uniformly in y. Initial and unsafe conditions remain functions of x only. This is a structured family with an embedded obstruction; it should not be marketed as a challenging application benchmark without additional evidence.

## Closest-work reading agenda

- **Horvath--Song--Terlaky:** distinguish Theorem 3.1's global inequalities and concavity assumptions from Theorem 5.1's inequalities restricted to the invariant polyhedron. The latter admits a zero matrix and therefore cannot establish the VBC inequality on a larger X.
- **Bogomolov--Frehse--Giacobbe--Henzinger:** understand the local completeness and convex interpolation conditions that permit adding template directions. The present witness arises from a propagation relaxation rather than a missing physical-space facet. Their hybrid model and time-elapse abstraction differ from the autonomous map here.
- **Anand--Jungers--Zamani--Allgower:** distinguish graph soundness/ordering from template-degree completeness. A constant-comparison matrix has summed row coupling, so graph simulation results cannot automatically be transferred to all VBC matrices.
- **Sogokon--Ghorbal--Tan--Platzer:** separate continuous-time comparison systems and their Metzler/off-diagonal conditions from discrete-time entrywise nonnegative matrices.
- **Oumer--Murali--Trivedi--Zamani:** check the original IBC formulation and relevant degree/frame-count examples before claiming novelty for implications.
- **Korda--Henrion--Jones and moment/SOS literature:** compare finite-degree obstructions, occupation-measure duality, representability, and invariant-set approximation. The obstruction here is not an occupation measure proving a true unsafe trajectory.
- **Polynomial-template lower-bound and invariant-barrier synthesis literature:** review scalar and vector nonexistence claims carefully. A fixed template or chosen SOS degree is different from all polynomial vectors of a fixed degree with unbounded finite component count.

The targeted web review found related continuous-time invariant-barrier and SDP-completeness work beyond the three suggested references. This package does not claim that those entire literatures were exhausted. Check for prior versions, revised manuscripts, and unpublished work known to collaborators before claiming first results.

## Expansion gates

Gate 1: coauthor agreement on the definitions, the three proposed theorems, and novelty scope.

Gate 2: a substantial converse/characterization or a provably effective obstruction hierarchy, with explicit assumptions and limitations.

Gate 3: exact separations beyond the structured scalar axis, plus reproducible comparisons under matched degree, domains, margins, and synthesis budgets.

Gate 4: write a TAC manuscript around the proven final contribution. Add switching or data-driven extensions only if they deepen the result without obscuring the autonomous safety theorem.

No gate is a guarantee of acceptance, and no paper or email has been submitted or sent.
