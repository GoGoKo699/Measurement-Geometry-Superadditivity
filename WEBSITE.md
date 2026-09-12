# Build and review the project website

The reader site makes the scientific baseline accessible as a complete project account. It is not a manuscript or a public deployment. New explanatory pages map to canonical sources; the model and complete proof are rendered directly. The source under `website/` contains no third-party scripts, analytics, external web fonts or public-hosting credentials.

## Local build

Install the scientific dependencies from `requirements.txt`. The site additionally needs **Pandoc 3.1.11.1** and **beautifulsoup4 4.14.3** in the checked environment; the build uses only Pandoc's Markdown-to-HTML/MathML conversion, not LaTeX or a PDF engine. Different Pandoc versions are not assumed byte-identical.

```bash
python -m pip install -r website/requirements.txt
python website/build.py --output build/project-site
python website/check.py --site build/project-site
python -m http.server 8000 --bind 127.0.0.1 --directory build/project-site
```

Open `http://127.0.0.1:8000` in a modern browser. The build is designed to support directly opening `build/project-site/index.html`: search data, MathML, styles and images are local and do not require fetch calls. A new output directory is required; no existing build is overwritten or recursively removed.

The read-only CI workflow builds an artifact for local review, not a public URL. The optional browser test uses Chromium and Playwright; it checks desktop and mobile layout, local resources, search, color switching and the proof page. Browser tooling is not required to read the built site.

The browser checker supports actual local HTTP navigation with `--base-url http://127.0.0.1:8765`. Without that option it uses an in-memory mirror of the same HTML, CSS, JavaScript and image bytes; this supports restricted runtimes but does not test file or HTTP navigation. Reports explicitly distinguish the modes. The CI workflow is configured for real local HTTP navigation. Both modes check desktop/mobile layouts, keyboard controls, search, color comparison, and no-JavaScript navigation.

## Reader routes

**Understand:** overview, optional selected Preskill background and crosswalk, channel and eight-use illustration, geometric proof guide, exact theorem/proof, controlled limits and verification. **Check:** exact model, full proof, verification guide, exact commands, references. **Use the material:** claim-to-evidence inventory, figure source files and original downloads, notation and provenance. No paper reading is required to obtain the complete model or proof.

There is one canonical mathematical source, not a separately edited website proof. `website/editorial_map.json` records the canonical source anchors used by each new reader page. The existing My-tone record describes the earlier reader pass; My-tone was not consulted in the Preskill redesign. Presentation guidance is not scientific verification.

## Colors and approved figures

`website/palette.json` records the painting reference, chosen display colors, roles and permitted SVG color substitutions. The builder creates themed derivatives in its output folder and checks exact equality after normalizing only permitted colors. Original SVG paths, labels, markers, line patterns, opacity and geometry stay unchanged. The approved PDF/SVG/PNG files and their hashes are never overwritten.

The Gachet-inspired palette is accepted for figures only. The protected older exports remain unchanged; this redesign does not request palette approval again. The original colors remain available beside each figure. Color is not the only distinction between branches or bounds.

## Privacy and release boundary

Do not enable Pages, change repository visibility or add a public deploy action as part of a routine build. GitHub Pages from a private repository is not automatically a private website. The owner has adopted the [reuse terms](LICENSE.md) on `release/public-readiness-v1`; publication and historical-disclosure decisions remain outstanding. Reuse notices and the [citation](CITATION.cff) accompany the source downloads. The preview includes a noindex directive, but that directive is not access control.

The CI workflow has only `contents: read` permission and no deployment action. The built site deliberately contains scientific source downloads and should be treated with the same access restriction as this repository. [GitHub Pages visibility documentation](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)

## Preservation checks

The original scientific manifest and old root documentation are retained in `website/provenance/`. The builder confirms that every old baseline file except README and STATUS is unchanged, and checks all approved graphics. The current root manifest records the two editorial updates. No verification implementation or equation is refactored by the website work.

## Maintain one editorial source

Edit **`website/pages/`** for reader prose. Edit **`website/learning_bridge.json`** for the selected tutorial's version, checked locations, concept crosswalk and internal destinations. Its small helper expands the same reading tables for both interfaces. `website/site.json` controls the routes; `website/editorial_map.json` records project-source anchors and editorial history. The learning map is not another proof-dependency ledger. Canonical technical pages and captions continue to render from their existing sources.

Generate the GitHub-native pages before checking them. Do not hand-edit `reader/` output. Routine generation and CI never fetch Preskill's PDF or other remote tutorial content.

```bash
python website/repository_preview.py --write
python website/repository_preview.py --check
python verify.py
python -m pytest -q -p no:cacheprovider tests website/tests
python website/build.py --output build/preskill-reader-review
python website/check.py --site build/preskill-reader-review
```

Use a fresh output directory. For actual browser review, install the recorded browser dependency and Chromium, then keep a loopback server running while the second command executes:

```bash
python -m pip install -r website/requirements-browser.txt
python -m playwright install --with-deps chromium
python -m http.server 8765 --bind 127.0.0.1 --directory build/preskill-reader-review
# In another terminal, from the same checkout and environment:
python website/browser_check.py --site build/preskill-reader-review --output build/preskill-reader-browser --base-url http://127.0.0.1:8765
```

Stop the server after review. HTTP mode performs real browser navigation. The default mirror mode is distinct and must not be reported as either loopback navigation or authenticated GitHub rendering. The [implementation report](website/review/PRESKILL_BRIDGE_REPORT.md) records which checks actually ran and the differences between the available local runtime and the recorded CI runtime. No public hosting is enabled by these commands.

The [starting manifest](website/provenance/preskill_starting_manifest.json) records all 208 pinned file hashes. The redesign preserves scientific and graphical artifacts, records authorized root-document hash changes, and keeps the pending audit corrections visible without merging that separate branch. Documentation work does not require rerunning the full entropy certificate.
