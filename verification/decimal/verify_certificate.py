"""New complete-domain recheck, with a different interval engine and envelope.

Reuses only the submitted RATIONAL partition, not stored claimed bounds.
Maximizes the secant majorant via binary-entropy convex conjugacy, rather than
the submitted midpoint-tangent envelope. Modelled channel parameters are fixed
by this code, not trusted from the proof object's numerical claims.
"""
import argparse,json,time
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
from decimal import Decimal
import decimal_interval as ar
from decimal_interval import Interval as I,h,log2

CL=F(1,2**28);CH=F(24,25);DT=F(1,10**6)

def coeff(c):
    a=1-I(c)
    return 1+a/4+a*a/4+a**3/10, I('3/4')+I('3/20')*a*a+a**3/10, I('1/4')+a/4+a*a/10

@lru_cache(maxsize=200000)
def costs(t,c):
    t=I(t);c=I(c);a=1-c
    # Stable small eigenvalue of a trace-one two-by-two matrix, det=c*t*(1-t).
    d=c*t*(1-t)
    small=2*d/(1+(1-4*d).sqrt())
    epsilon=c/(2*(1+a.sqrt()))
    # Joint classical entropy minus the correctly mixed reported-bit entropy.
    parallel=h(t)+h(epsilon)-h(epsilon+a.sqrt()*t)
    return h(small)/c,parallel

def lower_at(t,cl,ch):
    _,v,w=coeff(ch)
    return (v*costs(t,ch)[0]+w*costs(t,cl)[1]).lower()

def tail(cl,ch):
    c=I.hull(cl,ch);eta=(1-c).sqrt();e=c/(2*(1+eta));p,_,_=coeff(c);d=I(DT)
    return (1-c*p)*((1-d)*(1/c).ln()-d*(1/d).ln()-(1+c)*d)-(p-1)*eta*((1-e)/e).ln()

def maximum_upper(l,r,left,right,p):
    slope=(right-left)/I(r-l)
    # concave P*h(t)-secant(t), derivative P log2((1-t)/t)-slope
    dl=p*((1-I(l))/I(l)).ln()/log2()-slope
    dr=p*((1-I(r))/I(r)).ln()/log2()-slope
    if dl.hi<=0:return (p*h(I(l))-left).hi
    if dr.lo>=0:return (p*h(I(r))-right).hi
    # The unconstrained maximum over [0,1] is a safe upper bound.
    legendre=p*(1+(-slope*log2()/p).exp()).ln()/log2()
    return (legendre-left+slope*I(l)).hi

def verify(cert,precision):
    ar.set_precision(precision);costs.cache_clear()
    if cert.get('ell')!='c*(1+a/4+a^2/4+a^3/10), a=1-c' or cert.get('c_domain')!=[str(CL),str(CH)] or cert.get('t_tail')!=str(DT):raise ValueError('Wrong claim parameters')
    if cert.get('claim')!='(1-ell)*C0+(ell-c)*C1 >= ell*(1-c)*h(t)':raise ValueError('Wrong claimed inequality')
    prev=CL;worst=Decimal('-Infinity');mint=Decimal('Infinity');count=0;t0=time.monotonic()
    for i,band in enumerate(cert['bands']):
        cl,ch=F(band['c_lower']),F(band['c_upper'])
        if cl!=prev or not cl<ch<=CH:raise ValueError('Noise partition is not exact')
        tm=tail(cl,ch)
        if tm.lo<=0:raise ArithmeticError(('Input tail',i,tm.record()))
        mint=min(mint,tm.lo)
        p=coeff(cl)[0].upper();cache={};last=DT
        for ls,rs in band['intervals']:
            l,r=F(ls),F(rs)
            if l!=last or not l<r<=F(1,2):raise ValueError('Input partition is not exact')
            for t in (l,r):
                if t not in cache:cache[t]=lower_at(t,cl,ch)
            up=maximum_upper(l,r,cache[l],cache[r],p)
            if up>=0:raise ArithmeticError(('Leaf',i,ls,rs,str(up)))
            worst=max(worst,up);last=r;count+=1
        if last!=F(1,2):raise ValueError('Incomplete input partition')
        prev=ch
        if (i+1)%64==0:print(f'checked {i+1} bands, {count} rectangles, {time.monotonic()-t0:.1f}s',flush=True)
    if prev!=CH:raise ValueError('Incomplete noise domain')
    if cert.get('band_count')!=len(cert['bands']) or cert.get('leaf_count')!=count:raise ValueError('Incorrect declared counts')
    return {'passed':True,'method':'independently written Decimal intervals and entropy-conjugate secant maximum','precision':precision,'bands':len(cert['bands']),'rectangles':count,'largest_compact_upper':str(worst),'smallest_tail_lower_nats':str(mint),'domain':[str(CL),str(CH)],'input_tail':str(DT),'imports_submitted_numerical_code':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--precision',type=int,default=90);a=ap.parse_args()
    result=verify(json.loads(a.certificate.read_text()),a.precision);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n');print(result)
