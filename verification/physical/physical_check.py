"""New hidden-outcome channel checks. Uses no submitted code.

Constructs the actual projective outcomes, mixes them only according to the
observed erroneous report, then obtains receiver/reference entropy. Selected
small controls use the retained Pauli noise model; the eight-use rate is
independently certified by check_witness.py, not by huge matrix diagonalization.
"""
import itertools,json,argparse
from pathlib import Path
import numpy as np
from math import comb

I=np.eye(2,dtype=complex)
PAULI=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
EIG=[np.linalg.eigh(s)[1][:,::-1] for s in PAULI] # true label zero is eigenvalue +1

def entropy(matrix):
    matrix=(matrix+matrix.conj().T)/2
    val=np.linalg.eigvalsh(matrix)
    if min(val)<-2e-12:raise ArithmeticError('nonpositive physical state')
    val=val[val>1e-15]
    return float(-np.sum(val*np.log2(val)))

def embed_indices(record,n):
    survivors=[i for i,x in enumerate(record) if x==-1]
    ids=[]
    for r in range(2):
        for bits in itertools.product([0,1],repeat=len(survivors)):
            digits=[];biter=iter(bits)
            for x in record:digits.append(next(biter) if x==-1 else 2+x)
            pos=r*8**n
            for i,d in enumerate(digits):pos+=d*8**(n-1-i)
            ids.append(pos)
    return ids

def physical(iso,t,n,p=0.7,e=0.1,full=False):
    psi=np.vstack([np.sqrt(1-t)*iso[:,0],np.sqrt(t)*iso[:,1]]).reshape([2]+[2]*n)
    total=0.;trace=0.;nr=0;nh=0
    big=np.zeros((2*8**n,2*8**n),complex) if full else None
    for record in itertools.product(range(-1,6),repeat=n):
        measured=[(i,x//2,x%2) for i,x in enumerate(record) if x>=0]
        k=n-len(measured)
        block=np.zeros((2**(k+1),2**(k+1)),complex)
        for truth in itertools.product([0,1],repeat=len(measured)):
            v=psi;prob=(1-p)**k*(p/3)**len(measured)
            # Contract from the right; indices of the remaining earlier sites stay fixed.
            for (site,basis,reported),actual in reversed(list(zip(measured,truth))):
                prob*=1-e if actual==reported else e
                bra=EIG[basis][:,actual].conj()
                v=np.tensordot(v,bra,axes=([site+1],[0]))
            v=v.reshape(-1)
            block+=prob*np.outer(v,v.conj());nh+=1
        q=float(np.trace(block).real);trace+=q;nr+=1
        if q:
            rb=block/q
            b=np.trace(rb.reshape(2,2**k,2,2**k),axis1=0,axis2=2)
            total+=q*(entropy(b)-entropy(rb))
        if full:
            ix=embed_indices(record,n);big[np.ix_(ix,ix)]=block
    whole=None
    if full:
        bob=np.trace(big.reshape(2,8**n,2,8**n),axis1=0,axis2=2)
        whole=entropy(bob)-entropy(big)
    assert abs(trace-1)<2e-12
    return total,whole,nr,nh,trace

def antipodal(n):
    _,v=np.linalg.eigh(sum(PAULI)/np.sqrt(3))
    plus=v[:,1];minus=v[:,0]
    a=b=np.array([1],complex)
    for _ in range(n):a=np.kron(a,plus);b=np.kron(b,minus)
    return np.column_stack([a,b])

def triplet_cost(iso,t,p,e):
    rho=iso@np.diag([1-t,t])@iso.conj().T
    w,v=np.linalg.eigh(rho);sqrt=(v*np.sqrt(np.maximum(w,0)))@v.conj().T
    cost=0.
    for axis in PAULI:
        for sign in (1,-1):
            effect=(I+sign*(1-2*e)*axis)/2
            m=sqrt@effect@sqrt;q=float(np.trace(m).real)
            cost+=q*entropy(m/q)/3
    return (1-p)*entropy(rho)-p*cost

def binary_entropy(x):
    return 0. if x<=0 or x>=1 else -x*np.log2(x)-(1-x)*np.log2(1-x)

def repetition_rate(n,p,e,t=0.5):
    alpha=(1+(1-2*e)/np.sqrt(3))/2;beta=1-alpha
    off2=(1-2*e)**2/6
    tot=0.
    for m in range(n+1):
        A=binary_entropy(t) if m==0 else 0.;C=0.
        if m:
            for j in range(m+1):
                a=alpha**j*beta**(m-j);b=beta**j*alpha**(m-j)
                mat=np.array([[(1-t)*a,np.sqrt(t*(1-t))*np.sqrt(off2)**m],[np.sqrt(t*(1-t))*np.sqrt(off2)**m,t*b]])
                q=float(np.trace(mat));A+=comb(m,j)*q*binary_entropy(t*b/q);C+=comb(m,j)*q*entropy(mat/q)
        tot+=comb(n,m)*p**m*(1-p)**(n-m)*(-C if m==n else A-C)
    return tot

def run():
    rng=np.random.default_rng(2026090801);rows=[];rmax=0.;nrecords=nsummands=0
    # Every complex matrix unit tests the physical measurement map, not just densities.
    map_error=0.
    for j,k in itertools.product(range(2),repeat=2):
        X=np.zeros((2,2),complex);X[j,k]=1
        for b in range(3):
            for s in range(2):
                actual=sum(((.9 if truth==s else .1)*np.vdot(EIG[b][:,truth],X@EIG[b][:,truth]) for truth in range(2)))
                effect=(I+(-1)**s*.8*PAULI[b])/2
                map_error=max(map_error,abs(actual-np.trace(effect@X)))
    for n,t,kind in [(1,.27,'arbitrary'),(1,.5,'repetition'),(2,.5,'repetition'),(2,.31,'arbitrary'),(3,.5,'repetition')]:
        if kind=='repetition':enc=antipodal(n)
        else:
            z=rng.normal(size=(2**n,2))+1j*rng.normal(size=(2**n,2));enc=np.linalg.qr(z)[0]
        v,full,nr,nh,trace=physical(enc,t,n,full=(n<=2));nrecords+=nr;nsummands+=nh
        pred=triplet_cost(enc,t,.7,.1) if n==1 else repetition_rate(n,.7,.1,t) if kind=='repetition' else None
        err=abs(v-pred) if pred is not None else 0.
        if full is not None:err=max(err,abs(v-full))
        assert err<2e-12;rmax=max(rmax,err)
        rows.append({'n':n,'input':kind,'t':t,'branch_ic':v,'full_matrix_ic':full,'independent_formula_ic':pred,'max_discrepancy':err,'trace':trace,'reported_records':nr,'hidden_true_outcome_terms':nh})
    return {'passed':True,'seed':2026090801,'noise_model':'p=7/10, epsilon=1/10, three equally likely Pauli axes','matrix_unit_effect_error':map_error,
            'physical_cases':len(rows),'reported_records':nrecords,'hidden_outcome_terms':nsummands,'max_comparison_error':rmax,'largest_full_matrix_dimension':128,
            'exact_eight_use_value_in':'witness100.json and witness140.json','cases':rows,'full_eight_use_matrix_constructed':False}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();r=run();a.output.write_text(json.dumps(r,indent=2)+'\n');print(r)
