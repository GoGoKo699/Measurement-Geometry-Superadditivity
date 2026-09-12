# Build and maintain the reading pages

The repository provides a complete scientific account through GitHub-native Markdown and an optional local HTML site. Both use **`website/pages/` as the editorial source**. Canonical technical documents and captions are rendered or linked directly, so there is no second editable proof or caption set.

GitHub provides its own Markdown and mathematics renderer. The HTML site adds local search, navigation and figure-color comparison. It uses native MathML, local styles and scripts, with no analytics, CDN, remote tutorial fetch or external font requests. Building it does not deploy a public website.

## Maintain one source

Edit `website/pages/` for reader prose, `website/site.json` for routes, and `website/learning_bridge.json` for the selected Preskill v5 passages, crosswalk and return links. `website/editorial_map.json` records the current project-source anchors. The tutorial map is a learning aid, not a proof certificate.

Generate `reader/` before checking it; do not hand-edit those outputs. Keep canonical mathematics, numerical inputs, independent evaluators, reference evidence, captions and protected graphical files unchanged during editorial work. The accepted palette applies only to figures.

## Generate and check

Use an isolated environment and install `requirements.txt` and `website/requirements.txt`. The recorded HTML environment uses **Pandoc 3.1.11.1** and **beautifulsoup4 4.14.3**. Pandoc converts Markdown to HTML/MathML; no LaTeX or PDF engine is required. Different Pandoc versions are not assumed byte-identical.

```bash
python -m pip install -r requirements.txt -r website/requirements.txt
python website/repository_preview.py --write
python website/repository_preview.py --check
python verify.py
python integrity/check_scientific.py
python -m pytest -q -p no:cacheprovider tests website/tests
python website/build.py --output build/reader-review
python website/check.py --site build/reader-review
```

Use a fresh output directory. Do not use Python `-O`, because some checks depend on assertions. The builder directly checks the protected scientific sources, provenance, numerical inputs and approved graphics against [their current integrity inventory](integrity/SCIENTIFIC_FILES.json). The [integrity checker](integrity/check_scientific.py) verifies those identities without reconstructing an earlier checkout. Scientific expected values and figure approval hashes must not be refreshed to accept a changed result.

## Browser review

Install the recorded browser dependency and Chromium, then start a loopback server:

```bash
python -m pip install -r website/requirements-browser.txt
python -m playwright install --with-deps chromium
python -m http.server 8765 --bind 127.0.0.1 --directory build/reader-review
```

In another terminal, from the same checkout and environment:

```bash
python website/browser_check.py --site build/reader-review --output build/reader-browser --base-url http://127.0.0.1:8765
```

Stop the server after review. HTTP mode navigates the built pages in a real browser. The default in-memory mirror mode is a different check and must not be reported as loopback navigation or authenticated GitHub rendering. The HTML files also support opening `index.html` directly: search data, styles, figures and mathematics are local.

The CI reader workflow produces a review artifact and exercises desktop and mobile Chromium, source downloads, navigation, search, keyboard controls, mathematical rendering, figures and no-JavaScript access. It does not enable hosting. Report actual outcomes for the checked commit; a configured or running job is not a passed check.

## Scientific verification

[REPRODUCTION.md](docs/REPRODUCTION.md) distinguishes integrity checks, figure reproduction, witness calculations and complete certificate verification. Documentation work does not require another local full entropy-certificate run. The existing scientific CI gates remain in force. The [verification guide](reader/verification.md) explains their scope and links current CI results.
