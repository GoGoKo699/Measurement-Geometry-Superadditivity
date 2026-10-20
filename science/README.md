# How measurement geometry creates a collective-coding advantage

A lost qubit can leave an imperfect classical measurement record. This project asks whether the geometry of the possible measurements can guarantee quantum transmission beyond coherent information optimized over every one-use input.

The answer is affirmative for every allowed finite ensemble spanning the three Bloch directions, throughout the common symmetric reporting-error range $`0\lt\epsilon\lt1/2`$. The proof compares the entropy cost faced by an arbitrary single-qubit input with the loss of a fixed balanced repetition code. A quantitative geometric inequality separates those costs. A finite positive block then gives a positive asymptotic unassisted rate through outer coding.

[Physical picture](physical-picture.md) · [Exact theorem](geometric-gap.md#m04) · [30-milestone learning route](../learning/README.md) · [Figures](../reader/figures.md) · [Verification](../verification/README.md)

<a id="results-and-model"></a>
## Results and their scope

| Result | What it establishes | Exact argument |
|---|---|---|
| Global one-use boundary | $`p_1=1/(1+\Gamma)`$ is the exact boundary at or above which optimized one-use coherent information is zero. The infimum defining $`\Gamma`$ covers every mixed qubit input. | [Model M03 and P01](single-use.md) |
| Full-span guarantee | Every allowed full-span ensemble and every common interior reporting error has a nonempty measurement-probability interval with $`Q^{(1)}=0\lt Q`$. | [Theorem and geometric bound](geometric-gap.md), [finite block and outer coding](repetition-coding.md#p10) |
| Universal linear closure | $`p_{\mathrm{rep}}-p_1=\Theta_\epsilon(\lambda)`$ as the smallest frame eigenvalue tends to zero, uniformly over the allowed finite ensembles at a fixed interior error. | [P08 corollary](geometric-gap.md#p08-linear-closure) |
| Finite illustration | Equal Pauli axes at $`p=0.70`$, $`\epsilon=0.10`$ have global one-use zero and a certified eight-use value above $`7.47\times10^{-5}`$ bits per physical use. | [M05 and P13](eight-use-witness.md) |
| Controlled boundaries | Coplanarity closes the strict long-balanced-repetition comparison; noise endpoints and an exact cone family specify the limits of the guarantee. | [M06 and P11–P12](limiting-geometries.md) |

Here $`Q^{(1)}`$ is optimized one-use coherent information and $`Q`$ is unassisted asymptotic quantum capacity. The repetition quantity $`p_{\mathrm{rep}}`$ is a strict eventual-sign frontier for the specified construction. It is not an exact all-code capacity boundary. [The model and notation](model.md) define the accessible resources and all symbols.

## Read the connected argument

For a conceptual introduction, begin with [the physical picture](physical-picture.md) and [the proof strategy](proof-strategy.md). For background, [the selected Preskill bridge](../learning/preskill-bridge.md) returns to the exact place each concept is used. Specialists can enter directly at the theorem, its global one-use obstruction, or the all-record construction.

| Topic | Scientific question | Retained units |
|---|---|---|
| [Channel and quantities](model.md) | What survives a use, what is hidden, and what is optimized? | Model M01–M02 |
| [Exact one-use criterion](single-use.md) | When is coherent information nonpositive for every input? | Model M03; P01 |
| [Entropy tools](entropy-tools.md) | Which curvature and entropy facts make a global comparison possible? | P02–P03 |
| [Scalar inequality and certificate](scalar-inequality.md) | How is the full error and input domain covered? | P04–P07 |
| [Geometric gap and linear closure](geometric-gap.md) | Why does full span separate the costs, and how does the gap close? | Model M04; P08 |
| [Repetition coding](repetition-coding.md) | How do all records produce a finite positive block and a rate? | P09–P10 |
| [Limiting geometries](limiting-geometries.md) | What happens at coplanarity, at noise endpoints, and in the cone family? | Model M06; P11–P12 |
| [Eight-use witness](eight-use-witness.md) | How is one concrete separation certified? | Model M05; P13 |
| [Claim and evidence map](proof-map.md) | Which ingredients support each claim, and what is imported? | Model M07–M08; P14–P15 |
| [Notation crosswalk](notation.md) | How do source and implementation symbols translate? | Complete source/code crosswalk |

<a id="proof-route"></a>
## Proof route

Start with [P01](single-use.md#p01) for the physical channel and global minimization. [P02–P03](entropy-tools.md) derive the entropy tools and common-error chord. [P04–P07](scalar-inequality.md) prove the scalar comparison using analytical endpoints, nearly pure tails and the complete rational certificate. [P08](geometric-gap.md#p08) converts that comparison into a geometric separation.

The coding side is [P09–P10](repetition-coding.md): a fixed coherent encoder, the exact all-record identity, matching exponential-sign bounds and a finite-block capacity implication. The main theorem joins this coding result to the global one-use bound. [P11–P12](limiting-geometries.md#p11) and [P13](eight-use-witness.md#p13) supply controlled limits and an explicit example. [P14–P15](proof-map.md#p14) map evidence, dependencies and attribution.

The two-sided closure corollary uses the exact one-use identity and the geometric lower bound. Its upper estimate treats the nearly pure cost only as an upper bound on the true global minimum. The [mixed-input control](eight-use-witness.md#p134) makes that distinction concrete.

## What the comparison means physically

The measurement branch is destructive and returns only classical information. Quantum transmission concerns its flagged mixture with intact transmission. Every accessible record enters the entropy accounting, including the negative contribution when every qubit in a block is measured.

The code direction is fixed from known channel parameters before any branch, axis or outcome is realized. The proof uses no postselection, feedback or preshared entanglement. Encoding and decoding are otherwise unrestricted and noiseless; the theorem does not provide an efficient standalone decoder.

The smallest frame eigenvalue measures weighted departure from coplanarity. An ensemble can approach rank deficiency because axes approach a plane or because out-of-plane axes receive vanishing weight. At a fixed interior error, the threshold gap closes linearly in this quantity. The statement does not give uniform finite block lengths or a uniformly useful rate.

At exact coplanarity, the converse concerns the defined long balanced-repetition comparison. Other encodings and exceptional shorter blocks remain outside that converse. The two noise endpoints require their separate physical arguments.

## Sources, learning and evidence

[References and their roles](../references/README.md) distinguish established incomplete-erasure frameworks, repetition coding and coding theorems from the geometric comparison proved here. The source-specific correction concerning dephrasure rates and thresholds is retained there. Mathematical claims C1–C6 and literature assessment C7 have different evidential roles.

[The learning map](../learning/milestones.md) contains exactly 30 project-defined milestones with one Preskill anchor. [The verification guide](../verification/README.md) separates artifact integrity, directed interval verification, finite witness evaluation and figure reproduction.

The topic pages are generated from the retained scientific editing sources, so each proof has one editing authority. All 23 model and proof units, their equations and source links are carried into their topic homes. [The source-to-topic map](../website/furnishing-map.json) makes that correspondence explicit; [the maintenance guide](../CONTRIBUTING.md#scientific-source-ownership) explains how to keep it exact.
