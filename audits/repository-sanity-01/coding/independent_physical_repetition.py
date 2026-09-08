"""Bounded audit crosscheck: explicitly sum hidden projective outcomes.

No baseline modules are imported. This is floating-point corroboration of the
physical reduction, not a rigorous entropy certificate or global optimization.
Run with an ordinary (not -O) Python containing numpy, from any directory.
All masks, reported labels and hidden true signs are enumerated for n <= 3.
"""
from __future__ import annotations

import itertools
import json
import math
import platform
import sys
import time
from pathlib import Path

import numpy as np

TOL = 4e-12
PAULI = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])


def h(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -(x * math.log2(x) + (1.0 - x) * math.log2(1.0 - x))


def eig_entropy(matrix):
    eigen = np.linalg.eigvalsh(matrix)
    assert eigen.min(initial=0.0) > -TOL
    # A direct Hermitian eigensolver produces O(eps) signs for rank-deficient
    # zero eigenvalues. Only negative values in the asserted tolerance clip.
    return -sum(v * math.log2(v) for v in eigen if v > 0.0)


def kron_all(matrices):
    product = np.array([[1.0]], dtype=complex)
    for matrix in matrices:
        product = np.kron(product, matrix)
    return product


def state_pair(axis):
    eigen, vec = np.linalg.eigh(np.einsum('i,ijk->jk', axis, PAULI))
    assert abs(eigen[0] + 1) < TOL and abs(eigen[1] - 1) < TOL
    return vec[:, 1], vec[:, 0]


def run_case(name, axes, weights, direction, epsilon, p, n):
    axes = np.asarray(axes, dtype=float)
    axes /= np.linalg.norm(axes, axis=1)[:, None]
    direction = np.asarray(direction, dtype=float)
    direction /= np.linalg.norm(direction)
    weights = np.asarray(weights, dtype=float)
    assert abs(weights.sum() - 1.0) < TOL
    assert min(weights) > 0 and 0 <= epsilon <= 0.5 and 0 <= p <= 1
    eta = 1 - 2 * epsilon
    projection = axes @ direction
    sb = np.sqrt(1 - eta**2 * projection**2)
    kb = eta**2 * (1 - projection**2) / sb**2
    kb[np.abs(kb) < 1e-15] = 0.0
    assert min(kb) >= 0 and max(kb) <= 1 + TOL
    B, K = float(weights @ sb), float(weights @ (sb * kb))
    plus, minus = state_pair(direction)
    psi = (np.kron([1, 0], kron_all([plus[:, None]] * n).ravel())
           + np.kron([0, 1], kron_all([minus[:, None]] * n).ravel())) / math.sqrt(2)
    measurement_states = [state_pair(axis) for axis in axes]
    total_physical = total_reduced = total_trace = 0.0
    max_branch_difference = 0.0
    negative_all_measured = 0.0
    branches = 0
    hidden_terms = 0
    by_m = [{"physical": 0.0, "reduced": 0.0, "probability": 0.0} for _ in range(n + 1)]
    for mask in itertools.product([False, True], repeat=n):
        measured = [k for k, flag in enumerate(mask) if flag]
        m = len(measured)
        survivors = n - m
        mask_probability = p**m * (1-p)**survivors
        for record in itertools.product(range(2 * len(axes)), repeat=m):
            labels = [(label // 2, label % 2) for label in record]
            rb = np.zeros((2**(survivors+1), 2**(survivors+1)), complex)
            for hidden in itertools.product([0, 1], repeat=m):
                local = [np.eye(2)] * n
                likelihood = 1.0
                for k, (b, reported), true in zip(measured, labels, hidden):
                    local[k] = measurement_states[b][true].conj()[None, :]
                    likelihood *= weights[b] * (1-epsilon if reported == true else epsilon)
                projected = np.kron(np.eye(2), kron_all(local)) @ psi
                rb += likelihood * np.outer(projected, projected.conj())
                hidden_terms += 1
            # True outcomes and acquisition errors have been summed into rb;
            # they are never retained as receiver output labels.
            rb_tensor = rb.reshape(2, 2**survivors, 2, 2**survivors)
            receiver = np.trace(rb_tensor, axis1=0, axis2=2)
            physical = eig_entropy(receiver) - eig_entropy(rb)
            probability = float(np.trace(rb).real)
            pplus = pminus = chi = 1.0
            for b, reported in labels:
                pplus *= weights[b] * (1 + (-1)**reported * eta * projection[b]) / 2
                pminus *= weights[b] * (1 - (-1)**reported * eta * projection[b]) / 2
                chi *= kb[b]
            q = (pplus + pminus) / 2
            assert abs(q - probability) < TOL
            if q == 0:
                reduced = 0.0
            else:
                x = pminus / (pplus + pminus)
                root = math.sqrt(max(0.0, 1 - 4*(1-chi)*x*(1-x)))
                joint_entropy = h((1-root)/2)
                reduced = q * ((h(x) if survivors else 0.0) - joint_entropy)
            max_branch_difference = max(max_branch_difference, abs(physical-reduced))
            total_physical += mask_probability * physical
            total_reduced += mask_probability * reduced
            total_trace += mask_probability * probability
            by_m[m]["physical"] += mask_probability * physical
            by_m[m]["reduced"] += mask_probability * reduced
            by_m[m]["probability"] += mask_probability * probability
            if m == n:
                negative_all_measured += mask_probability * physical
            branches += 1
    assert abs(total_trace - 1) < TOL
    assert abs(total_physical - total_reduced) < TOL
    assert max_branch_difference < TOL
    assert negative_all_measured <= TOL
    # The zero-information-record endpoint has a transparent independent
    # prediction for balanced repetition: only no erasure/all erasure survive.
    endpoint_expected = None
    if epsilon == 0.5:
        endpoint_expected = (1-p)**n - p**n
        assert abs(total_physical - endpoint_expected) < TOL
    if epsilon == 0:
        assert abs(negative_all_measured) < TOL
    lower = upper = None
    if 0 < epsilon < 0.5:
        lr = sum(math.log((1+abs(eta*x))/(1-abs(eta*x))) for x in projection)
        xstar = 1/(1+math.exp(lr))
        ca, cr = h(xstar), 2/math.log(2)*xstar*(1-xstar)
        lower = cr/(n+1)**len(axes)*(1-p+p*K)**n - (p*B)**n
        upper = (1-p+p*K)**n - ca/(n+1)**len(axes)*(p*B)**n
        assert lower - TOL <= total_physical <= upper + TOL
    return dict(name=name, n=n, epsilon=epsilon, p=p, axes=axes.tolist(),
                weights=weights.tolist(), direction=direction.tolist(),
                branches=branches, hidden_terms=hidden_terms,
                trace=total_trace, physical=total_physical, reduced=total_reduced,
                max_branch_abs_difference=max_branch_difference,
                all_measured_contribution=negative_all_measured,
                all_measured_probability=by_m[n]['probability'],
                overlap_B=B, coherence_overlap_K=K,
                lower_envelope=lower, upper_envelope=upper,
                endpoint_expected=endpoint_expected, by_measured_count=by_m)


def main():
    start = time.monotonic()
    axes = [[1, 0, 0], [1, 2, 0], [1, -1, 2]]
    cases = [run_case('unequal_noncoplanar', axes, [.2, .3, .5], [2, -1, 3], .13, .7, n)
             for n in [1, 2, 3]]
    cases += [run_case('axis_aligned_kappa_zero', axes, [.2, .3, .5], [1, 0, 0], .13, .7, 3),
              run_case('perfect_reports', axes, [.2, .3, .5], [2, -1, 3], 0.0, .7, 2),
              run_case('uninformative_reports', axes, [.2, .3, .5], [2, -1, 3], .5, .7, 3),
              run_case('coplanar_perpendicular', [[1, 0, 0], [1, 2, 0]], [.4, .6], [0, 0, 1], .13, .7, 3)]
    output = dict(python=sys.version, numpy=np.__version__, platform=platform.platform(),
                  assertions_enabled=__debug__, tolerance=TOL,
                  arithmetic='IEEE double eigensolver; corroboration, not a rigorous enclosure',
                  elapsed_seconds=time.monotonic()-start, cases=cases)
    assert __debug__, 'Run without Python -O'
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    serialized = json.dumps(output, indent=2) + '\n'
    if target:
        with target.open('x') as f:
            f.write(serialized)
    else:
        print(serialized, end='')


if __name__ == '__main__':
    main()
