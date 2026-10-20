# The eight-use witness and numerical controls

[Science](README.md) · [Learning](../learning/README.md) · [References](../references/README.md) · [Verification](../verification/README.md)

This example makes the theorem's coding interpretation concrete. A global bound proves that every one-use input has nonpositive coherent information, while a directed arithmetic enclosure certifies a positive value for one balanced eight-use block.

The calculation includes all measured-count classes and the loss when all qubits are measured. Its per-use value becomes an achievable rate through outer coding; it does not specify recovery fidelity for an isolated block. The accompanying mixed-input and cancellation controls guard against two tempting but invalid shortcuts. [Figure 1](../reader/figures.md#figure-1) presents the same retained numerical inputs.

<!-- BEGIN canonical-unit M05 -->
<a id="m05"></a>
## 5. An eight-use numerical illustration (C5)

Use equally likely $`X,Y,Z`$ axes, common error $`\epsilon=1/10`$, measurement probability $`p=7/10`$, and a balanced eight-use input formed from the eigenstates of $`(X+Y+Z)/\sqrt3`$.

[P13](#p13) establishes $`\Gamma=27/59`$ and therefore the exact one-use positivity boundary $`p_1=59/86`$. Since $`p=7/10\gt p_1`$, the globally optimized one-use value is zero. The 140-digit interval record gives

```math
\begin{aligned} \frac{I_c(\rho_8,\mathcal N^{\otimes8})}{8} &=0.0000747747658815596371016563672617787\ldots\\ &\gt 7.47\times10^{-5}. \end{aligned} 
```

The total block value is approximately $`0.0005981981270524771`$ bits. The all-measured event has probability $`0.05764801`$ and a negative weighted contribution approximately $`-0.01653160578649`$ bits. The [stored certificate](../data/figures/figure1_original_witness140.json) includes all nine measured-count contributions.

This example uses a sharper single-use bound than the most conservative uniform $`3/35`$ theorem. The numerical illustration and the uniform theorem therefore use different one-use bounds. The positive block value has an outer-coding interpretation; it is not an eight-use recovery fidelity or a proof of optimal block length. The exact argument and the evidence contract are in [P13](#p13). **Sources:** [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §7; [W1](../docs/SOURCE_TO_CANONICAL.md#w1)–[W7](../docs/SOURCE_TO_CANONICAL.md#w7).

<!-- END canonical-unit M05 -->

<!-- BEGIN canonical-unit P13 -->
<a id="p13"></a>
## P13. The eight-use witness and two numerical controls

**Sources:** [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §7; [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §§6–8; [W1](../docs/SOURCE_TO_CANONICAL.md#w1)–[W7](../docs/SOURCE_TO_CANONICAL.md#w7); source [C3](../docs/SOURCE_TO_CANONICAL.md#c3)–[C4](../docs/SOURCE_TO_CANONICAL.md#c4). **Claim:** C5; safeguards for C2.

### P13.1 A global single-use zero at the witness parameters

For equal Pauli axes and $`\epsilon=1/10`$,

```math
a=\frac{16}{25},\qquad c=\frac9{25},\qquad G_{\min}=\frac{c}{1-a/3}=\frac{27}{59}.
```

Here $`\ell\gt 27/59`$; equivalently the cone-family equality condition applies since $`a\gt 1/2`$. Therefore $`\Gamma=27/59`$ and

```math
p_1=\frac{59}{86}.
```

At $`p=7/10`$, the mixed-input bound is

```math
\frac{I_c(t,\mathbf u)}{h_2(t)}\leq\frac3{10}-\frac7{10}\frac{27}{59} =-\frac6{295}\lt 0.
```

Together with pure-input value zero, this proves a globally optimized $`Q^{(1)}=0`$. It is not just the value of the maximally mixed state. The witness is justified by this sharper intermediate inequality, not necessarily by membership in the most conservative uniform $`3/35`$ subinterval.

### P13.2 Exact input and all-record formula

Choose $`\mathbf u=(1,1,1)/\sqrt3`$ and $`n=8`$, with the balanced input in P09. Put

```math
\alpha=\frac{1+\eta/\sqrt3}{2},\quad\bar\alpha=1-\alpha,\quad \kappa=\frac{2\eta^2}{3-\eta^2}.
```

The axis-conditioned diagonal probabilities and coherence magnitudes coincide for the three Pauli labels. Summing their probabilities therefore leaves, at each measured count $`m`$, the $`m+1`$ sign-count classes

```math
\begin{aligned} v_j&=\alpha^j\bar\alpha^{m-j},\\ w_j&=\bar\alpha^j\alpha^{m-j},\\ q_j&=(v_j+w_j)/2,\\ x_j&=w_j/(v_j+w_j). \end{aligned} 
```

Their contributions to $`\mathcal A_m`$ and $`\mathcal C_m`$ are

```math
\mathcal A_m=\sum_{j=0}^m{m\choose j}q_j h_2(x_j),
```

```math
\mathcal C_m=\sum_{j=0}^m{m\choose j}q_j\mathcal H(4(1-\kappa^m)x_j(1-x_j)).
```

For $`m=0`$ use $`\mathcal A_0=1,\mathcal C_0=0`$. The exact coherent information is then

```math
\mathcal I_8=\sum_{m=0}^7{8\choose m}(1-p)^{8-m}p^m(\mathcal A_m-\mathcal C_m)-p^8\mathcal C_8.
```

The two-dimensional formula evaluates the full flagged entropy sum, including the all-measured branch, without survivor filtering or postselection.

### P13.3 Numerical witness evidence

**W1**, `witness140.json`, supplies the numerical figure inputs. **W2** is a companion record at a different precision. **W3** is the Decimal evaluator using the separate primitive **V6**. The mpmath effect-determinant evaluator is **W5**, with output **W4**. Small direct hidden-outcome physical checks are **W6–W7**.

The stored enclosure supports

```math
\begin{aligned} \frac{\mathcal I_8}{8} &=0.0000747747658815596371016563672617787\ldots\\ &\gt 7.47\times10^{-5}. \end{aligned} 
```

The total block value is approximately $`0.0005981981270524771`$ bits. The exactly stored all-measured probability is $`p^8=0.05764801`$ and its weighted contribution is approximately $`-0.01653160578649`$ bits. All nine measured-count entries are present in W1.

The full verification command evaluates both witness implementations and compares their outputs with their respective immutable references. The enclosures are arithmetic intervals, not statistical confidence intervals. The rate is achievable with the asymptotic outer-coding interpretation in P10.

<a id="p134"></a>
### P13.4 Numerical controls

At equal Pauli axes with $`\epsilon=1/5`$, the directional nearly pure optimum would be $`G_{\min}=8/11`$. At its implied boundary $`p=11/19`$, the maximally mixed input instead has

```math
I_c=\frac{8-11h_2(1/5)}{19}\gt 0.
```

Source C3 stores a directed enclosure of this control. It demonstrates why $`\Gamma=G_{\min}`$ cannot be assumed at larger error without proof.

C4 gives a cancellation-sensitive numerical control at $`\epsilon=2/5`$, $`p=5083/10000`$, $`n=64`$, whose directed rate bound is negative. Its negative sign tests numerical reliability under severe cancellation.

<!-- END canonical-unit P13 -->

## Where this leads

[The proof and evidence map](proof-map.md) connects this witness, the general theorem and the limiting cases to their exact dependencies and source records.

---

Scientific editing sources: [COMPLETE_PROOF.md](../docs/COMPLETE_PROOF.md) · [MODEL_AND_CLAIMS.md](../docs/MODEL_AND_CLAIMS.md). [Section map](../website/furnishing-map.json).
