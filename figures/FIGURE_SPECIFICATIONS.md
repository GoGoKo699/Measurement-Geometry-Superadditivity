# Scientific figure specifications and canonical inputs

The three figures show the physical channel, the geometric separation guarantee and the approach to coplanarity. This specification defines their scientific content, parameter ranges and numerical inputs. The model and proof are in `docs/`, plotting inputs are in `data/figures/`, and rendered outputs are in `figures/approved/`. Input identities are recorded in `provenance/INPUT_ARCHIVES.json`.

## Figure sequence

The sequence is **physical channel and a concrete separation → family guarantee illustrated by one channel slice → controlled approach to a plane**. Each figure addresses one primary question.

Only one finite coding example is displayed: equal Pauli weights, $`\epsilon=1/10`$, $`p=7/10`$, and $`n=8`$. The theorem illustration sweeps reporting error for the same equal-Pauli geometry. The limiting-family illustration fixes the same reporting error, $`\epsilon=1/10`$, but changes the geometry to the canonical cone family. The latter is a different channel from the Pauli example, except at the orthogonal cone value outside the selected plotting range; no finite-code witness is transported to it.

## Figure 1: What is received, and what collective coding establishes

### Reader's question

What channel is being used, and what does $`Q^{(1)}=0\lt Q`$ mean in one explicit case?

### Panel (a): per-use operation and the coding order

A vector schematic shows the channel. An unknown logical input is encoded **before** independent uses of the channel. A magnified per-use box branches into:

- intact quantum output, probability $`1-p`$;
- random measurement axis $`b\sim w`$, destructive measurement, and noisy reported sign $`s=r\oplus z`$, probability $`p`$, with $`z\sim\mathrm{Bernoulli}(\epsilon)`$.

The receiver outputs are the intact qubits plus the correct mask/axis labels and reported signs. The measured qubit ends at a clearly labeled discarded-system mark. The hidden true sign $`r`$ and acquisition-error variable $`z`$ stay inside the channel box, explicitly unavailable to the receiver. There is no arrow from a future axis, outcome or error to the encoder. There is no selected-survivor pathway: all masks and reports reach the same receiver description.

The schematic uses a generic $`n`$-use wrapper; panel (b) specializes to $`n=8`$. The block denotes a coding input, with the operational rate obtained through outer coding. The measured branch is classical, and its outcome error is an **acquisition/report error**. These are the operations in canonical M01 and P01.

### Panel (b): one global baseline and one constructive value

Two positions on one vertical scale:

1. **Best one-use input:** $`Q^{(1)}=0`$, shown by a visible marker on the zero baseline.
2. **Eight-use construction / 8:** $`I_8/8=7.47747658815596\ldots\times10^{-5}`$, shown by a bar or stem/marker.

The parameter annotation is $`\epsilon=0.10`$, $`p=0.70`$, with equal $`X,Y,Z`$ axis probabilities. The vertical label is **Coherent information per physical use**. The linear axis includes zero, displays a $`\times10^{-5}`$ factor, and runs from $`0`$ to $`9\times10^{-5}`$ with ticks at $`0,2,4,6,8`$ times $`10^{-5}`$. This is not a plot of exact capacity. The first value is globally optimized; the second is a constructive lower bound, not the optimized eight-use value.

The positive label is rounded to $`7.48\times10^{-5}`$; the scientific caption records the source-supported bound $`I_8/8\gt 7.47\times10^{-5}`$. The rigorous numerical enclosures are far below visual resolution and represent arithmetic bounds, **not bootstrap confidence intervals**.

### Canonical inputs

- `data/figures/figure1_comparison.csv`: the two plotted quantities, source lower/upper bounds, status and normalization.
- `data/figures/figure1_original_witness140.json`: source W1 copied byte-for-byte.
- `data/figures/figure1_all_masks_not_for_display.csv`: all nine measured-count terms retained as verification inputs, not an extra plotted panel.
- `FIGURE_CONTRACT.json`: the required schematic information and forbidden arrows.

The exact single-use threshold is $`p_1=59/86\lt 7/10`$, from canonical P13. The source's all-measured probability is $`p^8=0.05764801`$; its weighted block contribution is negative. Both enter the all-record witness calculation.

### Caption content specification

Describe the two branches and what remains inaccessible. State that encoding precedes random choices and every outcome is included. Identify $`Q^{(1)}`$ as the maximum over every one-use input, not operational one-shot capacity. Specify the antipodal eigenstates of $`(X+Y+Z)/\sqrt3`$ and the balanced eight-use input, and distinguish the positive per-use block value from a finite-block decoding fidelity. The operational rate interpretation requires outer coding. Mention the exact one-use threshold $`59/86`$; avoid discussion of certificate digit counts in the figure.

### Acceptance checks

The plotted positive value must use the per-use source enclosure, not $`I_8`$ without division. Zero must mean the global optimum, not the maximally mixed input alone. No returned measured qubit, hidden-sign access, feedback, or postselected branch may appear. The numeric bar must not be labeled $`Q`$ or the globally optimized $`Q^{(8)}`$.

## Figure 2: What the geometric theorem guarantees across reporting noise

### Reader's question

Why is the separation systematic rather than a favorable isolated example?

### Quantitative design

A main parameter plot and a small width inset display the general sufficient condition: finite full-span axes and common $`0\lt \epsilon\lt 1/2`$ imply a nonempty certified interval. The plot is explicitly an **equal-Pauli illustrative slice**, not a picture of every full-span ensemble simultaneously:

```math
w_X=w_Y=w_Z=1/3,\qquad T=I/3,\qquad\lambda=1/3.
```

Horizontal axis: **Reporting-error probability $`\epsilon`$**, $`0\leq\epsilon\leq1/2`$.

Vertical axis: **Measurement probability $`p`$**, approximately $`0.48`$ to $`1.02`$ so both limiting endpoints remain visible.

Let

```math
a=(1-2\epsilon)^2,\quad c=1-a,\quad L=\frac{c}{\sqrt{1-a/3}},\quad d_\epsilon=\frac3{35}ca.
```

The two boundary curves are:

```math
p_{\mathrm{cert}}(\epsilon)=\frac{1}{1+L+d_\epsilon/3},\qquad p_{\mathrm{rep}}(\epsilon)=\frac{1}{1+L}.
```

Here $`p_{\mathrm{cert}}`$ is the display name for the lower endpoint already present in canonical M04/P10. It is a sufficient zero-one-use bound, not the exact $`p_1`$. $`p_{\mathrm{rep}}`$ is the construction's strict eventual-sign frontier, not an exact capacity boundary.

The shaded region is **only** $`p_{\mathrm{cert}}\leq p\lt p_{\mathrm{rep}}`$ at interior errors, with the label **Certified separation: $`Q^{(1)}=0\lt Q`$**. A leader points to the band, and distinct line styles identify its boundaries. The caption specifies the strict upper edge.

Outside the sufficient band, the neutral background indicates unclassified parameter values.

### Width inset: visible bound without artificial thickening

An inset makes the narrow strip visible through its width

```math
\Delta p_{\mathrm{cert}}=p_{\mathrm{rep}}-p_{\mathrm{cert}} =\frac{d_\epsilon/3}{(1+L)(1+L+d_\epsilon/3)}.
```

The inset uses the same horizontal error range and the vertical label **Certified interval width** with a $`\times10^{-3}`$ scale. This is probability width, not a transmission rate. The vertical range of $`0`$ to $`4\times10^{-3}`$ contains all plotted samples with margin.

At $`\epsilon=0`$ and $`1/2`$, the algebraic limiting curves coincide at $`p=1`$ and $`p=1/2`$. Open limit markers indicate **no separation at this endpoint**. The interior theorem is not asserted there; canonical P11 supplies the separate endpoint controls.

### Canonical inputs

`data/figures/figure2_pauli_guaranteed_region.csv` contains **1,001 exact-rational error coordinates**, $`\epsilon=j/2000`$, $`j=0,\ldots,1000`$. Every derived curve coordinate has an outward numerical enclosure and a 17-significant-digit plotting value. Endpoint rows are explicitly marked outside the theorem's interior domain. The same rows supply the inset.

The expressions come from canonical M03–M04, P08 and P12.1. **$`L`$ is evaluated using Pauli symmetry.** The displayed sufficient bound applies across the full error range, while exact $`p_1`$ formulas have their stated parameter-dependent domains.

### Cross-figure safeguard

At $`\epsilon=0.1`$ the two plotted boundaries are approximately

```math
p_{\mathrm{cert}}=0.70797878025951\ldots,\qquad p_{\mathrm{rep}}=0.71129378140889\ldots.
```

The Figure 1 witness has $`p=0.7`$, **below the conservative shaded strip**. It is valid because canonical P13 uses the sharper exact one-use threshold $`59/86`$. Figure 2 displays the conservative strip without a Figure 1 witness marker. The caption explains the sharper bound for the Figure 1 point and the sufficient character of the strip. The relationship is machine-checked in `data/figures/cross_figure_witness_bound_check.json`.

### Caption content specification

State the arbitrary-full-span theorem first, then identify this plot as one equal-Pauli slice. Define $`p_{\mathrm{cert}}`$ and $`p_{\mathrm{rep}}`$ with their sufficient/construction meanings. Identify the shaded interval, its open upper endpoint, and the absence of a separation guarantee at the two reporting-noise endpoints. Explain the width inset and distinguish the Figure 1 sharper bound. Do not call this a quantum-capacity phase diagram or evidence from 1,001 simulated channels: the grid evaluates an analytical bound already proved over the continuous domain.

## Figure 3: How the advantage becomes arbitrarily weak near a plane

### Reader's question

What happens as a full-span measurement ensemble approaches coplanarity?

### Panel (a): one explicitly defined geometric path

Panel (a) shows three snapshots of the equally weighted cone family at $`\lambda=0,1/16,1/4`$:

```math
n_j=(\sqrt{1-\lambda}\cos(2\pi j/3), \sqrt{1-\lambda}\sin(2\pi j/3),\sqrt\lambda),\quad j=0,1,2.
```

Each measurement axis is drawn as a line through the origin, with both representative directions $`\pm n_j`$, not as six independently selected bases. The positive representatives lie on the cone. A dashed vertical guide marks the axial coding direction $`u=(0,0,1)`$; it is **not a fourth measurement axis**. All snapshots share the same viewing direction and geometric scale.

The first snapshot is labeled “coplanar” and the other two “full span.” The geometry is determined by the displayed formula; full span is a positivity criterion whose gap can be arbitrarily small.

### Panel (b): exact threshold gap and its limiting tangent

The fixed error is **$`\epsilon=0.1`$**, matching Figure 1's record error while using a different ensemble. The displayed domain **$`0\leq\lambda\leq1/4`$** is the cone range valid for every interior reporting error.

The two frontiers are

```math
p_1(\lambda)=\frac{1-a\lambda}{1-a\lambda+c},\qquad p_{\mathrm{rep}}(\lambda)=\frac{\sqrt{1-a\lambda}}{\sqrt{1-a\lambda}+c},
```

and the plotted quantity is their difference

```math
\Delta p_{\mathrm{cone}}=p_{\mathrm{rep}}-p_1.
```

Horizontal axis: **Weakest directional coverage $`\lambda=\lambda_{\min}(T)`$**.

Vertical axis: **Threshold gap $`p_{\mathrm{rep}}-p_1`$**. The linear axis includes zero and spans $`0`$ to $`0.020`$. The solid curve is the exact gap between the exact one-use frontier and the stated repetition construction frontier in this family. It is **not** a gap to an exact all-code capacity threshold.

The dashed straight line is

```math
\Delta p_{\mathrm{linear}}=\frac{ca}{2(1+c)^2}\lambda=\frac{18}{289}\lambda.
```

Its label is **Small-$`\lambda`$ asymptote**. Derived from canonical P12, it provides a linear comparison across the plotted range; the exact curve includes higher-order corrections.

The exact zero point is included at $`\lambda=0`$. Its interpretation is coincidence of the two frontiers for this construction; it is not an all-code prohibition for the coplanar channel. Tiny-$`\lambda`$ numerical controls support verification of this limit.

### Canonical inputs

- `data/figures/figure3_cone_gap.csv`: **501 exact-rational coordinates**, $`\lambda=j/2000`$, $`j=0,\ldots,500`$, with exact rational $`p_1`$, outward enclosures of both frontiers, the stable gap, and the analytical tangent.
- `data/figures/figure3_cone_geometry.csv`: nine axis records, three per geometry snapshot, with equal weights and exact frame entries.
- `data/figures/figure3_small_lambda_controls_not_for_display.csv`: 12 numerical controls for the limiting formula.

Gap values are evaluated stably as

```math
\Delta p_{\mathrm{cone}}= \frac{ca\lambda\sqrt{1-a\lambda}} {(1+\sqrt{1-a\lambda})(\sqrt{1-a\lambda}+c)(1-a\lambda+c)},
```

an algebraic rewriting of the canonical exact formulas. This avoids subtracting nearly equal thresholds near the plane. At the selected endpoint $`\lambda=1/4`$, $`p_1=0.7`$ and $`\Delta p_{\mathrm{cone}}\simeq0.01798219308`$. This coincidence of $`p_1`$ with the Figure 1 measurement probability does not transfer the eight-use witness to the cone ensemble.

### Caption content specification

Define the cone axes and equal probabilities, the fixed error, the exact-domain restriction, the two different frontier meanings, and the theoretical linear asymptote. State that a nonzero geometric gap need not imply a uniformly short block or useful rate.

## Cross-figure presentation rules

The scalar costs $`\Gamma,L,\ell`$ and the numerical certificate machinery belong in the proof and figure caption as necessary, not in a crowded front-facing schematic. Figure 2 needs the boundary definitions but not an inset of the entropy-certificate partition.

A zero coherent-information value must not be relabeled zero operational single-use capacity. A code's positive value must not be relabeled exact $`Q`$. Numerical enclosures must not look like confidence intervals. Unshaded parameter regions are unclassified, not negative results. No “noise improves capacity” claim follows from a separation between coding quantities.

Plot fractions consistently on both probability axes; e.g. $`\epsilon=0.1`$ means 10%, not 0.1%. Probability widths are not percentages unless all values are explicitly converted. Coherent-information entropy units and block versus per-use normalization are stated next to their numbers.

The Python renderer reproduces all components, including the schematics, with the specified mathematical domains and probability scales.

## Rendering and verification

`figures/code/render_figures.py` renders the figures from the canonical inputs; `figures/code/verify_render.py` checks their content and output identities. `figures/CAPTIONS.md` supplies the scientific captions. See [REPRODUCTION.md](../docs/REPRODUCTION.md) for the reproduction commands and numerical checks.
