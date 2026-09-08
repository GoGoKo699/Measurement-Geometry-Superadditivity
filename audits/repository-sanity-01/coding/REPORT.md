# Independent coding and geometry audit

Audit baseline: `f0015c56a19fd953c6797b2c64d9b507105234e3` of
`GoGoKo699/Measurement-Geometry-Superadditivity`.

Scope: `docs/COMPLETE_PROOF.md` P08–P12; P02 as an entropy-tool dependency;
the matching statements in `docs/MODEL_AND_CLAIMS.md` and
`docs/FROZEN_ARGUMENT.md`. Baseline sources were read without modification.
This subaudit did not run the repository reproduction pipelines, alter reference
evidence, or access any other project. The parent audit separately covers the
computer-assisted all-noise scalar lemma and its numerical implementations.

## Verdict and evidence boundary

No scientific defect was found in the repetition construction, finite-axis
polynomial bounds, geometric separation, coplanar control, reporting-noise
endpoint reductions, or cone-family formulas in the stated domains. The proofs
below were independently reconstructed from the stated physical channel.

The headline full-span theorem still depends on the all-noise scalar bound
P4.2. This subaudit does **not** turn that computer-assisted dependency into an
independently established fact merely because the subsequent implication chain
is sound. Endpoint capacities also use an inspected external coding theorem and
erasure-channel result. The supporting finite calculation is a floating-point
physical consistency check, not a rigorous entropy enclosure or proof of global
input optimization.

## Claim-to-evidence ledger

| Claim/step | Exact source location | Independent check | Verdict |
|---|---|---|---|
| Record coherence coefficient | P09.1–P09.2, lines 465–499 | Product of physical reported-effect matrix elements in the two codewords; normalized squared off-diagonal equals the stated product of kappas. | Pass |
| All-record block identity | P9.2, lines 501–515 | Receiver and reference/receiver entropies evaluated separately for every mask, with the all-measured term retained. | Pass |
| Upper record envelopes | P9.3, lines 517–528 | Binary entropy overlap inequality, convex-coherence entropy chord, and factorization over independent records. | Pass |
| Polynomial lower envelopes | P9.4, lines 530–562 | Central-binomial classes, bounded total log likelihood, multinomial summation; constants independent of block length. | Pass for finite axes and interior error |
| Positive finite inner block | P10.1, lines 569–583 | Exponential ratio exceeds polynomial suppression whenever the stated strict inequality holds. | Pass |
| Positive unassisted quantum capacity | P10, lines 585–593 | A fixed positive inner block precedes an independent outer coding limit; external coding theorem checked at theorem/equation level. | Pass, conditional on positive block and external standard theorem |
| Frame-dependent gap | P08, lines 393–442 | Pointwise cost difference, compact directional minimization, exact spherical average, arcsine series and rational comparison. | Pass, conditional on P4.2 |
| Coplanar identity | P11.1, lines 600–610 | Common perpendicular achieves both costs c; concavity and near-pure limit bound all inputs. | Pass; no all-code converse follows |
| Perfect reports | P11.2, lines 612–618 | Rank-one effects give pure conditional reference states; p=1 is quantum-to-classical. | Pass |
| Random reports | P11.3, lines 620–626 | Exact input-independent flags on erasure channel; external erasure capacity Eq.(2). | Pass |
| Cone minima and exact domain | P12.1–P12.2 | Jensen plus smallest frame eigenvalue, vertical equality, exact polynomial condition. | Pass, with scalar-bound dependency for Gamma |
| Cone expansion | P12.3 | Independent Taylor expansion at fixed interior error. | Pass |

## Independent derivations

### Physical record state and the negative branch

Fix the encoding direction before the channel is used and work in its
orthonormal eigenbasis. Write `z_b = n_b dot u`.
For a reported effect, the two codeword diagonal matrix elements are
`(1 ± (-1)^s eta z_b)/2`. The magnitude squared of the off-diagonal element is
`a(1-z_b^2)/4`. Their diagonal product is `(1-a z_b^2)/4`, so the normalized
squared coherence is

`kappa_b = a(1-z_b^2)/(1-a z_b^2)`.

The axis weights multiply each matrix element and cancel in this ratio. A
record containing several measured sites multiplies these factors, including
their phases, and gives `chi = product kappa_b`. Full-rank effects guarantee
strictly positive codeword likelihoods for interior reporting noise. This
derivation first sums true projective outcomes with their reporting
probabilities; it does not output either the true signs or the acquisition
error bits.

If at least one site survives, its two codeword states are orthogonal. Tracing
the reference therefore leaves receiver spectrum `(1-x,x)`, while the joint
reference/receiver spectrum has determinant `(1-chi)x(1-x)`. The contribution
is exactly `q D_chi(x)`. If all sites are measured, the receiver conditional on
the full classical record has entropy zero. The remaining reference has the
same two-dimensional determinant, giving **minus** its entropy. Consequently

`I_n = sum_m binom(n,m) (1-p)^(n-m) p^m R_m - p^n A_n`.

The all-measured combined term is `-p^n C_n`, never a positive survivor term.
The phase of a record's coherence changes neither spectrum, so this entropy
calculation needs no phase side channel and makes no decoder assumption.

### Upper and lower exponential envelopes

For a record, `q=(p_++p_-)/2` and `x=p_-/(p_++p_-)`. Hence
`2 q sqrt(x(1-x)) = sqrt(p_+ p_-)` exactly. Combining
`h_2(x) <= 2 sqrt(x(1-x))` and `D_chi(x) <= chi h_2(x)` yields the upper
envelopes. Summing records factorizes because physical uses are independent:
`sum sqrt(P_+ P_-)=B` and `sum kappa sqrt(P_+ P_-)=K`.

For lower envelopes, first fix the axis counts `m_b`. For each axis choose
one central sign count `floor(m_b/2)`. Its binomial multiplicity is at least
`2^m_b/(m_b+1)` because the largest of the `m_b+1` binomial coefficients is at
least their mean. Its sign imbalance is at most one. The total absolute log
likelihood ratio across all such records is at most
`sum_b log(pi_b^+/pi_b^-)`, independent of `m`.

Every retained posterior therefore lies in `[x_*,1-x_*]`, giving strictly
positive constants `c_A=h_2(x_*)` and
`c_R=2 x_*(1-x_*)/ln(2)`. The probability `q` is at least the geometric mean
of the two codeword likelihoods. For fixed counts the latter contains a
sign-independent factor `product_b(s_b/2)^m_b`. Central multiplicities cancel
the powers of two. For the coherence entropy the additional factor is
`product_b kappa_b^m_b` by Pinsker's lower bound. Including axis weights and
summing their multinomial distribution gives

`A_m >= c_A B^m/(m+1)^J`,
`R_m >= c_R K^m/(m+1)^J`.

This is only a lower bound on a sum of nonnegative terms. No actual channel
event is discarded. A zero `kappa_b` correctly gives zero contribution for
records containing that axis. When `K=0`, every nonempty measured record has
zero retained coherence and the intact term is treated directly. At `m=0`,
`A_0=R_0=1` is compatible with `c_A,c_R <= 1`.

Finiteness of `J` and fixed strictly positive reporting error are real
assumptions: they ensure a polynomial prefactor and a positive likelihood
constant independent of block length. This does not assert uniform constants
as the ensemble or error varies.

### The two coding limits

Substituting the envelopes yields exactly P10.1 with
`nu_+=1-p+pK` and `nu_-=pB`. The identity
`B-K=sum_b w_b c/sqrt(1-a z_b^2)=Lambda(u)` makes
`nu_+>nu_-` equivalent to `p<1/(1+Lambda(u))`.
For any fixed channel and such fixed direction, positivity follows once

`n log(nu_+/nu_-) > J log(n+1) - log(c_R)`.

There exists a finite integer satisfying this inequality since its left side
is linear with positive slope and its right side is logarithmic. This is an
existence statement, not a practical block-size claim. One selects that
finite integer and only then applies the coherent-information direct coding
theorem to repeated uses of the corresponding block channel. Rates strictly
below `I_n/n` are achievable; capacity, being a supremum, is at least
`I_n/n>0`. A limit of `I_n/n` as the inner length tends to infinity is not
required. Equality of the two exponential bases remains unresolved by these
envelopes, as stated in the source.

The relevant external result is Devetak, arXiv:quant-ph/0304127v6,
Proposition 7, Eq.(53); the direct part of Theorem 5 explicitly obtains
coherent information and then uses further blocking (PDF pages 11–12 and
14–15). The repository's use matches the unassisted finite-dimensional
memoryless channel setting. No constructive efficient decoder is implied.

### Frame-dependent geometric gap

The positive power series of
`(1-y)^(-1)-(1-y)^(-1/2)` starts with `y/2` and has only nonnegative higher
coefficients. Thus for every fixed direction,

`G(u)-Lambda(u) >= ca (u^T T u)/2 >= ca lambda/2`.

Taking a minimum on the left in the correct order gives
`G_min >= L+ca lambda/2`. Positive denominators and compactness guarantee
existence of a minimizing direction. There is no exchange of minimization
and averaging.

For an independent uniformly spherical direction, its projection on any
fixed unit axis is uniform on `[-1,1]`. Hence the average loss is
`A_epsilon=c asin(sqrt(a))/sqrt(a)` and `L<=A_epsilon`. In the arcsine series,
the sum of coefficients from order `a^3` onward is
`pi/2-1-1/6-3/40=pi/2-149/120`. Because `a^k<=a^3` for `k>=3` on `[0,1]`,
this supplies the cubic upper bound in P08.

The exact comparison with `pi<22/7` gives the lower polynomial
`a(1/12+7a/40-193a^2/840)`. The parenthesized quadratic is concave; its
endpoint values are `1/12` and `1/35`, so its minimum is `1/35`.
The exact integral supplied for `22/7-pi` is valid and has a strictly
positive integrand on `(0,1)`. Thus `ell > L+ca/35`. Since `lambda<=1/3`,
combining this with the independently valid pointwise geometric difference
and **the separate scalar obligation** `Gamma>=min(G_min,ell)` proves
`Gamma>=L+(3ca/35)lambda`.

The guaranteed p interval has its lower endpoint included, because it is
where the global single-use bound becomes nonpositive; its upper endpoint
must be strict for the exponential coding comparison. Its width is the
stated exact reciprocal difference. Bounding its denominator with
`L<=A_epsilon` and `lambda<=1/3` gives the stated linear lower width bound.
These are widths in probability space, not communication rates.

### Coplanarity and noise endpoints

When the span has rank at most two, a common perpendicular direction makes
all squared projections zero. Every directional repetition loss is at least
`c`, and this direction attains it. For the single-use cost, monotonicity in
the squared projection and determinant-entropy concavity give
`C_epsilon(t,x)>=C_perp(t)>=c h_2(t)`. The perpendicular near-pure limit
approaches the bound, so `Gamma=L=c`. Together with the strict full-span
case this proves the stated rank equivalence **for this comparison**. It
does not forbid positive finite blocks from other codes or unexpected short
blocks above the eventual-sign frontier.

At zero reporting noise each reported effect has rank one; conditional
reference states are pure. Thus `I_c=(1-p)S(rho)` for every single input. At
`p=1` the channel is entanglement breaking, so the only single-use-zero point
has no quantum capacity. This argument avoids singular interior expressions.

At reporting error one half, every fixed-axis effect is `I/2`. The measured
record is an independent sample with probabilities `w_b/2`. Removing that
record produces the erasure channel, and locally resampling it restores the
original channel. The channels therefore have the same quantum capacity.
Single-use coherent information is `(1-2p)S(rho)`. Bennett, DiVincenzo and
Smolin, arXiv:quant-ph/9701015v2, Eq.(2), gives the unassisted erasure quantum
capacity `max(0,1-2p)`. Both statements yield the claimed endpoint equality.

### Cone domain and expansion

The three equally weighted azimuths have zero average horizontal components,
equal horizontal second moments `(1-lambda)/2`, and vertical second moment
`lambda`. For `0<=lambda<=1/3`, the last is the smallest eigenvalue. Jensen
applies because both `1/(1-ax)` and `1/sqrt(1-ax)` are increasing and convex.
The average squared projection is at least `lambda`, while the vertical
direction gives exactly `lambda` for all three axes. This proves the exact
minima `G_min=c/(1-a lambda)` and `L=c/sqrt(1-a lambda)`.

The condition `G_min<=ell=cP` is equivalent to `lambda<=W/P`, using the
identity `P-1=aW`. The scalar lower bound then matches the nearly pure upper
bound on Gamma. Direct subtraction gives
`4W-P=(3/4)a+(3/20)a^2-(1/10)a^3>=0`, proving the all-error safe domain
through `lambda=1/4`. Likewise
`3W-P=(2a-1)(5-a^2)/20`, so the stated sufficient extension to one third
when `a>=1/2` is exact. It does not extend that domain to all errors.

At fixed interior error,
`Gamma=c+ca lambda+O(lambda^2)` and
`L=c+(ca/2)lambda+O(lambda^2)`. Expanding their reciprocal thresholds gives
`p_rep-p_1=ca lambda/[2(1+c)^2]+O(lambda^2)`. The coefficient is positive
and vanishes at either error endpoint, consistent with the stated
nonuniformity. No finite-block rate scaling follows from this expansion.

## Supporting physical calculation

`independent_physical_repetition.py` was written without importing or using
any baseline evaluator. It forms a coherent reference/codeword state in the
computational basis, applies the actual projective-eigenstate bras, averages
hidden outcomes with the reporting error probability, and traces the
reference to evaluate receiver entropy. It enumerates every reported record
and every mask for blocks up to three uses.

The comparison independently implements the two-dimensional reduction for
unequal weights and nonorthogonal noncoplanar axes, an aligned direction with
one zero coherence factor, a perpendicular coplanar direction, and both
reporting-noise endpoints. No eight-use output density matrix is built.
The isolated-environment run completed with return code 0 in 0.8075 seconds
(0.7323 seconds inside the calculation), using Python 3.12.13 and the pinned
NumPy 2.3.5 with assertions enabled. Seven cases enumerated 1,259 reported
branches and 7,671 hidden-outcome terms. The largest branch discrepancy was
`1.2323475573339238e-14` bits against the declared comparison tolerance
`4e-12`. Every total trace agreed with 1 within that tolerance. All-measured
contributions were nonpositive; at perfect reporting the residual was of
floating roundoff size. At completely random reporting the three-use value
was `-0.3160000000000002`, agreeing with the independent identity
`(1-p)^3-p^3=-0.316` for `p=0.7`.

The code does not filter positive eigenvalues using an arbitrary cutoff:
its entropy routine retains every positive eigenvalue and asserts that any
negative eigenvalue is within the stated floating-point tolerance. Negative
near-zero eigensolver roundoff is omitted from the entropy sum. No claim of
rigorous outward enclosure is made for this calculation.

`physical_results.json` contains all seven parameter choices, per-mask-count
totals, traces, overlaps, bound comparisons and the execution environment.
`COMMANDS.json` records the exact execution commands, return codes, durations,
relevant process limits and SHA-256 values. The Python version differs from
the recorded source environment's 3.13.5; the parent's full reproduction log
assesses any artifact reproduction consequences. A preliminary NumPy import
failed before environment installation completed, and the same import
succeeded before executing this evidence. That setup observation was not
counted as a scientific failure or an executed check.

## Non-scientific observation for parent triage

The final paragraph of `docs/MODEL_AND_CLAIMS.md` says no remote repository
has been created. In the present named GitHub repository that is stale
current-status wording, not a scientific defect. The historical pending-audit
footer in `FROZEN_ARGUMENT.md` is explicitly identified elsewhere as
superseded; its preservation alone is not evidence that the later theorem
audit was omitted. The parent reader audit should assess whether the
historical/current distinction is sufficiently visible in each reading path.

## Primary-source records

- Devetak, *The private classical capacity and quantum capacity of a quantum
  channel*, arXiv:quant-ph/0304127v6 (2004 revision), Proposition 7 Eq.(53),
  Theorem 5 and its direct part. Retrieved directly from the arXiv PDF during
  this audit: https://arxiv.org/pdf/quant-ph/0304127 .
- Bennett, DiVincenzo and Smolin, *Capacities of Quantum Erasure Channels*,
  arXiv:quant-ph/9701015v2, Phys. Rev. Lett. 78, 3217–3220 (1997), Eq.(2).
  Retrieved directly from the arXiv PDF during this audit:
  https://arxiv.org/pdf/quant-ph/9701015 .

No novelty conclusion is drawn in this subaudit. The references above verify
the precise standard theorem dependencies only.
