# Full-span separation and universal linear closure

[Science](README.md) · [Learning](../learning/README.md) · [References](../references/README.md) · [Verification](../verification/README.md)

The smallest frame eigenvalue measures the least weighted squared projection onto a possible plane normal. Full span makes this quantity positive and removes a common perpendicular direction. The argument below turns that geometric fact into a strict separation between two entropy costs.

The theorem states the quantifiers and the conservative sufficient interval. The corollary then gives two-sided linear bounds on the gap between the exact one-use boundary and the balanced-repetition frontier, uniformly over finite ensembles at each fixed interior error. A threshold width does not determine a communication rate or a uniform block length. Capacity positivity also uses [the finite-block and outer-coding argument](repetition-coding.md#p10).

<!-- BEGIN canonical-unit M04 -->
<a id="m04"></a>
## 4. The theorem and quantifier order (C1–C4)

For every fixed allowed ensemble and every common $`0\lt \epsilon\lt 1/2`$,

```math
\boxed{\Gamma\geq L+d_\epsilon\lambda,\qquad d_\epsilon=\frac3{35}ca.}
```

If the axes span $`\mathbb R^3`$, then $`\lambda\gt 0`$ and

```math
\boxed{\begin{aligned} &\frac1{1+L+d_\epsilon\lambda}\leq p\lt \frac1{1+L}\\ &\quad\Longrightarrow\quad Q^{(1)}(\mathcal N_{p,\epsilon})=0\lt Q(\mathcal N_{p,\epsilon}). \end{aligned}} 
```

The endpoints certify a nonempty subinterval, not the complete capacity-positive/negative boundary. The constant is conservative, not optimized. The lower endpoint is included and the upper endpoint is excluded.

The order of choices is: fix the ensemble and reporting error; choose an allowed $`p`$; choose a code direction from those known channel parameters; then choose a sufficiently long finite block; then apply the asymptotic coding theorem to repeated uses of that fixed block. Realized future axes or outcomes do not influence the encoding. The achievable rate, required block length and interval of $`p`$ depend on the ensemble and reporting error.

The proof is the composition of a global one-use bound, a constructive all-record repetition bound, and the geometric inequality separating them. Its scalar entropy component is computer assisted. The complete proof is [P01–P10](single-use.md#p01). **Sources:** [S3](../docs/SOURCE_TO_CANONICAL.md#s3); [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §§1–4; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §§1–6; [S8](../docs/SOURCE_TO_CANONICAL.md#s8) §3.

<!-- END canonical-unit M04 -->

<!-- BEGIN canonical-unit P08 -->
<a id="p08"></a>
## P08. Geometry separates the global costs

**Sources:** [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §4; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §5; source [C1](../docs/SOURCE_TO_CANONICAL.md#c1)–[C2](../docs/SOURCE_TO_CANONICAL.md#c2). **Claims:** C1, C4, C6. The linear-closure corollary below is derived here from P01 and (P8.3).

For $`0\leq y\lt 1`$,

```math
(1-y)^{-1}-(1-y)^{-1/2}\geq y/2.
```

Apply it to $`y=a(\mathbf n_b\cdot\mathbf u)^2`$ before minimizing. With

```math
\Lambda(\mathbf u)=\sum_b\frac{w_b c}{\sqrt{1-a(\mathbf n_b\cdot\mathbf u)^2}},\quad L=\min_{\|\mathbf u\|=1}\Lambda(\mathbf u),
```

it yields

```math
G(\mathbf u)-\Lambda(\mathbf u)\geq\frac{ca}{2}\mathbf u^{\mathsf T}T\mathbf u\geq\frac{ca}{2}\lambda,
```

```math
G_{\min}\geq L+\frac{ca}{2}\lambda.
```

**(P8.1)**

The continuous directional losses have positive denominators for interior error, so compactness of the unit sphere gives an attained minimum $`L`$.

To bound the other entry in (P4.2), average over a uniformly distributed direction $`\mathbf u`$ on the Bloch sphere:

```math
L\leq A_\epsilon:=c\,\frac{\arcsin\sqrt a}{\sqrt a}.
```

This is an existence bound for a fixed encoding direction, not permission to adapt the encoder to a future randomly chosen measurement axis. Positivity of the arcsin power-series coefficients gives

```math
\frac{\arcsin\sqrt a}{\sqrt a}\leq1+\frac a6+\frac{3a^2}{40} +\left(\frac\pi2-\frac{149}{120}\right)a^3.
```

Using $`\pi\lt 22/7`$,

```math
P(a)-\frac{\arcsin\sqrt a}{\sqrt a}\gt a\left(\frac1{12}+\frac{7a}{40}-\frac{193a^2}{840}\right)\geq\frac a{35}.
```

The quadratic is concave and its smaller endpoint value on $`[0,1]`$ is $`1/35`$. The exact positive integral

```math
\frac{22}{7}-\pi=\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx\gt 0
```

is an elementary certification of the bound on $`\pi`$. Since $`\mathrm{Tr}(T)=1`$, $`0\leq\lambda\leq1/3`$. Therefore

```math
\ell\gt L+\frac{ca}{35}\geq L+\frac3{35}ca\lambda.
```

**(P8.2)**

Combine (P4.2), (P8.1) and (P8.2):

```math
\boxed{\Gamma\geq L+d_\epsilon\lambda,\qquad d_\epsilon=\frac3{35}ca.}
```

**(P8.3)**

If the supported axes span $`\mathbb R^3`$, positive weights give $`\lambda\gt 0`$; interior error gives $`ca\gt 0`$. No lower bound on $`\lambda`$ beyond positivity has been imposed.

The width of the guaranteed overlap interval is

```math
\begin{aligned} \Delta p_{\mathrm{cert}} &=\frac{d_\epsilon\lambda}{(1+L)(1+L+d_\epsilon\lambda)}\\ &\geq\frac{d_\epsilon}{(1+A_\epsilon)(1+A_\epsilon+d_\epsilon/3)}\lambda. \end{aligned} 
```

This is a width bound, not a rate. Its uniform coefficient can tend to zero near either noise endpoint, just as the width can vanish when the frame approaches a plane.

<!-- BEGIN linear-threshold-closure -->
<a id="p08-linear-closure"></a>
### Corollary: universal linear closing of the one-use/repetition threshold gap

Fix a common $`0\lt\epsilon\lt1/2`$ and any allowed finite ensemble. Write $`x_b(\mathbf u)=(\mathbf n_b\cdot\mathbf u)^2`$. Since $`a,c\in(0,1)`$ and $`a+c=1`$, the increasing function $`f(x)=c/\sqrt{1-ax}`$ has $`f''(x)=3ca^2/[4(1-ax)^{5/2}]\gt0`$ on $`[0,1]`$. Its endpoint chord gives

```math
c\leq f(x)\leq c+(\sqrt c-c)x.
```

Let $`\mathbf v`$ be a unit eigenvector of $`T`$ for $`\lambda`$. It is a trial direction for the minimum defining $`L`$: the identity $`\sum_b w_bx_b(\mathbf v)=\mathbf v^{\mathsf T}T\mathbf v=\lambda`$ yields

```math
c\leq L\leq\Lambda(\mathbf v)\leq c+(\sqrt c-c)\lambda.
```

Choose instead a unit minimizer $`\mathbf u_L`$ of $`\Lambda`$, whose existence follows from continuity, positive denominators and compactness as above. For $`s=\sqrt{1-ax}\in[\sqrt c,1]`$, the numerator $`c/s-c`$ is nonnegative, so

```math
\frac{c}{s^2}-\frac{c}{s}=\frac{c/s-c}{s}\leq\frac{c/s-c}{\sqrt c}.
```

Use the upper bound $`\Gamma\leq G_{\min}\leq G(\mathbf u_L)`$ from [P01](single-use.md#p01), and apply this scalar inequality before summing:

```math
\Gamma-L\leq G(\mathbf u_L)-\Lambda(\mathbf u_L)
\leq\frac{L-c}{\sqrt c}\leq(1-\sqrt c)\lambda.
```

The common reporting error supplies the same scalar chord and denominator bound for every axis. No optimizer of $`G`$ or $`\Gamma`$ is needed; the distinction between $`\Gamma`$ and $`G_{\min}`$ in [P13.4](eight-use-witness.md#p134) remains essential. Combining with (P8.3), and using $`(\sqrt c-c)+(1-\sqrt c)=a`$, proves

```math
\boxed{\begin{aligned}
d_\epsilon\lambda&\leq\Gamma-L\leq(1-\sqrt c)\lambda,\\
c&\leq L\leq\Gamma\leq c+a\lambda.
\end{aligned}}
```

By the threshold identities in [M03](single-use.md#m03), proved in [P01](single-use.md#p01) and [P10](repetition-coding.md#p10), their separation is

```math
\Delta p:=p_{\mathrm{rep}}-p_1
=\frac{\Gamma-L}{(1+L)(1+\Gamma)}.
```

The denominator lies between $`(1+c)^2`$ and $`(1+c+a\lambda)^2`$. Thus

```math
\boxed{\frac{d_\epsilon\lambda}{(1+c+a\lambda)^2}
\leq\Delta p\leq\frac{(1-\sqrt c)\lambda}{(1+c)^2}.}
```

In particular, since $`\lambda\leq1/3`$,

```math
\begin{aligned}
\frac{d_\epsilon}{(1+c+a/3)^2}\lambda
&\leq\Delta p\leq\frac{1-\sqrt c}{(1+c)^2}\lambda,\\
\Gamma-L&=\Theta_\epsilon(\lambda),\qquad
p_{\mathrm{rep}}-p_1=\Theta_\epsilon(\lambda).
\end{aligned}
```

Both comparison constants are strictly positive at each fixed interior error, independently of the directions, positive weights and finite number of axes. The scaling holds along every sequence of such full-span ensembles with $`\lambda\downarrow0`$; at $`\lambda=0`$ the bounds give $`\Gamma=L=c`$. The lower comparison constant vanishes at both noise endpoints, so the linear comparison fixes an interior error. The upper bounds are elementary; the lower bounds inherit the computer-assisted scalar lemma through (P8.3). The separate bound for the explicit certified subinterval $`\Delta p_{\mathrm{cert}}`$ above remains available.

Geometrically, $`\lambda=\min_{\|\mathbf u\|=1}\sum_b w_b(\mathbf n_b\cdot\mathbf u)^2`$ measures the least weighted squared projection onto a candidate plane normal. Small values express weighted departure from coplanarity: they can reflect axes close to a plane or small weights on axes outside it. Individual axes need not all approach a plane.

For $`\lambda\gt0`$, the interval $`[p_1,p_{\mathrm{rep}})`$ is sufficient for $`Q^{(1)}=0\lt Q`$, including its lower endpoint and excluding its upper endpoint. Positivity uses a finite inner block followed by asymptotic outer coding as in P10. The corollary quantifies separation of the two defined thresholds; its scaling concerns neither an achievable rate nor the complete capacity-positive region. The coding scope of P10 and the coplanar qualification of P11 remain in force.
<!-- END linear-threshold-closure -->

<!-- END canonical-unit P08 -->

## Where this leads

[Repetition coding](repetition-coding.md) supplies the positive finite block required by the theorem. [Limiting geometries](limiting-geometries.md) gives the restricted coplanar converse and an exactly soluble cone family.

---

Scientific editing sources: [COMPLETE_PROOF.md](../docs/COMPLETE_PROOF.md) · [MODEL_AND_CLAIMS.md](../docs/MODEL_AND_CLAIMS.md). [Section map](../website/furnishing-map.json).
