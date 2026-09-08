"""Tests target arithmetic boundaries, coverage and retained physical claims.

The full 29,635-leaf audit is run by reproduce.py, not replaced by unit tests.
"""
import sys,json,copy
from pathlib import Path
from fractions import Fraction as F
import pytest
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'verification/decimal'))
sys.path.insert(0,str(ROOT/'verification/analytic'))
import decimal_interval as d
from decimal_interval import Interval as I,h
import verify_certificate as v
import check_witness as w
import check_endpoints as e

@pytest.fixture(autouse=True)
def setup():
    d.set_precision(60)

@pytest.mark.parametrize('a,b',[('1/7','2/11'),('-4/9','2/7'),('-3/5','-5/11'),('0','1/3')])
def test_rational_arithmetic(a,b):
    x,y=F(a),F(b)
    for z,q in [(I(a)+I(b),x+y),(I(a)-I(b),x-y),(I(a)*I(b),x*y),(I(a)/I(b),x/y)]:
        assert F(z.lo)<=q<=F(z.hi)

def test_sqrt_log_exp():
    q=I('2/3').sqrt()
    assert F(q.lo)**2<=F(2,3)<=F(q.hi)**2
    r=I('2/3').ln().exp()
    assert F(r.lo)<=F(2,3)<=F(r.hi)
    assert I(1).ln().lo<=0<=I(1).ln().hi

def test_error_and_endpoints():
    assert h(0).lo==h(1).hi==0
    assert h('1/2').lo<=1<=h('1/2').hi
    with pytest.raises(TypeError):I(0.1)
    with pytest.raises(ZeroDivisionError):I(-1,1).inverse()
    with pytest.raises(ArithmeticError):I(-1).sqrt()
    with pytest.raises(ArithmeticError):I(0).ln()

CERT=ROOT/'certificates/common_noise_compact_certificate.json'
@pytest.fixture
def cert():return json.loads(CERT.read_text())

def test_wrong_claim_rejected(cert):
    cert['ell']='c';
    with pytest.raises(ValueError,match='parameters'):v.verify(cert,50)

def test_noise_gap_rejected(cert):
    cert['bands'][0]['c_lower']='1/10000'
    with pytest.raises(ValueError,match='Noise partition'):v.verify(cert,50)

def test_input_gap_rejected(cert):
    cert['bands'][0]['intervals'][0][0]='1/999999'
    with pytest.raises(ValueError,match='Input partition'):v.verify(cert,50)

def test_incomplete_input_rejected(cert):
    cert['bands'][0]['intervals']=cert['bands'][0]['intervals'][:1]
    with pytest.raises(ValueError,match='Incomplete input'):v.verify(cert,50)

def test_overlap_rejected(cert):
    cert['bands'][0]['intervals'].insert(1,cert['bands'][0]['intervals'][0][:])
    with pytest.raises(ValueError,match='Input partition'):v.verify(cert,50)

def test_secant_conjugacy_bound():
    # Flat lower line gives a maximum at one-half, equal to one bit.
    up=v.maximum_upper(F(1,4),F(1,2),I(0),I(0),I(1))
    assert up>=1
    # Affine cost has known conjugate at its stationary point.
    up=v.maximum_upper(F(1,100),F(1,2),I('1/100'),I('1/2'),I(1))
    ref=I('3/2').ln()/d.log2()
    assert up>=ref.lo

def test_witness_all_masks_and_one_use_zero():
    r=w.evaluate(65)
    assert r['passed'] and r['n']==8 and not r['postselection']
    assert [x['measured'] for x in r['all_mask_terms']]==list(range(9))
    ps=sum((I(x['mask_probability']['lower'],x['mask_probability']['upper']) for x in r['all_mask_terms']),I(0))
    assert ps.lo<=1<=ps.hi
    assert F(r['all_mask_terms'][-1]['weighted_contribution_bits']['upper'])<0
    assert F(r['per_use_rate']['lower'])>F('0.0000747')
    assert F(r['one_use_ic_over_input_entropy_upper']['upper'])<0

def test_analytic_constants():assert e.evaluate()['passed']
