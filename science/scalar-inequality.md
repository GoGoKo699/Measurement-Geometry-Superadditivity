# The scalar entropy inequality and its certificate

[Science](README.md) · [Learning](../learning/README.md) · [References](../references/README.md) · [Verification](../verification/README.md)

The geometric theorem needs an entropy comparison valid throughout the open reporting-error interval and for every input eigenvalue. This page gives the full scalar statement and its proof obligations.

Analytical arguments cover regions approaching both noise endpoints and arbitrarily nearly pure inputs. The remaining compact domain is covered by an exact rational certificate, checked by three separate arithmetic implementations. The computational intervals enclose complete regions; the result is not inferred from a grid of sampled channels. [Verification commands and expected outputs](../verification/README.md) explain how to inspect the evidence.

<!-- BEGIN canonical-unit P04 -->
<a id="p04"></a>
## P04. The all-common-noise scalar lemma

**Sources:** [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §3; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §§3–4; source [C1](../docs/SOURCE_TO_CANONICAL.md#c1)–[C2](../docs/SOURCE_TO_CANONICAL.md#c2) and [V1](../docs/SOURCE_TO_CANONICAL.md#v1)–[V9](../docs/SOURCE_TO_CANONICAL.md#v9). **Claims:** C2, C4.

Define

```math
P(a)=1+\frac a4+\frac{a^2}4+\frac{a^3}{10},\qquad \ell=cP(a),
```

```math
V(a)=\frac34+\frac{3a^2}{20}+\frac{a^3}{10},\qquad W(a)=\frac14+\frac a4+\frac{a^2}{10}.
```

The exact identities

```math
1-\ell=aV(a),\quad \ell-c=caW(a),\quad P=V+W
```

show that $`c\lt \ell\lt 1`$ for $`0\lt c\lt 1`$. The computer-assisted entropy lemma is

```math
\boxed{\mathscr D(t,c):=(1-\ell)C_\perp(t)+(\ell-c)C_\parallel(t)-\ell a h_2(t)\geq0}
```

**(P4.1)**

for every $`0\lt c\lt 1`$ and $`0\leq t\leq1/2`$. The proof has three domains: [P05](#p05) handles $`0\lt c\leq2^{-28}`$, [P06](#p06) handles $`0\lt a\leq1/25`$, and [P07](#p07) covers the remaining compact noise domain and its entire input range. These arguments jointly cover the whole open error interval; no sampling interpolation is used.

When (P4.1) is combined with (P3.3),

```math
C_\perp-c\beta h_2(t)\geq(1-\beta)\ell h_2(t),
```

and therefore

```math
\frac{C_\epsilon(t,x)}{h_2(t)}\geq\beta g+(1-\beta)\ell.
```

For each input weight, $`\beta(t,\epsilon)`$ is independent of the axis label. Summing over $`b`$ and taking the global infimum gives

```math
\boxed{\Gamma\geq\min\{G_{\min},\ell\}.}
```

**(P4.2)**

Equality $`\Gamma=G_{\min}`$ requires a separate argument. The common-coefficient step relies on the same reporting error for every axis.

<!-- END canonical-unit P04 -->

<!-- BEGIN canonical-unit P05 -->
<a id="p05"></a>
## P05. Analytical low-noise endpoint

**Sources:** [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §3.1; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §3; source [C1](../docs/SOURCE_TO_CANONICAL.md#c1)–[C2](../docs/SOURCE_TO_CANONICAL.md#c2). **Claim:** C4.

Let $`0\lt c\leq c_*=2^{-28}`$, $`\zeta=\ln(1/c)`$ and $`\delta_0=1/100`$. Use the bounds

```math
\ell\leq\frac85c,\quad \ell-c\leq\frac35c,\quad \ln2\gt \frac{69}{100},\quad\ln100\lt 5,\quad\ln4\lt 2.
```

The logarithm bounds have elementary rational certificates: three positive terms in the atanh series for $`\ln2`$, and finite lower exponential sums for $`\exp(5)`$ and $`\exp(2)`$, suffice. Their exact arithmetic checks are recorded in C2.

### P05.1 Input weights $`\delta_0\leq t\leq1/2`$

The smaller eigenvalue for $`C_\perp`$ is at least $`y=ct(1-t)`$ and lies below one half. Monotonicity of binary entropy and its nonnegative terms yield

```math
C_\perp(t)\geq\frac{ct(1-t)\zeta}{\ln2},\qquad h_2(t)\leq\frac{t[\ln(1/t)+1]}{\ln2}.
```

Since $`\zeta\geq28\ln2\gt 19.32`$, $`1-t\geq1/2`$ and $`\ln(1/t)\lt 5`$, the ratio exceeds $`1.61c`$. On the other hand,

```math
\frac{\ell a}{1-\ell}\leq\frac{(8/5)c}{1-(8/5)c_*}\lt 1.61c.
```

The $`C_\perp`$ term alone proves (P4.1); the nonnegative $`C_\parallel`$ term need not be used.

### P05.2 Arbitrarily nearly pure inputs

For $`0\lt t\leq\delta_0`$, the entropy bounds give

```math
C_\perp(t)-c h_2(t)\geq\frac{ct}{\ln2} \left[(1-\delta_0)\zeta-\delta_0\ln(1/\delta_0)-(1+c)\delta_0\right],
```

```math
h_2(t)-C_\parallel(t)\leq\frac{\eta t}{\ln2}\ln\frac{1-\epsilon}{\epsilon}.
```

Use $`\eta\ln((1-\epsilon)/\epsilon)\leq\ln(4/c)`$ and the exact cancellation

```math
\mathscr D=(1-\ell)(C_\perp-c h_2)- (\ell-c)(h_2-C_\parallel).
```

After applying the conservative bounds above, the coefficient of $`\zeta`$ is positive. Substitution at $`c=c_*`$ and $`\zeta\gt 19.32`$ gives the recorded strictly positive lower margin

```math
\frac{706479660745902522393}{112589990684262400000}
```

for the normalized low-noise tail expression. The exact compact-input comparison margin used in P05.1 is

```math
\frac{167771999}{16777215900}\gt 0.
```

C2 records these exact rational margins. The proof covers all positive $`c`$ in this range and all $`t\gt 0`$, however small. At $`t=0`$, (P4.1) is equality.

<!-- END canonical-unit P05 -->

<!-- BEGIN canonical-unit P06 -->
<a id="p06"></a>
## P06. Analytical high-noise endpoint

**Sources:** [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §3.2; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §3; source [C1](../docs/SOURCE_TO_CANONICAL.md#c1)–[C2](../docs/SOURCE_TO_CANONICAL.md#c2). **Claim:** C4.

Let $`0\lt a\leq1/25`$, equivalently $`2/5\leq\epsilon\lt 1/2`$, and set

```math
z=(1-2t)^2,\qquad\phi(z)=h_2\left(\frac{1-\sqrt z}{2}\right).
```

Define the explicitly labeled high-noise functions

```math
J_\phi=\phi(z+a(1-z))-(1-a)\phi(z),\qquad H_\phi=\phi(az)-\phi(a).
```

Then $`\mathscr D=(1-\ell)J_\phi-(\ell-c)H_\phi`$. The convergent entropy series is

```math
\phi(z)=1-\frac1{\ln2}\sum_{k\geq1}\frac{z^k}{2k(2k-1)}.
```

It makes $`f(z)=(1-z)[-\phi''(z)]`$ positive and increasing, with upper bound $`1/(4\ln2)`$; its coefficients are

```math
\frac1{2(2j+1)(2j+3)\ln2},\qquad j\geq0.
```

The derivative identity and integral representation give

```math
K_\phi(z)=\phi(z)+(1-z)\phi'(z)=\int_z^1 f(v)\,dv \geq(1-z)\left(1-\frac1{2\ln2}\right).
```

Taylor's integral remainder in $`a`$, bounded using $`f`$, yields

```math
J_\phi\geq a(1-z)\left[\frac{2\ln2-1}{2\ln2}-\frac{a}{8\ln2(1-a)}\right].
```

Also $`-\phi'(v)\leq1/[2\ln2(1-a)]`$ for $`0\leq v\leq a`$, hence

```math
H_\phi\leq\frac{a(1-z)}{2\ln2(1-a)}.
```

For $`t\gt 0`$ the required ratio is controlled by

```math
\frac{J_\phi}{H_\phi}\geq(1-a)(2\ln2-1)-\frac a4\gt \frac{887}{2500},
```

while

```math
\frac{\ell-c}{1-\ell}=\frac{cW(a)}{V(a)}\leq\frac{1084}{3125}.
```

The gap is $`99/12500\gt 0`$, proving (P4.1) on the whole high-noise region. These coefficient identities and rational constants are recorded in source C2. At $`t=0`$, one uses equality rather than dividing by a vanishing entropy difference. This argument reaches arbitrarily close to $`\epsilon=1/2`$; the endpoint itself is addressed physically in [P11](limiting-geometries.md#p11).

<!-- END canonical-unit P06 -->

<!-- BEGIN canonical-unit P07 -->
<a id="p07"></a>
## P07. Complete compact-domain certificate

**Sources:** [S4](../docs/SOURCE_TO_CANONICAL.md#s4) §3.3; [S5](../docs/SOURCE_TO_CANONICAL.md#s5) §4; [V1](../docs/SOURCE_TO_CANONICAL.md#v1)–[V9](../docs/SOURCE_TO_CANONICAL.md#v9); source [C1](../docs/SOURCE_TO_CANONICAL.md#c1)–[C2](../docs/SOURCE_TO_CANONICAL.md#c2). **Claims:** C2, C4.

### P07.1 Precisely what is certified

For

```math
c_*:=2^{-28}\leq c\leq\frac{24}{25},\qquad 0\lt t\leq\frac12,
```

divide (P4.1) by the positive factor $`ca`$:

```math
\mathscr D/(ca)=V(a)\bigl[C_\perp(t,c)/c\bigr]+W(a)C_\parallel(t,c)-P(a)h_2(t).
```

**(P7.1)**

Here $`C(t,c)`$ means the endpoint cost evaluated at the unique $`\epsilon=(1-\sqrt{1-c})/2`$ in $`[0,1/2]`$. For the coefficient bounds, define

```math
\bar P(c)=P(1-c),\quad\bar V(c)=V(1-c),\quad\bar W(c)=W(1-c).
```

Each barred coefficient decreases with $`c`$. By concavity of $`\mathcal H`$ with $`\mathcal H(0)=0`$, $`C_\perp(t,c)/c`$ decreases with $`c`$. By additional classical sign noise, $`C_\parallel(t,c)`$ increases with $`c`$.

For every complete noise band $`[c_l,c_h]`$, a lower bound on the positive cost terms in (P7.1) is

```math
S_-(t)=\bar V(c_h)\frac{C_\perp(t,c_h)}{c_h}+\bar W(c_h)C_\parallel(t,c_l).
```

**(P7.2)**

For all $`c`$ in that band, the quantity to bound above is

```math
\bar P(c_l)h_2(t)-S_-(t).
```

This is an enclosure over the **whole noise band**, not evaluation at two putative representative channels.

### P07.2 Lower input tail in every band

With $`d:=\delta_{\mathrm{cert}}=10^{-6}`$, the same elementary input-tail argument as P05.2 gives

```math
\mathscr D(t,c)\geq\frac{ct}{\ln2}\mu(c),\qquad 0\lt t\leq\delta_{\mathrm{cert}}.
```

Define the tail bracket and the resulting outward lower enclosure by

```math
\begin{aligned} B_d(c)&:=(1-d)\ln(1/c)-d\ln(1/d)-(1+c)d,\\ \mu(c)&=(1-c\bar P(c))B_d(c)\\ &\quad-(\bar P(c)-1)\eta\ln\frac{1-\epsilon}{\epsilon}. \end{aligned} 
```

**(P7.3)**

The saved checks certify $`\mu\gt 0`$ throughout every noise band. Thus the compact computation omits no arbitrarily nearly pure input. The value $`10^{-6}`$ is a junction between two proofs, not a lower cutoff on admissible inputs. The margin called `tail` in the source code is this normalized expression; it is not a physical communication rate.

### P07.3 Every remaining rectangle

The immutable certificate **V1** supplies 512 exact-rational noise bands and 29,635 exact-rational input intervals in total. For each noise band, its listed intervals join exactly and cover $`[\delta_{\mathrm{cert}},1/2]`$. The noise bands join exactly and cover $`[c_*,24/25]`$.

$`S_-(t)`$ is concave in $`t`$ by P02. Therefore the line through outward-lowered endpoint values on an input interval $`[l,r]`$ lies below $`S_-`$ throughout that interval. The integer checker uses a tangent upper bound for $`h_2(t)`$ and checks the resulting linear deficit at both ends. The mpmath checker uses the same proof obligations but a different arithmetic backend and a different expression for the parallel conditional entropy.

The Decimal checker uses a separate implementation and a different scalar envelope. For a lower secant $`s_l+k(t-l)`$ and an upper enclosure $`P_+`$ for $`\bar P(c_l)`$, the unrestricted entropy-conjugate upper bound is

```math
P_+\log_2\!\left(1+\exp\left[-\frac{k\ln2}{P_+}\right]\right)-s_l+kl.
```

Derivative signs permit endpoint maxima when the stationary point is outside the interval. Using the unrestricted maximum when a sign is unresolved remains safe. The checker recomputes these bounds; it does not trust saved claimed negativity in V1.

### P07.4 Certificate evidence

| Evidence chain | Arithmetic and formula distinction | Recorded outcome |
|:--|:--|:--|
| V1 + V2 + V3, result V8 | Exact-rational cover; integer outward intervals; midpoint entropy-tangent envelope. | Complete 224-bit verification; largest normalized compact upper bound below $`-5.71962366142\times10^{-12}`$. |
| V1 + V4, result V9 | Separate mpmath interval engine and entropy-difference expression for $`C_\parallel`$. | All rectangles and tails pass at 85 decimal digits. |
| V1 + V5 + V6, result V7 | Separate Decimal engine and entropy-conjugate/secant envelope. | All 512 bands and 29,635 rectangles pass at 130 digits; largest compact upper bound below $`-2.37355635215\times10^{-10}`$. |

The smallest recorded normalized tail margin exceeds $`0.00028189136168`$ nats. Different negative compact margins are expected from different valid upper envelopes. The table reports the stored certificate-verification results.

Certificate verification checks the polynomial, noise domain, input-tail split, exact rational coverage and all required interval signs, and rejects corrupted or incomplete covers. The source-code and result hashes, together with independent execution entry points, are mapped in [P14](proof-map.md#p14) and the provenance ledger. Arithmetic assumptions, including outward rounding of elementary functions, remain part of the explicit computer-assisted proof obligation.

The analytical domains of P05 and P06 meet this complete compact domain at their exact endpoints. Together with pure-input equality and the compact-domain certificate, they establish the all-noise scalar lemma (P4.1).

<!-- END canonical-unit P07 -->

## Where this leads

With the scalar inequality established, [the geometric argument](geometric-gap.md#p08) separates the global one-use cost from the repetition loss.

---

Scientific editing sources: [COMPLETE_PROOF.md](../docs/COMPLETE_PROOF.md). [Section map](../website/furnishing-map.json).
