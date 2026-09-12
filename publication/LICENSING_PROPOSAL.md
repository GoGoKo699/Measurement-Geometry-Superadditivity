# Proposed reuse terms

**Prepared for owner review; no project license is activated by this proposal.** The repository is still private. Its current README and preserved baseline status leave licensing and citation identity to an explicit owner decision. The standard terms below are proposed for the eventual public tree, not silently applied to protected historical material.

## Recommended choice

| Original project material | Proposed terms | Practical effect |
|---|---|---|
| Software, scripts, tests, website code and build configuration | [MIT](https://opensource.org/license/mit) | Broad reuse, modification and commercial distribution, with the copyright and license notice retained. |
| Scientific prose, original figures, numerical data and research records, to the extent copyright or database rights apply | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Sharing and adaptation, including commercial reuse, with attribution, a license reference and identification of changes. |
| Embedded font components and separately installed dependencies | Their existing terms | The project grant does not replace third-party licenses. See [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). |

This split lets code be reused under ordinary software terms while keeping a clear attribution route for the scientific account and figures. Creative Commons [recommends a software license for software](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software). Mathematical facts are not claimed as exclusively owned merely because they occur in this repository.

The proposed copyright holder and repository citation author are **Ruge Lin**. This is a concrete proposal based on the repository's attribution, not a determination of sole ownership. Confirm whether collaborators, an institution, or contributors to the supplied historical archives also hold rights or should appear in the citation.

## Exact scope to adopt after confirmation

The proposed [project license notice](proposed/PROJECT_LICENSE.md) identifies the material classes and exceptions. The [MIT text](proposed/MIT.txt) is supplied with the proposed name and year. CC BY uses the unmodified [official 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en). None of these proposed documents is currently an operative repository-wide grant.

The split is by material, not an offer to choose either license for any file. Original source code remains MIT when preserved as a code listing or historical `.py.txt` file. Narrative explanations, generated figures, numerical records, certificates and editorial metadata follow the content grant where applicable. Third-party notices, external source material and dependencies remain outside both project grants. New material of uncertain origin must be identified before inclusion.

Preskill's v5 textbook, the externally linked painting reproduction and cited primary papers are not relicensed. Their external availability is not permission to copy them into a release. Embedded DejaVu/STIX components retain their notices even though the project's original figure artwork would use CC BY.

Scientific citation is requested in [the candidate citation file](proposed/CITATION.cff). It is not an extra restriction added to MIT. Likewise, scientific byte-preservation rules govern project maintenance; they do not prohibit downstream modifications otherwise permitted by an adopted reuse license. Modified figures must not be represented as this repository's approved exports.

## Decision needed before activation

Confirm the MIT/CC BY split, the copyright-holder name and the complete citation-author list, and authority to license the original material, including supplied archives and later contributions. The CC [licensor guidance](https://creativecommons.org/licenses/by/4.0/legalcode.en) requires that authority and explains that granted permissions are irrevocable. This is why the project-wide grant remains pending rather than being inferred from a request to prepare the repository.

After confirmation, create the operative root notice from the approved proposal, replacing conditional review wording with the actual grant and repairing its relative links for the root location. Install the approved license texts, move the approved `CITATION.cff` to the root, and update live README/status/reuse wording and their authorized editorial identities together. Preserve these proposal copies as the decision record, recording adoption rather than relabeling them as earlier permission. Keep historical snapshots, equations, inputs, certificates and approved figure bytes intact. Include third-party notices with generated source/figure download packages. Check GitHub's license and citation presentation on the intended public branch before changing visibility.

No publication date, version tag, DOI, journal article, peer-review status, affiliation or ORCID is invented. A later archived release can add its real persistent identifier. The [publication checklist](../PUBLICATION.md) keeps licensing separate from branch integration and the final visibility decision.
