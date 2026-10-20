# The exact one-use boundary and the repetition frontier

[Science](README.md) · [Learning](../learning/README.md) · [References](../references/README.md) · [Verification](../verification/README.md)

The comparison begins with every single-qubit density matrix, including mixed inputs arbitrarily close to purity. Conditioning on the reported records gives an exact coherent-information identity and a global minimization problem.

The one-use positivity boundary is exact. The repetition frontier refers to a specified family of sufficiently long balanced blocks; [its coding proof](repetition-coding.md) establishes that separate statement. The nearly pure directional cost supplies an upper bound on the global minimum. [The mixed-input control](eight-use-witness.md#p134) explains why it cannot generally be substituted for that minimum.

<!-- BEGIN canonical-unit M03 -->
<a id="m03"></a>
## 3. Exact single-use benchmark and the constructed frontier

Every mixed qubit density matrix can be written

```math
\rho_{t,\mathbf u}=\frac{I+(1-2t)\mathbf u\cdot\boldsymbol\sigma}{2},\qquad 0\lt t\leq\frac12.
```

The flagged coherent-information identity and its global cost are

```math
\begin{aligned} I_c&=(1-p)h_2(t)-pC(t,\mathbf u),\\ \Gamma&=\inf_{\|\mathbf u\|=1,\ 0\lt t\leq1/2}\frac{C(t,\mathbf u)}{h_2(t)}. \end{aligned} 
```

Pure inputs have zero coherent information. Consequently the **exact one-use positivity boundary** is

```math
p_1=\frac1{1+\Gamma},\qquad Q^{(1)}=0\ \Longleftrightarrow\ p\geq p_1.
```

Define

```math
T=\sum_b w_b\mathbf n_b\mathbf n_b^{\mathsf T},\quad\lambda=\lambda_{\min}(T),
```

```math
\begin{aligned} \Lambda(\mathbf u)&=\sum_b\frac{w_b c}{\sqrt{1-a(\mathbf n_b\cdot\mathbf u)^2}},\\ L&=\min_{\|\mathbf u\|=1}\Lambda(\mathbf u). \end{aligned} 
```

The balanced antipodal repetition construction has a **strict eventual-sign frontier**, optimized over its fixed direction,

```math
p_{\mathrm{rep}}=\frac1{1+L}.
```

Below that frontier, some sufficiently large finite block has positive coherent information. Above the corresponding fixed-direction frontier, sufficiently long balanced blocks in that direction are negative. Equality and exceptional shorter blocks are not settled by those exponential bounds. Thus $`p_{\mathrm{rep}}`$ is not identified with the optimal quantum-capacity threshold or the best finite-block threshold. **Sources:** [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §§1–2, 4; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §§1, 6; [S8](../docs/SOURCE_TO_CANONICAL.md#s8) §§2–4.

<!-- END canonical-unit M03 -->

<!-- BEGIN canonical-unit P01 -->
<a id="p01"></a>
## P01. Physical channel and exact single-use positivity criterion

**Sources:** [S3](../docs/SOURCE_TO_CANONICAL.md#s3); [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §§1–2; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §1. **Claims:** C1–C3.

Fix finitely many unit axes $`\mathbf n_b`$, positive probabilities $`w_b`$, a common $`0\lt \epsilon\lt 1/2`$, and independent channel uses. Let $`r`$ denote the true projective bit and $`s`$ the reported bit. The projectors and reporting probabilities are

```math
\Pi_{b,r}=\frac{I+(-1)^r\mathbf n_b\cdot\boldsymbol\sigma}{2},\qquad \Pr(s\mid r)=\begin{cases}1-\epsilon,&s=r,\\\epsilon,&s\ne r.\end{cases}
```

The physical qubit is discarded after measurement. Summing over the hidden true bit gives

```math
E_{b,s}=\sum_r\Pr(s\mid r)\Pi_{b,r} =\frac{I+(-1)^s\eta\mathbf n_b\cdot\boldsymbol\sigma}{2},\quad\eta=1-2\epsilon.
```

The channel is

```math
\begin{aligned} \mathcal N_{p,\epsilon}(\rho)&=(1-p)\rho\oplus\\ &\quad p\sum_{b,s}w_b\,\mathrm{Tr}(E_{b,s}\rho)|b,s\rangle\langle b,s|. \end{aligned} 
```

The encoder knows the channel parameters, not the future branch, axis or outcomes. There is no assistance, postselection or rereading. The two receiver branches have orthogonal flags, and the axis probability sits outside each fixed-axis effect.

Write $`a=\eta^2`$ and $`c=1-a=4\epsilon(1-\epsilon)`$. An arbitrary input has eigenvalues $`(1-t,t)`$ with $`0\leq t\leq1/2`$ and eigenvectors $`|\mathbf u_+\rangle,|\mathbf u_-\rangle`$. A purification is

```math
|\Psi_{t,\mathbf u}\rangle=\sqrt{1-t}|0\rangle_{\mathsf R}|\mathbf u_+\rangle +\sqrt t|1\rangle_{\mathsf R}|\mathbf u_-\rangle.
```

In this input eigenbasis, put $`D_t=\mathrm{diag}(\sqrt{1-t},\sqrt t)`$. The fixed-axis subnormalized reference state for reported outcome $`s`$ is

```math
\tau_{b,s}=D_t(E_{b,s}^{(\mathbf u)})^{\mathsf T}D_t.
```

The transpose is fixed by the purification convention; it does not alter the eigenvalue formulas below. Its trace and determinant are

```math
q_{b,s}=\frac{1+(-1)^s\eta(1-2t)\mathbf n_b\cdot\mathbf u}{2},\qquad \det\tau_{b,s}=\Delta_t=\frac c4t(1-t).
```

For a positive $`2\times2`$ matrix with trace $`q`$ and determinant $`\Delta`$, define its homogeneous entropy

```math
F(q,\Delta)=q\,h_2\!\left(\frac{1-\sqrt{1-4\Delta/q^2}}2\right).
```

The entropy cost averaged within the measured branch is

```math
C(t,\mathbf u)=\sum_{b,s}w_b F(q_{b,s},\Delta_t).
```

Equivalently, with $`x=(\mathbf n\cdot\mathbf u)^2`$ and $`\mathcal H(z)=h_2((1-\sqrt{1-z})/2)`$,

```math
\begin{aligned} q_\pm&=\frac{1\pm\eta(1-2t)\sqrt x}{2},\\ C_\epsilon(t,x)&=\sum_{\pm}q_\pm\mathcal H(4\Delta_t/q_\pm^2),\\ C(t,\mathbf u)&=\sum_b w_b C_\epsilon(t,(\mathbf n_b\cdot\mathbf u)^2). \end{aligned} 
```

These are entropies conditioned on the **reported** bit, not on the hidden true bit. Because the two main flags and classical measured records are shared in the entropy difference, their Shannon entropies cancel. The intact branch contributes $`h_2(t)`$ and the measured branch contributes $`-C(t,\mathbf u)`$:

```math
\boxed{I_c(\rho_{t,\mathbf u},\mathcal N_{p,\epsilon})=(1-p)h_2(t)-pC(t,\mathbf u).}
```

**(P1.1)**

For $`t=0`$, the reference is one dimensional and the coherent information is exactly zero. For all mixed inputs define

```math
\Gamma=\inf_{\|\mathbf u\|=1,\ 0\lt t\leq1/2}\frac{C(t,\mathbf u)}{h_2(t)}.
```

If $`p\geq1/(1+\Gamma)`$, every mixed input has nonpositive coherent information, while pure inputs attain zero. Conversely, if $`0\lt p\lt 1/(1+\Gamma)`$, the definition of the infimum supplies a positive $`t`$ and direction with $`C/h_2\lt (1-p)/p`$. At $`p=0`$ any mixed input gives positive coherent information directly. Hence

```math
\boxed{Q^{(1)}(\mathcal N_{p,\epsilon})=0\quad\Longleftrightarrow\quad p\geq p_1:=\frac1{1+\Gamma}.}
```

**(P1.2)**

No optimizing direction or input weight has been presumed. For later use, the full-rank fixed-error posterior expansion gives the directional nearly pure ratio

```math
\lim_{t\downarrow0}\frac{C(t,\mathbf u)}{h_2(t)} =G(\mathbf u):=\sum_b\frac{w_b c}{1-a(\mathbf n_b\cdot\mathbf u)^2}.
```

Thus $`\Gamma\leq G_{\min}:=\min_{\mathbf u}G(\mathbf u)`$. Equality requires an additional argument and is not used as a general premise. The numerical control in [P13.4](eight-use-witness.md#p134) illustrates why.

<!-- END canonical-unit P01 -->

## Where this leads

The next step is to bound the global cost for every input. [Entropy tools and the endpoint chord](entropy-tools.md) provide the reduction used by the scalar inequality.

---

Scientific editing sources: [COMPLETE_PROOF.md](../docs/COMPLETE_PROOF.md) · [MODEL_AND_CLAIMS.md](../docs/MODEL_AND_CLAIMS.md). [Section map](../website/furnishing-map.json).
