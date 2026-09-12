# Tracked-tree exposure review

**Reviewed 12 September 2026:** `1107ac899d2e267c6cf03509168623c13db4038c` in `GoGoKo699/Measurement-Geometry-Superadditivity`.

This was a read-only pre-publication review of the 280 tracked files at that commit. The working tree was clean before and after inspection. No settings, scientific files, reference outputs or dependencies were changed. Line locations below refer to the reviewed commit.

The review combined a tracked-file inventory, text pattern scans, manual examination of flagged locations, workflow and website-source reading, PDF text/metadata inspection and PNG metadata inspection. It did not send repository material to an external service. It did not inspect another repository.

## Findings requiring an explicit publication decision

| Finding | Location | Interpretation and smallest response |
|---|---|---|
| Personal contact metadata is tracked | `website/review/CI_CHECKPOINT.json`, lines 36 and 40 | Both fields contain the same non-noreply personal email address copied from commit author/committer metadata. The address is deliberately not repeated here. Obtain the owner's exposure decision. Editing this snapshot alone would not remove an address from Git history. |
| Historical provenance names a separate project | `provenance/text_sources/H1__H1__START_HERE.md`, lines 34–38; `provenance/text_sources/S9__PROOF_AUDIT.md`, line 9; `provenance/text_sources/S10__PRIOR_PROOF_AUDIT.md`, line 7 | The handover records another repository's name, revision, PR/CI status and a historical figure limitation. The audit sources retain archive names containing that project's name. These are historical disclosures, not runtime dependencies. Preserve provenance and obtain an exposure decision rather than silently editing protected source. |
| Editorial provenance identifies another work context | `website/editorial_map.json`, lines 5–13; `website/pages/visual-design.md`, lines 31–33, and its generated reader page | The records name My-tone and its consulted historical revision. No private writing examples were found. The existence and revision metadata still form part of what publication would disclose. |
| Reuse and citation decisions are incomplete | `README.md`, line 71; absence of `LICENSE` and `CITATION.cff` at the reviewed commit | Select the rights holder, reuse terms and citation identity before describing the repository as a licensed release. No manuscript DOI, publication status or authorship list should be inferred from a GitHub account name. |
| Documentary corrections remain on a separate branch | `STATUS.md`, line 11; `website/pages/status.md`, lines 13–17 | The live reader account acknowledges the pending rate/threshold attribution correction, plotting-path correction and obsolete pre-repository wording. Decide how to integrate these before selecting the public source state. This review did not re-audit the science or inspect the other branch. |

These findings are confirmed from the tracked files. They do not establish that the owner considers the contact or historical metadata confidential. That decision remains separate from detecting its presence.

## Workflow and generated-artifact exposure

Both workflows declare only `contents: read`. No Pages, release publishing or deployment action was found. The reader workflow binds its HTTP review server to `127.0.0.1` at `.github/workflows/reader-site.yml:57`.

The labels at `.github/workflows/reader-site.yml:51,69` call the output private. `website/build.py:155,191,193` similarly supplies private-review wording and metadata. Those labels are not access controls. `WEBSITE.md:36` correctly explains that `noindex` is not access control. Live labels should describe the actual publication state when it changes; historical run records should keep their original meaning.

`website/build.py:168` copies every `.md`, `.json`, `.log` and `.txt` file under `website/review/` into site downloads. Consequently the raw CI metadata containing the personal email is also included in generated review artifacts. Future additions to that directory must be reviewed as distributable source material, not assumed to stay local because the directory is named `review`.

Website code uses local CSS, JavaScript, search data and native MathML. No analytics, remote font, remote mathematics renderer, telemetry call or website runtime fetch was found. Links to external literature and palette provenance are ordinary references. This pass inspected the code; it did not perform another browser session.

## Checks with no detected exposure

- Text scans found no recognizable GitHub/API credential, access token, private-key block, credential-bearing URL or signed download URL. Broad searches for authentication-related words produced ordinary documentation and parser references, not a credential value.
- Ninety-one absolute local-path matches identified managed workspace or CI paths. No personal home path or internal package/service hostname was detected. Local machine paths are reproducibility context, not evidence of a credential.
- The tracked tree contains no ZIP, `.env`, key file, notebook, database, standalone font or JPEG. No Preskill PDF, scanned chapter page or painting reproduction is included.
- All 11 tracked PDFs were inspected for document metadata and text patterns indicating contact information or secrets. Their metadata identifies the project or rendering tools; no such contact or credential pattern was found.
- The six tracked PNG files contain DPI metadata or no metadata. No personal or credential metadata was detected.
- SVG metadata includes Creative Commons RDF vocabulary namespaces. Those namespace references are not a Creative Commons license grant.

Pattern scans can miss credentials in an unfamiliar format or information whose sensitivity is apparent only to its owner. These results are a bounded inspection, not a guarantee that no sensitive information exists.

## Small improvements and licensing boundary

The current `.gitignore` covers the virtual environment, caches and build outputs. Narrow ignores for local credential/configuration files would reduce accidental additions. There was no such tracked file to remove.

The reader workflow uses version-tagged Actions and checks the downloaded Pandoc version, but does not verify a package digest. Commit-pinned Actions and a reviewed download digest would improve supply-chain control. `include-hidden-files: true` at workflow line 77 could also be removed unless a required artifact justifies it. No compromise was detected or implied by these suggestions.

`requirements.txt:7` pins PyMuPDF 1.26.7, which is used by the rendering code. Its upstream licensing belongs in the dependency/license review. A new repository license must not imply that it relicenses third-party dependencies. This document makes no legal conclusion about that dependency.

## Scope left to the publication decision

This review excludes Git history, branch and PR history, account settings, repository visibility, GitHub Actions logs and retained remote artifacts. It inspected committed CI snapshots only. Those other surfaces require their own review before an actual visibility change. It also excludes a vulnerability audit of dependencies, a new scientific audit, a full certificate rerun and external user testing.

A private route for sensitive reports must be established before the maintainer solicits sensitive details. No security-reporting feature or address was configured by this review. The accompanying [contribution guide](../CONTRIBUTING.md) gives ordinary issue and change-review guidance without inventing a license or private reporting channel.
