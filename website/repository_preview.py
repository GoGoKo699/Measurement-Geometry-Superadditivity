#!/usr/bin/env python3
"""Generate a GitHub-native reading route from existing scientific/site sources.

No deployment, runtime extraction, new science or scientific-source edits.
Canonical technical documents are linked directly instead of duplicated.
The derived SVGs use precisely the website's existing color-literal map.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / 'website'
sys.path.insert(0, str(WEB))
from learning_bridge import METADATA, expand_background, load_bridge, validate_routes
from markdown_math import to_github_math

def read_json(p):
    return json.loads(p.read_text(encoding='utf-8'))

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def page_path(page):
    if page.get('canonical'):
        return page['source']
    return 'reader/' + ('README' if page['slug'] == 'index' else page['slug']) + '.md'

def relative(target, origin):
    return os.path.relpath(ROOT / target, (ROOT / origin).parent).replace(os.sep, '/')

def expected_files():
    config = read_json(WEB / 'site.json')
    validate_routes(config)
    bridge = load_bridge()
    pages = config['pages']
    by_slug = {p['slug']: p for p in pages}
    by_source = {p['source']: page_path(p) for p in pages}
    outputs = {}
    source_hashes = {}

    def source(rel):
        p = ROOT / rel
        if not p.is_file():
            raise ValueError('Missing preview source: ' + rel)
        raw = p.read_bytes()
        source_hashes[rel] = sha(raw)
        return raw.decode('utf-8')

    # Read canonical sources to verify availability and track their unchanged hashes.
    for p in pages:
        source(p['source'])
    source(METADATA)
    source('website/site.json')
    palette = json.loads(source('website/palette.json'))
    mapping = {a.lower(): b.lower() for a, b in palette['svg_mapping'].items()}
    figdefs = [
        ('figure_01_channel_and_witness', 'The channel and a concrete separation',
         ['figure1_comparison.csv','figure1_all_masks_not_for_display.csv','figure1_original_witness140.json'], ['p01','p13']),
        ('figure_02_guaranteed_region', 'The geometric guarantee across reporting noise',
         ['figure2_pauli_guaranteed_region.csv','cross_figure_witness_bound_check.json'], ['p08','p10']),
        ('figure_03_coplanar_limit', 'The approach to a plane',
         ['figure3_cone_geometry.csv','figure3_cone_gap.csv'], ['p11','p12'])]
    for stem, _, _, _ in figdefs:
        old = source('figures/approved/' + stem + '.svg')
        new = re.sub(r'#[0-9a-fA-F]{6}\b', lambda m: mapping.get(m.group().lower(), m.group()), old)
        normalize = lambda s: re.sub(r'#[0-9a-fA-F]{6}\b', lambda m: '@COLOR@' if m.group().lower() in set(mapping) | set(mapping.values()) else m.group(), s)
        if normalize(old) != normalize(new):
            raise ValueError('Noncolor figure change')
        outputs['reader/assets/' + stem + '.svg'] = new.encode()
    captions = source('figures/CAPTIONS.md')
    claims = json.loads(source('provenance/CLAIM_COVERAGE.json'))['claims']

    def linked(label, target, origin, anchor=''):
        return '[' + label + '](' + relative(target, origin) + ('#'+anchor if anchor else '') + ')'

    def rewrite(text, src, origin):
        def change(match):
            prefix, ref = match.group(1), match.group(2)
            u = urlsplit(ref)
            if u.scheme or u.netloc or ref.startswith('#'):
                return match.group()
            path = (ROOT / src).parent / unquote(u.path)
            resolved = path.resolve()
            if not resolved.is_relative_to(ROOT):
                raise ValueError('Link outside repository: ' + ref)
            rel = resolved.relative_to(ROOT).as_posix()
            dest = by_source.get(rel, rel)
            return prefix + urlunsplit(('', '', relative(dest, origin), u.query, u.fragment)) + ')'
        return re.sub(r'(!?\[[^\]\n]*\]\()([^\s)]+)\)', change, text)

    for page in pages:
        if page.get('canonical'):
            continue
        origin = page_path(page)
        expanded = expand_background(source(page['source']), page['source'], bridge)
        body = rewrite(expanded, page['source'], origin)
        # GitHub custom anchors use name; canonical technical files stay untouched.
        body = re.sub(r'<a id="([^"]+)"></a>', r'<a name="\1"></a>', body)
        nav = ' · '.join(linked(label, page_path(by_slug[s]), origin) for s,label in [
            ('index','Overview'), ('background','Background'), ('channel','Channel'), ('proof-guide','Proof route'),
            ('figures','Figures'), ('model','Exact theorem'), ('proof','Complete proof'), ('materials','Materials')])
        toc = '\n'.join('- ' + linked(p['title'], page_path(p), origin) for p in pages)
        menu = '<details>\n<summary>All reading routes</summary>\n\n' + toc + '\n\n</details>'
        parts = body.split('\n', 1)
        intro = '\n\n' + nav + '\n\n' + menu + '\n\n'
        body = parts[0] + intro + (parts[1] if len(parts)>1 else '')
        if page['slug'] == 'index':
            body = body.replace('## Start with the channel',
                '![The channel and retained coding witness in the Gachet-inspired palette](assets/figure_01_channel_and_witness.svg)\n\n'
                '[Read the full figure and its sources](figures.md#figure-1) · [Compare the original colors](../figures/approved/figure_01_channel_and_witness.svg)\n\n'
                '## Start with the channel', 1)
        if page['slug'] == 'figures':
            body = body.replace('Switch to the approved colors to compare.', 'Open the approved originals beneath each figure to compare.')
            atlas = []
            for number, (stem,title,inputs,proofs) in enumerate(figdefs,1):
                match = re.search(rf'## Figure {number}\. [^\n]+\n(.*?)(?=\n## |\Z)', captions, re.S)
                if match is None:
                    raise ValueError('Missing canonical caption')
                caption = rewrite(match.group(1).strip(), 'figures/CAPTIONS.md', origin)
                download = ' · '.join(linked('Approved '+ext.upper(),'figures/approved/'+stem+'.'+ext,origin) for ext in ('pdf','svg','png'))
                palette_download = linked('Accepted-palette SVG','reader/assets/'+stem+'.svg',origin)
                data = ' · '.join(linked(n,'data/figures/'+n,origin) for n in inputs)
                proof = ' · '.join(linked(p.upper(),'docs/COMPLETE_PROOF.md',origin,p) for p in proofs)
                atlas.append(f'<a name="figure-{number}"></a>\n\n## Figure {number}. {title}\n\n'
                    f'![Figure {number}: {title}; only the colors differ from the approved original](assets/{stem}.svg)\n\n'
                    f'Accepted figure palette: {palette_download}. Protected originals: {download}.\n\n{caption}\n\n'
                    f'**Proof:** {proof}. **Unchanged caption source:** '
                    f'{linked("CAPTIONS.md","figures/CAPTIONS.md",origin)}.\n\n**Numerical inputs:** {data}.\n')
            body = body.replace('<!-- SITE:FIGURE_ATLAS -->', '\n'.join(atlas))
        rows = ['| Claim | Exact statement | Proof | Role |','|---|---|---|---|']
        for c in claims:
            rows.append('| '+c['id']+' | '+linked('Model statement','docs/MODEL_AND_CLAIMS.md',origin,c['canonical_model_anchor'])+' | '+' · '.join(linked(s,'docs/COMPLETE_PROOF.md',origin,s.lower()) for s in c['canonical_proof_sections'])+' | '+c['role'].replace('|','\\|')+' |')
        body = body.replace('<!-- SITE:CLAIM_TABLE -->', '\n'.join(rows))
        rows = ['| Role | Source or recorded result |','|---|---|']
        for label,path in [('Rational cover','certificates/common_noise_compact_certificate.json'),('Integer verifier','verification/integer/certify_all_noise.py'),('mpmath verifier','verification/mpmath/cross_backend.py'),('Decimal verifier','verification/decimal/verify_certificate.py'),('Recorded integer result','evidence/reference/integer224.json'),('Recorded mpmath result','evidence/reference/mpmath85.json'),('Recorded Decimal result','evidence/reference/decimal130.json')]:
            if not (ROOT/path).is_file():
                raise ValueError('Missing resource: '+path)
            rows.append('| '+label+' | '+linked(path,path,origin)+' |')
        body = body.replace('<!-- SITE:CHECKER_TABLE -->', '\n'.join(rows))
        palette_rows = ['| Color role | Display value |','|---|---|'] + ['| '+name+' | `'+value+'` |' for name,value in palette['roles'].items()]
        body = body.replace('<!-- SITE:PALETTE -->', '\n'.join(palette_rows))
        body = body.replace('<!-- SITE:FIGURE_COMPARISON -->',
            '**Accepted figure palette**\n\n![Figure 2 in the Gachet-inspired palette](assets/figure_02_guaranteed_region.svg)\n\n'
            '**Approved original**\n\n![The same Figure 2 in its approved original palette](../figures/approved/figure_02_guaranteed_region.svg)')
        if '<!-- SITE:' in body:
            raise ValueError('Unexpanded website content marker in '+origin)
        previous = by_slug.get(page.get('previous'))
        nxt = by_slug.get(page.get('next'))
        tail = linked('Continue: '+nxt['title'],page_path(nxt),origin) if nxt else linked('Return to the overview','reader/README.md',origin)
        if previous:
            tail = linked('Previous: '+previous['title'], page_path(previous), origin) + ' · ' + tail
        body += '\n\n---\n\n'+tail+'\n\n'
        body += 'GitHub reading view generated from '+linked('the website source',page['source'],origin)+'. '
        body += 'The equations, figure data and canonical captions retain their source meaning. '
        body += 'Custom website navigation, local search and interactive color switching are not executed in this GitHub view.\n'
        outputs[origin] = to_github_math(body).encode('utf-8')
    record = {'format':'GitHub Markdown with linked canonical technical documents','public_deployment':False,
              'canonical_technical_documents_duplicated':False,'routes':{p['slug']:page_path(p) for p in pages},
              'source_hashes':dict(sorted(source_hashes.items())),
              'generated_files':{n:sha(b) for n,b in sorted(outputs.items())},
              'rebuild_command':'python website/repository_preview.py --write',
              'check_command':'python website/repository_preview.py --check'}
    outputs['reader/PREVIEW_MANIFEST.json']=(json.dumps(record,indent=2,ensure_ascii=False)+'\n').encode()
    return outputs

def run(check=False):
    outputs = expected_files()
    for name,raw in outputs.items():
        p=ROOT/name
        if not p.resolve().is_relative_to(ROOT/'reader'):
            raise ValueError('Invalid output path')
        if check:
            if not p.is_file() or p.read_bytes()!=raw:
                raise ValueError('Stale or missing repository preview: '+name)
        else:
            p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
    if check:
        extra={p.relative_to(ROOT).as_posix() for p in (ROOT/'reader').rglob('*') if p.is_file()}-set(outputs)
        if extra:
            raise ValueError('Untracked preview outputs: '+str(sorted(extra)))
    pages = read_json(WEB / 'site.json')['pages']
    print(json.dumps({'passed':True,'mode':'check' if check else 'write','files':len(outputs),'reader_pages':sum(not p.get('canonical', False) for p in pages),'canonical_routes':sum(bool(p.get('canonical')) for p in pages),'derived_figures':len([name for name in outputs if name.endswith('.svg')]),'public_deployment':False}))

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    mode=ap.add_mutually_exclusive_group(required=True);mode.add_argument('--write',action='store_true');mode.add_argument('--check',action='store_true')
    run(ap.parse_args().check)
