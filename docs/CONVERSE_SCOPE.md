# Robust converse at prescribed degree

The reviewed October 12, 2026 note is [paper/converse.pdf](../paper/converse.pdf).
Its self-contained [LaTeX source](../paper/converse.tex) compiles with pdfLaTeX
and can be uploaded to Overleaf.

## Candidate result and assumptions

Fix a total polynomial degree bound d. The verification domain X is compact,
the map f: X -> X is continuous, and the nonempty compact initial and unsafe
sets are disjoint. The monomial feature map excludes the constant monomial;
affine offsets represent constant polynomial coefficients.

The transition relation is the convex hull of all pairs of a monomial lift
and its successor lift. It includes mixtures whose source atoms lie outside
the initial set. Reachable feature sets are convexified at every iteration.
Source and successor feature errors are independent perturbations in the
relative affine feature space.

Robust separation of this reachability closure from the convex hull of unsafe
lifts yields a finite bounded polyhedron and a fixed-anchor VBC of degree at
most d. Equivalence is claimed for certificates with a uniform strict
propagation margin, B(f(x)) <= A B(x) - eta*1, eta > 0. The same condition is
sufficient but need not be necessary for the ordinary inequality without eta.
The fixed unsafe anchor is one designated component positive throughout Xu.

The proof is an existence construction. It provides no terminating synthesis
algorithm or a priori component bound. Strict margins permit rational
coefficient approximation on compact data; this is not a general computable
rounding procedure. The matrix A is constant and entrywise nonnegative; no
spectral-radius assumption is imposed.

## Analytical examples and exact replay

A contracting quarter-turn admits four affine components and an exact
nonnegative cyclic comparison matrix with propagation margin 1/20. A scalar
affine VBC is impossible. Four is not claimed to be the minimum component count.

The earlier nonlinear scalar example has a one-frame interpolation-inspired
barrier certificate (IBC) of degree two. Its exact moment witness excludes
every finite fixed-anchor VBC of degree at most three, regardless of the
constant nonnegative comparison matrix.

From the repository root, run:

```sh
python src/exact_verify_converse.py
```

This requires only Python 3.10+ and the standard library. Do not use -O.
It reports EXACT_FINITE_EVIDENCE_VERIFIED and writes
[evidence/converse_report.json](../evidence/converse_report.json).
The replay checks every affine coefficient and offset in the global rotation
identity, the robustness bound 469/1000 < 1/2, the exact moments through degree
three, support membership, and unit probability masses.

The replay is finite evidence verification. The converse theorem and the
universal component-count exclusion rely on the analytical proofs in the note.

The existing exact degree-separation replay and its five tests remain:

```sh
python src/exact_verify.py
python -m unittest discover -s tests -v
```

GitHub Actions executes both exact replays and the tests, then checks that the
generated JSON evidence equals the committed evidence.

Compile the new note from paper/:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error converse.tex
```

## Literature and novelty boundary

The HST comparison was checked against arXiv:1607.01107v1, Theorem 3.10,
equation (11), and Remark 3.11. The row-multiplier argument is classical
convex separation.

The note also cites Jun Liu's robust discrete-time converse barrier result
(arXiv:2007.11086, Section IV, Theorem 30) and Alessio et al.'s construction of
polyhedral invariants from contractive ellipsoids (Automatica 43, 2007,
DOI 10.1016/j.automatica.2007.04.028).
A full comparison of assumptions and conclusions remains necessary before
claiming novelty for the fixed-degree convexified-relation characterization.
