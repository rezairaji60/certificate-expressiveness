# Scope requested in Majid's email

## Core paper

The explicit starting point is autonomous deterministic discrete-time systems and safety verification, with the certificate definitions and verification-domain assumptions of the submitted VBC–IBC manuscript. The three objectives concern barrier certificates:

1. A sufficient condition excluding prescribed-degree polynomial constant-comparison VBCs for every finite component count and every entrywise nonnegative constant comparison matrix.
2. A characterization of when invariance of the set defined by a specified polynomial vector B implies a constant global comparison matrix.
3. Exact higher-degree separations, beginning with a quadratic implication IBC and analytical quadratic VBC nonexistence.

The prepared technical note treats the submitted paper's fixed-anchor VBC definition explicitly. Its example supplies a stronger degree-three exclusion and an exact quartic upper bound within that class. It does not claim an exclusion for the broader pointwise unsafe-separation definition.

## Role of closure certificates

Majid's reference to building on three papers supplies research context. It does not require that this first-stage safety paper contain new closure-certificate results. Prior closure-certificate work belongs in the introduction and related-work discussion, especially when explaining propagation structures and transition-invariant reasoning.

Barrier certificates use functions of individual states, B_i(x). Closure certificates use functions of state pairs, C_i(x,y), to represent transition-invariant or reachability information. The general statements in this package concern the former. A state-pair formulation would require a new feature lift, its own propagation/composition relation, explicit endpoint separation assumptions, and new soundness and obstruction proofs.

A moment witness involving input and successor distributions is not itself a closure certificate, nor does its existence automatically extend a VBC obstruction theorem to closure certificates. Similarly, a multistep moment obstruction remains a theorem about the stated barrier class unless a separate relational-certificate definition is introduced.

## Expansion rule

Keep barrier characterizations and exact degree separations as the main mathematical contribution. Include a closure-certificate extension only after it provides a proved, substantive addition and is agreed with Majid. His email presents switched-system extensions as a later possibility as well; they are not part of the initial autonomous scope.

The project name **Certificate Expressiveness** accommodates those later extensions without committing the current paper to them. The working paper title remains **Structural Conservatism of Discrete-Time Barrier Certificates: Characterization and Degree Separations**.

## Converse stage

The October 21 revision incorporates the spectral-radius characterization and
scope restrictions identified in Majid’s comments on the October 12 note.
Robust convexified-feature separation is equivalent to finite forward fixed-anchor
VBCs with constant nonnegative Schur-stable matrices, ρ(A)<1, or to uniformly
strict global propagation. It does not characterize the ordinary boundary
ρ(A)=1. Onto maps and unsafe periodic points exclude the strict class at every
degree, including the original nonlinear map with a valid ordinary quartic VBC.

The constructive strengthening supplies a coarse component bound and a feasible
finite row LP from a certified chosen body, geometry/support bounds, and paired
source/successor feature-cover errors. A nonlinear exact rational example verifies
these conditions on the full convexified relation. Effective body discovery
and a general neutral-class converse remain open.

See [CONVERSE_SCOPE.md](CONVERSE_SCOPE.md),
[the revision audit](REVISION_CHECKS.md), and
[the revised note](../paper/converse.pdf).
