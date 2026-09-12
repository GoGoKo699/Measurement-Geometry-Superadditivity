# Historical distribution and log review

This is a bounded disclosure check on 12 September 2026, not a security certification or another scientific audit. It covers only this repository. It does not inspect the other projects named in preserved historical text.

## What was inspected

The six pre-existing branch heads reach 20 unique commits and 17 unique trees. Their inventories contain 464 distinct Git blobs. The review verified the exact Git identity of 462 blobs and scanned all 440 UTF-8 text blobs for private-key headers, common credential/token forms, credential-bearing URLs and signed-download URLs. No candidate matched those patterns. This does not exclude every possible secret representation, personal datum or copyrighted contribution.

The two remaining binary responses failed byte-identity validation and were excluded, not counted as passes. Other verified binary objects include current figure assets; the current-tree PDF/PNG/SVG inspection is described in [EXPOSURE_REVIEW.md](EXPOSURE_REVIEW.md) and [ATTRIBUTION_REVIEW.md](ATTRIBUTION_REVIEW.md).

All 40 enumerated Actions runs were inspected for available jobs. There were 54 jobs: 32 executed logs were retrieved and pattern-scanned, and 22 skipped jobs had no execution log to inspect. No credential-shaped pattern matched the retrieved logs. Four PR descriptions and their two issue-comment bodies were scanned as well; the inline-comment and review collections were empty. Raw logs and contact values are not republished in these preparation records. No additional workflow was launched by the review itself.

The exact branch/commit inventory and log-job summaries are in [evidence/HISTORY_INVENTORY.json](evidence/HISTORY_INVENTORY.json) and [evidence/ACTIONS_SCAN.json](evidence/ACTIONS_SCAN.json). The [scan summary](evidence/HISTORY_SCAN.json) records patterns, counts and the blocked objects. The branch added for this work initially points to the reader commit and introduces no additional historical source at that point. The existing PR head refs correspond to the inspected branch heads; the synthetic PR merge ref is GitHub's review merge, not a branch merged by this task.

GitHub reported no releases. Its tag-list route was unavailable through this connector; the allowed Git-ref inventory showed no tag refs. This is a recorded access boundary, not a reason to infer that an uninspected release asset is safe. Hosted artifact payloads from all historical runs were not downloaded and independently inspected; the two reader CI implementations and their explicitly recorded artifact inspection retain their earlier scope. Source and log scanning is not a claim to have examined every hosted binary artifact.

## Disclosure decisions

Git author metadata includes a personal, non-noreply address. The same address was copied into `website/review/CI_CHECKPOINT.json` at lines 36 and 40. This is contact information, not a discovered credential. The intended public tree and history must be reviewed with that exposure understood; editing the current JSON would not remove the commit metadata from older history.

`provenance/text_sources/H1__H1__START_HERE.md` at lines 34–38 contains historical references to another project, including a revision and earlier status. Other source records name old archives. `website/editorial_map.json` and the visual-design pages retain the earlier My-tone revision. These references were found in this repository; no other repository was accessed. The owner must decide whether these records may be public. Protected provenance was not silently edited.

The optional HTML builder copies review text and JSON into source downloads. Consequently, distributing its artifacts also distributes those records. GitHub [documents](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility) that Actions history and logs become visible when the repository becomes public. Current “private” labels and `noindex` do not prevent that exposure.

## Two exact binary objects still to inspect

| Git blob | Historical path | Expected bytes | Observed limitation |
|---|---|---:|---|
| `f4442ae622a7d96a2346c66acedcea54783a598f` | `Measurement-Geometry-scientific-baseline-v1-2026-09-08.zip` | 2,540,928 | The base64 file response supplied no content; the blob-text route rejected non-UTF-8 bytes. ZIP members have not been inspected here. |
| `0bac8266cbd5495b9b3a3ef7eecfd642b347af6d` | `audits/repository-sanity-01/reader/figure_02_guaranteed_region-display.png` | 85,639 | The base64 response contained only 60,000 decoded bytes; the blob-text route rejected the binary. The incomplete result did not match the Git blob. |

The smallest remaining path is a complete authenticated clone with the remote branch histories fetched. Read the two objects into a fresh temporary directory, without checking out or executing anything from the ZIP:

```bash
git fetch origin
publication_review_dir=$(mktemp -d)
git cat-file blob f4442ae622a7d96a2346c66acedcea54783a598f > "$publication_review_dir/baseline.zip"
git cat-file blob 0bac8266cbd5495b9b3a3ef7eecfd642b347af6d > "$publication_review_dir/figure.png"
git hash-object "$publication_review_dir/baseline.zip" "$publication_review_dir/figure.png"
python -m zipfile -t "$publication_review_dir/baseline.zip"
python -m zipfile -l "$publication_review_dir/baseline.zip"
```

Confirm both printed object hashes, inspect ZIP member names and content for the intended scientific package and any private or third-party material, and inspect the PNG and its metadata. A ZIP CRC check alone is not content clearance. Use bounded extraction or in-memory reading after checking member paths; do not run archived code. A shallow or single-branch clone may need its history completed before `git cat-file` can find these objects. No full simulation or entropy certificate is needed.

An incomplete connector transfer is an environment limitation, not evidence that either file is unsafe. It nevertheless remains unfinished evidence for publishing all existing repository history. No file, branch, log, artifact or history was deleted to conceal that limitation.
