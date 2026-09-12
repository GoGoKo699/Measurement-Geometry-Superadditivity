# Offline documentary integration candidate

The files described here are inside the unapplied [complete candidate patch](complete-candidate.patch). [Exact patch identity and local command results](CANDIDATE_CHECKS.json) accompany it. Candidate-only maintenance files are named as paths below; they are not active on the release branch.

**12 September 2026. Local candidate checks passed; the release source remains unchanged.** This candidate carries the exact nine documentary and dependent identity corrections from `9ccecbf4cd3d975de2c498ba4fe2a9862f90778b` into the completed Preskill reader and adopted license terms. It was prepared in a separate detached worktree and remains uncommitted. No branch merge, public release, visibility change, manuscript or new scientific repair is included.

The initial worktree basis was `5ec87029cb3ef0067ad2a8f1f1a66027041c9513`. The publication-closure delta was then copied exactly, without a merge, from `234e86439f44d7387134648ff088cf480ee1cd12`, tree `20149d6b68826f01b5a33ada7ff89ced5fc0afab`. That is the final comparison and patch basis. The copied delta closes the historical-binary inspection item through separate evidence; it changes no science. The candidate does not edit its current `PUBLICATION.md`, `publication/READINESS.json` or completed followup records.

Candidate preservation checker (`check_candidate.py`, inside the patch) · Starting file identities (`CANDIDATE_STARTING_FILES.json`, inside the patch) · Exact candidate edits (`CANDIDATE_EDITS.json`, inside the patch) · [Original integration review](../INTEGRATION_REVIEW.md)

## What the candidate changes

The nine core changes exactly match EDITORIAL_CORRECTIONS.json (`../../provenance/EDITORIAL_CORRECTIONS.json`, inside the patch). They qualify S6's dephrasure rate/threshold comparison, correct eight figure-input paths, remove M08's obsolete no-remote-repository clause, and update only the dependent documentary identity fields. Every after-hash matches the completed correction commit. The old metadata itself is copied byte for byte, including its original before-hashes and exact reversible substitutions.

Nine ancillary existing files adapt the current builder, preservation tests, root manifest, status documentation and generated native status/manifest. The builder retains the Preskill reading map, heading preparation, 17 routes, all eight license/citation downloads, source mathematics, local search and figure controls. It adds the candidate check/report downloads used by the status page. The accepted palette remains inside figures.

The root scientific manifest changes only for the nine recorded correction identities, their new exact correction-record entry and the current status hash. Reversing those fields recovers the complete comparison-baseline manifest. Neither the proof, numerical inputs, substantive verification implementations, certificate, expected results, canonical captions nor approved graphic hashes are edited.

The original correction negative tests are retained. They reject malformed metadata, absent or ambiguous substitutions, changed mathematical expressions, unrelated ledger fields, numerical hashes, row counts and precision changes. The Preskill preservation test recognizes the exact nine-file reconstruction rather than dropping the model from required coverage. No independent scientific evaluator is refactored or consolidated.

## Preservation and local checks

The new checker compares all 368 files at the closure basis: **350 remain byte-identical; 18 have exact recorded changes**, comprising the nine core corrections and nine ancillary files. All 27 protected original graphics and all three accepted-palette reader SVGs remain unchanged. The historical reader, audit, adoption and publication-followup scripts and records retain their original bytes and commit scopes. Their old expected hashes were not refreshed to approve this candidate.

The checks used the recorded Python dependency pins in the isolated Python 3.12.14 environment, with assertions enabled and OpenBLAS/OMP thread counts set to one. Local Pandoc is 3.1.3; the recorded CI converter is 3.1.11.1. No dependency or browser installation was attempted for this candidate.

| Command | Exit | Wall seconds | Observed result |
|---|---:|---:|---|
| `python verify.py` | 0 | 0.157 | Current source/provenance identities, explicit links, inputs and protected artifacts pass. |
| `python -m pytest -q -p no:cacheprovider tests website/tests` | 0 | 10.859 | **151 passed**; pytest reports 10.08 seconds. |
| `python website/repository_preview.py --check` | 0 | 0.166 | 14 generated files match their current sources, including ten native editorial pages, seven canonical routes and three unchanged SVGs. |
| `python publication/integration/check_candidate.py --output build/integration-candidate-checks/preservation-result.json` | 0 | 0.146 | Exact 368-file comparison and bounded core/ancillary scope pass. |
| `python reproduce.py --output build/integration-candidate-figures` | 0 | 6.174 | Ten current plotting/identity outputs and all 27 approved graphical artifacts reproduce byte for byte. |
| `python website/build.py --output build/integration-candidate-site` | 0 | 3.557 | Builds 17 HTML routes. |
| `python website/check.py --site build/integration-candidate-site --report build/integration-candidate-checks/site-result.json` | 0 | 1.702 | 1,315 local links and 761 MathML expressions checked; canonical model/proof retain 18/119 displayed equations. |

Native outputs were generated before checking. The default figure replay was used because the changed model-document identity flows into plotting provenance. It did not run the full entropy certificate, witness recalculation campaign or a new simulation. A final HTML build/check after completing this report is recorded separately with the exported command results.

One initial integrity failure is retained: the new root status linked `reader/status.md#correction-record`, while the unchanged canonical link checker requires an `id` anchor and the native generator correctly emits GitHub `name` anchors. Removing only the unnecessary fragment from that root link resolved the failure. The scientific checker and native generator were unchanged. A separate environment-inventory helper was initially invoked with the system Python and failed to find `mpmath`; it was rerun with the same isolated interpreter used for every principal check. Neither failure was suppressed or treated as a scientific defect.

## Scope of the checked result

The successful local checks concern the complete source candidate and the available local renderer. No actual browser was launched for this candidate in the local environment, and no authenticated GitHub renderer, Safari or Firefox inspection is claimed. Earlier browser successes belong to their earlier reader/adoption commits. The proposed private candidate CI must apply this exact patch and inspect its own actual browser outcome before claiming browser validation of this combined tree.

`publication/check_preparation.py`, `publication/check_followup.py` and `website/review/check_preservation.py` intentionally describe earlier, narrower states. They remain unchanged and are not used as integrated-tree gates. Run the new candidate checker for this combined state; the inherited correction mutation tests continue to check exact reconstruction and scientific preservation.

The release branch receives only an unapplied complete patch, this report and its command/hash record. The patch's comparison basis and SHA-256 are in `publication/integration/CANDIDATE_CHECKS.json` beside the exported payload. Later additive CI/evidence files are separate from the candidate patch. Changes to the comparison baseline's existing files need another explicit recorded comparison; they are not silently ignored.

After owner approval, apply the complete patch on the agreed integration branch, regenerate/check the same native files and run the listed checks at the resulting exact commit. Do not apply the smaller core-only patch by itself. Any final merge or visibility decision remains separate. The candidate status pages intentionally describe an offline review state; later stage changes must be recorded accurately rather than pretending a merge has already happened.
