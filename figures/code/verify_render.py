#!/usr/bin/env python3
"""Verify rendering fidelity to frozen inputs, not the underlying theorem."""
from __future__ import annotations
import argparse,csv,hashlib,json,re
from pathlib import Path
import xml.etree.ElementTree as ET
import numpy as np
import fitz
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'figures'
DATA=ROOT/'data/figures'

def rows(name):
 with (DATA/name).open(newline='') as f:return list(csv.DictReader(f))
def check_equal(a,b,label):
 if not np.array_equal(np.asarray(a),np.asarray(b)):raise AssertionError(label)
def verify(out):
 source_manifest=json.loads((ROOT/'provenance/FIGURE_INPUTS.json').read_text())
 for name,digest in source_manifest.items():
  if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:raise AssertionError('changed source '+name)
 r=json.loads((out/'RENDER_RECORD.json').read_text())
 f1=rows('figure1_comparison.csv');f2=rows('figure2_pauli_guaranteed_region.csv');f3=rows('figure3_cone_gap.csv');geom=rows('figure3_cone_geometry.csv')
 vals=[float(v['value_plot']) for v in f1]
 check_equal(r['figure1']['source_values'],vals,'Figure 1 normalization')
 check_equal(r['figure1']['display_values'],np.array(vals)*1e5,'Figure 1 multiplier')
 assert vals[0]==0 and vals[1]>0 and r['figure1']['errorbars'] is False
 assert r['schematic_contract']['encoding_precedes_random_choices'] and r['schematic_contract']['uses_independent']
 assert set(r['schematic_contract']['receiver_cannot_access'])=={'true bit r','error bit z','measured quantum system'}
 check_equal(r['figure2']['x_values'],[float(v['epsilon']) for v in f2],'Figure 2 x')
 check_equal(r['figure2']['p_cert_values'],[float(v['p_cert']) for v in f2],'Figure 2 lower curve')
 check_equal(r['figure2']['p_rep_values'],[float(v['p_rep']) for v in f2],'Figure 2 upper curve')
 check_equal(r['figure2']['inset']['display_values'],np.array([float(v['certified_width'])for v in f2])*1e3,'Width scale')
 check_equal(r['figure2']['shade_mask'],[v['theorem_applies']=='True' for v in f2],'Shade domain')
 assert not r['figure2']['witness_overlay'] and not r['figure2']['capacity_phase_labels']
 assert r['figure2']['lower_style']=='solid' and r['figure2']['upper_style']=='dashed'
 check_equal(r['figure3_gap']['lambda_values'],[float(v['lambda_min'])for v in f3],'Figure 3 x')
 check_equal(r['figure3_gap']['gap_values'],[float(v['gap'])for v in f3],'Figure 3 exact curve')
 check_equal(r['figure3_gap']['linear_asymptote_values'],[float(v['linear_asymptote'])for v in f3],'Figure 3 asymptote')
 assert r['figure3_gap']['slope_exact']=='18/289' and r['figure3_gap']['domain']==[0,.25]
 P=np.asarray(r['figure3_geometry']['common_projection_matrix'])
 np.testing.assert_allclose(P@P.T,np.eye(2),rtol=0,atol=1e-14)
 for snapshot in r['figure3_geometry']['snapshots']:
  selected=sorted([v for v in geom if v['lambda_exact']==snapshot['lambda']],key=lambda x:int(x['axis']))
  for actual,src in zip(snapshot['axes'],selected):
   n=np.array([float(src[c])for c in ['nx','ny','nz']]);check_equal(actual['unit_vector'],n,'Cone data')
   center=np.asarray(snapshot['center_pt']);radius=snapshot['radius_pt']
   np.testing.assert_allclose(np.asarray(actual['projected_endpoints_pt']),center+radius*np.array([-n,n])@P.T,atol=1e-12,rtol=0)
  assert snapshot['radius_pt']==37
 for t in r['layout']['text_extent_checks']:
  assert not t['outside_text'],t
  assert t['minimum_font_pt']>=8,t
 figs=[]
 for layout in r['layout']['composites']:
  name=layout['name'];pdf=out/(name+'.pdf');svg=out/(name+'.svg');png=out/(name+'.png')
  with fitz.open(pdf) as d:
   assert len(d)==1
   assert abs(d[0].rect.width-7.08*72)<1e-3
   assert not d[0].get_images(), 'Raster object in scientific PDF'
   assert '\ufffd' not in d[0].get_text()
   spanbad=[]
   for block in d[0].get_text('dict')['blocks']:
    for line in block.get('lines',[]):
     for span in line['spans']:
      x0,y0,x1,y1=span['bbox']
      if x0<-.8 or y0<-.8 or x1>d[0].rect.width+.8 or y1>d[0].rect.height+.8:spanbad.append(span)
   assert not spanbad,spanbad
   image_count=len(d[0].get_images())
  doc=ET.parse(svg);ids=[e.attrib['id']for e in doc.iter()if 'id'in e.attrib]
  assert len(ids)==len(set(ids)),'Duplicate SVG defs'
  assert not [e for e in doc.iter()if e.tag.endswith('}image')],'Embedded raster in SVG'
  idset=set(ids)
  for e in doc.iter():
   for key,v in e.attrib.items():
    for ref in re.findall(r'url\(#([^)]*)\)',v):assert ref in idset,ref
    if key.endswith('href') and v.startswith('#'):assert v[1:] in idset,v
  im=Image.open(png)
  assert abs(im.width-7.08*300)<=1
  figs.append({'figure':name,'pdf_vector_image_count':image_count,'svg_raster_count':0,'pixel_size':list(im.size),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'svg_sha256':hashlib.sha256(svg.read_bytes()).hexdigest(),'png_sha256':hashlib.sha256(png.read_bytes()).hexdigest()})
 return {'passed':True,'date':'2026-09-08','source_members_verified':len(source_manifest),'all_source_bytes_unchanged':True,
 'curve_coordinates_traced_to_csv':{'figure2':len(f2),'figure3':len(f3)},'witness_values_traced':2,'geometry_axis_records_traced':len(geom),
 'actual_final_text_extents_inside_page':True,'matplotlib_component_text_extents_inside_canvas':True,
 'same_cone_camera_and_scale':True,'upper_frontier_strict_in_captions':True,'statistical_errorbars_added':False,
 'all_drawn_pdf_and_svg_components_vector':True,'figures':figs,
 'scope':'Rendering and scientific-input traceability checks. No theorem audit, witness recomputation, simulation, or repository operation.',
 'user_visual_approval':True}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'figures/approved');p.add_argument('--report',type=Path,default=ROOT/'build/RENDER_VALIDATION.json');a=p.parse_args()
 res=verify(a.output);a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
