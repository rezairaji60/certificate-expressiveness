# Response to Majid's remaining points of October 23

Prepared October 25, 2026. This revision changes the scientific interpretation
of the extraction example and adds a separate analytic nonlinear separation.

| Requested point | Implemented response |
| --- | --- |
| Scalar baseline in Section 6 | b=x-3/5, A=1/2; initial margin 7/20, unsafe 1/10, propagation 1/20. It is simpler than the twelve-component pair. |
| Nonlinear example with a proved benefit from functions | Proposition 3 and Section 7: a uniform perturbation neighborhood of contracting rotation excludes every scalar affine certificate while four affine functions succeed. An explicit cubic family also has an exact scalar/vector minimum-degree tradeoff, two versus one. |
| Theorem-specific novelty assessment | Section 10 compares Theorem 1, Theorem 2/Proposition 2, and Theorem 3 separately, identifying assumptions, conclusions, and inherited mechanisms. It includes the Section 9 discrete-time discussion of Berger–Sankaranarayanan and HSCC 2024. |
| Precise computational scope | Conditional extraction from a supplied certified C; no automatic discovery of C. The ordinary rho(A)=1 class remains separate from the Schur characterization. |
| Consolidated manuscript outline | Included in the note and docs/MANUSCRIPT_OUTLINE.md, organized around moment obstructions, the Schur converse, conditional extraction, and exact separations. A neutral-class converse is not a prerequisite for drafting. |

## New proof, not solver-based nonexistence

Let X be the unit disk, X0 the disk of radius 1/4, Xu={(3/4,0)}, and R
a quarter-turn. Write f=(9/10)Rx+e with sup||e||<=delta<1/20.

Any affine separator b=a^T x-c has c>0 and c<(3/4)||a||.
At x_*=R^T a/||a||, b=-c<0 and
b(f(x_*))>=(9/10-delta)||a||-c>0. No lambda>=0 can satisfy b(f)<=lambda*b.
Four components +/-x_j-1/2 with A=(9/10)Pi have
B(f)-AB=G e-(1/20)1<=-(1/20-delta)1.

For f_theta=(9/10-theta*(1-||x||²))Rx, 0<theta<=1/40,
the perturbation bound holds uniformly. The four affine components have
margin 1/40 and the original separation margins 1/4.
The scalar quadratic ||x||²-1/4 works with multiplier 81/100 and margin 19/400.
This gives exact minimum forward degrees two (scalar) and one (finite vector).
The minimum vector function count is not proved.

The full convexified graph has t=(9/10)Rs+e_bar, ||e_bar||<=1/40.
The robust square bound is 247/500<1/2 for independent source and successor
errors 1/100. This includes mixtures, rather than only physical trajectories.

## Scope of significance

The new result is a rigorous perturbation-stable separation and a useful
function-count/degree comparison. It is an extension of the rotation mechanism;
it should not be called revolutionary or publication-novel without a separate
priority assessment. The combined moment and converse framework is the
candidate core for the manuscript. Classical duality, positive systems,
Dudley geometry, and finite LP synthesis are acknowledged as prior mechanisms.
