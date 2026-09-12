#!/usr/bin/env python3
"""Build the reader website locally. Never publishes or alters scientific inputs.

Requires Pandoc and Beautiful Soup; uses native MathML, local CSS/JS/search.
Canonical technical pages are rendered from their source files, not rewritten.
"""
from __future__ import annotations
import argparse,hashlib,html,json,os,re,shutil,subprocess,sys
from pathlib import Path
from urllib.parse import urlsplit,urlunsplit,unquote
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
WEB=ROOT/'website'
sys.path.insert(0,str(WEB))
from learning_bridge import METADATA, expand_background, load_bridge, validate_routes
# Download inventory only. The operative root license defines reuse scope.
REUSE_DOWNLOADS=(
 'LICENSE.md','LICENSES/MIT.txt','LICENSES/CC-BY-4.0.txt',
 'LICENSES/DejaVu.txt','LICENSES/STIX.txt','THIRD_PARTY_NOTICES.md',
 'CITATION.cff',
)
INTEGRITY_DOWNLOADS=('integrity/check_scientific.py','integrity/SCIENTIFIC_FILES.json')
FIGURES=[
 ('figure_01_channel_and_witness','The channel and a concrete separation','Figure 1: hidden true outcomes stay inside the channel; the eight-use per-use value is positive while optimized single-use coherent information is zero.',['figure1_comparison.csv','figure1_all_masks_not_for_display.csv','figure1_original_witness140.json'],['m01','m05'],['p01','p13']),
 ('figure_02_guaranteed_region','The geometric guarantee across reporting noise','Figure 2: equal-Pauli slice of the theorem. A solid sufficient lower bound and a dashed strict repetition frontier enclose a narrow certified region; the inset displays its width.',['figure2_pauli_guaranteed_region.csv','cross_figure_witness_bound_check.json'],['m03','m04'],['p08','p10']),
 ('figure_03_coplanar_limit','The approach to a plane','Figure 3: three cone geometries with the same camera and scale; below, the frontier gap approaches zero with its derived small-lambda tangent, not a fitted line.',['figure3_cone_geometry.csv','figure3_cone_gap.csv'],['m06'],['p11','p12'])]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(ok,message):
 if not ok:raise ValueError(message)
def load(p):return json.loads(p.read_text())
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def digest_string(s):return hashlib.sha256(s.encode()).hexdigest()
def prepare_markdown(text):
 # A blank line keeps an empty explicit anchor from swallowing the next heading
 # in Pandoc. This changes only rendering input, never the source or its math.
 return re.sub(r'(?m)^(<a (?:id|name)="[^"]+"></a>)\n(?=#{1,6}\s)',r'\1\n\n',text)

def pandoc(text):
 p=subprocess.run(['pandoc','--from=markdown+tex_math_dollars+raw_html','--to=html5','--mathml','--wrap=none'],input=prepare_markdown(text),capture_output=True,text=True,check=False)
 require(p.returncode==0,'Pandoc failed: '+p.stderr)
 require(not p.stderr.strip(),'Pandoc warning requires review: '+p.stderr)
 return p.stdout

def verify_baseline():
 """Check the current protected sources directly, without replaying old trees."""
 sys.path.insert(0,str(ROOT))
 from integrity.check_scientific import check
 return check(ROOT)


def theme_svgs(out,palette):
 target=out/'assets/theme';target.mkdir(parents=True,exist_ok=True);m=palette['svg_mapping'];records=[]
 approved=ROOT/'figures/approved'
 for src in sorted(approved.rglob('*.svg')):
  text=src.read_text();matches=[]
  def change(match):
   c=match.group().lower();new=m.get(c,c)
   matches.append((match.start(),c,new))
   return new if c in m else match.group()
  themed=re.sub(r'#[0-9a-fA-F]{6}\b',change,text)
  # Normalize only declared color values. Any other character change fails.
  def normalize(s):
   return re.sub(r'#[0-9a-fA-F]{6}\b',lambda q:'@COLOR@' if q.group().lower() in set(m)|set(m.values()) else q.group(),s)
  require(normalize(themed)==normalize(text),'Noncolor SVG content changed')
  p=target/src.relative_to(approved);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(themed)
  records.append({'source':str(src.relative_to(ROOT)),'source_sha256':sha(src),'output':str(p.relative_to(out)),'output_sha256':sha(p),'changed_color_occurrences':sum(a!=b for _,a,b in matches),'only_declared_colors_changed':True})
 return records

def rewrite_links(fragment,source,page_map):
 soup=BeautifulSoup(fragment,'html.parser')
 for tag in soup.find_all(['a','img']):
  key='href' if tag.name=='a' else 'src';ref=tag.get(key)
  if not ref:continue
  u=urlsplit(ref)
  if u.scheme or u.netloc or ref.startswith('#'):continue
  dest=(source.parent/unquote(u.path)).resolve()
  require(dest.is_relative_to(ROOT),'Source link escapes project: '+ref)
  rel=dest.relative_to(ROOT).as_posix()
  path=page_map.get(rel,'files/'+rel)
  tag[key]=urlunsplit(('', '',path,u.query,u.fragment))
 return str(soup)

def claim_table():
 claims=load(ROOT/'provenance/CLAIM_COVERAGE.json')['claims'];s='<table><thead><tr><th>Claim</th><th>Exact statement and proof</th><th>Role</th></tr></thead><tbody>'
 for c in claims:
  anchors=c['canonical_proof_sections'];links=' · '.join(f'<a href="proof.html#{x.lower()}">{x}</a>' for x in anchors)
  s+=f'<tr><td><strong>{c["id"]}</strong></td><td><a href="model.html#{c["canonical_model_anchor"]}">Model statement</a><br>{links}</td><td>{html.escape(c["role"])}</td></tr>'
 return s+'</tbody></table>'

def checker_table():
 rows=[('Canonical rational cover','certificates/common_noise_compact_certificate.json'),('Integer interval verifier','verification/integer/certify_all_noise.py'),('mpmath interval verifier','verification/mpmath/cross_backend.py'),('Independent Decimal verifier','verification/decimal/verify_certificate.py'),('Recorded integer result','evidence/reference/integer224.json'),('Recorded mpmath result','evidence/reference/mpmath85.json'),('Recorded Decimal result','evidence/reference/decimal130.json')]
 s='<table><thead><tr><th>Role</th><th>Local source or recorded output</th></tr></thead><tbody>'
 for title,p in rows:
  require((ROOT/p).is_file(),'Resource absent: '+p)
  s+=f'<tr><td>{title}</td><td><a href="files/{p}"><code>{p}</code></a></td></tr>'
 return s+'</tbody></table>'

def atlas():
 text=(ROOT/'figures/CAPTIONS.md').read_text();items=[]
 for i,(stem,title,alt,inputs,models,proofs) in enumerate(FIGURES,1):
  match=re.search(rf'## Figure {i}\. [^\n]+\n(.*?)(?=\n## |\Z)',text,re.S);require(match is not None,'Missing caption')
  caption=pandoc(match.group(1).strip())
  sourceimg=ROOT/'figures/approved'/f'{stem}.svg';svg=ET.parse(sourceimg).getroot()
  dims=svg.get('viewBox','0 0 720 400').split();ratio=f'{dims[2]}/{dims[3]}'
  pic=f'<img id="fig-{i}" src="assets/theme/{stem}.svg" data-themed="assets/theme/{stem}.svg" data-original="files/figures/approved/{stem}.svg" alt="{html.escape(alt)}" style="aspect-ratio:{ratio}" loading="eager">'
  downloads=''.join(f'<a href="files/figures/approved/{stem}.{ext}">Approved {ext.upper()}</a>' for ext in ('pdf','svg','png'))
  downloads+=f'<a href="assets/theme/{stem}.svg">Accepted-palette SVG</a>'
  data=' · '.join(f'<a href="files/data/figures/{p}">{html.escape(p)}</a>' for p in inputs)
  proofs_links=' · '.join(f'<a href="model.html#{p}">{p.upper()}</a>'for p in models)+' · '+' · '.join(f'<a href="proof.html#{p}">{p.upper()}</a>'for p in proofs)
  items.append(f'<section class="figure-atlas-item"><h2 id="figure-{i}">Figure {i}. {title}</h2><div class="figure-image-wrap">{pic}</div><div class="figure-controls"><button type="button" data-figure-toggle="fig-{i}" aria-pressed="false">Show approved colors</button><span id="fig-{i}-status" class="figure-status" aria-live="polite">Accepted figure palette; protected originals remain available.</span></div><div class="asset-links">{downloads}</div><p class="data-line">Canonical sources: {proofs_links}. <a href="files/figures/CAPTIONS.md">Unchanged caption source</a>.</p><div class="figure-caption">{caption}</div><p class="data-line">Numerical inputs: {data}</p></section>')
 return '\n'.join(items)

def palette_grid(palette):
 return '<div class="swatch-grid">'+''.join(f'<div class="swatch"><div class="swatch-color" style="background:{palette["roles"][role]}"></div><div class="swatch-desc"><strong>{name}</strong><code>{palette["roles"][role]}</code><br>{purpose}</div></div>' for role,name,purpose in [('indigo','Indigo','Primary structure and bound'),('rust','Terracotta','Secondary plotted contrast'),('sage','Sage','Quiet supporting surfaces'),('yellow','Ochre yellow','Accents with dark text'),('paper','Warm paper','Reading surface'),('ink','Blue-black','Text and mathematical labels')])+'</div>'

def decorate(fragment):
 soup=BeautifulSoup(fragment,'html.parser')
 first=soup.find('h1');title=first.get_text(' ',strip=True) if first else ''
 if first:first.decompose()
 toc=[]
 for math in list(soup.find_all('math')):
  wrap=soup.new_tag('span');wrap['class']='math display' if math.get('display')=='block' else 'math inline';math.wrap(wrap)
  if math.get('display')=='block':wrap['tabindex']='0';wrap['role']='region';wrap['aria-label']='Mathematical expression; scroll horizontally if needed'
 for n,h in enumerate(soup.find_all(['h2','h3'])):
  if not h.get('id'):h['id']='section-'+str(n+1)
  title_h=h.get_text(' ',strip=True)
  if h.name=='h2':toc.append((h['id'],title_h))
  a=soup.new_tag('a',href='#'+h['id']);a['class']='section-anchor';a['aria-label']='Link to '+title_h;a.string='§';h.append(a)
 for table in list(soup.find_all('table')):
  wrap=soup.new_tag('div');wrap['class']='table-scroll';wrap['tabindex']='0';wrap['role']='region';wrap['aria-label']='Horizontally scrollable data table';table.wrap(wrap)
 return title,str(soup),toc

def site_html(page,body,title,toc,config):
 group=None;links=[]
 for p in config['pages']:
  if p['group']!=group:group=p['group'];links.append(f'<div class="nav-label">{html.escape(group)}</div>')
  current=' aria-current="page"' if p['slug']==page['slug'] else ''
  links.append(f'<a class="nav-link" href="{p["slug"]}.html"{current}>{html.escape(p["title"])}</a>')
 toc_html=''.join(f'<a href="#{html.escape(i)}">{html.escape(t)}</a>' for i,t in toc)
 source=f'files/{page["source"]}'
 canonical='<p class="source-note">Canonical scientific source. <a href="status.html">Current project status</a>.</p>' if page.get('canonical') else ''
 previous=next((p for p in config['pages'] if p['slug']==page.get('previous')),None)
 nextpage=next((p for p in config['pages'] if p['slug']==page.get('next')),None)
 next_html=f'<a class="next-link" href="{nextpage["slug"]}.html"><small>Continue reading</small>{html.escape(nextpage["title"])}</a>' if nextpage else '<a class="next-link" href="index.html"><small>Return to</small>The project</a>'
 if previous:next_html=f'<p><a href="{previous["slug"]}.html" rel="prev">Previous: {html.escape(previous["title"])}</a></p>'+next_html
 if page['slug']=='index':
  soup=BeautifulSoup(body,'html.parser');first=soup.find('p')
  if first:first['class']='lead'
  h2=soup.find('h2')
  img='<figure class="home-figure"><a href="figures.html#figure-1"><img src="assets/theme/figure_01_channel_and_witness.svg" alt="The noisy-record channel and the retained eight-use separation" width="900" height="450"></a><figcaption>One channel, every outcome retained. <a href="figures.html#figure-1">Read Figure 1 and inspect its source.</a> <span class="review-label">Accepted figure palette</span></figcaption></figure>'
  if h2:h2.insert_before(BeautifulSoup(img,'html.parser'))
  body=str(soup)
 return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><meta name="color-scheme" content="light"><meta name="description" content="Measurement geometry, noisy classical records, and a geometric guarantee of coherent-information superadditivity. Scientific source, proof, figures, and reproducibility."><title>{html.escape(page['title'])} | Measurement Geometry</title><link rel="stylesheet" href="assets/style.css"><script src="assets/search-index.js" defer></script><script src="assets/site.js" defer></script></head>
<body><noscript><style>.search-open,.menu-open,.figure-controls button{{display:none!important}}@media(max-width:780px){{.sidebar{{display:block!important;position:static;width:100%;max-height:none;box-shadow:none;columns:2}}.sidebar a,.nav-label{{break-inside:avoid}}.nav-note{{column-span:all}}}}</style></noscript><a class="skip" href="#main">Skip to content</a><header class="topbar"><a href="index.html" class="brand"><span class="brand-mark" aria-hidden="true"></span><span><strong>Measurement Geometry</strong><small>Coherent-information superadditivity</small></span></a><div class="top-actions"><a href="materials.html">Source materials</a><a href="{config['repository']}" rel="noreferrer">GitHub</a><button class="search-open" type="button" aria-haspopup="dialog">Search <kbd>/</kbd></button><button class="menu-open" type="button" aria-expanded="false" aria-controls="site-navigation">Menu</button></div></header>
<div class="shell"><nav id="site-navigation" class="sidebar" aria-label="Project navigation">{''.join(links)}<p class="nav-note">Local reading edition.</p></nav><main id="main" class="content {'home' if page['slug']=='index' else ''}"><div class="eyebrow">{html.escape(page['group'])}</div><h1>{html.escape(title or page['title'])}</h1><div class="page-meta"><a href="{source}">Read source Markdown</a><a href="status.html">Scope and status</a></div>{canonical}<article class="document">{body}</article><footer class="article-footer">{next_html}<p class="fineprint">Canonical sources and evidence remain available directly. The accepted figure palette does not replace the protected original exports.<br><a href="references.html">References</a> · <a href="visual-design.html">Visual design</a> · <a href="files/BUILD_RECORD.json">Build record</a><br><a href="files/LICENSE.md">License scope</a> · <a href="files/CITATION.cff">Citation</a> · <a href="files/THIRD_PARTY_NOTICES.md">Third-party notices</a></p></footer></main><aside class="toc" aria-label="On this page"><div class="toc-label">On this page</div>{toc_html}</aside></div>
<dialog class="search-dialog" aria-labelledby="search-heading"><div class="search-heading"><h2 id="search-heading">Search the project</h2><button class="search-close" aria-label="Close search" type="button">Close</button></div><label class="visually-hidden" for="search-input">Words or quantities</label><input id="search-input" class="search-input" type="search" placeholder="Try: coplanar, eight-use, certificate" autocomplete="off"><p class="search-message" aria-live="polite">Search the explanations, proof sections, and figure captions.</p><ul class="search-results"></ul></dialog><noscript><p>JavaScript is disabled. Every page, equation, figure and download remains available through the navigation; search and color switching are optional enhancements.</p></noscript></body></html>'''

def build(out):
 out=out.resolve();require(out.is_relative_to(ROOT/'build'),'Output must be under this checkout\'s ignored build/ directory')
 require(not out.exists(),'Use a fresh output directory: '+str(out));out.mkdir(parents=True)
 checked=verify_baseline();config=load(WEB/'site.json');palette=load(WEB/'palette.json')
 validate_routes(config);bridge=load_bridge()
 page_map={p['source']:p['slug']+'.html' for p in config['pages']};page_map.update({'README.md':'index.html','STATUS.md':'status.html'})
 shutil.copytree(WEB/'assets',out/'assets')
 # Explicit allowlist: scientific sources, current reader sources and reuse terms.
 baseline=load(ROOT/'BASELINE_MANIFEST.json')['files'];sources=set(baseline)|{'BASELINE_MANIFEST.json'}
 sources|=set(load(ROOT/'integrity/SCIENTIFIC_FILES.json')['files'])
 sources|={p['source'] for p in config['pages']}
 sources|={'WEBSITE.md','website/palette.json',METADATA,'website/site.json',
  'website/editorial_map.json','website/learning_bridge.py'}
 sources|=set(REUSE_DOWNLOADS)
 sources|=set(INTEGRITY_DOWNLOADS)
 sources|={'CONTRIBUTING.md','website/requirements.txt','website/requirements-browser.txt'}
 for rel in sorted(sources):
  require((ROOT/rel).is_file(),'Missing source: '+rel)
  target=out/'files'/rel;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,target)
 theme=theme_svgs(out,palette);search=[];page_records=[]
 for page in config['pages']:
  src=ROOT/page['source'];text=expand_background(src.read_text(),page['source'],bridge)
  frag=rewrite_links(pandoc(text),src,page_map)
  for key,value in [('<!-- SITE:CLAIM_TABLE -->',claim_table()),('<!-- SITE:CHECKER_TABLE -->',checker_table()),('<!-- SITE:FIGURE_ATLAS -->',atlas()),('<!-- SITE:PALETTE -->',palette_grid(palette)),('<!-- SITE:FIGURE_COMPARISON -->','<div class="compare-grid"><figure><img src="files/figures/approved/figure_02_guaranteed_region.svg" alt="Figure 2 in its approved original colors"><figcaption>Approved v1 colors</figcaption></figure><figure><img src="assets/theme/figure_02_guaranteed_region.svg" alt="The identical Figure 2 geometry in the Accepted figure palette"><figcaption>Accepted figure palette</figcaption></figure></div>')]:
   frag=frag.replace('<p>'+key+'</p>',value).replace(key,value)
  require('<!-- SITE:' not in frag,'Unexpanded reader content marker: '+page['slug'])
  title,body,toc=decorate(frag)
  target=out/(page['slug']+'.html');target.write_text(site_html(page,body,title,toc,config))
  parsed=BeautifulSoup(body,'html.parser')
  search.append({'title':title or page['title'],'url':target.name,'text':parsed.get_text(' ',strip=True)[:450]})
  for h2 in parsed.find_all('h2'):
   snippets=[]
   for nxt in h2.next_siblings:
    if getattr(nxt,'name',None)=='h2':break
    if hasattr(nxt,'get_text'):snippets.append(nxt.get_text(' ',strip=True))
   search.append({'title':page['title']+' / '+h2.get_text(' ',strip=True).rstrip('§').strip(),'url':target.name+'#'+h2['id'],'text':' '.join(snippets)[:4000]})
  page_records.append({'page':target.name,'source':page['source'],'source_sha256':sha(src),'canonical_source_rendered':page.get('canonical',False),'heading_count':len(toc),'mathml_count':len(parsed.find_all('math'))})
 (out/'assets/search-index.js').write_text('window.PROJECT_SEARCH = '+json.dumps(search,ensure_ascii=False).replace('</','<\\/')+';\n')
 record={'site_version':'reader-site-v1','date':config['website_date'],'learning_bridge':{'source':METADATA,'sha256':sha(ROOT/METADATA),'tutorial_version':bridge['source']['version'],'scope':'editorial learning map, not a proof certificate'},'local_reading_edition':True,'public_deployment_performed':False,'canonical_materials':checked,'pages':page_records,'themed_svgs':theme,'build_dependencies':{'pandoc':subprocess.run(['pandoc','--version'],capture_output=True,text=True).stdout.splitlines()[0]},'rendering':'native MathML; local CSS/JS/search; no CDN requests','new_scientific_claims':False,'new_proof_or_numerical_audit':False,'palette_source':'website/palette.json'}
 record['reuse_source_downloads']=[{'source':rel,'download':'files/'+rel,'sha256':sha(ROOT/rel)} for rel in REUSE_DOWNLOADS]
 record['integrity_source_downloads']=[{'source':rel,'download':'files/'+rel,'sha256':sha(ROOT/rel)} for rel in INTEGRITY_DOWNLOADS]
 dump(out/'files/BUILD_RECORD.json',record)
 (out/'START_HERE.txt').write_text('Open index.html in a modern browser, or run: python -m http.server 8000 --bind 127.0.0.1\nThis is a local reading artifact, not a deployed website.\n')
 print(json.dumps({'pages':len(page_records),'themed_svg_files':len(theme),'mathml_expressions':sum(p['mathml_count'] for p in page_records),'baseline_preservation':checked,'output':str(out)},indent=2))
 return record

if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'build/project-site');a=ap.parse_args();build(a.output)
