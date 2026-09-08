"""Website checks are separate from proof verification and numeric tests."""
from pathlib import Path
from bs4 import BeautifulSoup
import sys,json,re,tempfile
import pytest
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
sys.path.insert(0,str(ROOT))
import build as builder
import check as checker

@pytest.fixture(scope='module')
def site():
    parent=REPO/'build';parent.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='reader-tests-',dir=parent) as tmp:
        out=Path(tmp)/'site'
        builder.build(out)
        yield out

def test_complete_site(site):
    r=checker.check(site)
    assert r['html_pages']==16 and r['local_links_checked']>1000
    assert r['source_preservation']['approved_graphical_artifacts_unchanged']==27

def test_canonical_equations(site):
    for slug,n in [('model',18),('proof',119)]:
        html=BeautifulSoup((site/(slug+'.html')).read_text(),'html.parser')
        assert len(html.select('math[display="block"]'))==n
        assert len(html.select('.math.display'))==n
        assert all(x.find('annotation',encoding='application/x-tex') for x in html.find_all('math'))

def test_every_reader_route_has_sources(site):
    pages=json.loads((ROOT/'site.json').read_text())['pages']
    assert len({p['slug'] for p in pages})==16
    for p in pages:
        assert (site/'files'/p['source']).read_bytes()==(REPO/p['source']).read_bytes()
        doc=BeautifulSoup((site/(p['slug']+'.html')).read_text(),'html.parser')
        assert len(doc.select('a[aria-current="page"]'))==1

def test_palette_has_scientific_roles():
    palette=json.loads((ROOT/'palette.json').read_text())
    assert palette['roles']['indigo']=='#304E66'
    assert palette['roles']['rust']=='#A34E38'
    for fg in ('ink','muted','indigo','rust','sage_ink'):
        assert checker.contrast(palette['roles'][fg],palette['roles']['paper'])>=4.5

def test_approved_downloads_and_color_toggle(site):
    doc=BeautifulSoup((site/'figures.html').read_text(),'html.parser')
    assert len(doc.select('[data-figure-toggle]'))==3
    for img in doc.select('img[data-original]'):
        assert (site/img['data-original']).read_bytes()==(REPO/img['data-original'][6:]).read_bytes()
        assert img.get('loading')=='eager'
    assert len(doc.select('img[data-original]'))==3

def test_no_external_runtime_assets(site):
    for file in site.glob('*.html'):
        doc=BeautifulSoup(file.read_text(),'html.parser')
        assert not doc.select('script[src^="http"],link[href^="http"],img[src^="http"]')
    js=(site/'assets/site.js').read_text()
    assert 'fetch(' not in js and 'localStorage' not in js and 'document.cookie' not in js

def test_no_javascript_navigation_fallback(site):
    doc=BeautifulSoup((site/'index.html').read_text(),'html.parser')
    ns=doc.find('noscript')
    assert ns and ns.find('style')
    assert '.sidebar' in str(ns.find('style').string) and 'display:block!important' in str(ns.find('style').string)

def test_search_is_local_and_has_proof_sections(site):
    raw=(site/'assets/search-index.js').read_text()
    data=json.loads(raw.removeprefix('window.PROJECT_SEARCH = ').strip().rstrip(';'))
    assert any(x['url'].startswith('proof.html#') for x in data)
    assert any('all-measured' in x['text'].lower() for x in data)

def test_safe_fresh_build_rule(tmp_path):
    with pytest.raises(ValueError):builder.build(tmp_path/'outside')

def test_existing_directory_rejected(site):
    with pytest.raises(ValueError):builder.build(site)

def test_editorial_source_anchors():
    e=json.loads((ROOT/'editorial_map.json').read_text())
    assert e['my_tone']['mode']=='repository' and not e['my_tone']['private_examples_copied']
    for entry in e['new_pages']:
        for source in entry['source_anchors']:
            path,_,anchor=source.partition('#')
            assert (REPO/path).is_file(),source
            if anchor:assert f'id="{anchor}"' in (REPO/path).read_text() or f'{{#{anchor}}}' in (REPO/path).read_text()

def test_public_deployment_is_absent():
    for page in (ROOT/'pages').glob('*.md'):assert '—' not in page.read_text()
    cfg=(REPO/'.github/workflows/reader-site.yml').read_text()
    assert 'contents: read' in cfg and 'deploy-pages' not in cfg and 'pages: write' not in cfg
