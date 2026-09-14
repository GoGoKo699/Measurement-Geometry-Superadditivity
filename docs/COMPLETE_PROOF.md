# Complete proof source: the common-noise full-span theorem

**Canonical scientific source, version 1 · 8 September 2026**

This is a consolidation of the supplied theorem and its final author-side audit, not a new result, manuscript draft or repeated audit. Required inherited lemmas are written directly below. Section-level provenance, exact source hashes and code/evidence identities are in [SOURCE_TO_CANONICAL.md](SOURCE_TO_CANONICAL.md). The notation agrees with [MODEL_AND_CLAIMS.md](MODEL_AND_CLAIMS.md); documentary renamings are explicit in [NOTATION_CROSSWALK.md](NOTATION_CROSSWALK.md).

**Meaning of “complete.”** The analytical dependency chain for retained claims C1–C6 is present in this document. The computer-assisted scalar lemma is tied to the preserved rational certificate and separate checkers, not replaced by a narrative assertion. Standard external tools are quantum conditional-entropy concavity, Pinsker's inequality, the coherent-information coding theorem, and the erasure-capacity endpoint; their supplied references and roles are listed in [REFERENCES.md](REFERENCES.md). The earlier prose consolidation imported the recorded verification status. The current baseline separately reports checks after executable relocation in [BASELINE_VALIDATION.json](../validation/BASELINE_VALIDATION.json); these do not constitute external verification of the theorem or arithmetic libraries. Absolute priority is a separate, bounded source assessment.

## Reading route

[P01](#p01) defines the physical channel and global one-use benchmark. [P02–P03](#p02) supply the elementary entropy tools and the transformed-variable comparison. [P04–P07](#p04) state and justify the all-noise scalar inequality, including the analytical tails and computer certificate. [P08](#p08) produces the geometric gap. [P09–P10](#p09) give the full all-record collective construction and capacity implication. [P11–P13](#p11) cover the retained limits and eight-use illustration. [P14–P15](#p14) specify the computational evidence boundary and completeness status.

<a id="p01"></a>
## P01. Physical channel and exact single-use positivity criterion

**Sources:** [S3](SOURCE_TO_CANONICAL.md#s3); [S4](SOURCE_TO_CANONICAL.md#s4) §§1–2; [S5](SOURCE_TO_CANONICAL.md#s5) §1. **Claims:** C1–C3.

Fix finitely many unit axes $\mathbf n_b$, positive probabilities $w_b$, a common $0<\epsilon<1/2$, and independent channel uses. Let $r$ denote the true projective bit and $s$ the reported bit. The projectors and reporting probabilities are

$$\Pi_{b,r}=\frac{I+(-1)^r\mathbf n_b\cdot\boldsymbol\sigma}{2},\qquad
\Pr(s\mid r)=\begin{cases}1-\epsilon,&s=r,\\\epsilon,&s\ne r.\end{cases}$$

The physical qubit is discarded after measurement. Summing over the hidden true bit gives

$$E_{b,s}=\sum_r\Pr(s\mid r)\Pi_{b,r}
=\frac{I+(-1)^s\eta\mathbf n_b\cdot\boldsymbol\sigma}{2},\quad\eta=1-2\epsilon.$$

The channel is

$$
\begin{aligned}
\mathcal N_{p,\epsilon}(\rho)&=(1-p)\rho\oplus\\
&\quad p\sum_{b,s}w_b\,\mathrm{Tr}(E_{b,s}\rho)|b,s\rangle\langle b,s|.
\end{aligned}
$$

The encoder knows the channel parameters, not the future branch, axis or outcomes. There is no assistance, postselection or rereading. The two receiver branches have orthogonal flags, and the axis probability sits outside each fixed-axis effect.

Write $a=\eta^2$ and $c=1-a=4\epsilon(1-\epsilon)$. An arbitrary input has eigenvalues $(1-t,t)$ with $0\leq t\leq1/2$ and eigenvectors $|\mathbf u_+\rangle,|\mathbf u_-\rangle$. A purification is

$$|\Psi_{t,\mathbf u}\rangle=\sqrt{1-t}|0\rangle_{\mathsf R}|\mathbf u_+\rangle
+\sqrt t|1\rangle_{\mathsf R}|\mathbf u_-\rangle.$$

In this input eigenbasis, put $D_t=\mathrm{diag}(\sqrt{1-t},\sqrt t)$. The fixed-axis subnormalized reference state for reported outcome $s$ is

$$\tau_{b,s}=D_t(E_{b,s}^{(\mathbf u)})^{\mathsf T}D_t.$$

The transpose is fixed by the purification convention; it does not alter the eigenvalue formulas below. Its trace and determinant are

$$q_{b,s}=\frac{1+(-1)^s\eta(1-2t)\mathbf n_b\cdot\mathbf u}{2},\qquad
\det\tau_{b,s}=\Delta_t=\frac c4t(1-t).$$

For a positive $2\times2$ matrix with trace $q$ and determinant $\Delta$, define its homogeneous entropy

$$F(q,\Delta)=q\,h_2\!\left(\frac{1-\sqrt{1-4\Delta/q^2}}2\right).$$

The entropy cost averaged within the measured branch is

$$C(t,\mathbf u)=\sum_{b,s}w_b F(q_{b,s},\Delta_t).$$

Equivalently, with $x=(\mathbf n\cdot\mathbf u)^2$ and $\mathcal H(z)=h_2((1-\sqrt{1-z})/2)$,

$$
\begin{aligned}
q_\pm&=\frac{1\pm\eta(1-2t)\sqrt x}{2},\\
C_\epsilon(t,x)&=\sum_{\pm}q_\pm\mathcal H(4\Delta_t/q_\pm^2),\\
C(t,\mathbf u)&=\sum_b w_b C_\epsilon(t,(\mathbf n_b\cdot\mathbf u)^2).
\end{aligned}
$$

These are entropies conditioned on the **reported** bit, not on the hidden true bit. Because the two main flags and classical measured records are shared in the entropy difference, their Shannon entropies cancel. The intact branch contributes $h_2(t)$ and the measured branch contributes $-C(t,\mathbf u)$:

$$\boxed{I_c(\rho_{t,\mathbf u},\mathcal N_{p,\epsilon})=(1-p)h_2(t)-pC(t,\mathbf u).} \tag{P1.1}$$

For $t=0$, the reference is one dimensional and the coherent information is exactly zero. For all mixed inputs define

$$\Gamma=\inf_{\|\mathbf u\|=1,\ 0<t\leq1/2}\frac{C(t,\mathbf u)}{h_2(t)}.$$

If $p\geq1/(1+\Gamma)$, every mixed input has nonpositive coherent information, while pure inputs attain zero. Conversely, if $0<p<1/(1+\Gamma)$, the definition of the infimum supplies a positive $t$ and direction with $C/h_2<(1-p)/p$. At $p=0$ any mixed input gives positive coherent information directly. Hence

$$\boxed{Q^{(1)}(\mathcal N_{p,\epsilon})=0\quad\Longleftrightarrow\quad p\geq p_1:=\frac1{1+\Gamma}.} \tag{P1.2}$$

No optimizing direction or input weight has been presumed. For later use, the full-rank fixed-error posterior expansion gives the directional nearly pure ratio

$$\lim_{t\downarrow0}\frac{C(t,\mathbf u)}{h_2(t)}
=G(\mathbf u):=\sum_b\frac{w_b c}{1-a(\mathbf n_b\cdot\mathbf u)^2}.$$

Thus $\Gamma\leq G_{\min}:=\min_{\mathbf u}G(\mathbf u)$. Equality requires an additional argument and is not used as a general premise. The countercontrol in [P13.4](#p134) illustrates why.

<a id="p02"></a>
## P02. Elementary entropy tools used below

**Sources:** [S8](SOURCE_TO_CANONICAL.md#s8) §3.2; [S9](SOURCE_TO_CANONICAL.md#s9) §§2–3, 7; [S10](SOURCE_TO_CANONICAL.md#s10) §5; [S4](SOURCE_TO_CANONICAL.md#s4) §§2–3; [S5](SOURCE_TO_CANONICAL.md#s5) §§2–3. **Claims:** C2–C4.

The retained proof uses the following standard binary-entropy and quantum-entropy facts. They are explicit assumptions/tools of the source proof, not new results of this consolidation.

For $0\leq x,\chi\leq1$, let

$$D_\chi(x)=h_2(x)-\mathcal H(4(1-\chi)x(1-x)).$$

This is the entropy decrease when a qubit's diagonal $(1-x,x)$ gains squared normalized coherence $\chi$. The source uses

$$h_2(x)\leq2\sqrt{x(1-x)},\qquad
\frac2{\ln2}\chi x(1-x)\leq D_\chi(x)\leq\chi h_2(x). \tag{P2.1}$$

For the lower bound, diagonal dephasing gives a relative-entropy difference $D_\chi(x)$. Pinsker's inequality and the trace norm $2\sqrt{\chi x(1-x)}$ of the off-diagonal difference give the displayed coefficient in bits. For the upper bound, $D_\chi(x)$ is convex in $\chi$ with endpoint values $0,h_2(x)$; its endpoint chord bounds it above. This follows from the concavity of the square-root form of binary entropy used in the source. The first inequality is the inherited binary-entropy overlap bound. Its role is to convert a sum of conditional entropies to a product of record overlaps.

The determinant-entropy function $\mathcal H$ is increasing and concave on $[0,1]$, with $\mathcal H(0)=0$. In particular,

$$\mathcal H(cy)\geq c\mathcal H(y),\qquad 0\leq c,y\leq1. \tag{P2.2}$$

For fixed measurement effects and a fixed input direction, the cost $C_\epsilon(t,x)$ is concave in $t$. The source's correct justification is an affine classical–quantum representation: the blocks $\sqrt{E_s}\rho_t\sqrt{E_s}$ depend affinely on $t$, and have the same nonzero spectra and traces as the conditional-reference blocks. The average conditional entropy is concave on this affine family. This is **not** an inference from subtracting arbitrary concave scalar entropies. It will justify the lower secants in [P07](#p07).

An increase of symmetric reporting error within $[0,1/2]$ can be implemented as additional classical sign flips. Such processing cannot decrease the average conditional-reference entropy. This fixes the direction of the noise-monotonic bound used in the certificate.

<a id="p03"></a>
## P03. Entropy integral and the comparison variable

**Sources:** [S9](SOURCE_TO_CANONICAL.md#s9) §§2–4; [S5](SOURCE_TO_CANONICAL.md#s5) §2; [S4](SOURCE_TO_CANONICAL.md#s4) §2; [S10](SOURCE_TO_CANONICAL.md#s10) §2. **Claims:** C2, C4.

### P03.1 Integral identity

Let $r_1,r_2\geq0$ be the two unnormalized eigenvalues of a conditional state. They have sum $q$ and product $\Delta$. Factorization gives

$$v(v+q)+\Delta=(v+r_1)(v+r_2).$$

Integrating the logarithm of the ratio on $v\in(0,\infty)$ and using $r_1+r_2=q$ to cancel the large-$v$ boundary term gives

$$\int_0^\infty\ln\left(1+\frac{\Delta}{v(v+q)}\right)dv
=q\ln q-r_1\ln r_1-r_2\ln r_2.$$

Consequently,

$$\boxed{F(q,\Delta)=\frac1{\ln2}\int_0^\infty\ln\left(1+\frac{\Delta}{v(v+q)}\right)dv.} \tag{P3.1}$$

Zero determinant is handled by continuity; it is not evaluated by an undefined logarithm expression.

### P03.2 Two compatible curvature statements

For fixed $t,\epsilon$, put $r_t=1-2t$ and

$$g=\frac{c}{1-ax}\in[c,1].$$

Pairing the two reports in (P3.1) yields an integrand

$$\ln(\mathsf A_v g+\zeta_t)-\ln(\mathsf B_v g+\zeta_t),$$

where

$$
\begin{aligned}
\mathsf A_v&=(v+1/2+\Delta_t/v)^2-r_t^2/4,\\
\mathsf B_v&=(v+1/2)^2-r_t^2/4,\\
\zeta_t&=r_t^2c/4.
\end{aligned}
$$

For interior inputs and $v>0$, $\mathsf A_v>\mathsf B_v>0$, $\zeta_t\geq0$. Its second derivative in $g$ is

$$-\left(\frac{\mathsf A_v}{\mathsf A_vg+\zeta_t}\right)^2
+\left(\frac{\mathsf B_v}{\mathsf B_vg+\zeta_t}\right)^2\leq0.$$

Thus $C_\epsilon(t,x)$ is concave as a function of $g$. At $t=1/2$ the integrand is constant in $g$; at $t=0$ use the pure-input limit.

In the original squared-projection variable, the paired integrand instead has the form

$$
\begin{aligned}
&\ln\frac{A_v-\omega_x/4}{B_v-\omega_x/4},\\
A_v&=(v+1/2+\Delta_t/v)^2,\\
B_v&=(v+1/2)^2,\\
\omega_x&=ar_t^2x.
\end{aligned}
$$

Its first derivative in $\omega_x$ is nonnegative and its second is

$$\frac1{16}\left[(B_v-\omega_x/4)^{-2}-(A_v-\omega_x/4)^{-2}\right]\geq0.$$

Therefore the paired cost is increasing and convex in $x$. The two statements do not conflict: $x\mapsto g$ is nonlinear. They support different parts of the proof.

### P03.3 The endpoint chord

Define the endpoint costs, with $\epsilon$ fixed,

$$
\begin{aligned}
C_\perp(t)&=\mathcal H(4ct(1-t)),\\
C_\parallel(t)&=h_2(t)+h_2(\epsilon)-h_2(\epsilon+\eta t).
\end{aligned}
$$

The second expression is classical conditional entropy for a noisy binary record of an input aligned with its measurement axis. Concavity in $g$ gives

$$C_\epsilon(t,x)\geq\frac{1-g}{a}C_\perp(t)+\frac{g-c}{a}C_\parallel(t). \tag{P3.2}$$

The previous facts imply

$$C_\perp(t)\geq c h_2(t),\qquad
C_\perp(t)\leq C_\parallel(t)\leq h_2(t).$$

For $t>0$ define

$$\beta(t,\epsilon)=\frac{C_\parallel(t)-C_\perp(t)}{a h_2(t)}\in[0,1].$$

Rearranging the chord,

$$\frac{C_\epsilon(t,x)}{h_2(t)}
\geq\beta g+\frac{C_\perp(t)-c\beta h_2(t)}{h_2(t)}. \tag{P3.3}$$

The next scalar inequality controls this intercept for all interior errors and all input weights. The same $\beta$ will apply to every axis precisely because the error is common.

<a id="p04"></a>
## P04. The all-common-noise scalar lemma

**Sources:** [S4](SOURCE_TO_CANONICAL.md#s4) §3; [S5](SOURCE_TO_CANONICAL.md#s5) §§3–4; source [C1](SOURCE_TO_CANONICAL.md#c1)–[C2](SOURCE_TO_CANONICAL.md#c2) and [V1](SOURCE_TO_CANONICAL.md#v1)–[V9](SOURCE_TO_CANONICAL.md#v9). **Claims:** C2, C4.

Define

$$P(a)=1+\frac a4+\frac{a^2}4+\frac{a^3}{10},\qquad \ell=cP(a),$$

$$V(a)=\frac34+\frac{3a^2}{20}+\frac{a^3}{10},\qquad
W(a)=\frac14+\frac a4+\frac{a^2}{10}.$$

The exact identities

$$1-\ell=aV(a),\quad \ell-c=caW(a),\quad P=V+W$$

show that $c<\ell<1$ for $0<c<1$. The submitted computer-assisted entropy lemma is

$$\boxed{\mathscr D(t,c):=(1-\ell)C_\perp(t)+(\ell-c)C_\parallel(t)-\ell a h_2(t)\geq0} \tag{P4.1}$$

for every $0<c<1$ and $0\leq t\leq1/2$. The proof has three domains: [P05](#p05) handles $0<c\leq2^{-28}$, [P06](#p06) handles $0<a\leq1/25$, and [P07](#p07) covers the remaining compact noise domain and its entire input range. These arguments jointly cover the whole open error interval; no sampling interpolation is used.

When (P4.1) is combined with (P3.3),

$$C_\perp-c\beta h_2(t)\geq(1-\beta)\ell h_2(t),$$

and therefore

$$\frac{C_\epsilon(t,x)}{h_2(t)}\geq\beta g+(1-\beta)\ell.$$

For each input weight, $\beta(t,\epsilon)$ is independent of the axis label. Summing over $b$ and taking the global infimum gives

$$\boxed{\Gamma\geq\min\{G_{\min},\ell\}.} \tag{P4.2}$$

The bound is not the equality $\Gamma=G_{\min}$. Nor does this common-coefficient step prove the same result for independently varied axis-dependent errors.

<a id="p05"></a>
## P05. Analytical low-noise endpoint

**Sources:** [S4](SOURCE_TO_CANONICAL.md#s4) §3.1; [S5](SOURCE_TO_CANONICAL.md#s5) §3; source [C1](SOURCE_TO_CANONICAL.md#c1)–[C2](SOURCE_TO_CANONICAL.md#c2). **Claim:** C4.

Let $0<c\leq c_*=2^{-28}$, $\zeta=\ln(1/c)$ and $\delta_0=1/100$. The source uses

$$\ell\leq\frac85c,\quad \ell-c\leq\frac35c,\quad
\ln2>\frac{69}{100},\quad\ln100<5,\quad\ln4<2.$$

The logarithm bounds have elementary rational certificates: three positive terms in the atanh series for $\ln2$, and finite lower exponential sums for $\exp(5)$ and $\exp(2)$, suffice. Their recorded exact checks are source C2, not recomputed here.

### P05.1 Input weights $\delta_0\leq t\leq1/2$

The smaller eigenvalue for $C_\perp$ is at least $y=ct(1-t)$ and lies below one half. Monotonicity of binary entropy and its nonnegative terms yield

$$C_\perp(t)\geq\frac{ct(1-t)\zeta}{\ln2},\qquad
h_2(t)\leq\frac{t[\ln(1/t)+1]}{\ln2}.$$

Since $\zeta\geq28\ln2>19.32$, $1-t\geq1/2$ and $\ln(1/t)<5$, the ratio exceeds $1.61c$. On the other hand,

$$\frac{\ell a}{1-\ell}\leq\frac{(8/5)c}{1-(8/5)c_*}<1.61c.$$

The $C_\perp$ term alone proves (P4.1); the nonnegative $C_\parallel$ term need not be used.

### P05.2 Arbitrarily nearly pure inputs

For $0<t\leq\delta_0$, the source entropy bounds give

$$C_\perp(t)-c h_2(t)\geq\frac{ct}{\ln2}
\left[(1-\delta_0)\zeta-\delta_0\ln(1/\delta_0)-(1+c)\delta_0\right],$$

$$h_2(t)-C_\parallel(t)\leq\frac{\eta t}{\ln2}\ln\frac{1-\epsilon}{\epsilon}.$$

Use $\eta\ln((1-\epsilon)/\epsilon)\leq\ln(4/c)$ and the exact cancellation

$$\mathscr D=(1-\ell)(C_\perp-c h_2)- (\ell-c)(h_2-C_\parallel).$$

After applying the conservative bounds above, the coefficient of $\zeta$ is positive. Substitution at $c=c_*$ and $\zeta>19.32$ gives the recorded strictly positive lower margin

$$\frac{706479660745902522393}{112589990684262400000}$$

for the normalized low-noise tail expression. The exact compact-input comparison margin used in P05.1 is

$$\frac{167771999}{16777215900}>0.$$

These rational values are read from source C2; their functional use is the argument just given. The proof covers all positive $c$ in this range and all $t>0$, however small. At $t=0$, (P4.1) is equality.

<a id="p06"></a>
## P06. Analytical high-noise endpoint

**Sources:** [S4](SOURCE_TO_CANONICAL.md#s4) §3.2; [S5](SOURCE_TO_CANONICAL.md#s5) §3; source [C1](SOURCE_TO_CANONICAL.md#c1)–[C2](SOURCE_TO_CANONICAL.md#c2). **Claim:** C4.

Let $0<a\leq1/25$, equivalently $2/5\leq\epsilon<1/2$, and set

$$z=(1-2t)^2,\qquad\phi(z)=h_2\left(\frac{1-\sqrt z}{2}\right).$$

Define the explicitly labeled high-noise functions

$$J_\phi=\phi(z+a(1-z))-(1-a)\phi(z),\qquad
H_\phi=\phi(az)-\phi(a).$$

Then $\mathscr D=(1-\ell)J_\phi-(\ell-c)H_\phi$. The convergent entropy series is

$$\phi(z)=1-\frac1{\ln2}\sum_{k\geq1}\frac{z^k}{2k(2k-1)}.$$

It makes $f(z)=(1-z)[-\phi''(z)]$ positive and increasing, with upper bound $1/(4\ln2)$; its coefficients are

$$\frac1{2(2j+1)(2j+3)\ln2},\qquad j\geq0.$$

The source's derivative identity and integral representation give

$$K_\phi(z)=\phi(z)+(1-z)\phi'(z)=\int_z^1 f(v)\,dv
\geq(1-z)\left(1-\frac1{2\ln2}\right).$$

Taylor's integral remainder in $a$, bounded using $f$, yields

$$J_\phi\geq a(1-z)\left[\frac{2\ln2-1}{2\ln2}-\frac{a}{8\ln2(1-a)}\right].$$

Also $-\phi'(v)\leq1/[2\ln2(1-a)]$ for $0\leq v\leq a$, hence

$$H_\phi\leq\frac{a(1-z)}{2\ln2(1-a)}.$$

For $t>0$ the required ratio is controlled by

$$\frac{J_\phi}{H_\phi}\geq(1-a)(2\ln2-1)-\frac a4>\frac{887}{2500},$$

while

$$\frac{\ell-c}{1-\ell}=\frac{cW(a)}{V(a)}\leq\frac{1084}{3125}.$$

The gap is $99/12500>0$, proving (P4.1) on the whole high-noise region. These coefficient identities and rational constants are recorded in source C2. At $t=0$, one uses equality rather than dividing by a vanishing entropy difference. This argument reaches arbitrarily close to $\epsilon=1/2$; the endpoint itself is addressed physically in [P11](#p11).

<a id="p07"></a>
## P07. Complete compact-domain certificate and its verification boundary

**Sources:** [S4](SOURCE_TO_CANONICAL.md#s4) §3.3; [S5](SOURCE_TO_CANONICAL.md#s5) §4; [V1](SOURCE_TO_CANONICAL.md#v1)–[V9](SOURCE_TO_CANONICAL.md#v9); source [C1](SOURCE_TO_CANONICAL.md#c1)–[C2](SOURCE_TO_CANONICAL.md#c2). **Claims:** C2, C4.

### P07.1 Precisely what is certified

For

$$c_*:=2^{-28}\leq c\leq\frac{24}{25},\qquad 0<t\leq\frac12,$$

divide (P4.1) by the positive factor $ca$:

$$\frac{\mathscr D}{ca}=V(a)\frac{C_\perp(t,c)}c+W(a)C_\parallel(t,c)-P(a)h_2(t). \tag{P7.1}$$

Here $C(t,c)$ means the endpoint cost evaluated at the unique $\epsilon=(1-\sqrt{1-c})/2$ in $[0,1/2]$. To make the source code's coefficient argument explicit, define

$$\bar P(c)=P(1-c),\quad\bar V(c)=V(1-c),\quad\bar W(c)=W(1-c).$$

Each barred coefficient decreases with $c$. By concavity of $\mathcal H$ with $\mathcal H(0)=0$, $C_\perp(t,c)/c$ decreases with $c$. By additional classical sign noise, $C_\parallel(t,c)$ increases with $c$.

For every complete noise band $[c_l,c_h]$, a lower bound on the positive cost terms in (P7.1) is

$$S_-(t)=\bar V(c_h)\frac{C_\perp(t,c_h)}{c_h}+\bar W(c_h)C_\parallel(t,c_l). \tag{P7.2}$$

For all $c$ in that band, the quantity to bound above is

$$\bar P(c_l)h_2(t)-S_-(t).$$

This is an enclosure over the **whole noise band**, not evaluation at two putative representative channels.

### P07.2 Lower input tail in every band

With $d:=\delta_{\mathrm{cert}}=10^{-6}$, the same elementary input-tail argument as P05.2 gives

$$\mathscr D(t,c)\geq\frac{ct}{\ln2}\mu(c),\qquad 0<t\leq\delta_{\mathrm{cert}}.$$

Define the tail bracket and the resulting outward lower enclosure by

$$
\begin{aligned}
B_d(c)&:=(1-d)\ln(1/c)-d\ln(1/d)-(1+c)d,\\
\mu(c)&=(1-c\bar P(c))B_d(c)\\
&\quad-(\bar P(c)-1)\eta\ln\frac{1-\epsilon}{\epsilon}.
\end{aligned}
\tag{P7.3}
$$

The saved checks certify $\mu>0$ throughout every noise band. Thus the compact computation omits no arbitrarily nearly pure input. The value $10^{-6}$ is a junction between two proofs, not a lower cutoff on admissible inputs. The margin called `tail` in the source code is this normalized expression; it is not a physical communication rate.

### P07.3 Every remaining rectangle

The immutable certificate **V1** supplies 512 exact-rational noise bands and 29,635 exact-rational input intervals in total. For each noise band, its listed intervals join exactly and cover $[\delta_{\mathrm{cert}},1/2]$. The noise bands join exactly and cover $[c_*,24/25]$.

$S_-(t)$ is concave in $t$ by P02. Therefore the line through outward-lowered endpoint values on an input interval $[l,r]$ lies below $S_-$ throughout that interval. The original integer checker uses a tangent upper bound for $h_2(t)$ and checks the resulting linear deficit at both ends. The mpmath checker uses the same proof obligations but a different arithmetic backend and a different expression for the parallel conditional entropy.

The final audit checker uses a separately written Decimal implementation and a different scalar envelope. For a lower secant $s_l+k(t-l)$ and an upper enclosure $P_+$ for $\bar P(c_l)$, the unrestricted entropy-conjugate upper bound is

$$P_+\log_2\!\left(1+\exp\left[-\frac{k\ln2}{P_+}\right]\right)-s_l+kl.$$

Derivative signs permit endpoint maxima when the stationary point is outside the interval. Using the unrestricted maximum when a sign is unresolved remains safe. The checker recomputes these bounds; it does not trust saved claimed negativity in V1.

### P07.4 Recorded evidence, explicitly not rerun here

| Evidence chain | Arithmetic and formula distinction | Recorded outcome |
|:--|:--|:--|
| V1 + V2 + V3, result V8 | Exact-rational cover; integer outward intervals; midpoint entropy-tangent envelope. | Complete 224-bit verification; largest normalized compact upper bound below $-5.71962366142\times10^{-12}$. |
| V1 + V4, result V9 | Separate mpmath interval engine and entropy-difference expression for $C_\parallel$. | All rectangles and tails pass at 85 decimal digits. |
| V1 + V5 + V6, result V7 | Final-audit Decimal engine and entropy-conjugate/secant envelope; no submitted numerical evaluator imported. | All 512 bands and 29,635 rectangles pass at 130 digits; largest compact upper bound below $-2.37355635215\times10^{-10}$. |

The smallest recorded normalized tail margin exceeds $0.00028189136168$ nats. Different negative compact margins are expected from different valid upper envelopes. These are stored source results, not numerical runs performed in this consolidation.

A replay must confirm the declared polynomial, noise domain, input-tail split, exact rational coverage, all required interval signs, and fail on corrupted or incomplete covers. Counts alone are not proof. The source source-code and result hashes, together with independent execution entry points, are mapped in [P14](#p14) and the provenance ledger. Arithmetic assumptions, including outward rounding of elementary functions, remain part of the explicit computer-assisted proof obligation.

The analytical domains of P05 and P06 meet this complete compact domain at their exact endpoints. Together with pure-input equality they establish the supplied all-noise scalar lemma (P4.1). This document consolidates that proof and its recorded certificate support; it does not claim a newly executed certificate or a formal proof-assistant derivation.

<a id="p08"></a>
## P08. Geometry separates the global costs

**Sources:** [S4](SOURCE_TO_CANONICAL.md#s4) §4; [S5](SOURCE_TO_CANONICAL.md#s5) §5; source [C1](SOURCE_TO_CANONICAL.md#c1)–[C2](SOURCE_TO_CANONICAL.md#c2). **Claims:** C1, C4.

For $0\leq y<1$,

$$(1-y)^{-1}-(1-y)^{-1/2}\geq y/2.$$

Apply it to $y=a(\mathbf n_b\cdot\mathbf u)^2$ before minimizing. With

$$\Lambda(\mathbf u)=\sum_b\frac{w_b c}{\sqrt{1-a(\mathbf n_b\cdot\mathbf u)^2}},\quad
L=\min_{\|\mathbf u\|=1}\Lambda(\mathbf u),$$

it yields

$$G(\mathbf u)-\Lambda(\mathbf u)\geq\frac{ca}{2}\mathbf u^{\mathsf T}T\mathbf u\geq\frac{ca}{2}\lambda,$$

$$G_{\min}\geq L+\frac{ca}{2}\lambda. \tag{P8.1}$$

The continuous directional losses have positive denominators for interior error, so compactness of the unit sphere gives an attained minimum $L$.

To bound the other entry in (P4.2), average over a uniformly distributed direction $\mathbf u$ on the Bloch sphere:

$$L\leq A_\epsilon:=c\,\frac{\arcsin\sqrt a}{\sqrt a}.$$

This is an existence bound for a fixed encoding direction, not permission to adapt the encoder to a future randomly chosen measurement axis. Positivity of the arcsin power-series coefficients gives

$$\frac{\arcsin\sqrt a}{\sqrt a}\leq1+\frac a6+\frac{3a^2}{40}
+\left(\frac\pi2-\frac{149}{120}\right)a^3.$$

Using $\pi<22/7$,

$$P(a)-\frac{\arcsin\sqrt a}{\sqrt a}>a\left(\frac1{12}+\frac{7a}{40}-\frac{193a^2}{840}\right)\geq\frac a{35}.$$

The quadratic is concave and its smaller endpoint value on $[0,1]$ is $1/35$. The exact positive integral

$$\frac{22}{7}-\pi=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx>0$$

is the source's elementary certification of the bound on $\pi$. Since $\mathrm{Tr}(T)=1$, $0\leq\lambda\leq1/3$. Therefore

$$\ell>L+\frac{ca}{35}\geq L+\frac3{35}ca\lambda. \tag{P8.2}$$

Combine (P4.2), (P8.1) and (P8.2):

$$\boxed{\Gamma\geq L+d_\epsilon\lambda,\qquad d_\epsilon=\frac3{35}ca.} \tag{P8.3}$$

If the supported axes span $\mathbb R^3$, positive weights give $\lambda>0$; interior error gives $ca>0$. No lower bound on $\lambda$ beyond positivity has been imposed.

The width of the guaranteed overlap interval is

$$
\begin{aligned}
\Delta p_{\mathrm{cert}}
&=\frac{d_\epsilon\lambda}{(1+L)(1+L+d_\epsilon\lambda)}\\
&\geq\frac{d_\epsilon}{(1+A_\epsilon)(1+A_\epsilon+d_\epsilon/3)}\lambda.
\end{aligned}
$$

This is a width bound, not a rate. Its uniform coefficient can tend to zero near either noise endpoint, just as the width can vanish when the frame approaches a plane.

<a id="p09"></a>
## P09. Complete all-record repetition construction

**Sources:** [S8](SOURCE_TO_CANONICAL.md#s8) §§3.1–3.3; [S5](SOURCE_TO_CANONICAL.md#s5) §6; [S9](SOURCE_TO_CANONICAL.md#s9) §7; [S10](SOURCE_TO_CANONICAL.md#s10) §5. **Claim:** C3. The inherited per-axis-noise lemma is restricted here to the current common-error model.

### P09.1 Fixed code and its record coefficients

Let $|\mathbf u_+\rangle,|\mathbf u_-\rangle$ be the orthonormal eigenstates of $\mathbf u\cdot\boldsymbol\sigma$. Choose the isometry

$$|0\rangle\mapsto|\mathbf u_+\rangle^{\otimes n},\qquad
|1\rangle\mapsto|\mathbf u_-\rangle^{\otimes n},$$

and the balanced mixed input

$$\rho_n(\mathbf u)=\frac12|\mathbf u_+\rangle\langle\mathbf u_+|^{\otimes n}
+\frac12|\mathbf u_-\rangle\langle\mathbf u_-|^{\otimes n}.$$

Its average density matrix is separable but correlated. The purified reference/code state retains coherent superpositions; this is a legitimate quantum coding input, not cloning an arbitrary qubit. Fix the code before any future realized measurement choices.

For axis $b$, define

$$
\begin{aligned}
s_b(\mathbf u)&=\sqrt{1-a(\mathbf n_b\cdot\mathbf u)^2},\\
\kappa_b(\mathbf u)&=\frac{a[1-(\mathbf n_b\cdot\mathbf u)^2]}{1-a(\mathbf n_b\cdot\mathbf u)^2},
\end{aligned}
$$

$$B(\mathbf u)=\sum_b w_b s_b,\qquad K(\mathbf u)=\sum_b w_b s_b\kappa_b.$$

The per-record probabilities conditional on the two codewords are

$$P_\pm(b,s)=w_b\frac{1\pm(-1)^s\eta\,\mathbf n_b\cdot\mathbf u}{2}.$$

The record overlap obeys

$$\sum_{b,s}\sqrt{P_+(b,s)P_-(b,s)}=B(\mathbf u),$$

and insertion of $\kappa_b$ gives $K(\mathbf u)$. Direct subtraction yields

$$B(\mathbf u)-K(\mathbf u)=\Lambda(\mathbf u). \tag{P9.1}$$

These record coefficients have a classical discrimination interpretation in the source. No separate discrimination theorem is required for the explicit finite-axis bounds below.

### P09.2 Exact conditional states and the all-measured contribution

For $m$ reported measured sites, let $\omega=(y_1,\ldots,y_m)$, with $y_j=(b_j,s_j)$, and define

$$
\begin{aligned}
\mathsf p_\pm(\omega)&=\prod_{j=1}^mP_\pm(y_j),\\
q_\omega&=\frac{\mathsf p_+(\omega)+\mathsf p_-(\omega)}2,\\
x_\omega&=\frac{\mathsf p_-(\omega)}{\mathsf p_+(\omega)+\mathsf p_-(\omega)},\\
\chi_\omega&=\prod_{j=1}^m\kappa_{b_j}.
\end{aligned}
$$

When at least one code qubit survives, its two conditional codeword states remain orthogonal. In the two-dimensional support spanned by the matching reference/codeword states, the joint conditional density matrix has diagonal $(1-x_\omega,x_\omega)$ and off-diagonal magnitude

$$\sqrt{\chi_\omega x_\omega(1-x_\omega)}.$$

Axis-dependent phases do not change its eigenvalues. They are not supplied as an extra assistance resource or dropped from the physical map. Its determinant is $(1-\chi_\omega)x_\omega(1-x_\omega)$.

Define the measured-record averages

$$\mathcal A_m=\sum_\omega q_\omega h_2(x_\omega),$$

$$\mathcal R_m=\sum_\omega q_\omega D_{\chi_\omega}(x_\omega),\qquad
\mathcal C_m=\mathcal A_m-\mathcal R_m,$$

with $\mathcal A_0=\mathcal R_0=1$ and $\mathcal C_0=0$. For at least one survivor, the conditional receiver entropy contributes $\mathcal A_m$ and the joint entropy contributes $\mathcal C_m$. If **all** $n$ qubits are measured, the receiver has no remaining quantum entropy: its conditional contribution is $-\mathcal C_n$.

Every mask and reported record therefore contributes to the exact block identity

$$
\boxed{\begin{aligned}
\mathcal I_n&:=I_c(\rho_n(\mathbf u),\mathcal N_{p,\epsilon}^{\otimes n})\\
&=\sum_{m=0}^n{n\choose m}(1-p)^{n-m}p^m\mathcal R_m-p^n\mathcal A_n.
\end{aligned}}
\tag{P9.2}
$$

The $m=n$ terms combine to $-p^n\mathcal C_n$. The favorable-branch interpretation of the first sum does not delete this negative term.

### P09.3 Upper envelopes

The two entropy bounds (P2.1) give

$$q_\omega h_2(x_\omega)\leq\sqrt{\mathsf p_+(\omega)\mathsf p_-(\omega)},$$

$$q_\omega D_{\chi_\omega}(x_\omega)
\leq\chi_\omega\sqrt{\mathsf p_+(\omega)\mathsf p_-(\omega)}.$$

Summing complete records factorizes into products of single-record sums:

$$\mathcal A_m\leq B^m,\qquad\mathcal R_m\leq K^m. \tag{P9.3}$$

### P09.4 Polynomial lower envelopes without postselection

For a proof bound only, relabel outcome signs so that

$$\pi_b^+=\frac{1+|\eta\mathbf n_b\cdot\mathbf u|}{2}\geq
\pi_b^-=1-\pi_b^+>0.$$

Full-rank noisy effects make the finite likelihood bound

$$\mathcal L_{\mathrm{rec}}=\sum_{b=1}^J\ln(\pi_b^+/\pi_b^-),\qquad
x_*=(1+e^{\mathcal L_{\mathrm{rec}}})^{-1}>0$$

well defined. Set

$$c_A=h_2(x_*)>0,\qquad c_R=\frac2{\ln2}x_*(1-x_*)>0.$$

Condition first on counts $m_b$ of each measurement axis, where $\sum_bm_b=m$. For each axis retain one central binomial sign class: its positive and negative counts differ by at most one, and its multiplicity is at least $2^{m_b}/(m_b+1)$. Consequently the entire retained record log-likelihood ratio has absolute value at most $\mathcal L_{\mathrm{rec}}$, independently of $m$. Thus its posterior satisfies

$$h_2(x_\omega)\geq c_A,\qquad \frac2{\ln2}x_\omega(1-x_\omega)\geq c_R.$$

Also $q_\omega\geq\sqrt{\mathsf p_+\mathsf p_-}$. Combining these facts with the central-class multiplicity gives, for those fixed axis counts, contributions at least

$$c_A\prod_b\frac{s_b^{m_b}}{m_b+1},\qquad
c_R\prod_b\frac{(s_b\kappa_b)^{m_b}}{m_b+1}$$

to $\mathcal A_m$ and $\mathcal R_m$, respectively. The axis probabilities are then included through their multinomial weights. Since $\prod_b(m_b+1)\leq(m+1)^J$, their sum gives

$$
\boxed{\begin{aligned}
\frac{c_A}{(m+1)^J}B^m&\leq\mathcal A_m\leq B^m,\\
\frac{c_R}{(m+1)^J}K^m&\leq\mathcal R_m\leq K^m.
\end{aligned}}
\tag{P9.4}
$$

The selection of central classes is only a lower bound on a sum of nonnegative entropy contributions. It does **not** change the channel or permit the decoder to postselect those events. The complete coherent-information identity remains (P9.2).

If an individual $\kappa_b=0$, the corresponding lower contribution is zero whenever that axis occurs; this agrees with the formula. If $K=0$, then $\mathcal R_m=0$ for $m>0$ and the no-measurement term is handled directly. Under full span $K>0$ for every fixed code direction. The $m=0$ convention is consistent with the bounds because $c_A,c_R\leq1$. Finitely many axes and strictly interior error are substantive here: the constants can depend strongly on the chosen channel and direction, but not on $m$.

<a id="p10"></a>
## P10. Finite inner blocks, outer coding and the main theorem

**Sources:** [S8](SOURCE_TO_CANONICAL.md#s8) §3.3–§4; [S5](SOURCE_TO_CANONICAL.md#s5) §6; [S4](SOURCE_TO_CANONICAL.md#s4) §§1, 4. **External input:** EXT1, the coherent-information coding theorem. **Claims:** C1, C3.

Set

$$\nu_+=1-p+pK(\mathbf u),\qquad\nu_-=pB(\mathbf u).$$

Insert (P9.4) into (P9.2), using $(m+1)^J\leq(n+1)^J$, to obtain

$$\boxed{\frac{c_R}{(n+1)^J}\nu_+^n-\nu_-^n
\leq\mathcal I_n\leq
\nu_+^n-\frac{c_A}{(n+1)^J}\nu_-^n.} \tag{P10.1}$$

If $\nu_+>\nu_-$, their exponential ratio eventually dominates the polynomial factor and $\mathcal I_n>0$ for every sufficiently large finite $n$. This strict condition is exactly

$$p<\frac1{1+\Lambda(\mathbf u)}.$$

If $\nu_+<\nu_-$, sufficiently large blocks in that fixed direction are negative. The equality case and exceptional shorter blocks above that frontier are not settled by (P10.1).

For the headline theorem, first fix the channel ensemble, $\epsilon$ and a measurement probability

$$\frac1{1+L+d_\epsilon\lambda}\leq p<\frac1{1+L},\qquad\lambda>0.$$

The global cost inequality (P8.3) and (P1.2) give $Q^{(1)}=0$. Choose a unit direction attaining $L$ and then a sufficiently large finite inner length $n$ so that $\mathcal I_n>0$. This is a code fixed from known channel parameters, not from the realized future record. Apply the standard coding theorem to repeated uses of the superchannel $\mathcal N_{p,\epsilon}^{\otimes n}$:

$$Q(\mathcal N_{p,\epsilon})\geq\frac{\mathcal I_n}{n}>0.$$

This concludes the source-derived full-span theorem. The proof does not require a positive limit of $\mathcal I_n/n$ as the inner block length itself diverges. It chooses a useful positive finite inner block and then takes the distinct outer coding limit. The constant, selected direction, sufficient inner length and achievable rate may depend on the fixed ensemble, error and measurement probability. No practical uniform rate or efficient outer code has been supplied.

<a id="p11"></a>
## P11. Coplanar geometry and the two reporting-noise endpoints

**Sources:** [S4](SOURCE_TO_CANONICAL.md#s4) §5; [S5](SOURCE_TO_CANONICAL.md#s5) §8; [S8](SOURCE_TO_CANONICAL.md#s8) §5; [S10](SOURCE_TO_CANONICAL.md#s10) §7. **External endpoint input:** EXT4–EXT5. **Claim:** C6.

### P11.1 Coplanarity and the restricted converse

If the supported axes are coplanar, choose $\mathbf u$ perpendicular to that plane. For that direction all squared projections vanish and $G(\mathbf u)=\Lambda(\mathbf u)=c$. For every direction, (P2.2) and monotonicity of the paired cost give

$$C_\epsilon(t,x)\geq C_\perp(t)\geq c h_2(t).$$

Thus $\Gamma\geq c$; the perpendicular nearly pure input approaches $c$, so $\Gamma=c$. The directional loss is always at least $c$ and reaches it perpendicularly, so $L=c$. Combining with the strict full-span bound proves

$$L<\Gamma\quad\Longleftrightarrow\quad\mathrm{rank}(T)=3$$

for the defined long-balanced-repetition comparison throughout the common interior-error range. This is not a zero-capacity theorem for all coplanar channels above their one-use threshold, and does not exclude other codes or exceptional finite blocks. Two noncommuting axes can still be coplanar; incompatibility alone is not the criterion.

### P11.2 Perfect records, $\epsilon=0$

The measurement effects have rank one and the conditional reference state for every reported outcome is pure. Hence

$$I_c=(1-p)S(\rho).$$

A mixed input has positive one-use coherent information whenever $p<1$. At $p=1$ the channel is quantum-to-classical and cannot transmit unknown quantum information. Thus there is no $Q^{(1)}=0<Q$ region at this endpoint. This reasoning is direct from the physical channel, not a substitution into formulas with $c$ in a denominator.

### P11.3 Completely random records, $\epsilon=1/2$

All reported signs are independent of the input. The axes and sign labels are additional independent flags on an erasure channel. Its known capacity is

$$Q=Q^{(1)}=\max\{0,1-2p\}.$$

There is again no separation. Full span of nominal axes does not make a record informative when $\eta=0$. The erasure-capacity theorem is an explicitly external endpoint result, not reproved by the interior entropy certificate. Errors above one half are outside the adopted convention; the source notes that a known sign inversion exchanges them with errors below one half.

<a id="p12"></a>
## P12. The exact near-coplanar family and its valid domain

**Sources:** [S4](SOURCE_TO_CANONICAL.md#s4) §6; [S5](SOURCE_TO_CANONICAL.md#s5) §8. **Claim:** C6.

For $j=0,1,2$, take equally probable axes

$$\mathbf n_j=(\sqrt{1-\lambda}\cos(2\pi j/3),\sqrt{1-\lambda}\sin(2\pi j/3),\sqrt\lambda).$$

For $0\leq\lambda\leq1/3$,

$$T=\mathrm{diag}\left(\frac{1-\lambda}{2},\frac{1-\lambda}{2},\lambda\right),$$

so the cone parameter is the smallest frame eigenvalue. The increasing-convex scalar functions $(1-ax)^{-1}$ and $(1-ax)^{-1/2}$, Jensen's inequality, and $\mathbf u^{\mathsf T}T\mathbf u\geq\lambda$ give minima attained by the vertical direction:

$$G_{\min}=\frac{c}{1-a\lambda},\qquad L=\frac{c}{\sqrt{1-a\lambda}}. \tag{P12.1}$$

If $\lambda\leq W(a)/P(a)$, then $G_{\min}\leq\ell$. The global lower bound (P4.2) and the axial nearly pure upper bound from P01 therefore agree:

$$\boxed{\Gamma=\frac{c}{1-a\lambda}\quad\text{for}\quad
0\leq\lambda\leq\min\{1/3,W(a)/P(a)\}.} \tag{P12.2}$$

The source identities imply $W/P\geq1/4$. Thus every common interior error has the exact cone formulas on $0\leq\lambda\leq1/4$. The larger domain must be justified for the chosen error; it cannot be inferred from the older one-percent example. Also

$$3W-P=\frac{(2a-1)(5-a^2)}{20},$$

so $a\geq1/2$ suffices to extend the exact formulas through $\lambda=1/3$. This includes the error of the retained eight-use example but not every interior error.

The source's fixed-error expansion gives

$$\boxed{p_{\mathrm{rep}}-p_1
=\frac{ca}{2(1+c)^2}\lambda+O(\lambda^2),\qquad\lambda\downarrow0.} \tag{P12.3}$$

Here $p_1$ is the exact single-use boundary for this valid cone range, while $p_{\mathrm{rep}}$ is the construction frontier. Neither is asserted to be the optimal capacity phase boundary. The gap can be arbitrarily small and does not promise a bounded working block or useful rate. This section consolidates the retained limiting family; it does not freeze a new plot range or add a resource-scaling investigation.

<a id="p13"></a>
## P13. The retained eight-use witness and two numerical safeguards

**Sources:** [S5](SOURCE_TO_CANONICAL.md#s5) §7; [S4](SOURCE_TO_CANONICAL.md#s4) §§6–8; [W1](SOURCE_TO_CANONICAL.md#w1)–[W7](SOURCE_TO_CANONICAL.md#w7); source [C3](SOURCE_TO_CANONICAL.md#c3)–[C4](SOURCE_TO_CANONICAL.md#c4). **Claim:** C5; safeguards for C2.

### P13.1 A global single-use zero at the witness parameters

For equal Pauli axes and $\epsilon=1/10$,

$$a=\frac{16}{25},\qquad c=\frac9{25},\qquad
G_{\min}=\frac{c}{1-a/3}=\frac{27}{59}.$$

The source has $\ell>27/59$; equivalently the cone-family equality condition applies since $a>1/2$. Therefore $\Gamma=27/59$ and

$$p_1=\frac{59}{86}.$$

At $p=7/10$, the mixed-input bound is

$$\frac{I_c(t,\mathbf u)}{h_2(t)}\leq\frac3{10}-\frac7{10}\frac{27}{59}
=-\frac6{295}<0.$$

Together with pure-input value zero, this proves a globally optimized $Q^{(1)}=0$. It is not just the value of the maximally mixed state. The witness is justified by this sharper intermediate inequality, not necessarily by membership in the most conservative uniform $3/35$ subinterval.

### P13.2 Exact input and all-record formula

Choose $\mathbf u=(1,1,1)/\sqrt3$ and $n=8$, with the balanced input in P09. Put

$$\alpha=\frac{1+\eta/\sqrt3}{2},\quad\bar\alpha=1-\alpha,\quad
\kappa=\frac{2\eta^2}{3-\eta^2}.$$

The axis-conditioned diagonal probabilities and coherence magnitudes coincide for the three Pauli labels. Summing their probabilities therefore leaves, at each measured count $m$, the $m+1$ sign-count classes

$$
\begin{aligned}
v_j&=\alpha^j\bar\alpha^{m-j},\\
w_j&=\bar\alpha^j\alpha^{m-j},\\
q_j&=(v_j+w_j)/2,\\
x_j&=w_j/(v_j+w_j).
\end{aligned}
$$

Their contributions to $\mathcal A_m$ and $\mathcal C_m$ are

$$\mathcal A_m=\sum_{j=0}^m{m\choose j}q_j h_2(x_j),$$

$$\mathcal C_m=\sum_{j=0}^m{m\choose j}q_j\mathcal H(4(1-\kappa^m)x_j(1-x_j)).$$

For $m=0$ use $\mathcal A_0=1,\mathcal C_0=0$. The exact coherent information is then

$$\mathcal I_8=\sum_{m=0}^7{8\choose m}(1-p)^{8-m}p^m(\mathcal A_m-\mathcal C_m)-p^8\mathcal C_8.$$

There is no survivor filter or postselection. The two-dimensional formula evaluates the full flagged entropy sum, not a claim to have diagonalized an exponentially large eight-use receiver/reference matrix.

### P13.3 Canonical retained evidence

Source **W1**, the final audit's `witness140.json`, is the selected record for subsequent figure-input specification. Its companion **W2** retains the earlier independent precision. **W3** is the final-audit evaluator using the separate Decimal primitive **V6**. The original mpmath effect-determinant route is **W5**, with output **W4** and associated records in the preserved archive. Small direct hidden-outcome physical checks are **W6–W7**.

The stored enclosure supports

$$
\begin{aligned}
\frac{\mathcal I_8}{8}
&=0.0000747747658815596371016563672617787\ldots\\
&>7.47\times10^{-5}.
\end{aligned}
$$

The total block value is approximately $0.0005981981270524771$ bits. The exactly stored all-measured probability is $p^8=0.05764801$ and its weighted contribution is approximately $-0.01653160578649$ bits. All nine measured-count entries are present in W1.

These figures are the retained source enclosures and approximations. The current baseline preserves their exact recorded bytes and re-evaluates the two substantive witness implementations in its full verification command. The regenerated values must agree with their own immutable reference; no new plot-rounding policy or optimal eight-use code is claimed. A rigorous arithmetic interval is not a statistical confidence interval. The rate is achievable only with the stated asymptotic outer-coding interpretation.

<a id="p134"></a>
### P13.4 Safeguards kept as verification evidence, not extra headline results

At equal Pauli axes with $\epsilon=1/5$, the directional nearly pure optimum would be $G_{\min}=8/11$. At its implied boundary $p=11/19$, the maximally mixed input instead has

$$I_c=\frac{8-11h_2(1/5)}{19}>0.$$

Source C3 stores a directed enclosure of this control. It demonstrates why $\Gamma=G_{\min}$ cannot be assumed at larger error without proof.

Source C4 records a rejected floating-point candidate at $\epsilon=2/5$, $p=5083/10000$, $n=64$, whose directed rate bound is negative. It is retained as a numerical-validation control against signs obtained from severe cancellation. It is not a second figure or a new positive witness in the consolidated story.

<a id="p14"></a>
## P14. Certificate and evidence dependencies, without merging independent evaluators

**Sources:** [V1](SOURCE_TO_CANONICAL.md#v1)–[V9](SOURCE_TO_CANONICAL.md#v9); [W1](SOURCE_TO_CANONICAL.md#w1)–[W7](SOURCE_TO_CANONICAL.md#w7); source [C1](SOURCE_TO_CANONICAL.md#c1)–[C4](SOURCE_TO_CANONICAL.md#c4); source [R1](SOURCE_TO_CANONICAL.md#r1)–[R6](SOURCE_TO_CANONICAL.md#r6); [S7](SOURCE_TO_CANONICAL.md#s7).

The canonical proof has three substantive computational paths to the same compact entropy claim:

| Path | Immutable input | Substantive implementation | Recorded result |
|:--|:--|:--|:--|
| Integer construction/checker | V1 rational certificate | V2 plus V3 | V8 and the construction's stored results |
| Independent mpmath checker | V1 | V4 | V9 |
| Final-audit Decimal checker | V1 | V5 plus V6 | V7 |

They share the mathematical statement and, where indicated, the rational partition. They do not become independent through differences in precision alone. Their source implementations, entropy expressions, arithmetic backends and envelope methods are identified individually. They are preserved unchanged; consolidation does not deduplicate these substantive routes into one evaluator.

All runtime certificate inputs and substantive evaluators are now included directly in this scientific baseline. No original audit ZIP or earlier chat is required to execute them. Historical source paths and hashes are retained as provenance; the current reading path is this proof.

From the package root, use:

```bash
python verify.py
python reproduce.py --output /path/to/new-output
python reproduce.py --output /path/to/new-full-output --full
```

`verify.py` checks package identity, claim/source coverage, local links, and approved artifact hashes; it does not certify an entropy inequality. The ordinary reproduction command checks numerical figure inputs and redraws the approved figures in a new output directory. `--full` additionally runs the distinct integer, mpmath, and Decimal compact-certificate paths, the endpoint checks, the retained witness and declared controls, and direct small physical checks. `--rebuild-certificate` may be added to reconstruct the rational cover as well. Output directories must not already exist and no command overwrites approved figures or reference evidence.

Target a single substantive checker without changing the model:

```bash
python verification/decimal/verify_certificate.py \
  --certificate certificates/common_noise_compact_certificate.json \
  --output /path/to/independent-certificate.json --precision 130
```

The three certificate algorithms and their arithmetic engines remain separate files in separate directories. Relocation did not make them independent merely by changing precision, nor merge their substantive entropy routines. The exact moved-file hashes, any adapter-only patches, and fresh runtime evidence are in `provenance/FILE_LINEAGE.json` and `validation/BASELINE_VALIDATION.json`. See [REPRODUCTION.md](REPRODUCTION.md) for dependencies, expected outputs, and scope of each check.

<a id="p15"></a>
## P15. Completion boundary and attribution

The proof obligations for the retained mathematical claims map as follows:

- C1: P01 plus P08–P10, relying on the scalar chain P02–P07.
- C2: P01 and P03–P08, with the exact computer-assisted obligation in P07.
- C3: P02 and P09–P10, with the coding theorem explicitly identified as external background.
- C4: P03–P08.
- C5: P12–P13 and the preserved numerical witness.
- C6: P11–P12, with the erasure-capacity endpoint explicitly sourced externally.

These links are also machine-readable in `provenance/CLAIM_COVERAGE.json`. Every imported section and numerical/checker identity has an original source path and SHA-256 in the ledger. Historical conditions are imported only where justified; the broader per-axis-noise repetition lemma is specialized to common error, and the older narrow-band scalar certificate is not substituted for the current all-noise proof.

C7, significance and originality relative to prior work, is not an additional mathematical lemma. The current source comparison supports a bounded working distinction from the inspected incomplete-erasure, dephrasure and structured-code literature. Absolute priority and external peer review remain unrecorded. [REFERENCES.md](REFERENCES.md) carries the existing attribution and its scope without reopening a web search or extending the claim.

No missing internally named dependency was discovered in the inspected source set. This consolidation does not assert that a fresh external audit would find no issue. The canonical argument is a dependency-complete account of the supplied author-audited result, with its explicit computer certificate and named standard tools. The scientific specifications, canonical plotting data, and user-approved figures are included directly in this baseline. Clean-directory checks are recorded separately in the current validation report; the original canonical derivations and their source links remain traceable.
