# Runtime verification follow-up

Date: 2026-09-08. This bounded follow-up retried the two environment limitations recorded in the completed audit. It did not change a scientific source, approved graphic, runtime requirement, or expected result.

The existing isolated environment still provides **Playwright 1.57.0** and the system converter remains **Pandoc 3.1.3**. Exact command arguments, working directories, return codes, elapsed times, and log SHA-256 values are recorded in `COMMANDS.jsonl` using the existing audit command recorder.

| Attempt | Result | Duration |
|---|---|---:|
| Official Pandoc 3.1.11.1 GitHub release download, with HTTPS restrictions and bounded connection/total timeout | curl exit 28; `Proxy CONNECT aborted due to timeout` | 10.032 s |
| Standard Playwright `install --only-shell chromium`, using a 10-second connection timeout | exit 1; three official CDN timeouts and two standard mirror HTTP 400 responses | 108.195 s |

The Playwright command requested Chromium Headless Shell 143.0.7499.4, build v1200. These were the installer's built-in attempts within **one invocation**; no custom mirror, repeated installer invocation, alternative network tunnel, or approval workaround was used. The official Pandoc route was invoked once. A separate tool polling error for the Pandoc session is preserved in `TOOL_EVENTS.json`; it is distinct from the completed and logged curl result.

After the failed installation, direct availability checks found no system `chromium`, `chromium-browser`, or `google-chrome`, no Playwright Chromium executable, and no executable at the exact Playwright 1.57 headless-shell path recorded by the earlier launch failure. The initial generic availability command included a glob for an older headless-shell directory layout; `headless-shell-availability.log` checks the exact current path directly.

**Both environment gaps remain open.** No browser was launched and no page, viewport, interaction, live MathML rendering, or browser network request was tested in this follow-up. The earlier audit's blocked browser status must not be converted into a pass. No unnecessary rerun of the known-to-fail browser launch was performed.

The remaining verification path is unchanged: install the recorded Pandoc and Chromium versions in an environment that permits their standard downloads, build into a fresh directory, run the static checker, and run `website/browser_check.py --base-url http://127.0.0.1:8765` against a server explicitly bound to `127.0.0.1`. Inspect the resulting desktop/mobile screenshots and browser report. These are environment-dependent verification tasks, not evidence of a scientific or website-source defect.

The parent correction report separately records the actual updated-site build and static checks. This follow-up created only the evidence in this directory.
