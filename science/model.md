# The channel, resources and information quantities

[Science](README.md) · [Learning](../learning/README.md) · [References](../references/README.md) · [Verification](../verification/README.md)

The receiver can distinguish intact transmission from destructive measurement. In the measured branch it receives an axis label and a noisy sign. The distinction between accessible records and hidden outcomes fixes the channel whose capacity is studied.

The definitions below specify the operation budget before introducing the information quantities. The same reporting error applies to every axis and every use; this assumption is used later in the scalar entropy comparison. [The physical picture](physical-picture.md) gives a gentler explanation, and [the notation crosswalk](notation.md) connects the proof to its sources and implementations.

<!-- BEGIN canonical-unit M01 -->
<a id="m01"></a>
## 1. The channel and its operation budget

There are $`J\lt \infty`$ unit Bloch axes $`\mathbf n_b\in\mathbb R^3`$, indexed by $`b=1,\ldots,J`$, with probabilities $`w_b\gt 0`$ and $`\sum_b w_b=1`$. All these channel parameters are known when the code is designed. Repeated or sign-reversed axes may be represented as separately labeled outcomes; the theorem concerns their supported span and positive weights.

Each physical use independently does one of two things. With probability $`1-p`$, the qubit arrives intact. With probability $`p`$, axis $`b`$ is drawn according to $`w_b`$, the qubit is projectively measured, and the quantum system becomes inaccessible. If the true outcome bit is $`r`$, the receiver sees $`s=r\oplus z`$, with $`z`$ an independent Bernoulli bit of **common** probability $`\epsilon`$ for every axis and use.

The principal theorem assumes

```math
0\leq p\leq1,\qquad 0\lt \epsilon\lt \frac12.
```

The mask distinguishing the branches and the measurement-axis label are delivered correctly. The receiver never learns the hidden true bit or whether acquisition error occurred, and cannot reread a discarded qubit. Encoding precedes all realized branch, axis and outcome choices. Gates for encoding and decoding are otherwise unrestricted and noiseless. There is no postselection, feedback, preshared entanglement, or measurement-dependent alteration of the encoder.

Set

```math
\eta=1-2\epsilon,\qquad a=\eta^2,\qquad c=1-a=4\epsilon(1-\epsilon).
```

For an individual axis, the reported-outcome effects are

```math
E_{b,s}=\frac{I+(-1)^s\eta\,\mathbf n_b\cdot\boldsymbol\sigma}{2},\qquad s\in\{0,1\}.
```

These effects sum to $`I`$ **for each fixed axis**. The axis weight is not included in $`E_{b,s}`$: the complete measured-branch POVM has effects $`w_bE_{b,s}`$. The receiver channel is

```math
\boxed{\begin{aligned} \mathcal N_{p,\epsilon}(\rho)&=(1-p)\rho\ \oplus\\ &\quad p\sum_{b,s}w_b\,\mathrm{Tr}(E_{b,s}\rho)\,|b,s\rangle\langle b,s|. \end{aligned}} 
```

The direct sum distinguishes the intact quantum branch from the classical record branch. Independent uses are represented by tensor powers of this channel. The measurement branch itself is quantum-to-classical; the claimed quantum transmission concerns its flagged mixture with intact transmission, not a capacity of the measured-only channel.

This channel is a specialization of the incomplete-erasure framework. See [references](../references/README.md) and [proof P01](single-use.md#p01). **Sources:** [S3](../docs/SOURCE_TO_CANONICAL.md#s3); [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §§1–2; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §1.

<!-- END canonical-unit M01 -->

<!-- BEGIN canonical-unit M02 -->
<a id="m02"></a>
## 2. Information quantities and notation

All von Neumann and binary entropies are in **bits**; $`\ln`$ denotes the natural logarithm in analytic estimates. A reference register is denoted $`\mathsf R`$ and the receiver register $`\mathsf B`$. For any input $`\rho`$ purified by $`\mathsf R`$,

```math
\begin{aligned} I_c(\rho,\mathcal N)&=S(\mathsf B)-S(\mathsf R\mathsf B),\\ Q^{(1)}(\mathcal N)&=\max_\rho I_c(\rho,\mathcal N). \end{aligned} 
```

$`Q(\mathcal N)`$ is the unassisted asymptotic quantum capacity. $`Q^{(1)}`$ is **not** defined here as an operational one-shot capacity. In particular, $`Q^{(1)}=0`$ does not mean that every conceivable single-use task is useless.

| Symbol | Canonical meaning |
|:--|:--|
| $`J`$ | Finite number of labeled measurement axes. |
| $`p,\epsilon`$ | Measurement probability and common symmetric reporting error. |
| $`r,s`$ | Hidden true outcome bit and reported bit. |
| $`\eta,a,c`$ | Noise parameters defined above; $`a,c`$ are never record probabilities. |
| $`t\in[0,1/2]`$, $`\mathbf u\in S^2`$ | Smaller input eigenvalue and unit Bloch direction. |
| $`C_\epsilon(t,x)`$ | Conditional-reference entropy cost for a single axis with squared projection $`x`$. |
| $`C(t,\mathbf u)`$ | Cost averaged over axis probabilities. |
| $`C_\perp(t),C_\parallel(t)`$ | Perpendicular and parallel single-axis endpoint costs; the fixed $`\epsilon`$ is implicit. |
| $`\Gamma`$ | Globally minimized measured-branch entropy cost relative to input entropy. |
| $`T,\lambda`$ | Measurement frame and its smallest eigenvalue. |
| $`\Lambda(\mathbf u),L`$ | Direction-dependent repetition loss and its minimum over all directions. |
| $`d_\epsilon`$ | Conservative full-span gap coefficient $`3ca/35`$. |
| $`G(\mathbf u),G_{\min}`$ | Directional nearly pure cost and its minimum; generally an **upper**, not an equality, for $`\Gamma`$. |
| $`P(a),V(a),W(a),\ell`$ | Polynomials and auxiliary scalar in the computer-assisted entropy comparison. |
| $`\beta(t,\epsilon)`$ | Chord coefficient shared by all axes because the error is common. |
| $`n,m,m_b`$ | Code block length, number of measured sites, and measured counts for axis $`b`$. |
| $`\mathcal A_m,\mathcal C_m,\mathcal R_m`$ | Record-averaged diagonal entropy, conditional joint entropy, and their difference for the repetition input. |
| $`B(\mathbf u),K(\mathbf u)`$ | Record-overlap and coherence-weighted overlap coefficients. $`B(\mathbf u)`$ is not the register $`\mathsf B`$. |
| $`\mathcal L_{\mathrm{rec}}`$ | A finite bound on the absolute record log-likelihood ratio for selected central sign classes, not the optimized loss $`L`$. |
| $`\nu_+,\nu_-`$ | Exponential bases $`1-p+pK`$ and $`pB`$, distinct from the polynomial $`V(a)`$. |

[NOTATION_CROSSWALK.md](notation.md) relates this notation to the symbols used by the source documents and verification implementations.

<!-- END canonical-unit M02 -->

## Where this leads

With the channel fixed, [the global one-use criterion](single-use.md) determines exactly when its optimized coherent information becomes zero.

---

Scientific editing sources: [MODEL_AND_CLAIMS.md](../docs/MODEL_AND_CLAIMS.md). [Section map](../website/furnishing-map.json).
