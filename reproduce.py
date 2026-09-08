#!/usr/bin/env python3
"""Reproduce this scientific baseline in a new output directory.

Default regenerates/validates figure inputs and redraws approved figures.
--full also reruns all three complete compact-certificate verifiers, the
retained witness, endpoint constants and declared physical/negative controls.
--rebuild-certificate adds generation of the canonical partition from scratch.
"""
from __future__ import annotations
import argparse,json,os,subprocess,sys
from pathlib import Path
from fractions import Fraction
from baseline_tools import ROOT,integrity,write_json,read,sha,require,compare_data,compare_figure_reproduction

def command(args,log:Path):
 log.parent.mkdir(parents=True,exist_ok=True)
 env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MPLBACKEND':'Agg'}
 with log.open('w') as stream:
  subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,env=env,stdout=stream,stderr=subprocess.STDOUT,check=True)

def check_full_results(out:Path):
 comparisons=[]
 pairs=[('certificate/integer/verification_224.json','evidence/reference/integer224.json'),('certificate/mpmath85.json','evidence/reference/mpmath85.json'),('certificate/decimal130.json','evidence/reference/decimal130.json'),('witness/decimal100.json','evidence/reference/witness100.json'),('witness/decimal140.json','data/figures/figure1_original_witness140.json'),('analytic/analytic_checks.json','evidence/reference/analytic_checks.json'),('physical/physical_check.json','evidence/reference/physical_check.json'),('witness/mpmath/mixed_input_control.json','evidence/controls/mixed_input_control.json'),('witness/mpmath/rejected_float_candidate.json','evidence/controls/rejected_float_candidate.json')]
 for rel,ref in pairs:
  a,b=out/rel,ROOT/ref
  require(a.is_file(),'missing full result '+rel)
  # Deterministic exact arithmetic and current environment also reproduce the
  # small floating-point check. Compare ordinary numbers with a tolerance only
  # in the physical record; all certificate/witness Decimal strings are exact.
  same=a.read_bytes()==b.read_bytes()
  if not same:
   if rel.startswith('physical/'):
    aa,bb=read(a),read(b)
    require(aa['passed'] and aa['max_comparison_error']<2e-12,'physical check failed')
    require(aa['reported_records']==bb['reported_records'] and aa['hidden_outcome_terms']==bb['hidden_outcome_terms'],'physical case accounting changed')
   else:raise ValueError('regenerated reference differs: '+rel)
  comparisons.append({'output':rel,'reference':ref,'byte_identical':same})
 a=read(out/'witness/mpmath/witness.json');b=read(out/'witness/decimal140.json')
 require(a['passed'] and b['passed'],'missing positive witness validation')
 al,ah=Fraction(a['per_use_rate']['lower']),Fraction(a['per_use_rate']['upper'])
 bl,bh=Fraction(b['per_use_rate']['lower']),Fraction(b['per_use_rate']['upper'])
 require(0<al<=bl<=bh<=ah,'independent witness enclosures not nested')
 require(len(a['all_mask_terms'])==9 and len(b['all_mask_terms'])==9,'missing all-mask witness terms')
 return {'passed':True,'reference_comparisons':comparisons,'independent_witness_enclosures_nested':True,'mathematical_scope_changed':False}

def run(output:Path,full=False,rebuild=False):
 output=Path(output).resolve()
 require(not output.exists(),'Use a new output directory; existing results are never overwritten')
 if output.is_relative_to(ROOT):require(output.is_relative_to(ROOT/'build'),'Inside the package, outputs may only be placed under build/')
 before=integrity();output.mkdir(parents=True);write_json(output/'integrity_before.json',before)
 def call(rel,*args,name):command([ROOT/rel,*args],output/'logs'/(name+'.log'))
 call('numerics/figure_inputs/build_inputs.py','--output',output/'data/figures',name='data_build')
 call('numerics/figure_inputs/verify_inputs.py','--data',output/'data/figures','--report',output/'data_validation.json',name='data_check')
 write_json(output/'data_comparison.json',compare_data(output/'data/figures'))
 # Regenerated data have just been checked byte-for-byte against the frozen
 # input files. The renderer reads that frozen baseline, never a historical ZIP.
 call('figures/code/render_figures.py','--output',output/'figures',name='figure_render')
 call('figures/code/build_review_pdf.py','--figures',output/'figures','--output',output/'figures/three_figure_review.pdf',name='review_render')
 call('figures/code/verify_render.py','--output',output/'figures','--report',output/'render_validation.json',name='figure_check')
 write_json(output/'figure_comparison.json',compare_figure_reproduction(output/'figures'))
 if full:
  for name in ('certificate','witness','analytic','physical'):(output/name).mkdir()
  cert=ROOT/'certificates/common_noise_compact_certificate.json'
  if rebuild:
   call('verification/integer/certify_all_noise.py','--output',output/'certificate/rebuilt','--bits','128',name='certificate_build')
   require(sha(output/'certificate/rebuilt/common_noise_compact_certificate.json')==sha(cert),'rebuilt rational certificate differs')
  call('verification/integer/certify_all_noise.py','--verify',cert,'--output',output/'certificate/integer','--bits','224',name='certificate_integer')
  call('verification/mpmath/cross_backend.py','--certificate',cert,'--output',output/'certificate/mpmath85.json','--digits','85',name='certificate_mpmath')
  call('verification/decimal/verify_certificate.py','--certificate',cert,'--output',output/'certificate/decimal130.json','--precision','130',name='certificate_decimal')
  call('verification/decimal/check_witness.py','--output',output/'witness/decimal100.json','--precision','100',name='witness_decimal100')
  call('verification/decimal/check_witness.py','--output',output/'witness/decimal140.json','--precision','140',name='witness_decimal140')
  call('verification/mpmath/witness_and_controls.py','--output',output/'witness/mpmath',name='witness_mpmath_controls')
  call('verification/analytic/check_endpoints.py','--output',output/'analytic/analytic_checks.json',name='analytic_symbolic')
  call('verification/analytic/run_rational_checks.py','--output',output/'analytic/rational_endpoint_checks.json',name='analytic_rational')
  call('verification/physical/physical_check.py','--output',output/'physical/physical_check.json',name='physical_checks')
  write_json(output/'full_reference_comparison.json',check_full_results(output))
 command(['-m','pytest','-q','-p','no:cacheprovider',ROOT/'tests'],output/'logs/tests.log')
 after=integrity();write_json(output/'integrity_after.json',after)
 result={'passed':True,'mode':'full' if full else 'figures','rebuilt_certificate':bool(full and rebuild),'approved_artifacts_unchanged':after['approved_artifacts_unchanged'],'nested_archive_extraction':False,'old_repository_access':False,'scientific_scope_changed':False,'external_audit':False}
 write_json(output/'REPRODUCTION_RESULT.json',result);print(json.dumps(result,indent=2))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);p.add_argument('--full',action='store_true');p.add_argument('--rebuild-certificate',action='store_true');a=p.parse_args()
 if a.rebuild_certificate and not a.full:p.error('--rebuild-certificate requires --full')
 run(a.output,a.full,a.rebuild_certificate)
