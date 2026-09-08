# Measurement Geometry Guarantees Coherent-Information Superadditivity

*Destructive measurements with noisy classical records | Scientific argument | 8 September 2026*

**The question.** A destructively measured qubit is no longer available to the receiver, but its classical outcome record may survive. Can the geometry of the possible measurements guarantee quantum communication beyond the globally optimized single-use coherent-information benchmark? The question concerns a specified channel, not whether measurement noise improves quantum capacity.

**The model.** Each input qubit arrives intact with probability $1-p$. Otherwise, it is measured along one of finitely many Bloch axes, selected with positive probabilities, and discarded. The receiver obtains the correct mask and axis label, but the outcome sign is flipped independently with one common probability $0<\epsilon<1/2$. Encoding precedes all random choices. Uses are independent; there is no postselection, feedback, or preshared entanglement. [S1]

**The result.** For every such measurement ensemble spanning all three Bloch directions, and every common error in the open interval above, a nonempty interval of measurement probabilities satisfies

$$
Q^{(1)}(\mathcal N)=\max_\rho I_c(\rho,\mathcal N)=0<Q(\mathcal N).
$$

Here $I_c=S(B)-S(RB)$, with $R$ purifying the input, and $Q$ is asymptotic unassisted quantum capacity. The optimization includes every single-use density matrix. This is a family-wide sufficient guarantee, not an exact capacity formula or a claim that the channel is useless in every single-use task. [S1, S2]

**Why geometry enters.** The proof compares the entropy penalty for every single-use input with the cost achieved by balanced repetitions of two antipodal codewords. The two costs weight the noisy classical records differently. Full span removes a common perpendicular encoding direction; a quantitative entropy inequality then separates the costs strictly. The single-use zero region consequently overlaps a region containing an explicit positive-coherent-information finite block. The coding theorem converts that block into a positive asymptotic rate. The global entropy comparison is computer-assisted; its proof obligations are explicit. [S2; R3]

**One finite witness.** For equally likely $X,Y,Z$ measurements, reporting error $\epsilon=0.10$, and measurement probability $p=0.70$, the optimized single-use quantity is zero. An eight-use balanced repetition input in the $(1,1,1)/\sqrt3$ direction has $I_c/8>7.47\times10^{-5}$ qubits per use. All measured masks and reports, including the all-measured loss, are included. This is an achievable rate through asymptotic outer coding, not a high-fidelity decoder for one eight-qubit block. [S2, S3]

**The controlled limit.** A family of three axes approaching a plane shows the certified separation closing linearly with its weakest directional coverage at fixed interior error. At exact coplanarity, the two optimized threshold costs coincide for this repetition criterion; other codes are not excluded. Perfect records and completely random records also have no zero-one-use/positive-capacity region. Full span therefore guarantees an advantage in principle, not a uniformly large gap, short block, or useful rate. [S2]

**The contribution to test against prior work.** Incomplete-erasure channels, repetition coding, and coherent-information superadditivity are established. The candidate contribution is the geometric guarantee throughout the entire nontrivial common-error range, with a constructive witness and controlled boundary, rather than another isolated nonadditivity example. [R1, R2]

---

**Sources.** S1: supplied theorem statement. S2: supplied `THEORY.md`, Sections 1–7. S3: supplied finite-witness table, eight-use row. R1: Siddhu–Griffiths, arXiv:2003.00583. R2: Leditzky–Leung–Smith, arXiv:1806.08327. R3: Devetak, arXiv:quant-ph/0304127. Full references and source locations accompany the proof map.

**Status.** Source-grounded narrative proposal, not a new proof audit. The final audit of the all-noise extension and the precise priority comparison remain outstanding.
