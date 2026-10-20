# All-record repetition coding and positive capacity

[Science](README.md) · [Learning](../learning/README.md) · [References](../references/README.md) · [Verification](../verification/README.md)

A fixed isometry encodes a logical qubit into the span of two antipodal product codewords. The balanced average input is separable but correlated, while its purification retains the logical coherence relevant to quantum transmission.

Every mask and reported record contributes to the coherent information, including the negative all-measured term. Polynomial prefactors and competing exponential bases determine the strict eventual sign. A positive finite inner block is selected before taking the separate asymptotic outer-coding limit. This order does not require the inner-block rate to have a positive limit as its length grows.

<!-- BEGIN canonical-unit P09 -->
<a id="p09"></a>
## P09. Complete all-record repetition construction

**Sources:** [S8](../docs/SOURCE_TO_CANONICAL.md#s8) §§3.1–3.3; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §6; [S9](../docs/SOURCE_TO_CANONICAL.md#s9) §7; [S10](../docs/SOURCE_TO_CANONICAL.md#s10) §5. **Claim:** C3. The repetition lemma is specialized to the common-error model.

### P09.1 Fixed code and its record coefficients

Let $`|\mathbf u_+\rangle,|\mathbf u_-\rangle`$ be the orthonormal eigenstates of $`\mathbf u\cdot\boldsymbol\sigma`$. Choose the isometry

```math
|0\rangle\mapsto|\mathbf u_+\rangle^{\otimes n},\qquad |1\rangle\mapsto|\mathbf u_-\rangle^{\otimes n},
```

and the balanced mixed input

```math
\rho_n(\mathbf u)=\frac12|\mathbf u_+\rangle\langle\mathbf u_+|^{\otimes n} +\frac12|\mathbf u_-\rangle\langle\mathbf u_-|^{\otimes n}.
```

Its average density matrix is separable but correlated. The purified reference/code state retains coherent superpositions; this is a legitimate quantum coding input, not cloning an arbitrary qubit. Fix the code before any future realized measurement choices.

For axis $`b`$, define

```math
\begin{aligned} s_b(\mathbf u)&=\sqrt{1-a(\mathbf n_b\cdot\mathbf u)^2},\\ \kappa_b(\mathbf u)&=\frac{a[1-(\mathbf n_b\cdot\mathbf u)^2]}{1-a(\mathbf n_b\cdot\mathbf u)^2}, \end{aligned} 
```

```math
B(\mathbf u)=\sum_b w_b s_b,\qquad K(\mathbf u)=\sum_b w_b s_b\kappa_b.
```

The per-record probabilities conditional on the two codewords are

```math
P_\pm(b,s)=w_b\frac{1\pm(-1)^s\eta\,\mathbf n_b\cdot\mathbf u}{2}.
```

The record overlap obeys

```math
\sum_{b,s}\sqrt{P_+(b,s)P_-(b,s)}=B(\mathbf u),
```

and insertion of $`\kappa_b`$ gives $`K(\mathbf u)`$. Direct subtraction yields

```math
B(\mathbf u)-K(\mathbf u)=\Lambda(\mathbf u).
```

**(P9.1)**

These record coefficients have a classical discrimination interpretation. The finite-axis bounds follow directly below.

### P09.2 Exact conditional states and the all-measured contribution

For $`m`$ reported measured sites, let $`\omega=(y_1,\ldots,y_m)`$, with $`y_j=(b_j,s_j)`$, and define

```math
\begin{aligned} \mathsf p_\pm(\omega)&=\prod_{j=1}^mP_\pm(y_j),\\ q_\omega&=\frac{\mathsf p_+(\omega)+\mathsf p_-(\omega)}2,\\ x_\omega&=\frac{\mathsf p_-(\omega)}{\mathsf p_+(\omega)+\mathsf p_-(\omega)},\\ \chi_\omega&=\prod_{j=1}^m\kappa_{b_j}. \end{aligned} 
```

When at least one code qubit survives, its two conditional codeword states remain orthogonal. In the two-dimensional support spanned by the matching reference/codeword states, the joint conditional density matrix has diagonal $`(1-x_\omega,x_\omega)`$ and off-diagonal magnitude

```math
\sqrt{\chi_\omega x_\omega(1-x_\omega)}.
```

Axis-dependent phases remain in the physical map but do not change its eigenvalues. Its determinant is $`(1-\chi_\omega)x_\omega(1-x_\omega)`$.

Define the measured-record averages

```math
\mathcal A_m=\sum_\omega q_\omega h_2(x_\omega),
```

```math
\mathcal R_m=\sum_\omega q_\omega D_{\chi_\omega}(x_\omega),\qquad \mathcal C_m=\mathcal A_m-\mathcal R_m,
```

with $`\mathcal A_0=\mathcal R_0=1`$ and $`\mathcal C_0=0`$. For at least one survivor, the conditional receiver entropy contributes $`\mathcal A_m`$ and the joint entropy contributes $`\mathcal C_m`$. If **all** $`n`$ qubits are measured, the receiver has no remaining quantum entropy: its conditional contribution is $`-\mathcal C_n`$.

Every mask and reported record therefore contributes to the exact block identity

```math
\boxed{\begin{aligned} \mathcal I_n&:=I_c(\rho_n(\mathbf u),\mathcal N_{p,\epsilon}^{\otimes n})\\ &=\sum_{m=0}^n{n\choose m}(1-p)^{n-m}p^m\mathcal R_m-p^n\mathcal A_n. \end{aligned}} 
```

**(P9.2)**

The $`m=n`$ terms combine to $`-p^n\mathcal C_n`$. The favorable-branch interpretation of the first sum does not delete this negative term.

### P09.3 Upper envelopes

The two entropy bounds (P2.1) give

```math
q_\omega h_2(x_\omega)\leq\sqrt{\mathsf p_+(\omega)\mathsf p_-(\omega)},
```

```math
q_\omega D_{\chi_\omega}(x_\omega) \leq\chi_\omega\sqrt{\mathsf p_+(\omega)\mathsf p_-(\omega)}.
```

Summing complete records factorizes into products of single-record sums:

```math
\mathcal A_m\leq B^m,\qquad\mathcal R_m\leq K^m.
```

**(P9.3)**

### P09.4 Polynomial lower envelopes without postselection

For a proof bound only, relabel outcome signs so that

```math
\pi_b^+=\frac{1+|\eta\mathbf n_b\cdot\mathbf u|}{2}\geq \pi_b^-=1-\pi_b^+\gt 0.
```

Full-rank noisy effects make the finite likelihood bound

```math
\mathcal L_{\mathrm{rec}}=\sum_{b=1}^J\ln(\pi_b^+/\pi_b^-),\qquad x_*=(1+e^{\mathcal L_{\mathrm{rec}}})^{-1}\gt 0
```

well defined. Set

```math
c_A=h_2(x_*)\gt 0,\qquad c_R=\frac2{\ln2}x_*(1-x_*)\gt 0.
```

Condition first on counts $`m_b`$ of each measurement axis, where $`\sum_bm_b=m`$. For each axis retain one central binomial sign class: its positive and negative counts differ by at most one, and its multiplicity is at least $`2^{m_b}/(m_b+1)`$. Consequently the entire retained record log-likelihood ratio has absolute value at most $`\mathcal L_{\mathrm{rec}}`$, independently of $`m`$. Thus its posterior satisfies

```math
h_2(x_\omega)\geq c_A,\qquad \frac2{\ln2}x_\omega(1-x_\omega)\geq c_R.
```

Also $`q_\omega\geq\sqrt{\mathsf p_+\mathsf p_-}`$. Combining these facts with the central-class multiplicity gives, for those fixed axis counts, contributions at least

```math
c_A\prod_b\frac{s_b^{m_b}}{m_b+1},\qquad c_R\prod_b\frac{(s_b\kappa_b)^{m_b}}{m_b+1}
```

to $`\mathcal A_m`$ and $`\mathcal R_m`$, respectively. The axis probabilities are then included through their multinomial weights. Since $`\prod_b(m_b+1)\leq(m+1)^J`$, their sum gives

```math
\boxed{\begin{aligned} \frac{c_A}{(m+1)^J}B^m&\leq\mathcal A_m\leq B^m,\\ \frac{c_R}{(m+1)^J}K^m&\leq\mathcal R_m\leq K^m. \end{aligned}} 
```

**(P9.4)**

The selection of central classes is only a lower bound on a sum of nonnegative entropy contributions. It does **not** change the channel or permit the decoder to postselect those events. The complete coherent-information identity remains (P9.2).

If an individual $`\kappa_b=0`$, the corresponding lower contribution is zero whenever that axis occurs; this agrees with the formula. If $`K=0`$, then $`\mathcal R_m=0`$ for $`m\gt 0`$ and the no-measurement term is handled directly. Under full span $`K\gt 0`$ for every fixed code direction. The $`m=0`$ convention is consistent with the bounds because $`c_A,c_R\leq1`$. Finitely many axes and strictly interior error are substantive here: the constants can depend strongly on the chosen channel and direction, but not on $`m`$.

<!-- END canonical-unit P09 -->

<!-- BEGIN canonical-unit P10 -->
<a id="p10"></a>
## P10. Finite inner blocks, outer coding and the main theorem

**Sources:** [S8](../docs/SOURCE_TO_CANONICAL.md#s8) §3.3–§4; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §6; [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §§1, 4. **External input:** EXT1, the coherent-information coding theorem. **Claims:** C1, C3.

Set

```math
\nu_+=1-p+pK(\mathbf u),\qquad\nu_-=pB(\mathbf u).
```

Insert (P9.4) into (P9.2), using $`(m+1)^J\leq(n+1)^J`$, to obtain

```math
\boxed{\frac{c_R}{(n+1)^J}\nu_+^n-\nu_-^n \leq\mathcal I_n\leq \nu_+^n-\frac{c_A}{(n+1)^J}\nu_-^n.}
```

**(P10.1)**

If $`\nu_+\gt \nu_-`$, their exponential ratio eventually dominates the polynomial factor and $`\mathcal I_n\gt 0`$ for every sufficiently large finite $`n`$. This strict condition is exactly

```math
p\lt \frac1{1+\Lambda(\mathbf u)}.
```

If $`\nu_+\lt \nu_-`$, sufficiently large blocks in that fixed direction are negative. The equality case and exceptional shorter blocks above that frontier are not settled by (P10.1).

For the headline theorem, first fix the channel ensemble, $`\epsilon`$ and a measurement probability

```math
\frac1{1+L+d_\epsilon\lambda}\leq p\lt \frac1{1+L},\qquad\lambda\gt 0.
```

The global cost inequality (P8.3) and (P1.2) give $`Q^{(1)}=0`$. Choose a unit direction attaining $`L`$ and then a sufficiently large finite inner length $`n`$ so that $`\mathcal I_n\gt 0`$. This is a code fixed from known channel parameters, not from the realized future record. Apply the standard coding theorem to repeated uses of the superchannel $`\mathcal N_{p,\epsilon}^{\otimes n}`$:

```math
Q(\mathcal N_{p,\epsilon})\geq\frac{\mathcal I_n}{n}\gt 0.
```

This proves the full-span theorem. The proof does not require a positive limit of $`\mathcal I_n/n`$ as the inner block length itself diverges. It chooses a useful positive finite inner block and then takes the distinct outer coding limit. The constant, selected direction, sufficient inner length and achievable rate may depend on the fixed ensemble, error and measurement probability. The capacity implication uses asymptotic outer coding.

<!-- END canonical-unit P10 -->

## Where this leads

[The eight-use witness](eight-use-witness.md) evaluates one explicit positive block. [The limiting cases](limiting-geometries.md) delimit what the repetition argument establishes.

---

Scientific editing sources: [COMPLETE_PROOF.md](../docs/COMPLETE_PROOF.md). [Section map](../website/furnishing-map.json).
