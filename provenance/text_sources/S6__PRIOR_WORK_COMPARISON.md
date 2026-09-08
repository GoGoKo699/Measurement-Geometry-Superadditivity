# Bounded prior-work comparison

**8 September 2026.** This is the equation-level comparison required by task E of the fixed claim map. It is not a certification that every relevant paper has been found. No outside researcher has reviewed or endorsed the proposed theorem. The main theoretical sources below were inspected directly; web keyword results were used only for discovery, not as proof of absence.

## 1. Exact channel-class identification

Siddhu and Griffiths, *Positivity and nonadditivity of quantum capacities using generalized erasure channels*, arXiv:2003.00583v2, Section IV, Eq. (35), define

$$\mathcal C_g=(1-\lambda)\mathcal C_1\oplus\lambda\,\mathrm{id}.$$

Taking `lambda=1-p` and `C1=M_epsilon`, the noisy classical measurement map in our theorem, gives the present receiver channel exactly, up to block order. Their Eq. (25) supplies the block-diagonal coherent-information accounting. Their evaluated examples use amplitude- and phase-damping channel pairs. Section V.C discusses incomplete-erasure positivity, not the present all-frame, all-common-error geometric guarantee.

**Disposition:** channel class and flag accounting are inherited. The formula alone does not imply the new entropy-cost bound or a separation for every full-span frame. Do not call this a new channel class, and compare the receiver map rather than only a complementary-channel name. [R1]

## 2. Closest repetition-code threshold precedent

Leditzky, Leung and Smith, *Dephrasure channel and superadditivity of coherent information*, arXiv:1806.08327, use dephasing on the quantum-survival branch and an input-independent erasure flag. Their weighted repetition formula is Eq. (15); Appendix F establishes a block-length-independent positivity threshold for that family. The present channel leaves surviving quantum outputs intact and retains a noisy input-dependent classical record in the destructive branch.

**Disposition:** repetition coding and coherent-information superadditivity are established. Their construction-specific threshold result does not directly give our full-span separation. It is not contradicted by a different channel. Neither their repetition theorem nor our coplanar equality excludes every other code. [R2]

## 3. Operational implication of one positive block

Devetak's quantum coding theorem identifies quantum capacity with regularized optimized coherent information. Apply it to the finite superchannel `N^tensor n` after selecting a positive inner block; divide its achievable rate by n. This establishes the stated positive capacity. It does not require the inner repetition family's per-use rate to have a positive limit as the inner length diverges.

**Disposition:** the passage from the constructed finite positive block to asymptotic communication is standard, necessary credit. It is not a newly proved decoder or efficient algorithm. [R3]

## 4. More recent neighboring work

Bhalerao and Leditzky, *Improving quantum communication rates with permutation-invariant codes*, arXiv:2508.09978v1, develop efficient evaluation of coherent information for structured many-use inputs and improve thresholds for several channel families, including dephrasure. Their scope makes a large-block numerical rate or threshold improvement alone insufficient as a novelty argument. Their stated families and construction do not supply the all-common-error arbitrary full-span noisy-axis theorem examined here. [R4]

Cheng and Berta, *Superadditivity for Entanglement-Assisted Communication*, arXiv:2607.15151v1, study Petz–Renyi information and entanglement-assisted reliability for measurement channels. They also use separable correlated input marginals. This is not the unassisted quantum-capacity threshold task, and separability of our average input should not be advertised as a new ingredient. The comparison here is limited to their stated theorem scope and abstract, not a full independent audit of their proof. [R5]

## 5. What is the defensible distinction?

The channel form, repetition strategy, global phenomenon of coherent-information nonadditivity, and outer-coding implication are not proposed as new. The candidate theorem adds the following specific statement:

> For every finite positive-weight full-span axis ensemble and every nontrivial common symmetric reporting error, a rigorously controlled entropy comparison separates the GLOBAL one-use cost from the constructive repetition cost, yielding a nonempty region with Q^(1)=0<Q.

The quantitative gap and controlled planar limit refine that statement. The eight-use example is an illustration, not the basis for a sweeping novelty claim.

In the inspected primary sources, the exact full-span/all-common-error implication is neither stated nor obtained by substituting into an existing evaluated example. Deriving it from the general channel framework still requires the entropy-cost comparison audited here. This supports a specific working contribution claim. It does not establish absolute priority, an optimal capacity theorem, or PRL acceptance.

The defensible manuscript wording is “We prove a full-span sufficient condition…” rather than “the first measurement channel with superadditivity,” “a new channel class,” or “full span is necessary for any collective coding advantage.” No theorem change is required by the comparisons completed in this audit.

## 6. Search limits and stopping decision

Searches included combinations of “incomplete erasure,” “noisy classical record,” “measurement geometry,” “informationally complete,” “coherent information,” and “superadditivity,” followed by inspection of the primary records below. These searches returned many irrelevant results and did not amount to exhaustive citation-network or unpublished-work coverage. Failure to find a title was not used as evidence that no related theorem exists.

**Task E status:** a defensible distinction from the checked closest frameworks is established for drafting; absolute priority remains unproved. Retain appropriate citations and invite specialist scrutiny during normal paper development. This is not a reason to continue an unbounded cycle of numerical searches or repeat audits without a specific new issue.

Together with A–D, the completed comparison meets the map's stopping rule for a first Letter draft. It does not replace eventual peer review.

## Primary records

R1. Vikesh Siddhu and Robert B. Griffiths, arXiv:2003.00583v2. Section IV, Eqs. (25), (34)–(35), and Section V.C. https://arxiv.org/abs/2003.00583

R2. Felix Leditzky, Debbie Leung and Graeme Smith, arXiv:1806.08327. Eq. (15), Section VI and Appendix F. https://arxiv.org/abs/1806.08327

R3. Igor Devetak, *The private classical capacity and quantum capacity of a quantum channel*, arXiv:quant-ph/0304127v6. https://arxiv.org/abs/quant-ph/0304127

R4. Sujeet Bhalerao and Felix Leditzky, arXiv:2508.09978v1. https://arxiv.org/abs/2508.09978

R5. Hao-Chung Cheng and Mario Berta, arXiv:2607.15151v1. https://arxiv.org/abs/2607.15151

Access date for this comparison: 8 September 2026. PDF text was inspected for R1–R3 and the HTML full text was opened for R4. The attempted browser PDF screenshots were unavailable; no figure or table-based claim rests on those failed screenshots.
