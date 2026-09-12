"""Offline presentation checks for the pinned tutorial and existing sources.

Prose accuracy still requires source reading and the recorded walkthroughs.
These tests neither fetch Preskill nor repeat a scientific certificate run.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'website'))
import learning_bridge as bridge


def metadata():
    return json.loads((ROOT / bridge.METADATA).read_text())


def test_selected_source_and_complete_learning_map():
    data = bridge.load_bridge()
    assert data['source']['version'] == '1604.07450v5'
    config = json.loads((ROOT / 'website/site.json').read_text())
    routes = bridge.validate_routes(config)
    assert routes['background']['source'] == 'website/pages/background.md'
    assert routes['background']['previous'] == 'index'
    assert routes['channel']['previous'] == 'background'
    for passage in data['passages']:
        assert passage['role'] == 'background'
    assert all(row['role'] == 'project' for row in data['bridges'])


@pytest.mark.parametrize('key,value', [
    ('version', '1604.07450'), ('version', '1604.07450v6'),
    ('abs_url', 'https://arxiv.org/abs/1604.07450'),
    ('pdf_url', 'https://arxiv.org/pdf/1604.07450v6'),
    ('pdf_page_offset', 0), ('pdf_sha256', 'unverified'),
])
def test_unpinned_or_unidentified_tutorial_is_rejected(key, value):
    data = metadata();data['source'][key] = value
    with pytest.raises(ValueError):
        bridge.validate_bridge(data)


@pytest.mark.parametrize('target', [
    'website/pages/missing.md', 'website/pages/channel.md#missing-learning-anchor',
    'docs/COMPLETE_PROOF.md#p999', '../outside.md',
    'https://example.invalid/other-tutorial',
])
def test_missing_or_nonlocal_return_anchor_is_rejected(target):
    data = metadata();data['passages'][0]['destination'] = target
    with pytest.raises(ValueError):
        bridge.validate_bridge(data)


def test_source_anchor_and_role_cannot_silently_diverge():
    for section, key, value in [
        ('passages', 'canonical_anchors', ['docs/COMPLETE_PROOF.md#p999']),
        ('bridges', 'canonical_anchors', []),
        ('bridges', 'role', 'background'),
        ('passages', 'role', 'project'),
    ]:
        data = metadata();data[section][0][key] = value
        with pytest.raises(ValueError):
            bridge.validate_bridge(data)


def test_assigned_passages_and_printed_pages_are_not_dropped():
    data = metadata();data['passages'] = [p for p in data['passages'] if p['tier'] != 'completion']
    with pytest.raises(ValueError):
        bridge.validate_bridge(data)
    data = metadata();data['passages'][0]['printed_pages'] = [56, 51]
    with pytest.raises(ValueError):
        bridge.validate_bridge(data)
    data = metadata();data['passages'][0]['pdf_viewer_pages'] = data['passages'][0]['printed_pages']
    with pytest.raises(ValueError):
        bridge.validate_bridge(data)
    data = metadata();data['edition_note']['correct_entropy_difference'] = 'H(E)-H(B)'
    with pytest.raises(ValueError):
        bridge.validate_bridge(data)
    data = metadata();data['passages'][0]['equations'] = [{'id': '10.275', 'printed_page': 999}]
    with pytest.raises(ValueError):
        bridge.validate_bridge(data)


def test_required_routes_and_existing_canonical_sources_are_enforced():
    original = json.loads((ROOT / 'website/site.json').read_text())
    for slug in ('background', 'channel', 'model', 'proof', 'figures', 'verification'):
        data = deepcopy(original);data['pages'] = [p for p in data['pages'] if p['slug'] != slug]
        with pytest.raises(ValueError):
            bridge.validate_routes(data)
    data = deepcopy(original)
    next(p for p in data['pages'] if p['slug'] == 'proof')['source'] = 'website/pages/proof-guide.md'
    with pytest.raises(ValueError):
        bridge.validate_routes(data)


def test_generated_native_map_tracks_its_single_editorial_source():
    manifest = json.loads((ROOT / 'reader/PREVIEW_MANIFEST.json').read_text())
    assert manifest['source_hashes'][bridge.METADATA] == hashlib.sha256((ROOT / bridge.METADATA).read_bytes()).hexdigest()
    data = bridge.load_bridge()
    expanded = bridge.expand_background((ROOT / 'website/pages/background.md').read_text(),
                                        'website/pages/background.md', data)
    native = (ROOT / 'reader/background.md').read_text()
    assert '<!-- SITE:' not in expanded and '<!-- SITE:' not in native
    for passage in data['passages']:
        assert passage['question'] in native
        assert passage['retain'] in native
        for section in passage['sections']:
            assert section in native
    for tutorial, project, meaning in ((r['tutorial'], r['project'], r['meaning']) for r in data['notation']):
        assert tutorial in native and project in native and meaning in native
    for equation in re.findall(r'(?<!\$)\$([^$\n]+)\$(?!\$)', expanded):
        assert equation in native


def test_native_learning_destinations_and_source_return_links():
    pages = json.loads((ROOT / 'website/site.json').read_text())['pages']
    for page in pages:
        if page.get('canonical'):
            continue
        target = ROOT / ('reader/README.md' if page['slug'] == 'index' else 'reader/' + page['slug'] + '.md')
        text = target.read_text()
        assert '../' + page['source'] in text
        for dest in re.findall(r'\]\(([^\s)]+)\)', text):
            if '://' in dest:
                continue
            path, _, anchor = dest.partition('#')
            resolved = (target.parent / path).resolve() if path else target
            if anchor and resolved.suffix == '.md':
                bridge.resolve_anchor(resolved.relative_to(ROOT).as_posix() + '#' + anchor)
    overview = (ROOT / 'reader/README.md').read_text()
    for dest in ('../docs/MODEL_AND_CLAIMS.md', '../docs/COMPLETE_PROOF.md', 'figures.md', 'verification.md'):
        assert dest in overview
    for slug in ('channel', 'proof-guide'):
        assert re.search(r'\]\(background\.md(?:#[^)]+)?\)', (ROOT / ('reader/' + slug + '.md')).read_text())


def test_current_science_and_graphical_artifacts_are_unchanged():
    from integrity.check_scientific import check
    result = check(ROOT)
    assert result['passed']
    assert result['approved_graphical_artifacts_unchanged'] == 27
    assert result['accepted_reader_svgs_unchanged'] == 3
    protected = json.loads((ROOT / 'integrity/SCIENTIFIC_FILES.json').read_text())['files']
    for required in ('docs/COMPLETE_PROOF.md', 'docs/MODEL_AND_CLAIMS.md',
                     'figures/CAPTIONS.md', 'certificates/common_noise_compact_certificate.json',
                     'verification/integer/certify_all_noise.py',
                     'verification/mpmath/cross_backend.py',
                     'verification/decimal/verify_certificate.py', 'website/learning_bridge.json'):
        assert required in protected
