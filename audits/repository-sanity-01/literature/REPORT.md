# Primary-literature and attribution audit

Audit date: 8 September 2026. Repository baseline: `f0015c56a19fd953c6797b2c64d9b507105234e3`.

This report checks attribution and the scope of the published results used or compared in the baseline. It is not a manuscript and does not determine the validity of the repository's computer-assisted lemma. No repository source was edited. Searches used public author names, paper identifiers and generic subject terms; private repository content was not submitted to a search service.

## Outcome

The channel-framework identification and coding-theorem attribution are correct. The distinction between the repository's unassisted capacity claim and entanglement-assisted reliability work is supported at theorem level. The cited entropy-comparison literature addresses a different information-combining problem and supplies no identified substitute for P4.1. The stated candidate contribution remains the global, all-common-error full-span comparison, conditional on its internal proof passing the scientific audit. This is a bounded distinction from inspected works, not an absolute-priority certificate.

One low-severity attribution error was found in a preserved historical comparison: it attributes a dephrasure threshold improvement to a paper that reports improved rates without an observed threshold improvement. The current short REFERENCES entry does not repeat that error. No central mathematical claim depends on it.

## Evidence ledger

Equation numbers below are from the PDF unless explicitly labeled HTML. Public links are retrieval paths for reproduction, not claims that the papers' entire proofs were independently reverified.

### L1. Established incomplete-erasure framework

Vikesh Siddhu and Robert B. Griffiths, *Positivity and nonadditivity of quantum capacities using generalized erasure channels*, arXiv:2003.00583v2.

PDF: <https://arxiv.org/pdf/2003.00583v2>. HTML: <https://arxiv.org/html/2003.00583v2>.

Section IV, Eq. (35), is `C_g(A)=(1−λ)C_1(A) ⊕ λA`. Taking `λ=1−p` and `C_1` equal to the repository's reported-outcome quantum-to-classical map reproduces M01 exactly, up to block order. Section III, Eq. (25), gives the weighted coherent-information identity when both outputs have the required orthogonal block structure. This supports the flag-entropy cancellation used in P01.

Sections V.A–C analyze amplitude-damping and dephasing channel pairs. Their incomplete-erasure examples yield positive single-letter coherent information through entropy singularities. Those evaluated examples do not establish a global zero-single-letter region for every full-span noisy measurement frame. The general formula still requires the repository's entropy comparison and geometric argument. The baseline's attribution in REFERENCES EXT2 and S6 §1 is accurate.

Retrieval refs: `turn149349view0`, `turn149349view1`, `turn149349view2`; HTML initial ref `turn899591view0`.

### L2. Established repetition construction and construction-specific thresholds

Felix Leditzky, Debbie Leung and Graeme Smith, *Dephrasure channel and superadditivity of coherent information*, arXiv:1806.08327v3; Physical Review Letters 121, 160501 (2018).

PDF: <https://arxiv.org/pdf/1806.08327v3>. HTML: <https://arxiv.org/html/1806.08327v3>.

The dephrasure channel applies dephasing in its nonerased quantum branch and sends an input-independent flag in its erased branch. PDF Eq. (13) defines the weighted repetition mixture; Eq. (15) evaluates its coherent information. Appendix F proves its optimized-weight positivity threshold coincides with the single-letter threshold for every finite repetition length. This is not a no-go theorem for other codes.

The repository uses the same established antipodal repetition form after a basis rotation, with balanced weight, but its channel retains input-dependent classical records and has intact surviving qubits. Its all-record entropy sum and full-span separation require additional reasoning. Attribution is accurate.

An apparent citation-number problem was investigated and rejected: arXiv's experimental HTML renumbers the repetition state and formula as (17) and (19). The repository's Eq. (15) locator is correct in the PDF. Do not “fix” it based on the HTML conversion alone.

Retrieval refs: `turn667015view0` (PDF equation), `turn874862view7` (HTML state/formula), `turn149938view1` (Appendix F).

### L3. Positive finite inner block to asymptotic unassisted quantum rate

Igor Devetak, *The private classical capacity and quantum capacity of a quantum channel*, arXiv:quant-ph/0304127v6; IEEE Transactions on Information Theory 51, 44–55 (2005).

PDF: <https://arxiv.org/pdf/quant-ph/0304127>.

Theorem 5, Eq. (36), gives regularized coherent information for entanglement generation; Proposition 7, Eq. (53), identifies this with quantum transmission capacity. The direct part explicitly obtains the regularized statement by additional blocking. Thus once one fixed finite block has `I_c>0`, using the block as a superchannel and dividing its achievable rate by its length supports P10. No positive limit of the chosen inner repetition rate as its length diverges is required. This source does not confer high single-block fidelity or an efficient decoder on the inner construction. REFERENCES EXT1 and S6 §3 use it within those bounds.

Retrieval refs: `turn170889view7`, `turn149938view8`.

### L4. Completely random reporting endpoint

C. H. Bennett, D. P. DiVincenzo and J. A. Smolin, *Capacities of Quantum Erasure Channels*, arXiv:quant-ph/9701015v2; Physical Review Letters 78, 3217–3220 (1997).

PDF: <https://arxiv.org/pdf/quant-ph/9701015>.

Eq. (2) states `Q=max(0,1−2p)` for qubit erasure probability `p`; the later discussion identifies the corresponding maximum coherent information. At reporting error one half, the repository's measured record is input independent. Appending or discarding such independently generated flags preserves capacity, so P11.3 makes the correct reduction. The pure/noisy record endpoints are separated from formulas with vanishing denominators.

Retrieval ref: `turn149938view6`.

### L5. Correct erasure converse and encoding scope

H. Barnum, J. A. Smolin and B. M. Terhal, *The quantum capacity is properly defined without encodings*, arXiv:quant-ph/9711032v2; Physical Review A 58, 3496 (1998).

PDF: <https://arxiv.org/pdf/quant-ph/9711032>.

Section III supplies the erasure upper bound without the continuity assumption used by an earlier presentation; Eqs. (45)–(48) relate unrestricted capacity to regularized coherent information and write the erasure entropy sum. Including this source alongside Bennett–DiVincenzo–Smolin is appropriate. No unsupported restriction to unencoded transmission is inherited by the repository's endpoint argument.

Retrieval ref: `turn149938view7`.

### L6. Adjacent entropy comparison, not a substitute proof

Christoph Hirche and David Reeb, *Bounds on Information Combining With Quantum Side Information*, arXiv:1706.09752.

PDF: <https://arxiv.org/pdf/1706.09752>.

Theorems VI.1 and VI.3 concern the conditional entropy of the XOR of independent uniform classical bits with quantum side information. Theorem V.3 bounds the fidelity parameter in terms of channel entropy. Their Eq. (65) is an entropy-combining bound, with different variables and optimization from the single-axis conditional-reference cost in repository P03–P04. No equation-level identification with P4.1 was found in the inspected statements. Thus EXT6's limited “adjacent comparison” role is accurate. In particular, the repository cannot count this paper as external verification of its polynomial `P(a)` or full-domain scalar inequality. Natural-log formulas in this source must be converted before a numerical comparison in bits.

Retrieval refs: `turn927159view5`, `turn149938view5`.

### L7. Recent structured-code work

Sujeet Bhalerao and Felix Leditzky, *Improving quantum communication rates with permutation-invariant codes*, arXiv:2508.09978v1.

HTML: <https://arxiv.org/html/2508.09978v1>.

Eq. (4.7) contains the repository's balanced repetition input; Theorems 4.1 and 4.3 provide structured coherent-information evaluation. Section 5.2, Eq. (5.30), studies dephrasure. These support precedent for separable correlated inputs, without implying the repository's global entropy lower bound. Finding ATTR-01 records a distinction concerning §5.2 after Eq. (5.34). The canonical REFERENCES entry's general description of code improvements is supported.

Retrieval refs: `turn778429view6`, `turn667015view3`.

### L8. Recent measurement-channel result with a different operational quantity

Hao-Chung Cheng and Mario Berta, *Superadditivity for Entanglement-Assisted Communication*, arXiv:2607.15151v1.

HTML: <https://arxiv.org/html/2607.15151v1>.

Theorem 3 and Appendix C, Theorem C.3, prove strict two-copy Petz–Rényi information superadditivity for a Fourier-measurement family with input dimension at least three and Rényi order below one. Eqs. (12)–(15) connect this quantity to an entanglement-assisted random-coding error-exponent bound. Entanglement-assisted capacity at order one remains additive. The correlated input marginal can be separable.

Consequently S6 §4 correctly distinguishes the result from qubit unassisted quantum-capacity positivity. Neither measurement channels nor separability of average input alone support a novelty claim for this repository. This audit checked the external theorem's scope and defining formulas, not its entire proof.

Retrieval refs: `turn431631view0`, `turn844410view0`.

### L9. Additional nearby positivity mechanism

Vikesh Siddhu, *Entropic singularities give rise to quantum transmission*, arXiv:2003.10367; Nature Communications 12, 5750 (2021).

PDF: <https://arxiv.org/pdf/2003.10367>.

Theorem 1 gives a sufficient dimension/rank condition for positive single-letter coherent information near a pure input. Appendix D.2 applies it to incomplete-erasure channels whose auxiliary map is a zero-capacity qubit channel with a qubit environment. The noisy multi-axis classical-output map in the repository is not that restricted auxiliary family. This work explains why nearly pure inputs are a substantive optimization risk; it supplies no global single-letter-zero theorem for the present model. Its omission from the short reference record is an optional contextual improvement, not a failed proof dependency.

Retrieval refs: `turn431631view1`, `turn844410view1`.

### L10. Additional information-combining development

Christoph Hirche, Xinyue Guan and Marco Tomamichel, *Chain Rules for Rényi Information Combining*, arXiv:2305.02589v1.

PDF: <https://arxiv.org/pdf/2305.02589>.

The introduction and Theorems III.2–III.3 concern conditional Rényi chain rules and BSC/BEC information-combining bounds. The described quantum generalization addresses complementary check/variable-node quantities. It does not state the repository's scalar polynomial comparison or measurement-frame theorem. This is an additional bounded check of the adjacent entropy line, not exhaustive coverage of that literature.

Retrieval refs: `turn431631view2`, `turn844410view3`.

## Finding ATTR-01

- **Severity:** low. **Confidence:** high.
- **Category:** inaccurate attribution in a preserved historical source; current reader-facing priority evidence inherits a narrow documentary discrepancy.
- **Location:** `provenance/text_sources/S6__PRIOR_WORK_COMPARISON.md:29`, §4. This source is invoked by `docs/REFERENCES.md:23`, M07's C7 entry and P15.
- **Problem:** S6 attributes threshold improvements to several families “including dephrasure.” The source reports dephrasure rate improvement and explicitly stops short of threshold improvement.
- **Reproduction:** open L7 §5.2 and inspect the paragraph after Eq. (5.34). It says the permutation-invariant ansatz improves noisy-regime rates but “does not seem to increase the known thresholds of this channel.” Compare with S6 line 29. The 11-word quoted clause here is the only direct quotation from that public source in this report.
- **Affected task:** accurate comparison with recent structured-code work, C7's historical supporting account. C1–C6 and the witness are unaffected; `docs/REFERENCES.md` itself uses the more accurate general “code improvements” wording.
- **Smallest correction:** add a current comparison note stating that this paper improves thresholds for some other families and rates for dephrasure. Preserve the archived S6 bytes; do not rewrite provenance or suggest its whole comparison failed.
- **Before manuscript preparation:** carry the corrected rate/threshold distinction into the eventual attribution account. No additional numerical experiment or new code family is required.

## Search and access log

Public primary records were fetched directly through the search service on 8 September 2026. Searches used the cited paper identifiers/authors and generic phrases including “incomplete erasure channel,” “quantum Mrs. Gerber,” “information combining,” “measurement channels quantum capacity superadditivity.” Both available search engines were used; recent-work queries included a two-year filter. Search results were discovery aids only. Claims above rely on primary PDF/HTML statements rather than aggregators.

All eight cited works were inspected at a relevant equation/theorem/section level. Two additional nearby papers were inspected as L9–L10. Shor–Smolin arXiv:quant-ph/9604006 was opened for broader code-history context, but no additional claim or mandatory citation is inferred from that preliminary read.

Access limitations were presentation-specific: arXiv HTML for 2003.10367v3 and an attempted 2305.02589v2 returned errors; unversioned PDF access succeeded. The Nature landing page returned an error; the author's arXiv paper supplied the necessary content. A requested web screenshot of dephrasure PDF page 4 failed because screenshot capability was unavailable. Its searchable PDF text successfully resolved Eq. (15). No visual claim about external figures is based on that failed screenshot.

Some generated arXiv HTML equations differ in numbering from the PDFs. The dephrasure Eq. (15) discrepancy was checked against the PDF and rejected as a repository finding. Full URLs were used for later retrieval because several combined ref-ID lookups resolved unexpectedly to earlier opened papers; none of those misresolved returns was accepted as evidence for a different work.

## Stopping assessment

Independently established here: the exact incomplete-erasure substitution, correct external coding-theorem application, endpoint reference suitability, and the stated distinctions from the inspected repetition, entropy-combining, structured-code and entanglement-assisted works. These are comparisons of definitions and theorem scope, not reproofs of the external coding theorem or of every cited paper.

Remaining unverified: exhaustive priority, unpublished equivalents, and validity of the internal analytical/certificate proof, which are not established by this literature component. Search failure is not evidence of novelty. Subject to the other audit components, no further bounded scientific task is required solely by attribution. ATTR-01 needs a small documentary correction before use in a manuscript account.
