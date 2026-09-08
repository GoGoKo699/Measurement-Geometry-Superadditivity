"""Repository-native preview checks; no scientific computations are rerun."""
import importlib.util
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('repository_preview',ROOT/'website/repository_preview.py')
preview=importlib.util.module_from_spec(spec);spec.loader.exec_module(preview)

def test_repository_preview_exact():
    preview.run(check=True)

def test_all_sixteen_routes_exist():
    m=json.loads((ROOT/'reader/PREVIEW_MANIFEST.json').read_text())
    assert len(m['routes'])==16 and not m['canonical_technical_documents_duplicated']
    assert all((ROOT/p).is_file() for p in m['routes'].values())

def test_native_no_site_placeholders_or_html_destinations():
    for p in (ROOT/'reader').glob('*.md'):
        t=p.read_text();assert '<!-- SITE:' not in t
        assert not re.search(r'\]\([^)]*\.html(?:#.*?)?\)',t)
        for dest in re.findall(r'\]\(([^\s)]+)\)',t):
            if '://' in dest or dest.startswith('#'):continue
            base=dest.split('#')[0]
            assert (p.parent/base).resolve().is_file(),(p,dest)

def test_all_source_math_preserved_in_native_pages():
    config=json.loads((ROOT/'website/site.json').read_text())
    for page in config['pages']:
        if page.get('canonical'):continue
        source=(ROOT/page['source']).read_text()
        target=(ROOT/preview.page_path(page)).read_text()
        for equation in re.findall(r'\$\$(.*?)\$\$|(?<!\$)\$([^$\n]+)\$(?!\$)',source,re.S):
            assert next(x for x in equation if x) in target

def test_only_three_color_derivatives():
    p=json.loads((ROOT/'website/palette.json').read_text())['svg_mapping']
    allowed=set(map(str.lower,p))|set(x.lower() for x in p.values())
    def stripped(t):return re.sub(r'#[0-9a-fA-F]{6}\b',lambda m:'@COLOR@' if m.group().lower() in allowed else m.group(),t)
    derivatives=list((ROOT/'reader/assets').glob('*.svg'));assert len(derivatives)==3
    for f in derivatives:
        assert stripped(f.read_text())==stripped((ROOT/'figures/approved'/f.name).read_text())

def test_private_no_manuscript_or_public_hosting():
    m=json.loads((ROOT/'reader/PREVIEW_MANIFEST.json').read_text())
    assert not m['public_deployment']
    assert m['routes']['proof']=='docs/COMPLETE_PROOF.md'
    assert m['routes']['model']=='docs/MODEL_AND_CLAIMS.md'
