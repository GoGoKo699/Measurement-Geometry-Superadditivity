"""Reader completion, contact and optional provenance routes stay coherent."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def test_current_completion_pages_keep_local_scope_and_expert_routes():
    for name in ('README.md', 'STATUS.md', 'website/pages/status.md'):
        text = (ROOT / name).read_text()
        assert 'complete for its stated scientific result' in text
        assert 'external peer review' in text
        assert 'manuscript' in text
        assert 'mailto:gogoko699@gmail.com' in text
        assert 'COMPLETE_PROOF.md' in text
        assert 'MODEL_AND_CLAIMS.md#m04' in text
        assert 'release/public-readiness-v1' not in text
        assert 'authorized integration' not in text


def test_history_is_optional_and_old_correction_anchor_still_resolves():
    status = (ROOT / 'website/pages/status.md').read_text()
    assert '<a id="correction-record"></a>' in status
    for name in ('status', 'materials'):
        text = (ROOT / f'website/pages/{name}.md').read_text()
        details = re.search(r'<details>\s*<summary>Provenance and maintenance records</summary>(.*?)</details>', text, re.S)
        assert details and '../../publication/PROJECT_HISTORY.md' in details.group(1)
        assert 'PR #5' not in text
    history = (ROOT / 'publication/PROJECT_HISTORY.md').read_text()
    for destination in ('../STATUS.md', '../reader/README.md', '../docs/REFERENCES.md#s6-correction'):
        assert destination in history


def test_learning_route_does_not_assign_preparation_records():
    for page in ('index', 'background', 'channel', 'proof-guide', 'limits'):
        text = (ROOT / f'website/pages/{page}.md').read_text()
        assert 'status.md#correction-record' not in text
        assert 'publication/' not in text
    source = (ROOT / 'website/build.py').read_text()
    assert 'Private review build.<br>' not in source
    assert 'Reader starting baseline: <code>' not in source
