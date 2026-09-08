"""Recheck complete noise/input rectangles using mpmath.iv, not integer engine.

Uses the entropy-difference formula for C1 rather than posterior entropy.
All domain endpoints are exact rational values; proof comparisons use bounds.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import argparse,json,time
from mpmath import mp,iv

CLOW=F(1,2**28);CHIGH=F(24,25);DELTA=F(1,10**6)
def q(x):
    x=F(x);return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def low(x):return mp.mpf(x._mpi_[0])
def high(x):return mp.mpf(x._mpi_[1])
def lowerpoint(x):return iv.mpf(x.a)
def upperpoint(x):return iv.mpf(x.b)
def h(x):return -(x*iv.log(x)+(1-x)*iv.log(1-x))/iv.log(2)
def pvw(c):
    a=1-c
    return 1+a/4+a*a/4+a**3/10, q('3/4')+q('3/20')*a*a+a**3/10,q('1/4')+a/4+a*a/10
@lru_cache(maxsize=200000)
def costs(t,c):
    t=q(t);c=q(c);eta=iv.sqrt(1-c);e=c/(2*(1+eta))
    # Direct eigenvalue subtraction is safe at this precision/domain.
    eig=(1-iv.sqrt(1-4*c*t*(1-t)))/2
    return h(eig)/c,h(t)+h(e)-h(e+eta*t)
def slower(t,cl,ch):
    _,v,w=pvw(q(ch));return v*costs(t,ch)[0]+w*costs(t,cl)[1]
def tail(cl,ch):
    c=iv.mpf([q(cl).a,q(ch).b]);a=1-c;eta=iv.sqrt(a);e=c/(2*(1+eta));p,_,_=pvw(c);dt=q(DELTA)
    return (1-c*p)*((1-dt)*iv.log(1/c)-dt*iv.log(1/dt)-(1+c)*dt)-(p-1)*eta*iv.log((1-e)/e)
def verify(c,dps):
    mp.dps=dps+30;iv.dps=dps;costs.cache_clear();start=time.time()
    if c['c_domain']!=[str(CLOW),str(CHIGH)] or c['t_tail']!=str(DELTA) or c['ell']!='c*(1+a/4+a^2/4+a^3/10), a=1-c':raise ValueError('params')
    previous=CLOW;maxu=mp.ninf;mint=mp.inf;leaves=0
    for i,b in enumerate(c['bands']):
        cl,ch=F(b['c_lower']),F(b['c_upper'])
        if cl!=previous or not cl<ch<=CHIGH:raise ValueError('noise cover')
        tm=tail(cl,ch)
        if low(tm)<=0:raise AssertionError('tail')
        mint=min(mint,low(tm));previous=ch;tprev=DELTA;cache={};pmax=upperpoint(pvw(q(cl))[0])
        for ls,rs in b['intervals']:
            l,r=F(ls),F(rs)
            if l!=tprev or not l<r<=F(1,2):raise ValueError('input cover')
            m=q((l+r)/2);hm=h(m);der=iv.log((1-m)/m)/iv.log(2)
            for t in (l,r):
                if t not in cache:cache[t]=lowerpoint(slower(t,cl,ch))
                v=pmax*(hm+der*(q(t)-m))-cache[t]
                if high(v)>=0:raise AssertionError((i,l,r,'leaf'))
                maxu=max(maxu,high(v))
            tprev=r;leaves+=1
        if tprev!=F(1,2):raise ValueError('incomplete input cover')
        if (i+1)%100==0:print('cross verify',i+1,'seconds',round(time.time()-start,1),flush=True)
    if previous!=CHIGH:raise ValueError('incomplete noise cover')
    return {'passed':True,'backend':'mpmath.iv with entropy-difference C1','digits':dps,'bands':len(c['bands']),'leaves':leaves,'maximum_upper':mp.nstr(maxu,70),'minimum_tail_lower':mp.nstr(mint,70)}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--digits',type=int,default=85);args=ap.parse_args()
    res=verify(json.loads(args.certificate.read_text()),args.digits);args.output.write_text(json.dumps(res,indent=2)+'\n');print(res)
