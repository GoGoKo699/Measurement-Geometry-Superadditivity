# What each verification command establishes

A readable theorem, an immutable input file, and an executed proof check are different things. The repository includes each, with their roles kept separate.

<a id="verification-roles"></a>

## Inspect the sources

Start with the [model and claims](../../docs/MODEL_AND_CLAIMS.md), [complete proof](../../docs/COMPLETE_PROOF.md), and [reference roles](../../docs/REFERENCES.md). The technical documents are the canonical scientific sources. This website renders them directly rather than maintaining a rewritten second proof.

The scientific argument is available without running software. The commands below check distinct parts of its supporting evidence; reading a stored result does not execute a new computation.

## Check file identity and method tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python verify.py
python -m pytest -q -p no:cacheprovider tests
```

`verify.py` checks integrity, protected figures, provenance, source links, and verifier boundaries. It does **not** verify the entropy inequality. The unit tests include method and rejection controls, but they are not the complete-domain certificate.

## Rebuild the approved figures

```bash
python reproduce.py --output build/figures-check
```

Use a new output directory. The default command regenerates plotting inputs and reproduces approved graphical files in the recorded environment. It does not recalculate the entire mathematical certificate. The accepted figure palette remains separate from the protected original exports.

## Recheck the mathematical evidence

```bash
python reproduce.py --output build/full-check --full
```

This runs the three complete compact-certificate verifiers, analytical endpoint constants, independent witness calculations, retained safeguards, direct small physical checks, and figure reproduction. Adding `--rebuild-certificate` also reconstructs the rational covering; it is not needed merely to check each inequality on the included cover.

The integer, mpmath, and Decimal routes remain separate. Their agreement supports the computational result, but shared analytical assumptions still require the written proof. The physical controls check the actual noisy-report calculation; they do not replace the universal entropy bound. [Exact commands, output contracts, and limitations](../../docs/REPRODUCTION.md)

## Inspect the outputs before claiming a result

The canonical cover has 512 noise bands and 29,635 input leaves. Evidence records and comparisons are in [the material inventory](materials.md). Ordinary floating-point physical controls use declared tolerances; exact certificates and approved graphical files have stronger identity contracts. Fresh results belong in a new build directory, not on top of reference evidence.

The stored records do not establish external peer review or proof-assistant formalization. No stronger assurance is implied by the reading interface.

To return to the explanation, see [the all-record witness](channel.md#eight-use-witness) and [where the scalar proof enters](proof-guide.md#scalar-proof). The [selected background](background.md) explains the coding quantities; it is not an additional certificate or a software dependency.

## Check the current revision

Run `python integrity/check_scientific.py` to compare the current scientific files and figure exports with their protected SHA-256 identities. This check is direct and works without Git history. It does not execute a certificate verifier.

[Protected file identities](../../integrity/SCIENTIFIC_FILES.json) · [Integrity checker source](../../integrity/check_scientific.py)

[GitHub Actions](https://github.com/GoGoKo699/Measurement-Geometry-Superadditivity/actions) shows the workflows for each commit. Open the run for the revision you are using and inspect its commands and result; a configured, skipped or running check is not a pass. Fresh local output directories let you inspect the same obligations yourself. The [website guide](../../WEBSITE.md) includes the separate Markdown, HTML and loopback browser checks.
