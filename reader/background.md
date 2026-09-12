# From Preskill to this channel

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


The [project result](README.md) is a geometric guarantee for a specific noisy-record channel. If you already know coherent information and its coding interpretation, go directly to [our channel](channel.md), the [exact theorem](../docs/MODEL_AND_CLAIMS.md#m04), [complete proof](../docs/COMPLETE_PROOF.md) or [figures](figures.md).

The one selected background tutorial is John Preskill's *Quantum Shannon Theory*, Chapter 10 of *Quantum Information*, **[arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5)** ([official PDF](https://arxiv.org/pdf/1604.07450v5)). Use the named passages below as questions arise. Reading the whole chapter or completing another chapter is not a prerequisite.

<a name="reading-map"></a>

## Which passages answer the main questions?

Start with Sections 10.7.1–10.7.2, printed pp. 51–56, then 10.7.4, printed pp. 58–60. Complete the operational picture by reading the **unassisted-achievability statement** in 10.9.4, printed pp. 75–76. The last assignment is its statement and meaning, not its full proof. Each return link below names where this repository uses the concept.

| Passage in v5 | Question and concept to retain | Used here |
|---|---|---|
| [§10.7.1; printed pp. 51–53](https://arxiv.org/pdf/1604.07450v5#page=57). Eq. (10.273), p. 52; Eq. (10.275), p. 53; Eq. (10.278), p. 53 | What is optimized, and what is a capacity? Input optimization differs from asymptotic regularization. | [Channel: reference-state quantities](channel.md#reference-state); [M02](../docs/MODEL_AND_CLAIMS.md#m02), [P01](../docs/COMPLETE_PROOF.md#p01) |
| [§10.7.2; printed pp. 53–56](https://arxiv.org/pdf/1604.07450v5#page=59). Eq. (10.281), p. 54; Eq. (10.282), p. 54; Eq. (10.289), p. 55; Eq. (10.297), p. 56 | Why do reference correlations matter for recovery? Decoupling connects the environment to recoverability. | [Channel: finite-block meaning](channel.md#eight-use-witness); [M02](../docs/MODEL_AND_CLAIMS.md#m02), [P10](../docs/COMPLETE_PROOF.md#p10) |
| [§10.7.4; printed pp. 58–60](https://arxiv.org/pdf/1604.07450v5#page=64). Eq. (10.310), p. 58; Eq. (10.316), p. 60 | How can a repetition inner code help? A coherent code subspace can be combined with an outer code. | [Channel: coherent repetition](channel.md#coherent-repetition); [P09](../docs/COMPLETE_PROOF.md#p09), [P13](../docs/COMPLETE_PROOF.md#p13) |
| [§10.9.4; printed pp. 75–76](https://arxiv.org/pdf/1604.07450v5#page=81). Eq. (10.366), p. 75; Eq. (10.367), p. 75; Eq. (10.368), p. 76 | Operational statement. Why does a positive block value give an unassisted rate? Read the unassisted-achievability statement; its full derivation is optional. | [Proof route: fixed inner block, then outer coding](proof-guide.md#finite-before-asymptotic); [P10](../docs/COMPLETE_PROOF.md#p10), [REFERENCES.md](../docs/REFERENCES.md) |

Page numbers are **printed pages**. In this v5 PDF, printed page $k$ is viewer page $k+6$ (zero-based PDF index $k+5$). The PDF links in the map use viewer numbers. The arXiv version is dated 8 July 2025; the title page says updated June 2025.

<a name="notation"></a>

## Which symbols change on the way here?

| Preskill | This project | Meaning |
|---|---|---|
| $H$ | $S$, with $h_2$ for binary entropy | Information entropies are in bits; the project reserves $\ln$ for natural logarithms in estimates. |
| $Q_1(\mathcal N)$, Eq. (10.273) | $Q^{(1)}(\mathcal N)$ | The maximum of coherent information over all one-use input states. Preskill calls it “one-shot”; here it is not an operational finite-error one-shot capacity. |
| Input $A$, reference $R$ | Input qubit (state $\rho$), reference $\mathsf R$ | The reference purifies the chosen input and is not sent through the channel. |
| Receiver $B$, environment $E$ | Receiver $\mathsf B$; environment of a dilation | With a pure $RBE$ dilation, $H(RB)=H(E)$. A classical output flag does not give access to the environment. |
| $p$ in Eq. (10.310) | $p$ and $\epsilon$ in M01 | Preskill uses total Pauli-error probability, $p/3$ per error. Here $p$ selects destructive measurement and $\epsilon$ flips its report. These are different channels. |
| $\epsilon,\delta$ in the capacity definition, p. 52 | Physical reporting error $\epsilon$ | The tutorial symbols are accuracy/rate tolerances, not this fixed noise parameter. |

The repository's [canonical notation crosswalk](../docs/NOTATION_CROSSWALK.md) connects the symbols used across the project's source materials. The tutorial crosswalk above explains how Preskill's notation relates to those symbols without renaming the canonical mathematics.

<a name="after-the-tutorial"></a>

## What changes after the tutorial's example?

Preskill's Section 10.7.4 already explains a qualitative threshold improvement using repetition followed by outer coding. Its depolarizing channel applies Pauli errors. **Our channel instead either transmits the qubit intact or destroys it in a measurement and returns an imperfect classical record.** The transferable ideas are the code subspace, its reference-state test, and the distinction between a finite-block quantity and an asymptotic rate. The probabilities and the source example's symmetry argument do not transfer.

The repository supplies the remaining steps. [The channel page](channel.md#channel-operation) specifies everything the receiver can access, derives the reported-record entropy average, and explains the [eight-use witness](channel.md#eight-use-witness). [The proof guide](proof-guide.md#geometric-guarantee) then compares a bound valid for every one-use input with a sufficient block construction. Its full-span gap and computer-assisted scalar inequality are **project-specific mathematics**, not consequences supplied by Preskill's example. The [limits page](limits.md) fixes where the geometric picture applies.

Incomplete-erasure channels, repetition and superadditivity are established ideas. The project's working contribution is its sufficient geometric condition over the stated finite-axis, common-error family. [Primary research attribution](../docs/REFERENCES.md) remains available for that distinction; those papers are not another required tutorial. No absolute-priority claim is added here.

<a name="edition-note"></a>

## One v5 sign note

In the rendered PDF, [Eq. (10.368), printed p. 76](https://arxiv.org/pdf/1604.07450v5#page=82), reverses the entropy difference. Read its rate as $H(B)-H(E)-o(1)$, consistent with [definition (10.275), p. 53](https://arxiv.org/pdf/1604.07450v5#page=59). The exponent in [bound (10.367), p. 75](https://arxiv.org/pdf/1604.07450v5#page=81), has the opposite order, so decay requires a rate below $H(B)-H(E)$. This note follows visual inspection of the actual v5 pages; it does not change the source.

<a name="optional-refreshers"></a>

## What if one background concept is unfamiliar?

These are optional refreshers within the **same source**, not a second prerequisite route. Read only the subsection addressing the question you have.

| Passage in v5 | Question and concept to retain | Used here |
|---|---|---|
| [§10.1; printed pp. 1–13](https://arxiv.org/pdf/1604.07450v5#page=7). Eq. (10.5), p. 2; Eq. (10.7), p. 3 | What do binary entropy and rate mean? Entropy and rate notation. | [Channel: flagged entropy average](channel.md#flagged-information); [M02](../docs/MODEL_AND_CLAIMS.md#m02) |
| [§10.2.1; printed pp. 15–16](https://arxiv.org/pdf/1604.07450v5#page=21). Eq. (10.68), p. 15; Eq. (10.73), p. 16 | Why can quantum conditional entropy be negative? Pure bipartitions have equal marginal entropies. | [Channel: reference and environment](channel.md#reference-state); [P01](../docs/COMPLETE_PROOF.md#p01) |
| [§10.2.2; printed pp. 16–17](https://arxiv.org/pdf/1604.07450v5#page=22). Eq. (10.74), p. 17 | How does a measurement enter an entropy calculation? Distinguish a measured record from an unobserved mixture. | [Channel: accessible records](channel.md#channel-operation); [P01](../docs/COMPLETE_PROOF.md#p01) |
| [§10.2.3; printed pp. 17–19](https://arxiv.org/pdf/1604.07450v5#page=23). Eq. (10.80), p. 18; Eq. (10.84), p. 18; Eq. (10.85), p. 19 | Which entropy inequality supports data processing? Strong subadditivity. | [Proof route: two costs](proof-guide.md#two-costs); [P02](../docs/COMPLETE_PROOF.md#p02) |
| [§10.2.4; printed pp. 19](https://arxiv.org/pdf/1604.07450v5#page=25). Eq. (10.89), p. 19; Eq. (10.91), p. 19 | Can processing the output restore lost correlations by itself? Data processing. | [Channel: what the witness establishes](channel.md#eight-use-witness); [P10](../docs/COMPLETE_PROOF.md#p10) |
| [§10.6.6; printed pp. 50–51](https://arxiv.org/pdf/1604.07450v5#page=56). Eq. (10.269), p. 51 | Why is a measured-only output insufficient? Entanglement breaking. | [Channel: destructive branch](channel.md#channel-operation); [M01](../docs/MODEL_AND_CLAIMS.md#m01) |
| [§10.7.3; printed pp. 56–58](https://arxiv.org/pdf/1604.07450v5#page=62). Eq. (10.298), p. 56; Eq. (10.303), p. 57; Eq. (10.309), p. 58 | When can a single-use expression give the capacity? Degradability and antidegradability describe special cases. | [Limits: reporting-noise endpoints](limits.md#noise-endpoints); [P11](../docs/COMPLETE_PROOF.md#p11) |

For optional proof depth, the derivation in 10.9.4 uses the earlier decoupling machinery, including Eq. (10.341), printed p. 69, and typical-subspace arguments. Following those internal dependencies is different from reading the achievability statement used here. You can proceed to the project without following that derivation.

The source's front-matter notice limits redistribution. This repository links to the pinned official edition and supplies original explanations; it includes no textbook PDF, page images or copied figures. The tutorial is not fetched during a build, test, numerical run or page render. The [learning metadata](../website/learning_bridge.json) records the checked locations separately from the scientific proof ledger.


---

[Previous: The project](README.md) · [Continue: The channel](channel.md)

GitHub reading view generated from [the website source](../website/pages/background.md). The equations, figure data and canonical captions retain their source meaning. Custom website navigation, local search and interactive color switching are not executed in this GitHub view.
