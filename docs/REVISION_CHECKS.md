# Revision audit — October 21, 2026

This revision responds to the detailed comments on Technical Note 2.
The assumptions and fixed unsafe anchor are retained. The new constructions
are conditional theorems with proofs, not claims based on solver success.

| Requested point | Revised result and location |
| --- | --- |
| Retain compact invariant domain, prescribed total degree, and fixed anchor | Section 1 keeps the original definitions; the same component is positive on every unsafe state. |
| Exact comparison-matrix class | Theorem 1 adds equivalence with an ordinary certificate having a constant nonnegative Schur-stable matrix. The left Perron-vector argument excludes rho(A)>1 for all ordinary certificates and rho(A)>=1 for strict ones. The constant shift proves the reverse implication. |
| Stronger dynamical consequences | Proposition 1 gives uniform eventual negativity and an explicit weighted contraction/time bound. Corollary 2 excludes unsafe periodic points and onto maps at every degree/count. Shifted functions are used for ordinary Schur-stable certificates. |
| Original quartic recovery | Section 8 states that the nonlinear degree-gap map is onto and every ordinary certificate there must have rho(A)=1. The quartic certificate remains valid; the robust converse does not explain it. |
| Physical versus feature robustness | Section 9 retains the identity example and adds f=x² with an ordinary quadratic certificate, physical disturbance radius 1/8, and an unsafe fixed point excluding the strict class at every degree/count. |
| Same-degree examples and fixed-anchor scope | Section 7 retains “one affine function impossible; four succeed,” without a minimality claim. Section 8 retains the moment obstruction through degree three for every finite fixed-anchor family. |
| Nonlinear positive example | Section 6 proves a contraction inequality for every pair in the convexified degree-two relation and verifies independent feature errors of radius 1/20. |
| Explicit finite construction | Sections 4–5 give support-net and projection component bounds, support-error allocation, a bounded-row-sum dual witness, and a feasible finite LP with separate source and successor error budgets. |
| Effective inputs | Section 5 states certified body/support/paired-cover oracles, an admissible semialgebraic representation, exact-node assumptions, and finite termination conditional on these inputs. Body discovery remains open. |
| Accurate comparisons | Section 10 compares HST Theorem 3.10/Remark 3.11, Liu Section IV/Theorem 30, and Alessio et al. Theorem 4 with its subsequent construction. A further comparison to Berger–Sankaranarayanan Sections 6–7 records finite LP/packing precedents. No classical mechanism is claimed independently new. |
| Finite continuous features | The remark following Corollary 1 explains the extension and the role of polynomial features in interpreting the degree bound. |

The spectral characterization, dynamical limitations, and physical-robustness
counterexample formalize observations supplied in Majid's comments. The
quantitative support bound and certified finite row-LP construction are the
additional steps developed in this revision.

## Proof and numerical audit

- The closure-to-transition argument retains a strict source-error allowance;
  it does not assume that closure preserves boundary source fibers.
- The support-net count uses disjoint radius-delta/2 balls in a spherical
  annulus. The chosen anchor is counted separately. The count scales as
  O_r((R/epsilon)^(r-1)); it is coarse.
- Support overestimation is charged to the outer distance and unsafe margin.
  The unsafe margin controls support accuracy, while the prescribed separator
  avoids an additional gamma-dependent facet count.
- The finite LP's universal row cap follows by evaluating the nominal dual
  inequality at an initial graph pair. Its feasibility proof uses exact graph
  nodes; soundness uses a common node covering both features.
- The nonlinear example uses an independently checked, more economical
  polyhedron within the full source tube. It does not claim its twelve
  directions form the finer net used by the universal count.
- The exact nonlinear matrix has only three nonzero entries:
  A[1,5]=28/125, A[5,5]=52/125, A[9,5]=58/125 (one-based indexing).
- The paired-cover errors are 3/160 and 1/80. Their row-cap-weighted sum is
  1/32. With target propagation margin 1/100, all 1,932 node inequalities
  have exact slack at least 1/400.
- Certified separation margins are at least 23/80 initially and 1/10 at the
  unsafe anchor. The maximum row sum is 58/125 < 1.
- The continuum conclusion follows from the proved derivative/cover bounds
  and affine extension to convex combinations. Grid checks alone are not proof.

## Further audit and strengthening

- The repeated attachment was verified to be byte-for-byte identical to the
  original comments. The repository already incorporated those requests.
- A new projection-based construction applies classical Dudley geometry, as
  presented by Har-Peled–Jones (arXiv:1912.01977v3). Its error proof is written
  out with support overestimation charged explicitly.
- The new rate is O_r((R/epsilon)^((r-1)/2)), conditional on exact projections or certified feasible projection/support-gap
  data. The worked example's guaranteed bound improves from 1,537 to 112.
  No optimality claim is made for VBC component count.
- The key bound is distance(z,C) <= ell^2/(2R)+6*alpha <= epsilon/2,
  where ell=sqrt(R*epsilon)/2 and alpha<=epsilon/16.
- Exact Bernstein conversion independently verifies all twelve global
  polynomial inequalities without using the state cover or derivative bounds.
  All sixty coefficients are recorded in the deterministic report.
- Their minimum is 73/2500, attained by the first residual at x=1, proving
  sharpness of that uniform margin for the fixed committed B,A.
- Two additional tests verify this endpoint sharpness and reject an excessive
  margin. All 13 tests pass.
- The effective mesh construction now explicitly selects eta_* strictly below
  epsilon to guarantee a positive mesh size.

## Limits of this review

The general proofs were rederived and checked in the revision; no formal
proof assistant or independent coauthor verification is claimed.
Priority and publication significance are not settled by a targeted literature
comparison. The conditional construction does not discover the robust body.
A general converse for the neutral rho(A)=1 class remains open in this work.
The original degree-gap proof and its computational evidence are preserved.
