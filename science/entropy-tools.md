# Entropy tools and the common-error comparison

[Science](README.md) · [Learning](../learning/README.md) · [References](../references/README.md) · [Verification](../verification/README.md)

Two parts of the proof use the same conditional-state entropies in different ways. The one-use argument compares costs over all input eigenvalues and directions; the repetition argument bounds the entropy carried by complete classical records.

The elementary tools are stated first. An integral representation then reveals two compatible curvature properties in different variables. Its endpoint chord has one coefficient shared by all axes because their reporting error is common. [The scalar inequality](scalar-inequality.md) bounds the remaining intercept uniformly.

<!-- BEGIN canonical-unit P02 -->
<a id="p02"></a>
## P02. Elementary entropy tools used below

**Sources:** [S8](../docs/SOURCE_TO_CANONICAL.md#s8) §3.2; [S9](../docs/SOURCE_TO_CANONICAL.md#s9) §§2–3, 7; [S10](../docs/SOURCE_TO_CANONICAL.md#s10) §5; [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §§2–3; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §§2–3. **Claims:** C2–C4.

The proof uses the following standard binary-entropy and quantum-entropy facts.

For $`0\leq x,\chi\leq1`$, let

```math
D_\chi(x)=h_2(x)-\mathcal H(4(1-\chi)x(1-x)).
```

This is the entropy decrease when a qubit's diagonal $`(1-x,x)`$ gains squared normalized coherence $`\chi`$. The relevant bounds are

```math
h_2(x)\leq2\sqrt{x(1-x)},\qquad \frac2{\ln2}\chi x(1-x)\leq D_\chi(x)\leq\chi h_2(x).
```

**(P2.1)**

For the lower bound, diagonal dephasing gives a relative-entropy difference $`D_\chi(x)`$. Pinsker's inequality and the trace norm $`2\sqrt{\chi x(1-x)}`$ of the off-diagonal difference give the displayed coefficient in bits. For the upper bound, $`D_\chi(x)`$ is convex in $`\chi`$ with endpoint values $`0,h_2(x)`$; its endpoint chord bounds it above. This follows from the concavity of the square-root form of binary entropy. The first inequality is the binary-entropy overlap bound. Its role is to convert a sum of conditional entropies to a product of record overlaps.

The determinant-entropy function $`\mathcal H`$ is increasing and concave on $`[0,1]`$, with $`\mathcal H(0)=0`$. In particular,

```math
\mathcal H(cy)\geq c\mathcal H(y),\qquad 0\leq c,y\leq1.
```

**(P2.2)**

For fixed measurement effects and a fixed input direction, the cost $`C_\epsilon(t,x)`$ is concave in $`t`$. An affine classical–quantum representation establishes this: the blocks $`\sqrt{E_s}\rho_t\sqrt{E_s}`$ depend affinely on $`t`$, and have the same nonzero spectra and traces as the conditional-reference blocks. The average conditional entropy is concave on this affine family. This concavity justifies the lower secants in [P07](scalar-inequality.md#p07).

An increase of symmetric reporting error within $`[0,1/2]`$ can be implemented as additional classical sign flips. Such processing cannot decrease the average conditional-reference entropy. This fixes the direction of the noise-monotonic bound used in the certificate.

<!-- END canonical-unit P02 -->

<!-- BEGIN canonical-unit P03 -->
<a id="p03"></a>
## P03. Entropy integral and the comparison variable

**Sources:** [S9](../docs/SOURCE_TO_CANONICAL.md#s9) §§2–4; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §2; [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §2; [S10](../docs/SOURCE_TO_CANONICAL.md#s10) §2. **Claims:** C2, C4.

### P03.1 Integral identity

Let $`r_1,r_2\geq0`$ be the two unnormalized eigenvalues of a conditional state. They have sum $`q`$ and product $`\Delta`$. Factorization gives

```math
v(v+q)+\Delta=(v+r_1)(v+r_2).
```

Integrating the logarithm of the ratio on $`v\in(0,\infty)`$ and using $`r_1+r_2=q`$ to cancel the large-$`v`$ boundary term gives

```math
\int_0^\infty\ln\left(1+\frac{\Delta}{v(v+q)}\right)dv =q\ln q-r_1\ln r_1-r_2\ln r_2.
```

Consequently,

```math
\boxed{F(q,\Delta)=\frac1{\ln2}\int_0^\infty\ln\left(1+\frac{\Delta}{v(v+q)}\right)dv.}
```

**(P3.1)**

Zero determinant is handled by continuity; it is not evaluated by an undefined logarithm expression.

### P03.2 Two compatible curvature statements

For fixed $`t,\epsilon`$, put $`r_t=1-2t`$ and

```math
g=\frac{c}{1-ax}\in[c,1].
```

Pairing the two reports in (P3.1) yields an integrand

```math
\ln(\mathsf A_v g+\zeta_t)-\ln(\mathsf B_v g+\zeta_t),
```

where

```math
\begin{aligned} \mathsf A_v&=(v+1/2+\Delta_t/v)^2-r_t^2/4,\\ \mathsf B_v&=(v+1/2)^2-r_t^2/4,\\ \zeta_t&=r_t^2c/4. \end{aligned} 
```

For interior inputs and $`v\gt 0`$, $`\mathsf A_v\gt \mathsf B_v\gt 0`$, $`\zeta_t\geq0`$. Its second derivative in $`g`$ is

```math
-\left(\frac{\mathsf A_v}{\mathsf A_vg+\zeta_t}\right)^2 +\left(\frac{\mathsf B_v}{\mathsf B_vg+\zeta_t}\right)^2\leq0.
```

Thus $`C_\epsilon(t,x)`$ is concave as a function of $`g`$. At $`t=1/2`$ the integrand is constant in $`g`$; at $`t=0`$ use the pure-input limit.

In the original squared-projection variable, the paired integrand instead has the form

```math
\begin{aligned} &\ln\frac{A_v-\omega_x/4}{B_v-\omega_x/4},\\ A_v&=(v+1/2+\Delta_t/v)^2,\\ B_v&=(v+1/2)^2,\\ \omega_x&=ar_t^2x. \end{aligned} 
```

Its first derivative in $`\omega_x`$ is nonnegative and its second is

```math
\frac1{16}\left[(B_v-\omega_x/4)^{-2}-(A_v-\omega_x/4)^{-2}\right]\geq0.
```

Therefore the paired cost is increasing and convex in $`x`$. The two statements do not conflict: $`x\mapsto g`$ is nonlinear. They support different parts of the proof.

### P03.3 The endpoint chord

Define the endpoint costs, with $`\epsilon`$ fixed,

```math
\begin{aligned} C_\perp(t)&=\mathcal H(4ct(1-t)),\\ C_\parallel(t)&=h_2(t)+h_2(\epsilon)-h_2(\epsilon+\eta t). \end{aligned} 
```

The second expression is classical conditional entropy for a noisy binary record of an input aligned with its measurement axis. Concavity in $`g`$ gives

```math
C_\epsilon(t,x)\geq\frac{1-g}{a}C_\perp(t)+\frac{g-c}{a}C_\parallel(t).
```

**(P3.2)**

The previous facts imply

```math
C_\perp(t)\geq c h_2(t),\qquad C_\perp(t)\leq C_\parallel(t)\leq h_2(t).
```

For $`t\gt 0`$ define

```math
\beta(t,\epsilon)=\frac{C_\parallel(t)-C_\perp(t)}{a h_2(t)}\in[0,1].
```

Rearranging the chord,

```math
\frac{C_\epsilon(t,x)}{h_2(t)} \geq\beta g+\frac{C_\perp(t)-c\beta h_2(t)}{h_2(t)}.
```

**(P3.3)**

The next scalar inequality controls this intercept for all interior errors and all input weights. The same $`\beta`$ will apply to every axis precisely because the error is common.

<!-- END canonical-unit P03 -->

## Where this leads

Use [the scalar lemma and its complete domain coverage](scalar-inequality.md) for the global one-use obstruction. The overlap bounds return in [the all-record repetition construction](repetition-coding.md#p09).

---

Scientific editing sources: [COMPLETE_PROOF.md](../docs/COMPLETE_PROOF.md). [Section map](../website/furnishing-map.json).
