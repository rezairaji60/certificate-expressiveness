# Archived manuscript outline

Prepared October 25, 2026, in response to Majid's October 23 remaining points.

Implemented as the complete [IEEE journal manuscript](../paper/manuscript.pdf) on October 26, 2026. This outline is historical; the manuscript, its source, and [current audit](MANUSCRIPT_CHECKS.md) are the current review materials.

Working title: **Structural Conservatism of Discrete-Time Barrier Certificates:
Moment Obstructions, a Schur-Stable Converse, and Exact Degree Separations**.

## Central question

At prescribed polynomial degree, when can adding functions repair a safety
certificate, and when must the degree or the propagation conditions change?

The contribution is a collection of proved, scoped answers. It is not a
complete decision procedure for all certificate formulations. IBC means
interpolation-inspired barrier certificate.

## 1. Problem, classes, and precise claims

- Autonomous deterministic discrete-time safety on a compact invariant domain.
- Polynomial degree means total degree at most d.
- Constant entrywise nonnegative comparison matrices; fixed unsafe anchor.
- Scalar versus vector comparisons, and implication-style IBCs.
- Distinguish ordinary matrices with rho(A)=1 from the Schur subclass.
- Earlier moment results permit forward/backward definitions; the robust
  converse and the new nonlinear scalar/vector tradeoff concern the forward class.
- Explain what is proved before discussing potential impact or novelty.

## 2. Convexification and obstructions independent of component count

State the fixed-family comparison characterization using convexified
certificate-value transitions and strict source feasibility.
Present the prescribed-degree moment obstruction for every finite number
of components and any nonnegative constant comparison matrix.

Show actual finitely supported probability measures, correct set support,
and exact input/successor moment equalities.
A witness concerns averages and need not describe an unsafe trajectory.
The criterion is sufficient, not established necessary.

## 3. Schur-stable prescribed-degree converse

Define the monomial lift, relative affine geometry, convexified transition
relation, and repeated convexification of reachable sets.
Use independent source/successor feature errors, with constants kept as offsets.

Prove equivalence of positive-radius robust convexified-feature separation,
a finite same-degree fixed-anchor certificate with strict propagation, and
an ordinary certificate with rho(A)<1.
Include finite facet selection, attained row duality, and constant shifts.
Derive uniform eventual avoidance from the entire verification domain and
the onto/unsafe-periodic obstructions.
Do not imply that physical state robustness supplies the feature premise.

## 4. Conditional finite certificate extraction

Input: a supplied convex body C with certified initial inclusion,
robust relational invariance, unsafe separation, geometry/support information,
and an exact paired cover of the nonlinear feature graph.
Output: finitely many degree-bounded functions and a global nonnegative
comparison matrix with certified separation and propagation margins.

Credit classical support approximation, Dudley's exponent, and
approximation within a dynamical margin.
Give the explicit count and the finite row LP, accounting for both cover errors.
Specify real-algebraic/oracle assumptions for finite termination.
Do not claim automatic discovery of C or practical efficiency in general.

## 5. Nonlinear recovery through functions or degree

Proposition: any continuous map uniformly within delta<1/20 of (9/10)Rx
on the unit disk has no scalar affine certificate, while four affine
functions work. The proof covers every scalar multiplier, not a solver search.

Use the explicit cubic family
f_theta=(9/10-theta*(1-||x||²))Rx, 0<theta<=1/40.
The same four affine functions work at degree one, and one scalar quadratic
works at degree two.
Hence minimum forward scalar comparison degree =2; minimum degree with
any finite vector =1. Do not claim the optimal affine vector component count.

Show full convexified transitions and independent feature errors explicitly.

## 6. Exact obstruction and a different kind of degree gap

The original scalar nonlinear system admits a quadratic single-frame
implication IBC. An exact moment witness excludes every finite fixed-anchor
constant-comparison VBC of degree at most three.
A quartic ordinary comparison certificate works with A=[1].

Explain the exact minimum degrees two and four for these different
propagation classes and retain the open parameter family from the first note.
The quartic certificate has rho(A)=1, so it does not follow from the Schur
converse. The obstruction cannot be bypassed merely by adding functions.

## 7. Reproducibility, theorem-specific comparisons, and conclusions

Keep the x/2+x²/4 twelve-component example as a supplied-body extraction
validation, with the scalar affine baseline b=x-3/5, A=1/2 prominently included.
It does not show an advantage of more functions or degree.

Use exact probability/moment checks, interval identities, multivariate
polynomial factors, paired-cover budgets, and the independent Bernstein proof.
Separate discovery from proof and avoid interpreting finite-grid
infeasibility as universal nonexistence.

Compare the existence theorem to HST Theorem 3.10/Remark 3.11, Liu Theorem 30,
and HSCC 2024 Theorem 3.5/Corollary 5.2.
Compare conditional extraction to Har-Peled–Jones Theorem 1.4, Alessio et al.
Theorem 4, Berger–Sankaranarayanan Propositions 13/15/19 and Theorem 21,
their Section 9 discrete-time discussion, and HSCC 2024 Algorithms 2–6.
The revised technical note gives exact assumption/conclusion differences.

## What the results establish

| Situation | Proved implication |
| --- | --- |
| Robust convexified-feature separation at degree d | A finite degree-d Schur fixed-anchor VBC exists. |
| Supplied certified body and effective geometric/cover data | A finite certificate can be extracted, including a global matrix. |
| New nonlinear family at degree one | One function fails; four suffice; one quadratic is an alternative. |
| Original moment witness at degrees two and three | No finite number of comparison components can repair the certificate. |
| Original quadratic IBC versus quartic comparison | Changing propagation conditions can lower the minimum degree. |
| Ordinary rho(A)=1 certificate | May work outside the robust/Schur characterization. |

The first two positive results use explicit sufficient/equivalent premises;
failure to verify those premises is not a proof that a certificate is absent.
There is no complete automatic diagnosis or automatic robust-body discovery claim.

## Work that is not required before drafting

The general rho(A)=1 converse, optimal component counts, automatic discovery
of C, switched/control/data-driven extensions, and publication-priority
claims remain separate questions. Majid explicitly said the neutral-class
converse need not be solved before drafting.
