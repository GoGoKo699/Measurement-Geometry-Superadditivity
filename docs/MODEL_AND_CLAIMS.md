# Measurement geometry and coherent-information superadditivity
## Canonical model and claims, version 1

**8 September 2026. Scientific consolidation, not a manuscript or a new theorem.** This document fixes the notation, assumptions and claim scope for the supplied all-common-noise result. Its companion [complete proof](COMPLETE_PROOF.md) brings the required derivations into one sequence. The frozen one-page story is unchanged in [FROZEN_ARGUMENT.md](FROZEN_ARGUMENT.md).

The latest source reports that final mathematical audit obligations A–D passed and that a bounded distinction from inspected prior work supports drafting. The canonical statement adopts that **recorded author-side status**. The present baseline reports its separate relocation/reproducibility checks without claiming a new external audit or priority clearance. The management sequence remains scientific consolidation and figures, then a dedicated repository, then manuscript drafting. [Sources S1–S7](SOURCE_TO_CANONICAL.md)

<a id="m01"></a>
## 1. The channel and its operation budget

There are $J<\infty$ unit Bloch axes $\mathbf n_b\in\mathbb R^3$, indexed by $b=1,\ldots,J$, with probabilities $w_b>0$ and $\sum_b w_b=1$. All these channel parameters are known when the code is designed. Repeated or sign-reversed axes may be represented as separately labeled outcomes; the theorem concerns their supported span and positive weights.

Each physical use independently does one of two things. With probability $1-p$, the qubit arrives intact. With probability $p$, axis $b$ is drawn according to $w_b$, the qubit is projectively measured, and the quantum system becomes inaccessible. If the true outcome bit is $r$, the receiver sees $s=r\oplus z$, with $z$ an independent Bernoulli bit of **common** probability $\epsilon$ for every axis and use.

The principal theorem assumes

$$0\leq p\leq1,\qquad 0<\epsilon<\frac12.$$

The mask distinguishing the branches and the measurement-axis label are delivered correctly. The receiver never learns the hidden true bit or whether acquisition error occurred, and cannot reread a discarded qubit. Encoding precedes all realized branch, axis and outcome choices. Gates for encoding and decoding are otherwise unrestricted and noiseless. There is no postselection, feedback, preshared entanglement, or measurement-dependent alteration of the encoder.

Set

$$\eta=1-2\epsilon,\qquad a=\eta^2,\qquad c=1-a=4\epsilon(1-\epsilon).$$

For an individual axis, the reported-outcome effects are

$$E_{b,s}=\frac{I+(-1)^s\eta\,\mathbf n_b\cdot\boldsymbol\sigma}{2},\qquad s\in\{0,1\}.$$

These effects sum to $I$ **for each fixed axis**. The axis weight is not included in $E_{b,s}$: the complete measured-branch POVM has effects $w_bE_{b,s}$. The receiver channel is

$$
\boxed{\begin{aligned}
\mathcal N_{p,\epsilon}(\rho)&=(1-p)\rho\ \oplus\\
&\quad p\sum_{b,s}w_b\,\mathrm{Tr}(E_{b,s}\rho)\,|b,s\rangle\langle b,s|.
\end{aligned}}
$$

The direct sum distinguishes the intact quantum branch from the classical record branch. Independent uses are represented by tensor powers of this channel. The measurement branch itself is quantum-to-classical; the claimed quantum transmission concerns its flagged mixture with intact transmission, not a capacity of the measured-only channel.

This is a specialization of the supplied incomplete-erasure framework attribution, not a new channel class. See [references](REFERENCES.md) and [proof P01](COMPLETE_PROOF.md#p01). **Sources:** [S3](SOURCE_TO_CANONICAL.md#s3); [S4](SOURCE_TO_CANONICAL.md#s4) §§1–2; [S5](SOURCE_TO_CANONICAL.md#s5) §1.

<a id="m02"></a>
## 2. Information quantities and notation

All von Neumann and binary entropies are in **bits**; $\ln$ denotes the natural logarithm in analytic estimates. A reference register is denoted $\mathsf R$ and the receiver register $\mathsf B$. For any input $\rho$ purified by $\mathsf R$,

$$
\begin{aligned}
I_c(\rho,\mathcal N)&=S(\mathsf B)-S(\mathsf R\mathsf B),\\
Q^{(1)}(\mathcal N)&=\max_\rho I_c(\rho,\mathcal N).
\end{aligned}
$$

$Q(\mathcal N)$ is the unassisted asymptotic quantum capacity. $Q^{(1)}$ is **not** defined here as an operational one-shot capacity. In particular, $Q^{(1)}=0$ does not mean that every conceivable single-use task is useless.

| Symbol | Canonical meaning |
|:--|:--|
| $J$ | Finite number of labeled measurement axes. |
| $p,\epsilon$ | Measurement probability and common symmetric reporting error. |
| $r,s$ | Hidden true outcome bit and reported bit. |
| $\eta,a,c$ | Noise parameters defined above; $a,c$ are never record probabilities. |
| $t\in[0,1/2]$, $\mathbf u\in S^2$ | Smaller input eigenvalue and unit Bloch direction. |
| $C_\epsilon(t,x)$ | Conditional-reference entropy cost for a single axis with squared projection $x$. |
| $C(t,\mathbf u)$ | Cost averaged over axis probabilities. |
| $C_\perp(t),C_\parallel(t)$ | Perpendicular and parallel single-axis endpoint costs; the fixed $\epsilon$ is implicit. |
| $\Gamma$ | Globally minimized measured-branch entropy cost relative to input entropy. |
| $T,\lambda$ | Measurement frame and its smallest eigenvalue. |
| $\Lambda(\mathbf u),L$ | Direction-dependent repetition loss and its minimum over all directions. |
| $d_\epsilon$ | Conservative full-span gap coefficient $3ca/35$. |
| $G(\mathbf u),G_{\min}$ | Directional nearly pure cost and its minimum; generally an **upper**, not an equality, for $\Gamma$. |
| $P(a),V(a),W(a),\ell$ | Polynomials and auxiliary scalar in the computer-assisted entropy comparison. |
| $\beta(t,\epsilon)$ | Chord coefficient shared by all axes because the error is common. |
| $n,m,m_b$ | Code block length, number of measured sites, and measured counts for axis $b$. |
| $\mathcal A_m,\mathcal C_m,\mathcal R_m$ | Record-averaged diagonal entropy, conditional joint entropy, and their difference for the repetition input. |
| $B(\mathbf u),K(\mathbf u)$ | Record-overlap and coherence-weighted overlap coefficients. $B(\mathbf u)$ is not the register $\mathsf B$. |
| $\mathcal L_{\mathrm{rec}}$ | A finite bound on the absolute record log-likelihood ratio for selected central sign classes, not the optimized loss $L$. |
| $\nu_+,\nu_-$ | Exponential bases $1-p+pK$ and $pB$, distinct from the polynomial $V(a)$. |

The exact source-to-canonical renaming is recorded in [NOTATION_CROSSWALK.md](NOTATION_CROSSWALK.md). These are documentary changes. Original source code, formulas in preserved snapshots, and numerical records are not rewritten.

<a id="m03"></a>
## 3. Exact single-use benchmark and the constructed frontier

Every mixed qubit density matrix can be written

$$\rho_{t,\mathbf u}=\frac{I+(1-2t)\mathbf u\cdot\boldsymbol\sigma}{2},\qquad 0<t\leq\frac12.$$

The flagged coherent-information identity and its global cost are

$$
\begin{aligned}
I_c&=(1-p)h_2(t)-pC(t,\mathbf u),\\
\Gamma&=\inf_{\|\mathbf u\|=1,\ 0<t\leq1/2}\frac{C(t,\mathbf u)}{h_2(t)}.
\end{aligned}
$$

Pure inputs have zero coherent information. Consequently the **exact one-use positivity boundary** is

$$p_1=\frac1{1+\Gamma},\qquad Q^{(1)}=0\ \Longleftrightarrow\ p\geq p_1.$$

Define

$$T=\sum_b w_b\mathbf n_b\mathbf n_b^{\mathsf T},\quad\lambda=\lambda_{\min}(T),$$

$$
\begin{aligned}
\Lambda(\mathbf u)&=\sum_b\frac{w_b c}{\sqrt{1-a(\mathbf n_b\cdot\mathbf u)^2}},\\
L&=\min_{\|\mathbf u\|=1}\Lambda(\mathbf u).
\end{aligned}
$$

The balanced antipodal repetition construction has a **strict eventual-sign frontier**, optimized over its fixed direction,

$$p_{\mathrm{rep}}=\frac1{1+L}.$$

Below that frontier, some sufficiently large finite block has positive coherent information. Above the corresponding fixed-direction frontier, sufficiently long balanced blocks in that direction are negative. Equality and exceptional shorter blocks are not settled by those exponential bounds. Thus $p_{\mathrm{rep}}$ is not identified with the optimal quantum-capacity threshold or the best finite-block threshold. **Sources:** [S4](SOURCE_TO_CANONICAL.md#s4) §§1–2, 4; [S5](SOURCE_TO_CANONICAL.md#s5) §§1, 6; [S8](SOURCE_TO_CANONICAL.md#s8) §§2–4.

<a id="m04"></a>
## 4. The retained theorem and quantifier order (C1–C4)

For every fixed allowed ensemble and every common $0<\epsilon<1/2$,

$$\boxed{\Gamma\geq L+d_\epsilon\lambda,\qquad d_\epsilon=\frac3{35}ca.}$$

If the axes span $\mathbb R^3$, then $\lambda>0$ and

$$
\boxed{\begin{aligned}
&\frac1{1+L+d_\epsilon\lambda}\leq p<\frac1{1+L}\\
&\quad\Longrightarrow\quad Q^{(1)}(\mathcal N_{p,\epsilon})=0<Q(\mathcal N_{p,\epsilon}).
\end{aligned}}
$$

The endpoints certify a nonempty subinterval, not the complete capacity-positive/negative boundary. The constant is conservative, not optimized. The lower endpoint is included and the upper endpoint is excluded.

The order of choices is: fix the ensemble and reporting error; choose an allowed $p$; choose a code direction from those known channel parameters; then choose a sufficiently long finite block; then apply the asymptotic coding theorem to repeated uses of that fixed block. Realized future axes or outcomes do not influence the encoding. No single nonzero rate, universal finite length, or common interval of $p$ is promised across all ensembles and errors.

The proof is the composition of a global one-use bound, a constructive all-record repetition bound, and the geometric inequality separating them. Its scalar entropy component is computer assisted. The complete source-derived route is [P01–P10](COMPLETE_PROOF.md#p01). **Sources:** [S3](SOURCE_TO_CANONICAL.md#s3); [S4](SOURCE_TO_CANONICAL.md#s4) §§1–4; [S5](SOURCE_TO_CANONICAL.md#s5) §§1–6; [S8](SOURCE_TO_CANONICAL.md#s8) §3.

<a id="m05"></a>
## 5. One retained numerical illustration (C5)

Use equally likely $X,Y,Z$ axes, common error $\epsilon=1/10$, measurement probability $p=7/10$, and a balanced eight-use input formed from the eigenstates of $(X+Y+Z)/\sqrt3$.

The source establishes $\Gamma=27/59$ and therefore the exact one-use positivity boundary $p_1=59/86$. Since $p=7/10>p_1$, the globally optimized one-use value is zero. The source's final 140-digit interval record gives

$$
\begin{aligned}
\frac{I_c(\rho_8,\mathcal N^{\otimes8})}{8}
&=0.0000747747658815596371016563672617787\ldots\\
&>7.47\times10^{-5}.
\end{aligned}
$$

The total block value is approximately $0.0005981981270524771$ bits. The all-measured event has probability $0.05764801$ and a negative weighted contribution approximately $-0.01653160578649$ bits. All nine measured-count contributions are retained. These numbers are **read from the stored certificate**, not recomputed by this consolidation.

This example uses a sharper single-use bound than the most conservative uniform $3/35$ theorem. A future figure must not imply that the two bounds are identical. The positive block value has an outer-coding interpretation; it is not an eight-use recovery fidelity or a proof of optimal block length. The exact argument and the evidence contract are in [P13](COMPLETE_PROOF.md#p13). **Sources:** [S5](SOURCE_TO_CANONICAL.md#s5) §7; [W1](SOURCE_TO_CANONICAL.md#w1)–[W7](SOURCE_TO_CANONICAL.md#w7).

<a id="m06"></a>
## 6. Retained controls and limiting family (C6)

**Coplanar axes.** A common perpendicular direction gives $\Gamma=L=c$. Thus, for this strict long-balanced-repetition criterion and the declared common-noise model,

$$L<\Gamma\quad\Longleftrightarrow\quad\mathrm{rank}(T)=3.$$

This is not an all-code converse against coplanar channels. It does not exclude exceptional finite blocks or a different encoding family. [P11](COMPLETE_PROOF.md#p11)

**Noise endpoints.** At $\epsilon=0$, $I_c=(1-p)S(\rho)$ is positive for mixed inputs when $p<1$, while the all-measured channel has zero capacity. At $\epsilon=1/2$, the record is input independent and the channel is an erasure channel up to independent flags, with $Q=Q^{(1)}=\max\{0,1-2p\}$. Neither endpoint has a $Q^{(1)}=0<Q$ region in this model. The endpoint arguments are separate from formulas that divide by $a$ or $c$ in the interior. [P11](COMPLETE_PROOF.md#p11)

**Cone family.** For three equally probable axes at azimuths $2\pi j/3$ and common vertical component $\sqrt\lambda$,

$$\mathbf n_j=(\sqrt{1-\lambda}\cos(2\pi j/3),\sqrt{1-\lambda}\sin(2\pi j/3),\sqrt\lambda),\quad j=0,1,2.$$

For every common interior error and $0\leq\lambda\leq1/4$,

$$\Gamma=\frac{c}{1-a\lambda},\qquad L=\frac{c}{\sqrt{1-a\lambda}},$$

$$p_{\mathrm{rep}}-p_1=\frac{ca}{2(1+c)^2}\lambda+O(\lambda^2)\qquad(\lambda\downarrow0,\ \epsilon\text{ fixed}).$$

The exact larger domain supplied by the source is $0\leq\lambda\leq\min\{1/3,W(a)/P(a)\}$. The all-error interval through $1/4$ is the default safe domain for the planned figure. Extension to $1/3$ requires the parameter-specific inequality, not an assumption based on the old one-percent family. Neither curve is an exact all-code capacity boundary. [P12](COMPLETE_PROOF.md#p12)

**Sources:** [S4](SOURCE_TO_CANONICAL.md#s4) §§5–6; [S5](SOURCE_TO_CANONICAL.md#s5) §8. This consolidation does not freeze new figure parameter choices or plot additional curves.

<a id="m07"></a>
## 7. Claim register and nonclaims

| Frozen ID | Canonical scientific content | Complete justification |
|:--|:--|:--|
| C1 | Full span gives the nonempty $Q^{(1)}=0<Q$ interval for every common interior error. | P01–P10. |
| C2 | The one-use obstruction applies to every qubit input. | P01, P03–P08; computational evidence in P07 and P14. |
| C3 | An all-record collective construction produces a positive finite block and asymptotic rate. | P02, P09–P10. |
| C4 | A uniform entropy inequality and geometry separate the two costs. | P03–P08. |
| C5 | The retained eight-use example has a global one-use zero and certified positive per-use block value. | P13 and preserved W-series records. |
| C6 | Coplanar, noise-endpoint and cone-family controls have the stated restricted meanings. | P11–P12. |
| C7 | The geometric guarantee is a distinctive scientific advance relative to the closest prior work. | Supplied bounded comparison S6; not a mathematical corollary or absolute priority certificate. |

The canonical source does **not** claim a new channel class; discovery of superadditivity itself; exact regularized capacity; quantum capacity enhanced by adding reporting noise; a general all-code no-go for coplanar channels; efficient or fault-tolerant decoding; practical uniform rates; independent per-axis, asymmetric, correlated or basis-label errors; infinitely many measurement labels; or a result derived from the old many-body simulations.

The averaged repetition input is separable but correlated; coherent logical superpositions and its reference purification can be entangled. This is not superactivation of two zero-capacity channels. These distinctions are part of the interpretation, not an invitation to enlarge the paper.

<a id="m08"></a>
## 8. Verification status and next boundary

The adopted scientific status is the **supplied final author-side audit**, not the superseded pending-audit footer in the frozen argument. Its stored results and source identities are preserved. Independent implementations do not constitute independent external researchers, and no proof-assistant formalization or absolute priority clearance is recorded.

The earlier canonical consolidation verified source identities and documentary traceability without rerunning arithmetic. This baseline keeps its mathematical content and now relocates executable dependencies. Rechecks performed after relocation are reported separately in [BASELINE_VALIDATION.json](../validation/BASELINE_VALIDATION.json); they are reproducibility checks, not a new external theorem audit. The analytical narrative is dependency complete for C1–C6, conditional on the explicitly identified standard background theorems and preserved computer-assisted certificate. See [current baseline status](../STATUS.md), [SOURCE_TO_CANONICAL.md](SOURCE_TO_CANONICAL.md) and [P14](COMPLETE_PROOF.md#p14).

The three figures have now been visually approved. Their exact files and inputs are protected by the baseline manifest. This local scientific package consolidates the executable dependencies; see [REPRODUCTION.md](REPRODUCTION.md) for current commands and [STATUS.md](../STATUS.md) for the baseline state. No manuscript has been drafted.
