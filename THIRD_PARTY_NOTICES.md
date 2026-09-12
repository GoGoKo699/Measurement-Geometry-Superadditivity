# Third-party material and dependency notices

These notices identify third-party material used by the repository. They do not select or grant a reuse license for the project's own work. The project license and citation remain pending owner confirmation; see the [licensing proposal](publication/LICENSING_PROPOSAL.md).

## Fonts in the scientific figures

The protected figure PDFs contain subsets of DejaVu Sans 2.35 in regular, bold and oblique styles. Figure 1, its channel panel and the three-figure review PDF also contain STIXNonUnicode-Italic 1.0.0, a mathematical fallback font. The SVG figures contain corresponding glyph outlines. No standalone font files are distributed.

The exact font notices supplied by the recorded Matplotlib 3.10.8 installation are preserved in [LICENSES/DejaVu.txt](LICENSES/DejaVu.txt) and [LICENSES/STIX.txt](LICENSES/STIX.txt). DejaVu retains the Bitstream and Arev notices; DejaVu changes are identified there as public domain. The bundled STIX notice includes its original copyright statements, Matplotlib's format-conversion note and SIL Open Font License 1.1.

These terms apply to the font components. They do not select the license for the project's scientific figures or prose. The [official OFL FAQ, sections 1.10–1.14](https://openfontlicense.org/ofl-faq/), distinguishes embedding and glyph artwork from distributing fonts for independent use. In particular, embedding an OFL font does not put the document under the OFL. Anyone extracting font material must respect its original terms.

The figure bytes have not been changed to add these companion notices. The review PDF also references the standard PDF font Helvetica without embedding a Helvetica font program.

## External educational and visual references

John Preskill's *Quantum Shannon Theory*, Chapter 10 of *Quantum Information*, is linked at the selected edition [arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5). The tutorial PDF, screenshots, textbook figures and chapter text are not distributed here. Its own front-matter notice restricts the draft to personal use and prohibits redistribution. The repository supplies original explanations and source references; its eventual license will grant no rights over that external tutorial.

The accepted figure palette is a manual visual interpretation of the first version of Vincent van Gogh's *Portrait of Dr. Gachet*. The consulted reproduction and method are recorded in [website/palette.json](website/palette.json). The painting image is not embedded or distributed, and the figure palette does not introduce third-party painting assets into the repository.

Research attribution remains in [docs/REFERENCES.md](docs/REFERENCES.md) and the source records. A citation is not a redistribution license for a cited paper.

## Software dependencies

The scientific and rendering packages are listed in [requirements.txt](requirements.txt); reader and browser dependencies are listed in [website/requirements.txt](website/requirements.txt) and [website/requirements-browser.txt](website/requirements-browser.txt). These packages are installed separately. Their source distributions, wheels and browser binaries are not included in the tracked repository.

Dependencies retain their own licenses. In particular, PyMuPDF 1.26.7, used by the figure-rendering and checking scripts, is offered under GNU AGPLv3 or an Artifex commercial license. See the [official PyMuPDF license explanation](https://pymupdf.readthedocs.io/en/latest/about.html) and [AGPL text](https://artifex.com/licensing/gnu-agpl-v3). The project license does not replace those terms or make the combined runtime permissively licensed.

AGPL section 2 distinguishes generated output from covered program code. Using PyMuPDF to create a figure does not by itself put the figure under AGPL. That distinction is not a claim that importing PyMuPDF is categorically exempt from AGPL obligations. Distribution of combined software, bundled environments or a network service must be assessed under the dependency's applicable terms before that distribution or service is offered.

The [attribution review](publication/ATTRIBUTION_REVIEW.md) records the inspected files, font versions, notice hashes and remaining ownership confirmation.
