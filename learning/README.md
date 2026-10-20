# Learning measurement geometry and superadditivity

This route explains why a family of noisy measurement channels can have zero optimized one-use coherent information and a positive asymptotic quantum rate. It connects the physical records, the global single-use bound, the repetition construction, and the geometric inequality that separates their thresholds.

**[The 30 milestones](milestones.md)** · **[Preskill-to-project bridge](preskill-bridge.md)** · **[Scientific reading route](../science/README.md)**

## One educational anchor

The selected source is **John Preskill, *Quantum Shannon Theory*, Chapter 10 of *Quantum Information*, [arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5)**. The [bridge](preskill-bridge.md#reading-map) preserves the exact sections, printed pages, viewer pages, and equation locators for that edition.

The core passages are §§10.7.1–10.7.2 on coherent information and decoupling, §10.7.4 on repetition followed by outer coding, and the unassisted-achievability statement in §10.9.4. Optional refreshers come from the same chapter. Reading its entire proof of the coding theorem is not a prerequisite for following the project.

The bridge translates the source's notation and separates its depolarizing example from this destructive-measurement channel. It also retains the [v5 sign note for Eq. (10.368)](preskill-bridge.md#edition-note): the achievable rate uses the entropy difference $`H(B)-H(E)`$. The project supplies the remaining geometry, conditional-record calculations, scalar inequality, and certificate arguments. [Primary research references](../references/README.md) attribute the imported theorems and related channels; they serve a different role from the single educational anchor.

## A project-defined map

The [milestone map](milestones.md) contains exactly 30 milestones, defined by the science and usable by any reader, including an LLM. Each has a central question, understanding target, prerequisite milestones, conceptual connections, and source pointers.

| Phase | Milestones | Purpose |
|---|---|---|
| Background and preliminaries | M01–M12 | Build from a qubit and its records to the entropy, geometry, coding, and rigorous-arithmetic tools used by the proof. |
| Narrative and innovation | M13–M30 | Build the channel calculation and global obstruction, assemble the all-record construction, and explain the theorem, finite witness, controlled limits, and uniform threshold-gap law. |

The 12/18 allocation reflects this project's combination of quantum information, measurement-frame geometry, and a computer-assisted entropy comparison. Within each phase, local objects and arguments lead toward their combined meaning. The milestones jointly cover the scientific story; the linked source and proof pages provide the further detail needed to check each derivation.

**Learning labels and model labels are separate.** M01–M30 on the milestone page identify learning milestones. The established model units M01–M08 remain in the scientific account. A link labeled “model M01” means the channel definition, while “milestone M01” means the first learning target. Proof labels P01–P15 and claims C1–C7 retain their scientific meanings.

## Choose a reading route

| What you want to understand | Route |
|---|---|
| The full argument from its foundations | [Milestone M01](milestones.md#m01), using the [Preskill bridge](preskill-bridge.md) where its concepts arise. |
| The project after learning coherent information and coding | [Milestone M13](milestones.md#m13) → [model](../science/model.md) → [one-use benchmark](../science/single-use.md). |
| The entropy inequality and where computation enters | [Milestones M16–M19](milestones.md#m16) → [entropy tools](../science/entropy-tools.md) → [scalar comparison](../science/scalar-inequality.md). |
| How collective coding produces a rate | [Milestones M21–M24](milestones.md#m21) → [all-record repetition proof](../science/repetition-coding.md). |
| The eight-use example and its interpretation | [Milestone M25](milestones.md#m25) → [witness proof and controls](../science/eight-use-witness.md). |
| What happens near rank deficiency | [Milestones M26–M28](milestones.md#m26) → [controlled limits](../science/limiting-geometries.md) → [universal linear closure](../science/geometric-gap.md#p08-linear-closure). |
| Direct specialist review | [Scientific route](../science/README.md) → [proof dependencies](../science/proof-map.md) → [verification commands](../verification/README.md). |

The important distinctions remain the same throughout these routes: one-use coherent information versus capacity; the strict eventual-sign frontier of balanced repetition versus an all-code boundary; a probability-interval width versus a communication rate; and an integrity check versus verification of the entropy certificate. The [notation crosswalk](../science/notation.md) and [model definitions](../science/model.md#m02) make those distinctions explicit.
