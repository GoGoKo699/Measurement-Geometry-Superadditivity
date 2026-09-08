# Full span at every nontrivial common reporting-error probability

**6 September 2026. New research result; separate from the accepted many-body manuscript.**

This document extends the previously audited common-error band to the whole open interval `0 < epsilon < 1/2`. The extension uses a new two-parameter entropy inequality with analytic endpoint arguments and a complete interval certificate on the remaining compact domain. It is a computer-assisted mathematical argument, not a sampling-based extrapolation, external review, or proof-assistant formalization. The inherited all-record repetition theorem and its audited source are preserved under `source/full_span_audit/`.

## 1. Model, scope, and main statement

There are finitely many unit Bloch axes $n_b$, with positive probabilities $w_b$ summing to one. Each channel use transmits the qubit intact with probability $1-p$. Otherwise it destructively measures a chosen axis, returns the correct axis label and a reported outcome sign, and makes the measured system unavailable. Each sign has the **same** symmetric acquisition error $e$; different uses are independent. The encoder acts before the random choices. No flags or unfavorable outcomes are postselected, and no feedback or preshared entanglement is supplied.

Set

$$\eta=1-2e,\quad a=\eta^2,\quad c=1-a=4e(1-e),\quad 0<e<1/2,$$
$$E_{b,s}=\frac{I+(-1)^s\eta n_b\cdot\sigma}{2},$$
$$\mathcal N_{p,e}(\rho)=(1-p)\rho\ \oplus\ p\sum_{b,s}w_b\operatorname{Tr}(E_{b,s}\rho)|b,s\rangle\langle b,s|.$$

The noisy classical measurement branch by itself is entanglement breaking. This is the established incomplete-erasure channel form, not a new class of channels.

Define

$$T=\sum_b w_b n_b n_b^{\mathsf T},\qquad\lambda=\lambda_{\min}(T),$$
$$\Lambda(u)=\sum_b\frac{w_b c}{\sqrt{1-a(n_b\cdot u)^2}},\qquad L=\min_{\|u\|=1}\Lambda(u),$$
$$d_e=\frac3{35}ca.$$

**Theorem.** For every such channel, every common error $0<e<1/2$, and every full-span ensemble ($\lambda>0$),

$$\boxed{\frac1{1+L+d_e\lambda}\leq p<\frac1{1+L}
\quad\Longrightarrow\quad Q^{(1)}(\mathcal N_{p,e})=0<Q(\mathcal N_{p,e}).}$$

These are a guaranteed subinterval and a sufficient repetition boundary, not exact regularized-capacity thresholds. No uniformly short block, useful rate, or efficient decoder is claimed. The constant $3/35$ is conservative. The older stronger constant in the narrow one-percent band remains valid; it is not replaced or contradicted by this uniform bound.

For the particular comparison of optimized one-use cost with the strict eventual-sign boundary of balanced antipodal repetitions,

$$\boxed{L<\Gamma\ \Longleftrightarrow\ \operatorname{rank}T=3}$$

throughout the same open error interval. This does **not** exclude every other finite-block or arbitrary-code phenomenon for coplanar channels.

## 2. The globally optimized one-use benchmark

For an input $\rho_{t,u}=[I+(1-2t)u\cdot\sigma]/2$, $0\leq t\leq1/2$, let $C_e(t,x)$ be the measured-branch conditional reference entropy for squared projection $x=(n\cdot u)^2$. Write

$$\mathcal H(z)=h_2\!\left(\frac{1-\sqrt{1-z}}2\right),$$
$$q_\pm=\frac{1\pm\eta(1-2t)\sqrt{x}}2,\qquad d=\frac c4t(1-t),$$
$$C_e(t,x)=\sum_{s=\pm}q_s\mathcal H(4d/q_s^2).$$

Then

$$I_c(t,u)=(1-p)h_2(t)-p\sum_b w_b C_e(t,(n_b\cdot u)^2),$$
$$\Gamma=\inf_{\|u\|=1,\ 0<t\leq1/2}\frac{\sum_b w_b C_e(t,(n_b\cdot u)^2)}{h_2(t)}.$$

Pure inputs give zero coherent information, so

$$Q^{(1)}=0\quad\Longleftrightarrow\quad p\geq\frac1{1+\Gamma}.$$

Every input weight and direction is included. No assumption that the near-pure limit is globally optimal is made.

The audited change of variable

$$g=\frac c{1-ax}$$

makes $C_e(t,x)$ concave in $g$. Its endpoint chord is

$$C_e(t,x)\geq\frac{1-g}{a}C_0(t)+\frac{g-c}{a}C_1(t),$$

where

$$C_0(t)=\mathcal H(4ct(1-t)),\qquad C_1(t)=h_2(t)+h_2(e)-h_2(e+\eta t).$$

The inherited entropy integral proves this concavity for all $0<e<1/2$, not only near one percent. Also $C_0\geq ch_2(t)$, $C_1\leq h_2(t)$, and $C_1\geq C_0$. Thus

$$\beta=\frac{C_1-C_0}{a h_2(t)}\in[0,1].$$

## 3. New global scalar inequality

Define the polynomials

$$P(a)=1+\frac a4+\frac{a^2}4+\frac{a^3}{10},\qquad\ell=cP(a),$$
$$V(a)=\frac34+\frac{3a^2}{20}+\frac{a^3}{10},\qquad W(a)=\frac14+\frac a4+\frac{a^2}{10}.$$

The useful identities are $1-\ell=aV$, $\ell-c=caW$, and $P=V+W$. In particular $c<\ell<1$ for $0<c<1$.

**Entropy lemma.** For every $0<c<1$ and $0\leq t\leq1/2$,

$$\boxed{(1-\ell)C_0(t)+(\ell-c)C_1(t)\geq\ell a h_2(t).}\tag{1}$$

The polynomial was selected using exploratory calculations and then proved on the complete domain. Exploration alone is not the evidence for (1).

Combining (1) with the $g$ chord gives

$$\frac{C_e(t,x)}{h_2(t)}\geq\beta g+(1-\beta)\ell.$$

Because $e$ is common, the same $\beta$ applies to every axis. Therefore

$$\Gamma\geq\min\{G_{\min},\ell\},\qquad G_{\min}=\min_u\sum_b\frac{w_b c}{1-a(n_b\cdot u)^2}.\tag{2}$$

This does not set $\Gamma=G_{\min}$. In fact that equality is false for some larger errors (Section 8).

### 3.1 Analytic low-error endpoint: $0<c\leq2^{-28}$

Put $u=\ln(1/c)$ and $\delta_0=1/100$. The simple bounds $\ell\leq8c/5$, $\ln2>69/100$, $\ln100<5$, and $\ln4<2$ suffice.

For $\delta_0\leq t\leq1/2$, the small eigenvalue in $C_0$ is at least $y=ct(1-t)$. It is in the increasing part of binary entropy. Hence

$$C_0\geq \frac{ct(1-t)u}{\ln2},\quad h_2(t)\leq\frac{t[\ln(1/t)+1]}{\ln2},$$

so $C_0/h_2(t)>1.61c$. On the other hand,

$$\frac{\ell a}{1-\ell}\leq\frac{(8/5)c}{1-(8/5)2^{-28}}<1.61c.$$

The $C_0$ term alone proves (1) on that input range.

For $0<t\leq\delta_0$, elementary entropy bounds give

$$C_0-ch_2(t)\geq\frac{ct}{\ln2}\left[(1-\delta_0)u-\delta_0\ln(1/\delta_0)-(1+c)\delta_0\right],$$
$$h_2(t)-C_1(t)\leq\frac{\eta t}{\ln2}\ln\frac{1-e}{e}.$$

Use $\eta\ln[(1-e)/e]\leq\ln(4/c)$ and $\ell-c\leq3c/5$. After cancellation of the leading $h_2(t)$ term, a strictly positive rational lower bound follows by substituting $u\geq28\ln2>19.32$. The exact rational check is in `analytic_endpoint_constants.json`. The pure endpoint has equality. This argument covers errors arbitrarily close to zero; there is no discarded noise tail.

For completeness, $\ln2>69/100$ follows from the first three positive terms of its atanh series. $\ln100<5$ and $\ln4<2$ follow from finite lower sums for $\exp(5)$ and $\exp(2)$, respectively. No numerical logarithm assumption is needed for these endpoint constants.

### 3.2 Analytic high-error endpoint: $0<a\leq1/25$

This is $2/5\leq e<1/2$. Put $z=(1-2t)^2$ and

$$\phi(z)=h_2((1-\sqrt z)/2),$$
$$J=\phi(a+(1-a)z)-(1-a)\phi(z),\qquad H=\phi(az)-\phi(a).$$

Then (1) is equivalent to $(1-\ell)J\geq(\ell-c)H$.

The series

$$\phi(z)=1-\frac1{\ln2}\sum_{k\geq1}\frac{z^k}{2k(2k-1)}$$

shows that $f(z)=(1-z)[-\phi''(z)]$ is increasing and bounded above by $1/(4\ln2)$. Indeed its positive series coefficients are $1/[2(2j+1)(2j+3)\ln2]$, for $j\geq0$.

Consequently $K(z)=\phi(z)+(1-z)\phi'(z)=\int_z^1f(v)\,dv$ satisfies

$$K(z)\geq(1-z)\left(1-\frac1{2\ln2}\right).$$

Taylor's formula in $a$, and the upper bound on $f$, imply

$$J\geq a(1-z)\left[\frac{2\ln2-1}{2\ln2}-\frac a{8\ln2(1-a)}\right].$$

Also $-\phi'(v)\leq1/[2\ln2(1-a)]$ for $0\leq v\leq a$, so

$$H\leq\frac{a(1-z)}{2\ln2(1-a)}.$$

For $z<1$, the ratio therefore obeys

$$\frac JH\geq(1-a)(2\ln2-1)-\frac a4>\frac{887}{2500}=0.3548.$$

The required ratio is bounded by

$$\frac{\ell-c}{1-\ell}=\frac{cW}{V}\leq\frac{1084}{3125}=0.34688.$$

The positive margin is $99/12500$. This proves (1) up to errors arbitrarily close to one half. The excluded $t=0$ case is equality and needs no division.

### 3.3 Compact noise domain and complete input coverage

It remains to prove (1) for $2^{-28}\leq c\leq24/25$. Normalize the difference by $ca$:

$$\frac{(1-\ell)C_0+(\ell-c)C_1-\ell a h_2(t)}{ca}
=V\frac{C_0}{c}+WC_1-Ph_2(t).$$

The covering contains **512 rational noise bands** and **29,635 rational input intervals** in total. Every band also has an analytical certificate for all $0<t\leq10^{-6}$; the listed intervals exactly cover $[10^{-6},1/2]$. The left and right noise endpoints join with no gaps or overlaps, covering the whole remaining domain.

The proof for an entire noise band $[c_l,c_h]$ uses these monotonicities:

- $P,V,W$ decrease with $c$.
- $C_0(t,c)/c$ decreases with $c$, since $\mathcal H(0)=0$ and $\mathcal H$ is concave.
- $C_1(t,c)$ increases with $c$, since increasing the binary reporting error is classical degradation.

Thus, throughout the noise band,

$$V\frac{C_0(t,c)}c+WC_1(t,c)
\geq V(c_h)\frac{C_0(t,c_h)}{c_h}+W(c_h)C_1(t,c_l)=S_-(t).$$

This lower function is concave in $t$. A secant with rigorously lowered endpoints bounds it below. A tangent bounds $h_2(t)$ above. The upper bound on $P(c_l)h_2(t)-S_-(t)$ is consequently linear on an input leaf and is checked at both endpoints.

The input-tail inequality uses the same elementary estimates as Section 3.1, now with $\delta=10^{-6}$ and all noise dependence enclosed outward. Its minimum normalized positive margin exceeds $0.00028189136168$ across the certified bands.

All compact rectangle upper bounds are strictly negative; the largest is below $-5.71962366142\times10^{-12}$ in the displayed normalization. The integer/dyadic engine built the cover at 128 bits and verified it at 224 bits. An independent mpmath interval backend rechecked every rectangle at 85 decimal digits, using the entropy-difference expression for $C_1$ rather than the Bayesian posterior formula in the first backend. Both agree on the signs and bounds.

These are entire-rectangle enclosures, not a grid of evaluations. The low- and high-noise analytic proofs in Sections 3.1–3.2 close the two remaining open endpoints. Accordingly (1) holds for all $0<c<1$.

## 4. From the scalar inequality to the full-span gap

The inherited angular comparison gives

$$G(u)-\Lambda(u)\geq\frac{ca}{2}u^{\mathsf T}Tu\geq\frac{ca}{2}\lambda,$$

because $(1-y)^{-1}-(1-y)^{-1/2}\geq y/2$ on $[0,1)$. Thus $G_{\min}\geq L+ca\lambda/2$.

To handle the other entry of the minimum in (2), average over directions:

$$L\leq A_e=c\frac{\arcsin\sqrt a}{\sqrt a}.$$

The positive arcsin power series gives

$$\frac{\arcsin\sqrt a}{\sqrt a}\leq1+\frac a6+\frac{3a^2}{40}+
\left(\frac\pi2-\frac{149}{120}\right)a^3.$$

Therefore, using $\pi<22/7$,

$$P(a)-\frac{\arcsin\sqrt a}{\sqrt a}
> a\left(\frac1{12}+\frac{7a}{40}-\frac{193a^2}{840}\right)
\geq\frac a{35}.$$

The quadratic is concave; its minimum on $[0,1]$ is the smaller endpoint value, $1/35$. One may certify the familiar bound on $\pi$ directly from $22/7-\pi=\int_0^1x^4(1-x)^4/(1+x^2)\,dx>0$.

Since $\lambda\leq1/3$,

$$\ell>L+\frac{ca}{35}\geq L+\frac3{35}ca\lambda.$$

Combining with (2) proves

$$\boxed{\Gamma\geq L+\frac3{35}ca\lambda.}$$

The threshold region in Section 1 follows from the exact characterization of $Q^{(1)}$ and the inherited all-record repetition theorem. The proof retains the same operation budget and does not grant the encoder knowledge of future axes or outcomes.

The guaranteed interval width is

$$\Delta p_{\mathrm{cert}}=\frac{d_e\lambda}{(1+L)(1+L+d_e\lambda)}
\geq\frac{d_e}{(1+A_e)(1+A_e+d_e/3)}\lambda.$$

This conservative lower coefficient is evaluated in `noise_gap_bounds.csv`. Its order is $\Theta(e)$ near perfect records and $\Theta((1/2-e)^2)$ near fully random records. It is not a rate bound or a claim of a uniform practical advantage.

## 5. Coplanar axes and the two noise endpoints

If the axes do not span $\mathbb R^3$, choose a common perpendicular $u$. Then $G(u)=\Lambda(u)=c$. The lower bound $C_e(t,x)\geq C_0(t)\geq c h_2(t)$ gives $\Gamma\geq c$, while a nearly pure perpendicular input approaches $c$. Hence $\Gamma=L=c$ for every interior error. This proves the construction-specific equivalence in Section 1.

At **$e=0$**, the conditional reference in the measured branch is pure, so $I_c=(1-p)S(\rho)$. Single-use coherent information is positive for every $p<1$. At $p=1$ the channel is quantum-to-classical, so $Q=0$. There is no $Q^{(1)}=0<Q$ region.

At **$e=1/2$**, the record is independent of the input. The channel is an erasure channel up to independent flags, with $Q=Q^{(1)}=\max\{0,1-2p\}$. There is again no separation. Full geometric span of the nominal axes does not make the effects informationally complete when $\eta=0$.

Thus the open noise interval in the theorem is meaningful. Known outcome inversion maps errors above one half to errors below one half, but the reporting convention here restricts errors to $[0,1/2]$.

## 6. Exact nearly coplanar family for the whole noise interval

For the equal-probability three-axis cone family of the earlier work,

$$n_j=(\sqrt{1-\lambda}\cos(2\pi j/3),\sqrt{1-\lambda}\sin(2\pi j/3),\sqrt\lambda),$$

$T=\operatorname{diag}((1-\lambda)/2,(1-\lambda)/2,\lambda)$. For $0\leq\lambda\leq1/3$, convexity in squared projection and the frame bound make the axial direction minimize $G$ and $\Lambda$:

$$G_{\min}=\frac c{1-a\lambda},\qquad L=\frac c{\sqrt{1-a\lambda}}.$$

If $\lambda\leq W(a)/P(a)$, then $G_{\min}\leq\ell$. Equation (2) and the opposite near-pure upper bound imply equality:

$$\Gamma=\frac c{1-a\lambda}\quad\text{for}\quad0\leq\lambda\leq\min\{1/3,W/P\}.$$

Since $W/P\geq1/4$, this gives an exact one-use formula for **all common interior errors and every cone parameter $\lambda\leq1/4$**. In particular,

$$p_{\mathrm{rep}}-p_1=\frac{ca}{2(1+c)^2}\lambda+O(\lambda^2)$$

as the cone approaches its plane, for every fixed interior error. It is still a construction threshold, not full capacity.

Moreover $3W-P=(2a-1)(5-a^2)/20$. Thus $a\geq1/2$ suffices for the exact formula over the entire cone range through $\lambda=1/3$. For the equal-Pauli channel this supplies an exact single-use positivity threshold throughout

$$0<e\leq\frac{1-1/\sqrt2}{2}\approx0.1464466094.$$

This additional expression is not extended to all errors. See the counterexample next.

## 7. New finite witnesses far outside the original noise band

For the equal-Pauli channel, the global lower bound $\Gamma\geq\min\{c/(1-a/3),\ell\}$ proves a one-use zero region. Balanced body-diagonal repetition inputs give the following directed-interval-positive per-use values:

| Error | Measurement probability | Inner block | Certified approximate rate lower witness |
|---:|---:|---:|---:|
| 0.10 | 0.70 | 8 | $7.4774765881\times10^{-5}$ |
| 0.20 | 0.59 | 16 | $3.9165766753\times10^{-7}$ |
| 0.30 | 0.536 | 48 | $3.4604346547\times10^{-17}$ |
| 0.40 | 0.5078 | 64 | $8.5121193975\times10^{-23}$ |

All four have globally zero one-use coherent information by the new bound. All mask and reported-record branches, including the negative all-measured contribution, are included. These are inner-block coherent-information rates with an outer-coding interpretation, not one-shot fidelities or efficient decoding schemes.

The primary calculation uses 125-digit mpmath intervals and a positive-sum discriminant for unnormalized effect determinants. A separate inherited Decimal posterior-state evaluator at 150 digits independently encloses each witness inside the outward-rounded primary records.

An exploratory double-precision candidate at $e=0.4,p=0.5083,n=64$ was rejected: the interval calculation gives a **negative** value, approximately $-8.01285455\times10^{-23}$. It is retained as a negative numerical control, not counted as a witness. This illustrates why near-cancellation of block contributions cannot be judged by ordinary floating-point sign alone.

## 8. A check against an incorrect noise extrapolation

For equal Pauli axes at $e=1/5$, the near-pure cost is $G_{\min}=8/11$. Blindly identifying that cost with $\Gamma$ would incorrectly claim a one-use zero at $p=11/19$.

The maximally mixed input actually has

$$I_c=\frac{8-11h_2(1/5)}{19}>0.$$

This is checked with directed intervals in `mixed_input_control.json`. Interior input weights can matter at larger errors. The new proof avoids this problem by lower bounding the full optimization; it does not merely extend the old near-pure formula in the noise parameter.

## 9. Evidence, dependency, and limits

The computer-assisted part is exactly the compact-domain proof of (1). The two unbounded noise endpoints and the nearly pure input tails are analytic. Both interval backends check complete rectangles and rational coverage. The integer engine is inherited from the prior audit; the polynomial, endpoint proofs, noise-monotonic lower envelope, and certificate cover are new. The alternative backend uses different entropy expressions and no integer-engine import.

New physical checks explicitly contract hidden true outcomes and mix them into imperfect reports before computing full receiver/reference entropies. They corroborate the formulas but do not prove the universal entropy lemma. Neither those checks nor the certificate is external review.

Common symmetric errors, independent uses, finite axes, intact surviving qubits, correct mask and basis labels, no postselection, and unavailable measured systems remain substantive restrictions. The theorem does not cover arbitrary per-axis errors, asymmetric errors, basis-label errors, correlated noise, or arbitrary encoders learning future randomness. It does not solve capacity, guarantee a significant rate, or exclude all coplanar coding improvements. The channel class, general coherent-information nonadditivity, and repetition coding are established antecedents. Priority for this precise all-common-noise full-span theorem remains to be checked.
