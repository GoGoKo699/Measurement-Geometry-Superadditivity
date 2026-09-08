# Reproduce the audit evidence

Use a checkout of the audit branch whose scientific source is pinned to `f0015c56a19fd953c6797b2c64d9b507105234e3`. Run from its root. All output paths below must be new. Do not use Python `-O`.

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt -r website/requirements.txt -r website/requirements-browser.txt
.venv/bin/python verify.py
.venv/bin/python -m pytest -q -p no:cacheprovider tests website/tests
.venv/bin/python reproduce.py --output build/audit-replay-full --full --rebuild-certificate
```

The full command first verifies all tracked reference hashes, generates ten plotting inputs, draws and byte-compares 27 approved artifacts, rebuilds the rational certificate at 128 bits, then checks all 512 bands and 29,635 leaves with integer224, mpmath85, and Decimal130 routes. It subsequently checks both Decimal witness precisions, the separate mpmath witness and retained controls, analytic constants and the physical reduction. Its own final tests cover `tests`, so the separate combined command above also includes `website/tests`. Read every stage log; no old result file is used as proof of execution.

Independent audit evidence can be regenerated separately:

```bash
mkdir -p build/audit-replay-independent
.venv/bin/python audits/repository-sanity-01/entropy/independent_entropy_checks.py --output build/audit-replay-independent/entropy.json
.venv/bin/python audits/repository-sanity-01/entropy/certificate_failure_checks.py --baseline . --output build/audit-replay-independent/failure-controls.json
.venv/bin/python audits/repository-sanity-01/coding/independent_physical_repetition.py build/audit-replay-independent/physical.json
.venv/bin/python audits/repository-sanity-01/witness/independent_hidden_outcomes.py --baseline . --output build/audit-replay-independent/witness.json
.venv/bin/python audits/repository-sanity-01/reader/independent_figure_check.py --baseline . --output build/audit-replay-independent/figures
```

The entropy point diagnostics, physical matrices and high-precision witness are independently derived checks, not new rigorous full-domain certificates. The figure checker uses exact rational square-root enclosures. The malformed-cover tests call the three unchanged implementations on separate in-memory mutations and expect failures. They do not repair, weaken, or replace the mathematical verifier.

For the optional website, install the recorded Pandoc 3.1.11.1 as specified in `.github/workflows/reader-site.yml`. The audit's available Pandoc 3.1.3 passed static semantic checks, but exact converter-version reproduction was unavailable. Then run:

```bash
.venv/bin/python website/repository_preview.py --check
.venv/bin/python website/build.py --output build/audit-replay-site
.venv/bin/python website/check.py --site build/audit-replay-site
.venv/bin/python -m playwright install --with-deps chromium
.venv/bin/python -m http.server 8765 --bind 127.0.0.1 --directory build/audit-replay-site
```

Leave that loopback server running and use a second terminal:

```bash
.venv/bin/python website/browser_check.py --site build/audit-replay-site --output build/audit-replay-browser --base-url http://127.0.0.1:8765
```

Stop the server after review. Browser runtime acquisition was blocked in this audit; the actual HTTP test was attempted and failed at launch, not passed. These commands are the smallest remaining behavioral verification path once Chromium is available. Do not substitute the in-memory mirror or prior hosted CI for an authenticated inspection of GitHub's renderer. The GitHub-native Markdown and optional HTML site are different interfaces.
