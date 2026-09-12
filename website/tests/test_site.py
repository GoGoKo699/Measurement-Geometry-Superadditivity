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
    from learning_bridge import REQUIRED_ROUTES
    assert REQUIRED_ROUTES <= set(r['routes_checked'])
    assert r['local_links_checked']>1000
    assert r['source_preservation']['approved_graphical_artifacts_unchanged']==27

def test_canonical_equations(site):
    for slug,n in [('model',18),('proof',119)]:
        html=BeautifulSoup((site/(slug+'.html')).read_text(),'html.parser')
        assert len(html.select('math[display="block"]'))==n
        assert len(html.select('.math.display'))==n
        assert all(x.find('annotation',encoding='application/x-tex') for x in html.find_all('math'))

def test_every_reader_route_has_sources(site):
    pages=json.loads((ROOT/'site.json').read_text())['pages']
    from learning_bridge import REQUIRED_ROUTES
    assert REQUIRED_ROUTES <= {p['slug'] for p in pages}
    for p in pages:
        assert (site/'files'/p['source']).read_bytes()==(REPO/p['source']).read_bytes()
        doc=BeautifulSoup((site/(p['slug']+'.html')).read_text(),'html.parser')
        assert len(doc.select('a[aria-current="page"]'))==1


def test_license_citation_and_third_party_downloads(site):
    required={
        'LICENSE.md','LICENSES/MIT.txt','LICENSES/CC-BY-4.0.txt',
        'LICENSES/DejaVu.txt','LICENSES/STIX.txt','THIRD_PARTY_NOTICES.md',
        'CITATION.cff',
    }
    assert set(builder.REUSE_DOWNLOADS)==required
    record=json.loads((site/'files/BUILD_RECORD.json').read_text())
    assert len(checker.check_reuse_downloads(site,record))==len(required)
    for rel in required:
        assert (site/'files'/rel).read_bytes()==(REPO/rel).read_bytes()
    for rel in ('website/requirements.txt','website/requirements-browser.txt'):
        assert (site/'files'/rel).read_bytes()==(REPO/rel).read_bytes()
    for file in site.glob('*.html'):
        page=BeautifulSoup(file.read_text(),'html.parser')
        for rel in ('LICENSE.md','CITATION.cff','THIRD_PARTY_NOTICES.md'):
            assert page.select_one(f'footer a[href="files/{rel}"]')


def test_current_integrity_sources_are_exact_downloads(site):
    required={'integrity/check_scientific.py','integrity/SCIENTIFIC_FILES.json'}
    assert set(builder.INTEGRITY_DOWNLOADS)==required
    record=json.loads((site/'files/BUILD_RECORD.json').read_text())
    assert len(checker.check_integrity_downloads(site,record))==len(required)
    page=BeautifulSoup((site/'verification.html').read_text(),'html.parser')
    for rel in required:
        assert page.select_one(f'a[href="files/{rel}"]')
    for path in ('publication','website/review','website/provenance'):
        assert not (site/'files'/path).exists()
    assert 'base_commit' not in record and 'reader_baseline_commit' not in record
    assert record['local_reading_edition'] and not record['public_deployment_performed']


def test_downloaded_scientific_bundle_passes_its_own_offline_check(site):
    from integrity.check_scientific import check
    result=check(site/'files')
    assert result['passed']
    assert result['approved_graphical_artifacts_unchanged']==27
    assert result['accepted_reader_svgs_unchanged']==3


@pytest.mark.parametrize('change',['missing','changed-bytes','forged-hash','missing-row','changed-path'])
def test_invalid_integrity_downloads_fail(site,tmp_path,change):
    import shutil
    record=json.loads((site/'files/BUILD_RECORD.json').read_text())
    for rel in builder.INTEGRITY_DOWNLOADS:
        target=tmp_path/'files'/rel
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(site/'files'/rel,target)
    target=tmp_path/'files/integrity/check_scientific.py'
    if change=='missing':
        target.unlink()
    elif change=='changed-bytes':
        target.write_bytes(target.read_bytes()+b'\n')
        record['integrity_source_downloads'][0]['sha256']=builder.sha(target)
    elif change=='forged-hash':
        record['integrity_source_downloads'][0]['sha256']='0'*64
    elif change=='missing-row':
        record['integrity_source_downloads'].pop()
    else:
        record['integrity_source_downloads'][0]['download']='../check_scientific.py'
    with pytest.raises(ValueError,match='Integrity download'):
        checker.check_integrity_downloads(tmp_path,record)


@pytest.mark.parametrize('change',['missing','changed-bytes','forged-hash','missing-row','changed-path'])
def test_invalid_license_downloads_fail(site,tmp_path,change):
    import shutil
    record=json.loads((site/'files/BUILD_RECORD.json').read_text())
    for rel in builder.REUSE_DOWNLOADS:
        target=tmp_path/'files'/rel
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(site/'files'/rel,target)
    target=tmp_path/'files/LICENSE.md'
    if change=='missing':
        target.unlink()
    elif change=='changed-bytes':
        target.write_bytes(target.read_bytes()+b'\n')
        record['reuse_source_downloads'][0]['sha256']=builder.sha(target)
    elif change=='forged-hash':
        record['reuse_source_downloads'][0]['sha256']='0'*64
    elif change=='missing-row':
        record['reuse_source_downloads'].pop()
    else:
        record['reuse_source_downloads'][0]['download']='../LICENSE.md'
    with pytest.raises(ValueError,match='License/citation'):
        checker.check_reuse_downloads(tmp_path,record)

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
    assert e['source_of_truth']=='website/pages/'
    assert e['learning_metadata']=='website/learning_bridge.json'
    assert e['scientific_proof_ledger']=='provenance/CLAIM_COVERAGE.json'
    assert {p['path'] for p in e['new_pages']} == {p['source'] for p in json.loads((ROOT/'site.json').read_text())['pages'] if not p.get('canonical')}
    assert not {'my_tone','preskill_bridge','current_reader_status'} & set(e)
    for entry in e['new_pages']:
        for source in entry['source_anchors']:
            path,_,anchor=source.partition('#')
            assert (REPO/path).is_file(),source
            if anchor:assert f'id="{anchor}"' in (REPO/path).read_text() or f'{{#{anchor}}}' in (REPO/path).read_text()

def test_public_deployment_is_absent():
    for page in (ROOT/'pages').glob('*.md'):assert '—' not in page.read_text()
    cfg=(REPO/'.github/workflows/reader-site.yml').read_text()
    assert 'contents: read' in cfg and 'deploy-pages' not in cfg and 'pages: write' not in cfg

def test_pinned_background_map_and_metadata_download(site):
    from learning_bridge import METADATA, expand_background, load_bridge
    data=load_bridge()
    page=BeautifulSoup((site/'background.html').read_text(),'html.parser')
    body=page.select_one('article').get_text(' ',strip=True)
    for passage in data['passages']:
        assert passage['question'] in body and passage['retain'] in body
    links={a.get('href') for a in page.find_all('a')}
    assert data['source']['abs_url'] in links and data['source']['pdf_url'] in links
    assert (site/'files'/METADATA).read_bytes()==(REPO/METADATA).read_bytes()
    record=json.loads((site/'files/BUILD_RECORD.json').read_text())
    assert record['learning_bridge']['sha256']==builder.sha(REPO/METADATA)
    expanded=expand_background((REPO/'website/pages/background.md').read_text(),
                               'website/pages/background.md',data)
    annotations={re.sub(r'\s+','',a.get_text()) for a in page.select('math annotation[encoding="application/x-tex"]')}
    for equation in re.findall(r'(?<!\$)\$([^$\n]+)\$(?!\$)',expanded):
        assert re.sub(r'\s+','',equation) in annotations


def test_learning_navigation_and_search_cover_required_routes(site):
    config=json.loads((ROOT/'site.json').read_text())
    expected={p['slug']+'.html' for p in config['pages']}
    for row in config['pages']:
        page=BeautifulSoup((site/(row['slug']+'.html')).read_text(),'html.parser')
        assert {a['href'] for a in page.select('nav .nav-link')}==expected
        if row.get('previous'):
            assert page.select_one('a[rel="prev"]')['href']==row['previous']+'.html'
        assert page.select_one('.next-link')['href']==(row.get('next') or 'index')+'.html'
    search=json.loads((site/'assets/search-index.js').read_text().removeprefix('window.PROJECT_SEARCH = ').strip().rstrip(';'))
    assert any(row['url'].startswith('background.html#') and 'Preskill' in row['text'] for row in search)


def test_editorial_section_headings_render_as_headings(site):
    config=json.loads((ROOT/'site.json').read_text())
    normalize=lambda text:text.replace('’',"'").strip()
    for row in config['pages']:
        if row.get('canonical'):
            continue
        source=(REPO/row['source']).read_text()
        expected={normalize(title) for title in re.findall(r'^## (.+)$',source,re.M)}
        page=BeautifulSoup((site/(row['slug']+'.html')).read_text(),'html.parser')
        actual={normalize(h.get_text(' ',strip=True).removesuffix('§')) for h in page.select('article h2')}
        assert expected <= actual, (row['slug'], sorted(expected-actual))


def test_canonical_section_headings_survive_rendering(site):
    config=json.loads((ROOT/'site.json').read_text())
    for row in config['pages']:
        if not row.get('canonical'):
            continue
        source=(REPO/row['source']).read_text()
        headings='\n\n'.join(re.findall(r'^#{2,6} .+$',source,re.M))
        expected=BeautifulSoup(builder.pandoc(headings),'html.parser')
        page=BeautifulSoup((site/(row['slug']+'.html')).read_text(),'html.parser')
        key=lambda h:(h.name,h.get_text(' ',strip=True).removesuffix('§').strip())
        assert [key(h) for h in expected.find_all(re.compile('^h[2-6]$'))] == [key(h) for h in page.select_one('article').find_all(re.compile('^h[2-6]$'))],row['slug']


def test_anchor_separator_changes_only_rendering_whitespace():
    source=(REPO/'docs/COMPLETE_PROOF.md').read_text()
    prepared=builder.prepare_markdown(source)
    assert prepared!=source
    assert re.sub(r'\s+','',prepared)==re.sub(r'\s+','',source)
    equations=lambda text:re.findall(r'\$\$(.*?)\$\$|(?<!\$)\$([^$\n]+)\$(?!\$)',text,re.S)
    assert equations(prepared)==equations(source)
    assert builder.prepare_markdown(prepared)==prepared
