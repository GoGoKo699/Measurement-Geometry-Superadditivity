# Thirty milestones for the scientific argument

[Learning route](README.md) · [Selected Preskill bridge](preskill-bridge.md) · [Scientific account](../science/README.md)

These **30 project-defined milestones** connect local concepts to the complete result. Phase I contains 12 background and preliminary milestones; Phase II contains 18 milestones for the project's narrative and innovation. Their dependencies describe the scientific structure and do not presume a particular reader's previous training.

Each milestone states a central question and the understanding it contributes. Together they cover the whole story, while the linked proofs retain its detailed derivations. Learning milestones M01–M30 are distinct from **model units** M01–M08. References below identify model units explicitly; P01–P15 denote proof units and C1–C7 denote scientific claims.

## Phase I: Background and preliminaries

<a id="m01"></a>
### M01. Qubit states and Bloch directions

**Central question:** How can every qubit input be described without guessing its orientation or purity?

**Understanding target:** Express a qubit density matrix through a unit Bloch direction and its smaller eigenvalue $`t\in[0,1/2]`$. Identify the antipodal eigenstates, the pure-input limit, and the direction-independent maximally mixed state. This parameterization must cover every density matrix that will enter the single-use optimization.

**Dependencies:** None within this map. **Connection:** A local state description becomes the domain of a global optimization in M08 and M14.

**Sources:** [Model M02](../science/model.md#m02), [model M03 and proof P01](../science/single-use.md), and the [notation crosswalk](../science/notation.md).

<a id="m02"></a>
### M02. Entropy of a qubit and a subnormalized state

**Central question:** How do eigenvalues become the entropy costs that the proof compares?

**Understanding target:** Relate the input entropy to binary entropy $`h_2(t)`$. Recover a positive two-dimensional state's eigenvalues from its trace and determinant, and interpret its homogeneous entropy as its probability times the entropy after normalization. Keep information entropies in bits and analytic logarithms in their stated natural-log convention.

**Dependencies:** [M01](#m01). **Connection:** Conditional-reference calculations in M14 use precisely these weighted entropies.

**Sources:** Preskill [§10.1 and optional entropy refreshers](preskill-bridge.md#optional-refreshers); [model M02](../science/model.md#m02); [P01, homogeneous entropy](../science/single-use.md#p01).

<a id="m03"></a>
### M03. Measurement effects and imperfect classical reports

**Central question:** Which measurement effect describes an observed sign when the true sign is hidden?

**Understanding target:** Form a noisy reported-outcome effect by averaging the true projectors with their classical reporting probabilities. Distinguish the normalization of the two effects for a fixed axis from the probabilities selecting the axes. Identify the observable record and the inaccessible information in a measurement model.

**Dependencies:** [M01](#m01). **Connection:** Classical processing of a record changes the conditional quantum state even after the measured qubit is gone.

**Sources:** Preskill [§10.2.2](preskill-bridge.md#optional-refreshers); [model M01](../science/model.md#m01); [P01, hidden-outcome averaging](../science/single-use.md#p01).

<a id="m04"></a>
### M04. Reference purification and receiver access

**Central question:** Why must quantum transmission be evaluated with a reference system?

**Understanding target:** Purify the chosen input and follow the reference without sending it through the channel. For a pure reference–receiver–environment dilation, explain why the joint reference–receiver entropy equals the environment entropy. Preserve the distinction between an accessible classical flag and an inaccessible environment register.

**Dependencies:** [M01](#m01), [M02](#m02), [M03](#m03). **Connection:** The reference exposes coherence and correlations absent from the receiver marginal alone.

**Sources:** Preskill [§§10.7.1–10.7.2](preskill-bridge.md#reading-map) and [§10.2.1](preskill-bridge.md#optional-refreshers); [model M02](../science/model.md#m02); [P01](../science/single-use.md#p01).

<a id="m05"></a>
### M05. Orthogonal flags and conditional entropy

**Central question:** How do classical records contribute to an entropy difference?

**Understanding target:** Decompose the entropy of a state with orthogonal classical flags into the record's Shannon entropy plus the averaged conditional entropy. Explain why the record entropy cancels when the same accessible flags occur in both terms of coherent information. The remaining average still includes every record with its physical probability.

**Dependencies:** [M02](#m02), [M03](#m03), [M04](#m04). **Connection:** The same cancellation underlies both the one-use cost and the block formula, without selecting favorable branches.

**Sources:** [P01, flagged identity (P1.1)](../science/single-use.md#p01); [P02, conditional-entropy tools](../science/entropy-tools.md#p02); Preskill [§10.2](preskill-bridge.md#optional-refreshers).

<a id="m06"></a>
### M06. Entropy tools for coherence and mixing

**Central question:** Which standard inequalities control the loss or survival of coherence?

**Understanding target:** Interpret dephasing as an entropy increase, use the relative-entropy identity and Pinsker's inequality in bits to obtain a lower coherence bound, and identify the binary-entropy overlap bound. Distinguish concavity under affine mixing from any separate curvature statement after a nonlinear change of variable.

**Dependencies:** [M02](#m02), [M04](#m04), [M05](#m05). **Connection:** These tools support the scalar secants and the repetition envelopes through different arguments.

**Sources:** [P02 and its attributions](../science/entropy-tools.md#p02); Preskill [§§10.2.3–10.2.4](preskill-bridge.md#optional-refreshers); [imported entropy ingredients](../references/README.md).

<a id="m07"></a>
### M07. Measurement frames and weakest directional coverage

**Central question:** How does a finite set of weighted axes become a geometric quantity?

**Understanding target:** Form $`T=\sum_b w_b\mathbf n_b\mathbf n_b^{\mathsf T}`$ and interpret its Rayleigh quotient as the weighted squared projection onto a direction. Explain its unit trace, the range $`0\leq\lambda\leq1/3`$, and why positive smallest eigenvalue is equivalent to full supported span. Two noncommuting axes can still leave a common perpendicular direction.

**Dependencies:** [M01](#m01), [M03](#m03). **Connection:** This original geometry bridge supplies the quantity that later controls both threshold separation and its closing near rank deficiency.

**Sources:** [Model M03](../science/single-use.md#m03), [P08](../science/geometric-gap.md#p08), and [P11.1](../science/limiting-geometries.md#p11).

<a id="m08"></a>
### M08. Optimized coherent information and asymptotic capacity

**Central question:** What exactly does the single-use benchmark optimize?

**Understanding target:** Distinguish a coherent-information value for one chosen state from its maximum over all one-use inputs, and distinguish that optimized quantity from asymptotic unassisted capacity. Explain why a zero optimized value requires a bound on every mixed input when pure inputs attain zero. Translate Preskill's $`Q_1`$ into the project's $`Q^{(1)}`$ without importing an operational finite-error one-shot definition.

**Dependencies:** [M01](#m01), [M04](#m04), [M05](#m05). **Connection:** An optimization over states and a coding limit answer different questions.

**Sources:** Preskill [§10.7.1 and notation crosswalk](preskill-bridge.md#notation); [model M02](../science/model.md#m02); [P01](../science/single-use.md#p01).

<a id="m09"></a>
### M09. Coherent code subspaces and correlated marginals

**Central question:** How can a repetition code carry an unknown qubit without cloning it?

**Understanding target:** Apply an isometry to a logical orthonormal basis and extend it linearly to superpositions. Distinguish that coherent encoding map, its entangled reference purification, and its separable but correlated balanced input marginal. A mixed test state can certify a quantum coding advantage because its purification retains the logical correlations.

**Dependencies:** [M01](#m01), [M04](#m04), [M08](#m08). **Connection:** The repetition construction's physical meaning depends on the code subspace, not only on its average density matrix.

**Sources:** Preskill [§10.7.4](preskill-bridge.md#reading-map); [P09.1](../science/repetition-coding.md#p09).

<a id="m10"></a>
### M10. Exponential rates and polynomial prefactors

**Central question:** When can asymptotic bounds determine the sign of a finite-block quantity?

**Understanding target:** Explain why a strict inequality between positive exponential bases eventually dominates fixed polynomial prefactors. Keep all parameters defining those prefactors fixed as the block length grows. Recognize that equal bases need further analysis and that eventual sign does not classify every shorter block.

**Dependencies:** [M08](#m08), [M09](#m09). **Connection:** This comparison produces a construction frontier while retaining a finite inner block for the capacity argument.

**Sources:** [P09.4, polynomial envelopes](../science/repetition-coding.md#p09); [P10, exponential comparison](../science/repetition-coding.md#p10).

<a id="m11"></a>
### M11. A certificate for a continuous domain

**Central question:** What makes a finite computer calculation support an inequality on a continuum?

**Understanding target:** Distinguish evaluations at sampled points from outward interval enclosures on complete rectangles. Explain exact-rational coverage, analytical tails, safe secant and tangent bounds, and rejection of incomplete covers. Separate the preserved certificate input, the algorithms that verify it, and their recorded outputs.

**Dependencies:** [M02](#m02), [M06](#m06). **Connection:** Finite verification supports a global entropy claim only through the stated domain and enclosure argument.

**Sources:** [P07](../science/scalar-inequality.md#p07), [P14](../science/proof-map.md#p14), and [verification scope](../verification/README.md).

<a id="m12"></a>
### M12. From a finite block to an unassisted quantum rate

**Central question:** What operational conclusion follows from a positive block coherent information?

**Understanding target:** First fix a finite inner block with positive coherent information, then apply the coding theorem to many independent uses of that block channel. Normalize the achievable rate by physical uses. Explain why this argument neither provides high-fidelity recovery from the inner block alone nor requires a positive limiting inner-block rate as its length tends to infinity.

**Dependencies:** [M08](#m08), [M09](#m09), [M10](#m10). **Connection:** The information quantity acquires its transmission meaning through a distinct outer-coding limit.

**Sources:** Preskill [§10.9.4 statement and edition note](preskill-bridge.md#edition-note); [P10](../science/repetition-coding.md#p10); [the coherent-information coding theorem's attribution](../references/README.md).

## Phase II: Narrative and innovation

<a id="m13"></a>
### M13. The channel and its operation budget

**Central question:** What physical communication task does this theorem actually describe?

**Understanding target:** Specify intact transmission versus destructive measurement; the finite known axis ensemble; the common symmetric error $`0\lt\epsilon\lt1/2`$; independent uses; and the receiver's surviving qubits, masks, labels, and reported signs. State that encoding precedes all realized random choices and that encoding and decoding gates are otherwise unrestricted and noiseless. Keep postselection, feedback, preshared entanglement, and access to discarded systems outside the model.

**Dependencies:** [M03](#m03), [M04](#m04), [M05](#m05), [M08](#m08). **Connection:** These access rules determine the entropy calculation and the theorem's physical scope.

**Sources:** [Model M01](../science/model.md#m01), [P01](../science/single-use.md#p01), and [incomplete-erasure attribution](../references/README.md).

<a id="m14"></a>
### M14. Exact reported-reference cost and the one-use threshold

**Central question:** How does the physical channel give an exact criterion for zero optimized one-use coherent information?

**Understanding target:** Derive the conditional reference blocks from the noisy reported effects, including the purification-basis transpose. Use their trace and determinant to obtain $`C(t,\mathbf u)`$ and the identity $`I_c=(1-p)h_2(t)-pC(t,\mathbf u)`$. Define the global infimum $`\Gamma`$ over every mixed input and prove $`Q^{(1)}=0`$ exactly when $`p\geq p_1=1/(1+\Gamma)`$, including the pure-input and infimum issues.

**Dependencies:** [M01](#m01), [M02](#m02), [M05](#m05), [M08](#m08), [M13](#m13). **Connection:** The threshold identity is exact even when a later estimate of $`\Gamma`$ is conservative.

**Sources:** [Model M03 and P01](../science/single-use.md).

<a id="m15"></a>
### M15. Why nearly pure inputs do not settle the optimization

**Central question:** What can the nearly pure directional limit establish about the global cost?

**Understanding target:** Derive the cost $`G(\mathbf u)`$ as $`t\downarrow0`$ and retain only the general implication $`\Gamma\leq G_{\min}`$. Explain the equal-Pauli control at $`\epsilon=1/5`$, where a mixed input is positive at the threshold inferred from $`G_{\min}`$. An equality claim therefore needs a separate matching lower bound.

**Dependencies:** [M07](#m07), [M08](#m08), [M14](#m14). **Connection:** This distinction remains essential in the eight-use proof and the universal linear-closure argument.

**Sources:** [P01, nearly pure ratio](../science/single-use.md#p01); [P13.4, global-optimization control](../science/eight-use-witness.md#p134).

<a id="m16"></a>
### M16. Entropy curvature and the endpoint chord

**Central question:** Which change of variable exposes a useful lower bound for every measurement direction?

**Understanding target:** Derive the integral formula for homogeneous entropy and pair the two reported signs. Explain why the cost is increasing and convex in squared projection $`x`$ but concave in the transformed variable $`g=c/(1-ax)`$. Use that concavity to build the chord between perpendicular and parallel costs; the two curvature statements concern different variables and serve different steps.

**Dependencies:** [M02](#m02), [M06](#m06), [M14](#m14), [M15](#m15). **Connection:** A single-axis directional problem becomes a scalar comparison that can be averaged over the ensemble.

**Sources:** [P03](../science/entropy-tools.md#p03), with [notation translations](../science/notation.md).

<a id="m17"></a>
### M17. The common-error scalar comparison

**Central question:** How does one scalar inequality yield a lower bound on the globally optimized cost?

**Understanding target:** Identify the polynomial choice $`\ell=cP(a)`$, the scalar deficit $`\mathscr D(t,c)`$, and the required inequality over all interior errors and all input weights. Combine it with the endpoint chord to obtain $`\Gamma\geq\min\{G_{\min},\ell\}`$. Locate the precise use of common reporting error: the same coefficient $`\beta(t,\epsilon)`$ must apply to every axis before the weighted average.

**Dependencies:** [M13](#m13), [M15](#m15), [M16](#m16). **Connection:** This is the global input bound needed before geometry can separate the thresholds.

**Sources:** [P04](../science/scalar-inequality.md#p04) and [P03.3](../science/entropy-tools.md#p03).

<a id="m18"></a>
### M18. Analytical noise endpoints and nearly pure tails

**Central question:** How is the scalar comparison controlled arbitrarily close to singular limits?

**Understanding target:** Follow the low-noise argument for $`0\lt c\leq2^{-28}`$ and the high-noise argument for $`0\lt a\leq1/25`$. Explain the input-weight split, the exact rational constants, and how arbitrarily nearly pure inputs are covered. Treat the pure-input equality separately from expressions divided by a vanishing entropy.

**Dependencies:** [M02](#m02), [M06](#m06), [M11](#m11), [M17](#m17). **Connection:** Analytical tails complete domains that cannot be replaced by an ordinary finite grid.

**Sources:** [P05](../science/scalar-inequality.md#p05), [P06](../science/scalar-inequality.md#p06), and [endpoint verification commands](../verification/README.md).

<a id="m19"></a>
### M19. The complete compact-domain certificate

**Central question:** Which remaining proof obligations do the numerical verifiers discharge?

**Understanding target:** Join the exact compact domain to the analytical regions. Explain how 512 rational noise bands and 29,635 input rectangles cover the required region, how each band's lower input tail is proved, and why the $`10^{-6}`$ split excludes no allowed input. Distinguish the three numerical implementations and their envelopes while recognizing that they share the claim and rational partition.

**Dependencies:** [M06](#m06), [M11](#m11), [M17](#m17), [M18](#m18). **Connection:** The scalar theorem combines analytical arguments with complete deterministic enclosures; backend agreement alone is not its proof structure.

**Sources:** [P07](../science/scalar-inequality.md#p07), [P14](../science/proof-map.md#p14), and [reproduction guide](../verification/README.md).

<a id="m20"></a>
### M20. Geometry separates the two optimized costs

**Central question:** Why does full span force a strictly positive gap for every common interior error?

**Understanding target:** Compare $`G(\mathbf u)`$ with the directional repetition loss $`\Lambda(\mathbf u)`$ before minimizing. Combine the Rayleigh lower bound with the spherical-average estimate for $`L`$ and the polynomial margin above that average. Recover $`\Gamma\geq L+(3ca/35)\lambda`$ without assuming that the different directional optimizers coincide.

**Dependencies:** [M07](#m07), [M15](#m15), [M17](#m17), [M18](#m18), [M19](#m19). **Connection:** The entropy comparison turns weighted directional coverage into a uniform separation of costs.

**Sources:** [P08](../science/geometric-gap.md#p08), [model M04](../science/geometric-gap.md#m04), and the definition of $`L`$ in [model M03](../science/single-use.md#m03).

<a id="m21"></a>
### M21. Fixed repetition direction and record overlaps

**Central question:** Which quantities control the two codewords after noisy measurement records accumulate?

**Understanding target:** Choose the antipodal repetition code from known channel parameters and derive its reported-record probabilities, overlap $`B(\mathbf u)`$, and coherence-weighted overlap $`K(\mathbf u)`$. Explain the exact identity $`B-K=\Lambda`$ and the role of the remaining conditional coherence. The code direction is fixed before future measurements.

**Dependencies:** [M03](#m03), [M09](#m09), [M13](#m13), [M20](#m20). **Connection:** The abstract directional loss now acquires the operational meaning needed by the coding construction.

**Sources:** [P09.1](../science/repetition-coding.md#p09) and [model M03](../science/single-use.md#m03).

<a id="m22"></a>
### M22. Exact block accounting over every mask and record

**Central question:** What changes when the last surviving quantum system is measured?

**Understanding target:** Construct the conditional reference–code state and the averages $`\mathcal A_m,\mathcal C_m,\mathcal R_m`$. Derive the full binomial mask sum and its subtraction $`-p^n\mathcal A_n`$. At the all-measured mask, combine the terms into $`-p^n\mathcal C_n`$ rather than dropping the event or retaining a nonexistent receiver quantum entropy.

**Dependencies:** [M04](#m04), [M05](#m05), [M06](#m06), [M21](#m21). **Connection:** Correct all-record accounting is the link between a legitimate channel input and the sign of its coherent information.

**Sources:** [P09.2 and identity (P9.2)](../science/repetition-coding.md#p09).

<a id="m23"></a>
### M23. Matching record envelopes without postselection

**Central question:** How are the useful contribution and the all-measured loss bounded on the same exponential scale?

**Understanding target:** Use entropy overlap bounds for the upper envelopes and central sign classes for polynomial lower envelopes. Explain why a finite axis count and interior reporting error give constants independent of block length. Central classes bound a sum of nonnegative contributions; their use in the proof does not authorize the decoder to discard other outcomes. Account for zero coherence factors using the stated conventions.

**Dependencies:** [M06](#m06), [M10](#m10), [M21](#m21), [M22](#m22). **Connection:** These envelopes control the complete block identity while retaining its physical channel and every event.

**Sources:** [P09.3–P09.4](../science/repetition-coding.md#p09).

<a id="m24"></a>
### M24. The strict repetition frontier and the full-span theorem

**Central question:** How do the two proof branches establish zero one-use coherent information and positive capacity together?

**Understanding target:** Compare $`\nu_+=1-p+pK`$ with $`\nu_-=pB`$, optimize over the fixed repetition direction, and identify $`p_{\mathrm{rep}}=1/(1+L)`$ as the strict eventual-sign frontier. Combine the geometric gap with the exact single-use criterion; then choose a positive finite inner block before applying outer coding. Preserve the closed lower and open upper endpoints and the complete order of choices.

**Dependencies:** [M12](#m12), [M14](#m14), [M20](#m20), [M23](#m23). **Connection:** This assembles the uniform sufficient theorem. Equality at the repetition frontier, shorter exceptional blocks, and the optimal all-code boundary remain outside that sign argument.

**Sources:** [P10](../science/repetition-coding.md#p10) and [model M04](../science/geometric-gap.md#m04).

<a id="m25"></a>
### M25. The eight-use witness and its two controls

**Central question:** What finite calculation concretely illustrates the theorem's separation?

**Understanding target:** For equal Pauli axes, $`\epsilon=1/10`$ and $`p=7/10`$, justify the matching global cost $`\Gamma=27/59`$ and exact one-use threshold $`p_1=59/86`$. Follow the eight-use record sum and its certified value above $`7.47\times10^{-5}`$ bits per physical use, including the negative all-measured term. Explain the distinct roles of the mixed-input optimization control and the cancellation-sensitive negative-rate control.

**Dependencies:** [M07](#m07), [M15](#m15), [M17](#m17), [M22](#m22), [M24](#m24). **Connection:** The example uses a sharper bound than the conservative uniform strip, and its positive block value has the outer-coding interpretation already established.

**Sources:** [Model M05 and P13](../science/eight-use-witness.md), [stored all-mask witness](../data/figures/figure1_original_witness140.json), and [verification commands](../verification/README.md).

<a id="m26"></a>
### M26. Coplanarity and the reporting-noise endpoints

**Central question:** Which boundaries explain the geometric guarantee's scope?

**Understanding target:** Prove $`\Gamma=L=c`$ for coplanar supported axes by using a common perpendicular direction and the global entropy lower bound. Interpret this as a statement about the defined long-balanced-repetition comparison. Treat perfect reports and completely random reports directly from their physical channels, including the erasure-capacity formula at $`\epsilon=1/2`$.

**Dependencies:** [M07](#m07), [M13](#m13), [M15](#m15), [M20](#m20), [M24](#m24). **Connection:** These controls distinguish weighted full span from mere incompatibility and prevent singular interior formulas from being mistaken for endpoint proofs.

**Sources:** [P11 and model M06](../science/limiting-geometries.md), with [erasure-capacity attribution](../references/README.md).

<a id="m27"></a>
### M27. An exact cone family near a plane

**Central question:** When can both threshold costs be evaluated exactly along a controlled geometric family?

**Understanding target:** Compute the frame of the equally weighted three-axis cone, use convexity and Jensen's inequality to find $`G_{\min}`$ and $`L`$, and identify the extra condition that makes $`\Gamma=G_{\min}`$ valid. Retain the exact domain $`0\leq\lambda\leq\min\{1/3,W(a)/P(a)\}`$ and its all-error subdomain through $`1/4`$. Obtain the fixed-error leading threshold-gap coefficient.

**Dependencies:** [M07](#m07), [M15](#m15), [M17](#m17), [M20](#m20), [M26](#m26). **Connection:** A solvable limiting family supplies an exact local comparison, without identifying an all-code capacity boundary.

**Sources:** [P12](../science/limiting-geometries.md#p12) and [model M06](../science/limiting-geometries.md#m06).

<a id="m28"></a>
### M28. Universal linear closure of the threshold gap

**Central question:** Why is linear closing near rank deficiency a family-wide result?

**Understanding target:** Use a least-eigenvalue trial direction to bound $`L-c`$, then use a minimizer of $`\Lambda`$ to bound $`\Gamma-L`$ from above. Combine with the geometric lower bound and the exact threshold identity to prove $`p_{\mathrm{rep}}-p_1=\Theta_\epsilon(\lambda)`$ at each fixed interior error, uniformly over finite ensembles. Explain why the proof needs only $`\Gamma\leq G_{\min}`$ and allows small weights outside a plane.

**Dependencies:** [M07](#m07), [M14](#m14), [M15](#m15), [M20](#m20), [M24](#m24), [M27](#m27). **Connection:** The cone's exact example becomes a general geometric law, with error-dependent constants and a threshold width distinct from a rate.

**Sources:** [P08 linear-closure corollary](../science/geometric-gap.md#p08-linear-closure) and [model M06 linear-closure statement](../science/limiting-geometries.md#m06-linear-closure).

<a id="m29"></a>
### M29. Evidence, proof dependencies, and attribution

**Central question:** What supports each claimed conclusion, and which ingredients are imported?

**Understanding target:** Trace claims C1–C6 to their analytical arguments, certificate obligations, and numerical witness records. Distinguish integrity checks, complete certificate verification, finite witness evaluation, and figure reproduction by their commands and outputs. Locate the coding and erasure theorems and the established incomplete-erasure and repetition frameworks. Treat claim C7 as a scoped literature comparison, including the correction that improved dephrasure rates need not improve thresholds.

**Dependencies:** [M11](#m11), [M19](#m19), [M24](#m24), [M25](#m25), [M26](#m26), [M28](#m28). **Connection:** A coherent scientific account includes exact evidential roles and attribution alongside its mathematical argument.

**Sources:** [Model M07–M08 and P14–P15](../science/proof-map.md), [references](../references/README.md), [verification guide](../verification/README.md), and [source/evidence index](../docs/SOURCE_TO_CANONICAL.md).

<a id="m30"></a>
### M30. The complete geometric-superadditivity story

**Central question:** What does the result explain about quantum communication with noisy measurement records?

**Understanding target:** Connect the physical operation budget to the global one-use entropy penalty, the all-record repetition construction, the strict geometric gap, and the finite-block coding implication. State the full ensemble and common-error quantifiers, explain the eight-use example and universal linear closure, and identify the constructive scope of each frontier. Full span guarantees a positive region in principle; its width, a sufficient inner length, and the achievable rate can depend strongly on the channel.

**Dependencies:** [M13](#m13), [M24](#m24), [M25](#m25), [M26](#m26), [M27](#m27), [M28](#m28), [M29](#m29). **Connection:** The local channel, entropy, geometry, and coding arguments now form one bounded contribution whose proofs, comparisons, and computational evidence can be followed directly.

**Sources:** [Scientific reading route](../science/README.md), [exact theorem](../science/geometric-gap.md#m04), [proof map](../science/proof-map.md), and [contribution and attribution](../references/README.md).
