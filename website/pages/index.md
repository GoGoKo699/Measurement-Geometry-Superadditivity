# Measurement geometry and collective quantum coding

A qubit either arrives intact or is measured and lost. In the second case, a classical record remains. **How much does the geometry of the possible measurements matter when that record is imperfect?**

For the channel studied here, every finite measurement ensemble spanning all three Bloch directions guarantees a nonempty range of measurement probabilities with

$$Q^{(1)}(\mathcal N)=0<Q(\mathcal N),$$

for every **common symmetric reporting error** $0<\epsilon<1/2$. Here $Q^{(1)}$ is coherent information optimized over all single-qubit input states; $Q$ is unassisted asymptotic quantum capacity. The theorem supplies a guaranteed region, not an exact capacity formula. Its scalar entropy inequality is partly computer assisted.

[The model and exact statement](../../docs/MODEL_AND_CLAIMS.md#m01) · [How the proof works](proof-guide.md)

## Start with the channel

The receiver knows which qubits survived and which axes were measured. For a measured qubit, only the reported sign is available. The true outcome, the reporting error, and the discarded quantum system are not available to the receiver. The encoder acts before these random choices; every outcome is included.

[Follow a single use](channel.md)

## Then compare one use with a block

For equally likely Pauli axes, a measurement probability of $0.70$ and a reporting error of $0.10$, every single-use input has nonpositive coherent information. A balanced eight-use repetition input instead gives

$$I_8/8>7.47\times10^{-5}\ \text{bits per physical use}.$$

An outer code gives this positive block value its asymptotic communication meaning. It is not a demonstration that an isolated eight-qubit block decodes nearly perfectly. [Exact witness and all outcome branches](../../docs/COMPLETE_PROOF.md#p13)

## What geometry guarantees

Full span removes the common perpendicular direction available to coplanar measurements. The proof turns that distinction into a strictly positive gap between a global single-use entropy bound and a constructive repetition bound. Near a plane, the gap can become arbitrarily small. Other codes are not excluded for a coplanar channel; the reverse statement concerns this construction's strict threshold criterion.

[Read the result](../../docs/MODEL_AND_CLAIMS.md#m04) · [See its limits](limits.md)

## Read, inspect, reproduce

The project has three entry routes. **Understand the result:** channel, proof guide, then figures. **Check the argument:** exact model, complete proof, and verification record. **Use the materials:** figure inputs, independent checkers, references, and the claim-to-evidence inventory.

[View the figures](figures.md) · [Run the checks](verification.md) · [Find the source materials](materials.md)
