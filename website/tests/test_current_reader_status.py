"""Reader completion, contact and direct evidence routes stay coherent."""
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


def test_reader_pages_do_not_depend_on_administrative_history():
    for name in ('status', 'materials', 'verification'):
        text = (ROOT / f'website/pages/{name}.md').read_text()
        assert 'publication/' not in text
        assert 'Provenance and maintenance records' not in text
        assert 'PR #5' not in text
        assert 'actions/runs/' not in text
    verification = (ROOT / 'website/pages/verification.md').read_text()
    assert 'python integrity/check_scientific.py' in verification
    assert 'without Git history' in verification
    assert 'a configured, skipped or running check is not a pass' in verification
    for path in ('publication', 'website/review', 'website/provenance'):
        assert not (ROOT / path).exists()


def test_learning_route_does_not_assign_preparation_records():
    for page in ('index', 'background', 'channel', 'proof-guide', 'limits'):
        text = (ROOT / f'website/pages/{page}.md').read_text()
        assert 'status.md#correction-record' not in text
        assert 'publication/' not in text
    source = (ROOT / 'website/build.py').read_text()
    assert 'Private review build.<br>' not in source
    assert 'Reader starting baseline: <code>' not in source
