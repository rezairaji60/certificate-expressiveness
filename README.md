# Certificate Expressiveness

Research draft prepared for Reza Iraji and Majid Zamani, October 5, 2026.
Repository: `rezairaji60/certificate-expressiveness` (private during coauthor review).

Theory and reproducible computations for the expressiveness, structural conservatism, and polynomial degree requirements of dynamical-system verification certificates.

This package implements the first technical-note request in Majid's email. It does not claim an accepted paper, established priority, a complete synthesis procedure, or an exhaustive literature review.

## Current paper scope

The core study follows Majid's requested starting point: barrier certificates for autonomous deterministic discrete-time safety verification. It compares fixed-anchor constant-comparison VBCs with implication IBCs at prescribed polynomial degree. Closure certificates inform the related-work discussion and remain a possible later extension requiring separate definitions and proofs. See `docs/RESEARCH_SCOPE.md`.

Working manuscript title: **Structural Conservatism of Discrete-Time Barrier Certificates: Characterization and Degree Separations**. The technical note retains its original title.

## Main proposed results

1. For a **fixed** continuous vector B on a compact invariant verification domain, with one strictly negative feasible point, a constant entrywise nonnegative comparison matrix exists if and only if the convex hull of `(B(x), B(f(x)))` preserves the nonpositive orthant. A violating distribution needs at most m+2 atoms.
2. Matching input and successor monomial moments to initial and unsafe distributions provides a sufficient obstruction to **every fixed-anchor VBC of prescribed degree**, regardless of the finite number of functions and the constant nonnegative comparison matrix. The proof covers forward and backward definitions.
3. An explicit invariant-domain polynomial system and a parameter family have minimum implication-IBC degree 2 and minimum fixed-anchor constant-comparison VBC degree 4. A rational moment witness excludes all degree-at-most-3 VBCs; a quartic scalar certificate establishes the upper bound.

The IBC witness uses a **single frame**, so it is also an ordinary scalar sign-inductive barrier. This example isolates the propagation-rule gap; it does not demonstrate a benefit from adding IBC frames. The exclusion is scoped to the submitted paper's fixed-anchor definition. A general VBC may use different unsafe separating components at different states; that broader class is not excluded by this proof.

## Contents

- `paper/note.pdf`: technical note, six pages of main text plus references.
- `paper/note.tex`: editable pdfLaTeX source, including all proofs and references.
- `src/exact_verify.py`: dependency-free rational evidence replay and polynomial checks.
- `src/search_witness.py`: finite-support LP discovery with exact rational reconstruction.
- `src/plot_geometry.py`: illustrative figure generation; not proof evidence.
- `tests/test_evidence.py`: exact replay and invalid-witness rejection checks.
- `evidence/exact_report.json`: rational weights, moments, margins, and Bernstein coefficients.
- `evidence/lp_discovery.json`: solver discovery results, clearly separated from exact evidence.
- `docs/RESEARCH_ROADMAP.md`: novelty boundaries and a staged TAC research program.
- `docs/SOURCE_MANIFEST.json`: checksums of the five supplied PDFs; their contents are not redistributed.

## Reproduce the exact evidence

Python 3.10 or later, with no external dependencies:

```sh
python src/exact_verify.py
python -m unittest discover -s tests -v
```

Expected replay status: `EXACT_EVIDENCE_VERIFIED`. All five tests should pass.
Do not run with `python -O`, which disables assertions; the verifier rejects that mode.

Optional discovery and figures:

```sh
python -m pip install -r requirements-optional.txt
python src/search_witness.py
python src/plot_geometry.py
```

Compile the note from `paper/`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error note.tex
```

The proof never infers nonexistence from solver infeasibility. Discovery at degrees 1, 2, and 3 passes exact reconstruction; degree-4 infeasibility concerns only the selected support grid. The theorem and the explicit quartic witness establish the exact minimum VBC degree. No SOS solver experiment was run.

## Scientific limits and review

- The compactness and strict-feasibility assumptions in the fixed-vector characterization are additions to the base definitions and are stated explicitly.
- The general moment obstruction is sufficient, not claimed necessary for existence of an unknown VBC.
- A feasible moment-SOS relaxation may contain pseudomoments; extract and verify actual measures before using it as an obstruction.
- Exact rational replay validates this finite evidence. Human mathematical review is still needed for the general theorems, and a separate literature review is needed for priority.
- The parameter family is structurally persistent over its open parameter region, not proven robust to arbitrary model perturbations.
- Autonomous deterministic discrete-time safety is the scope. Switching, control, persistence, and data-driven extensions remain future work.
- The supplied submission labels the affine obstruction **Theorem 9**; item 10 is a scope remark. Check manuscript versions before changing references in correspondence.

See `docs/RESEARCH_ROADMAP.md` before expanding the paper.
