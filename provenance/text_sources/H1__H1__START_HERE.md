# New project handover: measurement geometry and noisy records

**8 September 2026.** This packet starts a separate channel-theory project. It is not a new theorem, a new audit, a publication-ready repository, or a manuscript. The supplied research archive is unchanged.

## What to read

Unzip `source/Noisy-record-PRL-final-audit-2026-09-08.zip` into a separate working directory. Inside its `Noisy-record-PRL-final-audit/` root, read:

1. `source/Noisy-record-PRL-story-and-proof-map-v1/ONE_PAGE_ARGUMENT.md` for the agreed simple story.
2. `source/Noisy-record-PRL-story-and-proof-map-v1/CLAIM_PROOF_MAP.md` for claims and proof obligations.
3. `source/common_noise_range/THEOREM_STATEMENT.md` and `THEORY.md` for the actual all-common-noise theorem and dependencies.
4. Top-level `PROOF_AUDIT.md`, `PRIOR_WORK_COMPARISON.md`, `README.md`, and `results/AUDIT_SUMMARY.json` for the latest author-side audit, commands and limitations.

Nested earlier proof sources are preserved because they contain necessary lemmas and independent checking implementations. They should be traced and consolidated, not discarded indiscriminately. Historical titles and restrictions in those dependencies do not supersede the current theorem or the latest audit.

## Scientific boundary

The source reports a theorem for independent uses of a qubit channel with an intact branch and a destructive measurement branch. Measurement axes and masks are reported correctly; the outcome sign has independent common symmetric reporting error; discarded quantum systems and true signs are not available. The encoder acts before these choices. No postselection, feedback or preshared entanglement is used.

The central claim is a guaranteed nonempty region with zero globally optimized single-use coherent information but positive quantum capacity for every finite full-span measurement ensemble and every common symmetric error strictly between zero and one half. The proof is partly computer assisted. Coplanar converse wording is construction-specific, and the achieved boundary is not an exact capacity formula. The finite repetition input requires asymptotic outer coding; no efficient decoder or universally practical rate is established. Read the exact source quantifiers instead of relying on this summary.

This handover does not redo the scientific audit. The source records author-side independent implementations, not external peer review or proof-assistant formalization. Absolute priority is not certified. The original many-body data do not constitute evidence for the channel theorem.

## User's required sequence

First finish the scientific consolidation. This means one authoritative model/claim/notation document, one dependency-complete proof, the required certificates with genuinely separate checking implementations, canonical retained example and limit data, and scientifically finalized content for three proposed figures. Correctness and simplicity of the story both matter. No full manuscript yet.

Then populate a new repository dedicated to this paper and verify a clean checkout. Suggested name: `GoGoKo699/Measurement-Geometry-Superadditivity`; this is a proposal, not an existing repository. Ask the user for that repository when the upload-ready scientific baseline is available, not before.

Then draft the manuscript. The planned narrative is one channel, one geometric theorem, a short proof route, the eight-use equal-Pauli example at 10% record error and 70% measurement probability, and a controlled near-coplanar limit. Do not inherit the old four-figure count. No unrelated research extensions or larger searches without a specific reason.

The new repository should contain Markdown explanations/proofs, Python code, necessary inputs, certificates, independent verifiers and reproducible figure outputs. No manuscript TeX, TikZ, standalone fonts or nested historical ZIP dump in its active tree. Keep independent numerical evaluators separate rather than deduplicating away their independence. Select licensing explicitly; none is granted by this handover.

## Boundary from the old project

The original `GoGoKo699/Boundary-Entangling-Susceptibility` repository was cleaned and merged at `c54dca28464832ecebeb6602c4c490d3d68d3015` in PR #4. Both post-merge CI jobs passed. It remains the entanglement-response study under its old name. Do not rename, repurpose or modify it for the new paper.

The old Figure 1 historical bootstrap-metadata limitation is documented in that repository; it is not a dependency of this channel project. Earlier optimized-capability, routing, dynamical-memory and unknown-recovery screens are not prerequisites for the new theorem and are not imported here.

## First task in the new chat

Check the included hashes, read the authoritative sources, and produce a bounded scientific-completion inventory: what is already complete, what needs consolidation or figure preparation, and what would genuinely require new science. Do not repeat a large audit by default. Stop before creating a repository or drafting the manuscript and state the next concrete step.
