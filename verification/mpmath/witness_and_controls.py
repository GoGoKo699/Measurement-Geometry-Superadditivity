#!/usr/bin/env python3
"""Run only the retained example and two declared controls.

The effect-determinant computation is kept separate from the Decimal posterior
calculation. It is inherited mathematics with a new baseline-only entry point.
"""
from pathlib import Path
from fractions import Fraction
import argparse,json
import witness_formula as w


def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 a.output.mkdir(parents=True,exist_ok=False)
 rate,terms=w.block(8,'7/10','1/10')
 assert w.lo(rate)>0
 gamma=w.q('27/59');p0=w.q('7/10')
 exclusion=(1-p0)-p0*gamma
 assert w.hi(exclusion)<0
 result={'n':8,'p':'7/10','epsilon':'1/10','per_use_rate':w.record(rate),'all_mask_terms':terms,'one_use_entropy_coefficient_upper':w.record(exclusion),'passed':True,'backend':'mpmath unnormalized effect determinants','precision_digits':w.iv.dps}
 (a.output/'witness.json').write_text(json.dumps(result,indent=2)+'\n')
 neg,_=w.block(64,'5083/10000','2/5');assert w.hi(neg)<0
 rejected={'n':64,'p':'5083/10000','epsilon':'2/5','certified_rate':w.record(neg),'interpretation':'Negative; not used as a positive witness.'}
 (a.output/'rejected_float_candidate.json').write_text(json.dumps(rejected,indent=2)+'\n')
 val=1-w.q('11/19')-w.q('11/19')*w.h(w.q('1/5'));assert w.lo(val)>0
 mixed={'error':'1/5','p':'11/19','input':'maximally mixed','coherent_information':w.record(val),'conclusion':'At the nearly-pure zero line g=8/11 the true one-use optimum is still positive.'}
 (a.output/'mixed_input_control.json').write_text(json.dumps(mixed,indent=2)+'\n')
 print('Retained witness and both declared negative/mixed-input controls verified.')

if __name__=='__main__':main()
