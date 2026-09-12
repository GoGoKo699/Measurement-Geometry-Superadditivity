# From a claim to its supporting material

[Overview](README.md) · [Background](background.md) · [Channel](channel.md) · [Proof route](proof-guide.md) · [Figures](figures.md) · [Exact theorem](../docs/MODEL_AND_CLAIMS.md) · [Complete proof](../docs/COMPLETE_PROOF.md) · [Materials](materials.md)

<details>
<summary>All reading routes</summary>

- [The project](README.md)
- [Selected background](background.md)
- [The channel](channel.md)
- [The proof route](proof-guide.md)
- [Figure atlas](figures.md)
- [Scope and limits](limits.md)
- [Exact model and theorem](../docs/MODEL_AND_CLAIMS.md)
- [Complete proof](../docs/COMPLETE_PROOF.md)
- [Verification guide](verification.md)
- [Exact reproduction commands](../docs/REPRODUCTION.md)
- [References and their roles](../docs/REFERENCES.md)
- [Source materials](materials.md)
- [Notation crosswalk](../docs/NOTATION_CROSSWALK.md)
- [Source and proof ledger](../docs/SOURCE_TO_CANONICAL.md)
- [Frozen scientific argument](../docs/FROZEN_ARGUMENT.md)
- [Visual design](visual-design.md)
- [Status and publication](status.md)

</details>


The manuscript comes last. The repository already contains the model, complete proof, retained numerical inputs, figure specifications, approved figures, captions, and the declared computational evidence. This page connects those materials without drafting the paper.

## Background and project reasoning

The [focused Preskill map](background.md) is the one external educational route. Its [structured learning metadata](../website/learning_bridge.json) records the pinned edition, passage locations, return links and the canonical project anchors used by the bridge. It is separate from the scientific claim ledger below. [Current attribution correction](status.md#correction-record) · [Reader implementation and checks](../website/review/PRESKILL_BRIDGE_REPORT.md)

## Claim-to-evidence inventory

[Canonical claim map](../provenance/CLAIM_COVERAGE.json) · [Full source-to-proof ledger](../docs/SOURCE_TO_CANONICAL.md)

| Claim | Exact statement | Proof | Role |
|---|---|---|---|
| C1 | [Model statement](../docs/MODEL_AND_CLAIMS.md#m04) | [P01](../docs/COMPLETE_PROOF.md#p01) · [P02](../docs/COMPLETE_PROOF.md#p02) · [P03](../docs/COMPLETE_PROOF.md#p03) · [P04](../docs/COMPLETE_PROOF.md#p04) · [P05](../docs/COMPLETE_PROOF.md#p05) · [P06](../docs/COMPLETE_PROOF.md#p06) · [P07](../docs/COMPLETE_PROOF.md#p07) · [P08](../docs/COMPLETE_PROOF.md#p08) · [P09](../docs/COMPLETE_PROOF.md#p09) · [P10](../docs/COMPLETE_PROOF.md#p10) | Headline full-span sufficient interval; construction-specific scope. |
| C2 | [Model statement](../docs/MODEL_AND_CLAIMS.md#m03) | [P01](../docs/COMPLETE_PROOF.md#p01) · [P02](../docs/COMPLETE_PROOF.md#p02) · [P03](../docs/COMPLETE_PROOF.md#p03) · [P04](../docs/COMPLETE_PROOF.md#p04) · [P05](../docs/COMPLETE_PROOF.md#p05) · [P06](../docs/COMPLETE_PROOF.md#p06) · [P07](../docs/COMPLETE_PROOF.md#p07) · [P08](../docs/COMPLETE_PROOF.md#p08) · [P13](../docs/COMPLETE_PROOF.md#p13) | Global one-use optimization; no trial-input substitution. |
| C3 | [Model statement](../docs/MODEL_AND_CLAIMS.md#m03) | [P01](../docs/COMPLETE_PROOF.md#p01) · [P02](../docs/COMPLETE_PROOF.md#p02) · [P09](../docs/COMPLETE_PROOF.md#p09) · [P10](../docs/COMPLETE_PROOF.md#p10) | Every branch included; finite positive inner block before outer coding. |
| C4 | [Model statement](../docs/MODEL_AND_CLAIMS.md#m04) | [P02](../docs/COMPLETE_PROOF.md#p02) · [P03](../docs/COMPLETE_PROOF.md#p03) · [P04](../docs/COMPLETE_PROOF.md#p04) · [P05](../docs/COMPLETE_PROOF.md#p05) · [P06](../docs/COMPLETE_PROOF.md#p06) · [P07](../docs/COMPLETE_PROOF.md#p07) · [P08](../docs/COMPLETE_PROOF.md#p08) | Computer-assisted scalar inequality plus geometric gap. |
| C5 | [Model statement](../docs/MODEL_AND_CLAIMS.md#m05) | [P12](../docs/COMPLETE_PROOF.md#p12) · [P13](../docs/COMPLETE_PROOF.md#p13) · [P14](../docs/COMPLETE_PROOF.md#p14) | One retained eight-use witness; source enclosures not newly calculated. |
| C6 | [Model statement](../docs/MODEL_AND_CLAIMS.md#m06) | [P11](../docs/COMPLETE_PROOF.md#p11) · [P12](../docs/COMPLETE_PROOF.md#p12) | Coplanar criterion, physical noise endpoints, domain-restricted cone formulas. |
| C7 | [Model statement](../docs/MODEL_AND_CLAIMS.md#m07) | [P15](../docs/COMPLETE_PROOF.md#p15) | Source-reported bounded prior-work distinction only; absolute priority not certified. |

## Figure and numerical inputs

The [figure atlas](figures.md) gives each panel's question, exact caption, source data, proof anchors, and approved downloads. The all-measured terms behind Figure 1 remain available even though they are not another main-text panel.

[Original eight-use interval record](../data/figures/figure1_original_witness140.json) · [All measured-count terms](../data/figures/figure1_all_masks_not_for_display.csv) · [Figure 2 bounds](../data/figures/figure2_pauli_guaranteed_region.csv) · [Figure 3 gap](../data/figures/figure3_cone_gap.csv)

## Proof certificate and separate checkers

[Exact reproduction commands](../docs/REPRODUCTION.md) · [Canonical covering](../certificates/common_noise_compact_certificate.json)

| Role | Source or recorded result |
|---|---|
| Rational cover | [certificates/common_noise_compact_certificate.json](../certificates/common_noise_compact_certificate.json) |
| Integer verifier | [verification/integer/certify_all_noise.py](../verification/integer/certify_all_noise.py) |
| mpmath verifier | [verification/mpmath/cross_backend.py](../verification/mpmath/cross_backend.py) |
| Decimal verifier | [verification/decimal/verify_certificate.py](../verification/decimal/verify_certificate.py) |
| Recorded integer result | [evidence/reference/integer224.json](../evidence/reference/integer224.json) |
| Recorded mpmath result | [evidence/reference/mpmath85.json](../evidence/reference/mpmath85.json) |
| Recorded Decimal result | [evidence/reference/decimal130.json](../evidence/reference/decimal130.json) |

## Canonical writing material

The [model](../docs/MODEL_AND_CLAIMS.md) fixes definitions, assumptions and notation. The [complete proof](../docs/COMPLETE_PROOF.md) supplies the entire internal argument. The [frozen short argument](../docs/FROZEN_ARGUMENT.md) records the intended story; its historical planning footer does not change the later audit status. The [notation crosswalk](../docs/NOTATION_CROSSWALK.md) and [source ledger](../docs/SOURCE_TO_CANONICAL.md) explain how source fragments became the canonical account.

The [reference record](../docs/REFERENCES.md) distinguishes standard tools, closest antecedents, and the bounded priority assessment. It does not certify an absolute-first claim. No manuscript or publication metadata has been invented for this reader site.

## Reuse and publication

The repository remains private and no reuse license or public release has been selected. Its scientific source can be prepared for a public site later, but a private source repository alone does not guarantee a private hosted page. Public deployment is a separate decision. [Current project and site status](status.md)


---

[Previous: References and their roles](../docs/REFERENCES.md) · [Continue: Status and publication](status.md)

GitHub reading view generated from [the website source](../website/pages/materials.md). The equations, figure data and canonical captions retain their source meaning. Custom website navigation, local search and interactive color switching are not executed in this GitHub view.
