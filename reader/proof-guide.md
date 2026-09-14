# Three steps from the channel to the theorem

[Overview](README.md) · [Background](background.md) · [Channel](channel.md) · [Proof route](proof-guide.md) · [Figures](figures.md) · [Exact theorem](../docs/MODEL_AND_CLAIMS.md) · [Complete proof](../docs/COMPLETE_PROOF.md) · [Materials](materials.md)

<details>
<summary>All reading routes</summary>

- [The project](README.md)
- [Selected background](background.md)
- [The channel](channel.md)
- [The proof route](proof-guide.md)
- [Figure atlas](figures.md)
- [Scope and limits](limits.md)
- [Exact model and theorem](../docs/MODEL_AND_CLAIMS.md)
- [Complete proof](../docs/COMPLETE_PROOF.md)
- [Verification guide](verification.md)
- [Exact reproduction commands](../docs/REPRODUCTION.md)
- [References and their roles](../docs/REFERENCES.md)
- [Source materials](materials.md)
- [Notation crosswalk](../docs/NOTATION_CROSSWALK.md)
- [Source and proof ledger](../docs/SOURCE_TO_CANONICAL.md)
- [Frozen scientific argument](../docs/FROZEN_ARGUMENT.md)
- [Visual design](visual-design.md)
- [Project status](status.md)

</details>


The [channel and eight-use example](channel.md#eight-use-witness) show what a separation means. The theorem must do more: for every allowed finite full-span ensemble and every common $`0\lt \epsilon\lt 1/2`$, it must supply a nonempty interval of measurement probabilities with $`Q^{(1)}=0\lt Q`$. The proof joins three ingredients: **an obstruction for every single-use input**, **a sufficient finite-block construction**, and **a geometric inequality separating their costs**.

The exact [theorem](../docs/MODEL_AND_CLAIMS.md#m04), [complete proof](../docs/COMPLETE_PROOF.md#p01) and [verification guide](verification.md) are available directly. The explanation here is specific to this project; the [selected tutorial](background.md#reading-map) supplies the information-theoretic background.

<a name="two-costs"></a>

## 1. Bound every single-use input

Write a qubit input using its smaller eigenvalue $`0\lt t\leq1/2`$ and a Bloch direction $`\mathbf u`$. Let $`C(t,\mathbf u)`$ be the measured branch's average reference entropy conditional on the **reported** record. The flagged channel has

```math
I_c=(1-p)h_2(t)-pC(t,\mathbf u).
```

The measured branch subtracts entropy from the intact-branch contribution. To rule out positive coherent information for **every** one-use input, the proof needs a lower bound on that penalty relative to the input entropy, uniformly in both $`t`$ and $`\mathbf u`$. The smallest possible ratio is $`\Gamma=\inf_{t,\mathbf u}C(t,\mathbf u)/h_2(t)`$. Pure inputs have exactly zero coherent information, so the optimized one-use quantity is zero precisely when

```math
p\geq p_1:=\frac{1}{1+\Gamma}.
```

This optimization includes every mixed input and arbitrarily nearly pure states. Substituting a symmetry-motivated direction, a maximally mixed input or a nearly pure limit would not establish the obstruction. The identity for $`p_1`$ is exact, even when the proof supplies only a lower bound for $`\Gamma`$. [P01: exact channel accounting](../docs/COMPLETE_PROOF.md#p01)

<a name="finite-before-asymptotic"></a>

## 2. Construct a positive finite block

The second cost asks a different question: when does one fixed repetition direction eventually yield a positive finite block? Use the [coherent logical subspace and balanced test input](channel.md#coherent-repetition), and retain every outcome. If $`\mathcal A_m`$ is the record-averaged codeword uncertainty and $`\mathcal R_m`$ is the entropy contribution while a quantum output survives, then

```math
I_n=\sum_{m=0}^{n}{n\choose m}(1-p)^{n-m}p^m\mathcal R_m-p^n\mathcal A_n.
```

At $`m=n`$, the terms combine into the negative conditional-reference entropy of the all-measured branch. The final subtraction is essential. Record-overlap bounds control both the surviving-quantum contribution and this loss. For any fixed finite number of axes, their exponential rates determine the eventual sign because the accompanying factors grow or decay only polynomially in the block length. This is an all-record bound, not a decoder that selects favorable outcomes.

The resulting sufficient condition is $`p\lt 1/(1+L)`$. Here $`L`$ is the smallest directional loss available to this repetition construction:

```math
L=\min_{\|\mathbf u\|=1}\sum_b\frac{w_b c}{\sqrt{1-a(\mathbf n_b\cdot\mathbf u)^2}},\qquad a=(1-2\epsilon)^2,\quad c=1-a.
```

Thus $`\Gamma`$ controls the best possible **single-use input**, while $`L`$ controls this **specified block construction**. They optimize different quantities and need not have the same minimizing direction. The repetition frontier $`p_{\mathrm{rep}}=1/(1+L)`$ concerns the strict eventual sign. The equality case and exceptional shorter blocks above it are not classified by these bounds, and it is not an exact capacity boundary.

Fix the channel parameters and a suitable $`p`$, choose a direction from those known parameters, and then choose a finite $`n`$ with positive $`I_n`$. Only after fixing that inner block does the asymptotic coding theorem apply to repeated uses of the block channel, giving $`Q\geq I_n/n\gt 0`$. There is no requirement that $`I_n/n`$ have a positive limit as the inner length grows. The inner-block selection and outer-coding limit are separate steps. [P09: all-record bounds and polynomial factors](../docs/COMPLETE_PROOF.md#p09) · [P10: operational conclusion](../docs/COMPLETE_PROOF.md#p10) · [Tutorial achievability statement](background.md#reading-map)

<a name="geometric-guarantee"></a>

## 3. Separate the two costs geometrically

The measurement frame $`T=\sum_b w_b\mathbf n_b\mathbf n_b^{\mathsf T}`$ records how strongly the ensemble covers each Bloch direction. Its smallest eigenvalue $`\lambda=\lambda_{\min}(T)`$ is positive exactly when the supported axes span all three directions. A coplanar ensemble has a common perpendicular direction; full span removes it. That observation explains why geometry is relevant, but does not itself prove that the two entropy costs separate.

The quantitative step combines the global entropy comparison with directional minimization and a spherical-average bound. It proves

```math
\Gamma\geq L+\frac{3}{35}ca\lambda.
```

For full span, $`\lambda\gt 0`$; for every interior error, $`ca\gt 0`$. Thus the two regions overlap:

```math
\frac{1}{1+L+(3ca/35)\lambda}\leq p\lt \frac{1}{1+L}.
```

The lower equality is included and the upper equality excluded. This is a guaranteed subinterval, not the exact quantum-capacity boundary. Its width is a range of measurement probabilities, not a communication rate. [P08: geometric gap](../docs/COMPLETE_PROOF.md#p08) · [P10: composition into the theorem](../docs/COMPLETE_PROOF.md#p10)

[Figure 2](figures.md#figure-2) shows this sufficient strip for one explicit slice: equally weighted Pauli axes, for which $`T=I/3`$. It is not a phase diagram for arbitrary ensembles. Outside the strip the plotted theorem makes no classification. Figure 1's point at $`p=0.7`$, $`\epsilon=0.1`$ uses the sharper bound in [P13](../docs/COMPLETE_PROOF.md#p13) and lies below the conservative strip shown here.

<a name="scalar-proof"></a>

## Where the computer-assisted proof enters

The textbook framework does not establish the new global entropy inequality. The project compares each axis's conditional entropy using an endpoint chord. Its coefficient depends on the input weight and reporting error; the **common error** makes that coefficient identical for all axes, allowing the weighted comparison before global minimization. This is the step that prevents silently extending the result to arbitrary heterogeneous errors.

The scalar comparison uses $`\ell=c(1+a/4+a^2/4+a^3/10)`$. Analytical arguments cover the low- and high-noise regions and every nearly pure input tail. A complete rational covering handles the remaining compact noise/input domain. The three numerical verifiers check that covering with separate implementations and outward bounds; a grid of sampled inputs or an ordinary unit-test suite would not replace those obligations. These are deterministic mathematical enclosures, not statistical confidence statements.

[The exact inequality and analytical endpoints](../docs/COMPLETE_PROOF.md#p04) · [P07: complete covering](../docs/COMPLETE_PROOF.md#p07) · [Verification instructions](verification.md)

<a name="contribution"></a>

## What is added to the familiar superadditivity story?

Incomplete-erasure channels, repetition coding and coherent-information superadditivity are established ingredients. Preskill's selected example already illustrates a qualitative threshold improvement using repetition and outer coding for a different channel. The project's proposed contribution is the geometric sufficient condition across every permitted finite full-span ensemble and the entire common interior-error range, with the stated controlled limits. It is more than the isolated eight-use numerical illustration.

The precise attribution remains a bounded comparison with the cited primary research, not an absolute priority certificate. Those citations identify inherited frameworks and techniques; they do not create a second tutorial requirement. [Canonical claim and nonclaims](../docs/MODEL_AND_CLAIMS.md#m07) · [Primary references and their roles](../docs/REFERENCES.md) · [Controlled limits](limits.md#coplanar-control)


---

[Previous: The channel](channel.md) · [Continue: Exact model and theorem](../docs/MODEL_AND_CLAIMS.md)

GitHub reading view generated from [the website source](../website/pages/proof-guide.md). The equations, figure data and canonical captions retain their source meaning. Custom website navigation, local search and interactive color switching are not executed in this GitHub view.
