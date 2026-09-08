from pathlib import Path
from copy import deepcopy
import ast,importlib.util,json,hashlib,sys,tempfile
import pytest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import baseline_tools as bt

def test_canonical_provenance():
 r=bt.check_provenance()
 assert r['source_identities']==44 and r['canonical_units']==23 and r['source_fragments']==125

def test_approved_figures_protected():
 assert bt.check_protected()==27

def test_direct_inputs_and_independent_code_boundaries():
 assert bt.check_inputs() and bt.code_boundaries()

def test_no_nested_archive_runtime():
 assert not list(ROOT.rglob('*.zip'))
 for top in ['verification','numerics','figures/code']:
  for p in (ROOT/top).rglob('*.py'):
   assert '/mnt/data/' not in p.read_text()
   assert '/home/oai/' not in p.read_text()

def test_frozen_argument_identity():
 reg=bt.read(ROOT/'provenance/SOURCE_REGISTER.json')
 src=next(s for s in reg['sources'] if s['id']=='S1')
 assert bt.sha(ROOT/'docs/FROZEN_ARGUMENT.md')==src['sha256']

def test_reference_shape_and_flag_accounting():
 witness=bt.read(ROOT/'data/figures/figure1_original_witness140.json')
 assert witness['n']==8 and witness['p']=='7/10' and witness['epsilon']=='1/10'
 assert [x['measured'] for x in witness['all_mask_terms']]==list(range(9))
 assert witness['postselection'] is False

def test_actual_checker_algorithms_preserved():
 entries=bt.read(ROOT/'provenance/FILE_LINEAGE.json')['records']
 wanted={'verification/integer/certify_all_noise.py','verification/integer/dyadic_interval.py','verification/mpmath/cross_backend.py','verification/decimal/verify_certificate.py','verification/decimal/decimal_interval.py','verification/decimal/check_witness.py'}
 checked=set()
 for row in entries:
  if row['destination'] in wanted:
   assert row['source_sha256']==bt.sha(ROOT/row['destination'])
   checked.add(row['destination'])
 assert checked==wanted

def test_render_functions_unchanged_asts():
 entries=bt.read(ROOT/'provenance/FILE_LINEAGE.json')['records']
 row=next(x for x in entries if x['destination']=='figures/code/render_figures.py')
 preserved=set(row['unchanged_top_level_function_or_class_asts'])
 assert {'diagram1','witness1','header2','region2','width2','geometry3','gap3','combine','save_component'}<=preserved

def test_paper_scope_is_common_error():
 text=(ROOT/'docs/MODEL_AND_CLAIMS.md').read_text()
 assert '**common**' in text and 'postselection' in text

def test_invalid_output_directory_is_rejected():
 import reproduce
 with pytest.raises(ValueError,match='new output'):
  reproduce.run(ROOT/'figures/approved')
