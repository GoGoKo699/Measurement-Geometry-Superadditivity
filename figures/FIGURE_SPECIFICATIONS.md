# Scientific figure specifications and canonical inputs

**Measurement geometry and coherent-information superadditivity · version 1 · 8 September 2026**

This specification implements the frozen three-figure roles in canonical source S2. It selects presentation parameters and calculates plotting inputs, but adds no scientific claim and renders no figure. The existing theorem, proof, independent certificate checkers and frozen one-page argument are unchanged. The current baseline includes the canonical model and proof directly in `docs/` and the numerical inputs in `data/figures/`. `provenance/INPUT_ARCHIVES.json` preserves the specification-stage archive identities; those archives are not required or included as runtime dependencies. The original specification-stage rendered status is retained as historical metadata; the current approval is recorded in `STATUS.md`.

## Design decision and scope

The sequence is **physical channel and a concrete separation → family guarantee illustrated by one channel slice → controlled approach to a plane**. Each figure has one primary question. The complete all-record certificate remains available without becoming an extra main-text figure.

Only one finite coding example is displayed: equal Pauli weights, $`\epsilon=1/10`$, $`p=7/10`$, and $`n=8`$. The theorem illustration sweeps reporting error for the same equal-Pauli geometry. The limiting-family illustration fixes the same reporting error, $`\epsilon=1/10`$, but changes the geometry to the canonical cone family. The latter is a different channel from the Pauli example, except at the orthogonal cone value outside the selected plotting range; no finite-code witness is transported to it.

**Status of these choices.** The canonical theory prescribes the scientific roles and allowable domains; the concrete panel structure, grids, labels, fixed cone error and geometry snapshots below are new presentation choices in this version. Their numeric inputs are checked against the canonical formulas, not treated as newly audited physics.

## Figure 1: What is received, and what collective coding establishes

### Reader's question

What channel is being used, and what does $`Q^{(1)}=0\lt Q`$ mean in one explicit case?

### Panel (a): per-use operation and the coding order

Use one concise vector schematic of the channel. An unknown logical input is encoded **before** independent uses of the channel. A magnified per-use box branches into:

- intact quantum output, probability $`1-p`$;
- random measurement axis $`b\sim w`$, destructive measurement, and noisy reported sign $`s=r\oplus z`$, probability $`p`$, with $`z\sim\mathrm{Bernoulli}(\epsilon)`$.

The receiver outputs are the intact qubits plus the correct mask/axis labels and reported signs. The measured qubit ends at a clearly labeled discarded-system mark. The hidden true sign $`r`$ and acquisition-error variable $`z`$ stay inside the channel box, explicitly unavailable to the receiver. There is no arrow from a future axis, outcome or error to the encoder. There is no selected-survivor pathway: all masks and reports reach the same receiver description.

The figure may use a generic $`n`$-use wrapper; panel (b) then supplies $`n=8`$. Do not depict one block as an already demonstrated high-fidelity decoder. Do not draw the measured branch as a usable residual quantum output. Label the outcome error as an **acquisition/report error**, not an encoding-gate error or a damaged basis label. These are the operations in canonical M01 and P01.

### Panel (b): one global baseline and one constructive value

Two positions on one vertical scale:

1. **Best one-use input:** $`Q^{(1)}=0`$, shown by a visible marker on the zero baseline.
2. **Eight-use construction / 8:** $`I_8/8=7.47747658815596\ldots\times10^{-5}`$, shown by a bar or stem/marker.

Use $`\epsilon=0.10`$, $`p=0.70`$, and equal $`X,Y,Z`$ axis probabilities as a visible parameter annotation. Vertical label: **Coherent information per physical use**. Use a displayed $`\times10^{-5}`$ factor and a linear axis including zero; preliminary limits $`0`$ to $`9\times10^{-5}`$ with ticks at $`0,2,4,6,8`$ times $`10^{-5}`$. This is not a plot of exact capacity. The first value is globally optimized; the second is a constructive lower bound, not the optimized eight-use value.

The positive label can be rounded to $`7.48\times10^{-5}`$; the scientific caption records the source-supported bound $`I_8/8\gt 7.47\times10^{-5}`$. Do not draw artificially visible error bars. The source intervals are rigorous numerical enclosures, far below visual resolution, **not bootstrap confidence intervals**.

### Canonical inputs and numerical status

- `data/figures/figure1_comparison.csv`: the two plotted quantities, source lower/upper bounds, status and normalization.
- `data/figures/figure1_original_witness140.json`: source W1 copied byte-for-byte.
- `data/figures/figure1_all_masks_not_for_display.csv`: all nine measured-count terms retained as verification inputs, not an extra plotted panel.
- `FIGURE_CONTRACT.json`: the required schematic information and forbidden arrows.

The exact single-use threshold is $`p_1=59/86\lt 7/10`$, from canonical P13. The source's all-measured probability is $`p^8=0.05764801`$; its weighted block contribution is negative. Both are preserved and checked. The witness's entropy arithmetic was **not rerun** in this specification pass.

### Caption content specification

Describe the two branches and what remains inaccessible. State that encoding precedes random choices and every outcome is included. Identify $`Q^{(1)}`$ as the maximum over every one-use input, not operational one-shot capacity. Specify the antipodal eigenstates of $`(X+Y+Z)/\sqrt3`$ and the balanced eight-use input, and distinguish the positive per-use block value from a finite-block decoding fidelity. The operational rate interpretation requires outer coding. Mention the exact one-use threshold $`59/86`$; avoid discussion of certificate digit counts in the figure.

### Acceptance checks

The plotted positive value must use the per-use source enclosure, not $`I_8`$ without division. Zero must mean the global optimum, not the maximally mixed input alone. No returned measured qubit, hidden-sign access, feedback, or postselected branch may appear. The numeric bar must not be labeled $`Q`$ or the globally optimized $`Q^{(8)}`$.

## Figure 2: What the geometric theorem guarantees across reporting noise

### Reader's question

Why is the separation systematic rather than a favorable isolated example?

### Quantitative design

Use one main parameter plot with a small width inset. Above it, state the general sufficient condition: finite full-span axes and common $`0\lt \epsilon\lt 1/2`$ imply a nonempty certified interval. The plot is explicitly an **equal-Pauli illustrative slice**, not a picture of every full-span ensemble simultaneously:

```math
w_X=w_Y=w_Z=1/3,\qquad T=I/3,\qquad\lambda=1/3.
```

Horizontal axis: **Reporting-error probability $`\epsilon`$**, $`0\leq\epsilon\leq1/2`$.

Vertical axis: **Measurement probability $`p`$**, approximately $`0.48`$ to $`1.02`$ so both limiting endpoints remain visible.

Let

```math
a=(1-2\epsilon)^2,\quad c=1-a,\quad L=\frac{c}{\sqrt{1-a/3}},\quad d_\epsilon=\frac3{35}ca.
```

Draw exactly two boundary curves:

```math
p_{\mathrm{cert}}(\epsilon)=\frac{1}{1+L+d_\epsilon/3},\qquad p_{\mathrm{rep}}(\epsilon)=\frac{1}{1+L}.
```

Here $`p_{\mathrm{cert}}`$ is a **new display-only name** for the lower endpoint already present in canonical M04/P10. It is a sufficient zero-one-use bound, not the exact $`p_1`$. $`p_{\mathrm{rep}}`$ is the construction's strict eventual-sign frontier, not an exact capacity boundary.

Shade **only** $`p_{\mathrm{cert}}\leq p\lt p_{\mathrm{rep}}`$ at interior errors, with the label **Certified separation: $`Q^{(1)}=0\lt Q`$**. Use a leader pointing to the band rather than crowding text into it. Give the lower and upper lines distinct line styles. Make the strict upper-edge interpretation explicit in the caption; a filled plotting polygon must not be used to assert equality at that frontier.

Outside the band, leave the background neutral. It must not be labeled “no capacity,” “no advantage,” “classical,” or “failure.” The theorem has not classified the whole parameter plane.

### Width inset: visible bound without artificial thickening

Because the strip is narrow, include an inset of

```math
\Delta p_{\mathrm{cert}}=p_{\mathrm{rep}}-p_{\mathrm{cert}} =\frac{d_\epsilon/3}{(1+L)(1+L+d_\epsilon/3)}.
```

Use the same horizontal error range and vertical label **Certified interval width** with a $`\times10^{-3}`$ scale. This is probability width, not a transmission rate. A preliminary vertical range of $`0`$ to $`4\times10^{-3}`$ contains all chosen samples with margin. Do not thicken the band or normalize it differently without disclosure. The inset has no fitted peak, inferred phase transition, or extra parameter sweep.

At $`\epsilon=0`$ and $`1/2`$, the algebraic limiting curves coincide at $`p=1`$ and $`p=1/2`$. Use open limit markers and mark **no separation at this endpoint**. The interior theorem is not asserted there; canonical P11 supplies the separate endpoint controls.

### Canonical inputs and numerical status

`data/figures/figure2_pauli_guaranteed_region.csv` contains **1,001 exact-rational error coordinates**, $`\epsilon=j/2000`$, $`j=0,\ldots,1000`$. Every derived curve coordinate has an outward numerical enclosure and a 17-significant-digit plotting value. Endpoint rows are explicitly marked outside the theorem's interior domain. The same rows supply the inset.

The expressions come from canonical M03–M04, P08 and P12.1. **Only $`L`$ is evaluated using the Pauli symmetry here; no global single-use optimizer is used to create this plot.** There is no exact-$`p_1`$ curve extrapolated over the full error range.

### Cross-figure safeguard

At $`\epsilon=0.1`$ the two plotted boundaries are approximately

```math
p_{\mathrm{cert}}=0.70797878025951\ldots,\qquad p_{\mathrm{rep}}=0.71129378140889\ldots.
```

The Figure 1 witness has $`p=0.7`$, **below the conservative shaded strip**. It is valid because canonical P13 uses the sharper exact one-use threshold $`59/86`$. Do not move its marker into the strip, truncate the band to include it, or imply it is proved by this particular conservative bound. By default do **not** overlay the witness on Figure 2. The caption should say that the Figure 1 point uses a sharper bound and that this strip need not exhaust the separation region. The relationship is machine-checked in `data/figures/cross_figure_witness_bound_check.json`.

### Caption content specification

State the arbitrary-full-span theorem first, then identify this plot as one equal-Pauli slice. Define $`p_{\mathrm{cert}}`$ and $`p_{\mathrm{rep}}`$ with their sufficient/construction meanings. Identify the shaded interval, its open upper endpoint, and the absence of a separation guarantee at the two reporting-noise endpoints. Explain the width inset and distinguish the Figure 1 sharper bound. Do not call this a quantum-capacity phase diagram or evidence from 1,001 simulated channels: the grid evaluates an analytical bound already proved over the continuous domain.

## Figure 3: How the advantage becomes arbitrarily weak near a plane

### Reader's question

What happens as a full-span measurement ensemble approaches coplanarity?

### Panel (a): one explicitly defined geometric path

Show three snapshots of the equally weighted cone family at $`\lambda=0,1/16,1/4`$:

```math
n_j=(\sqrt{1-\lambda}\cos(2\pi j/3), \sqrt{1-\lambda}\sin(2\pi j/3),\sqrt\lambda),\quad j=0,1,2.
```

Each measurement axis should be drawn as a line through the origin, with both representative directions $`\pm n_j`$, not as six independently selected bases. The positive representatives lie on the cone. A dashed vertical guide may mark the axial coding direction $`u=(0,0,1)`$; it is **not a fourth measurement axis**. Use the same viewing direction and geometric scale in all snapshots.

Label the first snapshot “coplanar” and the other two “full span.” The geometry is determined entirely by the source formula, not drawn from an unconstrained artist's approximation. Do not claim that the small nonzero snapshot gives a large or practical advantage.

### Panel (b): exact threshold gap and its limiting tangent

Fix **$`\epsilon=0.1`$**, matching Figure 1's record error without implying the ensembles or witnesses are identical. Use only this error curve. Select the safe all-error domain **$`0\leq\lambda\leq1/4`$**, even though the selected error would permit a larger domain. This avoids teaching a parameter-dependent validity condition through a main-text axis limit.

Draw

```math
p_1(\lambda)=\frac{1-a\lambda}{1-a\lambda+c},\qquad p_{\mathrm{rep}}(\lambda)=\frac{\sqrt{1-a\lambda}}{\sqrt{1-a\lambda}+c},
```

through their difference

```math
\Delta p_{\mathrm{cone}}=p_{\mathrm{rep}}-p_1.
```

Horizontal axis: **Weakest directional coverage $`\lambda=\lambda_{\min}(T)`$**.

Vertical axis: **Threshold gap $`p_{\mathrm{rep}}-p_1`$**. Use linear axes, zero included, and a preliminary range $`0`$ to $`0.020`$. The solid curve is the exact gap between the exact one-use frontier and the stated repetition construction frontier in this family. It is **not** a gap to an exact all-code capacity threshold.

Overlay one dashed straight line,

```math
\Delta p_{\mathrm{linear}}=\frac{ca}{2(1+c)^2}\lambda=\frac{18}{289}\lambda.
```

Its label must say **Small-$`\lambda`$ asymptote**, not “fit.” It is derived from canonical P12, not estimated by regression. Extend it across the selected axis range only as a comparison line, without claiming the higher-order correction vanishes there.

Include the exact zero point at $`\lambda=0`$. Its interpretation is coincidence of the two frontiers for this construction; it is not an all-code prohibition for the coplanar channel. No logarithmic axis is required to make this point. Tiny-$`\lambda`$ numerical controls are retained for verification but not added as another panel.

### Canonical inputs and numerical status

- `data/figures/figure3_cone_gap.csv`: **501 exact-rational coordinates**, $`\lambda=j/2000`$, $`j=0,\ldots,500`$, with exact rational $`p_1`$, outward enclosures of both frontiers, the stable gap, and the analytical tangent.
- `data/figures/figure3_cone_geometry.csv`: nine axis records, three per geometry snapshot, with equal weights and exact frame entries.
- `data/figures/figure3_small_lambda_controls_not_for_display.csv`: 12 checks of the source's limiting formula, not a fitted exponent or a second error sweep.

Gap values are evaluated stably as

```math
\Delta p_{\mathrm{cone}}= \frac{ca\lambda\sqrt{1-a\lambda}} {(1+\sqrt{1-a\lambda})(\sqrt{1-a\lambda}+c)(1-a\lambda+c)},
```

an algebraic rewriting of the canonical exact formulas. This avoids subtracting nearly equal thresholds near the plane. It is an implementation identity, not a new scientific result. At the selected endpoint $`\lambda=1/4`$, $`p_1=0.7`$ and $`\Delta p_{\mathrm{cone}}\simeq0.01798219308`$. This coincidence of $`p_1`$ with the Figure 1 measurement probability does not transfer the eight-use witness to the cone ensemble.

### Caption content specification

Define the cone axes and equal probabilities, the fixed error, the exact-domain restriction, the two different frontier meanings, and the theoretical linear asymptote. State that a nonzero geometric gap need not imply a uniformly short block or useful rate. Do not add a block-length scaling curve: it is unnecessary to this figure's question and not a retained figure input.

## Cross-figure presentation rules

The scalar costs $`\Gamma,L,\ell`$ and the numerical certificate machinery belong in the proof and figure caption as necessary, not in a crowded front-facing schematic. Figure 2 needs the boundary definitions but not an inset of the entropy-certificate partition.

A zero coherent-information value must not be relabeled zero operational single-use capacity. A code's positive value must not be relabeled exact $`Q`$. Numerical enclosures must not look like confidence intervals. Unshaded parameter regions are unclassified, not negative results. No “noise improves capacity” claim follows from a separation between coding quantities.

Plot fractions consistently on both probability axes; e.g. $`\epsilon=0.1`$ means 10%, not 0.1%. Probability widths are not percentages unless all values are explicitly converted. Coherent-information entropy units and block versus per-use normalization are stated next to their numbers.

These are scientific layout decisions. Exact physical dimensions, font sizes, legend placement and any colors should be frozen after rendered vector drafts are inspected. All components, including the schematics, should ultimately be reproducible in Python; there is no TikZ or manuscript TeX dependency. No styling decision should alter a mathematical domain or magnify a band without disclosure.

## Completion boundary

This version supplies the scientific content contract, numerical inputs and validation checks. No figure is rendered, visually approved, or publication-frozen yet. The next step is to render these exact specifications and inspect legibility, truthful visual encoding, and cross-figure consistency. That step should not launch new simulations or alter the audited theorem. The dedicated repository is still not needed until the scientific baseline and its figures are ready for a clean checkout.
