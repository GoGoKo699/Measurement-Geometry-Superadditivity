# Reproduction and evidence boundaries

All commands are run from the unpacked baseline root. They use local files, not archived packages or the old entanglement repository. Mathematical source and reference results are never overwritten. Choose a new output directory for each run.

## Environment

`requirements.txt` pins the versions used to create the accepted scientific graphics and verification records. `ENVIRONMENT.json` records the interpreter/platform for the current packaging checks. To install dependencies use a new virtual environment. Installing them requires normal package availability; subsequent computations do not require internet. Do not use Python `-O`, which disables assertions used by the inherited proof checkers.

Exact graphics bytes depend on the numerical/rendering environment. The approved output files remain included regardless. In the recorded environment, regenerated PDF/SVG/PNG and review output bytes must match the approval manifest; the command fails rather than silently replacing a figure. No standalone font is distributed. The renderer uses the DejaVu fonts available with the pinned Matplotlib environment and never invokes TeX or an image-generation service.

## Four different kinds of check

| Command | What it executes | What it does not establish |
|---|---|---|
| `python verify.py` | Source/fragment identities, dependency graph, local links, file manifest, independent-code boundaries, protected figures | Does not evaluate the global entropy inequality |
| `python -m pytest -q -p no:cacheprovider tests` | Method tests, malformed-input/coverage controls, figure coordinate and notation tests | Does not replace the complete 29,635-leaf verification |
| `python reproduce.py --output build/figures-check` | Rebuild all figure inputs, check their exact values/domains, render all components/figures, compare approved bytes, run tests | Does not rerun the global entropy proof |
| `python reproduce.py --output build/full-check --full` | All of the above plus the three complete verifiers, retained witness and controls, endpoint constants and physical checks | Is a reproducibility check after relocation, not an external scientific audit |

`python verify.py --full --output build/another-full-check` is an alias for full reproduction. Paths outside the package may be used; within it, generated outputs are restricted to `build/`. All output directories must be new.

## Complete certificate and independent routes

The single canonical rational partition is [certificates/common_noise_compact_certificate.json](../certificates/common_noise_compact_certificate.json): 512 noise bands and 29,635 compact input leaves, with analytic nearly pure tails. The low- and high-noise endpoint arguments are in [P05–P07](COMPLETE_PROOF.md#p05).

| Implementation | Direct command from the root | Output |
|---|---|---|
| Integer/dyadic | `python verification/integer/certify_all_noise.py --verify certificates/common_noise_compact_certificate.json --output build/integer --bits 224` | `verification_224.json` |
| mpmath interval | `python verification/mpmath/cross_backend.py --certificate certificates/common_noise_compact_certificate.json --output build/mpmath85.json --digits 85` | Complete-domain independent-backend result |
| Final-audit Decimal | `python verification/decimal/verify_certificate.py --certificate certificates/common_noise_compact_certificate.json --output build/decimal130.json --precision 130` | Complete-domain different-envelope result |

Create parent output directories for individual commands where needed; the root reproduction command handles this itself. These substantive implementations are retained byte-identically from the audited sources. They share the stated mathematical claim and exact rational partition, not a common numerical entropy evaluator. The output names and differing margins reflect different valid bounds; same-environment results are compared against their own immutable records.

To reconstruct the partition itself:

```bash
python reproduce.py --output build/full-with-cover --full --rebuild-certificate
```

This additionally constructs the cover at 128 bits and checks that the resulting rational certificate matches the included one. Rebuilding is not needed just to verify every inequality on the included cover. A generation failure or disagreement is reported, not silently accepted as another partition.

## Retained witness and controls

The canonical Figure 1 input is [the original 140-digit posterior-state record](../data/figures/figure1_original_witness140.json). The full run recalculates it at 100 and 140 digits, compares the exact recorded JSON, and checks the independently implemented mpmath effect-determinant interval contains the tighter Decimal interval. All nine measured-count contributions remain in both records.

The original effect-determinant functions are retained without mathematical changes; their historical broad-example CLI was replaced by a wrapper selecting only the eight-use witness and the two declared safeguard controls. The controls are a positive mixed-input counterexample to an unjustified nearly pure optimum and a negative rate at a formerly misleading floating-point candidate. They are verification evidence, not extra main-text results.

Endpoint identities are independently checked by the retained symbolic/rational code; their continuous-domain proofs remain in the canonical document. The physical checker explicitly mixes the hidden true projective outcomes into reported signs before obtaining small receiver/reference matrices. It does not build an eight-use full density matrix or prove a global theorem by sampling.

## Figure reproducibility and approval

The complete scientific drawing code is unchanged except for direct local input paths and output defaults. Canonical plotting formulas and scalar comparisons are unchanged. Source-access adapters no longer unpack nested archives. `provenance/FILE_LINEAGE.json` records old/new hashes, exact patches and unchanged function/class ASTs. [The 137 displayed canonical equations](../provenance/MATHEMATICAL_CONTENT_CHECK.json) are byte-identical to their approved source consolidation.

Eight scientific input files remain exactly as specified; the two build/source metadata JSON files are regenerated to describe local unpacked inputs instead of an old ZIP. The numerical CSV contents and the exact retained witness are not altered by that metadata update. The renderer's new metadata reflects the current input manifest. All 27 approved graphical artifacts, including panels, preview PNGs and the captioned review PDF, must match the original bytes.

The original review footer and original render records predate visual approval and remain unchanged. The current approval is recorded separately in [APPROVED_FIGURE_HASHES.json](../provenance/APPROVED_FIGURE_HASHES.json). The historical contract's `rendered: false` means it was written at the specification stage, not that the current baseline lacks figures.

## Provenance and independent execution

The canonical model/proof now use direct active paths. Original textual sources retained for exact fragment mappings live under `provenance/text_sources/`; superseded executable source is stored as nonexecuted text when it is needed to check a historical fragment. The original archive names and SHA-256 values identify provenance but are not runtime dependencies. No nested ZIP/TAR is included or unpacked by the active code.

The stored author-side audit is not relabeled as external verification. `validation/BASELINE_VALIDATION.json` distinguishes fresh packaging/rerun operations from inherited mathematical review. After a layout or import change, affected numerical paths must be replayed against the reference outputs before the new package is frozen. No old manuscript, raw many-body data, or old repository clone is needed.
