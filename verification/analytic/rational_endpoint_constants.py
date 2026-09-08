"""Rational checks of the analytic noise-endpoint and geometry constants."""
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path

def run():
    c0=F(1,2**28);dt=F(1,100);a0=F(1,25)
    log2_lower=2*sum((F(1,3)**(2*j+1)/F(2*j+1) for j in range(3)),F(0))
    assert log2_lower>F(69,100)
    assert sum((F(5)**k/factorial(k) for k in range(7)),F(0))>100
    assert sum((F(2)**k/factorial(k) for k in range(3)),F(0))>4
    alpha=(1-F(8,5)*c0)*(1-dt)-F(3,5)
    assert alpha>0
    low_tail=alpha*28*F(69,100)-(1-F(8,5)*c0)*(5*dt+(1+c0)*dt)-F(3,5)*2
    low_compact=F(161,100)-F(8,5)/(1-F(8,5)*c0)
    high_lower=(1-a0)*(2*F(69,100)-1)-a0/4
    high_required=(F(1,4)+a0/4+a0*a0/10)/F(3,4)
    assert low_tail>0 and low_compact>0 and high_lower>high_required
    # q(a)=1/12+7a/40-193a^2/840 is concave on [0,1].
    q0=F(1,12);q1=F(1,12)+F(7,40)-F(193,840)
    assert q1==F(1,35) and q0>q1
    return {'passed':True,'low_c_upper':str(c0),'low_noise_input_split':str(dt),
        'low_noise_tail_margin_lower':str(low_tail),'low_noise_compact_margin_lower':str(low_compact),
        'high_noise_a_upper':str(a0),'high_noise_ratio_lower':str(high_lower),'high_noise_required_ratio_upper':str(high_required),
        'high_noise_margin':str(high_lower-high_required),'geometry_quadratic_minimum':str(q1),
        'global_gap_coefficient_in_ca_lambda':'3/35','remarks':'Exact rational inequalities. Functional arguments are supplied in THEORY.md.'}
if __name__=='__main__':
    r=run();p=Path(__file__).resolve().parents[1]/'results/analytic_endpoint_constants.json';p.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
