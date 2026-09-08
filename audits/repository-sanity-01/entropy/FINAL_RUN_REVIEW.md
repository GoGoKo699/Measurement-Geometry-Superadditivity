# Independent review of the completed full reproduction

Pinned scientific source: `f0015c56a19fd953c6797b2c64d9b507105234e3`.
Reviewed fresh output: `baseline/build/audit-full/` in the separate audit
workspace. The parent audit reports return code 0 for
`python reproduce.py --output build/audit-full --full --rebuild-certificate`.
This review read the resulting numerical files and stage logs, inspected
`reproduce.py` and the witness/control entry point, and independently compared
the nine declared reference pairs and rebuilt covering bytes. No heavy test
or numerical pipeline was rerun for this review.

The full run closes the positive-execution condition left explicit in the
earlier entropy report. All three complete compact-domain verifiers executed
and passed. Their bounds have already been independently inspected
mathematically in `REPORT.md`; this conclusion is not inferred from the wrapper
name or an old result file.

## Complete certificate results

All three checkers covered 512 noise bands and 29,635 input rectangles, with
`c` spanning `[1/268435456,24/25]`, input rectangles spanning `[1/1000000,1/2]`,
and a positive analytical lower-tail margin in every band. Values in the table
are abbreviated displays; the JSON files preserve the exact output endpoints.

| Executed implementation | Working precision | Largest compact upper bound | Smallest tail lower bound |
|---|---:|---:|---:|
| Integer/dyadic, midpoint tangent | 224 bits | `-5.7196236614297157e-12` | `0.00028189136168575773` |
| mpmath interval, entropy-difference parallel cost | 85 decimal digits | `-5.7196236614297157e-12` | `0.00028189136168575773` |
| Directed Decimal, entropy-conjugate secant maximum | 130 decimal digits | `-2.3735563521529992e-10` | `0.00028189136168575773` |

The different Decimal compact bound is expected from its different valid
upper envelope. These bounds certify signs on entire rectangles and tails;
they are not statistical confidence intervals or sampled minima. The tail
margin is a normalized entropy-proof expression in nats, not a coding rate.

The 128-bit construction stage regenerated the full rational covering from
scratch. Its log ends with `FINAL 512 29635 deterministic covering complete`.
The reconstructed file is independently confirmed byte-identical to
`certificates/common_noise_compact_certificate.json`, with SHA-256
`ab500804e56ba8c5ffb1ca7c1f38e3fd720b01561122b3a2bcc367a106ad66dd`.

Files reviewed: `certificate/integer/verification_224.json`,
`certificate/mpmath85.json`, `certificate/decimal130.json`, the rebuilt
certificate, and the four corresponding logs. Their fresh progress logs and
the `subprocess.run(...,check=True)` control flow confirm actual generation
and complete verification stages, rather than cached-result assertions.

## Analytical constants, witness, and retained controls

Both analytical routes executed. Their exact arithmetic agrees on the
low-noise tail margin
`706479660745902522393/112589990684262400000`, compact-input margin
`167771999/16777215900`, high-noise ratio gap `99/12500`, geometric polynomial
minimum `1/35`, and universal coefficient `3/35`. The symbolic route also
checks the coefficient identities and cone-domain relations. These arithmetic
checks supplement the functional derivations reviewed in `REPORT.md`.

The retained eight-use example was recalculated by Decimal at 100 and 140
digits and by the separate mpmath effect-determinant evaluator at 125 digits.
Each calculation includes all nine measured-count cases. They establish

`I_8/8 = 0.000074774765881559637101656367261778724371... > 7.47e-5`.

The rigorous Decimal140 interval is contained both in the Decimal100 interval
and in the outward-rounded independent mpmath interval; this nesting was
independently checked with exact `Fraction` comparisons. The global one-use
coefficient remains `-6/295`, approximately `-0.02033898305084746`, with the
all-input justification supplied by the independently reviewed scalar lemma.

The all-measured event has probability exactly `0.05764801` and contributes
approximately `-0.01653160578648965` bits to the block total. It is present and
negative, so the reported positive rate does not omit this loss.

The mpmath control entry point explicitly recalculates and asserts both
retained control signs:

- At `epsilon=1/5`, `p=11/19`, the maximally mixed one-use input has coherent
  information approximately `0.0030942608546849565 > 0`. This continues to
  reject a general identification of the nearly pure limit with the global
  optimum.
- At `n=64`, `epsilon=2/5`, `p=5083/10000`, the rejected candidate has per-use
  coherent information approximately `-8.0128545500827895e-23 < 0`.

No historical additional positive witness is required or claimed by this
retained-scope run.

## Actual stage coverage and comparison strength

`reproduce.py`, lines 61–76, sequentially executes certificate reconstruction,
all three complete verifiers, both Decimal witness precisions, the independent
witness and two controls, both analytical routes, and the physical check.
The corresponding fresh logs and outputs are all present. The internal
scientific test stage reports `52 passed in 2.35s`; it does not include website
tests, which belong to the parent audit's separate interface checks.

| Evidence class | Observed comparison | Meaning |
|---|---|---|
| Nine files in `full_reference_comparison.json` | Every file byte-identical; independently rechecked | Exact byte reproduction of recorded output, including all three certificate results, both Decimal witness files, symbolic constants, both controls, and physical diagnostic |
| Rebuilt rational certificate | Byte-identical; independently rechecked | Same complete rational proof object reconstructed |
| Independent mpmath versus Decimal witness | Rigorous interval nesting | Mathematically compatible deterministic enclosures, not expected byte identity between different evaluators |
| Regenerated plotting data | 10 files byte-identical | Same numerical plotting inputs and provenance records |
| Regenerated approved figures | 27 artifacts byte-identical | Exact rendering reproduction in this environment; visual/scientific figure review remains separate |
| Small physical reduction | Five cases, 455 reported records, 2,561 hidden-outcome terms; maximum discrepancy `1.4259426972529354e-15` | Floating-point agreement, well below the prescribed `2e-12` tolerance; not an exact interval proof |

The physical output also happened to reproduce its reference bytes exactly.
That fact does not change the character of its numerical method: it remains
an ordinary floating-point physical diagnostic. Its largest full matrix is
dimension 128, and it correctly records that no full eight-use output matrix
was constructed.

Two potentially confusing status fields have scoped meanings, not failures:
`data_validation.json` says its plotting stage copied the retained witness
instead of recalculating it; the separate full witness stages demonstrably
recalculate it. `REPRODUCTION_RESULT.json` records `external_audit:false`, a
fixed description of what the repository's reproduction command itself does;
it is not evidence against the independent audit now reviewing that command.

## Final disposition for this subaudit

No unexpected numerical behavior, skipped complete verifier, unsupported
tolerance relaxation, or substantive discrepancy was found in the completed
run. The compact scalar lemma now has both an independently inspected valid
proof envelope and successful fresh full-domain executions. Together with the
analytical endpoints and complete-input reasoning already reviewed, this
establishes the entropy/global-single-use component at the pinned baseline.
No additional bounded scientific task is needed for this component.
