# Independent entropy and global one-use proof audit

Audit source: `GoGoKo699/Measurement-Geometry-Superadditivity`, pinned commit
`f0015c56a19fd953c6797b2c64d9b507105234e3`, read from the separate `baseline/`
workspace. This report audits the existing claims, introduces no source fixes,
and is not manuscript text. The parent audit owns repository identity checks,
the full positive certificate executions, reproduction, and final disposition.

## Disposition

No scientific defect was found in the entropy integral, transformed-variable
curvature, global one-use comparison, low- and high-noise analytical endpoints,
arbitrarily nearly pure input tails, or frame-dependent separation. The
mathematical envelopes implemented by all three complete compact-domain
verifiers are valid. The implementations retain distinct arithmetic and, for
the Decimal checker, a distinct optimization envelope.

The global mathematical conclusion is conditional here on successful full
positive execution of at least one sound complete checker, which is being
performed by the parent audit. This subaudit inspected every checker and its
bounds, independently scanned the exact rational covering, and executed 36
malformed-proof rejection cases across the three backends. It did not duplicate
the full 29,635-rectangle positive runs.

Confidence: high for the analytical derivations and checker-bound validity.
No external proof-assistant formalization or verification of Python's runtime
or arithmetic libraries is claimed.

## Claim and evidence ledger

| Claim or obligation | Exact source location | Independent check | Disposition |
|---|---|---|---|
| Physical one-use reduction and complete input parameterization | `docs/COMPLETE_PROOF.md`, P01, lines 18–79, P1.1–P1.2 | Derived reported-outcome effect, reference determinant, flag cancellation, infimum criterion | Valid |
| Homogeneous entropy integral | P03.1, lines 114–127, P3.1 | Integrated four elementary logarithms and checked both boundaries | Valid |
| Concavity in transformed `g` and convexity in squared projection | P03.2, lines 131–160 | Recomputed paired integrand and both second derivatives | Valid |
| Endpoint chord and common coefficient | P03.3–P04, lines 164–223 | Verified endpoint weights, `0 <= beta <= 1`, polynomial identities, and full infimum step | Valid |
| Low-noise endpoint including all nearly pure inputs | P05, lines 230–271 | Reconstructed elementary entropy lower bound and exact rational margins | Valid |
| High-noise endpoint including `t -> 0` | P06, lines 278–316 | Derived positive series, telescoping coefficients, integral average, Taylor remainder, and ratio bounds | Valid |
| Whole noise-band enclosure | P07.1, lines 327–347 | Checked all monotonicity directions and positive coefficients | Valid |
| Complete lower input tail | P07.2, lines 351–360, P7.3 | Independently derived same tail from elementary entropy inequalities | Valid |
| Entire compact rectangles | P07.3, lines 364–372 | Proved secant/tangent and secant/conjugate envelope correctness | Valid |
| Exact domain coverage | `certificates/common_noise_compact_certificate.json` | Independent `Fraction` scan: 512 bands, 29,635 input intervals, exact endpoints | Passed |
| Failure detection | Three checker entry points listed below | 12 malformed-certificate cases per backend, plus 7 inadequate-precision cases | Passed all targeted cases |
| Global frame gap | P08, lines 393–444, P8.1–P8.3 | Pointwise comparison before minimization, spherical integral, arcsin remainder, width denominator | Valid |
| Global one-use zero for retained eight-use witness | P13.1 and P04/P08 | Independently obtain `Gamma=27/59`, `p1=59/86`, and `Ic/h <= -6/295` at `p=7/10` | Valid, conditional on compact scalar lemma |

“Valid” here describes the mathematical derivation, not a claim that diagnostic
point samples establish an uncountable domain.

## 1. Physical reduction and complete optimization

For a true projective outcome `r`, destructive measurement followed by classical
reporting noise leaves the receiver only a classical `s`. Summing over `r`
first gives `E_s = (I + (-1)^s eta n.sigma)/2`. The reference block after the
reported outcome is `D_t E_s^T D_t`, not a block conditioned on the hidden sign.
Its trace is the displayed `q_s`, and its determinant is
`det(D_t)^2 det(E_s) = c t(1-t)/4`.

For any normalized qubit input, choosing its eigenbasis parameterizes it by
`t in [0,1/2]` and an arbitrary unit Bloch direction `u`. This includes every
single-use input, including maximally mixed and pure states. Orthogonal branch
and report flags contribute equal classical entropies to `S(B)` and `S(RB)`;
the resulting difference is `(1-p)h(t) - p C(t,u)`. All reported outcomes and
axis probabilities remain in `C`.

Pure inputs have a trivial reference and coherent information exactly zero.
For mixed inputs, division by the strictly positive `h(t)` makes the threshold
criterion exact: every ratio is at least `Gamma`; conversely any threshold
strictly above its infimum is exceeded in the required direction by some
actual input. Attainment of the infimum is unnecessary. Consequently P1.2 is
valid, including its equality endpoint.

The nearly pure ratio follows from the small unnormalized eigenvalue
`r_small = Delta/q + O(Delta^2)` for fixed interior error. The coefficient of
`t log(1/t)` is `(c/4) sum_s 1/q_s(0) = c/(1-a x)`. This is a limit for each
fixed channel and direction; no uniformity over vanishing noise is assumed.
It gives an upper bound on `Gamma`, not a general equality.

## 2. Entropy tools, integral, and curvature

Let `q=r1+r2` and `Delta=r1*r2`. The integrand in P3.1 equals

`ln(v+r1)+ln(v+r2)-ln(v)-ln(v+q)`.

An antiderivative is the same signed sum of `(v+r)ln(v+r)`. Its limit at
infinity is zero because both the linear and logarithmic large-`v` terms
cancel. At zero it is `r1 ln(r1)+r2 ln(r2)-q ln(q)`. This proves the integral
with the factor `1/ln(2)` for bits. Degenerate eigenvalues follow by continuity;
no logarithm of zero is evaluated.

For fixed `t,c`, the two-report sum is

`ln(((v+1/2+Delta/v)^2 - a(1-2t)^2 x/4)
     /((v+1/2)^2 - a(1-2t)^2 x/4))`.

Substituting `a x = 1-c/g` and multiplying numerator and denominator by `g`
gives exactly the two affine functions in P03.2. For positive `A>B` and
nonnegative `zeta`, `A/(Ag+zeta) >= B/(Bg+zeta)`. Therefore the second derivative
of their log difference is nonpositive. In the original squared-projection
variable, the inverse-denominator difference gives a nonnegative first and
second derivative. These statements are compatible because `g(x)` is nonlinear.

The integrals and their derivatives are well defined for fixed interior
parameters: near `v=0` the logarithmic singularity is integrable, and at infinity
the paired terms decay. The pure-input and maximally mixed endpoints are
handled separately as in the source.

For the determinant entropy `H(z)`, putting `s=sqrt(1-z)` gives
`H'(z)=atanh(s)/(2 s ln(2))` and
`H''(z)=-(s/(1-s^2)-atanh(s))/(4 s^3 ln(2)) <= 0`.
Thus it is increasing and concave, including its continuous limits. This
proves `H(cy)>=c H(y)` and the upper chord bound on the entropy loss `D_chi`.
Pinsker's inequality gives the stated lower entropy-loss coefficient because
the trace-norm difference is `2 sqrt(chi x(1-x))` and entropy is measured in bits.

The classical overlap inequality `h(x)<=2 sqrt(x(1-x))` is also consistent
with a direct series proof. Set `z=(1-2x)^2`. The entropy series has coefficients
`c_k=1/(2k(2k-1)ln(2))`; the deficit series of `sqrt(1-z)` has coefficients
`d_k`. One has `c_1>d_1`, `d_k>c_k` for all `k>=2`, and both coefficient sums
equal one. The latter inequality starts at `k=2` from `ln(2)>2/3`, and its
ratio increases with `k`. Therefore
`sqrt(1-z)-phi(z)=(c_1-d_1)z-sum_(k>=2)(d_k-c_k)z^k >= 0` on `[0,1]`.

For input-weight concavity, the source correctly uses the affine blocks
`sqrt(E_s) rho_t sqrt(E_s)`, which share nonzero spectra and traces with the
reference blocks. Quantum conditional-entropy concavity applies to this
normalized classical–quantum state. Subtracting unrelated concave scalar
functions would not prove the claim; the source does not rely on that invalid
argument.

## 3. Chord, polynomial, and global one-use lower bound

The interval of `g` is `[c,1]`, with endpoint costs `C_perp` and `C_parallel`.
Its chord weights are `(1-g)/a` and `(g-c)/a`, nonnegative and summing to one.
The inequalities `C_perp>=c h`, `C_perp<=C_parallel<=h` imply
`0 <= beta=(C_parallel-C_perp)/(a h) <= 1` for every mixed input.

The exact identities `1-ell=aV`, `ell-c=caW`, and `P=V+W` are correct.
Rearrangement of P4.1 gives

`C_perp/h-c beta >= (1-beta)ell`.

Combining it with the chord and summing over axes gives
`C(t,u)/h(t) >= beta G(u)+(1-beta)ell >= min(G_min,ell)`.
The same `beta` applies to all axes because the reporting error is common.
This proves a lower bound for the complete input optimization, with no
directional grid or presumed nearly pure optimizer.

## 4. Analytical endpoint and input-tail checks

The low-noise compact-input proof is conservative but valid. For
`y=c t(1-t)`, the small eigenvalue is at least `y`, and entropy is increasing
up to one half. Thus `C_perp >= y ln(1/c)/ln(2)`. For `t>=1/100`, division by
`h(t)<=t[ln(1/t)+1]/ln(2)`, together with the strict coarse logarithm bounds,
gives `C_perp/h > 1.61c`. The source's required coefficient is smaller.

For arbitrary `0<t<=delta<=1/e`, elementary bounds give

`h(y) >= [y ln(1/y)+y(1-y)]/ln(2)` and
`h(t) <= [t ln(1/t)+t]/ln(2)`.

Substituting `y=c t(1-t)` and dropping the nonnegative term
`(1-t)ln(1/(1-t))` yields

`C_perp-c h(t) >= (ct/ln(2))[(1-delta)ln(1/c)
                          -delta ln(1/delta)-(1+c)delta]`.

This proves the lower-tail formula, both for `delta=1/100` in P05 and
`delta=10^-6` in P07. Concavity of binary entropy bounds the parallel-cost
deficit by `eta t ln((1-epsilon)/epsilon)/ln(2)`. Also
`eta ln((1-epsilon)/epsilon) <= ln(4/c)`, since `eta<=1` and
`(1-epsilon)/epsilon = 4(1-epsilon)^2/c <= 4/c`.

The low-noise tail bracket is positive in the stated domain, so replacing its
positive factor by the uniform lower bound `1-(8/5)c_*` is safe. The resulting
coefficient of `ln(1/c)` is positive. Independent exact `Fraction` arithmetic
reproduces both displayed margins:

- Tail: `706479660745902522393/112589990684262400000`.
- Compact input: `167771999/16777215900`.

For high noise, differentiating the convergent entropy series gives
`f(z)=(1-z)(-phi''(z))` with coefficients
`1/[2(2j+1)(2j+3)ln(2)]`. They are positive and telescope at `z=1` to
`1/(4ln(2))`, proving monotonicity and the upper bound. Further,
`K'(z)=-f(z)` and `K(1)=0`; hence `K(z)=integral_z^1 f(v)dv`.
An increasing function has terminal-interval average at least its total
interval average, yielding `K(z)>=(1-z)K(0)` with
`K(0)=1-1/(2ln(2))`.

The Taylor remainder in `a` is bounded by
`a^2(1-z)/(8ln(2)(1-a))`, because
`1-[z+s(1-z)] >= (1-z)(1-a)` for `0<=s<=a`. This produces P06's lower bound
on `J_phi`. Integrating the bound on `-phi'` over `[az,a]` produces its upper
bound on `H_phi`. For `t>0`, `H_phi>0`; the ratio division is justified.
The exact conservative ratio margin is `99/12500`. At `t=0`, use equality
instead of dividing. This establishes the full endpoint arbitrarily close to
one-half reporting error.

## 5. Computer-assisted proof obligations

The analytical domains `0<c<=2^-28` and `24/25<=c<1` meet the compact
certificate at exact endpoints. In each compact band, the tail covers
`0<t<=10^-6` and the exact-rational intervals cover `[10^-6,1/2]`. Pure inputs
give equality. There is no uncaptured limiting tail or interpolated gap.

The barred `P,V,W` coefficients decrease with `c`; `C_perp/c` decreases by
concavity, while `C_parallel` increases under additional reporting noise.
All coefficients are positive. These facts justify using the high-noise
endpoint in the first positive term and the low-noise endpoint in the second.
The resulting `S_-(t)` is concave. A chord through outward-lowered values is
below it throughout the entire interval, even when the two endpoint rounding
errors differ.

The integer and mpmath checkers upper-bound `h` by its tangent at the rational
midpoint. Subtracting the lower secant gives a linear upper bound, so checking
both ends is sufficient. The Decimal checker instead maximizes
`P h(t)-slope*t` by binary-entropy conjugacy. Its endpoint derivative tests
correctly identify boundary maxima; if unresolved, the unrestricted maximum
over `[0,1]` is an upper bound on the interval maximum. This does not depend on
an unverified local optimizer.

### Integer arithmetic

Files: `verification/integer/dyadic_interval.py`, lines 16–123;
`verification/integer/certify_all_noise.py`, lines 15–52 and 96–118.

Each bound is an integer multiple of `2^-BITS`; arithmetic uses exact integer
floor/ceiling operations. Square-root bounds use `isqrt(endpoint*SCALE)` and
increment the upper result precisely when necessary. Dyadic range reduction
puts logarithm mantissas in `[1,2]`. With `z=(m-1)/(m+1)<=1/3`, the remaining
atanh series after `n` terms is at most
`2 z^(2n+1)/[(2n+1)(1-z^2)]`. The code encloses this expression outward and
adds its nonnegative upper endpoint. This gives an inspectable transcendental
proof independent of libmpdec and mpmath.

### Decimal arithmetic

Files: `verification/decimal/decimal_interval.py`, lines 13–80;
`verification/decimal/verify_certificate.py`, lines 18–77.

Addition, multiplication, reciprocal, and rational division have separate
floor/ceiling contexts. For the monotone `ln`, `exp`, and `sqrt`, expansion by
one adjacent representable number on either side of the correctly rounded
nearest value safely encloses the exact function value. Precision changes
clear the relevant caches. Lower endpoints become exact representable points
before the secant is constructed. Domain, sign, coverage, and declared-count
failures raise errors; numerical bounds saved inside the certificate are not
trusted.

Official Python documentation supports the needed arithmetic contract:
https://docs.python.org/3.11/library/decimal.html . In particular the `ln` and
`exp` methods document correctly rounded half-even results, and `next_minus`
and `next_plus` define adjacent context-representable values. This audit does
not reverify libmpdec itself.

### mpmath arithmetic

File: `verification/mpmath/cross_backend.py`, lines 13–57.

The interval backend uses exact integer numerators/denominators and the
entropy-difference expression for the parallel cost, unlike the integer
checker's posterior-entropy expression. Conversion of interval endpoints to
`mp.mpf` is performed at 30 extra decimal digits, retaining these binary
endpoints rather than lowering working precision. No float constants enter
the proof. The source has explicit sign and exact-cover checks.

Official interval documentation describes interval inclusion and labels
mpmath's broader interval support experimental:
https://mpmath.org/doc/current/contexts.html . This is a library qualification,
not an identified defect in this calculation; the independently bounded
integer implementation avoids dependence on mpmath transcendental behavior.

The integer and mpmath verifiers do not validate descriptive `claim` text or
saved counts as strictly as the Decimal verifier. They instead prove their
hard-coded inequality on a checked complete domain and return freshly
computed counts. This does not weaken the mathematical claim at the pinned
baseline or permit changed polynomial/domain/tail parameters. No defect is
assigned for this metadata difference.

## 6. Geometry and retained global one-use witness

The inequality `(1-y)^-1-(1-y)^-1/2>=y/2` follows, for example, by integrating
its nonnegative derivative deficit or comparing its nonnegative power series.
It is applied pointwise before either directional minimum, which correctly
gives `G_min>=L+ca lambda/2`. Full span with positive weights is equivalent to
positive definiteness of the frame matrix.

For a uniformly distributed unit direction, `n.u` is uniform on `[-1,1]`,
and its elementary integral gives the spherical average
`c asin(sqrt(a))/sqrt(a)`. Minimum is no greater than average; no actual
encoder randomization or knowledge of future axes is required. Positive
arcsin coefficients permit bounding all terms of degree at least three by
their total coefficient at `a=1` times `a^3`. The resulting quadratic after
using `pi<22/7` has its smaller endpoint value `1/35`. Thus both entries in
`min(G_min,ell)` are bounded as required for P8.3. The width denominator bound
correctly uses `L<=A_epsilon` and `lambda<=1/3`.

For equal Pauli axes, convexity of `c/(1-a x)` and the identity
`sum_b (n_b.u)^2/3=1/3` prove its minimum at equal squared projections. At
`epsilon=1/10`, `a=16/25`, `c=9/25`, this minimum is `27/59`, smaller than
`ell`. The matching nearly pure body-diagonal input supplies the opposite
inequality, so `Gamma=27/59`. Hence at `p=7/10`, every mixed input obeys

`Ic/h <= 3/10-(7/10)(27/59) = -6/295 < 0`.

Pure inputs attain zero. This establishes genuinely global optimized one-use
zero for the retained eight-use example, without a numerical Bloch search.
It uses the sharper intermediate bound, not the weaker universal `3/35`
interval.

## 7. Executed independent diagnostics and precise limits

`independent_entropy_checks.py` imports only the Python standard library. It
reconstructed conditional-reference eigenvalues independently and compared
the parallel result with its classical entropy-difference expression. At 380
decimal digits it checked 187 scalar points and 935 directional points,
including `c=10^-100`, `a=10^-80`, and `t=10^-100`. All scalar signs were
positive; the largest parallel-formula discrepancy was `6e-380` bits. The
smallest chord residual was `-1e-380` at a mathematical equality, attributable
to the explicitly non-directed point arithmetic. These are diagnostic values
and are not presented as deterministic interval enclosures or a global proof.

`certificate_failure_checks.py` reads the unchanged baseline certificate and
calls each checker on separate in-memory malformed copies. All 36 targeted
cases raised errors: polynomial/domain/tail changes; empty noise or input
covers; reversed bands or intervals; gaps; a non-finite endpoint; overlapping
input intervals; and one coarse interval whose bound cannot be certified.
Seven deliberately inadequate mpmath precision settings also rejected the
reference certificate in the first band. A potential low-precision robustness
concern was investigated and did not reproduce a silent pass.

Portable commands executed, without `-O`, from the separate audit workspace:

```text
audit-venv/bin/python audit-notes/entropy/independent_entropy_checks.py --output audit-notes/entropy/portable-check/independent.json
audit-venv/bin/python audit-notes/entropy/certificate_failure_checks.py --baseline baseline --output audit-notes/entropy/portable-check/failure.json
```

Both returned code 0. Exact numerical results and per-case exception messages
are saved in `independent_entropy_results.json` and
`certificate_failure_results.json`. The first independent numerical run took
7.60 seconds; the second records per-case durations. Full positive replay
results belong in the parent command log and must be consulted before the
final computational verdict.

Before saving the audit scripts in git, their command-line adapters were
changed to accept explicit output paths, and the certificate diagnostic now
accepts an explicit baseline root. Neither adapter change modifies mathematical
formulas, case selection, precision, assertions, or checker behavior. Both
scripts reject an existing output path. The portable reruns above write fresh
results under `portable-check/`, preserving the initial evidence.

After these files are stored in `audits/repository-sanity-01/entropy/`, reproduce
from the repository root using a new output directory:

```text
python audits/repository-sanity-01/entropy/independent_entropy_checks.py --output build/<new>/independent.json
python audits/repository-sanity-01/entropy/certificate_failure_checks.py --baseline . --output build/<new>/failure.json
```

Replace `<new>` with a fresh directory name; it is a placeholder, not literal
shell redirection syntax.

## Substantive findings

None in this assigned scientific scope. No repair is recommended to the
entropy proof or theorem on the basis of this subaudit. The report preserves
the distinction between inspected mathematics, executed finite diagnostics,
and complete positive certificate replays. A successful replay, together with
the independently audited repetition argument, is sufficient for the stated
common-noise full-span conclusion; a new code family, heterogeneous-noise
study, exact-capacity optimization, or manuscript draft is not required by
these findings.
