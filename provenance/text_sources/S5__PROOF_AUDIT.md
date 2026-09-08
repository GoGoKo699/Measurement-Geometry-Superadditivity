# Proof audit: the fixed all-common-noise claim

**Audit date: 8 September 2026.** This is an author-side review of the supplied theorem, not a new generalization, external review, or proof-assistant formalization. The original argument and claim map are preserved unchanged under `source/`. The audit introduces a separately written numerical verifier and checks only the retained eight-use illustration.

## 1. Information available at the receiver (A; C2–C3)

A projective outcome r along axis b is hidden. A classical bit-flip channel reports s with probability `(1-epsilon)` for s=r and `epsilon` otherwise. Tracing out the measured system produces the receiver effect

$$E_{b,s}=\sum_r \Pr(s|r)\Pi_{b,r}=\tfrac12[I+(-1)^s(1-2\epsilon)n_b\cdot\sigma].$$

The receiver obtains b and s, not r, the measured qubit, or a flag indicating whether the report was flipped. The intact and measured branches are orthogonal output blocks with weights independent of the input. Their flag entropy cancels between S(B) and S(RB). For every input purification the surviving contribution is its input entropy and the measured contribution is minus the average conditional-reference entropy. Hence

$$I_c=(1-p)h_2(t)-p\sum_b w_b C_\epsilon(t,(n_b\cdot u)^2).$$

The supplied determinant expression follows from `det(rho)*det(E)=t(1-t)c/4`. It is the entropy of the correctly mixed conditional reference, not of a hypothetical pure true-outcome branch. Every qubit input is represented by `(t,u)`, including arbitrary complex Bloch directions. Pure t=0 inputs give zero. The infimum characterization of Gamma therefore proves a global one-use zero, even if the minimizing mixed state is not attained. An infimum below `(1-p)/p` guarantees a finite t with positive one-use coherent information.

`code/physical_check.py` independently constructs hidden outcomes and their classical mixture. It checks all complex matrix units for the effect identity, three repetition controls and two arbitrary complex encodings. All reported branches are retained. The eight-use rate is checked separately by a symmetry-reduced interval calculation; no full eight-use output matrix is claimed.

## 2. The endpoint chord and a concavity needed for certificates (B; C4)

For one axis, put `g=c/(1-a*x)`. In the supplied homogeneous entropy integral, pairing the two outcome contributions yields integrands of the form

$$\log(Ag+b)-\log(Bg+b),\qquad A>B>0,\ b\geq0.$$

Their second derivatives are nonpositive, so C is concave in g. The endpoint chord gives

$$C/h_2(t)\geq\beta g+(C_0-c\beta h_2(t))/h_2(t),\qquad
\beta=(C_1-C_0)/(a h_2(t)).$$

The source's `C0 >= c*h`, `C1 <= h` and `C1 >= C0` imply `0 <= beta <= 1`. These statements are used for t>0; t=0 is handled directly. The new polynomial inequality makes the intercept at least `(1-beta)*ell`. Because the reporting error is COMMON across axes, beta is common. Summing then gives `Gamma >= min(G_min,ell)`. A heterogeneous-error extension does not follow from this calculation.

The compact-domain secant argument also needs concavity in t. This is not obtained by subtracting two concave scalar functions. For each fixed measurement effect, `sqrt(E_s)*rho_t*sqrt(E_s)` is affine in t and has the same nonzero eigenvalues and trace as the conditional-reference matrix `sqrt(rho_t)*E_s^T*sqrt(rho_t)` (with a consistent purification convention). Including the classical register gives an affine classical-quantum state. Concavity of its conditional entropy proves the required concavity of C0 and C1. Positive linear combinations remain concave. This justification is made explicit here; no change to the source formula is necessary.

## 3. Global entropy inequality and analytic endpoint regions (B; C4)

Write

$$P=1+a/4+a^2/4+a^3/10,\quad\ell=cP,$$
$$V=3/4+3a^2/20+a^3/10,\quad W=1/4+a/4+a^2/10.$$

Exact algebra gives `1-ell=aV`, `ell-c=caW`, and `P=V+W`. The needed inequality is

$$D=(1-\ell)C_0+(\ell-c)C_1-\ell a h_2(t)\geq0.$$

### Low noise: 0<c<=2^-28

For delta=1/100 and t>=delta, the smaller eigenvalue for C0 is at least `y=ct(1-t)` and no greater than one half. The positive entropy terms give `C0 >= ct(1-t)*ln(1/c)/ln2`. With `h(t)<=t[ln(1/t)+1]/ln2`, `ln(1/c)>19.32` and `ln100<5`, this yields `C0/h>1.61c`. The needed `ell*a/(1-ell)` is strictly smaller. The nonnegative C1 term may be dropped.

For `0<t<=delta`, elementary entropy bounds give

$$C_0-c h_2(t)\geq\frac{ct}{\ln2}[(1-\delta)\ln(1/c)-\delta\ln(1/\delta)-(1+c)\delta],$$
$$h_2(t)-C_1(t)\leq\frac{\eta t}{\ln2}\ln[(1-\epsilon)/\epsilon].$$

Since `eta*ln((1-e)/e)<=ln(4/c)`, `ell<=8c/5` and `ell-c<=3c/5`, substituting in

$$D=(1-\ell)(C_0-ch_2(t))-(\ell-c)(h_2(t)-C_1)$$

gives a positive rational lower bound. The coefficient of ln(1/c) is positive, so evaluating at the largest c is safe. Finite positive exponential/atanh series establish the coarse logarithm constants without numerical endpoint assumptions. `check_endpoints.py` verifies those rational inequalities and the polynomial identities. The endpoint t=0 has D=0.

### High noise: 0<a<=1/25

Put `z=(1-2t)^2` and `phi(z)=h2((1-sqrt(z))/2)`. Set

$$J=\phi(z+a(1-z))-(1-a)\phi(z),\quad H=\phi(az)-\phi(a).$$

Then `D=(1-ell)J-(ell-c)H`. The series for phi makes `f=(1-z)(-phi'')` increasing, positive, and bounded by `1/(4ln2)`. Its coefficients are `1/[2(2j+1)(2j+3)ln2]`. Thus

$$\phi(z)+(1-z)\phi'(z)=\int_z^1 f(v)dv\geq(1-z)[1-1/(2\ln2)].$$

Taylor's integral remainder and the bound on f give

$$J\geq a(1-z)\left[\frac{2\ln2-1}{2\ln2}-\frac{a}{8\ln2(1-a)}\right],$$
$$H\leq\frac{a(1-z)}{2\ln2(1-a)}.$$

For t>0 this yields `J/H>887/2500`, whereas `cW/V<=1084/3125`. Their rational margin is `99/12500`. No division is used at t=0. The proof reaches arbitrarily close to epsilon=1/2 and joins the compact domain exactly at c=24/25.

## 4. Independently recomputed compact certificate (B; C4)

For `2^-28<=c<=24/25`, divide D by positive `ca`:

$$D/(ca)=V C_0/c+W C_1-P h_2(t).$$

On a complete rational noise band `[cl,ch]`, P,V,W decrease with c, C0/c decreases by concavity of the discriminant-entropy function, and C1 increases by classical degradation. Hence

$$V C_0/c+W C_1\geq S_-(t):=V(ch)C_0(t,ch)/ch+W(ch)C_1(t,cl).$$

S_- is concave. The submitted rational partition is valid: 512 bands have exact shared endpoints, and each band's input intervals cover `[10^-6,1/2]` without gaps or overlaps, for 29,635 rectangles. Every band's lower input tail is separately enclosed analytically. Exact rational parameter checks reject a different claim or noise range.

### What is independent

`decimal_interval.py` was written for this audit and imports no submitted numerical evaluator. Basic arithmetic uses distinct downward/upward Decimal contexts. Correctly rounded libmpdec ln/exp/sqrt are expanded by one representable value in each direction. Rational parameters enter through exact Fraction values; float inputs are rejected. The implementation depends on the documented correctly-rounded Decimal operations and is not a formal verification of libmpdec itself.

`verify_certificate.py` reads ONLY the rational covering, not saved numerical bounds. It evaluates C1 using the entropy-difference expression. It also replaces the source's midpoint tangent with a different leaf envelope. If the lower secant is `left+k(t-l)`, then an upper bound on its deficit against `P h2(t)` is

$$P\log_2(1+\exp(-k\ln2/P))-\mathrm{left}+kl.$$

The derivative's endpoint signs permit tighter endpoint maxima when the stationary point is outside the leaf. Interval quantities are enclosed outward throughout. An unconstrained maximum is safe when an endpoint sign cannot be certified. This is a different valid upper envelope, not a sample grid or local optimizer.

### Results

Complete checks at 90 and 130 decimal digits pass every rectangle and input tail. At 130 digits, the largest normalized compact upper bound is below `-2.37355635215e-10`; the smallest normalized tail margin exceeds `0.00028189136168` nats. The original integer checker was also rerun at 224 bits and reproduces the submitted `-5.71962366142e-12` compact bound. Different negative margins are expected because the envelopes differ; the assertion proved is the same.

This closes the new all-noise scalar obligation without treating the earlier narrow-band audit as sufficient. Both the analytic endpoint proofs and the machine-checked compact domain are necessary. Precision counts alone do not prove correct inequalities or domain coverage.

## 5. From the entropy lemma to the geometric gap (C; C1, C4)

For `y=a(n_b.u)^2`, the elementary inequality

$$(1-y)^{-1}-(1-y)^{-1/2}\geq y/2$$

implies `G_min>=L+ca*lambda/2`. It holds pointwise before minimization. Compactness of the unit sphere and positive denominators give an attained L for each fixed channel.

Spherical averaging gives `L<=c*asin(sqrt(a))/sqrt(a)`. The positive arcsin power series, bounded after degree two with `pi<22/7`, gives

$$P(a)-\frac{\arcsin\sqrt a}{\sqrt a}>a\left(\frac1{12}+\frac{7a}{40}-\frac{193a^2}{840}\right)\geq a/35.$$

The quadratic is concave with minimum 1/35 at an endpoint. The identity `22/7-pi=integral_0^1 x^4(1-x)^4/(1+x^2) dx>0` supplies the exact pi bound. Since `Tr(T)=1`, lambda<=1/3. Combining both lower bounds with `Gamma>=min(G_min,ell)` proves

$$\Gamma\geq L+(3/35)ca\lambda.$$

No optimizer is used to establish this statement for arbitrary frames. Positive weights and full span imply lambda>0, and all interior common errors have c*a>0. This establishes a nonempty interval for each channel, not a uniform-width interval across all channels.

## 6. All-record collective construction and quantifiers (C; C3)

The inherited proof is inspected in `source/common_noise_range/source/full_span_audit/submitted/noisy_record_full_span/source/record_geometry_criterion/THEORY.md`, Section 3. With antipodal codewords fixed before future choices, put

$$s_b=\sqrt{1-a(n_b.u)^2},\qquad\kappa_b=\frac{a[1-(n_b.u)^2]}{1-a(n_b.u)^2},$$
$$B=\sum_b w_b s_b,\qquad K=\sum_b w_b s_b\kappa_b.$$

Then `B-K=Lambda(u)`. Orthogonality of at least one surviving codeword pair yields a conditional classical entropy A_m; conditional reference entropy C_m gives R_m=A_m-C_m. The exact sum is

$$I_n=\sum_{m=0}^n {n\choose m}(1-p)^{n-m}p^mR_m-p^n A_n.$$

For m=n this is `-p^n C_n`, not zero. It retains the all-measured loss. Selection of central-binomial record classes is used only to bound a sum of positive R or A terms from below; it does not grant postselection to a decoder.

For finitely many axes J, the central-binomial record classes have sign imbalance at most one per axis. Their likelihood ratio is bounded by constants depending on the fixed channel and u, not on m. They contribute at least a polynomial fraction `(m+1)^-J` of the overlaps. The resulting bounds are

$$c_A B^m/(m+1)^J\leq A_m\leq B^m,\qquad
c_R K^m/(m+1)^J\leq R_m\leq K^m.$$

Zeros of individual kappa cause zero R contributions for those record types, not a failure of the inequality. Under full span K>0. The constants can be chosen positive for every fixed interior-error channel. Consequently

$$I_n\geq c_R[1-p+pK]^n/(n+1)^J-(pB)^n.$$

If `p<1/(1+Lambda(u))`, the first exponential dominates at a sufficiently large finite n. Choose u attaining L. Choose this finite n for the fixed channel, epsilon and p. The coding theorem is then applied to the memoryless superchannel N^tensor n, providing a positive asymptotic rate `I_n/n`. It is NOT necessary to have a positive limit of `I_n/n` as the inner n itself tends to infinity. This order of quantifiers is correct and essential. No input state is claimed globally optimal over block codes.

## 7. Retained illustration only (D; C5)

For equal Pauli axes, epsilon=1/10 gives `a=16/25`, `c=9/25`. The scalar/geometry argument has `Gamma>=min(27/59,ell)=27/59`. The matching nearly pure body-diagonal limit makes the inequality an equality. Thus the exact one-use positivity boundary here is 59/86; at p=7/10,

$$I_c(t,u)/h_2(t)\leq -6/295<0\quad(t>0).$$

Pure inputs give zero, so the maximum is exactly zero. The eight-use illustration is established by this sharper intermediate bound. It need not lie inside the most conservative displayed 3/35 interval for it to be a valid illustration of the zero-one-use/positive-capacity phenomenon.

`check_witness.py` uses posterior probabilities and normalized coherence, independently of the source's effect-determinant evaluator. Its 100- and 140-digit enclosures give

$$I_8/8=0.0000747747658815596371016563672617787\ldots>7.47\times10^{-5}.$$

All nine measured-count cases are included. The all-measured probability is exactly 0.05764801 and its weighted block contribution is about -0.01653160578649 bits. The total block value is about 0.00059819812705248 bits. The 140-digit rate enclosure lies inside the 100-digit enclosure, and both agree with the supplied witness. These are rigorous scalar evaluations; no full n=8 density matrix is claimed. This is an asymptotic rate lower bound, not single-block recovery fidelity.

## 8. Cone and noise endpoints (D; C6)

For the cone family, `T=diag((1-lambda)/2,(1-lambda)/2,lambda)`. Convexity of the two squared-projection functions and `u.Tu>=lambda` give exact minima `G_min=c/(1-a*lambda)` and `L=c/sqrt(1-a*lambda)` attained by the axial direction. If lambda<=W/P then G_min<=ell; the global lower bound and axial nearly pure upper bound coincide. Since `4W-P>=0`, lambda<=1/4 suffices for all common interior errors. The expansion of `1/(1+L)-1/(1+Gamma)` at lambda=0 is

$$\frac{ca}{2(1+c)^2}\lambda+O(\lambda^2).$$

This is a difference of one-use and construction thresholds, not an exact all-code phase boundary. No new cone plots or resource-scaling claims were introduced.

At zero record error the effects have rank one and every measured conditional reference is pure. One-use coherent information is `(1-p)S(rho)>0` for a mixed input and p<1. At p=1 the output is classical and has zero quantum capacity. At error1/2 the report is independent of the input; the channel is erasure up to independent flags and has `Q=Q1=max(0,1-2p)`. These exact endpoints have no separation. Coplanar axes give a perpendicular u, with Gamma=L=c, which excludes this strict long-repetition criterion only. The statement does not rule out every finite-code improvement in coplanar channels.

## 9. Final mathematical disposition

A–D of the fixed map support C1–C6. No change to the theorem or one-page claim is required by this audit. The main text should disclose the computer-assisted scalar lemma, give the two-cost proof route, and keep common-error and no-postselection assumptions visible. The independent implementation is not an independent external researcher. No new error model, new code family, new scientific figure, or new capacity claim was added. Original sources remain unchanged.
