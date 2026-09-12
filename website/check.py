#!/usr/bin/env python3
"""Check generated pages, local links, source identity and accessible colors.

This verifies website structure and preservation, not new scientific claims.
External links are listed but not fetched; publishing remains disabled.
"""
from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
import argparse,json,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'website'))
from build import REUSE_DOWNLOADS,verify_baseline,require,load,dump,sha
from learning_bridge import METADATA, load_bridge, validate_routes

def luminance(color):
 rgb=[int(color[i:i+2],16)/255 for i in (1,3,5)]
 values=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in rgb]
 return sum(w*v for w,v in zip((.2126,.7152,.0722),values))
def contrast(a,b):
 l1,l2=sorted((luminance(a),luminance(b)));return (l2+.05)/(l1+.05)

def check_reuse_downloads(site,record):
 rows=record.get('reuse_source_downloads',[])
 require([row.get('source') for row in rows]==list(REUSE_DOWNLOADS),'License/citation download inventory mismatch')
 for row in rows:
  rel=row['source'];source=ROOT/rel;download=site/'files'/rel
  require(row.get('download')=='files/'+rel,'License/citation download path mismatch: '+rel)
  require(source.is_file() and download.is_file(),'License/citation download missing: '+rel)
  require(source.read_bytes()==download.read_bytes(),'License/citation download byte mismatch: '+rel)
  require(row.get('sha256')==sha(source),'License/citation download hash mismatch: '+rel)
 return rows

def check(site):
 site=site.resolve();pres=verify_baseline();config=load(ROOT/'website/site.json');palette=load(ROOT/'website/palette.json');seen={};links=0;math=0;missing=[];outside=[];sources=[]
 validate_routes(config);bridge=load_bridge()
 files=list(site.rglob('*.html'));require({p.relative_to(site).as_posix() for p in files}=={p['slug']+'.html' for p in config['pages']},'Missing or unexpected HTML route')
 for p in files:
  soup=BeautifulSoup(p.read_text(),'html.parser');seen[p]=soup
  require(soup.html.get('lang')=='en','Missing language')
  require(len(soup.find_all('h1'))==1,'Expected one H1: '+p.name)
  require(soup.title and 'Measurement Geometry' in soup.title.get_text(),'Missing title')
  require(soup.select_one('.skip[href="#main"]') and soup.select_one('main#main'),'Missing skip route')
  require(soup.select_one('nav[aria-label="Project navigation"]'),'Missing navigation')
  require(len(soup.select('a[aria-current="page"]'))==1,'Bad current-page state')
  for rel in ('LICENSE.md','CITATION.cff','THIRD_PARTY_NOTICES.md'):
   require(soup.select_one(f'footer a[href="files/{rel}"]'),'Missing license/citation footer link: '+rel)
  require(not soup.find('script',src=re.compile('^https?:')),'External script')
  require(not soup.find('link',href=re.compile('^https?:')),'External stylesheet/font')
  require('{{' not in soup.get_text() and '<!-- SITE:' not in p.read_text(),'Unresolved content token')
  for image in soup.find_all('img'):require(bool(image.get('alt')),'Image lacks alt: '+p.name)
  for el in soup.select('math'):require(el.find('annotation',encoding='application/x-tex') is not None,'Math lacks source annotation');math+=1
  ids=[x['id'] for x in soup.find_all(id=True)];require(len(set(ids))==len(ids),'Duplicate HTML IDs: '+p.name)
 for p,soup in seen.items():
  for tag,key in [('a','href'),('img','src'),('script','src'),('link','href')]:
   for el in soup.find_all(tag):
    val=el.get(key)
    if not val:continue
    u=urlsplit(val)
    if u.scheme or u.netloc:
     require(u.scheme in ('https','http','mailto'),'Unexpected link scheme');outside.append(val);continue
    dest=(p.parent/unquote(u.path)).resolve() if u.path else p
    if not dest.is_relative_to(site):missing.append((p.name,val,'outside site'));continue
    if not dest.exists():missing.append((p.name,val,'missing file'));continue
    if u.fragment and dest.suffix=='.html':
     ds=seen.get(dest) or BeautifulSoup(dest.read_text(),'html.parser')
     if not (ds.find(id=unquote(u.fragment)) or ds.find('a',attrs={'name':unquote(u.fragment)})):missing.append((p.name,val,'missing anchor'))
    links+=1
  for img in soup.find_all('img'):
   for k in ('data-original','data-themed'):
    if img.get(k):require((p.parent/img[k]).is_file(),'Missing alternate figure')
 require(not missing,'Broken links: '+repr(missing[:25]))
 for page in config['pages']:
  rel=page['source'];require((ROOT/rel).read_bytes()==(site/'files'/rel).read_bytes(),'Copied source mismatch: '+rel)
  if page.get('canonical'):
   src=(ROOT/rel).read_text();count=len(re.findall(r'\$\$(.*?)\$\$',src,re.S))
   # Native MathML conversion retains original TeX in annotation, independently auditable.
   ann=[a.get_text() for a in seen[site/(page['slug']+'.html')].select('math annotation[encoding="application/x-tex"]')]
   for eq in re.findall(r'\$\$(.*?)\$\$',src,re.S):
    require(any(re.sub(r'\s+','',eq)==re.sub(r'\s+','',v) for v in ann),'Displayed equation missing in '+page['slug'])
   sources.append({'source':rel,'sha256':sha(ROOT/rel),'displayed_equations_retained':count})
 colors=palette['roles'];pairs=[]
 for fg,bg in [('ink','paper'),('muted','paper'),('indigo','paper'),('rust','paper'),('sage_ink','paper'),('white','indigo'),('ink','yellow'),('muted','mist')]:
  ratio=contrast(colors[fg],colors[bg]);require(ratio>=4.5,'Text contrast too low: '+str((fg,bg,ratio)));pairs.append({'foreground':fg,'background':bg,'contrast':ratio,'at_least_4_5':True})
 for fg in ('indigo','rust'):
  ratio=contrast(colors[fg],colors['white']);require(ratio>=3,'Curve contrast insufficient')
 record=load(site/'files/BUILD_RECORD.json')
 reuse=check_reuse_downloads(site,record)
 require(record['learning_bridge']['sha256']==sha(ROOT/METADATA),'Learning metadata hash mismatch')
 require((site/'files'/METADATA).read_bytes()==(ROOT/METADATA).read_bytes(),'Learning metadata download mismatch')
 require(record['learning_bridge']['tutorial_version']==bridge['source']['version'],'Unpinned tutorial build record')
 for row in record['themed_svgs']:
  original=(ROOT/row['source']).read_text();new=(site/row['output']).read_text();m=palette['svg_mapping'];allcolors=set(m)|set(m.values())
  normalize=lambda t:re.sub(r'#[0-9a-fA-F]{6}\b',lambda x:'@COLOR@' if x.group().lower() in allcolors else x.group(),t)
  require(normalize(original)==normalize(new),'SVG noncolor difference')
  expected=re.sub(r'#[0-9a-fA-F]{6}\b',lambda x:m.get(x.group().lower(),x.group()),original)
  require(new==expected,'Unexpected palette replacement')
 # No new em dash in authored reader copy; inherited exact source is not restyled.
 for p in (ROOT/'website/pages').glob('*.md'):require('—' not in p.read_text(),'New authored em dash')
 return {'passed':True,'html_pages':len(files),'routes_checked':sorted(p['slug'] for p in config['pages']),'learning_bridge_metadata_verified':True,'local_links_checked':links,'external_links_not_fetched':len(set(outside)),
  'mathml_expressions':math,'canonical_sources':sources,'reuse_source_downloads':reuse,'palette_text_contrasts':pairs,'color_only_svg_derivatives':len(record['themed_svgs']),
  'source_preservation':pres,'no_public_deployment':True,'new_math_verification':False,'browser_checks_separate':True}

if __name__=='__main__':
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--site',type=Path,required=True);ap.add_argument('--report',type=Path);a=ap.parse_args();r=check(a.site)
 if a.report:dump(a.report,r)
 print(json.dumps(r,indent=2))
