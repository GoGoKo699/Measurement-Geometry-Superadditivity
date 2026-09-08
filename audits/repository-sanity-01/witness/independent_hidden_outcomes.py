#!/usr/bin/env python3
"""Audit-only eight-use calculation from projective hidden outcomes.

This script imports no repository module.  It enumerates all six-label count
classes, retaining their complex logical coherences, and obtains entropy from
the eigenvalues of raw subnormalised 2x2 matrices.  Arbitrary-precision mpmath
values are precision checks, not directed-rounding interval certificates.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path
import platform
import resource
import sys
import time

import mpmath as mp


def compositions(n, slots):
    if slots == 1:
        yield (n,)
    else:
        for first in range(n + 1):
            for rest in compositions(n - first, slots - 1):
                yield (first,) + rest


def run(dps):
    mp.mp.dps = dps
    started = time.monotonic()
    one = mp.mpf(1)
    eps = one / 10
    p = 7 * one / 10
    n = 8
    tol = mp.mpf(10) ** (-(dps - 15))
    sqrt2 = mp.sqrt(2)
    coshalf = mp.sqrt((1 + one / mp.sqrt(3)) / 2)
    sinhalf = mp.sqrt((1 - one / mp.sqrt(3)) / 2)
    phase = (1 + 1j) / sqrt2
    codewords = (
        (coshalf, phase * sinhalf),
        (-mp.conj(phase) * sinhalf, coshalf),
    )
    # Each pair lists the actual + and - projective eigenvectors.
    axes = (
        ((one / sqrt2, one / sqrt2), (one / sqrt2, -one / sqrt2)),
        ((one / sqrt2, 1j / sqrt2), (one / sqrt2, -1j / sqrt2)),
        ((one, mp.mpf(0)), (mp.mpf(0), one)),
    )

    def inner(v, w):
        return sum(mp.conj(x) * y for x, y in zip(v, w))

    for k in range(2):
        for l in range(2):
            assert abs(inner(codewords[k], codewords[l]) - (k == l)) < tol

    # Logical reference matrix for a reported axis/sign.  Both hidden true
    # outcomes are summed at this point; they are never available to receiver.
    records = []
    for axis in axes:
        for reported in range(2):
            matrix = [[mp.mpc(0) for _ in range(2)] for _ in range(2)]
            for hidden in range(2):
                weight = ((1 - eps) if reported == hidden else eps) / 3
                amplitude = [inner(axis[hidden], psi) for psi in codewords]
                for k in range(2):
                    for l in range(2):
                        matrix[k][l] += weight * amplitude[k] * mp.conj(amplitude[l])
            records.append(matrix)

    for k in range(2):
        for l in range(2):
            assert abs(sum(e[k][l] for e in records) - (k == l)) < tol

    def entropy_eigenvalues(vals):
        q = sum(vals)
        assert q > 0
        assert all(v >= -tol for v in vals)
        # The sole rank-one case is m=0, handled analytically below.
        assert all(v > 0 for v in vals)
        return -sum(v * mp.log(v / q, 2) for v in vals)

    def weighted_joint_entropy(a, b, z):
        q = a + b
        determinant = a * b - abs(z) ** 2
        assert determinant > 0
        discriminant = (a - b) ** 2 + 4 * abs(z) ** 2
        top = (q + mp.sqrt(discriminant)) / 2
        # Quotient avoids catastrophic subtraction for the small eigenvalue.
        bottom = determinant / top
        return entropy_eigenvalues((top, bottom))

    terms = []
    raw_probability_defects = []
    phase_nontrivial_records = 0
    for m in range(n + 1):
        a_entropy = mp.mpf(0)
        c_entropy = mp.mpf(0)
        probability = mp.mpf(0)
        diagonal0 = mp.mpf(0)
        diagonal1 = mp.mpf(0)
        offdiagonal = mp.mpc(0)
        represented_sequences = 0
        classes = 0
        for counts in compositions(m, 6):
            multiplicity = math.factorial(m)
            for count in counts:
                multiplicity //= math.factorial(count)
            represented_sequences += multiplicity
            classes += 1
            qmatrix = [[mp.mpc(one / 2) for _ in range(2)] for _ in range(2)]
            for count, record in zip(counts, records):
                for k in range(2):
                    for l in range(2):
                        qmatrix[k][l] *= record[k][l] ** count
            aa, bb = mp.re(qmatrix[0][0]), mp.re(qmatrix[1][1])
            zz = qmatrix[0][1]
            assert abs(qmatrix[1][0] - mp.conj(zz)) < tol
            assert abs(mp.im(qmatrix[0][0])) + abs(mp.im(qmatrix[1][1])) < tol
            if abs(mp.im(zz)) > tol:
                phase_nontrivial_records += 1
            probability += multiplicity * (aa + bb)
            diagonal0 += multiplicity * aa
            diagonal1 += multiplicity * bb
            offdiagonal += multiplicity * zz
            a_entropy += multiplicity * entropy_eigenvalues((aa, bb))
            if m:
                c_entropy += multiplicity * weighted_joint_entropy(aa, bb, zz)
        assert represented_sequences == 6 ** m
        assert classes == math.comb(m + 5, 5)
        assert abs(probability - 1) < tol
        assert abs(diagonal0 - one / 2) < tol
        assert abs(diagonal1 - one / 2) < tol
        assert abs(offdiagonal - (one / 2 if m == 0 else 0)) < tol
        mask_probability = math.comb(n, m) * p ** m * (1 - p) ** (n - m)
        branch_ic = a_entropy - c_entropy if m < n else -c_entropy
        weighted_ic = mask_probability * branch_ic
        raw_probability_defects.append(abs(probability - 1))
        terms.append({
            "measured": m,
            "six_label_classes": classes,
            "represented_report_sequences": represented_sequences,
            "record_probability_sum": mp.nstr(probability, dps),
            "A_m_bits": mp.nstr(a_entropy, dps),
            "C_m_bits": mp.nstr(c_entropy, dps),
            "mask_probability": mp.nstr(mask_probability, dps),
            "conditional_ic_bits": mp.nstr(branch_ic, dps),
            "weighted_contribution_bits": mp.nstr(weighted_ic, dps),
        })
    result = sum(mp.mpf(t["weighted_contribution_bits"]) for t in terms)
    assert abs(sum(mp.mpf(t["mask_probability"]) for t in terms) - 1) < tol
    assert result > 0
    assert mp.mpf(terms[-1]["weighted_contribution_bits"]) < 0
    return {
        "decimal_precision": dps,
        "duration_seconds": time.monotonic() - started,
        "arithmetic": "mpmath arbitrary precision, nearest arithmetic, NOT rigorous intervals",
        "block_coherent_information_bits": mp.nstr(result, dps),
        "per_use_rate": mp.nstr(result / n, dps),
        "max_record_normalization_defect": mp.nstr(max(raw_probability_defects), 8),
        "complex_phase_classes_count": phase_nontrivial_records,
        "all_mask_terms": terms,
    }


def exact_thresholds():
    a, c = Fraction(16, 25), Fraction(9, 25)
    P = 1 + a / 4 + a * a / 4 + a ** 3 / 10
    ell = c * P
    gamma = c / (1 - a / 3)
    ratio_bound = Fraction(3, 10) - Fraction(7, 10) * gamma
    assert gamma == Fraction(27, 59)
    assert ratio_bound == -Fraction(6, 295)
    assert ell > gamma
    mp.mp.dps = 140
    loss = mp.mpf(c.numerator) / c.denominator / mp.sqrt(1 - mp.mpf(a.numerator) / a.denominator / 3)
    gap = Fraction(3, 35) * c * a / 3
    return {
        "Gamma_given_global_entropy_comparison": str(gamma),
        "P": str(P), "ell": str(ell), "ell_minus_Gamma": str(ell - gamma),
        "one_use_threshold": str(1 / (1 + gamma)),
        "Ic_over_Srho_upper_at_witness": str(ratio_bound),
        "L": mp.nstr(loss, 90),
        "uniform_additive_gap": str(gap),
        "uniform_lower_p": mp.nstr(1 / (1 + loss + mp.mpf(gap.numerator) / gap.denominator), 90),
        "repetition_frontier": mp.nstr(1 / (1 + loss), 90),
        "global_proof_dependency": "P3/P4 entropy comparison must hold for every input t and direction; this numerical witness alone does not prove global Q1=0",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert sys.flags.optimize == 0, "Run without Python -O"
    assert not args.output.exists(), "Fresh output required"
    result = {
        "utc_start": datetime.now(timezone.utc).isoformat(),
        "python": sys.version, "executable": sys.executable,
        "platform": platform.platform(), "mpmath_version": mp.__version__,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "command": sys.argv,
        "baseline_expected_commit": "f0015c56a19fd953c6797b2c64d9b507105234e3",
        "thresholds": exact_thresholds(),
        "calculations": [run(70), run(130)],
    }
    mp.mp.dps = 140
    lo, hi = result["calculations"]
    result["precision_difference_bits"] = str(abs(mp.mpf(lo["block_coherent_information_bits"]) - mp.mpf(hi["block_coherent_information_bits"])))
    assert mp.mpf(result["precision_difference_bits"]) < mp.mpf("1e-65")
    # Compare only after completing the independent calculation.
    reference_path = args.baseline / "evidence/reference/witness100.json"
    reference = json.loads(reference_path.read_text())
    comparison = []
    pairs = [
        ("block", hi["block_coherent_information_bits"], reference["block_coherent_information_bits"]),
        ("rate", hi["per_use_rate"], reference["per_use_rate"]),
    ]
    pairs += [
        (f"m={t['measured']}", t["weighted_contribution_bits"], r["weighted_contribution_bits"])
        for t, r in zip(hi["all_mask_terms"], reference["all_mask_terms"])
    ]
    for label, computed, interval in pairs:
        inside = mp.mpf(interval["lower"]) <= mp.mpf(computed) <= mp.mpf(interval["upper"])
        if interval["lower"] == interval["upper"]:
            # An ordinary rounded value cannot be required to lie in a
            # zero-width exact rational interval.  Independently prove this
            # unique contribution using rational arithmetic instead.
            assert label == "m=0"
            exact = Fraction(3, 10) ** 8
            assert exact == Fraction(interval["lower"])
            assert abs(mp.mpf(computed) - mp.mpf(interval["lower"])) < mp.mpf("1e-125")
            comparison.append({"quantity": label, "exact_rational_reference_verified": True,
                               "nearest_arithmetic_inside_zero_width_interval": inside})
        else:
            assert inside, label
            comparison.append({"quantity": label, "inside_stored_100_digit_enclosure": inside})
    result["stored_reference_comparison"] = comparison
    result["reference_sha256"] = sha256(reference_path.read_bytes()).hexdigest()
    result["peak_rss_kib_linux"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "passed": True,
        "block_bits": hi["block_coherent_information_bits"][:62],
        "rate": hi["per_use_rate"][:63],
        "all_measured_contribution": hi["all_mask_terms"][-1]["weighted_contribution_bits"][:65],
        "precision_difference": result["precision_difference_bits"],
        "runtime_seconds": [r["duration_seconds"] for r in result["calculations"]],
        "reference_quantities_checked": len(comparison),
    }, indent=2))


if __name__ == "__main__":
    main()
