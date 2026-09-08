"""Complete compact-domain certificate for a new common-noise entropy chord.

Reuses the explicitly archived integer interval engine. New bounds and
cover are independent of previous ell=0.065 certificates. No floats in proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,argparse
import dyadic_interval as di
from dyadic_interval import Box as I

CLOW=F(1,2**28); CHIGH=F(24,25); DELTA=F(1,10**6)

def pvw(c):
    a=1-I(c)
    P=1+a/4+a*a/4+a**3/10
    V=F(3,4)+F(3,20)*a*a+a**3/10
    W=F(1,4)+a/4+a*a/10
    return P,V,W

@lru_cache(maxsize=200000)
def costs(t,c):
    t=I(t); c=I(c); eta=(1-c).sqrt();e=c/(2*(1+eta))
    y=c*t*(1-t); small=2*y/(1+(1-4*y).sqrt())
    c0=di.entropy(small)/c
    q0=(1-e)*(1-t)+e*t;q1=e*(1-t)+(1-e)*t
    c1=q0*di.entropy(e*t/q0)+q1*di.entropy((1-e)*t/q1)
    return c0,c1

@lru_cache(maxsize=100000)
def ht(t): return di.entropy(I(t))

def lower_S(t,cl,ch):
    _,V,W=pvw(ch)
    # C0(c)/c decreases with c, C1(c) increases; P,V,W decrease with c.
    c0,_=costs(t,ch);_,c1=costs(t,cl)
    return V*c0+W*c1

def tail_margin(cl,ch):
    c=I.hull(cl,ch);a=1-c;eta=a.sqrt();e=c/(2*(1+eta))
    P,_,_=pvw(c);ell=c*P;dt=I(DELTA)
    return (1-ell)*((1-dt)*(1/c).log()-dt*(1/dt).log()-(1+c)*dt) - (P-1)*eta*((1-e)/e).log()

def upper_leaf(l,r,cl,ch,cache):
    for t in (l,r):
        if t not in cache:cache[t]=lower_S(t,cl,ch).lower_point()
    pmax=pvw(cl)[0].upper_point();m=I((l+r)/2)
    h=di.entropy(m);der=((1-m)/m).log()/di.ln2()
    ul=pmax*(h+der*(I(l)-m))-cache[l]
    ur=pmax*(h+der*(I(r)-m))-cache[r]
    return max(ul.hi,ur.hi)

PROBES=[DELTA,F(1,100000),F(1,10000),F(1,1000),F(1,100),F(1,20),F(1,10),F(1,5),F(3,10),F(2,5),F(1,2)]

def attempt_band(cl,ch):
    margin=tail_margin(cl,ch)
    if margin.lo<=0:return None
    cache={};pmax=pvw(cl)[0].upper_point()
    for t in PROBES:
        val=lower_S(t,cl,ch);cache[t]=val.lower_point()
        if (pmax*ht(t)-val).hi>=0:return None
    stack=[(DELTA,F(1,2))];out=[];maxub=None;cnt=0
    while stack:
        l,r=stack.pop();u=upper_leaf(l,r,cl,ch,cache);cnt+=1
        if u<0:
            out.append((l,r)); maxub=u if maxub is None else max(maxub,u)
        else:
            mid=(l+r)/2
            if (pmax*ht(mid)-lower_S(mid,cl,ch)).hi>=0:return None
            stack.extend([(mid,r),(l,mid)])
        if cnt>1000:return None
    out.sort()
    return {'c_lower':str(cl),'c_upper':str(ch),'tail_lower_numerator':str(margin.lo),'max_upper_numerator':str(maxub),
        'intervals':[[str(l),str(r)] for l,r in out]}

def construct(bits=160):
    di.set_precision(bits);costs.cache_clear();ht.cache_clear()
    bands=[];lo=CLOW
    while 2*lo<CHIGH:
        bands.append((lo,2*lo));lo*=2
    bands.append((lo,CHIGH));stack=list(reversed(bands));good=[];attempts=0;t0=time.time()
    while stack:
        l,r=stack.pop(); v=attempt_band(l,r); attempts+=1
        if v is not None:good.append(v)
        else:
            mid=(l+r)/2;stack.extend([(mid,r),(l,mid)])
        if attempts%50==0:print('attempts',attempts,'accepted',len(good),'pending',len(stack),'c',float(l),'seconds',round(time.time()-t0,1),flush=True)
        if attempts>10000:raise RuntimeError('limit')
    good.sort(key=lambda v:F(v['c_lower']))
    return {'claim':'(1-ell)*C0+(ell-c)*C1 >= ell*(1-c)*h(t)',
        'ell':'c*(1+a/4+a^2/4+a^3/10), a=1-c', 'bits':bits,'t_tail':str(DELTA),
        'c_domain':[str(CLOW),str(CHIGH)],'bands':good,'band_count':len(good),
        'leaf_count':sum(len(v['intervals']) for v in good),'attempts':attempts}

def validate(cert,bits):
    if cert['ell']!='c*(1+a/4+a^2/4+a^3/10), a=1-c' or cert['c_domain']!=[str(CLOW),str(CHIGH)] or cert['t_tail']!=str(DELTA):raise ValueError('parameters')
    di.set_precision(bits);costs.cache_clear();ht.cache_clear()
    prev=CLOW;worst=None;tailworst=None;leaves=0;t0=time.time()
    for ix,band in enumerate(cert['bands']):
        cl,ch=F(band['c_lower']),F(band['c_upper'])
        if cl!=prev or not cl<ch<=CHIGH:raise ValueError('noise cover')
        margin=tail_margin(cl,ch)
        if margin.lo<=0:raise ArithmeticError('tail')
        tailworst=margin.lo if tailworst is None else min(tailworst,margin.lo)
        tprev=DELTA;cache={}
        for ls,rs in band['intervals']:
            l,r=F(ls),F(rs)
            if l!=tprev or not l<r<=F(1,2):raise ValueError('input cover')
            u=upper_leaf(l,r,cl,ch,cache)
            if u>=0:raise ArithmeticError('leaf')
            worst=u if worst is None else max(worst,u);tprev=r;leaves+=1
        if tprev!=F(1,2):raise ValueError('incomplete input cover')
        prev=ch
        if (ix+1)%100==0:print('verify bands',ix+1,'seconds',round(time.time()-t0,1),flush=True)
    if prev!=CHIGH:raise ValueError('incomplete noise cover')
    return {'passed':True,'bits':bits,'bands':len(cert['bands']),'leaves':leaves,'largest_upper':I(raw=(worst,worst)).record(),
        'minimum_tail_lower':I(raw=(tailworst,tailworst)).record()}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--verify',type=Path);p.add_argument('--bits',type=int,default=128);args=p.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    if args.verify:
        c=json.loads(args.verify.read_text());res=validate(c,args.bits);(args.output/f'verification_{args.bits}.json').write_text(json.dumps(res,indent=2)+'\n');print(res)
    else:
        c=construct(args.bits);(args.output/'common_noise_compact_certificate.json').write_text(json.dumps(c,indent=2)+'\n');print('FINAL',c['band_count'],c['leaf_count'],'deterministic covering complete')
if __name__=='__main__':main()
