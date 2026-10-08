# Reproduction and verification

Run all commands from the repository root. They use the included local sources and preserve the mathematical sources and reference results. Choose a new output directory for each run.

## Environment

`requirements.txt` pins the versions used for the scientific graphics and verification records. `ENVIRONMENT.json` records the interpreter and platform for the validation checks. To install dependencies use a new virtual environment. Installing them requires normal package availability; subsequent computations do not require internet. Do not use Python `-O`, which disables assertions used by the proof checkers.

Exact graphics bytes depend on the numerical/rendering environment. The approved outputs are included in the repository. In the recorded environment, regenerated PDF/SVG/PNG and review output bytes must match the approval manifest; the command fails rather than silently replacing a figure. No standalone font is distributed. The renderer uses the DejaVu fonts available with the pinned Matplotlib environment and never invokes TeX or an image-generation service.

## Choose the verification scope

| Command | What it executes | Scope |
|---|---|---|
| `python verify.py` | Source/fragment identities, dependency graph, local links, file manifest, independent-code boundaries, protected figures | Repository integrity |
| `python -m pytest -q -p no:cacheprovider tests` | Method tests, malformed-input/coverage controls, figure coordinate and notation tests | Targeted verification of methods and controls |
| `python reproduce.py --output build/figures-check` | Rebuild all figure inputs, check their exact values/domains, render all components/figures, compare approved bytes, run tests | Figure reproduction and targeted tests |
| `python reproduce.py --output build/full-check --full` | All of the above plus the three complete verifiers, witness and controls, endpoint constants and physical checks | Complete computational verification, including all 29,635 certificate leaves |

`python verify.py --full --output build/another-full-check` is an alias for full reproduction. Paths outside the package may be used; within it, generated outputs are restricted to `build/`. All output directories must be new.

## Complete certificate and independent routes

The single canonical rational partition is [certificates/common_noise_compact_certificate.json](../certificates/common_noise_compact_certificate.json): 512 noise bands and 29,635 compact input leaves, with analytic nearly pure tails. The low- and high-noise endpoint arguments are in [P05–P07](COMPLETE_PROOF.md#p05).

| Implementation | Direct command from the root | Output |
|---|---|---|
| Integer/dyadic | `python verification/integer/certify_all_noise.py --verify certificates/common_noise_compact_certificate.json --output build/integer --bits 224` | `verification_224.json` |
| mpmath interval | `python verification/mpmath/cross_backend.py --certificate certificates/common_noise_compact_certificate.json --output build/mpmath85.json --digits 85` | Complete-domain independent-backend result |
| Decimal | `python verification/decimal/verify_certificate.py --certificate certificates/common_noise_compact_certificate.json --output build/decimal130.json --precision 130` | Complete-domain different-envelope result |

Create parent output directories for individual commands where needed; the root reproduction command handles this itself. The three implementations use the same mathematical claim and exact rational partition, with independent numerical entropy evaluators. The output names and differing margins reflect different valid bounds; same-environment results are compared against their own immutable records.

To reconstruct the partition itself:

```bash
python reproduce.py --output build/full-with-cover --full --rebuild-certificate
```

This additionally constructs the cover at 128 bits and checks that the resulting rational certificate matches the included one. Rebuilding is not needed just to verify every inequality on the included cover. A generation failure or disagreement is reported, not silently accepted as another partition.

## Witness and controls

The canonical Figure 1 input is [the original 140-digit posterior-state record](../data/figures/figure1_original_witness140.json). The full run recalculates it at 100 and 140 digits, compares the exact recorded JSON, and checks the independently implemented mpmath effect-determinant interval contains the tighter Decimal interval. All nine measured-count contributions remain in both records.

The effect-determinant wrapper evaluates the eight-use witness and two safeguard controls. A positive mixed-input counterexample checks that nearly pure inputs are not assumed to give the global optimum. A negative-rate control checks that floating-point error is not mistaken for a positive witness.

Endpoint identities are independently checked by the symbolic/rational code; their continuous-domain proofs remain in the canonical document. The physical checker explicitly mixes the hidden true projective outcomes into reported signs before obtaining small receiver/reference matrices. It does not build an eight-use full density matrix or prove a global theorem by sampling.

## Figure reproducibility

The figure pipeline reads the included numerical inputs, checks their exact values and parameter domains, and renders the three figures and their components. All 27 approved graphical artifacts, including panels, preview PNGs and the captioned review PDF, must match [APPROVED_FIGURE_HASHES.json](../provenance/APPROVED_FIGURE_HASHES.json). The numerical CSV files and exact witness are protected inputs; build metadata records the local input manifest.

[The mathematical-content record](../provenance/MATHEMATICAL_CONTENT_CHECK.json) checks the identities of 137 displayed canonical equations. `provenance/FILE_LINEAGE.json` records source hashes and function/class identities for reproducibility.

## Sources and recorded results

The source documents in `provenance/text_sources/` support exact fragment mappings; source names and SHA-256 values identify their contents. All runtime dependencies are available through direct repository paths.

`validation/BASELINE_VALIDATION.json` records the validation results and distinguishes computational reruns from mathematical review. After a layout or import change, replay affected numerical paths against the reference outputs. The computational checks provide reproducible evidence from independent numerical implementations.
