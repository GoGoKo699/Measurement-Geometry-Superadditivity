# Attribution and distribution review

This bounded preparation check was performed on 12 September 2026 against reader commit `1107ac899d2e267c6cf03509168623c13db4038c`. It inventories material distributed by this repository and supports the [third-party notices](../THIRD_PARTY_NOTICES.md). It does not select a project license, establish ownership of every contribution, or certify legal clearance. No other project repository was accessed.

## What is distributed

The inspected tree contains 11 PDF files, 13 SVG files and 6 PNG files, all scientific figures or figure-review outputs. The 13 SVGs comprise 10 protected originals and 3 accepted-palette reader figures. None contains an SVG image element. There are no tracked standalone fonts, painting images, tutorial PDFs or screenshots, copied textbook figures, dependency wheels or browser binaries.

The project preserves its own earlier source records under `provenance/text_sources/`, with identities in `SOURCE_REGISTER.json`, `INPUT_ARCHIVES.json` and `FILE_LINEAGE.json`. These records describe supplied project archives and scientific/code lineage. They are not third-party rights grants. The inspected historical prose and code are presented as earlier project material; this inventory cannot prove their complete ownership history.

## Font inspection and exact notices

`pdffonts` was run on every tracked PDF in `figures/approved/`. All 11 contain embedded DejaVu subsets. Three additionally contain STIXNonUnicode-Italic: `figure_01_channel_and_witness.pdf`, `panels/figure1a_channel.pdf` and `three_figure_review.pdf`. The review PDF's Helvetica reference is not embedded. SVG glyph identifiers confirm DejaVu styles and the STIX fallback in the channel panel.

The font name tables extracted from Figure 1 identify DejaVu version 2.35 and STIXNonUnicode version 1.0.0. Their copyright records remain present; the sampled embedded subsets have neither a license-description record nor a license-URL record (TrueType name IDs 13 and 14). This is a reason to supply companion notices without rewriting protected outputs. The website's main font setting alone would have missed the STIX fallback.

The following files were copied byte-for-byte from `matplotlib/mpl-data/fonts/ttf/` in the installed, recorded Matplotlib 3.10.8 environment:

| Repository notice | Upstream filename | Bytes | SHA-256 |
|---|---|---:|---|
| [DejaVu.txt](../LICENSES/DejaVu.txt) | `LICENSE_DEJAVU` | 4816 | `d75938dec098f06f0ac3c00853065d94f020be1c3c62ef1dc2975ba15b4d9b0e` |
| [STIX.txt](../LICENSES/STIX.txt) | `LICENSE_STIX` | 5476 | `bab3d31dfef07f483624f2f65f2711e76065b8e7273278b1c071ede1041c9959` |

DejaVu's Bitstream/Arev terms call for accompanying copyright, trademark and permission notices for copies of the typefaces. Preserving the bundled notice is the conservative treatment of the embedded font material. The current DejaVu project homepage describes a newer release; that is not substituted for the version actually found in the figures.

The STIX notice is for Matplotlib's historical font, not modern STIX Two. The official OFL FAQ permits embedding/subsetting and explains that a document or glyph artwork does not inherit OFL merely by using the font. Therefore, absence of a separate STIX notice in the earlier tree is not treated here as a confirmed violation of the embedding rules. The companion notice records the component's origin and terms for reuse.

Primary sources inspected:

- [DejaVu license](https://dejavu-fonts.github.io/License.html), especially the Bitstream and Arev notices.
- [Matplotlib 3.10.8 license page](https://matplotlib.org/3.10.8/project/license.html), STIX subsection and its format-conversion record.
- [Official OFL FAQ](https://openfontlicense.org/ofl-faq/), sections 1.10–1.15 on embedding, documents and extraction.

## Tutorial and palette boundaries

The temporary official [Preskill v5 PDF](https://arxiv.org/pdf/1604.07450v5) was inspected outside the checkout. Viewer page 5 contains the 2025 John Preskill copyright and the draft's personal-use/no-redistribution notice. The detailed source-version check is retained in [SOURCE_VERIFICATION.md](../website/review/SOURCE_VERIFICATION.md). The PDF itself and its illustrations remain outside the repository; the reading map and original bridge prose do not grant rights over that work.

[website/palette.json](../website/palette.json) records a manual interpretation of the first *Portrait of Dr. Gachet*, the consulted reproduction URL, and `painting_embedded: false`. The file inventory and SVG inspection agree with that description. No claim about licensing a redistributed painting photograph is needed for this tree, because no such image is distributed.

## Dependencies and generated output

The repository distributes project scripts, requirements and rendered results. It does not vendor the installed packages. Installed package metadata confirms PyMuPDF 1.26.7 is dual-licensed under AGPLv3 or an Artifex commercial license. The [official PyMuPDF documentation](https://pymupdf.readthedocs.io/en/latest/about.html) confirms that licensing model.

[AGPL section 2](https://artifex.com/licensing/gnu-agpl-v3) distinguishes generated output from program code. Figure generation alone is not a reason to apply AGPL to the scientific artwork. This review does not conclude that import-using scripts, combined distributions or services are exempt from AGPL. An eventual project license must retain this dependency boundary; any later bundled executable, environment image or interactive service needs a check of its actual distribution and use.

The [current Artifex licensing explanation](https://artifex.com/licensing) describes PDF producer/license metadata as a recommendation using “ideally.” It is not used here to justify changing the protected figure metadata. No dependency, evaluator or renderer was replaced or refactored for licensing preparation.

## What the owner still needs to confirm

Git commit metadata identifies Ruge Lin as the project author. That is evidence of attribution, not proof of sole copyright ownership. Before activating the [proposed project licenses](LICENSING_PROPOSAL.md), the owner must confirm the intended copyright holder and citation authors, authority to license the supplied project archives and later contributions, and whether any collaborator or institutional rights require consent.

Only new notice and review files are added in this work. Canonical scientific prose, equations, data, certificates, verification implementations, captions, historical source excerpts and protected figure bytes remain unchanged.

For a repeat inventory, list the tracked assets with `git ls-files`, run `pdffonts` on the 11 PDFs, inspect SVG image elements and glyph IDs, and compare `sha256sum LICENSES/DejaVu.txt LICENSES/STIX.txt` with the values above. These checks establish the recorded component inventory and byte identities; they do not establish ownership by themselves.
