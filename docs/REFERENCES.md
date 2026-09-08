# Attribution and standard tools carried from the supplied sources

**Original consolidation: 8 September 2026.** The initial record carried attribution from the supplied sources without a new literature search. The dated correction below records a subsequent primary-source check. Neither step certifies absolute priority.

## Standard results used in the proof

**EXT1 — The coherent-information coding theorem.** Igor Devetak, *The private classical capacity and quantum capacity of a quantum channel*, arXiv:quant-ph/0304127. Used only for the implication from a chosen finite block with positive coherent information to a positive asymptotic unassisted quantum rate. It does not supply an efficient decoder or high-fidelity recovery from the inner repetition block alone. Identified in source S4 and S6 §3.

**Entropy background, as invoked by the source proof.** Quantum conditional-entropy concavity under mixing; the relative-entropy identity for dephasing; Pinsker's inequality in bits; and the binary entropy overlap bound. Their precise forms used here are written in P02. The source's invocation is in S8 §3.2, S10 §5, and S5 §§2, 6. These established tools are not claimed as project results. The canonical text includes their application and the full internal measurement/repetition argument, rather than attempting to reprove the general coding theorem or general entropy foundations.

**EXT4–EXT5 — Erasure capacity and the endpoint converse.** C. H. Bennett, D. P. DiVincenzo and J. A. Smolin, *Capacities of Quantum Erasure Channels*, arXiv:quant-ph/9701015; H. Barnum, J. A. Smolin and B. M. Terhal, *The quantum capacity is properly defined without encodings*, arXiv:quant-ph/9711032. These are the supplied all-noise source's references for $Q=Q^{(1)}=\max(0,1-2p)$ at completely random reporting. The endpoint is treated separately from the interior certificate.

## Closest-framework attribution

**EXT2 — Generalized/incomplete erasure.** Vikesh Siddhu and Robert B. Griffiths, *Positivity and nonadditivity of quantum capacities using generalized erasure channels*, arXiv:2003.00583v2. The supplied final comparison identifies its Eq. (35) with the present receiver channel by taking its auxiliary channel to be the noisy classical measurement map and its intact probability to be $1-p$. The channel class and direct-sum structure are inherited, not the proposed new contribution. See S6 §1.

**EXT3 — Dephrasure and repetition thresholds.** Felix Leditzky, Debbie Leung and Graeme Smith, *Dephrasure channel and superadditivity of coherent information*, arXiv:1806.08327. The supplied comparison points to Eq. (15) and Appendix F for the weighted repetition construction and its positivity-threshold behavior. The output structure differs from the present channel, but repetition coding and superadditivity are not new general phenomena. See S6 §2.

**EXT6 — Adjacent entropy-comparison literature.** Christoph Hirche and David Reeb, *Bounds on Information Combining With Quantum Side Information*, arXiv:1706.09752. The supplied all-noise literature record lists this as adjacent comparison material, not a replacement theorem for the certified polynomial inequality. See S11.

## More recent neighboring works in the supplied final comparison

Sujeet Bhalerao and Felix Leditzky, *Improving quantum communication rates with permutation-invariant codes*, arXiv:2508.09978v1, and Hao-Chung Cheng and Mario Berta, *Superadditivity for Entanglement-Assisted Communication*, arXiv:2607.15151v1, are explicitly identified in S6 §4. The source comparison distinguishes structured unassisted code improvements and entanglement-assisted reliability from the current geometric guarantee. That assessment is carried as source-reported context, not newly researched or used as a mathematical premise here.

<a id="s6-correction"></a>
## Correction after the independent audit, 8 September 2026

The historical [S6 comparison](../provenance/text_sources/S6__PRIOR_WORK_COMPARISON.md), §4, overstates the dephrasure result as a threshold improvement. Bhalerao and Leditzky report improved dephrasure communication **rates**, without extending the threshold beyond weighted repetition codes; see [arXiv:2508.09978v1](https://arxiv.org/html/2508.09978v1), §5.2 after Eq. (5.34) and §6.1. Their comparison with neural-network codes is a separate benchmark. Read S6's dephrasure comparison with this correction. The historical S6 bytes are preserved, and the mathematical claims C1–C6 are unaffected.

## Claim boundary

The latest supplied comparison supports the working distinction of a global full-span, all-common-error sufficient condition within known channel theory. It does not certify the absence of every equivalent theorem, unpublished result or alternative formulation. C7 remains an interpretation and priority assessment, separate from C1–C6 and their proof dependencies. The present consolidation does not change that status.

Source IDs resolve to exact archived bytes and section anchors in [SOURCE_TO_CANONICAL.md](SOURCE_TO_CANONICAL.md). Original titles, identifiers and references are preserved in the immutable archive; there is no reliance on an unstated earlier chat or a fresh web claim.
