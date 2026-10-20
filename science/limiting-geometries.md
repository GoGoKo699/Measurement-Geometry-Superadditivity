# Coplanarity, noise endpoints and the exact cone family

[Science](README.md) · [Learning](../learning/README.md) · [References](../references/README.md) · [Verification](../verification/README.md)

The boundary cases clarify the content of the full-span guarantee. Coplanarity closes the strict comparison for long balanced repetitions, while the two noise endpoints follow from direct channel arguments. The coplanar statement is scoped to that coding comparison.

The universal closure result controls every allowed sequence of weighted ensembles at a fixed interior error. The cone family supplies a particular exact leading coefficient and has its own stated validity domain. Small frame eigenvalue can arise from small weights on out-of-plane axes as well as from axes moving toward a plane.

<!-- BEGIN canonical-unit M06 -->
<a id="m06"></a>
## 6. Controls and limiting family (C6)

**Coplanar axes.** A common perpendicular direction gives $`\Gamma=L=c`$. Thus, for this strict long-balanced-repetition criterion and the declared common-noise model,

```math
L\lt \Gamma\quad\Longleftrightarrow\quad\mathrm{rank}(T)=3.
```

This is not an all-code converse against coplanar channels. It does not exclude exceptional finite blocks or a different encoding family. [P11](#p11)

**Noise endpoints.** At $`\epsilon=0`$, $`I_c=(1-p)S(\rho)`$ is positive for mixed inputs when $`p\lt 1`$, while the all-measured channel has zero capacity. At $`\epsilon=1/2`$, the record is input independent and the channel is an erasure channel up to independent flags, with $`Q=Q^{(1)}=\max\{0,1-2p\}`$. Neither endpoint has a $`Q^{(1)}=0\lt Q`$ region in this model. The endpoint arguments are separate from formulas that divide by $`a`$ or $`c`$ in the interior. [P11](#p11)

<!-- BEGIN linear-threshold-closure -->
<a id="m06-linear-closure"></a>
**Universal linear closure.** For every allowed finite ensemble at each fixed common interior error,

```math
\frac{d_\epsilon\lambda}{(1+c+a\lambda)^2}
\leq p_{\mathrm{rep}}-p_1\leq\frac{(1-\sqrt c)\lambda}{(1+c)^2}.
```

Consequently $`p_{\mathrm{rep}}-p_1=\Theta_\epsilon(\lambda)`$ as $`\lambda\downarrow0`$, with positive comparison constants depending only on the fixed reporting error. This measures the closing of the one-use/repetition threshold gap under weighted departure from coplanarity. For full span, $`[p_1,p_{\mathrm{rep}})`$ is a sufficient interval with $`Q^{(1)}=0\lt Q`$; its width is distinct from an achievable rate. The lower bound inherits the entropy certificate. [Proof and uniform constants](geometric-gap.md#p08-linear-closure)
<!-- END linear-threshold-closure -->

**Cone family.** For three equally probable axes at azimuths $`2\pi j/3`$ and common vertical component $`\sqrt\lambda`$,

```math
\mathbf n_j=(\sqrt{1-\lambda}\cos(2\pi j/3),\sqrt{1-\lambda}\sin(2\pi j/3),\sqrt\lambda),\quad j=0,1,2.
```

For every common interior error and $`0\leq\lambda\leq1/4`$,

```math
\Gamma=\frac{c}{1-a\lambda},\qquad L=\frac{c}{\sqrt{1-a\lambda}},
```

```math
p_{\mathrm{rep}}-p_1=\frac{ca}{2(1+c)^2}\lambda+O(\lambda^2)\qquad(\lambda\downarrow0,\ \epsilon\text{ fixed}).
```

The exact larger domain is $`0\leq\lambda\leq\min\{1/3,W(a)/P(a)\}`$. The all-error interval through $`1/4`$ is the uniform domain used in the figure. Extension to $`1/3`$ requires the parameter-specific inequality. Neither curve is an exact all-code capacity boundary. [P12](#p12)

The cone calculation supplies a particular exact leading coefficient; the general corollary establishes linear scaling for every allowed ensemble.

**Sources:** [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §§5–6; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §8. The general linear-closure corollary is derived in P08 from P01 and (P8.3).

<!-- END canonical-unit M06 -->

<!-- BEGIN canonical-unit P11 -->
<a id="p11"></a>
## P11. Coplanar geometry and the two reporting-noise endpoints

**Sources:** [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §5; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §8; [S8](../docs/SOURCE_TO_CANONICAL.md#s8) §5; [S10](../docs/SOURCE_TO_CANONICAL.md#s10) §7. **External endpoint input:** EXT4–EXT5. **Claim:** C6.

### P11.1 Coplanarity and the restricted converse

If the supported axes are coplanar, choose $`\mathbf u`$ perpendicular to that plane. For that direction all squared projections vanish and $`G(\mathbf u)=\Lambda(\mathbf u)=c`$. For every direction, (P2.2) and monotonicity of the paired cost give

```math
C_\epsilon(t,x)\geq C_\perp(t)\geq c h_2(t).
```

Thus $`\Gamma\geq c`$; the perpendicular nearly pure input approaches $`c`$, so $`\Gamma=c`$. The directional loss is always at least $`c`$ and reaches it perpendicularly, so $`L=c`$. Combining with the strict full-span bound proves

```math
L\lt \Gamma\quad\Longleftrightarrow\quad\mathrm{rank}(T)=3
```

for the defined long-balanced-repetition comparison throughout the common interior-error range. This is not a zero-capacity theorem for all coplanar channels above their one-use threshold, and does not exclude other codes or exceptional finite blocks. Two noncommuting axes can still be coplanar; incompatibility alone is not the criterion.

### P11.2 Perfect records, $`\epsilon=0`$

The measurement effects have rank one and the conditional reference state for every reported outcome is pure. Hence

```math
I_c=(1-p)S(\rho).
```

A mixed input has positive one-use coherent information whenever $`p\lt 1`$. At $`p=1`$ the channel is quantum-to-classical and cannot transmit unknown quantum information. Thus there is no $`Q^{(1)}=0\lt Q`$ region at this endpoint. This reasoning is direct from the physical channel, not a substitution into formulas with $`c`$ in a denominator.

### P11.3 Completely random records, $`\epsilon=1/2`$

All reported signs are independent of the input. The axes and sign labels are additional independent flags on an erasure channel. Its known capacity is

```math
Q=Q^{(1)}=\max\{0,1-2p\}.
```

There is again no separation. Full span of nominal axes does not make a record informative when $`\eta=0`$. The endpoint capacity follows from the erasure-capacity theorem. A known sign inversion exchanges errors above one half with errors below one half.

<!-- END canonical-unit P11 -->

<!-- BEGIN canonical-unit P12 -->
<a id="p12"></a>
## P12. The exact near-coplanar family and its valid domain

**Sources:** [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §6; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §8. **Claim:** C6.

For $`j=0,1,2`$, take equally probable axes

```math
\mathbf n_j=(\sqrt{1-\lambda}\cos(2\pi j/3),\sqrt{1-\lambda}\sin(2\pi j/3),\sqrt\lambda).
```

For $`0\leq\lambda\leq1/3`$,

```math
T=\mathrm{diag}\left(\frac{1-\lambda}{2},\frac{1-\lambda}{2},\lambda\right),
```

so the cone parameter is the smallest frame eigenvalue. The increasing-convex scalar functions $`(1-ax)^{-1}`$ and $`(1-ax)^{-1/2}`$, Jensen's inequality, and $`\mathbf u^{\mathsf T}T\mathbf u\geq\lambda`$ give minima attained by the vertical direction:

```math
G_{\min}=\frac{c}{1-a\lambda},\qquad L=\frac{c}{\sqrt{1-a\lambda}}.
```

**(P12.1)**

If $`\lambda\leq W(a)/P(a)`$, then $`G_{\min}\leq\ell`$. The global lower bound (P4.2) and the axial nearly pure upper bound from P01 therefore agree:

```math
\boxed{\Gamma=\frac{c}{1-a\lambda}\quad\text{for}\quad 0\leq\lambda\leq\min\{1/3,W(a)/P(a)\}.}
```

**(P12.2)**

The polynomial identities imply $`W/P\geq1/4`$. Thus every common interior error has the exact cone formulas on $`0\leq\lambda\leq1/4`$. The larger domain depends on the chosen error. Also

```math
3W-P=\frac{(2a-1)(5-a^2)}{20},
```

so $`a\geq1/2`$ suffices to extend the exact formulas through $`\lambda=1/3`$. This includes the error of the eight-use example but not every interior error.

Expansion at fixed error gives

```math
\boxed{p_{\mathrm{rep}}-p_1 =\frac{ca}{2(1+c)^2}\lambda+O(\lambda^2),\qquad\lambda\downarrow0.}
```

**(P12.3)**

Here $`p_1`$ is the exact single-use boundary for this valid cone range, while $`p_{\mathrm{rep}}`$ is the construction frontier. Neither is asserted to be the optimal capacity phase boundary. The gap can be arbitrarily small; the working block length and achievable rate depend on the fixed channel parameters.

<!-- END canonical-unit P12 -->

## Where this leads

The Pauli witness uses a sharper equality case within the valid cone domain. See [its complete calculation and numerical controls](eight-use-witness.md).

---

Scientific editing sources: [COMPLETE_PROOF.md](../docs/COMPLETE_PROOF.md) · [MODEL_AND_CLAIMS.md](../docs/MODEL_AND_CLAIMS.md). [Section map](../website/furnishing-map.json).
