#!/usr/bin/env python3
"""Build canonical inputs for three specified figures, without drawing them.

Figure 1 is extracted from immutable evidence. Figures 2 and 3 evaluate
published-in-package analytic formulas; no state optimization, new code search,
or full entropy certificate is run. Formula samples use mpmath.iv. Outward
CSV bounds are exactly converted from binary endpoints by Fraction arithmetic.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, platform
from decimal import Decimal, localcontext
from fractions import Fraction as F
from pathlib import Path
from mpmath import mp, iv

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE=ROOT
WITNESS='data/figures/figure1_original_witness140.json'
MODELPATH='docs/MODEL_AND_CLAIMS.md'
PROOFPATH='docs/COMPLETE_PROOF.md'


def sha(b:bytes)->str:return hashlib.sha256(b).hexdigest()

def validate_source(source:Path):
    """Verify direct local canonical inputs; no historical archive extraction."""
    source=Path(source)
    manifest=json.loads((source/'provenance/CANONICAL_INPUTS.json').read_text())
    raw={}
    for name,expected in manifest['files'].items():
        p=source/name
        if not p.is_file() or sha(p.read_bytes())!=expected:
            raise ValueError('Canonical input mismatch: '+name)
        raw[name]=p.read_bytes()
    identity={'root':'baseline','manifest_sha256':sha((source/'provenance/CANONICAL_INPUTS.json').read_bytes()),
        'verified_manifest_entries':len(manifest['files']),
        'selected_members':{name:sha(value) for name,value in raw.items()},
        'source_claims_reaudited':False,'source_files_modified':False,
        'prior_canonical_archive_sha256':'34370f6f9c8f0eb9b8bcef813ac5c915ad12e734474add002cc4c448d9954622'}
    return raw,identity


def exact(x):
    f=F(x);return iv.mpf(f.numerator)/f.denominator

def endpoint_fraction(value):
    sign,man,exp,_=value
    f=F(-man if sign else man)
    return f*2**exp if exp>=0 else f/F(2**(-exp))

def fixed_dec(n:int,places:int):
    sign='-' if n<0 else '';digits=str(abs(n)).zfill(places+1)
    return sign+digits[:-places]+'.'+digits[-places:]

def bounds(v,places=60):
    l,u=(endpoint_fraction(a)*10**places for a in v._mpi_)
    return fixed_dec(l.numerator//l.denominator,places),fixed_dec(-((-u.numerator)//u.denominator),places)

def plot_fraction(f:F):
    with localcontext() as ctx:
        ctx.prec=100
        return format(Decimal(f.numerator)/Decimal(f.denominator),'.17g')

def plot_value(v):
    return plot_fraction((endpoint_fraction(v._mpi_[0])+endpoint_fraction(v._mpi_[1]))/2)

def emit(v,name):
    l,h=bounds(v);return {name:plot_value(v),name+'_lower':l,name+'_upper':h}

def lower(v):return endpoint_fraction(v._mpi_[0])
def upper(v):return endpoint_fraction(v._mpi_[1])

def noise_params(ef:F):
    if not 0<=ef<=F(1,2):raise ValueError('Reporting error outside [0,1/2]')
    a=(1-2*ef)**2;c=1-a;d=F(3,35)*c*a
    return a,c,d

def pauli_slice(ef:F):
    a,c,d=noise_params(ef);lam=F(1,3)
    s=(1-exact(a)/3)**exact(F(1,2))
    L=exact(c)/s
    pR=1/(1+L);pG=1/(1+L+exact(d*lam))
    # Stable expression: no subtraction of nearly coincident frontiers.
    width=exact(d*lam)/((1+L)*(1+L+exact(d*lam)))
    return a,c,d,L,pG,pR,width

def cone_slice(lam:F,ef:F=F(1,10)):
    if not 0<=lam<=F(1,4):raise ValueError('Outside the fixed all-error cone domain')
    if not 0<ef<F(1,2):raise ValueError('Cone figure uses an interior reporting error')
    a,c,d=noise_params(ef);ss=1-a*lam;s=exact(ss)**exact(F(1,2))
    p1f=ss/(ss+c);p1=exact(p1f);pR=s/(s+exact(c))
    width=exact(c*a*lam)*s/((1+s)*(s+exact(c))*(exact(ss)+exact(c)))
    slope=c*a/(2*(1+c)**2);linear=exact(slope*lam)
    return a,c,p1f,p1,pR,width,slope,linear

def save_csv(path:Path,rows:list[dict]):
    if not rows:raise ValueError('No rows')
    with path.open('w',newline='',encoding='utf-8')as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def interval_record(v):
    l,u=bounds(v);return {'lower':l,'upper':u,'plot_value':plot_value(v)}

def build(out:Path,source:Path=DEFAULT_SOURCE):
    mp.dps=110;iv.dps=85
    raw,integrity=validate_source(source)
    out.mkdir(parents=True,exist_ok=True)
    w=json.loads(raw[WITNESS])
    if (w['n'],F(w['p']),F(w['epsilon']),w['postselection'])!=(8,F(7,10),F(1,10),False):
        raise ValueError('Unexpected witness record')
    records=w['all_mask_terms']
    if [r['measured']for r in records]!=list(range(9)):raise ValueError('Incomplete witness branches')
    if F(w['per_use_rate']['lower'])<=0:raise ValueError('Witness is not positive')
    if F(w['one_use_threshold'])!=F(59,86):raise ValueError('Unexpected one-use threshold')
    if F(w['one_use_ic_over_input_entropy_upper']['upper'])>=0:raise ValueError('No one-use exclusion')
    comparison=[dict(object='optimized_single_use',plot_label='Best one-use input',value_plot='0',
            lower='0',upper='0',quantity='Q^(1)',status='exact_global_optimum_from_canonical_proof',
            source='MODEL_AND_CLAIMS.md#m05; COMPLETE_PROOF.md#p13',unit='bits of coherent information per physical channel use'),
        dict(object='balanced_eight_use',plot_label='Eight-use construction / 8',
             value_plot=plot_fraction((F(w['per_use_rate']['lower'])+F(w['per_use_rate']['upper']))/2),
             lower=w['per_use_rate']['lower'],upper=w['per_use_rate']['upper'],quantity='I_8/8',
             status='stored_certified_construction_value_not_globally_optimized_block_value',
             source='canonical source W1; COMPLETE_PROOF.md#p13',unit='bits of coherent information per physical channel use')]
    save_csv(out/'figure1_comparison.csv',comparison)
    probability_sum=F(0);lo_sum=hi_sum=F(0);masks=[]
    for r in records:
        m=r['measured'];pl,pu=map(F,[r['mask_probability']['lower'],r['mask_probability']['upper']])
        true=F(math.comb(8,m))*F(7,10)**m*F(3,10)**(8-m)
        if not pl==true==pu:raise ValueError('Mask probability differs from exact binomial value')
        probability_sum+=true;lo,hi=map(F,[r['weighted_contribution_bits']['lower'],r['weighted_contribution_bits']['upper']])
        lo_sum+=lo;hi_sum+=hi
        masks.append(dict(measured=m,mask_probability_exact=str(true),mask_probability_plot=plot_fraction(true),
          block_contribution_plot=plot_fraction((lo+hi)/2),lower=str(r['weighted_contribution_bits']['lower']),
          upper=str(r['weighted_contribution_bits']['upper']),included_in_main_rate=True,display_in_main_figure=False,
          all_measured=(m==8),unit='bits per eight-use block, not divided by eight'))
    if probability_sum!=1 or masks[-1]['lower'][0]!='-':raise ValueError('Probability/sign control failed')
    tl,tu=map(F,[w['block_coherent_information_bits']['lower'],w['block_coherent_information_bits']['upper']])
    if not (lo_sum<=tu and tl<=hi_sum):raise ValueError('Mask sum does not overlap total block enclosure')
    rateL,rateU=map(F,[w['per_use_rate']['lower'],w['per_use_rate']['upper']])
    if not (tl/8<=rateU and rateL<=tu/8):raise ValueError('Per-use normalization failed')
    save_csv(out/'figure1_all_masks_not_for_display.csv',masks)
    (out/'figure1_original_witness140.json').write_bytes(raw[WITNESS])

    f2=[]
    for j in range(1001):
        e=F(j,2000);a,c,d,L,pG,pR,width=pauli_slice(e)
        endpoint=e in (0,F(1,2))
        if not endpoint and lower(width)<=0:raise ValueError('Nonpositive interior strip')
        if endpoint and not (lower(width)==upper(width)==0):raise ValueError('Endpoint not zero')
        f2.append(dict(epsilon_exact=str(e),epsilon=plot_fraction(e),a_exact=str(a),c_exact=str(c),
          lambda_min_exact='1/3',loss_L=plot_value(L),**emit(pG,'p_cert'),**emit(pR,'p_rep'),**emit(width,'certified_width'),
          theorem_applies=not endpoint,endpoint_kind='perfect_record_limit' if e==0 else 'uninformative_record_limit' if e==F(1,2) else 'interior',
          lower_p_endpoint_included=not endpoint,upper_p_endpoint_included=False,
          ensemble='equally_weighted_Pauli_axes',exact_capacity_boundary=False))
    save_csv(out/'figure2_pauli_guaranteed_region.csv',f2)
    _,_,_,_,wpg,wpr,_=pauli_slice(F(1,10))
    if not F(7,10)<lower(wpg):raise ValueError('Expected finite witness outside conservative strip')
    context={'epsilon':'1/10','p_witness':'7/10','p_single_use_exact':'59/86',
       'p_cert_from_uniform_3_over_35_bound':interval_record(wpg),'p_rep':interval_record(wpr),
       'witness_below_conservative_lower_boundary':True,
       'instruction':'Do not place the Figure 1 point inside the Figure 2 certified strip. Do not overlay it by default. Its proof uses the sharper canonical P13 bound.',
       'no_exact_Q1_threshold_curve_plotted_over_all_epsilon':True}
    (out/'cross_figure_witness_bound_check.json').write_text(json.dumps(context,indent=2)+'\n')

    f3=[];slope=None
    for j in range(501):
        lam=F(j,2000);a,c,p1f,p1,pR,gap,slope,linear=cone_slice(lam)
        if lam and lower(gap)<=0:raise ValueError('Cone gap not positive')
        f3.append(dict(lambda_exact=str(lam),lambda_min=plot_fraction(lam),epsilon_exact='1/10',
         p_one_use_exact_rational=str(p1f),**emit(p1,'p_one_use'),**emit(pR,'p_rep'),**emit(gap,'gap'),
         asymptote_slope_exact=str(slope),**emit(linear,'linear_asymptote'),
         exact_one_use_domain='0 <= lambda <= 1/4; canonical P12',
         geometry='equal_weight_three_axis_cone',full_span=bool(lam),
         all_code_capacity_boundary=False))
    save_csv(out/'figure3_cone_gap.csv',f3)
    geometries=[]
    for lam in (F(0),F(1,16),F(1,4)):
        radial=exact(1-lam)**exact(F(1,2));z=exact(lam)**exact(F(1,2));s3=exact(3)**exact(F(1,2))
        for j,(xx,yy) in enumerate([(radial,exact(0)),(-radial/2,radial*s3/2),(-radial/2,-radial*s3/2)]):
            geometries.append(dict(lambda_exact=str(lam),axis=j,weight_exact='1/3',
                **emit(xx,'nx'),**emit(yy,'ny'),**emit(z,'nz'),
                opposite_axis_endpoint='negative_of_all_three_components',
                frame_xx_exact=str((1-lam)/2),frame_yy_exact=str((1-lam)/2),frame_zz_exact=str(lam),
                frame_off_diagonal_exact='0',code_direction='(0,0,1); guide only, not a fourth measurement axis',
                mode='coplanar' if not lam else 'full_span'))
    save_csv(out/'figure3_cone_geometry.csv',geometries)
    limit=[]
    for k in range(1,13):
        lam=F(1,10**k);a,c,p1f,p1,pR,gap,slope,linear=cone_slice(lam)
        ratio=gap/exact(lam)
        limit.append(dict(lambda_exact=str(lam),gap_per_lambda=plot_value(ratio),
                asymptotic_coefficient_exact=str(slope),relative_excess_over_limit=plot_value(ratio/exact(slope)-1),
                purpose='implementation control; not additional displayed curves or a fitted exponent'))
    save_csv(out/'figure3_small_lambda_controls_not_for_display.csv',limit)
    if slope!=F(18,289):raise ValueError('Wrong fixed-epsilon cone slope')
    panel_counts={'figure1_comparison':len(comparison),'figure1_masks':len(masks),'figure2_noise_grid':len(f2),'figure3_lambda_grid':len(f3),'figure3_geometry_axes':len(geometries),'figure3_limit_checks':len(limit)}
    summary={'schema_version':1,'date':'2026-09-08','source':integrity,'rows':panel_counts,
        'figure1':'unchanged certificate copied and transformed; not re-evaluated from a physical simulation',
        'figure2_3':'new evaluations of canonical analytic formulas with 85-digit mpmath intervals and exact outward 60-place decimal serialization',
        'plot_decimal_digits':17,'precision_is_not_statistical_confidence':True,
        'new_theorem_or_global_certificate_audit':False,'new_code_search':False,
        'figure2_lower_boundary_name':'p_cert := 1/(1+L+d_epsilon lambda), new display-only shorthand',
        'figure3_display_error':'1/10; no other error curves',
        'figures_rendered':False,'repository_changes':False}
    (out/'BUILD_RECORD.json').write_text(json.dumps(summary,indent=2)+'\n')
    (out/'SOURCE_IDENTITY.json').write_text(json.dumps(integrity,indent=2)+'\n')
    print(json.dumps(panel_counts,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'build/data/figures');p.add_argument('--baseline',type=Path,default=DEFAULT_SOURCE)
    args=p.parse_args();build(args.output,args.baseline)
