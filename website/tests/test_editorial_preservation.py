"""Editorial metadata must reconstruct frozen bytes and preserve mathematics."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil

import pytest

REPO=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('editorial_preservation_builder',REPO/'website/build.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
MODEL='docs/MODEL_AND_CLAIMS.md'
PROOF='docs/COMPLETE_PROOF.md'
LEDGER='provenance/SECTION_LEDGER.json'
RECORD='provenance/EDITORIAL_CORRECTIONS.json'
FIGURE='figures/approved/figure_01_channel_and_witness.svg'

def digest(data):
    return hashlib.sha256(data).hexdigest()

@pytest.fixture
def checkout(tmp_path,monkeypatch):
    """Use real corrected files and frozen hashes, with a small guard set."""
    old=json.loads((REPO/'website/provenance/baseline_manifest_v1.json').read_text())['files']
    selected=set(builder.EDITORIAL_FILES)|{PROOF,'README.md','STATUS.md',FIGURE}
    for rel in selected|{RECORD,'website/provenance/baseline_README.md','website/provenance/baseline_STATUS.md'}:
        target=tmp_path/rel;target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(REPO/rel,target)
    builder.dump(tmp_path/'website/provenance/baseline_manifest_v1.json',{'files':{p:old[p] for p in selected}})
    builder.dump(tmp_path/'provenance/APPROVED_FIGURE_HASHES.json',{'files':{FIGURE:old[FIGURE]}})
    monkeypatch.setattr(builder,'ROOT',tmp_path)
    monkeypatch.setattr(builder,'WEB',tmp_path/'website')
    return tmp_path

def test_valid_corrections_reconstruct_originals(checkout):
    result=builder.verify_baseline()
    assert result['baseline_members_with_verified_editorial_corrections']==9
    assert result['corrected_documentary_members']==5
    assert result['updated_documentary_identity_members']==4
    assert result['baseline_members_byte_unchanged']==2
    assert result['approved_graphical_artifacts_unchanged']==1

@pytest.mark.parametrize('rel',[MODEL,PROOF,FIGURE,'website/provenance/baseline_README.md','website/provenance/baseline_STATUS.md'])
def test_undeclared_source_or_preserved_export_change_rejected(checkout,rel):
    path=checkout/rel;path.write_bytes(path.read_bytes()+b'\nUnauthorized addition\n')
    with pytest.raises(ValueError):builder.verify_baseline()

def test_missing_correction_record_cannot_authorize_changes(checkout):
    (checkout/RECORD).unlink()
    with pytest.raises(ValueError,match='Protected scientific baseline changed'):builder.verify_baseline()

@pytest.mark.parametrize('case',[
    'unauthorized_path','empty_files','empty_replacements','no_op','empty_before',
    'empty_after','wrong_before_hash','wrong_after_hash','absent_replacement',
    'wrong_baseline','wrong_audit','invalid_date','unknown_field','malformed_replacement'])
def test_malformed_editorial_records_rejected(checkout,case):
    record=builder.load(checkout/RECORD);entry=record['files'][MODEL]
    if case=='unauthorized_path':record['files'][PROOF]=entry
    elif case=='empty_files':record['files']={}
    elif case=='empty_replacements':entry['replacements']=[]
    elif case=='no_op':entry['replacements'][0]['before']=entry['replacements'][0]['after']
    elif case=='empty_before':entry['replacements'][0]['before']=''
    elif case=='empty_after':entry['replacements'][0]['after']=''
    elif case=='wrong_before_hash':entry['before_sha256']='0'*64
    elif case=='wrong_after_hash':entry['after_sha256']='0'*64
    elif case=='absent_replacement':entry['replacements'][0]['after']='This replacement is absent.'
    elif case=='wrong_baseline':record['baseline_commit']='0'*40
    elif case=='wrong_audit':record['audit_commit']='0'*40
    elif case=='invalid_date':record['date']='2026-99-99'
    elif case=='unknown_field':record['allow_any_change']=True
    elif case=='malformed_replacement':entry['replacements'][0]={'before':123,'after':[]}
    builder.dump(checkout/RECORD,record)
    with pytest.raises(ValueError):builder.verify_baseline()

def record_additional_change(checkout,rel,before,after):
    path=checkout/rel;current=path.read_text()
    assert current.count(before)==1
    path.write_text(current.replace(before,after,1))
    record=builder.load(checkout/RECORD);entry=record['files'][rel]
    entry['replacements'].append({'before':before,'after':after})
    entry['after_sha256']=digest(path.read_bytes())
    builder.dump(checkout/RECORD,record)

def test_declaring_a_math_edit_still_does_not_authorize_it(checkout):
    text=(checkout/MODEL).read_text()
    equation=next(x for x in re.findall(r'\$[^$\n]+\$',text) if text.count(x)==1)
    record_additional_change(checkout,MODEL,equation,equation[:-1]+r'\,+0$')
    with pytest.raises(ValueError,match='Mathematical source changed'):builder.verify_baseline()

def test_declaring_another_ledger_change_does_not_authorize_it(checkout):
    record_additional_change(checkout,LEDGER,'"canonical_id": "M01"','"canonical_id": "M01-altered"')
    with pytest.raises(ValueError,match='extends beyond the M08 fragment hash'):builder.verify_baseline()

def test_an_updated_current_hash_cannot_hide_undeclared_changes(checkout):
    path=checkout/MODEL;path.write_bytes(path.read_bytes()+b'\nUnrecorded text.\n')
    record=builder.load(checkout/RECORD)
    record['files'][MODEL]['after_sha256']=digest(path.read_bytes())
    builder.dump(checkout/RECORD,record)
    with pytest.raises(ValueError,match='reconstruction differs'):builder.verify_baseline()

def test_ambiguous_replacement_rejected(checkout):
    record=builder.load(checkout/RECORD);entry=record['files'][MODEL]
    path=checkout/MODEL
    path.write_text(path.read_text()+entry['replacements'][0]['after'])
    entry['after_sha256']=digest(path.read_bytes());builder.dump(checkout/RECORD,record)
    with pytest.raises(ValueError,match='Ambiguous or absent'):builder.verify_baseline()

@pytest.mark.parametrize('rel,field',[
    ('provenance/CANONICAL_INPUTS.json','data/figures/figure1_original_witness140.json'),
    ('data/figures/SOURCE_IDENTITY.json','data/figures/figure1_original_witness140.json'),
    ('provenance/FIGURE_INPUTS.json','data/figures/figure1_comparison.csv')])
def test_declared_numerical_identity_change_rejected(checkout,rel,field):
    data=builder.load(checkout/rel)
    mapping=data.get('files',data.get('selected_members',data))
    old='"'+field+'": "'+mapping[field]+'"'
    new='"'+field+'": "'+'0'*64+'"'
    record_additional_change(checkout,rel,old,new)
    with pytest.raises(ValueError,match='extends beyond authorized hash fields'):builder.verify_baseline()

@pytest.mark.parametrize('rel,field,mapping',[
    ('provenance/CANONICAL_INPUTS.json',MODEL,'files'),
    ('data/figures/SOURCE_IDENTITY.json',MODEL,'selected_members'),
    ('data/figures/SOURCE_IDENTITY.json','manifest_sha256',None),
    ('provenance/FIGURE_INPUTS.json','data/figures/SOURCE_IDENTITY.json',None),
    ('provenance/FIGURE_INPUTS.json','data/figures/BUILD_RECORD.json',None)])
def test_allowed_identity_field_must_match_current_file(checkout,rel,field,mapping):
    path=checkout/rel;data=builder.load(path)
    values=data[mapping] if mapping else data
    old=values[field];values[field]='0'*64
    path.write_text(path.read_text().replace(old,values[field]))
    record=builder.load(checkout/RECORD);entry=record['files'][rel]
    changed=False
    for replacement in entry['replacements']:
        if old in replacement['after']:
            replacement['after']=replacement['after'].replace(old,values[field]);changed=True
    assert changed
    entry['after_sha256']=digest(path.read_bytes());builder.dump(checkout/RECORD,record)
    with pytest.raises(ValueError,match='does not identify|do not identify'):builder.verify_baseline()

@pytest.mark.parametrize('before,after',[
    ('"figure2_noise_grid": 1001','"figure2_noise_grid": 1000'),
    ('"plot_decimal_digits": 17','"plot_decimal_digits": 16')])
def test_declared_figure_build_numerical_contract_change_rejected(checkout,before,after):
    rel='data/figures/BUILD_RECORD.json'
    record_additional_change(checkout,rel,before,after)
    # Check this record first so the structural guard, rather than a dependent
    # file digest, is the reason the changed numerical contract is rejected.
    record=builder.load(checkout/RECORD)
    record['files']={rel:record['files'][rel],**record['files']}
    builder.dump(checkout/RECORD,record)
    with pytest.raises(ValueError,match='extends beyond authorized hash fields'):builder.verify_baseline()
