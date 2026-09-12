# Historical-object follow-up

This bounded follow-up starts from license-adoption commit `857d173c79140b5c2643c1a7d16b4a2321ed8dd4`. It addresses the two incomplete binary transfers recorded in [HISTORY_REVIEW.md](HISTORY_REVIEW.md). The repository remains private, and the earlier no-merge, no-history-rewrite and no-publication boundaries remain in force.

The added [inspection helper](inspect_historical_objects.py) reads only the two recorded Git object IDs. The [dedicated workflow](../.github/workflows/historical-object-review.yml) checks out complete history with read-only repository permission and runs that helper. It neither executes archived code nor runs numerical science. Checkout credentials are not persisted. Its Actions are pinned to the exact revisions observed in successful reader run `34685435836`.

The workflow retains an access-controlled review artifact containing the exact two objects and a structured inspection report for seven days. The word “private” in prose is not an access control; the repository's current private visibility supplies that boundary. No deployment or release action is present.

Both original transfer obligations are now completed. [Run 34686151760](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/actions/runs/34686151760), job `103533372360`, passed at checkpoint `5ec87029cb3ef0067ad2a8f1f1a66027041c9513`. Its private artifact `10295731779` was retrieved through the supported authenticated file-transfer route after a direct temporary URL returned HTTP 403. The 2,606,075 downloaded bytes match the reported artifact SHA-256 `dbc4b4fd0ee259ed1cc9c30a5c9339c2af5eb2d9aa8084ee3262fbf55c043fd9`. Both historical Git blob identities were independently reconstructed locally before inspection. No access control was changed.

The [complete CI inventory](evidence/HISTORICAL_OBJECTS_CI.json) and [local review](evidence/HISTORICAL_OBJECTS_REVIEW.json) record the following:

| Object | Actual content inspection |
|---|---|
| Baseline ZIP, `f4442ae622a7d96a2346c66acedcea54783a598f`, 2,540,928 bytes | All 166 members are recognized: 163 match current files exactly; README, STATUS and the manifest exactly match the three immutable baseline snapshots. All 165 embedded manifest hashes and ZIP CRCs pass. There are no unmatched members, separate project trees or credential-pattern candidates. No archived code was executed. |
| Figure 2 PNG, `0bac8266cbd5495b9b3a3ef7eecfd642b347af6d`, 85,639 bytes | Decoded as a 1,173 by 674 RGB image and visually inspected. It is the expected equal-Pauli Figure 2 display with the two bounds, endpoint markers and width inset. Its only auxiliary metadata is approximately 96 DPI; no text metadata is present. No protected export was replaced. |

The ZIP inspection does not repeat the scientific, PDF or font review of the 163 identical current members. It relies on their exact identity with the material inspected in the earlier bounded reviews. The three older root snapshots were also read and compared; their obsolete pre-repository and pending-license statements remain correctly historical. No additional unidentified content was found.

The exact objects were restored to the local Git object database without changing any tracked source, and the helper was run again successfully in a fresh directory. The [local command record](evidence/followup-local-objects.json) and [log](evidence/followup-local-objects.log) distinguish this completed replay from the earlier incomplete connector responses.

These completed checks close the two-object evidence gap, not the separate consent to disclose retained history. The initial [HISTORY_REVIEW.md](HISTORY_REVIEW.md) and license-adoption records remain unchanged. No new scientific result or blanket security/ownership clearance is claimed, and other historical hosted artifact payloads remain outside this two-object inspection.

To repeat in a complete authenticated checkout, use a new output directory:

```bash
python3 publication/inspect_historical_objects.py --output build/historical-object-review
```

The helper requires only the Python standard library and Git. Fourteen targeted tests cover exact object identity, unsafe paths, duplicate members, symlinks, encryption, count/size/ratio ceilings, corrupt ZIP/PNG CRCs, bounded metadata, redacted candidates, unavailable objects and reused output directories. [The recorded test run](evidence/followup-helper-tests.json) passed. Unified-diff context-space markers are retained in the proposed correction patch; the [whitespace check record](evidence/followup-patch-whitespace.json) separates those required markers from project-authored whitespace.

Root scientific documents, data, certificates, substantive numerical verifiers, figure exports and earlier audit outputs are not replaced. Only the live publication checklist and readiness metadata changed to record this follow-up. [FOLLOWUP_EDITS.json](FOLLOWUP_EDITS.json) records their exact before/after hashes against all 346 license-adoption files in [FOLLOWUP_STARTING_FILES.json](FOLLOWUP_STARTING_FILES.json). Run `python publication/check_followup.py` to check the 344 unchanged files, two recorded editorial changes and the completed object/patch evidence. Earlier preservation scripts retain their narrower historical commit scopes.

The separate [integration review](INTEGRATION_REVIEW.md) describes how the existing corrections relate to the reader and licensing work. A complete offline candidate is being prepared separately; neither that preparation nor this report grants permission to merge branches, disclose private history or change visibility.
