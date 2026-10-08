# Scientific figure overview

The three figures explain the physical channel, the geometric separation guarantee and its approach to coplanarity. Rendered outputs are in `figures/approved/`. The complete specification is in [FIGURE_SPECIFICATIONS.md](FIGURE_SPECIFICATIONS.md); the executable data contract is in `FIGURE_CONTRACT.json`.

## 1. The channel and one concrete separation

Panel (a) shows the two per-use branches, with the true outcome and acquisition error kept inside the channel and the measured qubit discarded. Encoding occurs before random choices. Panel (b) compares the exactly zero optimized one-use coherent information with the eight-use construction's positive value per physical use. The fixed parameters are equal Pauli weights, reporting error 0.1, measurement probability 0.7, and block length eight.

The per-use value is approximately $`7.4774765882\times10^{-5}`$. The 140-digit witness record includes all nine measured-count terms. There is no visible statistical error bar because these are deterministic arithmetic enclosures, not confidence intervals. The all-measured contribution remains included in the value; its complete breakdown is verification material, not another panel.

## 2. A guaranteed region across reporting noise

The main plot uses equal Pauli weights, $`T=I/3`$, as one explicitly identified slice of the general geometric theorem. It shows measurement probability versus reporting error, with only the region $`p_{\mathrm{cert}}\leq p\lt p_{\mathrm{rep}}`$ shaded at interior errors. Here $`p_{\mathrm{cert}}=1/(1+L+d_\epsilon/3)`$ is a sufficient global one-use-zero bound and $`p_{\mathrm{rep}}=1/(1+L)`$ is the repetition construction's strict frontier. Neither is labeled an exact capacity boundary. A small inset plots the same region's width so its narrowness is visible without artificially thickening it.

The curve data use 1,001 rational error coordinates through $`[0,1/2]`$. The endpoint rows are marked as limits with no guaranteed separation, not included theorem points. The unshaded region remains unclassified.

The two figures use different one-use bounds. At error 0.1 the conservative region starts near $`p=0.7079787803`$, whereas Figure 1 uses $`p=0.7`$. That witness is valid by the sharper canonical one-use bound $`p_1=59/86`$. Figure 2 therefore displays the conservative strip without a Figure 1 witness marker.

## 3. The approach to a plane

Panel (a) shows the canonical cone family at $`\lambda=0,1/16,1/4`$, with identical viewing scale and a distinct guide for the axial coding direction. A measurement axis is shown as the line through both signs, not two independent bases.

Panel (b) fixes reporting error 0.1 and plots the exact gap between the cone's one-use threshold and its repetition frontier for $`0\leq\lambda\leq1/4`$. It compares that curve with the derived straight-line asymptote $`(18/289)\lambda`$, not a fitted slope. This is the cone domain valid for every interior reporting error. The zero point means coincidence of these construction-related frontiers, not a no-capacity theorem for all coplanar codes.

There are 501 rational geometry coordinates. At the endpoint $`\lambda=1/4`$ the gap is approximately 0.01798219308; all data preserve the two frontier meanings. This cone is not the equal-Pauli channel used in Figure 1, so no finite-code value is transferred to it.

## Numerical inputs and verification

The witness data include exact binomial mask probabilities and per-block/per-use accounting. Curve values are evaluated from the analytical formulas with 85-digit mpmath intervals and outward-rounded 60-decimal-place bounds. A separate Decimal implementation evaluates algebraically equivalent formulas at 100 and 130 digits for all 1,502 plotted curve coordinates. Checks cover geometry, exact rational endpoints, asymptotic controls, the cross-figure band distinction, and rejection of malformed witness data or invalid intervals.

The Python renderer reproduces the figures from these inputs. See [REPRODUCTION.md](../docs/REPRODUCTION.md) for commands and the scope of the numerical checks.
