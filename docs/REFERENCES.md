# References and relation to prior work

The proof uses established channel-coding and entropy results. The comparisons below locate the geometric guarantee within that literature. Source identifiers resolve in [SOURCE_TO_CANONICAL.md](SOURCE_TO_CANONICAL.md).

## Standard results used in the proof

**EXT1 — The coherent-information coding theorem.** Igor Devetak, *The private classical capacity and quantum capacity of a quantum channel*, arXiv:quant-ph/0304127. Used only for the implication from a chosen finite block with positive coherent information to a positive asymptotic unassisted quantum rate. It does not supply an efficient decoder or high-fidelity recovery from the inner repetition block alone. See source S4 and S6 §3.

**Entropy background.** Quantum conditional-entropy concavity under mixing; the relative-entropy identity for dephasing; Pinsker's inequality in bits; and the binary entropy overlap bound. Their precise forms used here are written in P02. See S8 §3.2, S10 §5, and S5 §§2, 6 for their applications in the measurement and repetition arguments.

**EXT4–EXT5 — Erasure capacity and the endpoint converse.** C. H. Bennett, D. P. DiVincenzo and J. A. Smolin, *Capacities of Quantum Erasure Channels*, arXiv:quant-ph/9701015; H. Barnum, J. A. Smolin and B. M. Terhal, *The quantum capacity is properly defined without encodings*, arXiv:quant-ph/9711032. These give the capacity formula $`Q=Q^{(1)}=\max(0,1-2p)`$ at completely random reporting. The endpoint is treated separately from the interior certificate.

## Closest channel frameworks

**EXT2 — Generalized/incomplete erasure.** Vikesh Siddhu and Robert B. Griffiths, *Positivity and nonadditivity of quantum capacities using generalized erasure channels*, arXiv:2003.00583v2. Its Eq. (35) gives the present receiver channel by taking its auxiliary channel to be the noisy classical measurement map and its intact probability to be $`1-p`$. The geometric guarantee applies within this established channel class and direct-sum structure. See S6 §1.

**EXT3 — Dephrasure and repetition thresholds.** Felix Leditzky, Debbie Leung and Graeme Smith, *Dephrasure channel and superadditivity of coherent information*, arXiv:1806.08327. Equation (15) and Appendix F give the weighted repetition construction and its positivity-threshold behavior. The output structure differs from the present channel; repetition coding and superadditivity are established ingredients of both accounts. See S6 §2.

**EXT6 — Adjacent entropy-comparison literature.** Christoph Hirche and David Reeb, *Bounds on Information Combining With Quantum Side Information*, arXiv:1706.09752. This is related entropy-comparison material; the specific polynomial inequality used here has its own certificate. See S11.

## Related coding and communication results

<a id="s6-correction"></a>
**Permutation-invariant codes.** Sujeet Bhalerao and Felix Leditzky, *Improving quantum communication rates with permutation-invariant codes*, arXiv:2508.09978v1, report improved dephrasure communication **rates**, without extending the threshold beyond weighted repetition codes; see [§5.2 after Eq. (5.34) and §6.1](https://arxiv.org/html/2508.09978v1). Their comparison with neural-network codes is a separate benchmark. This rate-versus-threshold distinction is the one used here; the linked [S6 comparison](../provenance/text_sources/S6__PRIOR_WORK_COMPARISON.md), §4, describes it incorrectly as a threshold improvement.

**Entanglement-assisted communication.** Hao-Chung Cheng and Mario Berta, *Superadditivity for Entanglement-Assisted Communication*, arXiv:2607.15151v1, concerns entanglement-assisted reliability. This differs from the unassisted geometric guarantee studied here. See S6 §4.

## Relation to the geometric guarantee

The result here is a global full-span sufficient condition, valid for every common interior reporting error within the stated channel model. Claim C7 records this distinction from the works discussed above. It is a literature assessment, separate from the mathematical claims C1–C6 and their proof dependencies.

[SOURCE_TO_CANONICAL.md](SOURCE_TO_CANONICAL.md) provides exact source files and section anchors for these attributions.
