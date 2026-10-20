# Contributing

This repository documents a bounded channel-theory result, its proof, independent numerical checks and three scientific figures. Start with [the overview](README.md), [supporting materials](reader/materials.md) and [the model and claim boundaries](docs/MODEL_AND_CLAIMS.md). A proposed extension should be discussed separately from a correction to an existing claim.

## Report a problem

Give the commit, exact file or equation, expected behavior and the smallest reproducible example. For a scientific concern, state the affected claim and provide a derivation, counterexample or primary-source comparison. A failed command should include its arguments, return code, software versions and relevant output. Distinguish a blocked environment from a mathematical failure. A passing test suite alone does not establish a theorem.

Do not post live credentials, tokens or other sensitive information in an issue or pull request. A private security-reporting channel has not been established by this document. The maintainer must establish an appropriate private route before requesting sensitive details.

## Make a focused change

Use a branch and pull request. Keep proposed repairs separate from the findings they address, and explain what changed, why and how it was checked.

<a id="scientific-source-ownership"></a>
### Scientific source ownership

The complete reader-facing argument is organized by topic under `science/`. Its 23 model/proof units are generated from the protected scientific editing sources in `docs/`, with one topic owner per unit. The generator changes relative Markdown links and preserves the scientific text, TeX, equation labels and numerical literals. The [source-to-topic map](website/furnishing-map.json) records the exact correspondence. Keep canonical mathematics and captions in their existing source files.

Edit topic introductions and the section allocation in `website/furnishing.json`, then run `python website/furnish.py --write`. Generally useful learning material is maintained in `learning/README.md` and `learning/milestones.md`; retain exactly 30 project-defined milestones and the settled Preskill v5 anchor. The detailed source bridge is generated from `website/pages/background.md` and the protected `website/learning_bridge.json`.

The illustrated introduction and optional HTML edition retain their editorial sources in `website/pages/`. Generate `reader/` from those sources rather than editing its outputs. The topic edition also carries the complete channel introduction and proof-strategy explanation from those sources. See [the website and edition guide](WEBSITE.md).

Treat canonical equations, numerical inputs, reference evidence, certificates, independent verification implementations and approved figure bytes as protected scientific artifacts. Do not replace expected results, relax tolerances, refresh scientific approval hashes or merge independent evaluators to obtain a pass. A necessary scientific change needs an explicit review plan and supporting evidence. The accepted palette applies only to figures; older approved exports remain preserved.

## Check the affected work

Use an isolated environment with the recorded dependencies and fresh output directories. Do not use Python `-O`, because inherited checkers use assertions.

For reader changes, follow [WEBSITE.md](WEBSITE.md), including generation before consistency checks:

```bash
python website/repository_preview.py --write
python website/repository_preview.py --check
python website/furnish.py --write
python website/furnish.py --check
python verify.py
python -m pytest -q -p no:cacheprovider tests website/tests
```

The website guide also gives HTML and loopback browser checks. [REPRODUCTION.md](docs/REPRODUCTION.md) distinguishes integrity checks, figure reproduction, witness evaluation and complete certificate verification. Select checks that address the change; documentation work does not itself require another full certificate run. Report skipped or blocked checks explicitly.

## Reuse and contribution terms

Original code is licensed under MIT; original prose, figures and data are licensed under CC BY 4.0 where the relevant rights exist. [LICENSE.md](LICENSE.md) defines the scope and third-party exceptions. Identify third-party material and its source before proposing its inclusion, and state that you have authority to submit your contribution under the applicable repository terms. This guide introduces no contributor agreement or copyright assignment.
