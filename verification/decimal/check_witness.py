"""Independent audit of the one retained eight-use illustration.

No submitted numerical routine is imported. Interval expression uses posterior
probabilities and normalized coherence rather than effect-determinant spectra.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,argparse
import decimal_interval as ar
from decimal_interval import Interval as I,h

def evaluate(precision):
    ar.set_precision(precision)
    n=8;p=I('7/10');eps=I('1/10');eta=1-2*eps;c=1-eta*eta
    alpha=(1+eta/I(3).sqrt())/2;beta=1-alpha
    kappa=eta*eta*I('2/3')/(1-eta*eta/3)
    total=I(0);rows=[]
    for m in range(n+1):
        aentropy=I(1) if m==0 else I(0)
        centropy=I(0)
        if m:
            for j in range(m+1):
                prob0=alpha**j*beta**(m-j)
                prob1=beta**j*alpha**(m-j)
                weight=I(comb(m,j))*(prob0+prob1)/2
                x=I('1/2') if 2*j==m else (prob0 if 2*j<m else prob1)/(prob0+prob1)
                d=(1-kappa**m)*x*(1-x)
                eig=2*d/(1+(1-4*d).sqrt())
                aentropy+=weight*h(x);centropy+=weight*h(eig)
        maskweight=I(comb(n,m))*p**m*(1-p)**(n-m)
        value=maskweight*(-centropy if m==n else aentropy-centropy)
        rows.append({'measured':m,'mask_probability':maskweight.record(),'weighted_contribution_bits':value.record()})
        total+=value
    gamma=I('27/59')
    ell=I('9/25')*(1+I('16/25')/4+I('16/25')**2/4+I('16/25')**3/10)
    assert (ell-gamma).lo>0
    zero_coefficient=1-p-p*gamma
    assert zero_coefficient.hi<0
    assert (total/n).lo>0
    return {'passed':True,'n':n,'p':'7/10','epsilon':'1/10','block_coherent_information_bits':total.record(),'per_use_rate':(total/n).record(),
            'gamma_exact_given_audited_entropy_lemma':'27/59','one_use_threshold':'59/86','ell_minus_gamma':(ell-gamma).record(),
            'one_use_ic_over_input_entropy_upper':zero_coefficient.record(),'all_mask_terms':rows,'postselection':False,
            'note':'Quantum capacity lower bound via an outer code, not the fidelity or rate of an isolated inner block.'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--precision',type=int,default=100);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    r=evaluate(a.precision);a.output.write_text(json.dumps(r,indent=2)+'\n');print(r['per_use_rate'])
