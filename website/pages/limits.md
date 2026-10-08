# Theorem scope and controlled limits

The [geometric guarantee](proof-guide.md#geometric-guarantee) applies to finite ensembles of unit Bloch measurement axes with positive weights, common symmetric reporting noise, independent channel uses, intact surviving qubits, and correct branch and axis flags. Within this model, the theorem supplies a sufficient interval of measurement probabilities. The controls below show how its geometric separation closes at coplanarity and at the noise endpoints. They can be read directly from the proof without running software.

<a id="coplanar-control"></a>

## Coplanarity is a construction boundary

If all supported axes lie in a plane, a common perpendicular direction attains repetition loss $`c`$ and approaches single-use cost $`c`$ with nearly pure inputs. The global lower bound matches it, giving $`\Gamma=L=c`$. Full span is therefore necessary and sufficient for the **strict threshold comparison of this long balanced-repetition construction**. Two noncommuting axes can still be coplanar. This statement does not exclude other codes or exceptional finite-block improvements for a coplanar channel. [Exact statement and proof](../../docs/COMPLETE_PROOF.md#p11)

<a id="noise-endpoints"></a>

## The two record-noise endpoints are different

At $`\epsilon=0`$, the reported sign is the true sign, so each measured conditional reference state is pure. The flagged identity becomes $`I_c=(1-p)S(\rho)`$. Single-use coherent information is already positive for mixed inputs whenever $`p\lt 1`$; at $`p=1`$ the output is classical and has zero quantum capacity.

At $`\epsilon=1/2`$, the reported sign is input independent. The channel is an erasure channel up to independent flags, with $`Q=Q^{(1)}=\max(0,1-2p)`$. Neither endpoint has a zero-one-use/positive-capacity region. These are direct physical endpoint arguments, separate from interior formulas that divide by $`a`$ or $`c`$. [P11: endpoint arguments](../../docs/COMPLETE_PROOF.md#p11)

## Rates and block lengths depend on the channel

The guaranteed interval can shrink near a plane or near a noise endpoint. For each fixed channel in the interval, the proof chooses a finite block with positive coherent information; outer coding then gives a positive asymptotic rate. The guaranteed block length and rate depend on the chosen channel. [Quantifier order](../../docs/MODEL_AND_CLAIMS.md#m04)

## Exact thresholds for a cone family

<a id="cone-domain"></a>

[Figure 3](figures.md#figure-3) makes the approach to a plane concrete. Three equally weighted axes have azimuths $`0,2\pi/3,4\pi/3`$ and common vertical component $`\sqrt\lambda`$. Over $`0\leq\lambda\leq1/3`$, that parameter is the frame's smallest eigenvalue. The plot fixes $`\epsilon=0.1`$ and uses $`0\leq\lambda\leq1/4`$, where the exact formulas hold for every common interior error:

```math
\Gamma=\frac{c}{1-a\lambda},\qquad L=\frac{c}{\sqrt{1-a\lambda}}.
```

The larger established domain is $`0\leq\lambda\leq\min\{1/3,W(a)/P(a)\}`$, with $`P,W`$ defined in the [scalar lemma](../../docs/COMPLETE_PROOF.md#p04). Values beyond $`1/4`$ require this parameter-specific condition. The exact gap is between the one-use frontier $`p_1`$ and the construction frontier $`p_{\mathrm{rep}}`$, not an exact all-code capacity threshold.

At fixed interior error, the small-geometry expansion is

```math
p_{\mathrm{rep}}-p_1=\frac{ca}{2(1+c)^2}\lambda+O(\lambda^2)\qquad(\lambda\downarrow0).
```

For the plotted error, the dashed line is $`(18/289)\lambda`$. It is an analytical asymptote, not a fitted curve or an equality across the plot. The zero at coplanarity has the construction-specific meaning above. This cone family differs from the equal-Pauli witness geometry over the plotted range, so the eight-use witness is not transferred to it. [P12: exact family, domain and expansion](../../docs/COMPLETE_PROOF.md#p12)

## Trace the assumptions and evidence

The [channel model](../../docs/MODEL_AND_CLAIMS.md#m01) fixes the shared noise assumptions; the [threshold definitions](../../docs/MODEL_AND_CLAIMS.md#m03) distinguish the single-use threshold, the repetition-construction threshold and quantum capacity.

To trace these statements, the [figure atlas](figures.md) joins captions to formulas and inputs. The [verification guide](verification.md) distinguishes file-integrity tests, complete certificate checks, finite-witness evaluation and graphical reproduction. Each checks a different part of the evidence; none changes the theorem's scope.
