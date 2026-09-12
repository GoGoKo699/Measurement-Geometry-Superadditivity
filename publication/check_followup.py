#!/usr/bin/env python3
"""Check the bounded publication follow-up against the completed license commit.

This offline check verifies recorded identities. It neither queries live GitHub
settings nor establishes ownership, mathematical correctness or public clearance.
Earlier adoption and reader checkers remain unchanged and commit-scoped.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = '857d173c79140b5c2643c1a7d16b4a2321ed8dd4'
EDITORIAL = {'PUBLICATION.md', 'publication/READINESS.json'}
BLOBS = {
    'baseline.zip': ('f4442ae622a7d96a2346c66acedcea54783a598f', 2540928),
    'figure.png': ('0bac8266cbd5495b9b3a3ef7eecfd642b347af6d', 85639),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load(path):
    return json.loads((ROOT / path).read_text())


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def check():
    before = load('publication/FOLLOWUP_STARTING_FILES.json')
    edits = load('publication/FOLLOWUP_EDITS.json')
    require(before['commit'] == edits['starting_commit'] == START, 'Starting commit differs')
    require(set(edits['files']) == EDITORIAL, 'Unexpected editorial exception')
    for name, expected in before['files'].items():
        if name in EDITORIAL:
            item = edits['files'][name]
            require(item['before_sha256'] == expected, 'Starting editorial hash differs: ' + name)
            expected = item['after_sha256']
        require(sha(name) == expected, 'Unrecorded inherited-file change: ' + name)
    state = load('publication/READINESS.json')
    require(state['license_active'] is True, 'Confirmed licenses must remain active')
    require(state['public_visibility_changed'] is False and state['merge_performed'] is False,
            'This follow-up does not perform either action')
    review = load('publication/evidence/HISTORICAL_OBJECTS_REVIEW.json')
    ci = load('publication/evidence/HISTORICAL_OBJECTS_CI.json')
    require(review['status'] == 'both_previous_binary_transfer_obligations_completed', 'Review incomplete')
    require(ci['status'] == 'passed_bounded_inspection', 'Bounded CI inspection incomplete')
    require(set(ci['objects']) == set(review['objects']) == set(BLOBS), 'Historical object inventory differs')
    for name, (oid, size) in BLOBS.items():
        for item in (ci['objects'][name], review['objects'][name]):
            require(item['git_blob'] == oid and item['bytes'] == size and
                    item['byte_identity'] == 'verified', 'Historical object identity differs: ' + name)
        require(ci['objects'][name]['sha256'] == review['objects'][name]['sha256'],
                'Object digest records differ: ' + name)
    require(review['ci']['artifact_digest_independently_verified'] is True, 'Artifact identity unverified')
    require(review['archive']['members'] == 166 and review['archive']['unmatched_members'] == 0,
            'Archive inventory differs from the inspected package')
    rows = review['archive']['identity_map']
    require(len(rows) == 166 and len({r['archive_member'] for r in rows}) == 166,
            'Archive mapping incomplete or duplicated')
    for row in rows:
        path = (ROOT / row['repository_identity_source']).resolve()
        require(path.is_relative_to(ROOT), 'Archive comparison path escapes checkout')
        require(row['exact_bytes'] is True and sha(row['repository_identity_source']) == row['sha256'],
                'Recognized archive member differs: ' + row['archive_member'])
    require(review['png']['pixel_decode'] == 'passed', 'PNG decode not completed')
    require(review['publication_clearance'] is False and ci['publication_clearance'] is False,
            'Bounded checks are not public clearance')
    replay = load('publication/integration/CORE_PATCH_REPLAY.json')
    require(replay['starting_commit'] == START and replay['live_sources_changed'] is False,
            'Core correction proposal scope differs')
    require(sha(replay['patch']) == replay['patch_sha256'], 'Proposed patch digest differs')
    for item in replay['files']:
        require(sha(item['path']) == item['before_sha256'], 'Core proposal has been applied to live source')
    return {'passed': True, 'starting_commit': START,
            'inherited_files_unchanged': len(before['files']) - len(EDITORIAL),
            'recorded_editorial_changes': sorted(EDITORIAL),
            'historical_objects_reviewed': len(BLOBS), 'archive_identity_mappings': len(rows),
            'core_corrections_applied_to_live_source': False,
            'scope': 'Offline record consistency and preservation; no live settings query, scientific re-evaluation or public clearance.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = check()
    if args.output:
        require(not args.output.exists(), 'Use a fresh output file')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
