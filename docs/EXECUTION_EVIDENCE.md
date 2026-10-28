# Executed verification

Executed in the task workspace on October 5, 2026:

| Check | Observed result |
| --- | --- |
| Standard-library rational verifier | `EXACT_EVIDENCE_VERIFIED` |
| Evidence unit tests | 5 passed |
| Degree-3 finite-support LP discovery | Reconstructed and verified exact atomic witness |
| Degree-4 discovery on chosen grid | Infeasible grid; explicitly treated as inconclusive about other supports |
| Degree-4 use of the degree-3 witness | Correctly rejected because input fourth moments differ |
| Corrupted successor, negative weights, wrong support | Correctly rejected |
| Optimized Python mode | Correctly rejected because it disables proof assertions |
| pdfLaTeX build through latexmk | Successful; 7 pages (6 main text + 1 references) |
| PDF diagnostics | No overfull boxes, undefined references, or LaTeX warnings; benign underfull table/bibliography lines |
| Rendered PDF inspection | All pages inspected; mathematical text, tables, and figure legible |

The exact JSON is deterministic. The optional scientific-Python environment is recorded in `evidence/environment.json` and pinned in `requirements-optional.txt`. The exact proof replay does not require those packages.

The continuous-domain inequalities are supported by rational polynomial identities and sign/monotonicity arguments, not by a dense sample grid. The universal nonexistence claim is an analytical consequence of the moment-obstruction theorem; no finite collection of solver failures substitutes for that proof.

The remote repository `rezairaji60/certificate-expressiveness`, private at the time of the initial import and now public, has been verified. All 19 imported package files were fetched and matched against their local Git blob hashes; text contents also matched exactly. The initial package commit is `a79514b023e9ddc60c41d0bb6fe3ac686c47c10e`.

GitHub Actions [run 37376705604](https://github.com/rezairaji60/certificate-expressiveness/actions/runs/37376705604) completed successfully on that commit. The `replay` job passed the exact rational replay, all five evidence tests, and the deterministic committed-evidence check. This document records the completed import and remote verification.

Independent mathematical review of the general theorems and further novelty assessment remain outstanding.

## Converse replay and reviewed note — October 12, 2026

Executed on the current repository snapshot with the converse update:

| Check | Observed result |
| --- | --- |
| Original exact degree-separation replay | `EXACT_EVIDENCE_VERIFIED` |
| Converse example replay | `EXACT_FINITE_EVIDENCE_VERIFIED` |
| Existing evidence tests | All 5 passed |
| Both JSON evidence reports | Recomputed byte-for-byte identically |
| Optimized Python mode for converse replay | Correctly rejected |
| Converse PDF compilation | Successful; 6 pages; no LaTeX warnings or overfull/underfull boxes |
| Converse PDF inspection | First five pages unchanged from the reviewed note; updated repository paragraph and final page visually checked |

The workflow now runs both exact replays and checks both committed JSON files.
The checks validate finite evidence and reproducibility. General theorem validity
and novelty remain matters for mathematical and literature review.

## Schur characterization and finite construction — October 21, 2026

Executed against the revised note and code:

| Check | Observed result |
| --- | --- |
| Original exact degree-separation replay | EXACT_EVIDENCE_VERIFIED |
| Rotation and moment replay | EXACT_FINITE_EVIDENCE_VERIFIED |
| New nonlinear constructive replay | EXACT_CONSTRUCTIVE_EVIDENCE_VERIFIED |
| Deterministic committed reports | All three reports recomputed byte-for-byte identically |
| Evidence and rejection tests | All 11 passed |
| Optional nonlinear LP discovery | SciPy 1.17.0 proposed a matrix; rational reconstruction passed exact replay |
| Nonlinear polygon | All 12 exact vertices enumerated; maximum squared norm 2/5 |
| Finite node inequalities | 1,932 passed with minimum exact slack 1/400 |
| Feature-cover errors | Source 3/160, successor 1/80, row cap 1 |
| Certified margins | Initial >=23/80, unsafe anchor >=1/10, propagation >=1/100 |
| Schur bound | Exact maximum row sum 58/125 < 1; no floating eigenvalue test |
| Revised PDF | Successful pdfLaTeX/latexmk build, 11 pages, no warnings or overfull/underfull boxes |
| Rendered PDF | All 11 pages visually inspected; final modified page re-rendered and inspected |

The finite LP's continuum soundness uses the proved derivative and paired-cover
bounds and affine extension to the full convexified relation. It is not an
inference from finitely many samples without an error bound.
The general theorems remain mathematical proofs in the note, rather than
formal proof-assistant results. The targeted primary-source comparison does
not establish publication priority or revolutionary significance.

The CI workflow runs all three exact replays and the full test suite, then
checks the three deterministic reports against their committed versions.

## Further verification and projection refinement — October 21, 2026

This audit starts from the published Schur-stable revision. The reattached
feedback was byte-for-byte identical to the comments already addressed.
The proof review adds a sharper, attributed geometric construction and a
second exact continuum verification of the nonlinear example.

| Check | Observed result |
| --- | --- |
| Original, converse, and constructive replays | All three status checks passed |
| Default replay determinism | All three JSON reports recomputed byte-for-byte identically |
| Evidence and rejection tests | All 13 passed |
| Optional LP discovery | Reconstructed exactly the same committed comparison matrix; both continuum arguments passed |
| Projection count for the example | At most 112, replacing the direct support-net bound 1,537 under the stated projection certificates |
| Projection error constants | ell²/(2R)+6 alpha <= epsilon/2; the inexact variant charges alpha+sigma |
| Independent polynomial proof | All 60 degree-four Bernstein coefficients verified exactly |
| Exact uniform margin for the fixed B,A | 73/2500, attained at component 1 and x=1 |
| Excessive margin rejection | A target just above 73/2500 is rejected |
| Revised PDF | 13 pages, successful pdfLaTeX/latexmk build with no warnings or overfull/underfull boxes |
| PDF visual inspection | All 13 pages inspected; no orphan continuation page, clipped math, or unresolved references |
| Copyable command | Literal --discover preserved in extracted PDF text |

The improved geometric exponent is classical Dudley approximation, cited
through Har-Peled–Jones, arXiv:1912.01977v3. Its use here includes explicit
support and projection-gap budgets before extraction of the degree-bounded
certificate. The 112 bound is a conditional geometric guarantee; twelve
components still suffice in the explicit example, and no optimal component
count is asserted.

The Bernstein argument is independent of the cover nodes and derivative
bounds. The sharp 73/2500 margin concerns only the fixed committed functions
and matrix, not an optimization over all certificates. The general theorem
proofs and publication novelty still require independent mathematical review.

## Remaining-comments revision — October 25, 2026

This revision addresses Majid's new, one-page October 23 feedback.
It adds the scalar baseline, a separate nonlinear separation, theorem-specific
comparisons, and a consolidated manuscript outline.

| Check | Observed result |
| --- | --- |
| Original exact degree-separation replay | EXACT_EVIDENCE_VERIFIED |
| Converse replay, including new baseline and cubic-family identities | EXACT_FINITE_EVIDENCE_VERIFIED |
| Supplied-body extraction replay and independent Bernstein proof | EXACT_CONSTRUCTIVE_EVIDENCE_VERIFIED |
| All three deterministic reports | Recomputed byte-for-byte identically |
| Acceptance and rejection tests | All 20 passed |
| Scalar baseline | Exact endpoint propagation margin 1/20; initial/unsafe 7/20 and 1/10 |
| New nonlinear vector certificate | Four affine components; uniform family propagation margin 1/40 |
| New nonlinear scalar alternative | One quadratic; multiplier 81/100; propagation margin 19/400 |
| Nonlinear graph mixtures and both independent feature errors | Robust square bound 247/500 < 1/2 at error radius 1/100 |
| Polynomial proof | Exact multivariate coefficient identities and nonnegative factors on the disk, without a grid |
| Invalid new evidence | Wrong rotation coupling, excessive margin, and uncertified feature-error radius rejected |
| Final revised PDF | 15 pages; pdfLaTeX/latexmk successful, no warnings or overfull/underfull boxes |
| Visual inspection | All 15 pages inspected; final changed pages re-rendered and inspected |
| Literature checks | Primary papers checked for the cited HST, Dudley, Automatica 2023, and HSCC 2024 theorem/algorithm statements |

The universal scalar affine exclusion and exact minimum-degree conclusions
are analytic proofs in the note. The finite replays check their explicit
identities and numerical bounds, not a formal proof-assistant derivation.
The new nonlinear example extends the contracting-rotation mechanism.
Publication priority and revolutionary significance are not established.
The extraction method takes a supplied, certified convex body C and its
geometric/cover data; it does not discover C automatically.


## Complete IEEE journal manuscript — October 26, 2026

The complete manuscript is paper/manuscript.tex, with its compiled PDF and a
source-only Overleaf project. Code and data are pinned in the paper to evidence
revision 7b2d025abdf9786f55819a36b10ffd8a5e343375.

| Check | Observed result |
| --- | --- |
| Three exact replays | All expected status checks passed |
| Evidence and rejection tests | All 20 passed |
| Deterministic evidence | All three JSON reports reproduced byte-for-byte |
| Code and data provenance | Source, tests, evidence, and geometry.pdf unchanged |
| Journal build | Official unmodified IEEEtran v1.8b, pdfLaTeX/latexmk, 13 pages |
| Build diagnostics | No unresolved references, LaTeX warnings, or overfull boxes; 11 benign underfull lines |
| Visual review | All 13 rendered pages inspected |
| Overleaf package | Clean extraction and successful build; PDF text matches on every page |
| Research response | Completed definitions, proofs, related work, examples, comparison table, and conclusion; see MANUSCRIPT_CHECKS.md |

The consolidated manuscript adds no new solver experiment. The exact
replays validate finite evidence; the general theorems remain mathematical
proofs for coauthor review. Publication priority is not established by these checks.


## Download reissue verification — October 27, 2026

All three exact status checks and all 20 tests passed again. The deterministic
JSON reports are unchanged. The complete manuscript was reread against the
four requests in Majid's October 26 response. One incorrect internal section
reference and one grammatical typo were corrected; no mathematical statement,
verification code, or evidence changed.

The revised 13-page PDF and Overleaf archive both compile successfully, with
no unresolved references, LaTeX warnings, or overfull boxes and 11 benign
underfull lines. A fresh extraction of the archive reproduces the manuscript's
text on every page. The two affected pages were visually reinspected, and all
other page renders match the preceding reviewed version byte-for-byte.


## Project authorship check — October 28, 2026

The canonical project author list is Reza Iraji and Majid Zamani. The source,
visible title page, PDF Author field, Overleaf source package, and project
README were synchronized. The rebuilt source-only ZIP compiles in a clean
directory and reproduces all 13 pages of the checked manuscript. Page one was
visually inspected; later page renders match the preceding reviewed version.
Repository-wide text and PDF checks found other author names only in citations
to earlier works, whose attribution remains accurate. The mathematical body,
verification programs, tests, and exact evidence are unchanged.
