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

The private remote repository `rezairaji60/certificate-expressiveness` has been verified. All 19 imported package files were fetched and matched against their local Git blob hashes; text contents also matched exactly. The initial package commit is `a79514b023e9ddc60c41d0bb6fe3ac686c47c10e`.

GitHub Actions [run 37376705604](https://github.com/rezairaji60/certificate-expressiveness/actions/runs/37376705604) completed successfully on that commit. The `replay` job passed the exact rational replay, all five evidence tests, and the deterministic committed-evidence check. This document records the completed import and remote verification.

Independent mathematical review of the general theorems and further novelty assessment remain outstanding.
