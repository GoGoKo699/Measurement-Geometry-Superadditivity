#!/usr/bin/env python3
"""Render the frozen figure contract without recomputing scientific inputs.

Each numerical chart is created as its own Matplotlib figure. Composite
panels and the width inset are assembled as vector PDF/SVG assets. No TeX,
TikZ, external image generator, network access, or source-data writes.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, re
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon
from matplotlib.ticker import FixedLocator, FixedFormatter
import numpy as np
import fitz
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'figures'
DATA=ROOT/'data/figures'
# The user's stated cold-tone preference; redundant dash/marker encodings remain.
NAVY='#1B4264'; TEAL='#177D89'; INK='#25313B'; GRAY='#66727C'
PALE='#DCEDEF'; LIGHT='#EDF2F5'; GRID='#D5DEE4'; WHITE='#FFFFFF'
STAMP=datetime(2026,9,8,tzinfo=timezone.utc)
SVG_NS='http://www.w3.org/2000/svg'
ET.register_namespace('',SVG_NS);ET.register_namespace('xlink','http://www.w3.org/1999/xlink')
STYLE={
 'font.family':'DejaVu Sans','font.size':9.2,'mathtext.fontset':'dejavusans',
 'axes.labelsize':10.0,'xtick.labelsize':9.2,'ytick.labelsize':9.2,
 'axes.linewidth':.65,'xtick.major.width':.65,'ytick.major.width':.65,
 'xtick.major.size':3.2,'ytick.major.size':3.2,'axes.unicode_minus':True,
 'pdf.fonttype':42,'ps.fonttype':42,'svg.fonttype':'path',
 'svg.hashsalt':'measurement-geometry-figure-render-v1','path.simplify':False,
 'savefig.facecolor':WHITE,'figure.facecolor':WHITE,
 'text.color':INK,'axes.labelcolor':INK,'axes.edgecolor':GRAY,
 'xtick.color':INK,'ytick.color':INK,
}
plt.rcParams.update(STYLE)


def rows(name):
 with (DATA/name).open(newline='') as f:return list(csv.DictReader(f))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check_source():
 m=json.loads((ROOT/'provenance/FIGURE_INPUTS.json').read_text())
 for path,h in m.items():
  p=ROOT/path
  if not p.is_file() or digest(p)!=h:raise RuntimeError('Source mismatch: '+path)
 return m

def base(w,h):
 return plt.figure(figsize=(w,h),dpi=160)
def canvas(w,h):
 f=base(w,h);a=f.add_axes([0,0,1,1]);a.set_xlim(0,w*72);a.set_ylim(0,h*72);a.set_axis_off();return f,a

def text(ax,x,y,s,size=9.2,**kw):
 return ax.text(x,y,s,fontsize=size,ha=kw.pop('ha','left'),va=kw.pop('va','center'),**kw)
def box(ax,x,y,w,h,edge=GRAY,fill=WHITE,lw=.75,r=3):
 p=FancyBboxPatch((x,y),w,h,boxstyle=f'round,pad=0,rounding_size={r}',linewidth=lw,edgecolor=edge,facecolor=fill)
 ax.add_patch(p);return p

def arrow(ax,xy1,xy2,color=INK,lw=.9,head=7,style='-',**kw):
 p=FancyArrowPatch(xy1,xy2,arrowstyle='-|>',mutation_scale=head,linewidth=lw,color=color,linestyle=style,shrinkA=0,shrinkB=0,**kw)
 ax.add_patch(p);return p

def inspect_text(fig,name):
 fig.canvas.draw();r=fig.canvas.get_renderer();bad=[];small=[]
 for artist in fig.findobj(match=matplotlib.text.Text):
  if not artist.get_visible() or not artist.get_text():continue
  b=artist.get_window_extent(r)
  # Checking the actual canvas catches clipped labels after layout changes.
  if b.x0 < -.8 or b.y0 < -.8 or b.x1 > fig.bbox.width+.8 or b.y1 > fig.bbox.height+.8:
   bad.append({'text':artist.get_text(),'bounds_px':[round(v,2) for v in b.extents]})
  small.append(artist.get_fontsize())
 return {'component':name,'outside_text':bad,'minimum_font_pt':min(small) if small else None}

def save_component(fig,name,folder,reports):
 reports.append(inspect_text(fig,name))
 fig.savefig(folder/(name+'.pdf'),metadata={'Title':name,'Author':'Measurement-Geometry-Superadditivity','CreationDate':STAMP,'ModDate':STAMP,'Creator':'Python / Matplotlib'},transparent=False)
 fig.savefig(folder/(name+'.svg'),metadata={'Title':name,'Date':'2026-09-08','Creator':'Python / Matplotlib'},transparent=False)
 plt.close(fig)

def axes_tidy(ax,grid=False):
 ax.spines['top'].set_visible(False);ax.spines['right'].set_visible(False)
 ax.tick_params(direction='out',pad=3.0)
 if grid:ax.yaxis.grid(True,color=GRID,lw=.45,alpha=.65);ax.set_axisbelow(True)


def diagram1():
 f,ax=canvas(4.68,3.72)
 text(ax,1,257,'(a)',11,weight='bold')
 text(ax,22,257,'Encoding before random channel uses',10.2,weight='bold')
 text(ax,20,224,r'$\rho_{\mathrm{L}}$',13,ha='center')
 text(ax,28,204,'logical input',8.3,ha='center')
 arrow(ax,(38,225),(66,225),NAVY,1)
 box(ax,68,208,68,34,edge=NAVY,fill=LIGHT)
 text(ax,102,225,'Encode',10,ha='center')
 arrow(ax,(138,225),(169,225),NAVY,1)
 text(ax,153,239,r'$n$',9.0,ha='center')
 box(ax,172,207,153,36,edge=NAVY,fill=LIGHT)
 text(ax,248.5,231,r'$\mathcal{N}^{\otimes n}$',11,ha='center')
 text(ax,248.5,216,'independent channel uses',8.8,ha='center')
 # Dotted zoom guides are not physical feedback paths.
 ax.plot([180,50],[206,189],color=GRID,lw=.75,ls=(0,(2,2)))
 ax.plot([319,250],[206,189],color=GRID,lw=.75,ls=(0,(2,2)))
 box(ax,47,43,204,147,edge=GRAY,fill='#F7F9FA',lw=.65,r=4)
 text(ax,58,181,'One use',8.4,color=GRAY)
 text(ax,17,134,'qubit',8.5,ha='center')
 arrow(ax,(5,125),(57,125),NAVY,1.05)
 ax.plot([57,57],[125,163],color=NAVY,lw=1.05)
 ax.plot([57,57],[125,109],color=NAVY,lw=1.05)
 ax.add_patch(Circle((57,125),1.35,color=NAVY))
 text(ax,73,153,r'$1-p$',9.4,ha='center',color=NAVY)
 arrow(ax,(57,163),(102,163),NAVY,1.0)
 box(ax,102,150,98,26,edge=NAVY,fill=WHITE)
 text(ax,151,163,'intact qubit',9.6,ha='center')
 arrow(ax,(202,163),(267,163),NAVY,1.05)
 text(ax,72,101,r'$p$',10,ha='center',color=TEAL)
 arrow(ax,(57,109),(88,109),TEAL,1)
 box(ax,88,89,57,39,edge=TEAL,fill=WHITE)
 text(ax,116.5,115,'measure',9.3,ha='center')
 text(ax,116.5,100,r'$b\sim w$',9.3,ha='center')
 arrow(ax,(146,109),(168,109),TEAL,1)
 text(ax,157,120,r'$r$',9.4,ha='center',color=TEAL)
 box(ax,169,90,71,38,edge=TEAL,fill=WHITE)
 text(ax,204.5,116,'report',9.1,ha='center')
 text(ax,204.5,101,r'$s=r\oplus z$',9.5,ha='center')
 text(ax,204,77,r'$z\sim\mathrm{Bernoulli}(\epsilon)$',8.1,ha='center')
 text(ax,204,59,r'$r,z$ hidden',8.4,ha='center',color=GRAY)
 arrow(ax,(105,88),(105,68),GRAY,.8,head=6)
 ax.plot([101.5,108.5],[60,67],lw=.9,color=GRAY);ax.plot([101.5,108.5],[67,60],lw=.9,color=GRAY)
 text(ax,103.5,50,'discarded qubit',8.1,ha='center',color=GRAY)
 arrow(ax,(241,109),(267,109),TEAL,1.05)
 box(ax,269,84,67,97,edge=NAVY,fill=LIGHT,lw=.85)
 text(ax,302.5,169,'Receiver',9.5,ha='center',weight='bold')
 text(ax,302.5,151,'intact qubits',8.1,ha='center')
 text(ax,302.5,137,'+ records',8.7,ha='center')
 text(ax,302.5,122,r'mask, $b,s$',8.6,ha='center')
 text(ax,302.5,99,'all outcomes',8.0,ha='center',color=GRAY)
 text(ax,48,23,'No access to the discarded qubit or hidden signs.',8.7,color=GRAY)
 return f


def witness1(data,audit):
 f=base(2.35,3.72)
 f.text(.03,.955,'(b)',fontsize=11,weight='bold',va='center')
 f.text(.18,.955,'A concrete separation',fontsize=9.7,weight='bold',va='center')
 f.text(.62,.89,r'$\epsilon=0.10,\ p=0.70$',fontsize=9.1,ha='center')
 f.text(.62,.845,'Equal X, Y, Z probabilities',fontsize=8.3,ha='center')
 ax=f.add_axes([.26,.20,.70,.575])
 axes_tidy(ax,grid=True)
 y=np.array([float(x['value_plot']) for x in data])*1e5
 ax.vlines([0,1],[0,0],y,colors=[NAVY,TEAL],lw=1.8)
 ax.scatter([0],[y[0]],s=35,marker='o',facecolor=NAVY,edgecolor=WHITE,lw=.7,zorder=5,clip_on=False)
 ax.scatter([1],[y[1]],s=42,marker='D',facecolor=TEAL,edgecolor=WHITE,lw=.7,zorder=5)
 ax.annotate('0',xy=(0,0),xytext=(0,9),textcoords='offset points',ha='center',fontsize=9.5,color=NAVY)
 ax.annotate('7.48',xy=(1,y[1]),xytext=(0,9),textcoords='offset points',ha='center',fontsize=10,color=TEAL,weight='bold')
 ax.set_xlim(-.47,1.47);ax.set_ylim(0,9)
 ax.set_yticks([0,2,4,6,8]);ax.set_xticks([0,1])
 ax.set_xticklabels(['Best one-use\ninput\n$Q^{(1)}$','Eight-use\nconstruction / 8\n$I_8/8$'],fontsize=8.2,linespacing=1.45)
 ax.tick_params(axis='x',length=0,pad=8)
 ax.set_ylabel('Coherent information\nper physical use (bits)',fontsize=8.8,labelpad=7)
 ax.text(-.09,1.03,r'$\times10^{-5}$',transform=ax.transAxes,fontsize=9.3)
 audit['figure1']={'source':'figure1_comparison.csv','quantity':'coherent_information_bits_per_physical_use','x':[0,1],'source_values':[float(r['value_plot']) for r in data],'display_multiplier':1e5,'display_values':y.tolist(),'errorbars':False,'globally_optimized':['Q^(1)'],'constructive_only':['I_8/8'],'all_mask_terms_copied':True}
 return f


def header2():
 f,ax=canvas(7.08,.54)
 text(ax,5,29,r'Full span guarantees separation for every common error $0<\epsilon<1/2$',11,weight='bold')
 text(ax,5,11,r'Illustrative slice: equal Pauli weights, $T=I/3$',9.7,color=GRAY)
 return f


def region2(data,audit):
 f=base(7.08,3.53);ax=f.add_axes([.108,.19,.872,.772]);axes_tidy(ax)
 e=np.array([float(x['epsilon']) for x in data]);pc=np.array([float(x['p_cert']) for x in data]);pr=np.array([float(x['p_rep']) for x in data])
 interior=np.array([r['theorem_applies']=='True' for r in data])
 ax.fill_between(e,pc,pr,where=interior,color=TEAL,alpha=.20,linewidth=0,zorder=1)
 ax.plot(e,pc,color=NAVY,lw=.95,label=r'$p_{\mathrm{cert}}$: sufficient one-use-zero bound',zorder=3)
 ax.plot(e,pr,color=TEAL,lw=.95,ls=(0,(4.0,2.4)),label=r'$p_{\mathrm{rep}}$: strict repetition frontier',zorder=4)
 ax.set_xlim(0,.5);ax.set_ylim(.48,1.02);ax.set_xticks(np.arange(0,.51,.1));ax.set_yticks(np.arange(.5,1.01,.1))
 ax.set_xlabel(r'Reporting-error probability $\epsilon$',labelpad=7)
 ax.set_ylabel(r'Measurement probability $p$',labelpad=8)
 leg=ax.legend(loc='upper left',bbox_to_anchor=(.235,1.005),frameon=False,fontsize=9.1,handlelength=2.7,handletextpad=.65,labelspacing=.62,borderaxespad=0)
 ax.scatter([0,.5],[1,.5],s=31,facecolors=WHITE,edgecolors=NAVY,lw=1.0,zorder=6,clip_on=False)
 ax.annotate('No separation',xy=(0,1),xytext=(.018,.982),fontsize=8.4,ha='left',va='center',color=GRAY,
             arrowprops=dict(arrowstyle='-',lw=.65,color=GRAY,connectionstyle='arc3,rad=0'))
 ax.annotate('No separation',xy=(.5,.5),xytext=(.402,.55),fontsize=8.4,ha='left',va='center',color=GRAY,
             arrowprops=dict(arrowstyle='-',lw=.65,color=GRAY,shrinkA=2,shrinkB=5))
 idx=np.argmin(abs(e-.145));target=(float(e[idx]),float((pc[idx]+pr[idx])/2))
 ax.annotate('Certified separation:\n'+r'$Q^{(1)}=0<Q$',xy=target,xytext=(.022,.615),ha='left',va='center',fontsize=10,color=NAVY,linespacing=1.4,
             arrowprops=dict(arrowstyle='-',color=GRAY,lw=.8,shrinkA=6,shrinkB=1,connectionstyle='arc3,rad=-0.08'))
 audit['figure2']={'source':'figure2_pauli_guaranteed_region.csv','x_values':e.tolist(),'p_cert_values':pc.tolist(),'p_rep_values':pr.tolist(),'shade_mask':interior.tolist(),
   'lower_style':'solid','upper_style':'dashed','lower_status':'sufficient one-use-zero bound','upper_status':'strict repetition frontier','capacity_phase_labels':False,'witness_overlay':False,
   'endpoint_markers':{'epsilon':[0.,.5],'p':[1.,.5],'fill':'white','meaning':'limit, no separation'},'p_ylim':[.48,1.02]}
 return f


def width2(data,audit):
 f=base(2.40,1.71);ax=f.add_axes([.255,.23,.705,.68]);axes_tidy(ax)
 e=np.array([float(r['epsilon']) for r in data]);y=np.array([float(r['certified_width']) for r in data])*1e3
 ax.plot(e,y,color=TEAL,lw=1.05)
 ax.set_xlim(0,.5);ax.set_ylim(0,4);ax.set_xticks([0,.25,.5]);ax.set_xticklabels(['0','0.25','0.5'],fontsize=8.1);ax.set_yticks([0,2,4]);ax.tick_params(labelsize=8.1,length=2.5,pad=2)
 ax.set_ylabel('Certified interval width',fontsize=8.2,labelpad=4)
 ax.set_xlabel(r'$\epsilon$',fontsize=9,labelpad=2)
 ax.text(-.11,1.020,r'$\times10^{-3}$',transform=ax.transAxes,fontsize=8.5)
 audit['figure2']['inset']={'source':'certified_width','actual_values':[float(r['certified_width']) for r in data],
   'display_values':y.tolist(),'display_multiplier':1e3,'ylim':[0,4],'quantity':'measurement-probability interval width, not rate'}
 return f


def geometry3(data,audit):
 f,ax=canvas(7.08,1.93)
 text(ax,3,132,'(a)',11,weight='bold')
 text(ax,26,132,'One path from coplanar to full-span measurements',10.3,weight='bold')
 az=np.deg2rad(25);el=np.deg2rad(35)
 proj=np.array([[-np.sin(az),np.cos(az),0],[-np.sin(el)*np.cos(az),-np.sin(el)*np.sin(az),np.cos(el)]])
 depth=np.array([np.cos(el)*np.cos(az),np.cos(el)*np.sin(az),np.sin(el)])
 centers=[(91,69),(256,69),(421,69)];radius=37
 snapshots=[]
 for lf,center,label in zip(['0','1/16','1/4'],centers,[r'$\lambda=0$',r'$\lambda=1/16$',r'$\lambda=1/4$']):
  center=np.array(center);text(ax,center[0],112,label,10.5,ha='center')
  ax.add_patch(Circle(tuple(center),radius,facecolor='none',edgecolor=GRID,lw=.55))
  phi=np.linspace(0,2*np.pi,241);equator=np.array([np.cos(phi),np.sin(phi),np.zeros_like(phi)])
  eq=center[:,None]+radius*proj@equator
  ax.fill(eq[0],eq[1],facecolor=LIGHT,alpha=.45,zorder=0)
  ax.plot(eq[0],eq[1],color=GRID,lw=.65,ls=(0,(1,2)))
  code=np.array([[0,0,-1.08],[0,0,1.08]])
  cp=center[:,None]+radius*proj@code.T
  ax.plot(cp[0],cp[1],color=GRAY,lw=.75,ls=(0,(3,2)))
  rows=[r for r in data if r['lambda_exact']==lf]
  ends=[]
  # Same camera and radius in every snapshot. Only supplied axis coordinates vary.
  for r in sorted(rows,key=lambda r:float(np.array([float(r[c]) for c in ['nx','ny','nz']])@depth)):
   v=np.array([float(r[c]) for c in ['nx','ny','nz']]);coords=center[:,None]+radius*proj@np.array([-v,v]).T
   ax.plot(coords[0],coords[1],color=NAVY,lw=1.15,solid_capstyle='round')
   ax.scatter(coords[0],coords[1],s=10,facecolor=NAVY,edgecolor=WHITE,linewidths=.35,zorder=5)
   ends.append({'axis':int(r['axis']),'unit_vector':v.tolist(),'negative':(-v).tolist(),'projected_endpoints_pt':coords.T.tolist()})
  ax.scatter([center[0]],[center[1]],s=6,color=INK,zorder=7)
  text(ax,center[0],22,'coplanar' if lf=='0' else 'full span',9.4,ha='center',color=GRAY if lf=='0' else NAVY)
  snapshots.append({'lambda':lf,'center_pt':center.tolist(),'radius_pt':radius,'axes':sorted(ends,key=lambda z:z['axis'])})
 text(ax,255,5,r'Dashed vertical guide: $u=(0,0,1)$, not a measurement axis.',8.2,ha='center',color=GRAY)
 audit['figure3_geometry']={'source':'figure3_cone_geometry.csv','snapshot_count':3,'axis_count_per_snapshot':3,'common_projection_matrix':proj.tolist(),'azimuth_degrees':25,'elevation_degrees':35,'projection':'orthographic linear map','snapshots':snapshots,'endpoint_count_per_axis':2,'code_guide_counts_as_axis':False}
 return f


def gap3(data,audit):
 f=base(7.08,2.76);ax=f.add_axes([.112,.23,.868,.697]);axes_tidy(ax,grid=True)
 x=np.array([float(r['lambda_min']) for r in data]);y=np.array([float(r['gap']) for r in data]);lin=np.array([float(r['linear_asymptote']) for r in data])
 ax.plot(x,y,color=NAVY,lw=1.5,label='Exact frontier gap')
 ax.plot(x,lin,color=TEAL,lw=1.2,ls=(0,(4.5,2.5)),label=r'Small-$\lambda$ asymptote: $(18/289)\lambda$')
 ax.scatter([0],[0],s=22,color=NAVY,zorder=5,clip_on=False)
 ax.set_xlim(0,.25);ax.set_ylim(0,.020)
 ax.set_xticks([0,.05,.1,.15,.2,.25]);ax.set_xticklabels(['0','0.05','0.10','0.15','0.20','0.25'])
 ax.set_yticks([0,.005,.01,.015,.02]);ax.set_yticklabels(['0','0.005','0.010','0.015','0.020'])
 ax.set_xlabel(r'Weakest directional coverage $\lambda=\lambda_{\min}(T)$',labelpad=6)
 ax.set_ylabel(r'Threshold gap $p_{\mathrm{rep}}-p_1$',labelpad=7)
 ax.text(.024,.925,r'$\epsilon=0.10$; equal cone weights',transform=ax.transAxes,fontsize=9.6)
 ax.legend(loc='upper left',bbox_to_anchor=(.022,.81),frameon=False,fontsize=9.2,handlelength=2.65,labelspacing=.72,borderaxespad=0)
 f.text(.006,.958,'(b)',fontsize=11,weight='bold',va='center')
 audit['figure3_gap']={'source':'figure3_cone_gap.csv','lambda_values':x.tolist(),'gap_values':y.tolist(),'linear_asymptote_values':lin.tolist(),
  'fixed_error':'1/10','domain':[0,.25],'curve_status':'exact difference of one-use frontier and construction frontier',
  'asymptote_status':'analytical, not fitted','slope_exact':'18/289','axis_scales':['linear','linear'],'y_limits':[0,.020],'origin_marked':True,'witness_transferred_from_figure1':False}
 return f


def combine(name,w,h,placements,panels,out):
 """Placement tuple: (component, x_in, top_y_in, width_in, height_in)."""
 d=fitz.open();page=d.new_page(width=w*72,height=h*72)
 svg=ET.Element('{%s}svg'%SVG_NS,{'width':f'{w*72:g}pt','height':f'{h*72:g}pt','viewBox':f'0 0 {w*72:g} {h*72:g}','version':'1.1'})
 for comp,x,y,pw,ph in placements:
  doc=fitz.open(panels/(comp+'.pdf'));page.show_pdf_page(fitz.Rect(x*72,y*72,(x+pw)*72,(y+ph)*72),doc,0);doc.close()
  s=ET.parse(panels/(comp+'.svg')).getroot();orig=[float(v) for v in s.attrib['viewBox'].split()];sx=pw*72/orig[2];sy=ph*72/orig[3]
  # Namespace all defs/clip ids so independent charts do not collide on assembly.
  mapping={el.attrib['id']:f'{comp}_{el.attrib["id"]}' for el in s.iter() if 'id' in el.attrib}
  for el in s.iter():
   for k,v in list(el.attrib.items()):
    if k=='id':el.set(k,mapping[v]);continue
    v=re.sub(r'url\(#([^)]+)\)',lambda m:'url(#'+mapping.get(m[1],m[1])+')',v)
    if v.startswith('#') and v[1:] in mapping:v='#'+mapping[v[1:]]
    el.set(k,v)
  g=ET.SubElement(svg,'{%s}g'%SVG_NS,{'transform':f'translate({x*72:g} {y*72:g}) scale({sx:g} {sy:g})','id':'component_'+comp})
  for child in list(s):
   if child.tag.endswith('metadata'):continue
   g.append(child)
 d.set_metadata({'title':name,'author':'Measurement-Geometry-Superadditivity','creator':'Python reproducible figure rendering','creationDate':'D:20260908000000Z','modDate':'D:20260908000000Z'})
 d.save(out/(name+'.pdf'),garbage=4,deflate=True,no_new_id=True);d.close()
 ET.ElementTree(svg).write(out/(name+'.svg'),encoding='utf-8',xml_declaration=True)
 with fitz.open(out/(name+'.pdf')) as doc:
  doc[0].get_pixmap(dpi=300,alpha=False).save(out/(name+'.png'))
 with Image.open(out/(name+'.png')) as im:
  width=1200
  im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS).save(out/(name+'_preview.png'))
 return {'name':name,'width_inches':w,'height_inches':h,'placements':placements,'formats':['pdf','svg','png'],'png_dpi':300}


def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'build/figures');args=ap.parse_args()
 check_source();out=args.output;out.mkdir(parents=True,exist_ok=True);panels=out/'panels';panels.mkdir(exist_ok=True)
 d1=rows('figure1_comparison.csv');d2=rows('figure2_pauli_guaranteed_region.csv');d3=rows('figure3_cone_gap.csv');geom=rows('figure3_cone_geometry.csv')
 audit={};reports=[]
 builders=[('figure1a_channel',lambda:diagram1()),('figure1b_witness',lambda:witness1(d1,audit)),
  ('figure2_header',lambda:header2()),('figure2_main',lambda:region2(d2,audit)),('figure2_width',lambda:width2(d2,audit)),
  ('figure3a_geometry',lambda:geometry3(geom,audit)),('figure3b_gap',lambda:gap3(d3,audit))]
 for name,fn in builders:save_component(fn(),name,panels,reports)
 composites=[]
 composites.append(combine('figure_01_channel_and_witness',7.08,3.72,[('figure1a_channel',0,0,4.68,3.72),('figure1b_witness',4.73,0,2.35,3.72)],panels,out))
 composites.append(combine('figure_02_guaranteed_region',7.08,4.07,[('figure2_header',0,0,7.08,.54),('figure2_main',0,.54,7.08,3.53),('figure2_width',4.56,1.13,2.40,1.71)],panels,out))
 composites.append(combine('figure_03_coplanar_limit',7.08,4.69,[('figure3a_geometry',0,0,7.08,1.93),('figure3b_gap',0,1.93,7.08,2.76)],panels,out))
 audit['schematic_contract']=json.loads((SOURCE/'FIGURE_CONTRACT.json').read_text())['figure_1']['schematic']
 audit['source_provenance']={'spec_manifest_sha256':digest(ROOT/'provenance/FIGURE_INPUTS.json'),'data_hashes':{p.name:digest(p) for p in sorted(DATA.iterdir()) if p.is_file()},'no_scientific_data_modified':True}
 audit['layout']={'units':'inches at intended final figure size','composites':composites,'font_family':'DejaVu Sans','palette':{'navy':NAVY,'teal':TEAL,'neutral':GRAY},'scalar_figures':'each numerical chart generated separately; vector composition only','text_extent_checks':reports}
 (out/'RENDER_RECORD.json').write_text(json.dumps(audit,indent=2)+'\n')
 print(json.dumps({'figures':len(composites),'component_figures':len(builders),'outside_text':[r for r in reports if r['outside_text']]},indent=2))
if __name__=='__main__':main()
