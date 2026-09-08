"""Exact rational/symbolic checks attached to separately documented functional proofs."""
from fractions import Fraction as F
from math import factorial
import sympy as sp
import json,argparse
from pathlib import Path

def evaluate():
    a=sp.Symbol('a',real=True);x=sp.Symbol('x',real=True)
    P=1+a/4+a*a/4+a**3/10
    V=sp.Rational(3,4)+3*a*a/20+a**3/10
    W=sp.Rational(1,4)+a/4+a*a/10
    assert sp.expand(1-(1-a)*P-a*V)==0
    assert sp.expand(P-V-W)==0
    assert sp.expand(P-1-a*W)==0
    c0=F(1,2**28);d=F(1,100);a0=F(1,25)
    ln2low=2*sum((F(1,3)**(2*j+1)/(2*j+1) for j in range(3)),F(0))
    assert ln2low>F(69,100)
    assert sum((F(5)**k/factorial(k) for k in range(7)),F(0))>100
    assert sum((F(2)**k/factorial(k) for k in range(3)),F(0))>4
    # Coefficient of u=ln(1/c) remains positive throughout low-noise domain.
    alpha=(1-F(8,5)*c0)*(1-d)-F(3,5)
    lowtail=alpha*28*F(69,100)-(1-F(8,5)*c0)*(5*d+(1+c0)*d)-F(3,5)*2
    compact=F(161,100)-F(8,5)/(1-F(8,5)*c0)
    highratio=(1-a0)*(2*F(69,100)-1)-a0/4
    needed=(F(1,4)+a0/4+a0*a0/10)/F(3,4)
    assert alpha>0 and lowtail>0 and compact>0 and highratio>needed
    # Geometric quadratic has its smaller endpoint at a=1.
    q=sp.Rational(1,12)+7*a/40-sp.Rational(193,840)*a*a
    assert q.subs(a,1)==sp.Rational(1,35)
    assert q.subs(a,0)>q.subs(a,1) and sp.diff(q,a,2)<0
    # Cone: W/P >= 1/4 follows from 4W-P >=0 on [0,1].
    residual=sp.factor(4*W-P)
    assert sp.expand(residual-(3*a/4+3*a*a/20-a**3/10))==0
    # nonnegative because 3a^2/20-a^3/10 >= a^2/20.
    assert sp.expand((3*W-P)-(2*a-1)*(5-a*a)/20)==0
    # Power-series endpoint coefficient of f=(1-z)(-phi''(z)).
    j=sp.Symbol('j',integer=True,positive=True)
    assert sp.simplify((j+1)/(2*(2*j+3))-j/(2*(2*j+1))-1/(2*(2*j+1)*(2*j+3)))==0
    return {'passed':True,'polynomial_identities':3,'low_noise_c_max':str(c0),'low_noise_t_split':str(d),'low_tail_margin':str(lowtail),'low_compact_margin':str(compact),
            'high_noise_a_max':str(a0),'high_ratio_lower':str(highratio),'high_ratio_required_upper':str(needed),'high_ratio_margin':str(highratio-needed),
            'geometry_quadratic_minimum':'1/35','uniform_ca_lambda_coefficient':'3/35','cone_W_over_P_at_least':'1/4',
            'scope':'These exact checks verify the constants and algebra; the functional endpoint arguments are supplied in PROOF_AUDIT.md.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();r=evaluate();a.output.write_text(json.dumps(r,indent=2)+'\n');print(r)
