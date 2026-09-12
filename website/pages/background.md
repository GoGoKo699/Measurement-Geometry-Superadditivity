# From Preskill to this channel

The [project result](index.md) is a geometric guarantee for a specific noisy-record channel. If you already know coherent information and its coding interpretation, go directly to [our channel](channel.md), the [exact theorem](../../docs/MODEL_AND_CLAIMS.md#m04), [complete proof](../../docs/COMPLETE_PROOF.md) or [figures](figures.md).

The one selected background tutorial is John Preskill's *Quantum Shannon Theory*, Chapter 10 of *Quantum Information*, **[arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5)** ([official PDF](https://arxiv.org/pdf/1604.07450v5)). Use the named passages below as questions arise. Reading the whole chapter or completing another chapter is not a prerequisite.

<a id="reading-map"></a>

## Which passages answer the main questions?

Start with Sections 10.7.1–10.7.2, printed pp. 51–56, then 10.7.4, printed pp. 58–60. Complete the operational picture by reading the **unassisted-achievability statement** in 10.9.4, printed pp. 75–76. The last assignment is its statement and meaning, not its full proof. Each return link below names where this repository uses the concept.

<!-- SITE:BACKGROUND_CORE -->

Page numbers are **printed pages**. In this v5 PDF, printed page $k$ is viewer page $k+6$ (zero-based PDF index $k+5$). The PDF links in the map use viewer numbers. The arXiv version is dated 8 July 2025; the title page says updated June 2025.

<a id="notation"></a>

## Which symbols change on the way here?

<!-- SITE:BACKGROUND_NOTATION -->

The repository's [canonical notation crosswalk](../../docs/NOTATION_CROSSWALK.md) serves a different purpose: it reconciles the project's historical source fragments. It remains unchanged. The tutorial crosswalk above does not rename canonical mathematical symbols.

<a id="after-the-tutorial"></a>

## What changes after the tutorial's example?

Preskill's Section 10.7.4 already explains a qualitative threshold improvement using repetition followed by outer coding. Its depolarizing channel applies Pauli errors. **Our channel instead either transmits the qubit intact or destroys it in a measurement and returns an imperfect classical record.** The transferable ideas are the code subspace, its reference-state test, and the distinction between a finite-block quantity and an asymptotic rate. The probabilities and the source example's symmetry argument do not transfer.

The repository supplies the remaining steps. [The channel page](channel.md#channel-operation) specifies everything the receiver can access, derives the reported-record entropy average, and explains the [eight-use witness](channel.md#eight-use-witness). [The proof guide](proof-guide.md#geometric-guarantee) then compares a bound valid for every one-use input with a sufficient block construction. Its full-span gap and computer-assisted scalar inequality are **project-specific mathematics**, not consequences supplied by Preskill's example. The [limits page](limits.md) fixes where the geometric picture applies.

Incomplete-erasure channels, repetition and superadditivity are established ideas. The project's working contribution is its sufficient geometric condition over the stated finite-axis, common-error family. [Primary research attribution](../../docs/REFERENCES.md) remains available for that distinction; those papers are not another required tutorial. No absolute-priority claim is added here.

<a id="edition-note"></a>

## One v5 sign note

In the rendered PDF, [Eq. (10.368), printed p. 76](https://arxiv.org/pdf/1604.07450v5#page=82), reverses the entropy difference. Read its rate as $H(B)-H(E)-o(1)$, consistent with [definition (10.275), p. 53](https://arxiv.org/pdf/1604.07450v5#page=59). The exponent in [bound (10.367), p. 75](https://arxiv.org/pdf/1604.07450v5#page=81), has the opposite order, so decay requires a rate below $H(B)-H(E)$. This note follows visual inspection of the actual v5 pages; it does not change the source.

<a id="optional-refreshers"></a>

## What if one background concept is unfamiliar?

These are optional refreshers within the **same source**, not a second prerequisite route. Read only the subsection addressing the question you have.

<!-- SITE:BACKGROUND_OPTIONAL -->

For optional proof depth, the derivation in 10.9.4 uses the earlier decoupling machinery, including Eq. (10.341), printed p. 69, and typical-subspace arguments. Following those internal dependencies is different from reading the achievability statement used here. You can proceed to the project without following that derivation.

The source's front-matter notice limits redistribution. This repository links to the pinned official edition and supplies original explanations; it includes no textbook PDF, page images or copied figures. The tutorial is not fetched during a build, test, numerical run or page render. The [learning metadata](../learning_bridge.json) records the checked locations separately from the scientific proof ledger.
