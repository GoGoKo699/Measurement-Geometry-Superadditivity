#!/usr/bin/env python3
"""Three-page publication-size figure review; vectors are kept as vectors."""
from pathlib import Path
import argparse,io
import fitz
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
import matplotlib.font_manager as fm

ROOT=Path(__file__).resolve().parents[2]
CAPTIONS=[
('Figure 1. The channel and a concrete collective separation',
'''<b>(a)</b> An unknown logical input is encoded before independent channel uses. A qubit arrives intact with probability 1 − p; otherwise it is projectively measured along an axis b drawn from w and becomes inaccessible. The receiver gets the correct mask and axis label and the reported sign s = r ⊕ z, where z is an independent acquisition/report error with probability ε. The true sign r, error variable z, and measured qubit are unavailable. Every outcome is included. <b>(b)</b> For equal Pauli-axis weights, ε = 0.10 and p = 0.70, the globally optimized one-use coherent information is exactly zero: p exceeds its threshold 59/86. The balanced repetition input formed from the two eigenstates of (X + Y + Z)/√3 has I<sub>8</sub>/8 &gt; 7.47 × 10<super>−5</super> bits per physical use. This is one certified constructive value, not the optimal eight-use value or exact capacity. Positive block coherent information has an asymptotic rate interpretation through outer coding, not a demonstrated eight-qubit decoding fidelity. Numerical enclosures are smaller than the markers and are not statistical error bars.'''),
('Figure 2. A certified region across reporting noise',
'''The theorem gives a nonempty separation interval for every finite full-span measurement ensemble and common 0 &lt; ε &lt; 1/2. The illustrated slice has equal Pauli-axis weights, T = I/3 and λ = 1/3. Put a = (1 − 2ε)<super>2</super>, c = 1 − a, L = c/√(1 − a/3), and d<sub>ε</sub> = 3ca/35. The solid curve is the sufficient one-use-zero bound p<sub>cert</sub> = [1 + L + d<sub>ε</sub>/3]<super>−1</super>; the dashed curve is the repetition construction’s strict frontier p<sub>rep</sub> = (1 + L)<super>−1</super>. Only p<sub>cert</sub> ≤ p &lt; p<sub>rep</sub> at interior errors is shaded. The upper equality is not claimed; neither curve is an exact capacity boundary, and unshaded regions remain unclassified. Open endpoints mark perfect and fully random record limits, where there is no separation. The inset shows the interval width in p, not a communication rate, without thickening the strip. Figure 1 uses a sharper one-use threshold at ε = 0.1: its p = 0.7 witness lies below this conservative strip. These are evaluations of a proved analytical bound, not a simulation sweep.'''),
('Figure 3. The approach to coplanarity',
'''<b>(a)</b> Three equally probable axes are n<sub>j</sub> = (√(1 − λ) cos(2πj/3), √(1 − λ) sin(2πj/3), √λ), j = 0, 1, 2, at λ = 0, 1/16, 1/4. One fixed orthographic camera and scale is used. Each solid line includes both signs of one measurement axis. The dashed vertical is the axial coding-direction guide, not an additional measurement axis; the faint dotted ellipse indicates the reference plane. <b>(b)</b> At ε = 0.10, the solid curve is the exact difference between the one-use positivity frontier p<sub>1</sub> = (1 − aλ)/(1 − aλ + c) and repetition frontier p<sub>rep</sub> = √(1 − aλ)/[√(1 − aλ) + c], within 0 ≤ λ ≤ 1/4, where a = 0.64 and c = 0.36. The dashed line is the derived small-λ asymptote (18/289)λ, not a fit. Equality at λ = 0 concerns these frontiers, not an all-code no-capacity claim. A nonzero gap need not supply a uniformly short block or useful rate. These cone ensembles differ from Figure 1’s Pauli ensemble; its finite-code value is not transferred here.''')]
FILES=['figure_01_channel_and_witness','figure_02_guaranteed_region','figure_03_coplanar_limit']

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--figures',type=Path,default=ROOT/'build/figures');ap.add_argument('--output',type=Path,default=ROOT/'build/figures/three_figure_review.pdf');args=ap.parse_args()
 for face,weight in [('Review','normal'),('ReviewBold','bold')]:
  path=fm.findfont(fm.FontProperties(family='DejaVu Sans',weight=weight),fallback_to_default=False)
  pdfmetrics.registerFont(TTFont(face,path))
 pdfmetrics.registerFontFamily('Review',normal='Review',bold='ReviewBold')
 style=ParagraphStyle('caption',fontName='Review',fontSize=9.5,leading=14.0,spaceAfter=6)
 stream=io.BytesIO();c=canvas.Canvas(stream,pagesize=A4,invariant=1)
 pw,ph=A4;placements=[]
 for i,((title,caption),name) in enumerate(zip(CAPTIONS,FILES),1):
  c.setFont('Review',8.7);c.drawString(43,ph-29,'MEASUREMENT-GEOMETRY-SUPERADDITIVITY  |  FIGURE REVIEW v1')
  c.setFont('ReviewBold',14);c.drawString(43,ph-53,title)
  with fitz.open(args.figures/(name+'.pdf')) as d:w,h=d[0].rect.width,d[0].rect.height
  x=(pw-w)/2;top=80;placements.append((name,(x,top,x+w,top+h)))
  para=Paragraph(caption,style);cw,ch=para.wrap(pw-86,ph)
  bottom=ph-top-h-19-ch
  if bottom<75:raise RuntimeError('Caption does not fit the review page')
  para.drawOn(c,43,bottom)
  c.setFont('Review',8);c.drawString(43,40,'Rendered from frozen figure inputs; no scientific changes. Visual approval remains pending.')
  c.drawRightString(pw-43,24,str(i));c.showPage()
 c.save();base=fitz.open(stream=stream.getvalue(),filetype='pdf')
 for i,(name,rect) in enumerate(placements):
  with fitz.open(args.figures/(name+'.pdf')) as d:base[i].show_pdf_page(fitz.Rect(rect),d,0,overlay=True)
 base.set_metadata({'title':'Measurement geometry: three-figure review v1','author':'Measurement-Geometry-Superadditivity','creator':'Python, ReportLab and PyMuPDF','creationDate':'D:20260908000000Z','modDate':'D:20260908000000Z'})
 base.save(args.output,garbage=4,deflate=True,no_new_id=True);base.close();print(args.output)
if __name__=='__main__':main()
