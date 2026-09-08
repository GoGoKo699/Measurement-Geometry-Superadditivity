# All-common-noise full-span separation

Let a channel transmit a qubit intact with probability $1-p$ and otherwise return only the correctly labeled result of a destructive measurement along one of finitely many unit Bloch axes $n_b$. The axis probabilities $w_b$ are positive and sum to one. Each reported sign is independently flipped with a **common** probability $0<e<1/2$. The mask and axis labels are correct. The encoder does not know future choices; discarded systems and hidden true signs cannot be recovered. There is no postselection, feedback, or preshared entanglement.

Define

$$a=(1-2e)^2,\qquad c=1-a,\qquad T=\sum_b w_b n_b n_b^{\mathsf T},\qquad\lambda=\lambda_{\min}(T),$$
$$L=\min_{\|u\|=1}\sum_b\frac{w_bc}{\sqrt{1-a(n_b\cdot u)^2}},\qquad d_e=\frac3{35}ca.$$

**Theorem.** If $\lambda>0$, then

$$\boxed{\frac1{1+L+d_e\lambda}\leq p<\frac1{1+L}
\implies Q^{(1)}(\mathcal N)=0<Q(\mathcal N).}$$

The one-use optimization is over every input density matrix, not just nearly pure or maximally mixed inputs. Positive capacity is established by a sufficiently long finite balanced antipodal repetition block followed by the quantum coding theorem. The displayed interval is guaranteed and nonempty but is not asserted to describe exact optimal capacity thresholds.

For the strict eventual-sign criterion of this repetition construction, $L<\Gamma$ if and only if the axes span three dimensions. This is **not** an all-code exclusion for coplanar measurement channels.

At $e=0$ there is no zero-one-use/positive-capacity region: one-use coherent information is positive for $p<1$, and at $p=1$ the channel is classical. At $e=1/2$ the channel is erasure up to independent flags and $Q^{(1)}=Q$. The theorem's open noise range is therefore meaningful, while the available gap can shrink to zero near either endpoint.

The proof uses a new entropy comparison with

$$\ell=c\left(1+\frac a4+\frac{a^2}4+\frac{a^3}{10}\right).$$

Both noise endpoints and every nearly pure input tail are controlled analytically. The remaining compact noise/input domain is covered by 512 rational noise bands and 29,635 rational input intervals, verified with two interval-arithmetic backends. See [THEORY.md](THEORY.md), the shipped certificate, and `reproduce.py`.

This is an author-side, computer-assisted theorem, not external review or proof-assistant formalization. Finite measurement ensembles, common symmetric sign noise, independent uses, correct labels, and inaccessible measured systems are substantive assumptions. The result neither proves an efficient decoder nor guarantees a useful finite rate. Prior work on incomplete-erasure channels and repetition-code nonadditivity remains credited in [LITERATURE.md](LITERATURE.md). Absolute priority is not certified.
