"""Check the implemented documentary repairs against the pinned audit evidence.

No repository evaluator is imported. Run from the repository root; the output
must be new. Browser behavior is deliberately outside this check.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--root', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
root = args.root.resolve()
assert not args.output.exists(), 'Fresh output required'
audit = root / 'audits/repository-sanity-01'
old = json.loads((audit / 'environment/FINAL_BASELINE_STATE.json').read_text())

# Enumerated scope: these current reader/provenance files may change. Every
# other member of the pinned 208-file source tree must retain its original hash.
allowed = {
    'BASELINE_MANIFEST.json', 'STATUS.md', 'WEBSITE.md',
    'docs/MODEL_AND_CLAIMS.md', 'docs/REFERENCES.md',
    'docs/SOURCE_TO_CANONICAL.md', 'figures/FIGURE_SPECIFICATIONS.md',
    'provenance/SECTION_LEDGER.json', 'provenance/CANONICAL_INPUTS.json',
    'provenance/FIGURE_INPUTS.json', 'data/figures/SOURCE_IDENTITY.json',
    'data/figures/BUILD_RECORD.json',
    'website/build.py', 'website/tests/test_default_style.py',
    'website/pages/status.md', 'reader/status.md', 'reader/PREVIEW_MANIFEST.json',
}
changed, unchanged = [], []
for entry in old['source_file_hashes']:
    path = entry['path']
    same = hashlib.sha256((root / path).read_bytes()).hexdigest() == entry['sha256']
    if same:
        unchanged.append(path)
    else:
        assert path in allowed, f'Unexpected pinned-source change: {path}'
        changed.append(path)

spec = (root / 'figures/FIGURE_SPECIFICATIONS.md').read_text()
paths = re.findall(r'`(data/figures/[^`]+)`', spec)
assert len(paths) == 8 and all((root / path).is_file() for path in paths)
assert not re.findall(r'`data/(?!figures/)[^`]+`', spec)
model = (root / 'docs/MODEL_AND_CLAIMS.md').read_text()
assert 'no remote repository has been created' not in model
assert 'No manuscript has been drafted.' in model
refs = (root / 'docs/REFERENCES.md').read_text()
assert '<a id="s6-correction"></a>' in refs
assert 'without extending the threshold beyond weighted repetition codes' in refs
assert 'https://arxiv.org/html/2508.09978v1' in refs
assert 'REFERENCES.md#s6-correction' in (root / 'docs/SOURCE_TO_CANONICAL.md').read_text()
for path in ['WEBSITE.md', 'website/build.py']:
    commands = [line for line in (root / path).read_text().splitlines()
                if 'python -m http.server' in line]
    assert commands and all('--bind 127.0.0.1' in line for line in commands)

# Original audit reports/results are historical evidence, never rewritten as
# though the pinned source had already contained these corrections.
original_manifest = json.loads((audit / 'EVIDENCE_MANIFEST.json').read_text())
for entry in original_manifest['files']:
    raw = (audit / entry['path']).read_bytes()
    assert len(raw) == entry['bytes']
    assert hashlib.sha256(raw).hexdigest() == entry['sha256'], entry['path']

figures = json.loads((root / 'provenance/APPROVED_FIGURE_HASHES.json').read_text())
for path, digest in figures['files'].items():
    assert hashlib.sha256((root / path).read_bytes()).hexdigest() == digest
inputs = [x for x in old['source_file_hashes'] if x['path'].startswith('data/figures/')]
numeric_unchanged = [x['path'] for x in inputs if x['path'] not in {'data/figures/SOURCE_IDENTITY.json', 'data/figures/BUILD_RECORD.json'}]
assert len(numeric_unchanged) == 8
assert all(path in unchanged for path in numeric_unchanged)
result = {
    'passed': True,
    'pinned_commit': old['head'],
    'pinned_files_checked': len(old['source_file_hashes']),
    'pinned_files_byte_unchanged': len(unchanged),
    'authorized_changed_files': changed,
    'corrected_data_paths': paths,
    'historical_audit_records_unchanged': len(original_manifest['files']),
    'approved_graphics_byte_unchanged': len(figures['files']),
    'figure_input_files_byte_unchanged': numeric_unchanged,
    'figure_source_identity_only': 'updated model-document digest and dependent manifest digest',
    'browser_validation': 'not performed by this script',
}
args.output.parent.mkdir(parents=True, exist_ok=True)
with args.output.open('x') as output:
    json.dump(result, output, indent=2)
    output.write('\n')
print(json.dumps(result, indent=2))
