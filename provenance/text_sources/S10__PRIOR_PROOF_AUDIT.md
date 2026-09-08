# Theorem audit: destructive Pauli measurements with noisy classical reports

Audit date: 6 September 2026. This document distinguishes the submitted theorem from independent checks and a new comparison derived during the audit. It does not edit the submitted source.

## 1. Scope and verdict

The audited archive is `Boundary-Entangling-Susceptibility-noisy-record-threshold-screen-2026-09-06.zip`, SHA-256 `7260f16efb4243ef5c876070e6d42ef20d0cd640cefe5a8249303046ed1ede54`. The central separation survives this audit. No mathematical defect requiring withdrawal of the stated open interval was found. This is author-side analysis with independently written checking code, not external peer review or formal proof-assistant verification.

A qubit either survives with probability 1-p, or is destructively measured in one of three uniformly selected Pauli bases. Only the basis and noisy reported sign survive the measurement branch. The sign flips independently with probability e. The channel includes the mask and basis labels, but neither the true outcome nor the discarded physical qubit. No favorable outcomes are selected and no assistance is introduced at the decoder.

Writing eta=1-2e,

    N(rho) = (1-p) rho  direct-sum
             (p/3) sum_(b,s) Tr(E_bs rho) |b,s><b,s|,
    E_bs = [I+(-1)^s eta sigma_b]/2.

Q1 denotes optimized one-use coherent information, not a one-block operational capacity. Positive block coherent information gives an asymptotic achievable rate through the quantum coding theorem; a separate outer code is implicit.

## 2. Orientation reduction: rederived analytically

At fixed eigenvalues (1-t,t), put d=e(1-e)t(1-t), and let q be one conditional report probability. Its unnormalized reference entropy is

    F(q,d) = q h2((1-sqrt(1-4d/q^2))/2).

The identity

    F(q,d) = (1/ln 2) integral_0^infinity ln[1+d/(v(v+q))] dv

can be verified by factoring v^2+qv+d into its two eigenvalue factors and integrating their logarithms. It converges for the physical domain; zero determinant is handled by continuity.

For opposite reports q=(1+-z)/2, the summed integrand, with w=z^2, is

    ln[(A-w/4)/(B-w/4)],
    A=(v+1/2+d/v)^2, B=(v+1/2)^2.

Its second derivative is

    (1/16)[(B-w/4)^(-2) - (A-w/4)^(-2)] >= 0.

Averaging three such functions at fixed sum of squared Bloch components minimizes the cost when the components have equal magnitude. This supplies a global orientation argument, including complex qubit states. Cubic symmetry alone would not justify the extremum; the convexity step is essential. No concavity of coherent information is assumed.

## 3. Exact one-use zero at e=1/100

The independent verifier recomputes the submitted inequality

    C_e(t) >= (297/5099) h2(t), 0 <= t <= 1/2,

where C_e is the body-diagonal conditional-reference entropy cost. The theorem's lower-noise parameter is exactly rational, not a rounded floating-point value.

### Pure-input tail

For 0<t<=delta=10^-6, the posterior smaller eigenvalue z obeys r<=z<=2r with r=e(1-e)t(1-t)/q^2. The positivity and denominator bounds needed to lower-bound q h2(z) have been checked. The resulting lower bound for C_e(t)-g h2(t) is t times a bracket greater than

    0.0356419266159366736745110918232390347.

It covers arbitrarily small positive t analytically. There is no declaration that tiny numerical values equal zero. The exactly pure point gives zero coherent information analytically.

### Compact interval

The cost C_e(t) is concave because it is a sum of entropy perspectives of the linear efficient instrument sqrt(E) rho_t sqrt(E). Its conditional spectra coincide with the reference spectra used in the formula. Endpoint chords therefore lower-bound C_e. At p0=5099/5396, each chord gives a concave upper envelope of coherent information, whose maximum is found from an explicit stationary point or an endpoint. Fourteen exact-rational intervals cover [10^-6,1/2] without gaps or overlaps.

The largest independently verified upper bound on those intervals is

    -9.94959542235910954436564991517494624657899e-8.

The audit uses CPython Decimal/libmpdec arithmetic, not the source's mpmath interval engine. Directed arithmetic and outward-enlarged elementary functions enclose all operations. Results were computed at 100 and 130 significant decimal digits. All eight higher-precision witness enclosures lie within their lower-precision counterparts. Incorrect parameters and incomplete interval coverage are rejected.

Together with the positive near-pure coefficient below p0, this proves the submitted exact statement:

    Q1(N_(p,.01)) > 0 iff p < 5099/5396;
    Q1(N_(p,.01)) = 0 for p >= 5099/5396.

This exact characterization has only been established at the specified readout error. Neither this certificate nor the near-pure expansion proves the same formula for every e.

## 4. All-record repetition formula

The codewords are orthogonal single-qubit body-diagonal states repeated n times. The balanced average input has two orthogonal product components. It is a separable correlated density matrix; the associated logical superpositions and purification retain quantum coherence.

Set

    a=(1+eta/sqrt(3))/2, b=1-a,
    s=2 sqrt(ab), kappa=2 eta^2/(3-eta^2), g=1-kappa.

For m measured sites and k positive reports, u=a^k b^(m-k), v=b^k a^(m-k), q=(u+v)/2 and x=v/(u+v). The conditional reference spectrum has determinant x(1-x)(1-kappa^m). Basis-dependent phases disappear from this two-dimensional spectrum but their probabilities are still summed. The source A_m, C_m, R_m=A_m-C_m definitions then give

    I_n = sum_m binom(n,m)(1-p)^(n-m)p^m R_m - p^n A_n.

For m=n this is exactly -p^n C_n, not a surviving quantum contribution. In the independent Decimal implementation, the last branch is accumulated directly as -C_n, avoiding reliance on cancellation of an artificially extended R_n term.

A further, physically independent evaluator contracts actual projective measurement eigenbras for every true outcome, then mixes them according to the erroneous recorded bits. Only afterward does it compute density-matrix entropies. It neither starts from the posterior two-eigenvalue formula nor imports any source evaluator. It checks 5,600 reported branches and 61,880 hidden-outcome summands for n=1,2,3,4 at two parameter pairs. The largest grouped-formula disagreement is 6.81e-16. Eight full receiver/reference density-matrix controls, including two arbitrary complex code isometries, agree within 7.76e-15; their largest matrix dimension is 1024. No large-n full-matrix diagonalization is claimed.

## 5. The all-length achievability proof

For binary diagonal x and normalized squared coherence y, define D_y(x) as diagonal entropy minus state entropy. The two bounds used are

    (2/ln 2)y x(1-x) <= D_y(x) <= y h2(x).

Pinsker supplies the first bound; concavity of h2((1+sqrt(v))/2) in v makes D_y convex in y, giving the endpoint-chord upper bound. The bound h2(x)<=2sqrt(x(1-x)) controls the record sum.

The audit checked the central-binomial lower-bound step separately for even and odd m. For odd m the retained term has x=a or b and weight (s/2)^m/s; omitting this factor would give an incorrect constant. With the stated constants, both parities are covered:

    c_A s^m/(m+1) <= A_m <= s^m,
    c_R (s kappa)^m/(m+1) <= R_m <= (s kappa)^m,
    c_A=h2(b)/s, c_R=s/(2 ln 2).

For U=1-p+ps kappa and V=ps,

    c_R U^n/(n+1)-V^n <= I_n <= U^n-c_A V^n/(n+1).

If U>V the exponential ratio eventually beats the polynomial prefactor. Thus some finite n has strictly positive coherent information. If U<V, sufficiently large balanced blocks have negative coherent information. The proof leaves equality unresolved and does not exclude exceptional finite blocks above the asymptotic boundary.

The strict sufficient region is therefore

    p < p_rep(e) = 1/(1+s g) = s/[s+4e(1-e)].

This is an achievable boundary, not the unknown all-code capacity threshold. Choosing a large finite inner block and invoking an outer coding theorem is legitimate even though the inner block's per-use rate tends to zero as its length tends to infinity. Fixed-block t->0 and balanced-input n->infinity are distinct limits.

## 6. Converse and robustness: scope checked

Revealing whether a bit-flipped record arose from a perfect report or an independent fair bit gives a more informative flagged channel, with weights

    a=1-p (identity), b=p(1-2e) (ideal measured record), c=2pe (erasure).

The ideal measurement channel is self-complementary. For a>=c, the flagged extension is degradable: route c/a of the intact outputs to the complementary intact branch, and map its remaining intact plus erased weight to the complementary constant branch. Its coherent information is (a-c)S(rho). For a<=c it is antidegradable. Forgetting the enhancement cannot increase capacity. Thus the inherited capacity upper bound

    Q(N) <= max(0,1-p-2pe)

remains valid. The audit needs only this constructive bound; it does not use an unproved inference that every non-antidegradable channel has positive capacity.

Increasing p or e is receiver-side postprocessing. The reported robust rectangle follows from these degradations and two corner certificates, not parameter sampling. At the rectangle's worst corner, the independently enclosed 16-use rate is greater than 3.2756766876482338e-6.

## 7. New audit comparison: known single-basis measurements

This subsection is a new analytical control, not content attributed to the earlier screen.

Replace the three random Pauli bases by a single known Z basis, keeping the same destructive measurement and readout error. The sign-cost integrand above is increasing in w: its first derivative is (1/4)[(B-w/4)^(-1)-(A-w/4)^(-1)]>=0. Its minimum is therefore at zero longitudinal Bloch component, a direction perpendicular to Z. Both reports then have probability 1/2. Put c=4e(1-e), so 1-c=eta^2. The conditional-reference entropy is h2((1-sqrt(1-4c t(1-t)))/2).

The bound D_y(t)<=y h2(t) implies this entropy is at least c h2(t). Its near-pure ratio tends to c. The exact optimized one-use positivity threshold for this control is consequently

    p_fixed=1/(1+4e(1-e)), 0<e<1/2.

For the equatorial weighted repetition family, A_m=h2(t), and R_m<=eta^(2m)h2(t). Hence

    I_n <= h2(t)[(1-p+p eta^2)^n-p^n].

At or above p_fixed this is nonpositive for every n and input weight. Below p_fixed the fixed-n near-pure expansion supplies positive coherent information. Thus this specific repetition family does not move that control's one-use boundary. Seventy-five parameter/length/weight evaluations corroborate the inequality; the universal statement follows from the derivation.

This comparison isolates an important feature: in the three-basis body-diagonal construction, the likelihood coefficient s is strictly below one, whereas it equals one in the known-basis equatorial control. It does NOT prove that incompatible measurements are necessary for all forms of superadditivity, that every measurement ensemble behaves like three Pauli axes, or that no other code can improve the fixed-basis channel's threshold. The easier known-basis channel is not a benchmark we claim to outperform.

## 8. Technical conclusion

The claim Q1=0<Q on the stated .01-noise interval is supported by the audited orientation theorem, complete zero certificate, all-record branch formula and all-length exponent bounds. The largest remaining uncertainty is not the sign of a numerical witness; it is originality and significance of the particular channel specialization relative to existing incomplete-erasure and coding results. See PRIORITY_MAP.md and REVIEW_NOTE.md.
