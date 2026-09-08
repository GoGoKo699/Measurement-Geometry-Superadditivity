"""Independent directed decimal intervals. No submitted evaluator is imported.

Basic operations use separate FLOOR/CEILING decimal Contexts. Decimal ln, exp,
and sqrt are correctly rounded to nearest by libmpdec, so their endpoints are
expanded by one representable value in each direction. Rational inputs only.
"""
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction
from functools import lru_cache

PREC = 90

def set_precision(precision: int):
    global PREC, DOWN, UP, NEAR
    if precision < 40:
        raise ValueError('Need at least 40 decimal digits')
    PREC=precision
    DOWN=Context(prec=precision,rounding=ROUND_FLOOR,Emin=-999999,Emax=999999)
    UP=Context(prec=precision,rounding=ROUND_CEILING,Emin=-999999,Emax=999999)
    NEAR=Context(prec=precision,rounding=ROUND_HALF_EVEN,Emin=-999999,Emax=999999)
    log2.cache_clear()

class Interval:
    __slots__=('lo','hi')
    def __init__(self,x=0,hi=None):
        if hi is not None:
            self.lo=Decimal(x);self.hi=Decimal(hi)
        elif isinstance(x,Interval):self.lo=x.lo;self.hi=x.hi
        elif isinstance(x,Decimal):self.lo=self.hi=x
        else:
            if isinstance(x,float):raise TypeError('Float input disallowed')
            f=Fraction(x);n=Decimal(f.numerator);d=Decimal(f.denominator)
            self.lo=DOWN.divide(n,d);self.hi=UP.divide(n,d)
        if not self.lo.is_finite() or not self.hi.is_finite() or self.lo>self.hi:
            raise ArithmeticError('Invalid interval')
    @classmethod
    def hull(cls,l,r):
        l=cls(l);r=cls(r);return cls(l.lo,r.hi)
    def __add__(self,o):
        o=Interval(o);return Interval(DOWN.add(self.lo,o.lo),UP.add(self.hi,o.hi))
    __radd__=__add__
    def __neg__(self):return Interval(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self,o):return self+-Interval(o)
    def __rsub__(self,o):return Interval(o)+-self
    def __mul__(self,o):
        o=Interval(o)
        return Interval(min(DOWN.multiply(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)),max(UP.multiply(x,y) for x in (self.lo,self.hi) for y in (o.lo,o.hi)))
    __rmul__=__mul__
    def inverse(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('Interval contains zero')
        return Interval(DOWN.divide(Decimal(1),self.hi),UP.divide(Decimal(1),self.lo))
    def __truediv__(self,o):return self*Interval(o).inverse()
    def __rtruediv__(self,o):return Interval(o)*self.inverse()
    def __pow__(self,n):
        if not isinstance(n,int):raise TypeError('Only integer powers')
        if n<0:return self.inverse()**(-n)
        r=Interval(1);b=self
        while n:
            if n&1:r=r*b
            b=b*b;n//=2
        return r
    def sqrt(self):
        if self.lo<0:raise ArithmeticError('Negative square root')
        l=NEAR.sqrt(self.lo);h=NEAR.sqrt(self.hi)
        return Interval(Decimal(0) if self.lo==0 else NEAR.next_minus(l),Decimal(0) if self.hi==0 else NEAR.next_plus(h))
    def ln(self):
        if self.lo<=0:raise ArithmeticError('Nonpositive logarithm')
        return Interval(NEAR.next_minus(NEAR.ln(self.lo)),NEAR.next_plus(NEAR.ln(self.hi)))
    def exp(self):return Interval(NEAR.next_minus(NEAR.exp(self.lo)),NEAR.next_plus(NEAR.exp(self.hi)))
    def lower(self):return Interval(self.lo)
    def upper(self):return Interval(self.hi)
    def record(self):return {'lower':str(self.lo),'upper':str(self.hi),'decimal_digits':PREC}

@lru_cache(None)
def log2():return Interval(2).ln()
def h(x):
    x=Interval(x)
    if x.lo==x.hi and x.lo in (0,1):return Interval(0)
    if not (0<x.lo<=x.hi<1):raise ArithmeticError('Entropy outside domain')
    return -(x*x.ln()+(1-x)*(1-x).ln())/log2()
set_precision(PREC)
