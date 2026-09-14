# Source-to-canonical notation crosswalk

**Documentary normalization only, 8 September 2026.** Executable files and recorded numerical outputs retain their original bytes. This table prevents locally valid historical definitions from colliding when the proof is read as one document. Source IDs resolve in [SOURCE_TO_CANONICAL.md](SOURCE_TO_CANONICAL.md).

| Source notation and location | Canonical notation | Change and reason |
|:--|:--|:--|
| `e` or `epsilon`, S3–S5 | $`\epsilon`$ | One symbol for common symmetric reporting error. |
| $`\epsilon_b`$, S8 general repetition lemma | $`\epsilon`$ throughout the canonical proof | Explicit restriction of the broader inherited lemma to the current theorem's common-error model; no broader theorem imported. |
| Local $`L=\sum_b\log(a_b/b_b)`$, S8 §3.2 | $`\mathcal L_{\mathrm{rec}}=\sum_b\ln(\pi_b^+/\pi_b^-)`$ | Avoid collision with the globally minimized repetition loss $`L`$. The exponential convention fixes these as natural logarithms. |
| Local $`a_b,b_b`$, S8 §3.2 | $`\pi_b^+,\pi_b^-`$ | Single-axis likelihoods do not reuse global noise parameters $`a,c`$ or the axis index. |
| Record products $`a,b`$, S8 §3.1 | $`\mathsf p_+(\omega),\mathsf p_-(\omega)`$ | Distinguish probability products from $`a=(1-2\epsilon)^2`$ and axis $`b`$. |
| Record string, locally unnamed or $`y_j`$ | $`\omega=(y_1,\ldots,y_m)`$, with $`y_j=(b_j,s_j)`$ | Distinguish a whole record from an outcome or high-noise variable. |
| Squared coherence called $`y`$, S8 §3.1 | $`\chi_\omega=\prod_j\kappa_{b_j}`$ | Avoid overloading a record symbol $`y_j`$. |
| Outcome posterior $`q,x`$ in S8 §3.1 | $`q_\omega,x_\omega`$ | Distinguish posterior from geometric squared projection $`x=(\mathbf n\cdot\mathbf u)^2`$. |
| $`C_0(t),C_1(t)`$, S4–S5 | $`C_\perp(t),C_\parallel(t)`$ | These single-axis endpoint functions no longer collide with the repetition convention $`\mathcal C_0=0`$. |
| $`A_m,C_m,R_m`$, S8 | $`\mathcal A_m,\mathcal C_m,\mathcal R_m`$ | Clearly separate record-averaged block quantities, reference register $`\mathsf R`$, and the single-axis endpoint cost. |
| $`I_n`$, S4–S8 | $`\mathcal I_n`$ | Distinguish the block coherent information from identity operator $`I`$; no normalization change. |
| Receiver/reference $`B,R`$ | $`\mathsf B,\mathsf R`$ | Distinguish the receiver register from the scalar overlap $`B(\mathbf u)`$. |
| Exponential bases $`U,V`$, S8 §3.3 | $`\nu_+=1-p+pK`$, $`\nu_-=pB`$ | Avoid collision with the polynomial $`V(a)`$. |
| Axis count $`n_b`$, S8 §3.2 | $`m_b`$ | Counts of measured sites do not reuse the vector $`\mathbf n_b`$ or the full block length $`n`$. |
| High-noise functions $`J,H,K`$, S4 §3.2 | $`J_\phi,H_\phi,K_\phi`$ | Distinguish the number of axes $`J`$, entropy transform $`\mathcal H`$, and coherence overlap $`K(\mathbf u)`$. |
| $`u=\ln(1/c)`$, S4 §3.1 | $`\zeta=\ln(1/c)`$ | Do not reuse coding direction $`\mathbf u`$. |
| $`P(c),V(c),W(c)`$ when evaluating code-generated envelopes | $`\bar P(c)=P(1-c)`$, $`\bar V(c)=V(1-c)`$, $`\bar W(c)=W(1-c)`$ | Makes the change of argument explicit. Original polynomials remain functions of $`a`$. |
| Stationary point denoted $`t_*`$ in envelope optimizers | $`t_{\mathrm{stat}}`$ | Distinguish this computational extremum from an optimized channel input. |
| $`d=(c/4)t(1-t)`$ in posterior spectra | $`\Delta_t=(c/4)t(1-t)`$ | Avoid collision with the full-span coefficient $`d_\epsilon=3ca/35`$. |
| Paired integral constants $`A_v,B_v,b`$ | $`\mathsf A_v,\mathsf B_v,\zeta_t`$ | Avoid confusion with record overlap $`B`$, axis $`b`$ and the input weight. |
| $`C1`$–$`C7`$ in the frozen map | Claim C1–C7 | Preserved exactly. Intake source IDs C1–C4 are always labeled **source C1–C4** or resolved in the register, never treated as claim numbers. |
| Source IDs R1–R6 from intake | Source R1–R6 | Retained for reproducibility files; external background references are named **EXT1–EXT6**, not reused R labels. |

## Terms that must not be interchanged

$`Q^{(1)}`$ is optimized one-use coherent information; $`Q`$ is asymptotic unassisted quantum capacity. $`p_1`$ is the exact one-use positivity boundary expressed using $`\Gamma`$; $`p_{\mathrm{rep}}`$ is the optimized strict eventual-sign frontier of the balanced repetition construction. The theorem's lower endpoint is a sufficient one-use-zero bound and can be larger than the exact $`p_1`$. Its upper endpoint is open.

The cone parameter $`\lambda`$ equals the frame's smallest eigenvalue only in the specified range $`0\leq\lambda\leq1/3`$. The safe uniform exact one-use formula for the planned limit is stated on $`0\leq\lambda\leq1/4`$, unless the larger parameter-dependent range is explicitly justified.

Noise endpoint symbols and claims are treated separately; formulas dividing by $`a`$, $`c`$ or $`h_2(t)`$ are not evaluated at singular endpoints by notation alone. No additional noise model is introduced by renaming symbols.
