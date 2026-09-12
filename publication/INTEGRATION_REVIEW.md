# Review of the intended publication tree

**12 September 2026. Reviewed integration plan and unapplied patch only.** This review starts at `857d173c79140b5c2643c1a7d16b4a2321ed8dd4` on `release/public-readiness-v1`. It does not authorize or perform a merge, history rewrite, visibility change, deployment or new scientific study. Read [PUBLICATION.md](../PUBLICATION.md) for the separate owner decisions. The confirmed licenses remain operative on the preparation branch.

The smallest scientific-account integration is to carry forward the nine documentary and dependent identity corrections already recorded at `9ccecbf4cd3d975de2c498ba4fe2a9862f90778b`, while retaining the current Preskill reader, adopted licensing and browser-capable build. Replacing the current reader with the older audit versions would lose completed work.

## Inspected sources and exact comparison

The local checkout was clean at the starting commit. Its reader parent is `1107ac899d2e267c6cf03509168623c13db4038c`; the scientific pin is `f0015c56a19fd953c6797b2c64d9b507105234e3`. Local objects did not contain the correction commit, so its actual GitHub commit diff, correction report, correction metadata and checker were read through the repository connection. No other project was accessed.

The GitHub comparison from the scientific pin to the correction head reports two commits and 229 changed paths. Of these, 210 are under `audits/repository-sanity-01/` and 19 are outside it. The correction commit's parent is audit commit `5e367b1e541bf7d5ba1af90e85796d59db9e03f4`; its tree is `3b52207c7dfaea9975aaafe113764841f99acd7c`.

The seven path overlaps between those changes and the current release branch are:

- `BASELINE_MANIFEST.json`
- `STATUS.md`
- `WEBSITE.md`
- `reader/PREVIEW_MANIFEST.json`
- `reader/status.md`
- `website/build.py`
- `website/pages/status.md`

This is a path-overlap inventory, not a claim that Git has tested a full branch merge. No merge was attempted. The current branch's canonical nine files still match every before-hash in the correction record, so their precise documentary substitutions are unambiguous.

The inspected historical [correction report](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/blob/9ccecbf4cd3d975de2c498ba4fe2a9862f90778b/audits/repository-sanity-01/corrections/REPORT.md) records 108 tests, exact figure reproduction, and then-blocked browser dependencies. Those counts and limitations belong to that commit. Later reader and license checks have their own records; neither set proves a future integrated tree.

## Minimal core payload

[core-corrections.patch](integration/core-corrections.patch) is an **unapplied** patch against the release starting commit. It contains only the following nine existing-file changes. [CORE_PATCH_REPLAY.json](integration/CORE_PATCH_REPLAY.json) records their exact before/after hashes and the patch digest.

| File | Exact intended change |
|---|---|
| `docs/REFERENCES.md` | Preserve the original consolidation date as historical; add the dated S6 rate/threshold qualification and its existing primary-source reference. |
| `docs/SOURCE_TO_CANONICAL.md` | Link that qualification beside S6 and identify the reversible editorial correction record. |
| `figures/FIGURE_SPECIFICATIONS.md` | Correct eight `data/<name>` paths to `data/figures/<name>`. No input contents change. |
| `docs/MODEL_AND_CLAIMS.md` | Remove only the obsolete clause saying no remote repository has been created from M08. |
| `provenance/SECTION_LEDGER.json` | Update only the M08 current-fragment hash for that clause removal. |
| `provenance/CANONICAL_INPUTS.json` | Update only the model-document hash. |
| `data/figures/SOURCE_IDENTITY.json` | Update only the model-document and canonical-manifest hashes. |
| `data/figures/BUILD_RECORD.json` | Update those same two hashes inside the embedded source identity. |
| `provenance/FIGURE_INPUTS.json` | Update only the two affected identity-record hashes. |

All 21 recorded substitutions were replayed in memory. Each original text occurred once; every resulting file matched the recorded correction after-hash. The extracted dollar-delimited mathematical expressions in all four Markdown files matched before and after. This checks the exact documentary payload, not scientific correctness. `git apply --check publication/integration/core-corrections.patch` returned 0 without changing live files.

The patch deliberately omits ancillary integration work below. Applying it alone would cause existing preservation checks to reject the changed document identities. A successful dry-run is not permission to apply it and does not establish a buildable final tree.

## Ancillary changes needed in the candidate

| Current location | Required integration treatment |
|---|---|
| `provenance/EDITORIAL_CORRECTIONS.json` | Import the exact existing record from correction commit `9ccecbf4`; its SHA-256 is `3e3207a166379b4f8714e711e73b9e4a1ec25d299abdc248e5c0a9815c4e56d8`. Do not write a broader permission record. |
| `website/build.py` | Port the correction commit's `date` import, three explicit correction-file sets, `verify_editorial_corrections`, and its `verify_baseline` composition into the current builder. Preserve current Markdown heading preparation, Preskill expansion, routes, license/citation downloads and footer. The existing loopback command already satisfies the older optional correction. |
| `website/tests/test_default_style.py` | Port the correction-aware preservation test. It must check the exact nine-file set, five documentary/ledger files and four identity records, while retaining the current figure-only styling tests. |
| `website/tests/test_editorial_preservation.py` | Carry over the existing negative tests for malformed records, nonunique substitutions, altered equations, unrelated ledger changes, numerical hashes, precision and row counts. These are presentation/provenance tests, not a consolidation of scientific evaluators. |
| `website/tests/test_learning_bridge.py`, `test_starting_science_and_graphical_artifacts_are_unchanged` | Its current raw-byte condition must recognize only the nine verified reversible changes. Continue requiring exact original proof, verifier, certificate, caption and graphical bytes. The model must remain covered by reconstruction and equation preservation rather than being silently dropped from the required set. |
| `BASELINE_MANIFEST.json` | Carry only the nine corrected file identities and the exact new correction-record entry, plus current authorized README/STATUS identities. Do not replace the whole manifest with its older audit copy or update protected scientific hashes. Reversing the nine documented changes and current root editorial entries must recover the frozen manifest. |
| `STATUS.md`, `website/pages/status.md` | Explain that the candidate includes the recorded documentary corrections. Preserve adopted licensing and distinguish historical browser limitations from later successful reader CI. Avoid restoring the old pending-license or globally unverified-browser wording. |
| `WEBSITE.md` | Describe correction-aware reconstruction while retaining the current 17-route Preskill and license/download maintenance instructions. Keep loopback examples. |
| `reader/status.md`, `reader/PREVIEW_MANIFEST.json` | Regenerate through the current native generator; never copy the audit branch's old generated files. |
| `PUBLICATION.md`, `publication/READINESS.json` | Update the candidate-stage description and remaining decisions without claiming any merge, visibility change or final-tree PASS prematurely. Record new edits separately from the completed license adoption. |

The other historical audit files need not be copied into the minimal content patch: existing pinned GitHub links already preserve their provenance. Their eventual public distribution, including retained branches and history, remains part of the disclosure decision. Avoid copying the entire 210-file evidence tree merely to obtain the three documentary corrections.

Three preservation scripts have intentionally narrower historical scopes:

- `website/review/check_preservation.py` accepts only the original reader edit set and reconstructs a manifest with two root-document hash changes. It will reject the nine corrections.
- `publication/check_preparation.py` and `publication/ADOPTION_EDITS.json` identify the completed license adoption at exact before/after hashes. They will reject further changes to inherited files.
- The audit's `corrections/check_corrections.py` accepts its old 17-file correction set and will reject the later README and Preskill changes.

Do not broaden those historical records or refresh their expected hashes to make an integration pass. Keep them commit-scoped. Add a small current integration check and edit record that composes the exact reader/adoption state with the exact nine-file correction record and the explicitly listed ancillary adaptations. Run historical checkers at their recorded commits if a replay is needed. A skipped historical replay is not a new integrated-tree pass.

## Preparation and validation sequence

1. Recheck branch heads and the release working tree. Confirm that no new overlapping edit changes this comparison. Keep the finished license and reader commits as the base.
2. Prepare a separate candidate worktree or an offline patch series. The supplied core patch can be dry-run checked without a merge; after authorization, apply it together with the exact correction metadata and ancillary adaptations. Preserve existing audit/reader/adoption reports as historical records.
3. Regenerate native reader outputs and check their consistency. Verify the S6 return link, all eight data paths, M08 wording, selected tutorial routes, source downloads and license notices in both reading interfaces.
4. Run the bounded integrity, presentation and figure routes below with recorded dependencies and fresh directories. The default figure replay is sufficient to resolve the changed documentary source identities; it does not run the full entropy certificate.
5. Inspect actual reader CI and browser results at the complete candidate commit. Keep the PR draft during preparation. In the existing workflow, making any PR ready starts both scientific jobs, including `reproduce.py --full`; that gate needs to be scheduled explicitly as part of an authorized integration. Do not alter its condition or call a skipped job passed.
6. After explicit integration authorization, preserve the stacked PRs: merge reader PR #4 to `main`, then retarget/review the complete preparation PR #5 against that updated `main` before its separate merge. Recheck exact heads and CI after each base change. An alternative stack order needs the same final-tree validation; no merge order is executed by this report.

The applicable candidate commands are:

```bash
python website/repository_preview.py --write
python website/repository_preview.py --check
python verify.py
python -m pytest -q -p no:cacheprovider tests website/tests
python reproduce.py --output build/integration-review-figures
python website/build.py --output build/integration-review-site
python website/check.py --site build/integration-review-site
```

Run the new integration-preservation check as well once it exists. Do not substitute an unmodified adoption checker as proof that subsequent changes are authorized. For actual HTML browser review, serve only on loopback:

```bash
python -m http.server 8765 --bind 127.0.0.1 --directory build/integration-review-site
python website/browser_check.py --site build/integration-review-site --output build/integration-review-browser --base-url http://127.0.0.1:8765
```

Stop the server after review. Inspect desktop/mobile routes, mathematics, source and license downloads, local search, keyboard navigation, figure switching and no-JavaScript reading. Native Markdown anchors are a separate check; do not describe HTML browser results as inspection of GitHub's authenticated renderer.

No core correction, ancillary adaptation, branch integration or scientific replay was executed in this review. The only new artifacts are this review, the unapplied patch and its in-memory replay record. There is no new mathematical concern or scientific research task indicated by this comparison. Final public clearance still depends on the separate history/distribution review, explicit integration and visibility decisions, and checks at the actual intended final tree.
