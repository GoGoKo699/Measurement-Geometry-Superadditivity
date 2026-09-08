"""New illustrative witnesses, certified with mpmath interval arithmetic.

Code construction is inherited; the block values at these larger errors and
the global single-use zero bounds use the new entropy comparison theorem.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import csv,json
from mpmath import mp,iv
mp.dps=160;iv.dps=125

def q(z):
    z=F(z);return iv.mpf(z.numerator)/z.denominator

def lo(z):return mp.mpf(z._mpi_[0])
def hi(z):return mp.mpf(z._mpi_[1])
def record(x):
    # Exact rational conversion of binary interval endpoints; decimal bounds
    # use integer floor/ceiling, not a rounded high-precision product.
    places=100
    def endpoint(v):
        sign,man,exp,_=v
        f=F(-man if sign else man,1)
        return f*(2**exp) if exp>=0 else f/F(2**(-exp),1)
    l=endpoint(x._mpi_[0])*10**places;u=endpoint(x._mpi_[1])*10**places
    li=l.numerator//l.denominator;ui=-((-u.numerator)//u.denominator)
    def fmt(k):
        sign='-' if k<0 else '';z=str(abs(k)).zfill(places+1)
        return sign+z[:-places]+'.'+z[-places:]
    return {'lower':fmt(li),'upper':fmt(ui),'decimal_places':places}

def h(x):
    if lo(x)==hi(x)==0 or lo(x)==hi(x)==1:return iv.mpf(0)
    return -(x*iv.log(x)+(1-x)*iv.log(1-x))/iv.log(2)

def parameters(e):
    e=q(e);a=(1-2*e)**2;c=1-a;P=1+a/4+a*a/4+a**3/10;ell=c*P
    g=c/(1-a/3);L=c/iv.sqrt(1-a/3)
    # min of interval enclosures, valid even if ordering unresolved.
    lower=iv.mpf([min(ell.a,g.a),min(ell.b,g.b)])
    return {'a':a,'c':c,'P':P,'ell':ell,'g':g,'L':L,'gamma_lower':lower}

def block(n,p,e):
    p=q(p);ep=q(e);eta=1-2*ep;ap=(1+eta/iv.sqrt(3))/2;bp=1-ap;off2=eta*eta/6
    total=iv.mpf(0);terms=[]
    for m in range(n+1):
        A=iv.mpf(1) if m==0 else iv.mpf(0);C=iv.mpf(0)
        if m:
            for k in range(m+1):
                v=ap**k*bp**(m-k);w=bp**k*ap**(m-k);prob=(v+w)/2
                posterior=q('1/2') if 2*k==m else (v if 2*k<m else w)/(v+w)
                det=(v*w-off2**m)/4
                # Positive sum avoids cancelling 1 - 4det/prob^2.
                disc=((v-w)**2+4*off2**m)/4
                small=(2*det)/(prob*(prob+iv.sqrt(disc)))
                A+=comb(m,k)*prob*h(posterior);C+=comb(m,k)*prob*h(small)
        weight=comb(n,m)*p**m*(1-p)**(n-m)
        term=weight*(-C if m==n else A-C);total+=term
        terms.append({'measured':m,'probability':record(weight),'contribution':record(term)})
    return total/n,terms
