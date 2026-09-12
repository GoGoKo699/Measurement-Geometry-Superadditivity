# What each verification command establishes

[Overview](README.md) · [Background](background.md) · [Channel](channel.md) · [Proof route](proof-guide.md) · [Figures](figures.md) · [Exact theorem](../docs/MODEL_AND_CLAIMS.md) · [Complete proof](../docs/COMPLETE_PROOF.md) · [Materials](materials.md)

<details>
<summary>All reading routes</summary>

- [The project](README.md)
- [Selected background](background.md)
- [The channel](channel.md)
- [The proof route](proof-guide.md)
- [Figure atlas](figures.md)
- [Scope and limits](limits.md)
- [Exact model and theorem](../docs/MODEL_AND_CLAIMS.md)
- [Complete proof](../docs/COMPLETE_PROOF.md)
- [Verification guide](verification.md)
- [Exact reproduction commands](../docs/REPRODUCTION.md)
- [References and their roles](../docs/REFERENCES.md)
- [Source materials](materials.md)
- [Notation crosswalk](../docs/NOTATION_CROSSWALK.md)
- [Source and proof ledger](../docs/SOURCE_TO_CANONICAL.md)
- [Frozen scientific argument](../docs/FROZEN_ARGUMENT.md)
- [Visual design](visual-design.md)
- [Status and publication](status.md)

</details>


A readable theorem, an immutable input file, and an executed proof check are different things. The repository includes each, with their roles kept separate.

<a name="verification-roles"></a>

## Inspect the sources

Start with the [model and claims](../docs/MODEL_AND_CLAIMS.md), [complete proof](../docs/COMPLETE_PROOF.md), and [reference roles](../docs/REFERENCES.md). The technical documents are the canonical scientific sources. This website renders them directly rather than maintaining a rewritten second proof.

The reader redesign preserves the scientific files at `f0015c56a19fd953c6797b2c64d9b507105234e3`. The earlier import checks and later audit are recorded prior results. The [current status](status.md#correction-record) distinguishes them from the actual presentation checks in this redesign. Reading this page does not execute a computation. [Recorded baseline validation](../validation/BASELINE_VALIDATION.json)

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

The integer, mpmath, and Decimal routes remain separate. Their agreement supports the computational result, but shared analytical assumptions still require the written proof. The physical controls check the actual noisy-report calculation; they do not replace the universal entropy bound. [Exact commands, output contracts, and limitations](../docs/REPRODUCTION.md)

## Inspect the outputs before claiming a result

The canonical cover has 512 noise bands and 29,635 input leaves. Evidence records and comparisons are in [the material inventory](materials.md). Ordinary floating-point physical controls use declared tolerances; exact certificates and approved graphical files have stronger identity contracts. Fresh results belong in a new build directory, not on top of reference evidence.

The stored records do not establish external peer review or proof-assistant formalization. No stronger assurance is implied by the reading interface.

To return to the explanation, see [the all-record witness](channel.md#eight-use-witness) and [where the scalar proof enters](proof-guide.md#scalar-proof). The [selected background](background.md) explains the coding quantities; it is not an additional certificate or a software dependency.


---

[Previous: Scope and limits](limits.md) · [Continue: Exact reproduction commands](../docs/REPRODUCTION.md)

GitHub reading view generated from [the website source](../website/pages/verification.md). The equations, figure data and canonical captions retain their source meaning. Custom website navigation, local search and interactive color switching are not executed in this GitHub view.
