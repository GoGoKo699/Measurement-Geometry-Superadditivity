# Claim-to-proof map and final audit scope

**8 September 2026 | Noisy-record channel follow-up**

This document fixes the proposed Letter's argument and the evidence required to support it. It does not extend the theorem, run a new simulation, or certify its priority. The latest supplied all-common-noise proof is the scientific basis. The earlier focused audit covers only a narrow common-error band and cannot be treated as an audit of the later global extension. [S1, S2, S4]

## 1. The claim contract

The headline is a **one-way geometric guarantee**. For each finite positive-weight full-span ensemble and each common symmetric reporting error $0<\epsilon<1/2$, there exists a nonempty interval of measurement probabilities. For each $p$ in that interval, the optimized one-use coherent information is zero while some finite block input has positive coherent information. The block length may depend on the ensemble, error, and measurement probability.

The fixed channel is

$$
\mathcal N_{p,\epsilon}(\rho)=(1-p)\rho\ \oplus\ p\sum_{b,s}w_b\,\mathrm{Tr}(E_{b,s}\rho)|b,s\rangle\langle b,s|,
\qquad
E_{b,s}=\frac{I+(-1)^s(1-2\epsilon)\mathbf n_b\cdot\boldsymbol\sigma}{2}.
$$

Axes, probabilities and error are known channel parameters; realized masks, axes and true outcomes are not known to the encoder in advance. The decoder receives the correct mask and axis and only the noisy reported sign. Discarded systems, feedback and preshared entanglement are unavailable. All uses and acquisition errors are independent. The optimization permits otherwise unrestricted noiseless encoding and decoding. [S1, S2, Section 1]

Write $a=(1-2\epsilon)^2$ and $c=1-a$. Define

$$
T=\sum_b w_b\mathbf n_b\mathbf n_b^{\mathsf T},\qquad \lambda=\lambda_{\min}(T).
$$

Let

$$
L=\min_{\|\mathbf u\|=1}\sum_b\frac{w_bc}{\sqrt{1-a(\mathbf n_b\cdot\mathbf u)^2}},
\qquad d_\epsilon=\frac3{35}ca.
$$

The quantitative statement retained for the proof is

$$
\frac1{1+L+d_\epsilon\lambda}\leq p<\frac1{1+L}
\quad\Longrightarrow\quad Q^{(1)}=0<Q,\qquad \lambda>0.
$$

These bounds certify a subinterval, not the exact capacity threshold. The constant is not a headline, nor an optimum. A common error that may take any value is not independently variable per-axis error. [S1]

## 2. Minimal proof dependency

**Single-use side.** Parameterize every mixed qubit input by its smaller eigenvalue $0<t\leq1/2$ and direction $\mathbf u$. If $C(t,\mathbf u)$ is the conditional-reference entropy after the noisy record in the measured branch, define

$$
\Gamma=\inf_{t,\mathbf u}\frac{C(t,\mathbf u)}{h_2(t)}.
$$

The exact flagged-channel identity is $I_c=(1-p)h_2(t)-pC(t,\mathbf u)$. Since pure inputs give zero, $p\geq1/(1+\Gamma)$ implies the global optimum is exactly zero. Neither symmetry nor a nearly pure expansion alone proves this assertion. [S2, Section 2]

**Collective side.** Balanced antipodal repetition inputs have positive coherent information for sufficiently large finite length if $p<1/(1+L)$. The inherited proof sums every record and bounds competing terms by exponential factors with polynomial corrections. A chosen positive finite block yields a positive asymptotic rate by outer coding. It is not necessary that the inner-block rate have a positive limit as its length grows. [S2, Sections 1 and 9; S5; R3]

**The bridge.** The all-noise scalar inequality and the geometric comparison give

$$
\Gamma\geq L+d_\epsilon\lambda.
$$

This is where full span supplies strict separation. The overlap of the two bounds proves the headline. The finite witness illustrates this implication; it does not prove the universal statement. The cone family explains its boundary; it is not required for the existence proof. [S2, Sections 3–6]

## 3. Claim ledger

| ID | Claim and its role | Exact source dependency | Final check required |
|---|---|---|---|
| C1 | Full span gives a nonempty $Q^{(1)}=0<Q$ interval at every common interior error. The headline theorem. | S1; S2 Sections 2–4; inherited repetition bound S5; R3. | Audit both threshold implications, the global bridge, and quantifier order. |
| C2 | The one-use upper bound covers every qubit density matrix. Necessary protection against a weak baseline. | S2 Section 2, scalar inequality in Section 3, mixed-input control in Section 8. | Reconstruct the receiver/reference state using noisy rather than true outcomes; include all weights and directions and the pure endpoint. |
| C3 | The collective construction includes every branch and supplies a positive finite-block rate. Constructive half of C1. | S5 exact record sum and polynomial bounds, inherited into S2. | Check the all-measured subtraction, constants independent of block length, fixed encoder direction, and correct outer-coding interpretation. |
| C4 | The geometry separates the global one-use cost from the repetition cost. Explanation of the family-wide result. | S2 Section 3 entropy comparison and Section 4 frame inequalities. | Independently audit the new polynomial inequality, analytic tails, complete interval cover, and the use of common error in summing axis costs. |
| C5 | Eight uses suffice for a particular equal-Pauli witness at $(p,\epsilon)=(0.70,0.10)$. One concrete example. | S2 Section 7; S3; saved second-backend witness enclosure. | Check both global one-use zero and block positivity at the same parameters; retain unfavorable branches and per-use normalization. |
| C6 | The cone family closes the separation at the planar boundary; the two noise endpoints have no such gap. Controlled limits. | S2 Sections 5–6. | Distinguish exact one-use and construction thresholds from optimal capacity. For all-error exact cone formulas keep $0\leq\lambda\leq1/4$. |
| C7 | The geometric all-noise guarantee is a distinctive contribution beyond the nearest literature. Significance claim, not a mathematical consequence. | S2 Section 9; R1–R2 and their relevant prior references. | Equation-level priority comparison. No absence-of-keyword result is sufficient. |

C1–C6 have author-side derivations or numerical certificates in the supplied source. This pass records that support; it does not newly recertify those proofs. C7 remains unresolved. External specialist review remains distinct from author-side checking.

## 4. The bounded final audit

### A. Verify the information available to the receiver

Derive the channel and conditional-reference entropy from hidden projective outcomes followed by classical sign noise. Independently recover the effective effects $E_{b,s}$ and the flagged coherent-information identity. Check that the decoder never receives the hidden true sign, the discarded qubit, or a flag distinguishing acquisition-error events. Confirm that negative all-measured contributions are not removed. **Closes:** C2 and the model dependence of C3. **Deliverable:** a short density-matrix derivation and one physical-branch cross-check, not another large simulation.

### B. Audit the new global entropy inequality

The specific new obligation is

$$
(1-\ell)C_0(t)+(\ell-c)C_1(t)\geq \ell a h_2(t),
\qquad
\ell=c\left(1+\frac a4+\frac{a^2}4+\frac{a^3}{10}\right).
$$

Review the analytical low-error and high-error arguments, every nearly pure input tail, and the compact-domain certificate. Verify the tangent/secant directions, normalization by $ca$, monotonic envelopes over an entire noise band, exact-rational coverage, and outward rounding. The declared cover has 512 noise bands and 29,635 input intervals; checking counts is not proof of coverage. Verify the reuse of one common coefficient across measurement axes. The earlier narrow-band audit does not close this obligation. **Closes:** the new part of C4. **Deliverable:** an independently justified inequality with a complete certificate record, or an explicitly narrowed claim if a defect is found.

### C. Check the geometric and coding implications

From the entropy lemma, recover $\Gamma\geq\min\{G_{\min},\ell\}$. Verify both $G_{\min}\geq L+ca\lambda/2$ and $\ell>L+ca/35$. Use $\lambda\leq1/3$. Separately inspect the inherited all-record repetition proof and the coding theorem application. Check that positivity holds at a finite inner length for each fixed channel in the interval, without asserting a uniform length or exchanging incompatible limits. **Closes:** C1, C3 and the geometric part of C4.

### D. Audit only the retained illustration and limits

Recompute the eight-use witness against its global one-use bound at exactly $p=7/10,\epsilon=1/10$, and the body-diagonal balanced input. For the cone family, verify the exact formula in the all-error domain $0\leq\lambda\leq1/4$ and the small-$\lambda$ expansion. Check the endpoint record models. Do not replace either threshold by an exact all-code boundary. **Closes:** C5–C6. More block lengths, error grids, and channels are outside this audit.

### E. Establish the contribution relative to the closest theory

Compare the receiver channel, not merely a complementary-channel name, with R1's incomplete-erasure construction. Compare R2's single-letter and repetition positivity results with the actual global-input and full-span statements. Classify each ingredient as inherited, specialized, or new; inspect whether the all-noise geometry statement follows from an existing general result. **Closes:** C7 only if a defensible distinction is obtained. Reopening three primary records for this planning document is not an exhaustive priority audit.

**Stopping rule.** When A–E support the stated claims and one standalone source package reproduces the required certificates and retained witness, stop expanding the science and draft the Letter. Neither improved constants nor heterogeneous noise is required. External review may add assurance but has not already happened. A discovered proof or priority problem changes the claim; it is not solved by stronger wording.

## 5. What the reader sees, and what stays in the supplement

The main text contains one physical model, one sufficient geometric theorem, its short two-cost proof route, one finite witness, and one controlled limiting family. It states that a scalar entropy inequality is computer-assisted. The supplement contains the full inequality, analytic tails, covering specification, interval verifiers, branch accounting and additional controls. The code repository preserves the complete calculation and provenance.

A proposed three-figure plan is sufficient. **Figure 1:** channel operation and the eight-use witness, answering what is transmitted and what the separation means. **Figure 2:** the theorem's geometric condition and certified subinterval, answering why the effect is systematic. **Figure 3:** the cone family approaching a plane, answering how the guarantee becomes arbitrarily weak. Shaded regions must be labeled certified, not exact capacity phases. These are roles for future figures; none is generated in this pass. Merge panels if they repeat the same point.

Keep out of the Letter's main argument: the earlier many-body response study; the optimization, routing and memory screens; historical noise-band generalizations; long lists of tiny positive rates; benchmark ratios against a nearly zero quantity; and verification-volume statistics. Those records may be preserved without determining the reader's route.

Wording boundaries are fixed. Use “optimized single-use coherent information,” not “single-use capacity.” Use “full span guarantees,” not “full span is necessary for all collective gains.” Do not claim that adding noise improves capacity. A small positive inner-block coherent information is not an efficient decoder or a large practical rate. The open error interval and common symmetric acquisition-error assumption belong next to the theorem.

## 6. Source register and current status

**S1–S3.** The supplied all-common-noise theorem, proof, and finite-witness records are copied unchanged into `sources/current/`. The proof sections needed are 1–4 (central theorem), 5–6 (limits), 7 (witness), and 9 (dependencies). **S4.** The earlier narrow-band audit is copied as `sources/PRIOR_NARROW_BAND_AUDIT.md`. **S5.** The inherited all-record repetition derivation remains in the original archive's `source/full_span_audit/` tree; its general-axis statement is in `record_geometry_criterion/THEORY.md`, Section 3. These short source snapshots do not replace the complete proof-reproduction archive.

**R1.** Siddhu–Griffiths, generalized-erasure channels, arXiv:2003.00583. **R2.** Leditzky–Leung–Smith, dephrasure superadditivity, arXiv:1806.08327. **R3.** Devetak, quantum coding theorem, arXiv:quant-ph/0304127. Full references and clickable primary records are in `REFERENCES.md`. Reopening these three records is not an exhaustive priority audit.

**Checks in this pass.** The source ZIP and all 139 internal manifest entries match their hashes. Exact rational arithmetic confirms the retained witness's sufficient one-use zero threshold $59/86<7/10$; its stored enclosure exceeds the safely rounded $7.47\times10^{-5}$. The block value and global certificate were not rerun. File identities and document checks are in `verification/`.

**Status.** This is a source-grounded argument and audit specification, not a new theorem audit or self-contained theorem-reproduction package. No repository, manuscript, or accepted figure was modified. The final all-noise proof audit and precise priority comparison remain outstanding.
