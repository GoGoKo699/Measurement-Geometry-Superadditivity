#!/usr/bin/env python3
"""Check reader controls through a local HTTP server or an in-memory mirror.

With --base-url, real navigation is tested against a loopback-only server.
The default mirror also works where browser navigation is restricted: CSS,
JS and images are read from the checked build and inlined only for the test.
Actual site files are not altered. Neither mode publishes a site. Static link
and source checks are performed separately by check.py.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import argparse,json,shutil,base64,mimetypes
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright

def mirrored(site,name):
 soup=BeautifulSoup((site/(name+'.html')).read_text(),'html.parser')
 for css in soup.find_all('link',rel='stylesheet'):
  style=soup.new_tag('style');style.string=(site/css['href']).read_text();css.replace_with(style)
 # Scripts must run after the DOM in this mirror, like defer does in the site.
 scripts=[]
 for script in list(soup.find_all('script',src=True)):
  scripts.append((site/script['src']).read_text());script.decompose()
 for script in scripts:
  tag=soup.new_tag('script');tag.string=script;soup.body.append(tag)
 for img in soup.find_all('img'):
  for key in ('src','data-original','data-themed'):
   if img.get(key):
    p=site/img[key];mime=mimetypes.guess_type(str(p))[0] or 'application/octet-stream'
    img[key]='data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()
 return str(soup)

def run(site,out,executable,base_url=None):
 site=site.resolve();out.mkdir(parents=True,exist_ok=True);errors=[];external=[];records=[]
 with sync_playwright() as pw:
  browser=pw.chromium.launch(executable_path=executable,headless=True,args=['--no-sandbox'])
  ctx=browser.new_context(viewport={'width':1440,'height':1000},device_scale_factor=1)
  def route_handler(route):
   if base_url and route.request.url.startswith(base_url.rstrip('/')+'/'):route.continue_()
   else:external.append(route.request.url);route.abort()
  ctx.route('**/*',route_handler)
  page=None;viewport={'width':1440,'height':1000}
  def load(name):
   nonlocal page
   if page is not None: page.close()
   page=ctx.new_page();page.set_viewport_size(viewport);page.on('pageerror',lambda e:errors.append(str(e)))
   if base_url:page.goto(base_url.rstrip('/')+'/'+name+'.html',wait_until='networkidle')
   else:page.set_content(mirrored(site,name),wait_until='load')
   page.evaluate('document.fonts.ready')
  for name in ['index','channel','proof-guide','figures','limits','model','proof','verification','reproduce','references','materials','notation','provenance','argument','visual-design','status']:
   load(name)
   overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth+2')
   imgs=page.locator('img').evaluate_all('(imgs)=>imgs.filter(x=>!x.complete || x.naturalWidth===0).length')
   assert not overflow,(name,'desktop page overflow');assert imgs==0,(name,'image failed')
   records.append({'page':name,'desktop_no_page_overflow':True,'images_loaded':True})
   if name in ('index','figures','proof-guide','visual-design'):page.screenshot(path=str(out/(name+'-desktop.png')),full_page=True)
  load('index');page.keyboard.press('Tab');assert page.locator('.skip').evaluate('(x)=>x===document.activeElement')
  page.locator('.search-open').click();page.locator('.search-input').fill('all-measured');assert page.locator('.search-results a').count()>0
  search_count=page.locator('.search-results a').count();page.keyboard.press('Escape');assert not page.locator('dialog').is_visible()
  load('figures');button=page.locator('[data-figure-toggle="fig-1"]');before=page.locator('#fig-1').get_attribute('src');button.click();after=page.locator('#fig-1').get_attribute('src')
  assert before!=after and after==page.locator('#fig-1').get_attribute('data-original');button.click();assert page.locator('#fig-1').get_attribute('src')==before
  viewport={'width':390,'height':844}
  for name in ('index','model','proof','figures','materials','visual-design'):
   load(name);assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+2'),(name,'mobile page overflow')
   assert page.locator('.menu-open').is_visible();page.locator('.menu-open').click();assert page.locator('.sidebar').is_visible();page.keyboard.press('Escape');assert not page.locator('.sidebar').is_visible()
   page.screenshot(path=str(out/(name+'-mobile.png')),full_page=(name in ('index','figures','visual-design')))
  if base_url:
   load('index');page.locator('.next-link').click();assert page.url.endswith('channel.html')
  nojs=browser.new_context(java_script_enabled=False,viewport={'width':1280,'height':900});nojs.route('**/*',route_handler);p=nojs.new_page()
  if base_url:p.goto(base_url.rstrip('/')+'/proof.html',wait_until='networkidle')
  else:p.set_content(mirrored(site,'proof'),wait_until='domcontentloaded')
  assert p.locator('math').count()>100 and p.locator('nav a').count()==16
  p.set_viewport_size({'width':390,'height':844});assert p.locator('.sidebar').is_visible();assert not p.locator('.menu-open').is_visible();assert not p.locator('.search-open').is_visible()
  assert p.evaluate('document.documentElement.scrollWidth <= innerWidth+2')
  if base_url:p.goto(base_url.rstrip('/')+'/figures.html',wait_until='networkidle')
  else:p.set_content(mirrored(site,'figures'),wait_until='domcontentloaded')
  assert p.locator('img').count()==3
  nojs.close();ctx.close();browser.close()
 assert not errors,errors;assert not external,external
 result={'passed':True,'mode':'local HTTP navigation' if base_url else 'in-memory local-file mirror; HTTP and file navigation not tested','desktop_viewport':[1440,1000],'mobile_viewport':[390,844],'pages_checked':len(records),'search_results_for_all_measured':search_count,'keyboard_skip_link_focus':True,'escape_closes_search_and_mobile_nav':True,'figure_theme_toggle':True,'no_javascript_math_and_navigation':True,'no_javascript_mobile_navigation':True,'real_link_navigation_tested':bool(base_url),'external_requests':external,'console_page_errors':errors,'page_records':records,'accessibility_scope':'Keyboard controls, alt-text/static checks and selected contrast ratios; not a full WCAG audit.'}
 (out/'BROWSER_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');return result

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--site',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--chromium',default=shutil.which('chromium') or None);ap.add_argument('--base-url',help='Optional local HTTP server for actual navigation tests.');a=ap.parse_args()
 if a.base_url and (urlsplit(a.base_url).scheme!='http' or urlsplit(a.base_url).hostname not in ('127.0.0.1','localhost')):ap.error('Use a local HTTP review server, not a public site.')
 print(json.dumps(run(a.site,a.output,a.chromium,a.base_url),indent=2))
