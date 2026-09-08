# Audit of the full-span noisy-record theorem

**Date:** 6 September 2026. **Status:** author-side mathematical review with independently written computations. Not external peer review or a proof-assistant formalization.

## Decision and source boundary

No invalidating defect was found in the submitted entropy-comparison proof or the full-span conclusion within its stated domain. The new computations independently certify that domain. No theorem outside the submitted common-error interval is asserted.

Audited submission: `submitted/noisy_record_full_span/`, extracted without modification from `Boundary-Entangling-Susceptibility-noisy-record-full-span-theorem-2026-09-06.zip`, SHA-256 `72bbb29f2e69dc824ae420b350cdf6b922bca56587fa4365c4bf0246ff7e4f51`. All 65 entries in its internal hash manifest match. The original theory and source are retained separately from this audit's code and explanations.

The proof's central definitions are preserved. Put

$$\eta=1-2\epsilon,\quad a=\eta^2,\quad c=1-a,$$
$$T=\sum_b w_b n_b n_b^{\mathsf T},\quad \lambda=\lambda_{\min}(T),$$
$$\Lambda(u)=\sum_b w_b\frac{c}{\sqrt{1-a(n_b\cdot u)^2}},\quad L=\min_{\|u\|=1}\Lambda(u),$$
$$\Gamma=\inf_{\|u\|=1,\ 0<t\leq1/2}\frac{C(t,u)}{h_2(t)}.$$

The channel uses finitely many axes with positive probabilities and one **common** symmetric record error

$$\epsilon\in[999/100000,1001/100000].$$

The intact branch is flagged; the measured branch is destructive and only its correct basis label and noisy sign reach the decoder. Encoding is fixed before the random branch and basis choices. Uses are independent. There is no postselection, preshared entanglement, rereading of measured qubits, or feedback.

## 1. Start from the physical conditional state

A purification of an input with eigenvalues $(1-t,t)$ can be written in the input eigenbasis as $\sqrt{1-t}|00\rangle+\sqrt t|11\rangle$. Conditional on a reported measurement outcome, the subnormalized reference density matrix has trace

$$q_\pm=\frac{1\pm\eta(1-2t)\sqrt x}{2},\qquad x=(n\cdot u)^2,$$

and determinant

$$d=\epsilon(1-\epsilon)t(1-t)=\frac c4t(1-t).$$

Thus the measured-branch conditional entropy is $C_\epsilon(t,x)=F(q_+,d)+F(q_-,d)$ with the submitted homogeneous binary entropy $F$. The basis is known, while the true outcome is not. The new physical verifier first contracts true projectors and then mixes them according to the erroneous report. It does not condition on a true outcome that the decoder lacks.

For the whole flagged channel,

$$I_c(\rho_{t,u},\mathcal N_p)=(1-p)h_2(t)-p C(t,u).$$

Pure inputs give zero. The claimed variational characterization of the zero single-use region follows exactly from the infimum defining $\Gamma$. It does not require that the infimum be attained at a pure or mixed input.

## 2. Integral identity: a direct proof

Let $r_1,r_2$ be the two eigenvalues with sum $q$ and product $d$. Factorization gives

$$v(v+q)+d=(v+r_1)(v+r_2).$$

Integrating the logarithm of the ratio and using $r_1+r_2=q$ to cancel the large-$v$ boundary term gives

$$\int_0^\infty\log\frac{(v+r_1)(v+r_2)}{v(v+q)}\,dv
=q\log q-r_1\log r_1-r_2\log r_2.$$

Division by $\log2$ proves the submitted identity for $F(q,d)$. It also justifies the limiting zero-determinant case by continuity. This derivation checks the normalization and does not merely numerically differentiate the proposed integral.

## 3. The new concavity variable is valid

Set $r=1-2t$ and $g=c/(1-a x)$. The paired integral has integrand

$$\log(A_vg+b)-\log(B_vg+b),$$

where

$$A_v=(v+1/2+d/v)^2-r^2/4,\quad B_v=(v+1/2)^2-r^2/4,\quad b=r^2c/4.$$

For $v>0$, $0<t\leq1/2$, and $0<\epsilon<1/2$, $A_v>B_v>0$ and $b\geq0$. Its second derivative is

$$-\left(\frac{A_v}{A_vg+b}\right)^2+
\left(\frac{B_v}{B_vg+b}\right)^2\leq0.$$

The inequality follows by multiplying positive denominators: $A_v(B_vg+b)\geq B_v(A_vg+b)$. On finite integration ranges the integral is concave, and taking the finite limit retains the inequality. At $t=1/2$, $b=0$ and the integrand is constant in $g$; at $t=0$, continuity gives zero cost.

This lemma is analytic for all strictly interior symmetric error probabilities, not only the certified band. The numerical band enters later, through a scalar inequality required for the full-span implication. No expansion of the full theorem's noise scope follows from the lemma alone.

The same paired integral is increasing and convex in $x$. These two different curvature properties are compatible because $g$ is nonlinear in $x$.

The resulting endpoint chord is

$$C_\epsilon(t,x)\geq\frac{1-g}{1-c}C_0(t)+\frac{g-c}{1-c}C_1(t),$$

with

$$C_0(t)=\mathcal H(4ct(1-t)),\quad
C_1(t)=h_2(t)+h_2(\epsilon)-h_2(\epsilon+\eta t).$$

The normalization is correct: $C_0\geq ch_2(t)$, $C_0\leq C_1\leq h_2(t)$. Hence

$$\beta(t,\epsilon)=\frac{C_1-C_0}{(1-c)h_2(t)}\in[0,1].$$

## 4. Why the compact-domain certificate may use secants

A difference of two concave entropies is not automatically concave. This point deserves an explicit justification, rather than an appeal to coherent-information concavity.

For fixed effects $E_s$, the matrices $\sqrt{E_s}\rho_t\sqrt{E_s}$ are affine in $t$. They have the same eigenvalues as the corresponding conditional-reference matrices and the same outcome probabilities. Placing them in a classical outcome register realizes the cost as a quantum conditional entropy of an affine family. Conditional-entropy concavity therefore gives concavity in $t$. Equivalently, $C_0$ is the increasing-concave composition used by the source, and $C_1$ is a classical conditional entropy of an affine joint distribution.

As $\ell-c>0$ throughout the certified interval, the combination

$$S(t)=(1-\ell)C_0(t)+(\ell-c)C_1(t),\qquad\ell=13/200,$$

is concave for every fixed error probability in the band. Endpoint lower bounds define a secant below every such curve, even when those endpoints were bounded uniformly over the error interval. This validates the domain-enclosure strategy.

## 5. Independent scalar certificates

The required inequality is

$$S(t)\geq\ell(1-c)h_2(t).$$

The source uses Decimal/mpmath intervals and the exact logistic maximizer of an entropy-minus-line envelope. The audit does **not** import those evaluators. It uses a new integer-only dyadic interval implementation and a different upper envelope.

All interval endpoints are integers times $2^{-B}$. Addition, multiplication and division round using exact integer floor/ceiling operations. Square roots are enclosed by integer square roots. Logarithms use dyadic range reduction followed by the positive atanh series

$$\log m=2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}+R_N,\quad
z=(m-1)/(m+1)\in[0,1/3],$$
$$0\leq R_N\leq\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.$$

This replaces both the submitted arithmetic engine and its transcendental-function implementation. It is a purpose-built certificate checker, not a formally verified general-purpose interval library.

For each interval $[l,r]$, the new code subtracts the lower secant of $S$ from the tangent upper bound to $h_2$ at $(l+r)/2$. The difference is linear, so its maximum is bounded at the two endpoints. No numerical optimizer or exponential/logistic evaluation is used. Adaptive splitting continues until every interval proves the required sign.

### Near-pure tail

For $0<t\leq\delta=10^{-6}$, the source's analytic bound was rederived. It follows from the small eigenvalue being at least $ct(1-t)$, elementary lower/upper logarithmic entropy bounds, and concavity of binary entropy at $\epsilon$. After cancellation of the leading $h_2(t)$ terms, the remaining lower bound is $tM/\log2$, with

$$M=(1-\ell)c[(1-\delta)\log(1/c)-\delta\log(1/\delta)-(1+c)\delta]
-(\ell-c)\eta\log[(1-\epsilon)/\epsilon].$$

The audit encloses $M$ using its own integer-series arithmetic. This covers arbitrarily nearly pure inputs; numerical positivity on a finite grid is not used for that domain.

### Results

| Domain | New covering intervals | Largest upper bound on the prohibited quantity | Tail margin, nats |
|---|---:|---:|---:|
| $\epsilon=0.01$ | 27 | below $-5.2492516\times10^{-9}$ | above $0.0051718271377$ |
| Every common $\epsilon\in[0.00999,0.01001]$ | 30 | below $-2.7835397\times10^{-9}$ | above $0.0048060625699$ |

Certificates are constructed at 224 bits and reverified at 320 bits. Every error-band leaf contains the full interval of error probabilities. The new cover is independently generated and need not coincide with the source's 20 intervals. The source's 20-leaf results are also reproduced in the separate unchanged-source rerun.

## 6. Completion of the full-span inequality

Combining the scalar bound with the chord gives

$$C_\epsilon(t,x)/h_2(t)\geq \beta g+(1-\beta)\ell,$$

and therefore $\Gamma\geq\min(G_{\min},\ell)$, where

$$G_{\min}=\min_u\sum_b w_b\frac{c}{1-a(n_b\cdot u)^2}.$$

This does not set $\Gamma=G_{\min}$. The common error is needed because $\beta(t,\epsilon)$ must be identical across all axes in the sum.

The pointwise inequality

$$(1-y)^{-1}-(1-y)^{-1/2}\geq y/2$$

gives $G_{\min}\geq L+ca\lambda/2$. The spherical average gives $L\leq c\arcsin(\eta)/\eta$. The source's series recurrence for this average has ratio less than $a$; its stated geometric remainder is valid. A new integer calculation verifies the positive margin

$$\ell-c\arcsin(\eta)/\eta-ca/6>0$$

over the whole common-error band. Since $\lambda\leq1/3$, this proves

$$\boxed{\Gamma\geq L+ca\lambda/2.}$$

At exactly one-percent error the independently enclosed width coefficient is greater than $0.01697074153$ as claimed. The full-span implication is supported by inequalities uniform over directions and frames, not by a numerical eigenvalue search over selected examples.

## 7. The inherited repetition argument was checked for hidden restrictions

The exact record sum includes a negative all-measured contribution. Its factors arise from products of noisy reported-record likelihoods and conditional coherences. The finite-alphabet lower bound chooses a central binomial sign class for each axis. That keeps the log-likelihood ratio bounded independently of block length, at only polynomial multiplicity cost. The axis probabilities remain inside the multinomial sum.

This yields, for fixed channel and coding direction, constants $c_A,c_R>0$ and finite $J$ such that

$$\frac{c_R}{(n+1)^J}U^n-V^n\leq I_n
\leq U^n-\frac{c_A}{(n+1)^J}V^n,$$

with $U=1-p+pK$ and $V=pB$. The strict inequality $U>V$ implies positive coherent information for a sufficiently large finite block. Constants can depend strongly on the frame, and no uniform practical rate follows. The step from that positive block to $Q>0$ is the standard coding theorem [R1].

Phases of individual record coherences do not change the branch eigenvalues; they are not discarded from the physical channel. The new true-outcome calculation independently checks this reduction for small blocks, including nonorthogonal axes and unequal weights.

## 8. Coplanar limit and exact cone family

For coplanar axes, the perpendicular direction gives $\Gamma=L=c$. Thus the submitted biconditional

$$L<\Gamma\quad\Longleftrightarrow\quad\operatorname{rank}T=3$$

is correct **for this strict long-balanced-repetition comparison and the declared common-error band**. It is not an all-code converse for coplanar channels.

For the cone family at precisely one-percent error, convexity in squared projection and Jensen's inequality prove that the axial direction minimizes the one-use conditional cost at every $t$ and minimizes $\Lambda$. The supplementary isotropic scalar inequality needed to identify $\Gamma$ exactly was rebuilt independently: an analytic tail plus 18 new compact intervals prove $C_{0.01}(t,1/3)\geq(297/5099)h_2(t)$. Concavity in $g$ extends it to all $x\in[0,1/3]$.

Consequently, the submitted formulas

$$\Gamma(\lambda)=c/(1-a\lambda),\qquad L(\lambda)=c/\sqrt{1-a\lambda}$$

survive. The leading gap coefficient is the exact rational

$$\frac{ca}{2(1+c)^2}=\frac{237699}{13509602}.$$

All six submitted sufficient-length certificates were re-evaluated using integer logarithm intervals at 448 bits. The new enclosures lie inside the source's reported enclosures and certify positive logarithmic margins. No full large-block matrix is evaluated or needed for these bounds.

The source correctly proves that every fixed finite balanced axial block remains negative at the limiting coplanar threshold and invokes continuity to exclude a uniform bounded working length along the midpoint path. This is not a lower bound for every possible encoding. Its $O(\lambda^{-1}\log(1/\lambda))$ construction is sufficient, not optimal.

## 9. What this audit does not do

It does not extend the common-noise band, prove the result for arbitrary basis-dependent errors, determine the actual capacity boundary, optimize rates or block lengths, supply an efficient outer decoder, or establish literature priority. It does not modify the original many-body figures or turn the channel theorem into an experimentally observed monitored-circuit result.

No mathematical correction to the submitted full-span statement was required. The more explicit affine-CQ concavity justification, a new analytic tail for the cone endpoint, and a separately implemented integer certificate provide additional verification rather than changed scientific claims.

## References and attribution

[R1] I. Devetak, *The private classical capacity and quantum capacity of a quantum channel*, arXiv:quant-ph/0304127; IEEE Transactions on Information Theory 51, 44–55 (2005). Standard conversion of positive block coherent information to achievable asymptotic quantum rate.

[R2] V. Siddhu and R. B. Griffiths, *Positivity and nonadditivity of quantum capacities using generalized erasure channels*, arXiv:2003.00583v2; IEEE Transactions on Information Theory 67, 4533–4545 (2021). Established identity-plus-auxiliary-channel framework.

[R3] F. Leditzky, D. Leung, and G. Smith, *Dephrasure channel and superadditivity of coherent information*, arXiv:1806.08327v3; Physical Review Letters 121, 160501 (2018). Established repetition-code coherent-information and positivity-threshold methodology. The present classical-record auxiliary channel is not the standard dephrasure output.

The mathematical full-span and scalar statements above are source-derived or audit-derived results, not attributed to R1–R3.
