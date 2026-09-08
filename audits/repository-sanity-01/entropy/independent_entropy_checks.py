"""Independent stdlib-only diagnostic checks, never imports repository code.

These high-precision point checks supplement the analytical derivations. They
are explicitly not interval proofs of the global inequality.
"""
import argparse
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json, platform, time


def run():
    began = time.monotonic()
    facts = {}
    # Exact arithmetic independently transcribed from the derivations.
    cstar, delta, astar = F(1, 2**28), F(1, 100), F(1, 25)
    ln2_lower = 2*sum((F(1, 3)**(2*j+1)/(2*j+1) for j in range(3)), F(0))
    assert ln2_lower > F(69, 100)
    assert sum((F(5)**k/factorial(k) for k in range(7)), F(0)) > 100
    assert sum((F(2)**k/factorial(k) for k in range(3)), F(0)) > 4
    alpha = (1-F(8,5)*cstar)*(1-delta)-F(3,5)
    tail_margin = alpha*28*F(69,100)-(1-F(8,5)*cstar)*(5*delta+(1+cstar)*delta)-F(3,5)*2
    compact_margin = F(161,100)-F(8,5)/(1-F(8,5)*cstar)
    high_lower = (1-astar)*(2*F(69,100)-1)-astar/4
    high_upper = (F(1,4)+astar/4+astar**2/10)/F(3,4)
    assert alpha > 0 and tail_margin > 0 and compact_margin > 0
    assert high_lower-high_upper == F(99,12500)
    assert F(1,12)+F(7,40)-F(193,840) == F(1,35)
    # Telescoping coefficient identity for f=(1-z)*(-phi'').
    # Drop the common positive factor 1/ln(2).
    for j in range(200):
        current = F(j+1, 2*(2*j+3))
        previous = F(j, 2*(2*j+1))
        assert current-previous == F(1, 2*(2*j+1)*(2*j+3))
    facts['exact_rational_checks'] = {
        'low_tail_margin': str(tail_margin),
        'low_compact_margin': str(compact_margin),
        'high_ratio_lower': str(high_lower),
        'high_required_upper': str(high_upper),
        'high_margin': str(high_lower-high_upper),
        'f_coefficient_identities_checked': 200,
    }

    with localcontext() as ctx:
        ctx.prec = 380
        log2 = D(2).ln()

        def h(t):
            if t in (0, 1):
                return D(0)
            return -(t*t.ln()+(1-t)*(1-t).ln())/log2

        def cost(t, c, x):
            # Conditional reference blocks: trace q and determinant
            # Delta = c*t*(1-t)/4. No repository evaluator is imported.
            eta = (1-c).sqrt()
            trace_offset = eta*(1-2*t)*x.sqrt()
            det = c*t*(1-t)/4
            ans = D(0)
            for sign in (-1, 1):
                q = (1+sign*trace_offset)/2
                # Stable smaller unnormalized eigenvalue.
                eig = 2*det/(q+(q*q-4*det).sqrt())
                ans += q*h(eig/q)
            return ans

        cs = [D(10)**(-k) for k in (100, 60, 30, 12, 8, 3, 1)]
        cs += [D(k)/100 for k in (4, 16, 36, 50, 75, 96)]
        cs += [1-D(10)**(-k) for k in (2, 8, 30, 80)]
        ts = [D(10)**(-k) for k in (100, 50, 12, 7, 6, 3)]
        ts += [D(k)/100 for k in (1, 10, 25, 49, 50)]
        xs = [D(0), D(1)/7, D(1)/3, D(9)/10, D(1)]
        scalar_min = None
        chord_min = None
        pair_error_max = D(0)
        tail_min = None
        count = 0
        for c in cs:
            a = 1-c
            ell = c*(1+a/4+a*a/4+a*a*a/10)
            eps = c/(2*(1+a.sqrt()))
            for t in ts:
                cp = cost(t, c, D(0))
                ca = cost(t, c, D(1))
                ca_alternative = h(t)+h(eps)-h(eps+a.sqrt()*t)
                pair_error_max = max(pair_error_max, abs(ca-ca_alternative))
                scalar = ((1-ell)*cp+(ell-c)*ca-ell*a*h(t))/(c*a*t)
                scalar_min = scalar if scalar_min is None else min(scalar_min, scalar)
                assert scalar > 0
                # P05/P07 common tail bound derived in the audit report.
                if t <= D('0.01'):
                    d = D('0.01')
                    rhs = c*t*((1-d)*(1/c).ln()-d*(1/d).ln()-(1+c)*d)/log2
                    tail = cp-c*h(t)-rhs
                    tail_min = tail if tail_min is None else min(tail_min, tail)
                    assert tail >= 0
                for x in xs:
                    g = c/(1-a*x)
                    chord = (1-g)*cp/a+(g-c)*ca/a
                    v = cost(t,c,x)
                    residual = (v-chord)/h(t)
                    # Endpoints have exact equality, allowing guard precision.
                    assert residual > -D('1e-275')
                    if x not in (0, 1):
                        chord_min = residual if chord_min is None else min(chord_min,residual)
                    count += 1
        facts['point_checks'] = {
            'not_a_global_interval_certificate': True,
            'decimal_digits': ctx.prec,
            'scalar_points': len(cs)*len(ts),
            'directional_points': count,
            'noise_c_extremes': [str(min(cs)),str(max(cs))],
            'smallest_t': str(min(ts)),
            'minimum_scalar_D_over_cat': str(scalar_min),
            'minimum_interior_chord_residual_over_h': str(chord_min),
            'maximum_parallel_formula_discrepancy_bits': str(pair_error_max),
            'minimum_tail_comparison_residual_bits': str(tail_min),
        }
    facts['python'] = platform.python_version()
    facts['duration_seconds'] = time.monotonic()-began
    facts['passed'] = True
    return facts


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='New JSON output path; existing files are never overwritten.')
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f'Output already exists: {args.output}')
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as output:
        output.write(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
