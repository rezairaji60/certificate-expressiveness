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
