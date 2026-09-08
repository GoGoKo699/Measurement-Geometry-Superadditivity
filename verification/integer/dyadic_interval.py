"""Independent outward intervals using integers, not libmpdec/mpmath arithmetic.

Endpoints are integer multiples of 2**(-BITS). Logarithms use the
atanh power series after dyadic range reduction, with a proved remainder.
Square roots use math.isqrt; each arithmetic operation rounds outward.
This is a small purpose-built verifier, not a general interval library.
"""
from __future__ import annotations
from fractions import Fraction
from functools import lru_cache
from math import isqrt

BITS = 256
SCALE = 1 << BITS

def ceildiv(a: int, b: int) -> int:
    if b <= 0:
        raise ValueError('positive denominator required')
    return -((-a)//b)

class Box:
    __slots__ = ('lo','hi')
    def __init__(self, value=0, *, raw=None):
        if raw is not None:
            self.lo, self.hi = raw
        elif isinstance(value, Box):
            self.lo,self.hi=value.lo,value.hi
        else:
            if isinstance(value,float):
                raise TypeError('binary floating-point constants are not certificate inputs')
            q=Fraction(value)
            self.lo=(q.numerator*SCALE)//q.denominator
            self.hi=ceildiv(q.numerator*SCALE,q.denominator)
        if self.lo>self.hi:
            raise ValueError('reversed interval')
    @classmethod
    def hull(cls, a, b):
        a,b=cls(a),cls(b)
        return cls(raw=(min(a.lo,b.lo),max(a.hi,b.hi)))
    def __add__(self,b):
        b=Box(b);return Box(raw=(self.lo+b.lo,self.hi+b.hi))
    __radd__=__add__
    def __neg__(self):return Box(raw=(-self.hi,-self.lo))
    def __sub__(self,b):return self+-Box(b)
    def __rsub__(self,b):return Box(b)+-self
    def __mul__(self,b):
        b=Box(b);v=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        return Box(raw=(min(v)//SCALE,ceildiv(max(v),SCALE)))
    __rmul__=__mul__
    def reciprocal(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('interval contains zero')
        if self.hi<0:return -(-self).reciprocal()
        return Box(raw=(SCALE*SCALE//self.hi,ceildiv(SCALE*SCALE,self.lo)))
    def __truediv__(self,b):return self*Box(b).reciprocal()
    def __rtruediv__(self,b):return Box(b)*self.reciprocal()
    def __pow__(self,n):
        if not isinstance(n,int):raise TypeError('integer powers only')
        if n<0:return self.reciprocal()**(-n)
        out=Box(1);a=self
        while n:
            if n&1:out=out*a
            a=a*a;n>>=1
        return out
    def sqrt(self):
        if self.lo<0:raise ValueError('negative square-root domain')
        l=isqrt(self.lo*SCALE);h=isqrt(self.hi*SCALE)
        if h*h<self.hi*SCALE:h+=1
        return Box(raw=(l,h))
    def log(self):
        if self.lo<=0:raise ValueError('nonpositive logarithm domain')
        return Box(raw=(log_endpoint(self.lo).lo,log_endpoint(self.hi).hi))
    def lower_point(self):return Box(raw=(self.lo,self.lo))
    def upper_point(self):return Box(raw=(self.hi,self.hi))
    def contains_rational(self,q):
        q=Fraction(q)
        return self.lo*q.denominator<=q.numerator*SCALE<=self.hi*q.denominator
    def rational_bounds(self):
        return Fraction(self.lo,SCALE),Fraction(self.hi,SCALE)
    def record(self, places=35):
        # Only presentation uses base ten. Return directed decimal endpoints.
        p=10**places
        l=self.lo*p//SCALE;h=ceildiv(self.hi*p,SCALE)
        def render(i):
            sign='-' if i<0 else '';s=str(abs(i)).zfill(places+1)
            return sign+s[:-places]+'.'+s[-places:]
        return {'lower':render(l),'upper':render(h),'bits':BITS,
                'lo_dyadic_numerator':str(self.lo),'hi_dyadic_numerator':str(self.hi)}

def set_precision(bits):
    global BITS,SCALE
    if not isinstance(bits,int) or bits<96:raise ValueError('at least 96 bits')
    BITS=bits;SCALE=1<<bits
    log_endpoint.cache_clear();ln2.cache_clear()

def log_mantissa(m: Box) -> Box:
    """m in [1,2]; ln(m)=2 sum z**(2j+1)/(2j+1), z=(m-1)/(m+1)."""
    if m.lo<SCALE or m.hi>2*SCALE:raise ValueError('mantissa outside [1,2]')
    z=(m-1)/(m+1);zz=z*z;term=z;total=Box(0)
    # z<=1/3. 1/(1-z^2) controls the geometric upper remainder.
    for j in range(BITS):
        total+=term/(2*j+1)
        term*=zz
        n=j+1
        remainder=2*term/((2*n+1)*(1-zz))
        if remainder.hi<=32:
            return Box(raw=(2*total.lo,2*total.hi+max(0,remainder.hi)))
    raise ArithmeticError('log series did not terminate')

@lru_cache(maxsize=2)
def ln2():return log_mantissa(Box(2))

@lru_cache(maxsize=32768)
def log_endpoint(v: int):
    if v<=0:raise ValueError('positive endpoint required')
    k=v.bit_length()-1-BITS
    mant=Fraction(v,1<<(BITS+k)) # exactly in [1,2)
    return log_mantissa(Box(mant))+k*ln2()

def entropy(x):
    x=Box(x)
    if x.lo<0 or x.hi>SCALE:raise ValueError('entropy outside [0,1]')
    if x.lo==x.hi==0 or x.lo==x.hi==SCALE:return Box(0)
    return -(x*x.log()+(1-x)*(1-x).log())/ln2()
