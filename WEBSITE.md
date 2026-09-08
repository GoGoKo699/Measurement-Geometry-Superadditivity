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

**Understand:** overview, channel, three-step proof guide, figures, limits. **Check:** exact model, full proof, verification guide, exact commands, references. **Use the material:** claim-to-evidence inventory, figure source files and original downloads, notation and provenance. No paper reading is required to obtain the complete model or proof.

There is one canonical mathematical source, not a separately edited website proof. `website/editorial_map.json` records the canonical source anchors used by each new reader page. Applying My-tone is presentation work only; it is not a scientific audit or a claim of semantic equivalence established by software.

## Colors and approved figures

`website/palette.json` records the painting reference, chosen display colors, roles and permitted SVG color substitutions. The builder creates themed derivatives in its output folder and checks exact equality after normalizing only permitted colors. Original SVG paths, labels, markers, line patterns, opacity and geometry stay unchanged. The approved PDF/SVG/PNG files and their hashes are never overwritten.

These web colors are a visual study. Adopting them for the paper exports is a separate approval step. The original colors remain available beside each figure. Color is not the only distinction between branches or bounds.

## Privacy and release boundary

Do not enable Pages, change repository visibility or add a public deploy action as part of a routine build. GitHub Pages from a private repository is not automatically a private website. The owner's publishing and reuse-license decisions are still outstanding. The preview includes a noindex directive, but that directive is not access control.

The CI workflow has only `contents: read` permission and no deployment action. The built site deliberately contains scientific source downloads and should be treated with the same access restriction as this repository. [GitHub Pages visibility documentation](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)

## Preservation checks

The original scientific manifest and old root documentation are retained in `website/provenance/`. The builder checks all approved graphics and reconstructs the original bytes of the five explicitly recorded documentary corrections and their four dependent source-identity records in `provenance/EDITORIAL_CORRECTIONS.json`. Every other old baseline file except README and STATUS must remain byte-identical. The current root manifest records the corrected documentation and its provenance. Equations and verification implementations remain unchanged.
