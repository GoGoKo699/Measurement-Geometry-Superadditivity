"""Targeted malformed-proof rejection checks. No scientific files are changed.

This is not a full positive replay (handled separately in the main audit).
"""
import argparse
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True


def run(baseline):
    baseline = Path(baseline).resolve()
    sys.path[:0] = [str(baseline/'verification'/name) for name in ('integer','mpmath','decimal')]
    import certify_all_noise as integer
    import cross_backend as mpmath
    import verify_certificate as decimal

    cert = json.loads((baseline/'certificates/common_noise_compact_certificate.json').read_text())
    prev = F(1,2**28)
    leaves = 0
    for b in cert['bands']:
        assert F(b['c_lower']) == prev
        assert prev < F(b['c_upper']) <= F(24,25)
        prev = F(b['c_upper'])
        last = F(1,10**6)
        for l,r in b['intervals']:
            assert F(l) == last < F(r) <= F(1,2)
            last = F(r)
            leaves += 1
        assert last == F(1,2)
    assert prev == F(24,25)
    assert len(cert['bands']) == cert['band_count'] == 512
    assert leaves == cert['leaf_count'] == 29635

    def altered(name):
        c = copy.deepcopy(cert)
        b = c['bands'][0]
        if name == 'changed_polynomial': c['ell'] = 'c'
        elif name == 'changed_domain': c['c_domain'][0] = '1/100000000'
        elif name == 'changed_tail_split': c['t_tail'] = '1/1000'
        elif name == 'empty_noise_cover': c['bands'] = []
        elif name == 'reversed_noise_band': b['c_upper'] = str(F(b['c_lower'])/2)
        elif name == 'noise_gap': b['c_lower'] = str(F(b['c_lower'])*2)
        elif name == 'nan_noise_endpoint': b['c_lower'] = 'NaN'
        elif name == 'empty_input_cover': b['intervals'] = []
        elif name == 'missing_first_input_interval': b['intervals'].pop(0)
        elif name == 'reversed_input_interval': b['intervals'][0].reverse()
        elif name == 'overlapping_input_intervals': b['intervals'].insert(1,b['intervals'][0][:])
        elif name == 'uncertifiable_single_coarse_interval': b['intervals'] = [['1/1000000','1/2']]
        else: raise ValueError(name)
        return c

    names = ('changed_polynomial','changed_domain','changed_tail_split','empty_noise_cover',
             'reversed_noise_band','noise_gap','nan_noise_endpoint','empty_input_cover',
             'missing_first_input_interval','reversed_input_interval','overlapping_input_intervals',
             'uncertifiable_single_coarse_interval')
    records=[]
    for backend, verifier, precision in (
        ('integer',integer.validate,128),('mpmath',mpmath.verify,85),('decimal',decimal.verify,50)
    ):
        for name in names:
            started=time.monotonic()
            try:
                result=verifier(altered(name),precision)
            except Exception as error:
                records.append({'backend':backend,'case':name,'rejected':True,
                                'exception':type(error).__name__,'message':str(error),
                                'seconds':time.monotonic()-started})
            else:
                raise AssertionError((backend,name,'silently accepted',result))
    low_precision=[]
    for digits in (-20,-1,0,1,2,5,10):
        try:
            # Actual reference cover, failures occur in the first band.
            result=mpmath.verify(cert,digits)
        except Exception as error:
            low_precision.append({'digits':digits,'rejected':True,
                                  'exception':type(error).__name__,'message':str(error)})
        else:
            raise AssertionError(('unexpected low-precision acceptance',digits,result))
    return {'passed':True,'positive_full_replay':False,
            'exact_cover':{'bands':len(cert['bands']),'rectangles':leaves,'input':['1/1000000','1/2'],
                           'c':['1/268435456','24/25']},
            'malformed_certificate_rejections':records,'mpmath_low_precision_rejections':low_precision}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline',type=Path,required=True,help='Repository root containing verification/ and certificates/.')
    parser.add_argument('--output',type=Path,required=True,help='New JSON output path; existing files are never overwritten.')
    args=parser.parse_args()
    if args.output.exists():
        parser.error(f'Output already exists: {args.output}')
    result=run(args.baseline)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as output:
        output.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':result['passed'],'exact_cover':result['exact_cover'],
                      'malformed_rejections':len(result['malformed_certificate_rejections']),
                      'low_precision_rejections':len(result['mpmath_low_precision_rejections'])},indent=2))
