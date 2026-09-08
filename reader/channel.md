# What reaches the receiver?

[Overview](README.md) · [Channel](channel.md) · [Proof route](proof-guide.md) · [Figures](figures.md) · [Exact theorem](../docs/MODEL_AND_CLAIMS.md) · [Complete proof](../docs/COMPLETE_PROOF.md) · [Materials](materials.md)

<details>
<summary>All reading routes</summary>

- [The project](README.md)
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
- [Status and publication](status.md)

</details>


Two probabilities describe different events. $p$ is the probability that the qubit is measured rather than transmitted intact. $\epsilon$ is the error probability of the classical sign **conditional on measurement**. Increasing one is not the same as increasing the other.

## An intact qubit or a classical record

The possible measurement axes $\mathbf n_b$ and their probabilities $w_b$ are known when the code is designed. On each independent use, an intact qubit arrives with probability $1-p$. Otherwise, axis $b$ is selected, the qubit is measured, and its quantum system becomes inaccessible. If the true bit is $r$, the receiver sees $s=r\oplus z$, where $z$ is an independent bit with probability $\epsilon$ of being one.

The mask and axis labels are correct. Neither $r$ nor $z$ is delivered separately. The same symmetric reporting error applies to every axis and use. There is no postselection, feedback, preshared entanglement, or encoding chosen after the future measurement outcomes are known. Encoding and decoding operations are otherwise unrestricted and noiseless.

[Full operation budget](../docs/MODEL_AND_CLAIMS.md#m01)

## The channel in one expression

With $\eta=1-2\epsilon$ and $E_{b,s}=[I+(-1)^s\eta\mathbf n_b\cdot\boldsymbol\sigma]/2$,

$$\mathcal N_{p,\epsilon}(\rho)=(1-p)\rho\ \oplus\ p\sum_{b,s}w_b\operatorname{Tr}(E_{b,s}\rho)|b,s\rangle\langle b,s|.$$

The direct sum records which kind of output arrived. The measured branch is quantum-to-classical. The theorem concerns its combination with intact transmission, not quantum communication by a classical record alone. This is an instance of the established incomplete-erasure framework, not a new channel class. [Definition and attribution](../docs/MODEL_AND_CLAIMS.md#m01)

## What is being compared?

For an input purified by a reference $\mathsf R$, coherent information is $I_c=S(\mathsf B)-S(\mathsf R\mathsf B)$. The receiver is $\mathsf B$. Its maximum over every single-qubit density matrix is $Q^{(1)}$. The quantity $Q$ instead allows coherent encoding across many independent uses.

The statement $Q^{(1)}=0<Q$ does not say that the channel is useless for every one-shot task. It says that the globally optimized single-use coherent information misses an achievable positive asymptotic quantum rate. [Definitions and units](../docs/MODEL_AND_CLAIMS.md#m02)

## Why use a common error?

The main proof compares conditional entropies using a coefficient shared by all measurement axes. A common error makes that coefficient common. Independently assigning different errors to different axes is not covered by the headline theorem. [Where the assumption enters](../docs/COMPLETE_PROOF.md#p04)


---

[Continue: The proof route](proof-guide.md)

GitHub reading view generated from [the website source](../website/pages/channel.md). The equations, figure data and canonical captions retain their source meaning. Custom website navigation, local search and interactive color switching are not executed in this GitHub view.
