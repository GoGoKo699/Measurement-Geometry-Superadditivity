from pathlib import Path
import csv,json,sys,xml.etree.ElementTree as ET
import numpy as np
import pytest
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'figures/code'))
import render_figures as rf
from verify_render import verify
import matplotlib.pyplot as plt

def test_source_integrity():
 assert len(rf.check_source())==len(json.loads((ROOT/'provenance/FIGURE_INPUTS.json').read_text()))

def test_render_validation():
 assert verify(ROOT/'figures/approved')['passed']

def test_witness_plot_data():
 audit={};data=rf.rows('figure1_comparison.csv');f=rf.witness1(data,audit)
 ax=f.axes[0]
 np.testing.assert_array_equal(ax.collections[1].get_offsets(),[[0,0]])
 np.testing.assert_allclose(ax.collections[2].get_offsets(),[[1,float(data[1]['value_plot'])*1e5]],rtol=0,atol=0)
 assert ax.get_yscale()=='linear'
 plt.close(f)

def test_region_actual_curves():
 audit={};data=rf.rows('figure2_pauli_guaranteed_region.csv');f=rf.region2(data,audit);ax=f.axes[0]
 assert len(f.axes)==1
 for line,col in zip(ax.lines,['p_cert','p_rep']):
  np.testing.assert_array_equal(line.get_ydata(),[float(v[col])for v in data])
 assert ax.lines[0].get_linestyle()=='-' and ax.lines[1].get_linestyle()=='--'
 plt.close(f)

def test_region_endpoint_mask():
 r=json.loads((ROOT/'figures/approved/RENDER_RECORD.json').read_text())['figure2']
 assert r['shade_mask'][0] is False and r['shade_mask'][-1] is False
 assert all(r['shade_mask'][1:-1]);assert r['witness_overlay'] is False

def test_width_is_probability_width_not_rate():
 a={'figure2':{}};data=rf.rows('figure2_pauli_guaranteed_region.csv');f=rf.width2(data,a)
 np.testing.assert_array_equal(f.axes[0].lines[0].get_ydata(),np.array([float(x['certified_width'])for x in data])*1e3)
 plt.close(f)

def test_gap_and_tangent_are_actual_source_arrays():
 a={};data=rf.rows('figure3_cone_gap.csv');f=rf.gap3(data,a);ax=f.axes[0]
 np.testing.assert_array_equal(ax.lines[0].get_ydata(),[float(v['gap'])for v in data])
 np.testing.assert_array_equal(ax.lines[1].get_ydata(),[float(v['linear_asymptote'])for v in data])
 assert ax.get_xlim()==(0,.25) and ax.get_ylim()==(0,.02)
 plt.close(f)

def test_no_fitted_asymptote():
 r=json.loads((ROOT/'figures/approved/RENDER_RECORD.json').read_text())['figure3_gap']
 assert r['slope_exact']=='18/289' and r['asymptote_status']=='analytical, not fitted'
 assert not r['witness_transferred_from_figure1']

def test_geometry_same_camera_and_scale():
 r=json.loads((ROOT/'figures/approved/RENDER_RECORD.json').read_text())['figure3_geometry']
 P=np.array(r['common_projection_matrix']);np.testing.assert_allclose(P@P.T,np.eye(2),atol=1e-14)
 assert {s['radius_pt']for s in r['snapshots']}=={37}
 assert [s['lambda'] for s in r['snapshots']]==['0','1/16','1/4']
 assert all(len(s['axes'])==3 for s in r['snapshots'])


def test_hidden_receiver_semantics():
 r=json.loads((ROOT/'figures/approved/RENDER_RECORD.json').read_text())['schematic_contract']
 assert r['encoding_precedes_random_choices'] and r['no_finite_block_perfect_decoder_claim']
 assert r['measured_branch']['reported_bit']=='s=r xor z'
 assert r['measured_branch']['measured_system']=='discarded, inaccessible'

def test_caption_protects_boundary_meanings():
 txt=(ROOT/'figures/CAPTIONS.md').read_text()
 for fragment in ['not the optimal eight-use','p_{\\mathrm{cert}}\\leq p<p_{\\mathrm{rep}}','below this conservative strip','not a fit','not transferred here']:
  assert fragment in txt

def test_source_contract_stays_historical():
 r=json.loads((ROOT/'figures/FIGURE_CONTRACT.json').read_text())
 assert r['rendered'] is False
 # The new rendering status is separate, never retroactively written into source.
 assert (ROOT/'figures/approved/figure_01_channel_and_witness.pdf').is_file()
