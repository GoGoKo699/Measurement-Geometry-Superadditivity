# Preskill reader bridge implementation

**Implemented on `reader/preskill-bridge-v1`; review checks are recorded below.** This is educational documentation work. It contains no manuscript, new theorem, simulation campaign, scientific source repair or deployment.

## Starting point and authority

Repository identity and authenticated push access were confirmed for `GoGoKo699/Measurement-Geometry-Superadditivity`. The starting commit is **`f0015c56a19fd953c6797b2c64d9b507105234e3`**, tree **`72e93a89a691ec4d2ea799bb3b1008bd6c0dee20`**. `main` was still at that exact commit. The requested reader branch did not exist and was created there. The local checkout was reconstructed through the authenticated GitHub connector, with all 208 blob identities and the complete Git tree verified before editing; its working tree was clean. No repository-specific AGENTS or CONTRIBUTING instruction file was present in that tree.

The actual audit report at `5e367b1e541bf7d5ba1af90e85796d59db9e03f4`, correction report and exact correction metadata at `9ccecbf4cd3d975de2c498ba4fe2a9862f90778b` were read. Those commits remain on the separate, unmerged audit branch. The reader status links them and explains the rate/threshold qualification, figure-input path correction and obsolete remote-repository sentence. This branch does not silently import those canonical-file changes or contradict the corrected interpretation. Their eventual integration remains a separate review item.

The implementation checkpoint is **`4dba83be51ca8113f7082edf06a7e04b999f4a27`**, tree **`d1f0f8fcc203df35575f03584d66f9f1ab1f809c`**. [PR #4](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/pull/4) carries this work and the final evidence commit. Its final head is identified by the PR and delivery response, avoiding a self-referential commit hash in this file. The PR is intentionally draft because the existing scientific workflow skips its full-certificate jobs for draft PRs. Reader CI still executes. No workflow gate was weakened.

My-tone was not consulted or modified. Its earlier revision remains explicitly historical in the editorial record. No other project was accessed. Repository privacy, licensing and hosting settings remain unchanged.

## What the reader route now supplies

| Reader task | Before | After |
|---|---|---|
| Understand the result | Overview → channel → proof guide → atlas → limits → model/proof | Result and physical meaning first; optional focused background → channel and eight-use witness → geometric proof guide → exact model/proof → limits → verification |
| Bring tutorial knowledge into the project | No selected source or tutorial-to-project map | One pinned Preskill page, short notation crosswalk, exact return anchors and source/project roles |
| Inspect the mathematics directly | Existing technical routes | Direct expert bypass to theorem, full proof, figures and evidence remains on the overview and navigation |
| Read figures in context | Primarily the atlas and overview | Figure 1 linked at the witness, Figure 2 at the family guarantee, Figure 3 at the controlled limit; atlas still consolidates captions, data and original downloads |
| Maintain two interfaces | Website Markdown plus generated GitHub pages | Same editorial sources, one shared offline learning map, regenerated native pages, synchronized previous/next routes and local search |

[ROUTE_MAP.json](ROUTE_MAP.json) records exact old/new source paths and navigation. No existing route was removed and no second editable theorem, proof or caption was created.

The channel page now connects the operation budget to the reference-state calculation, reported-record average and flagged entropy identity. It distinguishes coherent repetition encoding from cloning and from its balanced test marginal. The retained eight-use example includes block/per-use normalization, every measured-count contribution, the negative all-measured term and the global one-use proof at the same parameters. The proof guide introduces the roles of Gamma and L before composing the geometric guarantee, and makes finite inner-block selection precede outer coding. It identifies the common-error step and computer-assisted scalar inequality as project mathematics. The limits page states the exact cone domain and keeps construction-specific statements distinct from all-code converses.

## Selected source and verified reading map

The sole external tutorial is **John Preskill, Quantum Shannon Theory, Chapter 10 of Quantum Information, [arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5)**. The [official PDF](https://arxiv.org/pdf/1604.07450v5) was read directly; title/version, subsection locations, equation identifiers and printed pages were checked. Its title says updated June 2025; arXiv dates v5 to 8 July 2025. Printed page k is viewer page k+6, not viewer page k.

The core route is §§10.7.1–10.7.2, printed pp. 51–56, and §10.7.4, pp. 58–60. The operational completion is the unassisted-achievability **statement** in §10.9.4, pp. 75–76. Optional refreshers remain within the same source: §§10.1, 10.2.1–10.2.4, 10.6.6 and 10.7.3. The page gives the question, retained concept and exact project destination for each passage. Optional proof depth is below the main route and does not become another prerequisite list.

The crosswalk distinguishes H/S, Q1/Q^(1), input state/register, reference/receiver/environment, physical probabilities and accuracy tolerances. It translates Preskill's “one-shot” terminology without calling the project quantity an operational one-shot capacity. Preskill already gives a qualitative repetition-code threshold improvement for a different channel; the bridge does not present that phenomenon as missing from the tutorial or newly discovered here.

Visual inspection confirms that v5 Eq. (10.368), printed p. 76, reverses the entropy difference. One short reader note gives H(B)-H(E), supported by definition (10.275) and the preceding exponent in (10.367). [SOURCE_VERIFICATION.md](SOURCE_VERIFICATION.md) records the inspection and PDF identity. No PDF, screenshot, chapter extract or textbook figure is committed. The tutorial is never fetched by the build, CI, numerical runtime or page renderer. Primary research citations remain attribution, not an additional tutorial route.

## Actual local checks and preservation

The isolated environment uses Python 3.12.14 with assertions enabled and the exact recorded Python package pins. Available Pandoc is 3.1.3; the recorded 3.1.11.1 download timed out. Thread limits, package versions, return codes and durations are retained in [runtime](runtime/) and [CHECK_RESULTS.json](CHECK_RESULTS.json). A different converter is not claimed to produce historically identical HTML bytes.

| Command or comparison | Actual result |
|---|---|
| `python verify.py` | Exit 0; source identities, provenance, inputs, independent-verifier boundaries and 27 protected originals checked. This is integrity, not entropy verification. |
| `python -m pytest -q -p no:cacheprovider tests website/tests` | Final local run: **96 passed**, 9.10 seconds reported by pytest, 9.689 seconds wall time. |
| `python website/repository_preview.py --write` then `--check` | Exit 0; 14 generated files, ten native editorial pages, seven linked canonical routes and three unchanged display SVGs. |
| `python website/build.py --output build/preskill-reader-review` | Exit 0; 17 HTML routes and 761 MathML expressions, using local Pandoc 3.1.3. |
| `python website/check.py --site build/preskill-reader-review` | Exit 0; 1,242 local links, source copies, canonical display equations, metadata identity and declared figure-color transformations checked. |
| Independent comparison against all 208 pinned files | **176 byte-identical; 32 authorized editorial/generator/test changes.** All canonical docs, scientific data, evidence, certificates, numerical implementations, captions and protected graphics remain identical. |
| Actual loopback HTTP crawl | 17 routes, 112 resources, 6,587,240 bytes matching the build and 571 resolved HTML anchor references. Twenty external links were observed but not requested. Server bound only to 127.0.0.1 and stopped. |
| Actual local `browser_check.py --base-url` attempt | Exit 1 at missing Chromium executable; zero browser pages visited. HTTP retrieval is not reported as a browser pass. |

[PRESERVATION.json](PRESERVATION.json) enumerates the exact byte comparisons and before/after hashes. [check_preservation.py](check_preservation.py) replays them without numerical computation or network access. The only changes in the root scientific manifest are README and STATUS identities; reversing those two fields recovers its original bytes. [ROOT_EDITORIAL_DIFF.txt](ROOT_EDITORIAL_DIFF.txt) preserves the authorized root-document diff. All 27 original graphical exports and all three accepted-palette reader SVGs are unchanged. Approval hashes were not regenerated. Canonical captions are inserted from their source and remain unchanged.

The first combined run correctly failed on a missing HTML source download and missing searchable sections. The new anchor/heading adjacency exposed a Pandoc issue also present in the inherited canonical pages: the old HTML proof rendered one H2 instead of its 16 source H2s, and the model one instead of nine. Authored Markdown now separates anchors from headings. For untouched canonical files, the converter inserts only that separator in memory. New tests check rendered heading coverage and unchanged TeX; no canonical byte is edited. The initial failures remain in [logs/tests.log](logs/tests.log), followed by the passing rerun. Tolerances and scientific reference results were not changed.

Browser installation used the recorded routes. The dependency installer hit managed-runtime apt restrictions, and standard Chromium downloads timed out or returned HTTP 400. A first HTTP attempt also exposed isolation between execution contexts; running the server and clients together resolved transport. The final reachable-server attempt still failed only at browser launch. [LOCAL_BROWSER_CHECK.json](LOCAL_BROWSER_CHECK.json) and [the server lifecycle](runtime/HTTP_REVIEW_LIFECYCLE.json) keep these limitations separate from source defects.

## Browser CI and interface boundary

The [checkpoint reader workflow](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/actions/runs/34681565631) **completed successfully** on implementation commit `4dba83be51ca8113f7082edf06a7e04b999f4a27`. The workflow ran from 07:45:47 to 07:49:28 UTC on 12 September 2026. It installed the recorded Python 3.13.5, Pandoc 3.1.11.1 and Python dependencies, passed all **96 tests** in 13.36 seconds, and executed the real loopback HTTP browser checks. This resolves the browser and pinned-converter verification gap for the implementation; it does not retroactively turn the local installation failures into passes.

The inspected [browser record](ci/CHECKPOINT_BROWSER_CHECK.json) reports **Chromium 152.0.7977.0**, desktop 1440 × 1000 and mobile 390 × 844. All 17 routes passed configured navigation, source-download byte checks and viewport checks. The run exercised previous/next and background return links, mobile navigation, search for Preskill and the all-measured branch, keyboard skip/search/Escape controls, all three figure-color switches, and no-JavaScript reading and mathematics on the proof, figures, background and channel pages. It recorded no external requests, failed requests or console/page errors. These are actual browser interactions, not an in-memory mirror.

The workflow artifact was retrieved and its SHA-256 matched GitHub's recorded digest. Its build, integrity and browser records were inspected, together with desktop/mobile screenshots of the overview, background, channel, proof guide and figure atlas. The pages use plain documentation styling; the accepted palette remains inside the three figures. Mobile prose is legible, and wide mathematics and tables use the existing horizontal scroll regions. Visual inspection at the initial scroll position does not claim that every table column is simultaneously visible or that horizontal scrolling was separately exercised. [VISUAL_REVIEW.md](VISUAL_REVIEW.md) and [the artifact comparison](ci/ARTIFACT_VERIFICATION.json) record the inspection and exact evidence hashes. The protected figure downloads and accepted display SVGs match their repository bytes.

[CI_CHECKPOINT.json](CI_CHECKPOINT.json) preserves the actual workflow, job and artifact results. The [scientific workflow](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/actions/runs/34681565622) is **skipped** by its existing draft-PR condition; skipped jobs are not passes. No full entropy certificate or large simulation was run for this redesign. The final commit adds review records only; its own PR checks are inspected at handoff and reported in the PR without presenting a running check as passed.

GitHub-compatible generated Markdown, source links and explicit anchor targets were checked separately. GitHub's authenticated renderer was not inspected. No Safari or Firefox run is claimed. These checks do not constitute an external user study or certify educational prose automatically.

## Reader walkthroughs and maintenance

[READER_WALKTHROUGHS.md](READER_WALKTHROUGHS.md) documents the three assistant walkthroughs: a reader prepared by the selected tutorial, an expert bypassing it, and a reader tracing each display to its source and scope. They found no concrete semantic defect and verified the witness/strip distinction, analytical asymptote, restricted cone domain and known-background/project-result separation. These are our own reviews, not invented external testing or measured learning outcomes.

Future reader prose has one editorial home: **`website/pages/`**. The selected background map and crosswalk live in **`website/learning_bridge.json`**. Route configuration is `website/site.json`; editorial source attribution is `website/editorial_map.json`. Run the actual native `--write` command after editing and then the documented checks. Keep canonical mathematics and captions in their existing files. The new tests validate metadata, routes, headings, source math and generated consistency; they perform no online tutorial fetch.

The branch is for author review. Pending audit-correction integration is visible and separate. No new bounded scientific task is indicated or undertaken by this redesign. No merge, release, public hosting, manuscript or research extension follows this report.
