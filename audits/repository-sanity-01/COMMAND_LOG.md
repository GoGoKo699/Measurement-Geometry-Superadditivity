# Command and result log

Audit baseline: `f0015c56a19fd953c6797b2c64d9b507105234e3`; tree `72e93a89a691ec4d2ea799bb3b1008bd6c0dee20`. The scientific checkout was kept unchanged. Fresh results were generated under its ignored `build/audit-full` and `build/audit-site` directories; their retained evidence is linked below. No test was run with Python `-O`, no tolerance or reference hash was changed, and a failed or blocked command is not counted as a pass.

All durations below are measured wall-clock seconds, rounded to six decimals unless the original record has fewer digits. Machine-readable records retain their full measured precision, original command arguments, UTC timestamps and working directories. Several independent audit tasks overlapped, so elapsed times are audit execution records, not isolated performance benchmarks. Reproduction instructions are in [REPLAY.md](REPLAY.md).

## Environment and resource limits

The principal commands used `../audit-venv/bin/python` from the pinned checkout. The isolated environment installed the versions in `requirements.txt`, `website/requirements.txt` and `website/requirements-browser.txt`; [install.log](environment/install.log) records installation, and [environment.json](environment/environment.json) lists the complete observed package set.

| Component | Recorded scientific environment | Observed audit environment | Consequence |
|---|---|---|---|
| Python | 3.13.5, GCC 14.2.0 | 3.12.13, Clang 22.1.3 | Interpreter differs; successful byte reproduction is established by actual comparisons below. |
| Platform | Linux 6.18.35, glibc 2.41 | Linux 6.18.35, glibc 2.39 | Platform differs; no universal cross-platform byte guarantee is inferred. |
| Scientific packages | Pinned package versions | All nine listed scientific package pins matched | NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0, SymPy 1.14.0, Matplotlib 3.10.8, PyMuPDF 1.26.7, Pillow 12.3.0, ReportLab 4.4.9 and pytest 9.0.2. |
| HTML converter | Pandoc 3.1.11.1 | Pandoc 3.1.3 | HTML semantic/static checks passed; exact historical HTML-byte reproduction is not claimed. |
| Website Python dependencies | Beautiful Soup 4.14.3; Playwright 1.57.0 | Same versions installed | Chromium runtime acquisition failed; browser execution remained blocked. |
| Independent SVG visual inspection | Not a scientific dependency | Inkscape 1.2.2 | Used only to inspect accepted-color SVGs; no approved export was replaced. |

The environment exposed nine CPUs in affinity, a cgroup quota of eight CPU-equivalents (`800000 100000`), and a 20 GiB cgroup memory maximum (`21474836480` bytes). `RLIMIT_AS` and `RLIMIT_CPU` were unlimited; the open-file limit was 16,384 and soft stack limit was 8 MiB. The principal wrapper set `PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `MPLBACKEND=Agg` and `PYTHONUNBUFFERED=1`. The logged maximum child RSS is a process-resource statistic, not an aggregate measurement of simultaneous memory use across all audit agents.

## Principal repository commands

Here `python` denotes the isolated interpreter recorded above, not an unspecified system Python.

| Command | Return code | External wall seconds | Recorded child maximum RSS, KiB | Actual result |
|---|---:|---:|---:|---|
| `python verify.py` | 0 | 0.683400 | 29,304 | Integrity/provenance check passed: 165 manifest files, 44 source identities, 23 canonical units, 125 source fragments, seven claims, 237 current-document links and 27 protected graphical artifacts. This command does not prove the entropy inequality. |
| `python -m pytest -q -p no:cacheprovider tests website/tests` | 0 | 17.561725 | 185,924 | **73 tests passed**; pytest's internal report says 14.68 s. This includes the scientific and website test directories. |
| `python reproduce.py --output build/audit-full --full --rebuild-certificate` | 0 | **1010.528159** | 160,120 | Full scientific replay and certificate reconstruction completed; before/after integrity passed. Its own final test run passed **52 tests in 2.35 s** and covers `tests`, not `website/tests`. |

Exact command records: [integrity.json](environment/integrity.json), [tests.json](environment/tests.json), [full.json](environment/full.json). Raw output: [integrity.log](environment/integrity.log), [tests.log](environment/tests.log), [full.log](environment/full.log), and the full replay's separate [inner tests log](full-run/logs/tests.log). The top-level [REPRODUCTION_RESULT.json](full-run/REPRODUCTION_RESULT.json) is corroborated by the stage evidence below; its wrapper name and final Boolean are not used as substitutes for inspecting coverage.

## Full replay stages actually executed

The pinned `reproduce.py` invokes each stage with `subprocess.run(..., check=True)` and aborts on failure. All stage commands below therefore completed with return code zero before the final top-level zero result. Separate complete wall times were not recorded for individual stages; none are invented from file timestamps. Certificate generation logs include periodic elapsed progress messages, but those are not a complete final-stage timer.

In this table, `OUT` means the fresh `build/audit-full` output directory and `CERT` means the unchanged `certificates/common_noise_compact_certificate.json`. Every command was invoked with the same isolated interpreter.

| Stage command, excluding interpreter | Fresh stage evidence | Established result |
|---|---|---|
| `numerics/figure_inputs/build_inputs.py --output OUT/data/figures` | [data_build.log](full-run/logs/data_build.log) | Regenerated ten data/provenance outputs, including the two-value witness panel, all nine mask terms, 1,001 error rows, 501 cone rows, nine geometry axes and 12 small-geometry controls. |
| `numerics/figure_inputs/verify_inputs.py --data OUT/data/figures --report OUT/data_validation.json` | [data_check.log](full-run/logs/data_check.log), [data_validation.json](full-run/data_validation.json) | Checked the new plotting inputs, formulas, geometry, controls and interpretation flags. |
| `figures/code/render_figures.py --output OUT/figures` | [figure_render.log](full-run/logs/figure_render.log) | Regenerated all three figures and seven separate vector components. |
| `figures/code/build_review_pdf.py --figures OUT/figures --output OUT/figures/three_figure_review.pdf` | [review_render.log](full-run/logs/review_render.log) | Recreated the protected review PDF. |
| `figures/code/verify_render.py --output OUT/figures --report OUT/render_validation.json` | [figure_check.log](full-run/logs/figure_check.log), [render_validation.json](full-run/render_validation.json) | Checked regenerated render structure and source-derived values; visual inspection is recorded separately in the reader report. |
| `verification/integer/certify_all_noise.py --output OUT/certificate/rebuilt --bits 128` | [certificate_build.log](full-run/logs/certificate_build.log), [partition identity](environment/partition_rebuild.json) | Rebuilt a complete deterministic cover: **512 noise bands and 29,635 input leaves**. The reconstructed certificate is byte-identical to the canonical one. |
| `verification/integer/certify_all_noise.py --verify CERT --output OUT/certificate/integer --bits 224` | [certificate_integer.log](full-run/logs/certificate_integer.log), [integer result](full-run/certificate/integer/verification_224.json) | Full integer/dyadic verification of all 512 bands and 29,635 leaves; strict compact negativity and positive tail bounds. |
| `verification/mpmath/cross_backend.py --certificate CERT --output OUT/certificate/mpmath85.json --digits 85` | [certificate_mpmath.log](full-run/logs/certificate_mpmath.log), [mpmath result](full-run/certificate/mpmath85.json) | Full 85-digit mpmath interval verification of the same entire cover, using its separate entropy-difference evaluation. |
| `verification/decimal/verify_certificate.py --certificate CERT --output OUT/certificate/decimal130.json --precision 130` | [certificate_decimal.log](full-run/logs/certificate_decimal.log), [Decimal result](full-run/certificate/decimal130.json) | Full 130-digit Decimal interval verification of all 29,635 rectangles, using its independently written entropy-conjugate secant maximum. |
| `verification/decimal/check_witness.py --output OUT/witness/decimal100.json --precision 100` | [witness_decimal100.log](full-run/logs/witness_decimal100.log) | Recalculated the retained witness at 100 digits, including all mask terms. |
| `verification/decimal/check_witness.py --output OUT/witness/decimal140.json --precision 140` | [witness_decimal140.log](full-run/logs/witness_decimal140.log) | Recalculated the retained witness at 140 digits and reproduced the stored witness record. |
| `verification/mpmath/witness_and_controls.py --output OUT/witness/mpmath` | [witness_mpmath_controls.log](full-run/logs/witness_mpmath_controls.log) | Recalculated the separate mpmath witness and both retained mixed-input/rejected-floating-candidate controls. |
| `verification/analytic/check_endpoints.py --output OUT/analytic/analytic_checks.json` | [analytic_symbolic.log](full-run/logs/analytic_symbolic.log) | Checked three polynomial identities, exact endpoint constants, the geometric coefficient and the cone-domain bound. |
| `verification/analytic/run_rational_checks.py --output OUT/analytic/rational_endpoint_checks.json` | [analytic_rational.log](full-run/logs/analytic_rational.log) | Independently checked exact rational low/high-noise constants, the `1/35` geometry minimum and `3/35` gap coefficient. The functional endpoint arguments still require the proof audit. |
| `verification/physical/physical_check.py --output OUT/physical/physical_check.json` | [physical_checks.log](full-run/logs/physical_checks.log), [physical result](full-run/physical/physical_check.json) | Five tractable physical cases; 455 reported records and 2,561 hidden-outcome terms. Largest full matrix dimension 128; maximum comparison error `1.4259426972529354e-15`, below the declared `2e-12` limit. No full eight-use matrix was constructed. |
| `-m pytest -q -p no:cacheprovider tests` | [tests.log](full-run/logs/tests.log) | **52 passed in 2.35 s**, followed by another unchanged-baseline integrity check. |

The compact certificate covers exact rational domains `c in [1/268435456,24/25]` and `t in [1/1000000,1/2]`; analytical endpoint and nearly pure-input arguments complete the claimed domain. Each full verifier reports its own enclosure. The integer/mpmath compact upper is approximately `-5.71962366e-12`; Decimal's alternative bound is approximately `-2.37355635e-10`. These different valid upper bounds are not discrepancies requiring equal numeric output. All three report a positive tail margin approximately `0.00028189136168575773`.

### Exact bytes, valid numerical comparison, and unsupported agreement

- **Exact bytes:** [data_comparison.json](full-run/data_comparison.json) reports all ten regenerated plotting/provenance files byte-identical. [figure_comparison.json](full-run/figure_comparison.json) reports all **27** regenerated approved graphical artifacts byte-identical. [full_reference_comparison.json](full-run/full_reference_comparison.json) reports all nine explicitly compared scientific result records byte-identical, including this run's ordinary floating-point physical record.
- **Exact reconstructed cover:** The rebuilt certificate contains 2,524,387 bytes, SHA-256 `ab500804e56ba8c5ffb1ca7c1f38e3fd720b01561122b3a2bcc367a106ad66dd`; [partition_rebuild.json](environment/partition_rebuild.json) confirms byte identity. Checking the stored cover and reconstructing it are separate steps, both completed here.
- **Mathematical enclosure comparison:** The separately recalculated mpmath witness interval contains the positive Decimal140 witness interval, and both contain nine all-mask records. This nesting is checked explicitly by the full comparator. The three compact certificate implementations need not produce identical bounds because their valid analytical evaluators differ.
- **Numerical diagnostic agreement:** Independent high-precision witness calculations and small physical matrices are described below with their precision/tolerance limits. They are not promoted to new rigorous full-domain certificates.
- **Not established merely by these results:** Byte equality, backend agreement and test counts do not by themselves validate a shared analytical inequality, literature priority, browser behavior, or proof-assistant formalization. The separate scientific and attribution reports address their own evidence.

## Website and independent figure commands

Complete arguments, original working directory, UTC start time, return code, duration and output-log SHA-256 are preserved in [reader/COMMANDS.jsonl](reader/COMMANDS.jsonl). The table lists all recorded reader-subtask commands in functional form; output paths remain explicit in that raw record.

| Command / recorded name | Return code | Wall seconds | Result / evidence |
|---|---:|---:|---|
| `website/repository_preview.py --check` | 0 | 0.074562 | Generated GitHub Markdown/assets match; [log](reader/reader-generated-check.log). |
| `website/build.py --output build/audit-site` | 0 | 5.579608 | Fresh 16-page HTML site built with Pandoc 3.1.3; [log](reader/site-build.log). |
| `website/check.py --site build/audit-site --report .../SITE_CHECK.json` | 0 | 2.285869 | 1,028 local links and 664 MathML expressions checked; [SITE_CHECK.json](reader/SITE_CHECK.json). |
| Independent figure checker, initial invocation | 0 | 0.995354 | 5,034 rational enclosures passed; [log](reader/independent-figure-check.log). |
| Independent figure checker, portable `--baseline/--output` replay | 0 | 1.499798 | Same result after adding portable arguments; [log](reader/independent-figure-portable-replay.log), [result](reader/INDEPENDENT_FIGURE_CHECK.json). |
| Documentary finding reproduction | 0 | 0.140729 | Reproduced stale paths/status and documented server binding defaults; [log](reader/documentary-findings.log). |
| Independent loopback HTTP resource check | 0 | 1.525508 | 107 unique resources returned 6,382,131 exact matching bytes; [HTTP_LINK_CHECK.json](reader/HTTP_LINK_CHECK.json). This is not a browser test. |
| Official Pandoc 3.1.11.1 `.deb` download using `curl --connect-timeout 10 --max-time 20` | **28** | 10.024726 | Proxy CONNECT timed out; [log](reader/pandoc-pinned-download.log). |
| `apt-get install -y chromium` | **100** | 0.050056 | System package unavailable; [log](reader/system-chromium-install.log). |
| `website/browser_check.py --site build/audit-site --output .../browser --base-url http://127.0.0.1:8765` | **1** | 0.871899 | Failed at Chromium launch; no browser page was reached; [log](reader/browser-http-check.log). |
| `env PLAYWRIGHT_DOWNLOAD_CONNECTION_TIMEOUT=10000 python -m playwright install --only-shell chromium` | **1** | 91.424848 | Standard smaller-runtime attempt also failed via official CDN timeouts / mirror HTTP 400; [log](reader/playwright-headless-shell-install.log). |

The earlier standard `python -m playwright install chromium` attempt was observed to exit 1 after official CDN timeouts and mirror HTTP 400 responses. It preceded the complete command recorder, so its overall duration is **not recorded**; it is not guessed. A tool polling operation during the Pandoc attempt separately reported that network approval was cancelled before a decision. The subprocess's completed result remains the recorded curl return code 28 and timeout log; these are distinct observations. No restriction-bypassing download method was used.

All local review servers bound to `127.0.0.1` and were stopped. [BROWSER_ATTEMPT.json](reader/BROWSER_ATTEMPT.json) explicitly reports zero tested browser pages and no authenticated GitHub renderer inspection. Desktop/mobile layout, JavaScript search, keyboard controls, color switching and no-JavaScript browser layout are **blocked**, not passed. No in-memory mirror was substituted. The GitHub-native Markdown route and optional HTML route remain separate interfaces.

Visual inspection used the three original PNG previews and the three display SVGs rasterized with Inkscape; image evidence and the initial PyMuPDF dash-style limitation are explained in [READER_AND_FIGURES_AUDIT.md](reader/READER_AND_FIGURES_AUDIT.md). These are figure inspections, not website screenshots.

## Additional independent audit commands and preserved failures

These checks were separate from the pinned implementations. They did not modify the source, replace approved outputs, or rerun a legacy pipeline.

| Subaudit | Return code and measured time | Scope and evidence |
|---|---|---|
| Entropy identities and extreme-point diagnostics | 0; 10.218056 s | Exact rational endpoint constants and 200 coefficient identities; 187 scalar and 935 directional points at 380 decimal digits, including very small noise/input values. This point evidence is expressly not a global interval certificate. [Command manifest](entropy/subaudit_manifest.json), [result](entropy/portable-check/independent.json). |
| Malformed-cover and low-precision rejection diagnostics | Driver 0; recorded malformed-subcase time sum 1.982089 s, **not a recorded overall process duration** | Twelve malformed cases for each of three unchanged verifiers: 36 expected failures, plus seven mpmath low-precision failures. Includes changed polynomial/domain/tail split, empty/gapped/reversed domains, NaN endpoints, missing/reversed/overlapping input intervals and an uncertifiable coarse leaf. All were rejected. [Failure evidence](entropy/portable-check/failure.json). |
| Independent small physical repetition calculation | 0; 0.807485 s | Seven complete cases, 1,259 reported branches and 7,671 hidden terms, using pinned NumPy but no imported repository evaluator. [Command record](coding/COMMANDS.json), [physical results](coding/physical_results.json). |
| Independent eight-use hidden-outcome witness, final run | 0; 2.694 s shell wall time | Two nearest-arithmetic precisions, no full eight-use density matrix. Block value approximately `0.0005981981270524771`, per-use value `0.00007477476588155964`, all-measured contribution approximately `-0.01653160578648965`. Eleven reference quantities checked; precision difference approximately `3.5530e-72`. [Command record](witness/command-results.json), [final log](witness/calculation-final.log), [results](witness/results.json). |

The entropy diagnostic's portable adapter was replayed to confirm that adding explicit baseline/output arguments and fresh-output protection changed no mathematical/test result; [comparison.json](entropy/portable-check/comparison.json) excludes only timing fields. Audit helper portability is separate from altering scientific implementations, which were kept intact.

Preserved unsuccessful attempts are not hidden:

- An early coding-subtask dependency probe returned 1 in 0.054893 s because NumPy installation was still in progress. The subsequent identical probe returned 0 in 0.379089 s with NumPy 2.3.5; see [coding/COMMANDS.json](coding/COMMANDS.json).
- The independent witness initially attempted `/usr/bin/time -v`, returning 127 because that executable was absent. The shell timer was then used. Its first timed calculation returned 1 after 3.759 s because the new audit harness mishandled a zero-width rational comparison. Only that audit-script comparison was corrected; the baseline was unchanged. The successful 2.694 s run and both earlier logs remain in [witness/command-results.json](witness/command-results.json), [run.log](witness/run.log), [calculation.log](witness/calculation.log) and [calculation-final.log](witness/calculation-final.log).
- Malformed-certificate failures are expected rejection evidence. Browser/Pandoc acquisition failures are environment limitations. They are neither successful checks nor counterexamples to the scientific theorem.

Primary-literature examination is documented in [literature/REPORT.md](literature/REPORT.md); it is not a numerical command gate. Read the [executive report](REPORT.md), scientific subreports and claim ledger for what the inspected proof and attribution evidence establish beyond this execution record.
