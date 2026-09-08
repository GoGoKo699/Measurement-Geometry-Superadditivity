# Independent figures and reader-interface audit

Audited scientific baseline: `f0015c56a19fd953c6797b2c64d9b507105234e3`, repository `GoGoKo699/Measurement-Geometry-Superadditivity`. This report covers the figure and reader-interface subtask. It does not independently certify the central entropy theorem or eight-use entropy arithmetic; those are separately audited in the parent report. No scientific source or approved artifact was changed.

The three figures are scientifically faithful to their stated formulas, parameter choices, and interpretation limits. An independent rational checker verified every Figure 2 and Figure 3 plotting enclosure, all geometry coordinates, and the cross-figure threshold ordering. The GitHub reading route and custom HTML build are present and internally consistent. The optional HTML browser audit remains **blocked**, because a Chromium runtime could not be installed. Static HTML checks and real HTTP downloads passed, but neither is a browser-rendering pass.

## Evidence reviewed and independent checks

Read the root README and STATUS; WEBSITE; all nine authored reader pages and their website counterparts; figure overview, specifications, contract and captions; plotting-input and rendering implementations; site generator, repository-preview generator, static checker, browser checker, CSS and JavaScript; site configuration and palette; editorial source map, reader manifest and website CI/tests. The canonical model/proof sections referenced by the figures and simplified reader explanations were compared for scope. The parent audit owns the independent proof and complete scientific replay conclusions.

| Object | Independent evidence | Result and limit |
|---|---|---|
| Figure 1 channel schematic | Visual inspection of original PNG and accepted-color SVG rendered with Inkscape; `diagram1()` source | Encoding occurs before channel choices. Both branches reach the receiver. True sign, reporting bit and discarded quantum system remain unavailable. No postselection or future-axis feedback appears. |
| Figure 1 numerical panel | CSV metadata and exact fraction checks; caption/proof comparison | Zero is labeled optimized one-use coherent information; positive stem is explicitly `I_8/8`, in bits per physical use, with a `10^-5` multiplier. Nine mask probabilities sum exactly to one and the all-measured term is negative. Full independent entropy recalculation is in the parent audit. |
| Figure 2 | `independent_figure_check.py`, 1,001 exact rational error coordinates | All 3,003 displayed-value enclosure checks passed using integer-square-root bounds and rational arithmetic. Solid sufficient lower boundary and dashed strict repetition frontier have the correct meanings. |
| Figure 3 gap | Same checker, 501 exact rational geometry coordinates | All 2,004 enclosure checks passed. Exact rational one-use frontier, repetition frontier, stable gap and analytical tangent agree. The slope is exactly `18/289`; the stated domain is `0 <= lambda <= 1/4`, with fixed error `1/10`. |
| Figure 3 geometry | Same checker, nine axes | All 27 coordinate enclosures passed. Equal weights, unit-axis formula, exact diagonal frame entries and weakest eigenvalue agree. Common projection and scale are explicit in renderer code. Opposite endpoints belong to one axis; vertical guide is not an additional measurement. |
| Accepted display derivatives | Exact string substitution from original SVGs using only declared color mapping | All three match exactly apart from permitted hex-color substitutions. Geometry, labels, opacity, markers and dash patterns are preserved. |
| GitHub-native reading pages | `website/repository_preview.py --check`; inspection of generated links and equations | All 13 generated files match their sources; nine Markdown pages, three display SVGs and a manifest. Seven technical routes link directly to canonical documents. This is not an authenticated inspection of GitHub's renderer. |
| Optional HTML site | Fresh `website/build.py` and `website/check.py` | 16 HTML pages; 1,028 local links; 664 MathML expressions. The model retains 18 display equations and proof retains 119. Canonical TeX annotations and downloaded source bytes match. |
| Actual local HTTP delivery | `http_link_check.py` using a server bound to `127.0.0.1` | 107 unique local pages/resources returned HTTP 200; all 6,382,131 returned bytes matched the generated local files. Includes source and original/display figure downloads. This does not execute JavaScript or test browser layout. |
| Actual browser behavior | Recorded `website/browser_check.py --base-url http://127.0.0.1:8765` attempt | Failed at browser launch because the Chromium executable was absent. No pages or viewports were browser tested. |

The independent figure checker imports **no repository evaluator**, mpmath, or Decimal interval implementation. For each nonnegative rational `q`, it constructs a 120-decimal-place enclosure for `sqrt(q)` by integer square-root and verifies `lo^2 <= q <= hi^2`. Exact rational interval operations then enclose the plotted formulas. Every resulting interval lies inside the stored 60-place outward CSV enclosure. This checks the mathematical numerical values directly, without treating agreement with the source evaluator as proof. A total of **5,034** enclosures passed. The largest absolute error in a 17-significant-digit plotting value was approximately `4.9994204e-18`.

The cross-figure distinction was checked exactly:

`59/86 < 7/10 < p_cert(1/10) < p_rep(1/10)`.

The retained witness is therefore below the Figure 2 conservative strip, as the captions state. No witness marker is overlaid on that strip. Figure 3 uses a different ensemble and does not inherit the eight-use value.

## Visual inspection

All three approved preview PNGs were opened and inspected. All three accepted-color SVG derivatives were separately rasterized at 1,200 px width with Inkscape 1.2.2 and opened. Their files are `figure_01_channel_and_witness-display-inkscape.png`, `figure_02_guaranteed_region-display-inkscape.png`, and `figure_03_coplanar_limit-display-inkscape.png`.

Figure 1 has readable labels, unambiguous branch probabilities, correct sign/report distinction, a visible zero marker and correct block/per-use normalization. Figure 2 shows a narrow region without artificial thickening, an inset explicitly measuring probability width, distinct line styles, neutral unclassified surroundings, and open endpoint markers. Its captions specify the strict upper edge. Figure 3 has a common camera/scale for the three geometries, includes the zero endpoint, and labels the dashed line as a small-`lambda` asymptote rather than a fit. No scientifically incorrect visual encoding was found in these assets.

An initial PyMuPDF rasterization of SVGs displayed dash patterns as solid lines. Since exact SVG comparison showed unchanged `stroke-dasharray` attributes, this was investigated with Inkscape; Inkscape rendered the intended dashes correctly. The PyMuPDF raster files are retained only as an audit-renderer limitation, **not as evidence of a repository figure defect**. The PNGs named `*-display-inkscape.png` are the accepted visual-inspection evidence. Inkscape issued a `GtkRecentManager` warning but exited zero and produced the complete images.

The original 27 protected outputs and accepted palette-derived display assets intentionally serve different roles. Existing preapproval text in preserved historical exports is explained by README/STATUS and is not counted as a defect. The optional HTML pages use white backgrounds, system fonts, ordinary links and neutral navigation; the painting palette is confined to figure assets. No redesign is recommended.

## Reader semantics and interface limits

The short account correctly restricts the headline to finite full-span ensembles, independent uses and a common symmetric error strictly between zero and one half. It distinguishes optimized single-use coherent information from operational one-shot capacity; construction frontiers from exact capacity boundaries; a coplanar limitation of the long balanced repetition comparison from an all-code prohibition; and positive block coherent information from finite-block decoding fidelity or efficient decoding. The reader proof guide explicitly selects a positive finite inner block before invoking outer coding.

Both reading interfaces supply overview, channel, proof route, exact theorem, complete proof, figure atlas, limitations, references, source/evidence inventory and reproduction commands. GitHub-native pages are plain Markdown with linked canonical sources; local search and color-switch controls belong to the optional HTML version. README and generated reader footers distinguish them explicitly. No in-memory browser mirror was used or represented as GitHub.

The inspected JavaScript performs local search from a bundled index, toggles figures through local URLs, controls navigation/dialogs, and copies code. It contains no fetch, analytics or third-party content request. The CSS imports no remote font/style. Static checks found no external runtime assets. Since no browser launched, the absence of runtime-generated third-party requests is a source-inspection conclusion, not an observed browser-network claim. The HTTP resource checker itself made zero third-party requests.

The repository browser checker would check 16 desktop pages at 1440x1000, six selected mobile pages at 390x844, skip-link focus, search, Escape controls, Figure 1 color switching, a real next-page link, and no-JavaScript navigation/MathML. That is the intended executable coverage, **not coverage obtained here**. Desktop/mobile layout, live MathML appearance, keyboard behavior, search results, color switching, no-JavaScript layout, and GitHub's authenticated renderer all remain unverified in this audit environment. Safari and Firefox were not tested. The static contrast checks in `website/check.py` concern selected palette combinations and are not a comprehensive website accessibility audit.

## Findings and minimal recommendations

### R1. Relocated figure-input paths remain stale in the canonical specifications

- **Severity/confidence:** Low / high. **Type:** stale reader-facing documentation.
- **Locations:** `figures/FIGURE_SPECIFICATIONS.md` lines 45-47, 104, 115, 165-167.
- **Evidence:** Eight code-formatted paths use `data/<filename>` even though the files are at `data/figures/<filename>`. `DOCUMENTARY_FINDINGS.json` enumerates every missing path and existing replacement. The opening paragraph does correctly identify `data/figures/`, and current reader links and executable paths are correct.
- **Affected task:** A reader following a specific figure-input path can look in the wrong location. No scientific or numerical claim changes.
- **Smallest correction:** Update the eight documentary paths, or explicitly mark them as historical paths and provide a compact current-path mapping. Keep original source excerpts unchanged. This audit applies no correction.

### R2. Current status sentence retains the pre-repository assertion

- **Severity/confidence:** Low / high. **Type:** stale current wording.
- **Location:** `docs/MODEL_AND_CLAIMS.md`, section M08, line 181.
- **Evidence:** Its current paragraph says that no remote repository has been created, while README/STATUS identify this dedicated repository and its import commit. Unlike the explicitly preserved source footer, this sentence appears in the current status paragraph.
- **Affected task:** Understanding the current project stage; no theorem or data claim.
- **Smallest correction:** Remove only the obsolete no-remote-repository clause or date it explicitly as historical. Retain the no-manuscript statement and other source-provenance distinctions.

### R3. Actual browser review is blocked by the environment

- **Severity/confidence:** Moderate evidence gap / high. **Type:** environment limitation, not a demonstrated website defect.
- **Locations/commands:** `website/browser_check.py:36`; `browser-http-check.log`; `playwright-headless-shell-install.log`; `system-chromium-install.log`.
- **Evidence:** Playwright 1.57.0 installed successfully. Standard full Chromium installation failed with official CDN timeouts and mirror HTTP 400 responses. A smaller standard `--only-shell chromium` installation also exited 1 after 91.425 s. System `apt-get install -y chromium` exited 100 because the package was unavailable. The actual HTTP-mode checker exited 1 at launch in 0.872 s, before a single page was tested.
- **Affected task:** Independent confirmation of live desktop/mobile rendering and interactions. Figure assets and static/HTTP checks are unaffected.
- **Smallest verification path:** In an environment able to install the recorded Chromium runtime, run the existing browser checker against the already documented loopback server. No new scientific investigation or source redesign is required. Until then, do not call browser review passed.

### R4. Recorded Pandoc version could not be installed

- **Severity/confidence:** Low environment difference / high. **Type:** environment limitation.
- **Evidence:** The available converter is Pandoc 3.1.3 rather than the recorded 3.1.11.1. The documented official `.deb` download exited 28 after 10.025 s with `Proxy CONNECT aborted due to timeout`; see `pandoc-pinned-download.log`. A separate tool polling response reported `network approval was cancelled before a decision was returned`; this is recorded separately from the completed subprocess result, not substituted for its exit code. No escalation or network-policy workaround was attempted.
- **Affected task:** Recreating the exact historical HTML environment. Current build/static checks pass, and retained TeX annotations/source identity provide semantic evidence, but exact historical HTML-byte reproduction is not claimed.
- **Smallest verification path:** Install Pandoc 3.1.11.1 using the existing CI installation route and repeat the site build/check in a fresh directory. This does not affect the independently exact figure-data checks.

### Optional local-preview instruction improvement

`WEBSITE.md:13` and the `START_HERE.txt` generated by `website/build.py` show `python -m http.server` without a bind argument. Python's own help reports the default as all interfaces; the CI command already binds explicitly to `127.0.0.1`. For a reader who intends a loopback-only private preview, adding `--bind 127.0.0.1` would make the documentation consistent with that intent. This is a low-priority documentation improvement, not evidence of disclosure, public deployment, or a scientific pre-manuscript blocker. Every server used in this audit was bound to `127.0.0.1` and stopped.

## Reproduction and evidence inventory

Observed commands, exact return codes, elapsed times, log paths and SHA-256 values are in `COMMANDS.jsonl`. It preserves original audit-machine paths as historical execution evidence. The first full Chromium install was observed through tool output before the command recorder was established; its final exit was 1, but a precise overall duration was not recorded. The fully logged headless-shell attempt independently establishes the same runtime blocker. No Python invocation used `-O`.

Use the audit branch checkout and a new build directory for portable replay:

```bash
python audits/repository-sanity-01/reader/independent_figure_check.py --baseline . --output build/reader-independent-replay
python audits/repository-sanity-01/reader/documentary_findings.py --baseline . --output build/reader-independent-replay
python website/repository_preview.py --check
python website/build.py --output build/reader-site-replay
python website/check.py --site build/reader-site-replay
python audits/repository-sanity-01/reader/http_link_check.py --site build/reader-site-replay --output build/reader-independent-replay
```

When Chromium is installable, the smallest remaining live check is:

```bash
python -m pip install -r website/requirements-browser.txt
python -m playwright install --with-deps chromium
python -m http.server 8765 --bind 127.0.0.1 --directory build/reader-site-replay
```

In a second terminal, run:

```bash
python website/browser_check.py --site build/reader-site-replay --output build/reader-browser-replay --base-url http://127.0.0.1:8765
```

Then stop the local server. Inspect its screenshots and logs; the command name alone is not a visual review.

The core supporting evidence is `INDEPENDENT_FIGURE_CHECK.json`, `SITE_CHECK.json`, `HTTP_LINK_CHECK.json`, `DOCUMENTARY_FINDINGS.json`, `BROWSER_ATTEMPT.json`, the standalone checker scripts, recorded logs, and the three Inkscape figure images. Mathematical validity beyond these plotting checks and the parent's exact witness calculation remains the responsibility of the separate scientific audit findings. The only bounded follow-up indicated by this subtask is completion of the blocked browser review plus small documentary corrections; no additional scientific scope is required by these findings.
