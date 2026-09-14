"""Validate and render the small, offline tutorial-to-project reading map.

This is editorial metadata, not the scientific proof-dependency ledger.  Both
reading interfaces expand the same Markdown before rewriting local links.
"""
from __future__ import annotations
import json
import os
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
METADATA = 'website/learning_bridge.json'
PIN = '1604.07450v5'
REQUIRED_ROUTES = {
    'index', 'background', 'channel', 'proof-guide', 'figures', 'limits',
    'model', 'proof', 'verification', 'reproduce', 'references', 'materials',
    'notation', 'provenance', 'visual-design', 'status',
}
LEARNING_ROUTE = ('index', 'background', 'channel', 'proof-guide', 'model',
                  'proof', 'limits', 'verification')
TOKENS = {
    '<!-- SITE:BACKGROUND_CORE -->',
    '<!-- SITE:BACKGROUND_OPTIONAL -->',
    '<!-- SITE:BACKGROUND_NOTATION -->',
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def markdown_anchors(text):
    """Explicit anchors plus ordinary GitHub-compatible heading identifiers."""
    anchors = set(re.findall(r'\b(?:id|name)=[\"\']([^\"\']+)', text))
    anchors.update(re.findall(r'\{#([^}]+)\}', text))
    counts = {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        title = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', title)
        title = re.sub(r'<[^>]*>', '', title).lower()
        title = re.sub(r'[^\w\-\s]', '', title).replace(' ', '-')
        count = counts.get(title, 0)
        anchors.add(title + ('-' + str(count) if count else ''))
        counts[title] = count + 1
    return anchors


def resolve_anchor(target, root=ROOT):
    """Check a repository-root-relative path and, when supplied, its anchor."""
    require(isinstance(target, str) and bool(target), 'Empty bridge destination')
    url = urlsplit(target)
    require(not url.scheme and not url.netloc and not url.query,
            'Bridge destinations must be repository paths: ' + target)
    path = (root / unquote(url.path)).resolve()
    require(path.is_relative_to(root.resolve()) and path.is_file(),
            'Missing or outside bridge destination: ' + target)
    if url.fragment:
        require(unquote(url.fragment) in markdown_anchors(path.read_text()),
                'Missing bridge anchor: ' + target)
    return path


def validate_routes(config, root=ROOT):
    pages = config['pages']
    slugs = [p['slug'] for p in pages]
    require(len(slugs) == len(set(slugs)), 'Duplicate reader route')
    require(REQUIRED_ROUTES <= set(slugs), 'Missing required learning or expert route')
    require(len({p['source'] for p in pages}) == len(pages), 'Duplicate editorial source')
    by_slug = {p['slug']: p for p in pages}
    for page in pages:
        resolve_anchor(page['source'], root)
        for key in ('next', 'previous'):
            require(page.get(key) is None or page[key] in by_slug, 'Broken ' + key + ' route')
    for previous, following in zip(LEARNING_ROUTE, LEARNING_ROUTE[1:]):
        require(by_slug[previous]['next'] == following and
                by_slug[following].get('previous') == previous,
                'Missing learning-route connection: ' + previous + ' -> ' + following)
    for slug, source in [('model', 'docs/MODEL_AND_CLAIMS.md'),
                         ('proof', 'docs/COMPLETE_PROOF.md')]:
        require(by_slug[slug].get('canonical') and by_slug[slug]['source'] == source,
                'Canonical expert route must render its existing source')
    return by_slug


def validate_bridge(data, root=ROOT):
    require(data['schema_version'] == 1, 'Unsupported learning-map schema')
    source = data['source']
    require(source['required_external_tutorials'] == 1, 'The route has one external tutorial')
    require(source['id'] == 'preskill-qst-v5' and source['version'] == PIN,
            'Tutorial must use the selected Preskill v5 edition')
    require(source['abs_url'] == 'https://arxiv.org/abs/' + PIN and
            source['pdf_url'] == 'https://arxiv.org/pdf/' + PIN,
            'Tutorial links must pin the official v5 source')
    require(source['author'] == 'John Preskill' and source['title'], 'Missing tutorial attribution')
    require(re.fullmatch(r'\d{4}-\d{2}-\d{2}', source['verified_date']) is not None,
            'Missing source inspection date')
    require(source['pdf_page_offset'] == 6, 'Keep printed pages distinct from PDF page numbers')
    require(re.fullmatch(r'[0-9a-f]{64}', source['pdf_sha256']) is not None,
            'Missing inspected PDF identity')
    passages = data['passages']
    require(bool(passages), 'Missing selected reading passages')
    ids = [p['id'] for p in passages] + [b['id'] for b in data['bridges']]
    require(len(ids) == len(set(ids)), 'Duplicate learning-map identifier')
    sections = {'core': set(), 'completion': set(), 'optional': set()}
    for passage in passages:
        require(passage['role'] == 'background' and passage['tier'] in sections,
                'Invalid background reading role')
        require(bool(passage['sections']), 'Missing section reference')
        sections[passage['tier']].update(passage['sections'])
        first, last = passage['printed_pages']
        require(type(first) is int and type(last) is int and 1 <= first <= last <= 97,
                'Invalid printed-page range')
        require(passage['pdf_viewer_pages'] == [first + 6, last + 6],
                'Printed pages and one-based viewer pages disagree')
        require(passage['question'].strip() and passage['retain'].strip() and passage['destination_label'].strip(),
                'Reading passage needs a question and retained concept')
        for equation in passage['equations']:
            require(re.fullmatch(r'10\.\d+', equation['id']) is not None and
                    type(equation['printed_page']) is int and
                    first <= equation['printed_page'] <= last,
                    'Equation outside its assigned printed-page range')
        resolve_anchor(passage['destination'], root)
        require(passage['canonical_anchors'], 'Missing project return anchors')
        for target in passage['canonical_anchors']:
            resolve_anchor(target, root)
    require(sections['core'] == {'10.7.1', '10.7.2', '10.7.4'},
            'Core route must remain the selected coherent-information passages')
    require(sections['completion'] == {'10.9.4'},
            'Operational completion must retain the unassisted-achievability statement')
    require(sections['optional'] <= {'10.1', '10.2.1', '10.2.2', '10.2.3', '10.2.4', '10.6.6', '10.7.3'},
            'Do not add another prerequisite list')
    require(bool(data['notation']) and bool(data['bridges']), 'Missing notation or project bridge')
    for row in data['notation']:
        require(all(isinstance(row[key], str) and row[key].strip()
                    for key in ('tutorial', 'project', 'meaning')), 'Incomplete notation crosswalk')
    for bridge in data['bridges']:
        require(bridge['role'] == 'project' and bridge['concept'].strip(), 'Invalid project bridge role')
        resolve_anchor(bridge['destination'], root)
        require(bridge['canonical_anchors'], 'Project explanation needs a canonical source')
        for target in bridge['canonical_anchors']:
            resolve_anchor(target, root)
    note = data['edition_note']
    resolve_anchor(note['destination'], root)
    require(note['confirmed_visually'] is True and note['correct_entropy_difference'] == 'H(B)-H(E)',
            'Keep the edition note tied to the recorded visual inspection')
    note_equations = [note['incorrect_equation']] + note['supporting_equations']
    expected = [('10.368', 76), ('10.275', 53), ('10.367', 75)]
    require([(e['id'], e['printed_page']) for e in note_equations] == expected,
            'Edition-note references differ from the inspected equations')
    for equation in note_equations:
        require(equation['pdf_viewer_page'] == equation['printed_page'] + 6,
                'Edition-note viewer page disagrees with its printed page')
    return data


def load_bridge(root=ROOT):
    return validate_bridge(json.loads((root / METADATA).read_text()), root)


def expand_background(text, source, data, root=ROOT):
    """Expand only the three map tokens; relative paths match the page source."""
    if not any(token in text for token in TOKENS):
        return text
    origin = root / source

    def cell(value):
        return str(value).replace('|', '\\|').replace('\n', ' ')

    def link(target, label):
        path, _, anchor = target.partition('#')
        rel = os.path.relpath(root / path, origin.parent).replace(os.sep, '/')
        return '[' + label + '](' + rel + ('#' + anchor if anchor else '') + ')'

    def reading_rows(tiers):
        rows = ['| Passage in v5 | Question and concept to retain | Used here |',
                '|---|---|---|']
        for p in data['passages']:
            if p['tier'] not in tiers:
                continue
            first, last = p['printed_pages']
            pages = str(first) if first == last else f'{first}–{last}'
            label = '§' + ', §'.join(p['sections']) + '; printed pp. ' + pages
            url = data['source']['pdf_url'] + '#page=' + str(first + data['source']['pdf_page_offset'])
            references = '[' + label + '](' + url + ')'
            if p['equations']:
                references += '. ' + '; '.join('Eq. (' + e['id'] + '), p. ' + str(e['printed_page']) for e in p['equations'])
            role = 'Operational statement. ' if p['tier'] == 'completion' else ''
            concept = role + p['question'] + ' ' + p['retain']
            destination = link(p['destination'], p['destination_label'])
            destination += '; ' + ', '.join(link(t, t.partition('#')[2].upper() or Path(t).name)
                                           for i, t in enumerate(p['canonical_anchors']))
            rows.append('| ' + ' | '.join(map(cell, (references, concept, destination))) + ' |')
        return '\n'.join(rows)

    notation = ['| Preskill | This project | Meaning |', '|---|---|---|']
    notation.extend('| ' + ' | '.join(cell(row[key]) for key in ('tutorial', 'project', 'meaning')) + ' |'
                    for row in data['notation'])
    rendered = {
        '<!-- SITE:BACKGROUND_CORE -->': reading_rows({'core', 'completion'}),
        '<!-- SITE:BACKGROUND_OPTIONAL -->': reading_rows({'optional'}),
        '<!-- SITE:BACKGROUND_NOTATION -->': '\n'.join(notation),
    }
    for token, replacement in rendered.items():
        text = text.replace(token, replacement)
    return text
