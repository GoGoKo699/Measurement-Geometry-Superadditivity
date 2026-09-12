# Public-readiness preparation

**The preparation is implemented; publication and the project-wide license grant remain pending.** This is a licensing, attribution and repository-distribution task. It adds no manuscript, scientific claim, simulation or source repair.

## Repository and starting state

Authenticated access confirmed `GoGoKo699/Measurement-Geometry-Superadditivity` is private, with no detected repository license, no releases and Pages disabled. `main` remains at the scientific pin `f0015c56a19fd953c6797b2c64d9b507105234e3`. The completed reader branch is `1107ac899d2e267c6cf03509168623c13db4038c`, tree `d75a22453776a366d4860317f3708f0c5c00bc57`.

The new `release/public-readiness-v1` branch and separate worktree start at that reader commit. There was no pre-existing branch of that name. The starting worktree was clean; no AGENTS or CONTRIBUTING instruction file was present. README and preserved baseline status explicitly leave the reuse-license and citation choice to the owner. The existing unmerged audit corrections and reader PR were inspected and preserved as separate work, not silently merged.

## Implemented changes

[PUBLICATION.md](../PUBLICATION.md) is the entry point. The [licensing proposal](LICENSING_PROPOSAL.md) recommends MIT for original software and CC BY 4.0 for original scientific content, with concrete scope, unmodified MIT text, official CC terms and exclusions for third-party material. It explains the actual remaining decision: license choice, correct rights holder, authority over the included original archives/contributions, and complete citation-author list. The proposed name is Ruge Lin. That proposal is not presented as a legal ownership finding or an active grant.

The candidate `CITATION.cff` identifies the repository as software and omits unconfirmed publication and personal metadata. It was validated against the official CFF 1.2.0 JSON schema using jsonschema 4.23.0 in a separate temporary validation directory. No production requirement or CI dependency was changed. [CITATION_VALIDATION.json](evidence/CITATION_VALIDATION.json) records the exact candidate/schema identities and result. Schema validity does not establish authorship.

[THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) and the two exact font-license files supply companion notices for existing DejaVu 2.35 and STIXNonUnicode 1.0.0 material. The PDF/SVG byte content is unchanged. The notices distinguish the external Preskill tutorial and consulted painting reproduction from actual distributed assets, and keep PyMuPDF's AGPL/commercial dependency terms separate from the proposed project grant and generated figure artwork.

[CONTRIBUTING.md](../CONTRIBUTING.md) gives short scientific-issue, editing and reproduction guidance. It adds no contributor agreement, copyright assignment, invented security contact or promised response time. A full community-policy framework, public hosting, archival DOI integration and dependency refactor are unnecessary for this preparation.

## Inspection and remaining evidence

The current-tree review covered 280 tracked files, all 11 PDF metadata records, six PNGs and 13 SVGs. The history inventory covered 20 distinct commits and 17 trees reachable from six pre-existing branch heads. Of 464 distinct blobs, 462 had verified identities and all 440 UTF-8 text blobs were scanned. No common credential, key or signed-URL pattern was found. Two binary objects failed transfer identity checks and remain uninspected: the historical baseline ZIP and one audit display PNG. Their exact hashes, sizes, failure mode and smallest full-clone inspection route are in [HISTORY_REVIEW.md](HISTORY_REVIEW.md).

All 40 enumerated Actions runs yielded 54 jobs. All 32 executed job logs were retrieved and scanned; 22 jobs were skipped. Four PR descriptions and two comment bodies were also scanned. No credential-shaped value matched these checks. Raw logs and contact values were not newly committed. Historical artifact payloads were not all downloaded, and these checks are not an assurance that no possible secret or private datum exists.

Actual disclosure items remain: a personal author email in Git metadata and copied CI records, historical project/archive references, and the prior My-tone revision. The owner must accept those exposures or authorize a separate targeted treatment before public visibility. Nothing was deleted or rewritten. The review did not access any other private project repository.

## Verification record

The command results are recorded in [CHECK_RESULTS.json](evidence/CHECK_RESULTS.json). All four local routes completed with exit code 0, using Python 3.12.14 and the recorded scientific dependencies, with assertions enabled and numerical thread counts limited to one.

| Route | Actual result |
|---|---|
| `python publication/check_preparation.py` | All 280 inherited files unchanged, both font notices exact, pending-license boundaries intact and 54 new-document local links resolved. |
| `python verify.py --report build/publication-integrity.json` | Integrity passed: 44 source identities, 23 canonical units, 125 fragments, 7 claims, 165 manifest files and 27 protected original graphical artifacts checked. This is not a fresh entropy verification. |
| `python -m pytest -q -p no:cacheprovider tests website/tests` | 96 passed in 8.87 seconds; 9.514 seconds wall time. |
| `python website/repository_preview.py --check` | All 14 generated files consistent: ten native reader pages, seven canonical routes and three unchanged display SVGs. |

The preparation checker and CFF validation are packaging checks. Neither proves copyright ownership or scientific correctness. No full entropy certificate or numerical campaign was run for this additive preparation.

The all-file `git diff --cached --check` reports two trailing spaces in the copied `LICENSES/DejaVu.txt`, at lines 49 and 76. Those spaces are present in the exact upstream notice and are deliberately retained; the font hash comparison passes. The same whitespace check excluding only that upstream file passes for project-authored additions. No numerical assertion or tolerance is relaxed. The downloaded CFF schema was also checked against its exact upstream Git blob after removing one newline added by the file-materialization wrapper; full schema validation then passed again.

The implementation changes no existing source file, so the earlier reader HTML/browser evidence remains explicitly attached to reader commit `1107ac899d2e267c6cf03509168623c13db4038c`. The preparation PR's actual CI status is inspected and reported in that PR at handoff. A configured or skipped job is not called a pass. New root notices are not yet included by the unchanged website download generator; the final activation step must add them to distributed download packages together with the adopted project license.

## Remaining decisions and stopping point

The next owner decision is the proposed license/rights/citation confirmation. Before public visibility, also settle the intended integrated branch, historical disclosure, the two blocked binary objects, any retained hosted artifact exposure, accurate live release wording, and the final integrated-tree checks. License activation and visibility are separate actions.

This branch is for review. It does not change repository privacy, licensing settings, Pages, workflows, history, scientific source, reader output or `main`. Its PR is draft so the unchanged workflow does not launch the full scientific campaign excluded from this task. No merge, release, deployment or manuscript follows this preparation.
