"""Algebraic regressions for the linear threshold-closure corollary.

These checks verify scalar identities and the exact cone specialization in
COMPLETE_PROOF P08/P12. They do not establish the general entropy theorem,
rerun its certificate, or optimize a channel or code. The cone checks stay in
the all-error validity range 0 <= lambda <= 1/4.
"""
from __future__ import annotations

import mpmath as mp
import pytest
import sympy as sp


def test_scalar_chords_and_reciprocal_difference_slacks():
    # q = sqrt(c), s = sqrt(1-a*x), so 0 < q <= s <= 1 and a=1-q**2.
    # Every displayed factor in these slacks is nonnegative on that domain.
    q, s = sp.symbols("q s", positive=True)
    x = (1 - s**2) / (1 - q**2)
    g, h = q**2 / s**2, q**2 / s
    slacks = (
        (
            q**2 + (1 - q**2) * x - g,
            (1 - s**2) * (s - q) * (s + q) / s**2,
        ),
        (
            q**2 + (q - q**2) * x - h,
            q * (1 - s) * (s - q) * (s + q + 1) / ((1 + q) * s),
        ),
        (
            (h - q**2) / q - (g - h),
            q * (1 - s) * (s - q) / s**2,
        ),
    )
    for difference, factored_slack in slacks:
        assert sp.cancel(difference - factored_slack) == 0

    # The third relation can be evaluated at a minimizer of Lambda. The
    # second chord is then evaluated in a minimum-eigenvalue direction of T;
    # no coincidence of the G and Lambda minimizers is assumed.
    lam = sp.symbols("lambda", nonnegative=True)
    assert sp.cancel(((q - q**2) * lam) / q - (1 - q) * lam) == 0


@pytest.mark.parametrize("power", [sp.Rational(1, 2), sp.Integer(1)])
def test_scalar_costs_are_increasing_and_convex(power):
    a, c = sp.symbols("a c", positive=True)
    x = sp.symbols("x", real=True)
    cost = c / (1 - a * x) ** power
    first = c * power * a / (1 - a * x) ** (power + 1)
    second = c * power * (power + 1) * a**2 / (1 - a * x) ** (power + 2)
    assert sp.simplify(sp.diff(cost, x) - first) == 0
    assert sp.simplify(sp.diff(cost, x, 2) - second) == 0
    # The derivative numerators and denominators are positive for
    # a,c>0 and 1-a*x>0, including the stated common-noise domain.
    assert power > 0


def test_threshold_identity_and_denominator_slacks():
    gamma, loss, c, upper = sp.symbols("Gamma L c U", positive=True)
    denominator = (1 + loss) * (1 + gamma)
    assert sp.cancel(
        1 / (1 + loss) - 1 / (1 + gamma) - (gamma - loss) / denominator
    ) == 0
    # c <= L <= Gamma <= U makes both factored slacks nonnegative.
    assert sp.expand(
        denominator - (1 + c) ** 2
        - ((loss - c) * (1 + gamma) + (gamma - c) * (1 + c))
    ) == 0
    assert sp.expand(
        (1 + upper) ** 2 - denominator
        - ((upper - loss) * (1 + upper) + (upper - gamma) * (1 + loss))
    ) == 0


def test_exact_cone_gap_and_linear_coefficient():
    a, c = sp.symbols("a c", positive=True)
    lam = sp.symbols("lambda", real=True)
    s = sp.sqrt(1 - a * lam)
    gamma, loss = c / s**2, c / s
    stable_cost_gap = c * a * lam / (s**2 * (1 + s))
    stable_threshold_gap = c * a * lam * s / ((1 + s) * (s + c) * (s**2 + c))
    threshold_gap = 1 / (1 + loss) - 1 / (1 + gamma)
    assert sp.simplify(gamma - loss - stable_cost_gap) == 0
    assert sp.simplify(threshold_gap - stable_threshold_gap) == 0
    assert sp.simplify(
        sp.diff(threshold_gap, lam).subs(lam, 0) - c * a / (2 * (1 + c) ** 2)
    ) == 0


@pytest.mark.parametrize("epsilon_text", [
    "1e-20", "0.1", "0.3", "0.49999999999999999999",
])
@pytest.mark.parametrize("lambda_text", ["0", "1e-30", "0.25"])
def test_exact_cone_obeys_cost_and_threshold_bounds(epsilon_text, lambda_text):
    with mp.workdps(140):
        epsilon, lam = mp.mpf(epsilon_text), mp.mpf(lambda_text)
        a = (1 - 2 * epsilon) ** 2
        # Equivalent stable expression for 1-a close to the perfect-record end.
        c = 4 * epsilon * (1 - epsilon)
        q, s = mp.sqrt(c), mp.sqrt(1 - a * lam)
        gamma, loss = c / s**2, c / s
        d, upper = 3 * c * a / 35, c + a * lam
        coefficient_upper = a / (1 + q)  # Stable form of 1-sqrt(c).
        denominator = (1 + loss) * (1 + gamma)
        cost_gap = c * a * lam / (s**2 * (1 + s))
        threshold_gap = c * a * lam * s / ((1 + s) * (s + c) * (s**2 + c))
        p_one = (1 - a * lam) / (1 - a * lam + c)
        p_rep = s / (s + c)

        assert 0 < epsilon < mp.mpf("0.5")
        assert 0 <= lam <= mp.mpf("0.25")
        assert c <= loss <= gamma <= upper
        assert d * lam <= cost_gap <= coefficient_upper * lam
        assert (1 + c) ** 2 <= denominator <= (1 + upper) ** 2
        assert d * lam / (1 + upper) ** 2 <= threshold_gap
        assert threshold_gap <= coefficient_upper * lam / (1 + c) ** 2

        if not lam:
            assert gamma == loss == c
            assert cost_gap == threshold_gap == 0
            assert p_one == p_rep == 1 / (1 + c)
            return

        relative = mp.mpf("1e-60")
        assert mp.almosteq(cost_gap, gamma - loss, rel_eps=relative, abs_eps=0)
        assert mp.almosteq(threshold_gap, p_rep - p_one, rel_eps=relative, abs_eps=0)
        assert mp.almosteq(
            threshold_gap, cost_gap / denominator, rel_eps=relative, abs_eps=0
        )
        if lam == mp.mpf("1e-30"):
            leading_coefficient = c * a / (2 * (1 + c) ** 2)
            assert abs(threshold_gap / (lam * leading_coefficient) - 1) < mp.mpf("1e-28")
