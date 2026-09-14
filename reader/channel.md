# What reaches the receiver?

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


The channel combines an intact quantum output with a destructive measurement whose noisy classical record remains available. This is the project-specific step after the [selected Preskill background](background.md#after-the-tutorial). His repetition example uses a different channel; its error probability and any symmetry-based input choice must not be imported here.

<a name="channel-operation"></a>

## An intact qubit or a classical record

Two probabilities describe different events. $`p`$ is the probability that a qubit is measured instead of transmitted intact. $`\epsilon`$ is the probability that its classical sign is reported incorrectly **conditional on measurement**. The allowed ensemble has finitely many unit Bloch axes $`\mathbf n_b`$, with known positive weights $`w_b`$ summing to one.

On each independent use, an intact qubit arrives with probability $`1-p`$. Otherwise, axis $`b`$ is selected with probability $`w_b`$, the qubit is measured, and its quantum system becomes inaccessible. If the true outcome bit is $`r`$, the receiver sees $`s=r\oplus z`$, where the independent bit $`z`$ equals one with probability $`\epsilon`$.

The receiver gets the surviving qubits, the correct intact/measured mask, the correct measured-axis labels and the reported signs. The true signs, error bits and discarded quantum systems remain unavailable. An accessible flag identifies an output branch; it does not give access to the environment.

The code may depend on the known axes, weights, $`p`$ and $`\epsilon`$, but is chosen before all realized branch, axis and outcome choices. The same symmetric reporting error applies to every axis and use. Encoding and decoding operations are otherwise unrestricted and noiseless. There is no postselection, feedback, preshared entanglement or rereading of a measured qubit. [Full operation budget](../docs/MODEL_AND_CLAIMS.md#m01)

## The channel in one expression

With $`\eta=1-2\epsilon`$ and $`E_{b,s}=[I+(-1)^s\eta\mathbf n_b\cdot\boldsymbol\sigma]/2`$,

```math
\begin{aligned} \mathcal N_{p,\epsilon}(\rho)&=(1-p)\rho\ \oplus\\ &\quad p\sum_{b,s}w_b\mathrm{Tr}(E_{b,s}\rho)|b,s\rangle\langle b,s|. \end{aligned} 
```

The effects $`E_{b,s}`$ already average over the hidden true sign and the reporting error. For each fixed axis they sum to the identity; the separate weight $`w_b`$ supplies the axis probability. The direct sum keeps the intact and measured branches distinguishable. The measured-only channel is quantum-to-classical and cannot transmit an unknown quantum state. The capacity claim concerns its mixture with intact transmission. This is an instance of the established incomplete-erasure framework. [Physical derivation and attribution](../docs/COMPLETE_PROOF.md#p01)

<a name="reference-state"></a>

## What is being compared?

To test transmission of quantum information, purify the input using a reference $`\mathsf R`$ that stays outside the channel. The receiver register $`\mathsf B`$ includes every surviving qubit and accessible classical record. Coherent information is $`I_c=S(\mathsf B)-S(\mathsf R\mathsf B)`$, with entropies in bits. The joint state with the reference keeps track of correlations that the receiver's state alone cannot describe.

If the input/reference state is pure and the channel is represented by an isometry into receiver and environment registers, the final $`\mathsf R\mathsf B\mathsf E`$ state is pure. Then $`S(\mathsf R\mathsf B)=S(\mathsf E)`$ and the same quantity is $`S(\mathsf B)-S(\mathsf E)`$. The environment in that representation includes everything needed to purify the channel's action. This equality does not make those systems accessible to the decoder. [Preskill notation and sign convention](background.md#notation) · [Project definitions](../docs/MODEL_AND_CLAIMS.md#m02)

The maximum over every single-qubit density matrix is $`Q^{(1)}`$. The quantity $`Q`$ is the unassisted asymptotic quantum capacity, allowing coherent encoding across many independent uses. The statement $`Q^{(1)}=0<Q`$ says that globally optimized single-use coherent information misses an achievable positive asymptotic quantum rate. It does not identify $`Q^{(1)}`$ with an operational one-shot capacity or declare every single-use task useless.

<a name="flagged-information"></a>

## How do the classical records enter the entropy difference?

Write an arbitrary mixed input using its smaller eigenvalue $`0<t\leq1/2`$ and direction $`\mathbf u`$. Its input entropy is $`h_2(t)`$. In the intact branch, the reference and received qubit remain in their pure joint state, so that branch contributes $`h_2(t)`$ to coherent information.

In a measured branch, conditioning on the **reported** axis and sign leaves a conditional state of the reference. The receiver has only that classical record, while the reference generally remains mixed because the true outcome is hidden. Let $`C(t,\mathbf u)`$ be the reference entropy averaged over both reported signs and all axis probabilities. The canonical calculation forms each subnormalized reference state from the noisy effect $`E_{b,s}`$, then weights its normalized entropy by the probability of that report.

For orthogonal classical records, the same Shannon entropy of the record appears in both $`S(\mathsf B)`$ and $`S(\mathsf R\mathsf B)`$ and cancels. Averaging the intact contribution and the negative measured contribution therefore gives

```math
I_c=(1-p)h_2(t)-pC(t,\mathbf u).
```

This is an average over every record, not conditioning on survival. Pure inputs have a trivial reference and coherent information zero. Proving $`Q^{(1)}=0`$ also requires showing that **all mixed inputs** have nonpositive coherent information, which is the first step of the [proof guide](proof-guide.md#two-costs). [Exact conditional states and flagged identity, P01](../docs/COMPLETE_PROOF.md#p01)

<a name="coherent-repetition"></a>

## Does repetition copy an unknown qubit?

Choose an orthonormal pair $`|\mathbf u_+\rangle,|\mathbf u_-\rangle`$ before transmission. The repetition encoder maps the logical basis states to $`|\mathbf u_+\rangle^{\otimes n}`$ and $`|\mathbf u_-\rangle^{\otimes n}`$. By linearity, an unknown logical superposition becomes the same superposition of these two codewords. It does not become $`n`$ independent copies of the unknown input. The two-dimensional logical subspace carries quantum coherence, rather than only a classical bit.

The coherent-information test uses the balanced input marginal

```math
\rho_n(\mathbf u)=\frac12|\mathbf u_+\rangle\langle\mathbf u_+|^{\otimes n} +\frac12|\mathbf u_-\rangle\langle\mathbf u_-|^{\otimes n}.
```

Its purification is the normalized equal superposition of $`|0\rangle_{\mathsf R}|\mathbf u_+\rangle^{\otimes n}`$ and $`|1\rangle_{\mathsf R}|\mathbf u_-\rangle^{\otimes n}`$. Tracing out the reference produces the displayed separable but correlated mixture. That test marginal is distinct from the encoder's coherent action on an unknown logical state. [Code and conditional-state reduction, P09](../docs/COMPLETE_PROOF.md#p09)

<a name="eight-use-witness"></a>

## What does the eight-use example establish?

For equally likely $`X,Y,Z`$ axes, take $`p=7/10`$, $`\epsilon=1/10`$, $`n=8`$ and $`\mathbf u=(1,1,1)/\sqrt3`$. The retained calculation gives approximately $`0.0005981981270524771`$ bits **per block**, or

```math
\frac{\mathcal I_8}{8}>7.47\times10^{-5}\quad\text{bits per physical use}.
```

All nine measured-count branches, from zero through eight measured qubits, are included. The all-measured event has probability $`0.05764801`$ and contributes approximately $`-0.01653160578649`$ bits to the block value. Its loss is included in the positive total. The small positive number is supported by deterministic arithmetic enclosures, not a statistical confidence interval.

At the same parameters, a bound valid for every one-use input gives $`\Gamma=27/59`$ and the exact one-use positivity boundary $`p_1=59/86<7/10`$. Pure inputs attain zero and every mixed input is bounded above by a negative value. Thus the comparison uses a genuinely global single-use zero, alongside one constructive eight-use value. A successful trial input alone could establish only the latter. [Witness, global bound and numerical records, P13](../docs/COMPLETE_PROOF.md#p13)

[Figure 1](figures.md#figure-1) brings the channel and this comparison together. Its witness uses a sharper one-use bound than the conservative universal strip shown in Figure 2; the witness lies below that strip. This is a difference in the sufficient bounds, not an inconsistency between the figures.

Once this positive finite inner block is fixed, the coding theorem applied to many independent uses of that block gives a positive asymptotic rate per physical use. It does not establish a practical decoder, near-perfect recovery from an isolated eight-use block or an optimal inner block length. The [next page](proof-guide.md#finite-before-asymptotic) explains how the theorem guarantees some positive finite block throughout its stated family.

## Why use a common error?

The main proof compares conditional entropies using a coefficient shared by all measurement axes. A common error makes that coefficient common. Independently assigning different errors to different axes is not covered by the headline theorem. [Where the assumption enters](../docs/COMPLETE_PROOF.md#p04)


---

[Previous: Selected background](background.md) · [Continue: The proof route](proof-guide.md)

GitHub reading view generated from [the website source](../website/pages/channel.md). The equations, figure data and canonical captions retain their source meaning. Custom website navigation, local search and interactive color switching are not executed in this GitHub view.
