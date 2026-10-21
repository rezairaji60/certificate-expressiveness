# Certificate Expressiveness

Research drafts prepared for Reza Iraji and Majid Zamani.
Repository: [rezairaji60/certificate-expressiveness](https://github.com/rezairaji60/certificate-expressiveness) (public).
Latest converse revision: October 21, 2026, incorporating Majid’s detailed comments.

Theory and reproducible computations for the expressiveness, structural conservatism, and polynomial degree requirements of dynamical-system verification certificates.

This repository contains the initial degree-separation note and the subsequent candidate converse requested by Majid. These are research drafts for review. The converse now includes a conditional finite construction from certified body and cover data; discovery of those data and publication-level novelty remain open.

## Latest note: Schur-stable fixed-anchor certificates

[Read the revised converse PDF](paper/converse.pdf) or [open its self-contained Overleaf source](paper/converse.tex).

At a prescribed total degree bound, robust separation of the convexified monomial dynamics is equivalent to a finite forward fixed-anchor VBC with a constant nonnegative **Schur-stable** comparison matrix, ρ(A) < 1. This is exactly the class that can be shifted to have a uniform strict global propagation margin. Both transition pairs and reachable feature sets are convexified.

This class forces uniform eventual unsafe avoidance from the entire verification domain. Onto maps and unsafe periodic points exclude it at every degree and component count. The original quartic recovery remains valid as an ordinary certificate with ρ(A) = 1; this converse does not explain that recovery.

The new constructive result gives a coarse explicit component bound from a certified convex invariant body and a feasible finite row LP with separate source and successor feature-error budgets. A nonlinear example uses 12 quadratic components, 161 exact cover nodes, and certified margins 23/80 (initial), 1/10 (unsafe anchor), and 1/100 (global propagation). Exact replay validates the finite LP and rational geometry; the continuum conclusion uses the proved cover and derivative bounds. Twelve is not claimed minimal.

The rotation still proves that one affine component is impossible while four succeed; the moment witness still excludes every finite quadratic or cubic fixed-anchor VBC. Physical robust safety alone does not imply the feature-space hypothesis.

See [scope and reproduction](docs/CONVERSE_SCOPE.md) and [the revision audit](docs/REVISION_CHECKS.md). Classical multiplier, approximation-within-margin, and finite LP mechanisms are attributed explicitly; novelty of the combined theorem remains to be established.

## Current paper scope

The core study follows Majid's requested starting point: barrier certificates for autonomous deterministic discrete-time safety verification. It compares fixed-anchor constant-comparison VBCs with interpolation-inspired barrier certificates (IBCs) using implication-style propagation at prescribed polynomial degree. Closure certificates inform the related-work discussion and remain a possible later extension requiring separate definitions and proofs. See `docs/RESEARCH_SCOPE.md`.

Working manuscript title: **Structural Conservatism of Discrete-Time Barrier Certificates: Characterization and Degree Separations**. The technical note retains its original title.

## Main proposed results

1. For a **fixed** continuous vector B on a compact invariant verification domain, with one strictly negative feasible point, a constant entrywise nonnegative comparison matrix exists if and only if the convex hull of `(B(x), B(f(x)))` preserves the nonpositive orthant. A violating distribution needs at most m+2 atoms.
2. Matching input and successor monomial moments to initial and unsafe distributions provides a sufficient obstruction to **every fixed-anchor VBC of prescribed degree**, regardless of the finite number of functions and the constant nonnegative comparison matrix. The proof covers forward and backward definitions.
3. An explicit invariant-domain polynomial system and a parameter family have minimum implication-IBC degree 2 and minimum fixed-anchor constant-comparison VBC degree 4. A rational moment witness excludes all degree-at-most-3 VBCs; a quartic scalar certificate establishes the upper bound.
4. Under compactness and continuity, robust convexified-feature separation is equivalent to existence of a degree-bounded forward fixed-anchor VBC with a constant nonnegative Schur-stable comparison matrix, and to strict global propagation. Ordinary certificates on compact invariant domains necessarily satisfy ρ(A) ≤ 1; the neutral boundary class ρ(A) = 1 is outside this converse.
5. A certified robust convex body and geometric bounds give an explicit component bound. Exact graph nodes with a certified paired cover yield feasible finite LPs that preserve the initial, unsafe-anchor, and global propagation margins after both feature errors are charged. This is conditional on certified body/support/cover information, rather than an automatic discovery algorithm.

The IBC witness uses a **single frame**, so it is also an ordinary scalar sign-inductive barrier. This example isolates the propagation-rule gap; it does not demonstrate a benefit from adding IBC frames. The exclusion is scoped to the submitted paper's fixed-anchor definition. A general VBC may use different unsafe separating components at different states; that broader class is not excluded by this proof.

## Contents

- `paper/note.pdf`: technical note, six pages of main text plus references.
- `paper/note.tex`: editable pdfLaTeX source, including all proofs and references.
- `paper/converse.pdf`: revised converse and constructive note, October 21, 2026.
- `paper/converse.tex`: self-contained Overleaf source for the converse note.
- `src/exact_verify.py`: dependency-free rational evidence replay and polynomial checks.
- `src/exact_verify_converse.py`: exact affine comparison, robustness-bound, and moment-witness replay for the converse examples.
- `src/constructive_converse.py`: dependency-free exact replay of the nonlinear finite construction; optional SciPy `--discover` proposes a matrix and then exactly verifies it.
- `src/search_witness.py`: finite-support LP discovery with exact rational reconstruction.
- `src/plot_geometry.py`: illustrative figure generation; not proof evidence.
- `tests/test_evidence.py`: exact replay and invalid-witness rejection checks.
- `tests/test_constructive.py`: exact continuum-certificate replay and rejection of corrupted matrices or understated feature-cover errors.
- `evidence/exact_report.json`: rational weights, moments, margins, and Bernstein coefficients.
- `evidence/converse_report.json`: exact comparison matrix, strict margins, robust square bound, and moment identities for the converse note.
- `evidence/nonlinear_comparison_matrix.json`: rational 12-component matrix and ordered facet normals.
- `evidence/constructive_converse_report.json`: exact polygon geometry, paired-cover error budget, finite LP slacks, and strict margins.
- `evidence/lp_discovery.json`: solver discovery results, clearly separated from exact evidence.
- `docs/RESEARCH_ROADMAP.md`: novelty boundaries and a staged TAC research program.
- `docs/SOURCE_MANIFEST.json`: checksums of the five supplied PDFs; their contents are not redistributed.
- `docs/CONVERSE_SCOPE.md`: converse assumptions, limitations, and reproduction instructions.

## Reproduce the exact evidence

Python 3.10 or later, with no external dependencies:

```sh
python src/exact_verify.py
python src/exact_verify_converse.py
python src/constructive_converse.py
python -m unittest discover -s tests -v
```

Expected statuses are `EXACT_EVIDENCE_VERIFIED`, `EXACT_FINITE_EVIDENCE_VERIFIED`, and `EXACT_CONSTRUCTIVE_EVIDENCE_VERIFIED`. All 11 tests should pass.
GitHub Actions runs all three replays and all tests, then checks that their JSON reports match the committed files.
Do not run with `python -O`, which disables assertions; the verifier rejects that mode.

Optional discovery and figures:

```sh
python -m pip install -r requirements-optional.txt
python src/search_witness.py
python src/constructive_converse.py --discover
python src/plot_geometry.py
```

Compile the note from `paper/`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error note.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error converse.tex
```

The proof never infers nonexistence from solver infeasibility. Discovery at degrees 1, 2, and 3 passes exact reconstruction; degree-4 infeasibility concerns only the selected support grid. The theorem and the explicit quartic witness establish the exact minimum VBC degree. No SOS solver experiment was run.

## Scientific limits and review

- The compactness and strict-feasibility assumptions in the fixed-vector characterization are additions to the base definitions and are stated explicitly.
- The general moment obstruction is sufficient, not claimed necessary for existence of an unknown VBC.
- The converse equivalence covers exactly the Schur-stable fixed-anchor class. Its uniform eventual-avoidance consequence excludes onto maps and unsafe periodic points. Ordinary certificates with ρ(A) = 1 can still exist.
- Additive physical robust safety does not imply robustness of the convexified feature relation; the nonidentity map x² supplies an exact counterexample.
- Strict margins permit rational coefficient approximation as an existence statement. The new component bound and finite LP are constructive only with the stated certified body, geometry, support, and paired-cover information; they do not discover a suitable body automatically.
- A feasible moment-SOS relaxation may contain pseudomoments; extract and verify actual measures before using it as an obstruction.
- Exact rational replay validates this finite evidence. Human mathematical review is still needed for the general theorems, and a separate literature review is needed for priority.
- The parameter family is structurally persistent over its open parameter region, not proven robust to arbitrary model perturbations.
- Autonomous deterministic discrete-time safety is the scope. Switching, control, persistence, and data-driven extensions remain future work.
- The supplied submission labels the affine obstruction **Theorem 9**; item 10 is a scope remark. Check manuscript versions before changing references in correspondence.

See `docs/RESEARCH_ROADMAP.md` before expanding the paper.
