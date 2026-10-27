# Consolidated manuscript audit — October 26, 2026

This audit records the completed first journal draft requested in Majid's
"Preparing the TAC Manuscript" response. The paper is an author-review draft,
not a journal submission. Earlier technical notes and the old outline remain archived.

## Request-to-manuscript map

| Request | Completed manuscript location |
| --- | --- |
| Complete, coherent IEEE journal first draft | Sections I–X: introduction, definitions, related work, proofs, examples, reproducibility, conclusion |
| General fixed-family comparison characterization with assumptions and proof | Section IV, Lemma 1 and Theorem 1; fixed finite continuous B, compact invariant X, strict source feasibility; extra backward Slater condition stated |
| General prescribed-degree moment obstruction | Section IV, Theorem 2 and Corollary 1; actual measures, both directions, all finite component counts, explicit fixed-anchor scope |
| Account for mixtures and lifted transitions | Section V, full convexified graph relation and repeated reachable-set convexification with independent source/successor errors |
| Schur-stable converse and scope | Section V, Theorem 3, strict/Schur shifts, eventual unsafe avoidance, onto and periodic-point obstructions |
| Conditional constructive extraction | Section VI, Theorems 4–5, supplied certified body, facet counts and finite LP error budgets |
| Define IBC; analytic affine impossibility and quartic proof | Sections II and VII-A; single-frame quadratic implication certificates, both directions; moment lower bound and analytic quartic comparison |
| Separate degree 2/4 from scalar/vector degree 2/1 | Section VII and Table I; the latter is a different explicit cubic family and forward only |
| Explain the 12-component example honestly | Section VIII and Table I; the scalar affine baseline already works, so this validates extraction rather than a component advantage |
| Precise relation to submitted/group/external work | Section III, with theorem-specific comparisons; original affine result credited, classical duality/geometry attributed |
| Exact revision and commands | Section IX pins code/data revision 7b2d025abdf9786f55819a36b10ffd8a5e343375 and all four reproduction commands |
| Leave neutral converse, automatic body discovery, minimum component counts open | Introduction, scope remarks, Table I, and conclusion |

## Completed checks

- All three dependency-free exact replays pass:
  EXACT_EVIDENCE_VERIFIED, EXACT_FINITE_EVIDENCE_VERIFIED,
  EXACT_CONSTRUCTIVE_EVIDENCE_VERIFIED.
- All 20 unit tests pass, including corrupted-evidence rejection checks.
- All three generated JSON reports reproduce byte-for-byte.
- Code, tests, evidence, and the published geometry.pdf are unchanged from the evidence revision.
- The complete paper compiles with the official unmodified IEEEtran v1.8b
  journal class and pdfLaTeX to 13 pages.
- No undefined references, LaTeX warnings, or overfull boxes remain.
  The checked build reports 11 benign underfull column/bibliography lines.
- Every rendered page was visually inspected for clipped equations,
  overlapping text, table layout, figure placement, and references.
- The source-only Overleaf archive was extracted and compiled in a clean directory;
  all 13 pages of extracted PDF text match the checked manuscript.

## Mathematical review points

The row-multiplier proof is included and invoked explicitly by the fixed-family
theorem. Forward strict feasibility is not silently assumed in the backward
analogue. The moment theorem quantifies over arbitrary finite component counts
but requires a fixed unsafe anchor; it does not exclude pointwise selection of
different unsafe components. The finite-chain consequence uses actual convex
feature states, not a claimed unsafe trajectory.

The quartic ordinary certificate has spectral radius one and is explicitly
outside the Schur-stable converse. The quadratic IBC and quartic comparison
have explicit backward witnesses, obtained by negation with the needed strict
interior-preimage argument. The cubic family proves a scalar/vector degree
tradeoff, but four components are an upper bound, not an optimal count.

Supplied-body extraction is conditional on certified body/support/cover
information. Dudley's exponent is classical. Finite-node feasibility is lifted
to the continuum only after charging both feature errors; an independent exact
Bernstein proof checks the worked example. Physical state robustness is not
substituted for convexified-feature robustness.

## Remaining coauthor judgments

The general theorems are mathematical proofs, not proof-assistant formalizations.
The targeted primary-source comparison does not establish exhaustive priority.
Coauthor review should assess the final novelty and presentation for TAC,
including the relation to the separately submitted VBC/IBC paper.
No journal acceptance or revolutionary significance is claimed.


## Download reissue and proofread — October 27, 2026

The complete manuscript was checked again against Majid's October 26 request.
The general definitions, fixed-family and moment proofs, Schur equivalence,
conditional extraction, and both distinct degree separations were reread.
An incorrect literal Section 3 reference in the parameter-family proof now
uses the correct cross-reference to Section VII-A. A grammatical typo in
the scope paragraph was corrected. No mathematical statement, code, or evidence changed.

All three exact replays and all 20 tests passed again. All three generated
JSON reports reproduced byte-for-byte. The source-only Overleaf ZIP was
rebuilt, extracted into a fresh directory, and compiled successfully.
All 13 pages of PDF text match the checked manuscript. The two affected
pages were rendered and visually inspected; all other rendered pages are
byte-identical to the preceding reviewed version. The build has no unresolved
references, LaTeX warnings, or overfull boxes; 11 benign underfull lines remain.

Fresh download copies are exact copies of the committed PDF, source, and
Overleaf archive. The reproducibility code/data revision remains
7b2d025abdf9786f55819a36b10ffd8a5e343375.
