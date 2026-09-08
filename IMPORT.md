# Initial scientific-baseline import

This setup branch has not yet published the scientific baseline to `main`.
It imports exactly `Measurement-Geometry-scientific-baseline-v1-2026-09-08.zip`
with SHA-256:

```
087dbe4b1128a1494abc411415434df2c9a52aa5967053783779a041a32c8944
```

Upload that original ZIP, without extracting or renaming it, to the root of
`setup/scientific-baseline-v1`. The workflow verifies the archive and every
baseline file before it executes any of the imported code. It installs the
pinned dependencies, checks canonical-source and figure hashes, and runs the
complete mathematical and rendering verification. Only after success does it
commit the 166 baseline files to this setup branch and remove the transfer ZIP.

It also accepts a browser-uploaded `Measurement-Geometry-Superadditivity/`
folder or the exact baseline files at repository root. A missing hidden
`.gitignore` is restored from its exact approved bytes. No other missing or
changed file is silently repaired.

The workflow cannot merge this PR, change repository visibility or licensing,
or force-push. It refuses to overwrite a branch that moved during its run.
The 27 approved figure artifacts are checked against their existing hashes;
the independent scientific verifiers are not combined or rewritten.

After the imported tree and workflow evidence are inspected, remove this note,
`.bootstrap/`, and the temporary import workflow before merging. Keep the
read-only `Scientific baseline verification` workflow for the actual project.
No manuscript is part of this import. The old entanglement-response repository
is neither read nor modified.
