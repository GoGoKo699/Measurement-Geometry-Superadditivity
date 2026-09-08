# Three-figure scientific plan

**8 September 2026 · Specification v1, not yet rendered.**

The three figures now have selected panel contents, parameter ranges, mathematical definitions, source-traced inputs and explicit interpretation rules. They follow the frozen story without adding a new research result. The complete specification is in [FIGURE_SPECIFICATIONS.md](FIGURE_SPECIFICATIONS.md); the executable data contract is in `FIGURE_CONTRACT.json`.

## 1. The channel and one concrete separation

Panel (a) shows the two per-use branches, with the true outcome and acquisition error kept inside the channel and the measured qubit discarded. Encoding occurs before random choices. Panel (b) compares the exactly zero optimized one-use coherent information with the retained eight-use construction's positive value per physical use. The fixed parameters are equal Pauli weights, reporting error 0.1, measurement probability 0.7, and block length eight.

The source's per-use value is approximately $7.4774765882\times10^{-5}$. The original 140-digit record and all nine measured-count terms are preserved. There is no visible statistical error bar because these are deterministic arithmetic enclosures, not confidence intervals. The all-measured contribution remains included in the value; its complete breakdown is verification material, not another panel.

## 2. A guaranteed region across reporting noise

The main plot uses equal Pauli weights, $T=I/3$, as one explicitly identified slice of the general geometric theorem. It shows measurement probability versus reporting error, with only the region $p_{\mathrm{cert}}\leq p<p_{\mathrm{rep}}$ shaded at interior errors. Here $p_{\mathrm{cert}}=1/(1+L+d_\epsilon/3)$ is a sufficient global one-use-zero bound and $p_{\mathrm{rep}}=1/(1+L)$ is the repetition construction's strict frontier. Neither is labeled an exact capacity boundary. A small inset plots the same region's width so its narrowness is visible without artificially thickening it.

The curve data use 1,001 rational error coordinates through $[0,1/2]$. The endpoint rows are marked as limits with no guaranteed separation, not included theorem points. The unshaded region remains unclassified.

A necessary cross-figure check is now explicit. At error 0.1 the conservative region starts near $p=0.7079787803$, whereas Figure 1 uses $p=0.7$. That witness is valid by the sharper canonical one-use bound $p_1=59/86$. It must not be silently drawn inside the conservative Figure 2 strip. No witness marker is overlaid by default.

## 3. The approach to a plane

Panel (a) shows the canonical cone family at $\lambda=0,1/16,1/4$, with identical viewing scale and a distinct guide for the axial coding direction. A measurement axis is shown as the line through both signs, not two independent bases.

Panel (b) fixes reporting error 0.1 and plots the exact gap between the cone's one-use threshold and its repetition frontier for $0\leq\lambda\leq1/4$. It compares that curve with the derived straight-line asymptote $(18/289)\lambda$, not a fitted slope. This safely uses the canonical all-error cone domain and adds no second noise sweep. The zero point means coincidence of these construction-related frontiers, not a no-capacity theorem for all coplanar codes.

There are 501 rational geometry coordinates. At the endpoint $\lambda=1/4$ the gap is approximately 0.01798219308; all data preserve the two frontier meanings. This cone is not the equal-Pauli channel used in Figure 1, so no finite-code value is transferred to it.

## What was checked

All 47 source-manifest entries and the archive identity were verified. The witness is copied byte-for-byte, with exact binomial mask probabilities and its per-block/per-use accounting checked. Curve values were newly evaluated from the canonical formulas with 85-digit mpmath intervals and exactly outward-rounded 60-decimal-place bounds. Algebraically equivalent formulas were independently evaluated with Decimal at 100 and 130 digits for all 1,502 plotted curve coordinates. Geometry, exact rational endpoints, asymptotic controls and the cross-figure band distinction were also checked.

The 16 tests include malformed witness and wrong-interval rejection. A fresh-directory data build reproduced every generated data file byte-for-byte. This is figure-input verification, not a new entropy-proof audit, new physical simulation or literature search. The source model, complete proof and frozen argument are unchanged.

## Next step

Render these specifications in Python and inspect the figures' legibility and truthful visual encoding. Exact font sizes, spacing and legend placement can then be adjusted without changing scientific domains or values. No plot is yet visually approved or publication-frozen, and no new repository is required at this point.
