"""Independent rational enclosure checks of every plotted Figure 2/3 row.

Uses only Python stdlib and elementary formulas transcribed from the captions.
No repository numerical modules, mpmath, Decimal intervals or rendering records
are imported. All square-root bounds are certified by integer squaring.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse, csv, hashlib, json, re

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--baseline',type=Path,required=True,help='Pinned scientific checkout, read only')
parser.add_argument('--output',type=Path,required=True,help='Audit evidence output directory')
args=parser.parse_args()
ROOT=args.baseline.resolve(); OUT=args.output.resolve(); OUT.mkdir(parents=True,exist_ok=True)
N = 10**120

class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(hi) if hi is not None else F(lo)
        assert self.lo<=self.hi
    def __add__(self,other):
        o=other if isinstance(other,I) else I(other)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __mul__(self,other):
        o=other if isinstance(other,I) else I(other)
        p=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=other if isinstance(other,I) else I(other)
        assert o.lo>0
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,other): return I(other)/self

def sqrt(q):
    q=F(q); assert q>=0
    k=isqrt((q.numerator*N*N)//q.denominator)
    lo=F(k,N); hi=lo if lo*lo==q else F(k+1,N)
    assert lo*lo<=q<=hi*hi
    return I(lo,hi)

def rows(name):
    with (ROOT/'data/figures'/name).open(newline='') as f:return list(csv.DictReader(f))

checks=0; max_plot_error=F(0)
def check(row,name,v):
    global checks,max_plot_error
    # A rational independent interval containing the exact value lies entirely
    # inside the source's outward 60-place enclosure.
    assert F(row[name+'_lower'])<=v.lo<=v.hi<=F(row[name+'_upper']),(name,row)
    p=F(row[name]); error=max(abs(p-v.lo),abs(p-v.hi))
    assert error<=F(1,10**16)*max(abs(v.lo),abs(v.hi),F(1,10**120)),(name,'plot precision')
    max_plot_error=max(max_plot_error,error); checks+=1

f2=rows('figure2_pauli_guaranteed_region.csv')
assert [F(r['epsilon_exact']) for r in f2]==[F(j,2000) for j in range(1001)]
for row in f2:
    e=F(row['epsilon_exact']); a=(1-2*e)**2; c=1-a; d=c*a/35
    s=sqrt(1-a/3); L=I(c)/s
    pc=1/(1+L+d); pr=1/(1+L); width=I(d)/((1+L)*(1+L+d))
    for name,v in [('p_cert',pc),('p_rep',pr),('certified_width',width)]:check(row,name,v)
    assert row['theorem_applies']==str(0<e<F(1,2))
    assert row['upper_p_endpoint_included']=='False'
    assert row['lower_p_endpoint_included']==str(0<e<F(1,2))

f3=rows('figure3_cone_gap.csv')
assert [F(r['lambda_exact']) for r in f3]==[F(j,2000) for j in range(501)]
a=F(16,25); c=F(9,25)
assert c*a/(2*(1+c)**2)==F(18,289)
for row in f3:
    lam=F(row['lambda_exact']); q=1-a*lam; s=sqrt(q)
    p1=I(q/(q+c)); pr=s/(s+c)
    gap=c*a*lam*s/((1+s)*(s+c)*(q+c)); linear=I(F(18,289)*lam)
    for name,v in [('p_one_use',p1),('p_rep',pr),('gap',gap),('linear_asymptote',linear)]:check(row,name,v)
    assert F(row['p_one_use_exact_rational'])==p1.lo
    assert row['all_code_capacity_boundary']=='False'

geom=rows('figure3_cone_geometry.csv')
assert len(geom)==9
for row in geom:
    lam=F(row['lambda_exact']); j=int(row['axis']); r=sqrt(1-lam); z=sqrt(lam)
    xx=r if j==0 else r*F(-1,2)
    yy=I(0) if j==0 else r*sqrt(3)*F(1 if j==1 else -1,2)
    for name,v in [('nx',xx),('ny',yy),('nz',z)]:check(row,name,v)
    assert F(row['weight_exact'])==F(1,3)
    assert F(row['frame_xx_exact'])==F(row['frame_yy_exact'])==(1-lam)/2
    assert F(row['frame_zz_exact'])==lam<=F(row['frame_xx_exact'])

f1=rows('figure1_comparison.csv'); masks=rows('figure1_all_masks_not_for_display.csv')
assert [r['quantity'] for r in f1]==['Q^(1)','I_8/8']
assert F(f1[0]['value_plot'])==0
assert F(f1[1]['lower'])>F(747,10**7)
assert len(masks)==9 and sum(F(r['mask_probability_exact']) for r in masks)==1
assert F(masks[-1]['mask_probability_exact'])==F(7,10)**8
assert F(masks[-1]['upper'])<0
assert F(59,86)<F(7,10)<F(f2[200]['p_cert_lower'])<F(f2[200]['p_rep_lower'])

# Exact structural color comparison checks every byte apart from specified hex
# literal replacement. No geometry/text/opacity/line-pattern edits are allowed.
mapping=json.loads((ROOT/'website/palette.json').read_text())['svg_mapping']
color=[]
for original in sorted((ROOT/'figures/approved').glob('figure_*.svg')):
    old=original.read_text(); new=(ROOT/'reader/assets'/original.name).read_text()
    expected=re.sub(r'#[0-9a-fA-F]{6}\b',lambda m:mapping.get(m[0].lower(),m[0]),old)
    assert new==expected
    color.append(dict(figure=original.name,original_sha256=hashlib.sha256(old.encode()).hexdigest(),display_sha256=hashlib.sha256(new.encode()).hexdigest()))

result=dict(passed=True,method='stdlib rational arithmetic; integer-square-root bounds at 120 decimal places; source modules not imported',
            figure2_rows=len(f2),figure3_rows=len(f3),geometry_rows=len(geom),enclosures_checked=checks,
            max_absolute_plotting_error=float(max_plot_error),
            figure1_scope='metadata, normalization and negative all-measured term only; independent entropy witness audit delegated separately',
            cross_figure_order='59/86 < 0.7 < p_cert(0.1) < p_rep(0.1)',
            cone_slope='18/289',color_only_derivatives=color)
(OUT/'INDEPENDENT_FIGURE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
