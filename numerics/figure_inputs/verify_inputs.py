#!/usr/bin/env python3
"""Verify the figure data contract, not the underlying all-noise theorem.

Uses exact rational checks, independent high-precision Decimal evaluation of
algebraically different curve formulas, domain checks and source identity.
"""
from __future__ import annotations
import argparse,csv,json,hashlib
from decimal import Decimal as D,localcontext
from fractions import Fraction as F
from pathlib import Path
from build_inputs import ROOT,DEFAULT_SOURCE,validate_source,WITNESS


def read_csv(p):
    with p.open(newline='')as f:return list(csv.DictReader(f))
def dec(q):
    q=F(q);return D(q.numerator)/D(q.denominator)
def in_enclosure(value,row,name):
    if not D(row[name+'_lower'])<=value<=D(row[name+'_upper']):
        raise AssertionError((name,row.get('epsilon_exact',row.get('lambda_exact')),str(value)))

def verify(data:Path,source:Path=DEFAULT_SOURCE):
    raw,identity=validate_source(source)
    witness=json.loads(raw[WITNESS]);copied=(data/'figure1_original_witness140.json').read_bytes()
    assert copied==raw[WITNESS]
    bar=read_csv(data/'figure1_comparison.csv');masks=read_csv(data/'figure1_all_masks_not_for_display.csv')
    assert len(bar)==2 and len(masks)==9
    assert F(bar[0]['lower'])==F(bar[0]['upper'])==0
    assert bar[1]['lower']==witness['per_use_rate']['lower']
    assert bar[1]['upper']==witness['per_use_rate']['upper']
    assert F(bar[1]['lower'])>F(747,10**7)
    assert sum((F(x['mask_probability_exact'])for x in masks),F(0))==1
    assert F(masks[-1]['upper'])<0
    assert [int(x['measured'])for x in masks]==list(range(9))
    x2=read_csv(data/'figure2_pauli_guaranteed_region.csv');x3=read_csv(data/'figure3_cone_gap.csv')
    assert len(x2)==1001 and len(x3)==501
    # Two ordinary high-precision backends are intentionally not described as
    # independent external audit. Directed intervals were written by builder.
    counts={}
    for precision in (100,130):
        with localcontext()as ctx:
            ctx.prec=precision
            previous=None
            for j,row in enumerate(x2):
                ef=F(row['epsilon_exact']);assert ef==F(j,2000)
                e=dec(ef);a=(1-2*e)**2;c=1-a
                s=(1-a/3).sqrt();L=c/s;d=3*c*a/35
                # Different algebraic presentation from the generator.
                pr=s/(s+c);pg=s/(s+c+d*s/3)
                width=pr-pg
                for v,name in [(pg,'p_cert'),(pr,'p_rep'),(width,'certified_width')]:in_enclosure(v,row,name)
                endpoint=j in (0,1000)
                assert (row['theorem_applies']=='True')== (not endpoint)
                assert (row['lower_p_endpoint_included']=='True')== (not endpoint)
                assert row['upper_p_endpoint_included']=='False'
                assert row['exact_capacity_boundary']=='False'
                assert width>0 if not endpoint else width==0
                if previous is not None:assert pr<previous
                previous=pr
                assert D(row['certified_width'])<D('.004')
            assert D(x2[0]['p_rep'])==1 and D(x2[-1]['p_rep'])==D('.5')
            e=D('.1');a=(1-2*e)**2;c=1-a;slope=c*a/(2*(1+c)**2)
            previous=0
            for j,row in enumerate(x3):
                lf=F(row['lambda_exact']);assert lf==F(j,2000) and lf<=F(1,4)
                l=dec(lf);s=(1-a*l).sqrt();p1=(1-a*l)/(1-a*l+c);pr=1/(1+c/s)
                gap=pr-p1;linear=slope*l
                for v,name in [(p1,'p_one_use'),(pr,'p_rep'),(gap,'gap'),(linear,'linear_asymptote')]:in_enclosure(v,row,name)
                exact_p1=(1-F(16,25)*lf)/(1-F(16,25)*lf+F(9,25))
                assert F(row['p_one_use_exact_rational'])==exact_p1
                assert F(row['asymptote_slope_exact'])==F(18,289)
                assert (row['full_span']=='True')==bool(lf)
                if j:assert gap>previous
                previous=gap
            assert F(x3[-1]['p_one_use_exact_rational'])==F(7,10)
        counts[str(precision)]={'figure2_formula_rows':len(x2),'figure3_formula_rows':len(x3),'passed':True}
    geometry=read_csv(data/'figure3_cone_geometry.csv');assert len(geometry)==9
    for row in geometry:
        lf=F(row['lambda_exact']);assert lf in (F(0),F(1,16),F(1,4))
        assert 2*F(row['frame_xx_exact'])+F(row['frame_zz_exact'])==1
        assert F(row['frame_zz_exact'])==lf
        assert float(row['nx'])**2+float(row['ny'])**2+float(row['nz'])**2>1-1e-14
        assert float(row['nx'])**2+float(row['ny'])**2+float(row['nz'])**2<1+1e-14
    for lf in ('0','1/16','1/4'):
        cols=[r for r in geometry if r['lambda_exact']==lf]
        a=[[float(r[k])for k in ('nx','ny','nz')] for r in cols]
        T=[[sum(v[i]*v[j]/3 for v in a)for j in range(3)]for i in range(3)]
        f=float(F(lf));target=[(1-f)/2,(1-f)/2,f]
        for i in range(3):
            for j in range(3):assert abs(T[i][j]-(target[i]if i==j else 0))<1e-14
    controls=read_csv(data/'figure3_small_lambda_controls_not_for_display.csv');assert len(controls)==12
    deviations=[abs(D(r['relative_excess_over_limit']))for r in controls]
    assert all(deviations[j+1]<deviations[j]for j in range(len(deviations)-1))
    assert deviations[-1]<D('1e-11')
    c=json.loads((data/'cross_figure_witness_bound_check.json').read_text())
    assert F(c['p_single_use_exact'])<F(c['p_witness'])
    assert F(c['p_witness'])<F(c['p_cert_from_uniform_3_over_35_bound']['lower'])
    assert F(c['p_witness'])<F(c['p_rep']['lower'])
    return {'passed':True,'canonical_input_manifest_sha256':identity['manifest_sha256'],'source_manifest_entries':identity['verified_manifest_entries'],
       'witness_copied_byte_for_byte':True,'witness_recomputed':False,'all_nine_mask_terms_retained':True,
       'independent_scalar_formula_checks':counts,'cone_axes_checked':len(geometry),'asymptotic_formula_controls':len(controls),
       'witness_outside_conservative_figure2_strip_explicitly_checked':True,
       'curve_values_have_outward_mpmath_interval_records':True,
       'alternative_scalar_checks':'Decimal ordinary high-precision point evaluations of equivalent expressions; not a new global interval certificate',
       'proof_reaudit':False,'physical_simulation':False,'figures_rendered':False,'repository_access':False}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data',type=Path,default=ROOT/'data/figures');p.add_argument('--baseline',type=Path,default=DEFAULT_SOURCE);p.add_argument('--report',type=Path,default=ROOT/'build/INPUT_VALIDATION.json');args=p.parse_args()
    result=verify(args.data,args.baseline);args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
