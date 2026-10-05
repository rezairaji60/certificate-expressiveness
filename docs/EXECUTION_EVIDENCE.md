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

The GitHub Actions workflow is prepared but has not been run remotely. The private remote repository `rezairaji60/certificate-expressiveness` has been verified and the prepared source is being imported. No paper has been submitted and no email has been sent. Independent theorem and novelty review remain outstanding.
