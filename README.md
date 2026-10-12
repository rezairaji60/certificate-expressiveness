# Certificate Expressiveness

Research drafts prepared for Reza Iraji and Majid Zamani.
Repository: [rezairaji60/certificate-expressiveness](https://github.com/rezairaji60/certificate-expressiveness) (public).
Latest reviewed converse note: October 12, 2026.

Theory and reproducible computations for the expressiveness, structural conservatism, and polynomial degree requirements of dynamical-system verification certificates.

This repository contains the initial degree-separation note and the subsequent candidate converse requested by Majid. These are research drafts for review; novelty assessment and a complete synthesis procedure remain open.

## Latest note: a robust converse at prescribed degree

[Read the reviewed converse PDF](paper/converse.pdf) or [open its self-contained Overleaf source](paper/converse.tex).

The candidate theorem relates robust safety of the convexified monomial transition relation to a finite fixed-anchor VBC of the prescribed degree with a uniform strict propagation margin. The proof includes mixtures of transition pairs and convex combinations of reachable feature vectors. The robustness condition is sufficient for ordinary fixed-anchor VBCs; equivalence is asserted only for the additional strict propagation margin.

The two analytical examples are a contracting rotation where four affine functions succeed while one cannot, and the moment obstruction excluding every finite quadratic or cubic fixed-anchor VBC. The note compares Horváth–Song–Terlaky's Theorem 3.10 and identifies related robust-converse and polyhedral-invariant work. See [the converse scope and reproduction guide](docs/CONVERSE_SCOPE.md).

## Current paper scope

The core study follows Majid's requested starting point: barrier certificates for autonomous deterministic discrete-time safety verification. It compares fixed-anchor constant-comparison VBCs with interpolation-inspired barrier certificates (IBCs) using implication-style propagation at prescribed polynomial degree. Closure certificates inform the related-work discussion and remain a possible later extension requiring separate definitions and proofs. See `docs/RESEARCH_SCOPE.md`.

Working manuscript title: **Structural Conservatism of Discrete-Time Barrier Certificates: Characterization and Degree Separations**. The technical note retains its original title.

## Main proposed results

1. For a **fixed** continuous vector B on a compact invariant verification domain, with one strictly negative feasible point, a constant entrywise nonnegative comparison matrix exists if and only if the convex hull of `(B(x), B(f(x)))` preserves the nonpositive orthant. A violating distribution needs at most m+2 atoms.
2. Matching input and successor monomial moments to initial and unsafe distributions provides a sufficient obstruction to **every fixed-anchor VBC of prescribed degree**, regardless of the finite number of functions and the constant nonnegative comparison matrix. The proof covers forward and backward definitions.
3. An explicit invariant-domain polynomial system and a parameter family have minimum implication-IBC degree 2 and minimum fixed-anchor constant-comparison VBC degree 4. A rational moment witness excludes all degree-at-most-3 VBCs; a quartic scalar certificate establishes the upper bound.
4. Under compactness, continuity, and robust separation from the convex hull of unsafe monomial lifts, a finite polyhedral invariant exists in the monomial representation. The robust condition is equivalent to existence of a degree-bounded fixed-anchor VBC with a uniform strict propagation margin. It is sufficient, but need not be necessary, for the ordinary VBC inequality.

The IBC witness uses a **single frame**, so it is also an ordinary scalar sign-inductive barrier. This example isolates the propagation-rule gap; it does not demonstrate a benefit from adding IBC frames. The exclusion is scoped to the submitted paper's fixed-anchor definition. A general VBC may use different unsafe separating components at different states; that broader class is not excluded by this proof.

## Contents

- `paper/note.pdf`: technical note, six pages of main text plus references.
- `paper/note.tex`: editable pdfLaTeX source, including all proofs and references.
- `paper/converse.pdf`: reviewed six-page candidate converse note, October 12, 2026.
- `paper/converse.tex`: self-contained Overleaf source for the converse note.
- `src/exact_verify.py`: dependency-free rational evidence replay and polynomial checks.
- `src/exact_verify_converse.py`: exact affine comparison, robustness-bound, and moment-witness replay for the converse examples.
- `src/search_witness.py`: finite-support LP discovery with exact rational reconstruction.
- `src/plot_geometry.py`: illustrative figure generation; not proof evidence.
- `tests/test_evidence.py`: exact replay and invalid-witness rejection checks.
- `evidence/exact_report.json`: rational weights, moments, margins, and Bernstein coefficients.
- `evidence/converse_report.json`: exact comparison matrix, strict margins, robust square bound, and moment identities for the converse note.
- `evidence/lp_discovery.json`: solver discovery results, clearly separated from exact evidence.
- `docs/RESEARCH_ROADMAP.md`: novelty boundaries and a staged TAC research program.
- `docs/SOURCE_MANIFEST.json`: checksums of the five supplied PDFs; their contents are not redistributed.
- `docs/CONVERSE_SCOPE.md`: converse assumptions, limitations, and reproduction instructions.

## Reproduce the exact evidence

Python 3.10 or later, with no external dependencies:

```sh
python src/exact_verify.py
python src/exact_verify_converse.py
python -m unittest discover -s tests -v
```

Expected replay status: `EXACT_EVIDENCE_VERIFIED`. All five tests should pass.
The converse replay reports `EXACT_FINITE_EVIDENCE_VERIFIED`.
GitHub Actions runs both replays, the five tests, and checks that their JSON evidence matches the committed files.
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
latexmk -pdf -interaction=nonstopmode -halt-on-error converse.tex
```

The proof never infers nonexistence from solver infeasibility. Discovery at degrees 1, 2, and 3 passes exact reconstruction; degree-4 infeasibility concerns only the selected support grid. The theorem and the explicit quartic witness establish the exact minimum VBC degree. No SOS solver experiment was run.

## Scientific limits and review

- The compactness and strict-feasibility assumptions in the fixed-vector characterization are additions to the base definitions and are stated explicitly.
- The general moment obstruction is sufficient, not claimed necessary for existence of an unknown VBC.
- The converse equivalence requires a uniform strict propagation margin. An identity-map example shows that an ordinary VBC may exist while robust convexified separation fails.
- Strict margins on compact data permit rational coefficient approximation, but the converse does not provide a terminating synthesis algorithm or an a priori component bound.
- A feasible moment-SOS relaxation may contain pseudomoments; extract and verify actual measures before using it as an obstruction.
- Exact rational replay validates this finite evidence. Human mathematical review is still needed for the general theorems, and a separate literature review is needed for priority.
- The parameter family is structurally persistent over its open parameter region, not proven robust to arbitrary model perturbations.
- Autonomous deterministic discrete-time safety is the scope. Switching, control, persistence, and data-driven extensions remain future work.
- The supplied submission labels the affine obstruction **Theorem 9**; item 10 is a scope remark. Check manuscript versions before changing references in correspondence.

See `docs/RESEARCH_ROADMAP.md` before expanding the paper.
