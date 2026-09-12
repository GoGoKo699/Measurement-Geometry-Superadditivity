# Confirmed license adoption

The owner explicitly confirmed MIT for original code, CC BY 4.0 for original prose, figures and data where applicable rights exist, Ruge Lin as rights holder and citation author, and authority to license the included original material. This change implements that decision on `release/public-readiness-v1`. It does not authorize publication of private history, a merge or a visibility change.

The starting commit is `a0ef38a9ea18145028a4e784242738d995e37e87`, tree `c1b4bb1f03b875cf3d9206400d91d59fa3acfac8`. Its reader parent is `1107ac899d2e267c6cf03509168623c13db4038c`; the scientific pin and unchanged `main` are `f0015c56a19fd953c6797b2c64d9b507105234e3`. The current review head and commit-specific CI results are recorded in [PR #5](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/pull/5). This report records local validation, not a prediction of CI success.

## Implemented

- The root [LICENSE.md](../LICENSE.md) assigns licenses by material. The [MIT text](../LICENSES/MIT.txt) exactly matches the reviewed candidate with the confirmed holder. The complete [CC BY 4.0 text](../LICENSES/CC-BY-4.0.txt) is an unchanged download from the official Creative Commons plaintext endpoint. Source URLs and file hashes are in [LICENSE_ADOPTION.json](LICENSE_ADOPTION.json).
- Root [CITATION.cff](../CITATION.cff) provides repository metadata. It invents no paper, DOI, version, release date, contact, ORCID or affiliation. Its bytes match the confirmed candidate and pass the full CFF 1.2.0 schema with format checks. GitHub's default-branch citation interface is not activated by an unmerged branch.
- Current README, status, materials and contribution wording reflects adoption. The website page sources remain in `website/pages/`; native `reader/` files were regenerated. Historical proposals and prior reports retain their original bytes and decision scopes.
- Every HTML footer links license scope, citation and third-party notices. Eight operative legal/citation/notice files are copied exactly and recorded by SHA-256, including the DejaVu and STIX notices for existing figure components. Both website dependency lists accompany the source downloads. Historical publication reviews are explicit repository-snapshot links rather than newly bundled evidence.
- Six targeted cases verify the download inventory and reject missing files, changed bytes even with a matching forged output hash, incorrect hashes, omitted entries and changed paths. They do not share or alter any numerical evaluator.

The notice requests an exact commit for reproducibility without adding an MIT license condition. Internal approval hashes attest only to original exports. Third-party components retain their own terms; the project licenses do not relicense dependencies, fonts or the external tutorial.

The complete staged `git diff --check` returns 2 solely for the official CC text's final blank line at line 396. Its exact bytes are intentionally retained. The same check excluding only that upstream file returns 0 for all project-authored changes; no source text was trimmed to obtain a pass. Both outcomes are recorded in `evidence/adoption-upstream-whitespace.json` and `evidence/adoption-authored-whitespace.json`.

## Local validation

Use the recorded dependency files in an isolated Python environment, without `-O`, and fresh output paths. Command records below contain actual arguments, return codes, durations and logs. The [environment record](evidence/adoption-environment.json) distinguishes local Python 3.12.14/Pandoc 3.1.3 from recorded CI Python 3.13.5/Pandoc 3.1.11.1.

| Command or comparison | Observed result | Evidence |
|---|---|---|
| `python verify.py` | Exit 0; 165 manifest entries, 27 approved graphical artifacts, independent verifier boundaries intact | [Command](evidence/adoption-verify.json), [log](evidence/adoption-verify.log) |
| `python -m pytest -q -p no:cacheprovider tests website/tests` | Exit 0; 102 tests passed in 9.45 seconds, 10.042 seconds wall time | [Command](evidence/adoption-tests.json), [log](evidence/adoption-tests.log) |
| `python website/repository_preview.py --write`, then `--check` | Generation completed; check exit 0; 10 native editorial pages, 7 canonical routes, 3 preserved display figures | [Check command](evidence/adoption-native.json), [log](evidence/adoption-native.log) |
| `python website/build.py --output build/license-adoption-review` | Exit 0; 17 routes, 761 MathML expressions | [Command](evidence/adoption-build.json), [log](evidence/adoption-build.log) |
| `python website/check.py --site build/license-adoption-review` | Exit 0; 1,306 local HTML links; eight exact operative downloads | [Command](evidence/adoption-site-check.json), [result](evidence/adoption-site-result.json) |
| Actual loopback HTTP requests | All eight operative downloads returned HTTP 200 and exact repository bytes | [HTTP evidence and repeat path](evidence/adoption-http-downloads.json) |
| `python publication/check_preparation.py` | Exit 0; 295 inherited files unchanged, 17 explicitly recorded editorial changes, both upstream font notices exact | [Command](evidence/adoption-preservation.json), [result](evidence/adoption-preservation-result.json) |
| Full CFF 1.2.0 schema and format validation | Passed using jsonschema 4.23.0 and the identity-checked upstream schema | [Schema and citation hashes](evidence/adoption-citation-schema.json) |
| Local browser attempt | Exit 1 before navigation: recorded Chromium executable absent | [Command](evidence/adoption-browser-attempt.json), [failure log](evidence/adoption-browser-attempt.log) |

The local browser attempt is blocked, not passed, and is not an authenticated inspection of GitHub's renderer. The existing PR reader workflow installs the recorded browser and tests actual HTTP navigation at `127.0.0.1`, including desktop/mobile layouts, math, search, keyboard controls, figure switching and no-JavaScript pages. Its actual result at the completed commit belongs in the PR record. The scientific workflow is intentionally skipped for this draft PR under its existing condition; no full certificate or simulation campaign is needed for these documentation changes.

To repeat CFF validation, retrieve the exact schema referenced in the evidence file outside the repository, check its SHA-256, and validate `CITATION.cff` with `jsonschema` 4.23.0 using `validators.validator_for(schema)` and that validator's `FORMAT_CHECKER`. The schema fetch is not a routine CI or build dependency.

## Preservation and remaining decisions

[ADOPTION_STARTING_FILES.json](ADOPTION_STARTING_FILES.json) records all 312 starting files. [ADOPTION_EDITS.json](ADOPTION_EDITS.json) enumerates the 17 authorized existing-file changes with before/after hashes; Git retains their readable diff. Every other starting file remains byte-identical. In particular, the canonical equations, scientific inputs, certificates, numerical implementations, expected outputs, captions, 27 protected graphical artifacts and three native display SVGs are preserved.

Only the README and STATUS entries changed in `BASELINE_MANIFEST.json`; restoring those two entries exactly recovers the prior manifest. Existing math in the eight edited prose sources is unchanged. See the [editorial preservation comparison](evidence/adoption-editorial-preservation.json). The independent checks establish packaging and editorial preservation, not a new proof or ownership adjudication.

[PUBLICATION.md](../PUBLICATION.md) remains the current publication checklist. Separate branch integration, consent to retained historical contact/project metadata, the two incompletely fetched historical binary objects, final integrated-tree validation and an explicit visibility instruction remain outstanding. The confirmed license choice does not resolve those items. No other project was accessed. The repository remains private, Pages is disabled, and no merge, history rewrite, release, manuscript or deployment was performed.
