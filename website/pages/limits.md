# What the result does not claim

The guarantee is broad in measurement geometry, but its physical model is specific. The boundaries below are part of the result, not conditions to discard when summarizing it.

## Coplanarity is a construction boundary

If all axes lie in a plane, a common perpendicular direction gives $\Gamma=L=c$. Full span is therefore necessary and sufficient for the **strict threshold comparison of this long balanced-repetition construction**. It is not a theorem excluding every other code or exceptional finite-block improvement for a coplanar channel. [Exact statement](../../docs/MODEL_AND_CLAIMS.md#m06)

## The two record-noise endpoints are different

At $\epsilon=0$, the measured conditional reference states are pure. Single-use coherent information is already positive for mixed inputs whenever $p<1$; at $p=1$ the output is classical. At $\epsilon=1/2$, the record is input independent and the channel is erasure up to independent flags, with $Q=Q^{(1)}=\max(0,1-2p)$. Neither endpoint has the zero-one-use/positive-capacity region. [P11: endpoint arguments](../../docs/COMPLETE_PROOF.md#p11)

## A nonzero gap need not be useful in practice

The guaranteed interval can shrink near a plane or near a noise endpoint. The theorem does not provide a fixed minimum rate or block length uniformly across all these channels. Its positive-capacity statement invokes an asymptotic outer code, not an efficient decoder for the retained eight-qubit example. [Quantifier order](../../docs/MODEL_AND_CLAIMS.md#m04)

## An exact special case is not an exact capacity formula

For the cone family, the source gives exact expressions for the one-use frontier and the repetition frontier on a stated parameter range. Figure 3 uses the all-error-safe range $0\leq\lambda\leq1/4$. Neither frontier is asserted to be the exact all-code capacity boundary. The dashed tangent is derived, not fitted. [P12: cone family](../../docs/COMPLETE_PROOF.md#p12)

## No silent extension of the noise model

The headline theorem does not cover arbitrary axis-dependent, asymmetric, correlated, or basis-label errors. Surviving qubits arrive intact. The source does not claim external peer review, proof-assistant formalization, exhaustive priority clearance, or a practical fault-tolerant protocol. [Complete claim register](../../docs/MODEL_AND_CLAIMS.md#m07)
