# Measurement geometry and collective quantum coding

A qubit either arrives intact or is measured and lost. In the second case, an imperfect classical record remains. **The geometry of those measurements can guarantee quantum communication beyond the globally optimized single-use coherent-information benchmark.**

For every permitted finite measurement ensemble spanning all three Bloch directions, and every **common symmetric reporting error** $`0<\epsilon<1/2`$, the project proves a nonempty interval of measurement probabilities with

```math
Q^{(1)}(\mathcal N)=0<Q(\mathcal N).
```

Here $`Q^{(1)}`$ maximizes coherent information over every single-qubit input state. $`Q`$ is unassisted asymptotic quantum capacity. A suitable collective encoding certifies a positive asymptotic rate where this fully optimized single-use quantity is zero. The theorem gives a sufficient region, not an exact capacity formula or a practical finite-block decoder.

**Expert bypass:** [exact theorem and assumptions](../../docs/MODEL_AND_CLAIMS.md#m04) · [complete proof](../../docs/COMPLETE_PROOF.md) · [figure atlas and downloads](figures.md) · [verification and evidence](verification.md).

## Start with the channel

The receiver gets surviving qubits and the correct measurement mask and axis labels, but only the reported signs. True outcomes, error bits and discarded qubits stay inaccessible. Encoding happens before those random choices, and every outcome enters the calculation.

If coherent information is familiar, [continue directly to the channel and eight-use illustration](channel.md). Otherwise, the [focused Preskill reading map and crosswalk](background.md) supplies the selected background and returns you to the exact place each concept is used. Preskill is the one external tutorial; the project supplies its own physical and geometric bridge.

## Then compare one use with a block

For equally likely Pauli axes, measurement probability $`0.70`$ and reporting error $`0.10`$, every one-use input has nonpositive coherent information and pure inputs attain zero. A balanced eight-use repetition input gives

```math
I_8/8>7.47\times10^{-5}\ \text{bits per physical use}.
```

The [channel guide](channel.md#eight-use-witness) explains the coherent encoder, its purified test input and every measured-count contribution, including the negative all-measured term. [Figure 1](figures.md#figure-1) shows this comparison. A finite positive inner block is chosen before outer coding gives it an asymptotic rate interpretation; an isolated eight-use decoding fidelity is not established.

## What geometry guarantees

The [proof guide](proof-guide.md#geometric-guarantee) joins an obstruction for every one-use input, a sufficient repetition construction and a geometric inequality separating their costs. Full span removes a common perpendicular direction, but the quantitative guarantee also needs the project's computer-assisted scalar entropy inequality.

[Figure 2](figures.md#figure-2) illustrates the guaranteed band for equally weighted Pauli axes. Its conservative band is distinct from the sharper bound supporting the eight-use witness. [Figure 3](figures.md#figure-3) follows a controlled approach to a plane; the [limits page](limits.md) explains the cone domain, coplanarity and both reporting-noise endpoints.

## Read, inspect, reproduce

The repository contains the complete scientific account for the stated result, including its proof, computational evidence and figures. [Project status and scope](status.md)

The learning route is **selected background → channel and witness → geometric proof guide → exact theorem and proof → limits and verification**. Every stage can be opened directly. You do not need to run software to read the argument.

Incomplete-erasure channels, repetition coding and superadditivity are established. The working contribution is the sufficient geometric condition over the stated family, subject to the [canonical priority qualifiers](../../docs/MODEL_AND_CLAIMS.md#m07). [Primary citations](../../docs/REFERENCES.md) serve attribution, not an additional prerequisite list.

[Source materials](materials.md) · [Current project status](status.md) · [GitHub and optional HTML instructions](../../WEBSITE.md)
