# Three steps from the channel to the theorem

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


The proof compares **a cost applying to every single-use input** with **a cost attained by a specified collective construction**. A geometric inequality separates the two. The complete derivations are available directly; the guide below does not replace them.

## 1. Bound every single-use input

Write a qubit input using its smaller eigenvalue $0<t\leq1/2$ and a Bloch direction $\mathbf u$. Let $C(t,\mathbf u)$ be the measured branch's average reference entropy conditional on the **reported** record. The flagged channel has

$$I_c=(1-p)h_2(t)-pC(t,\mathbf u).$$

Define $\Gamma=\inf_{t,\mathbf u}C(t,\mathbf u)/h_2(t)$. Pure inputs have exactly zero coherent information, so the optimized one-use quantity is zero precisely when

$$p\geq p_1:=\frac{1}{1+\Gamma}.$$

This optimization includes every mixed input and arbitrarily nearly pure states. Substituting one convenient trial input would not establish the obstruction. [P01: exact channel accounting](../docs/COMPLETE_PROOF.md#p01)

## 2. Construct a positive finite block

Choose antipodal single-qubit codewords and form a balanced mixture of their $n$-fold repetitions. The reduced calculation retains every outcome. If $\mathcal A_m$ is the record-averaged codeword uncertainty and $\mathcal R_m$ is the entropy contribution while a quantum output survives, then

$$I_n=\sum_{m=0}^{n}{n\choose m}(1-p)^{n-m}p^m\mathcal R_m-p^n\mathcal A_n.$$

The final term is essential: with all qubits measured, the total contribution is the negative conditional reference entropy. It is not discarded as a failed block. Bounds on the two terms give positive coherent information for a sufficiently large finite block whenever $p<1/(1+L)$, where

$$L=\min_{\|\mathbf u\|=1}\sum_b\frac{w_b c}{\sqrt{1-a(\mathbf n_b\cdot\mathbf u)^2}},\qquad a=(1-2\epsilon)^2,\quad c=1-a.$$

The direction depends on the known channel, not future realized outcomes. Choose a positive finite block first, then apply the quantum coding theorem to its repeated use. No positive limit of $I_n/n$ as the inner block grows is asserted. [P09: all-record construction](../docs/COMPLETE_PROOF.md#p09) · [P10: operational conclusion](../docs/COMPLETE_PROOF.md#p10)

## 3. Separate the two costs geometrically

Let $T=\sum_b w_b\mathbf n_b\mathbf n_b^{\mathsf T}$ and $\lambda=\lambda_{\min}(T)$. The global entropy comparison proves

$$\Gamma\geq L+\frac{3}{35}ca\lambda.$$

For full span, $\lambda>0$; for every interior error, $ca>0$. Thus the two regions overlap:

$$\frac{1}{1+L+(3ca/35)\lambda}\leq p<\frac{1}{1+L}.$$

The lower equality is included and the upper equality excluded. This is a guaranteed subinterval, not the exact quantum-capacity boundary. [P08: geometric gap](../docs/COMPLETE_PROOF.md#p08)

## Where the computer-assisted proof enters

The scalar comparison uses $\ell=c(1+a/4+a^2/4+a^3/10)$. Analytical arguments control the open noise endpoints and every nearly pure input tail. A complete rational covering handles the remaining compact noise/input domain. The three numerical verifiers check that covering with separate implementations; passing an ordinary unit-test suite is not a substitute for running them.

[The exact inequality and analytical endpoints](../docs/COMPLETE_PROOF.md#p04) · [P07: complete covering](../docs/COMPLETE_PROOF.md#p07) · [Verification instructions](verification.md)


---

[Continue: Figure atlas](figures.md)

GitHub reading view generated from [the website source](../website/pages/proof-guide.md). The equations, figure data and canonical captions retain their source meaning. Custom website navigation, local search and interactive color switching are not executed in this GitHub view.
