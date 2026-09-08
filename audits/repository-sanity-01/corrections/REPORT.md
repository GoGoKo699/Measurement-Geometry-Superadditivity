# Implementation of the audit corrections

Date: 8 September 2026. Repository: `GoGoKo699/Measurement-Geometry-Superadditivity`. Starting audit commit: `5e367b1e541bf7d5ba1af90e85796d59db9e03f4`. Audited scientific baseline: `f0015c56a19fd953c6797b2c64d9b507105234e3`. Work remains on `audit/repository-sanity-01`; `main` is unchanged.

**All three documentary findings are corrected.** The optional loopback-server improvement is also implemented. Integrity, 108 combined tests, figure reproduction, native reader generation, HTML static checks and actual loopback HTTP resource checks passed. Both environment limitations remain open after bounded standard installation retries. No manuscript, scientific extension, merge, deployment or source repair beyond these documentary changes was performed.

## Findings and disposition

| Finding | Implemented correction | Status |
|---|---|---|
| ATTR-01: historical rate/threshold overstatement | Added a dated note in [REFERENCES.md](../../../docs/REFERENCES.md#s6-correction), linked beside S6 in [SOURCE_TO_CANONICAL.md](../../../docs/SOURCE_TO_CANONICAL.md#s6). The note distinguishes improved dephrasure rates from an extension beyond weighted-repetition thresholds, with the exact primary-paper sections. | Closed. Historical S6 bytes preserved. |
| DOC-01: eight incorrect figure-input paths | Corrected each `data/<file>` reference to `data/figures/<file>` in [FIGURE_SPECIFICATIONS.md](../../../figures/FIGURE_SPECIFICATIONS.md). All eight files exist. | Closed. Numerical values and figure specifications otherwise unchanged. |
| DOC-02: obsolete remote-repository status | Removed the false pre-repository clause from the final sentence of model section M08. Its canonical line range is unchanged; only the M08 current-fragment digest changes in the section ledger. | Closed. Mathematical model and proof unchanged. |
| Optional local-preview binding | Added `--bind 127.0.0.1` to WEBSITE's server command and the generated START_HERE command; the documented URL now uses the same address. | Implemented. |
| ENV-01: Chromium unavailable | Retried one standard Playwright installation. Official CDN timeouts and standard mirror HTTP 400 responses prevented installation. | Still blocked. Zero browser pages tested in this follow-up. |
| ENV-02: recorded Pandoc unavailable | Retried the official Pandoc 3.1.11.1 download once; curl returned 28 after a proxy connection timeout. | Still blocked. HTML built and checked with available 3.1.3. |

The attribution correction was rechecked against [Bhalerao–Leditzky, arXiv:2508.09978v1](https://arxiv.org/html/2508.09978v1), §5.2 after Eq. (5.34) and §6.1. Comparisons with neural-network codes are a different benchmark. The historical source and original audit report are retained as evidence, with the current qualification visible through the canonical reader route.

## Preservation and dependent identity records

The repository hashes entire source documents, including their status prose. Removing the obsolete M08 sentence therefore changes its document digest even though every equation is identical. Four dependent provenance records now identify that corrected document: `CANONICAL_INPUTS.json`, the source portions of `SOURCE_IDENTITY.json` and `BUILD_RECORD.json`, and their entries in `FIGURE_INPUTS.json`. These changes update document identity only. No numerical value, row count, precision, witness bound, certificate, scientific expected result or approved figure hash was replaced.

[EDITORIAL_CORRECTIONS.json](../../../provenance/EDITORIAL_CORRECTIONS.json) records exact before/after hashes and reversible substitutions for five documentary/ledger files and four dependent identity files. The website validator reconstructs the original bytes and compares them to the unchanged historical website manifest. It also checks equation-byte equality, restricts the ledger change to M08's digest, and restricts the four identity files to their explicitly named hash fields. Negative tests reject unauthorized equations, witness/CSV hashes, row counts, precision changes and malformed correction records. No numerical evaluator was refactored or shared.

The current root manifest records these authorized changes. The original website manifest, approval record, historical excerpts and original audit evidence remain unchanged. Root and website status pages explain the corrections and remaining environment limits; native reader outputs were regenerated from their sources.

[CORRECTION_CHECK.json](CORRECTION_CHECK.json) independently verifies all 208 pinned source members: 191 remain byte-identical and 17 changed only within the enumerated documentary, reader, metadata and preservation-check scope. It also verifies all 145 original audit evidence files, all 27 approved graphics, and all eight numerical files under `data/figures/`. The other two files in that data directory are the explicitly updated source-identity records. All verification implementations, the full proof, frozen argument, mathematical inputs and rational certificate remain byte-identical.

## Actual verification

The same isolated Python environment and recorded dependency pins were used, with assertions enabled and BLAS/OpenMP threads limited to one. Each recorded principal command includes its exact arguments, UTC start, duration, return code, environment overrides and child maximum RSS in the adjacent JSON/log pair. No browser success is inferred from these checks.

| Command | Return code | Wall seconds | Result |
|---|---:|---:|---|
| `python verify.py` after initial identity integration | 0 | 0.274 | Provenance, source/claim coverage, protected artifacts and current manifest pass; final figure reproduction repeats integrity before and after. |
| `python -m pytest -q -p no:cacheprovider tests website/tests` | 0 | 21.567 | **108 passed**; pytest reports 19.97 seconds. |
| `python reproduce.py --output build/audit-corrections-figures-final` | 0 | 10.050 | All ten current plotting/provenance outputs reproduced exactly; all **27 approved graphics byte-identical**. |
| `python website/repository_preview.py --write`, final generation | 0 | 0.073 | Regenerated native pages/manifest; derived figure bytes unchanged. |
| `python website/repository_preview.py --check`, final check | 0 | 0.069 | All 13 generated files match. |
| `python website/build.py --output build/audit-corrections-site` | 0 | 9.268 | 16-page site, 664 MathML expressions, ten figure color derivatives. |
| `python website/check.py --site build/audit-corrections-site --report .../SITE_CHECK.json` | 0 | 1.838 | 1,035 local links and canonical equations checked. |
| Existing independent HTTP resource checker against the new site | 0 | 1.284 | 108 resources, 6,397,725 bytes, all HTTP 200 and byte-identical to local files. Server bound only to `127.0.0.1` and stopped afterward. |
| New independent correction check | 0 | 0.074 | Exact preservation and finding-resolution checks described above. |

Fresh figure evidence is under [figure-reproduction](figure-reproduction/), including logs, result/validation records, source identities and an output hash manifest. Regenerated graphics are not duplicated again because all their bytes match the existing protected exports. Website evidence is in [SITE_CHECK.json](SITE_CHECK.json), [SITE_BUILD_RECORD.json](SITE_BUILD_RECORD.json) and [HTTP_LINK_CHECK.json](HTTP_LINK_CHECK.json).

Two intermediate failures are preserved. The first integrity run correctly rejected the old model-document digest before dependent metadata was updated. The first figure replay then correctly rejected BUILD_RECORD's still-old embedded source digest. Their logs are [integrity.log](integrity.log), [figures.log](figures.log) and [initial-figure-attempt](initial-figure-attempt/). Only the documented identity fields were subsequently corrected; assertions, tolerances and numerical reference values were untouched. Both final routes passed.

The full all-noise certificate and eight-use scientific audit was not rerun in this correction pass. It remains recorded at the starting audit commit and applies to the mathematically unchanged source, inputs and implementations. This pass verifies the actual affected document-to-data-to-render route and preservation behavior.

## Remaining environment boundary and replay

[runtime/README.md](runtime/README.md) and its command records preserve the bounded retries: Pandoc download exit 28 after 10.032 seconds; Playwright installation exit 1 after 108.195 seconds. A separately reported cancelled tool polling operation is recorded distinctly from the completed curl failure. No network restriction was bypassed.

Desktop/mobile browser layout, live MathML rendering, search, keyboard controls, color switching and no-JavaScript browser access remain unverified here. Neither authenticated GitHub rendering nor Safari/Firefox was tested. Static checks and loopback HTTP retrieval do not establish those behaviors. The smallest remaining task is to run the existing Chromium checker once the recorded dependencies are available.

From a checkout of this correction commit, use fresh output paths and the recorded Python requirements:

```bash
python verify.py
python -m pytest -q -p no:cacheprovider tests website/tests
python reproduce.py --output build/correction-replay-figures
python website/repository_preview.py --check
python website/build.py --output build/correction-replay-site
python website/check.py --site build/correction-replay-site
python audits/repository-sanity-01/corrections/check_corrections.py --root . --output build/correction-replay-check.json
```

For the remaining browser task, install the recorded Pandoc and Playwright Chromium runtime, then serve the new site with `python -m http.server 8765 --bind 127.0.0.1 --directory build/correction-replay-site` and run `python website/browser_check.py --site build/correction-replay-site --output build/correction-replay-browser --base-url http://127.0.0.1:8765`. Stop the server after review. No further scientific task is indicated by these corrections.
