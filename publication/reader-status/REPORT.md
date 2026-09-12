# Current reader-status presentation

The reader pages now lead with the complete scientific account and its scope. Branch creation, adoption and integration chronology is available through one optional [provenance index](../PROJECT_HISTORY.md). The author-approved email is visible as ordinary contact information. This change does not alter scientific claims or repository visibility.

Starting commit: `ba5fe59a31b7b833a458ee3761fbc9777d8c47e4`; tree: `4adee205cbb23ff54b16094f0084593fa0c97aa0`. The local starting tree was clean, and authenticated repository inspection confirmed the same main commit, private visibility and disabled Pages. Work is on `reader/current-status-v1`, with the existing merge authorization and CI gates retained.

## Reading route

| Reader task | Before | After |
|---|---|---|
| Is the project complete? | Status led with branch history and integration authorization | Overview and status identify the completed model, proof, evidence and figures, with exact limits |
| Inspect the scientific result | Theorem, proof, figures and verification were linked directly | All expert routes and mathematical content retained |
| Trace a claim | Material inventory mixed sources with correction and license chronology | Inventory links scientific sources; history is optional below it |
| Contact the author | Email existed in Git and copied metadata | Ordinary mail link in overview, status and material inventory |
| Maintain the reader | Current and historical stage wording mixed | `website/pages/` remains the source; historical stages are labeled and retained |

The conclusion about completeness uses the existing bounded C1–C6 account and canonical M07–M08 limitations. It does not assert external peer review, absolute priority, an exact capacity formula, practical decoding or a completed manuscript. The recorded scientific results at the starting commit are linked in the [verification guide](../../reader/verification.md#recorded-checks); this presentation work is not another scientific audit.

## Preservation and validation

The current preservation check passed against all 406 files at the starting commit: 375 are byte-identical and 31 have explicit editorial or generated changes. All canonical scientific documents, equations, inputs, certificates, independent evaluators, reference evidence, captions, 27 protected graphical exports and three accepted-palette SVGs are byte-identical. The earlier integration checker, edit record and evidence are unchanged and also pass on their exactly reconstructed historical tree. Only the README and STATUS identities change in the root scientific manifest. `verify.yml` and `reader-site.yml` are unchanged; the two presentation/inspection gates call the new preservation stage.

Local environment: isolated Python 3.12.14, assertions enabled, Pandoc 3.1.3, beautifulsoup4 4.14.3, Playwright 1.57.0; BLAS and OpenMP thread counts set to one. CI retains recorded Python 3.13.5 and Pandoc 3.1.11.1. Cross-version HTML byte identity is not claimed.

| Check | Actual local result | Record |
|---|---|---|
| `python verify.py` | Passed; 166 manifest entries, 27 graphical artifacts | [Log](../evidence/reader-status-verify.log) |
| `python -m pytest -q -p no:cacheprovider tests website/tests` | 197 passed in 11.65 seconds | [Log](../evidence/reader-status-tests-final.log) |
| `python website/repository_preview.py --write`, then `--check` | 14 generated outputs checked, 17 reading routes | [Check log](../evidence/reader-status-preview-final.log) |
| `python publication/reader-status/check_reader_status.py --output build/current-reader-preservation-final.json` | Passed; exact current changes and historical integration replay | [Log](../evidence/reader-status-preservation-final.log) |
| `python website/build.py --output build/current-reader-review-final` | Built 17 routes with 761 MathML expressions | [Log](../evidence/reader-status-html-final.log) |
| `python website/check.py --site build/current-reader-review-final` | Passed structure, internal links and source checks | [Log](../evidence/reader-status-html-check.log) |

Each log has a same-stem JSON command record with UTC start, return code, elapsed time and limits. The local runtime has no Chromium executable, so no local browser pass is claimed. The unchanged CI browser workflow installs Chromium and performs actual loopback HTTP checks; its outcome will be recorded in the pull request. GitHub's authenticated Markdown renderer, Firefox and Safari were not inspected. No new local full certificate or simulation run was performed for this prose work. Existing scientific CI remains required before merging.

Initial presentation checks found and resolved three issues: a root-document link used a generated named anchor where the inherited integrity checker expects an explicit ID, an explicit verification anchor duplicated its automatically generated heading ID, and the native-link test treated a valid `mailto:` URI as a file path. The root link now targets the page, the heading has a distinct name, and the test validates the mail address before checking file paths. The two failed tests and 195 successes from the first suite remain in [the original log](../evidence/reader-status-tests.log); no scientific tolerance or expected result was changed. Raw diagnostic whitespace is retained in that log.

## Documented reader walkthroughs

1. A new reader reaches the physical result first, then the selected Preskill route or channel explanation. Project status says what is complete before explaining the boundaries. No historical report or second tutorial is assigned.
2. An expert retains direct theorem, full-proof, figure and evidence links. The verification guide distinguishes stored evidence and actual executed checks, with exact commit/run attribution.
3. A reader traces displayed quantities through the unchanged atlas and source inventory. Optional provenance links preserve earlier corrections and approvals, while their pending-stage wording is not presented as the current status.

These are the assistant's documented walkthroughs, not external user testing. No source PDF, screenshot or copied tutorial content was added. No scientific source, caption, graphical asset, license text or citation identity was changed. Repository visibility, hosting and history remain unchanged.
