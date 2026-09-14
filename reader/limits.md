# What the result does not claim

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
- [Visual design](visual-design.md)
- [Project status](status.md)

</details>


The [geometric guarantee](proof-guide.md#geometric-guarantee) is broad in measurement geometry, but its physical model and boundary statements are specific. These controls show how the separation can close and what remains unclassified. They can be read directly from the proof without running software.

<a name="coplanar-control"></a>

## Coplanarity is a construction boundary

If all supported axes lie in a plane, a common perpendicular direction attains repetition loss $`c`$ and approaches single-use cost $`c`$ with nearly pure inputs. The global lower bound matches it, giving $`\Gamma=L=c`$. Full span is therefore necessary and sufficient for the **strict threshold comparison of this long balanced-repetition construction**. Two noncommuting axes can still be coplanar. This statement does not exclude other codes or exceptional finite-block improvements for a coplanar channel. [Exact statement and proof](../docs/COMPLETE_PROOF.md#p11)

<a name="noise-endpoints"></a>

## The two record-noise endpoints are different

At $`\epsilon=0`$, the reported sign is the true sign, so each measured conditional reference state is pure. The flagged identity becomes $`I_c=(1-p)S(\rho)`$. Single-use coherent information is already positive for mixed inputs whenever $`p\lt 1`$; at $`p=1`$ the output is classical and has zero quantum capacity.

At $`\epsilon=1/2`$, the reported sign is input independent. The channel is an erasure channel up to independent flags, with $`Q=Q^{(1)}=\max(0,1-2p)`$. Neither endpoint has a zero-one-use/positive-capacity region. These are direct physical endpoint arguments, separate from interior formulas that divide by $`a`$ or $`c`$. [P11: endpoint arguments](../docs/COMPLETE_PROOF.md#p11)

## A nonzero gap need not be useful in practice

The guaranteed interval can shrink near a plane or near a noise endpoint. The theorem does not provide a fixed minimum rate or block length uniformly across all these channels. Its positive-capacity statement invokes an asymptotic outer code, not an efficient decoder for the retained eight-qubit example. [Quantifier order](../docs/MODEL_AND_CLAIMS.md#m04)

## An exact special case is not an exact capacity formula

<a name="cone-domain"></a>

[Figure 3](figures.md#figure-3) makes the approach to a plane concrete. Three equally weighted axes have azimuths $`0,2\pi/3,4\pi/3`$ and common vertical component $`\sqrt\lambda`$. Over $`0\leq\lambda\leq1/3`$, that parameter is the frame's smallest eigenvalue. The plot fixes $`\epsilon=0.1`$ and uses $`0\leq\lambda\leq1/4`$, where the exact formulas hold for every common interior error:

```math
\Gamma=\frac{c}{1-a\lambda},\qquad L=\frac{c}{\sqrt{1-a\lambda}}.
```

The larger established domain is $`0\leq\lambda\leq\min\{1/3,W(a)/P(a)\}`$, with $`P,W`$ defined in the [scalar lemma](../docs/COMPLETE_PROOF.md#p04). Extending beyond $`1/4`$ requires checking this parameter-specific condition; no such extension is needed to read the figure. The exact gap is between the one-use frontier $`p_1`$ and the construction frontier $`p_{\mathrm{rep}}`$, not an exact all-code capacity threshold.

At fixed interior error, the small-geometry expansion is

```math
p_{\mathrm{rep}}-p_1=\frac{ca}{2(1+c)^2}\lambda+O(\lambda^2)\qquad(\lambda\downarrow0).
```

For the plotted error, the dashed line is $`(18/289)\lambda`$. It is an analytical asymptote, not a fitted curve or an equality across the plot. The zero at coplanarity has the construction-specific meaning above. This cone family differs from the equal-Pauli witness geometry over the plotted range, so the eight-use witness is not transferred to it. [P12: exact family, domain and expansion](../docs/COMPLETE_PROOF.md#p12)

## No silent extension of the noise model

The headline theorem does not cover arbitrary axis-dependent, asymmetric, correlated, or basis-label errors. Surviving qubits arrive intact. The source does not claim external peer review, proof-assistant formalization, exhaustive priority clearance, or a practical fault-tolerant protocol. [Complete claim register](../docs/MODEL_AND_CLAIMS.md#m07)

To trace these statements, the [figure atlas](figures.md) joins unchanged captions to formulas and inputs. The [verification guide](verification.md) distinguishes file-integrity tests, complete certificate checks, finite-witness evaluation and graphical reproduction. Each checks a different part of the evidence; none changes the theorem's scope.


---

[Previous: Complete proof](../docs/COMPLETE_PROOF.md) · [Continue: Verification guide](verification.md)

GitHub reading view generated from [the website source](../website/pages/limits.md). The equations, figure data and canonical captions retain their source meaning. Custom website navigation, local search and interactive color switching are not executed in this GitHub view.
