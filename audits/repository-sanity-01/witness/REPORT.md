# Independent retained-witness audit

Audit baseline: `GoGoKo699/Measurement-Geometry-Superadditivity`, commit
`f0015c56a19fd953c6797b2c64d9b507105234e3`.

## Verdict and scope

No scientific defect was found in the retained eight-use witness, its inclusion
of the all-measured branch, or its distinction from the conservative universal
band. The independent calculation reproduces every one of the nine measured-count
contributions. The global single-use conclusion still depends on the full-domain
entropy comparison in P03–P07, audited separately by the parent audit team. A
positive numerical block calculation alone cannot establish that conclusion.

This sub-audit addresses `docs/COMPLETE_PROOF.md` P01, P09.1–P09.2 and
P13.1–P13.3, `docs/MODEL_AND_CLAIMS.md` §5, the selected witness record, and
`data/figures/cross_figure_witness_bound_check.json`. It does not rerun or import
any repository numerical evaluator and does not certify mpmath's arithmetic.

## Independent physical reduction

The implementation `independent_hidden_outcomes.py` constructs the two
eigenvectors of `(X+Y+Z)/sqrt(3)` directly in the computational basis. For each
of the six receiver records `y=(axis, reported sign)`, it forms a logical matrix

\[
E_y[k,l]=\frac13\sum_{r=0}^1\Pr(s\mid r)
\langle n_{b,r}|u_k\rangle\langle u_l|n_{b,r}\rangle.
\]

The true projective sign is summed inside this expression. It is never supplied
as a receiver register. The `1/3` axis probability is present before any record
aggregation. For a record sequence of length `m`, the subnormalized reference and
surviving-code state has matrix

\[
M_\omega[k,l]=\tfrac12\prod_{j=1}^m E_{y_j}[k,l].
\]

This follows by applying the local projective Kraus bras to the reference
purification. If a physical qubit survives, the two surviving codewords are
orthogonal, so the conditional receiver spectrum is the diagonal of `M`. Its
joint reference/receiver spectrum is the spectrum of `M`. If every qubit is
measured, the receiver is one-dimensional conditional on its classical record;
only the reference spectrum remains. Thus the all-measured conditional coherent
information is negative, with magnitude the conditional entropy of `M`.

The code retains complex off-diagonal entries. It computes both eigenvalues
from trace/discriminant and determinant (small eigenvalue = determinant / large
eigenvalue), then evaluates the homogeneous entropy
`-sum eigenvalue * log2(eigenvalue / trace)`.
It does not use the repository's `kappa`, sign-count, posterior-entropy, or
effect-determinant evaluator implementation.

Each record-matrix element is an ordinary product of scalar factors. Consequently
sequence ordering does not alter `M`: six-label count compositions, with exact
multinomial multiplicities, enumerate the entire receiver record space. At
`m=8`, 1,287 compositions represent all 1,679,616 receiver-record sequences.
Across `m=0,...,8`, the script evaluates 3,003 compositions per precision.
Mask probabilities include the exact binomial multiplicity from independent
uses. This is a tractable exact reduction of the flagged state calculation,
with numerical entropy evaluation; it is not postselection.

## Numerical evidence

The fresh calculation ran at 70 and 130 decimal digits. It yielded

\[
I_8=0.000598198127052477096813250938094229794969238984634090064978\ldots
\]

bits, and

\[
I_8/8=0.0000747747658815596371016563672617787243711548730792612581222\ldots.
\]

| Measured count | Six-label classes | Mask probability | Weighted coherent information, bits |
|---:|---:|---:|---:|
| 0 | 1 | 0.00006561 | 0.0000656100000000000 |
| 1 | 6 | 0.00122472 | 0.0004545141799871604 |
| 2 | 21 | 0.01000188 | 0.001626838911860192 |
| 3 | 56 | 0.04667544 | 0.003446447940204892 |
| 4 | 126 | 0.13613670 | 0.004635233012800187 |
| 5 | 252 | 0.25412184 | 0.004022971290728753 |
| 6 | 462 | 0.29647548 | 0.002192951568869483 |
| 7 | 792 | 0.19765032 | 0.0006852370090914598 |
| 8 | 1,287 | 0.05764801 | -0.01653160578648965 |

The record probabilities sum to one at every measured count, both diagonal
sums are `1/2`, and the summed off-diagonal element vanishes for every positive
measured count. The maximum record normalization residual at 130 digits is
`5.636e-130`. Complex coherences are nonreal in 2,531 of the evaluated classes.
Both all-measured probability and negative contribution agree with the retained
record. All nine mask probabilities sum to one.

The 70- versus 130-digit total difference is approximately `3.5531e-72` bits.
The independent 130-digit result lies within the repository's immutable
100-digit enclosures for the total, per-use rate, and eight nontrivial mask
contributions. The ninth contribution, `m=0`, is the exact rational
`(3/10)^8 = 0.00006561`, checked as a `Fraction` against the exact reference.

This is agreement of independently derived numerical values, supported by large
precision separation and direct normalization checks. It is not byte-for-byte
reproduction of the reference JSON and is not a new directed-rounding
certificate. `results.json` explicitly records that limitation. The stored
rigorous interval remains a separate evidence claim for its interval-checker
audit.

## Global single-use and band distinction

For the three equally weighted Pauli axes, Jensen's inequality applied to the
increasing convex function `c/(1-a x)` gives

\[
G(u)=\frac13\sum_{b=X,Y,Z}\frac{c}{1-a u_b^2}
\geq\frac{c}{1-a/3}=\frac{27}{59},
\]

with equality at the retained direction. This minimizes over every direction,
not a grid. The nearly pure expansion supplies the upper bound
`Gamma <= G_min`. Independently recomputed exact rationals give

\[
P=\frac{100673}{78125},\quad
\ell=\frac{906057}{1953125},\quad
\ell-\frac{27}{59}=\frac{722988}{115234375}>0.
\]

Therefore, **conditional on the separately audited all-input bound P4.2**,
`Gamma >= min(G_min,ell)` establishes `Gamma=27/59`,
`p_1=59/86`, and the exact all-mixed-input bound

\[
I_c(t,u)/h_2(t)\leq-6/295<0
\]

at `p=7/10`. Pure inputs give zero. This identifies the global optimized
single-use coherent information; it is not operational single-shot capacity.

The independent thresholds are

| Quantity | Value |
|---|---:|
| Exact single-use zero boundary | `59/86 ≈ 0.6860465116279070` |
| Witness measurement probability | `0.7` |
| Conservative universal lower boundary | `0.707978780259509526638497285857...` |
| Repetition frontier | `0.711293781408885403711792705652...` |

The witness is strictly below the universal band's lower edge. It is justified
by the sharper P4.2/P13 global result, as the scientific documentation and
cross-figure record correctly state. This report does not assert that either
frontier is an exact quantum-capacity boundary, nor that the eight-use block
has a high-fidelity or efficient standalone decoder.

## Reproduction and operational record

Run in the already-isolated audit environment, without `-O`:

```bash
/workspace/scratch/323c19becda4/audit-venv/bin/python \
  independent_hidden_outcomes.py \
  --baseline /workspace/scratch/323c19becda4/baseline \
  --output /a/fresh/path/results.json
```

The output must not exist. The baseline is only read for the final comparison
with `evidence/reference/witness100.json`; all witness arithmetic is completed
before this read. The script source hash, reference hash, interpreter, library
version, precise output values, timings, and peak RSS are in `results.json`.

Environment: Python 3.12.13, mpmath 1.3.0. The final command returned zero in
2.694 s wall time (2.668 s user, 0.022 s system); measured calculation times were
1.225 s and 1.375 s. Linux peak RSS was 15,904 KiB. Shell CPU, virtual-memory,
and data-size limits were unlimited; stack size was 8,192 KiB. No large
eight-use output matrix, optimizer, sampling approximation, or third-party
service was used.

Two audit-development attempts are preserved separately:

1. The initial timing wrapper returned 127 because `/usr/bin/time` is absent.
   `run.log` records the environment limitation. Bash's `time` and Python's
   resource module supplied a workable timing/resource path.
2. The first comparison returned 1 when a 130-digit nearest-arithmetic value
   differed infinitesimally from the zero-width rational reference for `m=0`.
   `calculation.log` preserves the assertion. The mathematical value was proved
   with exact rational arithmetic in the final script; no reference or
   repository tolerance was changed. This was a comparison error in the new
   audit script, not a defect in the repository's witness.

`calculation-final.log` records the successful final calculation. No baseline
source, reference output, approval hash, or repository evaluator was modified.

## Findings and remaining obligations

No substantive defect is reported for this bounded sub-audit. Confidence is
high in the physical reduction, all-record normalization, exact threshold
arithmetic, and retained witness value. The independently checked block
positivity is numerically overwhelming relative to arithmetic differences,
but its classification remains high-precision independent numerical evidence.

The proof of global single-use zero relies on the independently inspected
global entropy comparison, not on this witness script; the parent audit must
retain that dependency in its verdict. The capacity implication also requires
the standard asymptotic coherent-information coding theorem after this fixed
positive finite inner block is chosen. No additional witness search, new code
family, or manuscript task is needed on the evidence examined here.
