# What each verification command establishes

A readable theorem, an immutable input file, and an executed proof check are different things. The repository includes each, with their roles kept separate.

## Inspect the sources

Start with the [model and claims](../../docs/MODEL_AND_CLAIMS.md), [complete proof](../../docs/COMPLETE_PROOF.md), and [reference roles](../../docs/REFERENCES.md). The technical documents are the canonical scientific sources. This website renders them directly rather than maintaining a rewritten second proof.

The preserved scientific baseline is commit `9a1e4cb3bad843db9cec1fa348870ca7162df0e0`. Its read-only GitHub checks passed during import and on merged main. That is a recorded baseline result, not a claim that opening this page reruns a computation. [Recorded baseline validation](../../validation/BASELINE_VALIDATION.json)

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

Use a new output directory. The default command regenerates plotting inputs and reproduces approved graphical files in the recorded environment. It does not recalculate the entire mathematical certificate. The new website colors are a separate presentation study and do not replace those approved outputs.

## Recheck the mathematical evidence

```bash
python reproduce.py --output build/full-check --full
```

This runs the three complete compact-certificate verifiers, analytical endpoint constants, independent witness calculations, retained safeguards, direct small physical checks, and figure reproduction. Adding `--rebuild-certificate` also reconstructs the rational covering; it is not needed merely to check each inequality on the included cover.

The integer, mpmath, and Decimal routes remain separate. Their agreement supports the computational result, but shared analytical assumptions still require the written proof. The physical controls check the actual noisy-report calculation; they do not replace the universal entropy bound. [Exact commands, output contracts, and limitations](../../docs/REPRODUCTION.md)

## Inspect the outputs before claiming a result

The canonical cover has 512 noise bands and 29,635 input leaves. Evidence records and comparisons are in [the material inventory](materials.md). Ordinary floating-point physical controls use declared tolerances; exact certificates and approved graphical files have stronger identity contracts. Fresh results belong in a new build directory, not on top of reference evidence.

The stored audit is author-side work with independently written implementations, not an independent external researcher or a proof-assistant formalization. No stronger assurance is implied by this website.
