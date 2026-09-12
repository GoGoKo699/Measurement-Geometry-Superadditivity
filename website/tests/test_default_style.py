"""The accepted art reference applies to figures, not repository chrome."""
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[2]

def test_plain_documentation_chrome():
    css=(ROOT/'website/assets/style.css').read_text().lower()
    assert '--paper:#fff;' in css
    assert '.brand-mark{display:none}' in css
    assert 'georgia' not in css and 'times new roman' not in css
    palette=json.loads((ROOT/'website/palette.json').read_text())
    for color in set(palette['svg_mapping'].values()):
        assert color.lower() not in css
    assert 'background-image:' not in css and '@import' not in css

def test_acceptance_is_figure_only():
    palette=json.loads((ROOT/'website/palette.json').read_text())
    assert palette['status']=='accepted by the author; figures only'
    assert palette['svg_mapping']=={
        '#1b4264':'#304e66','#177d89':'#a34e38','#25313b':'#24343d',
        '#66727c':'#59676c','#dcedef':'#dee9df','#edf2f5':'#e8efea',
        '#d5dee4':'#ced9d3','#f7f9fa':'#f7f4ec'}
    text=(ROOT/'website/pages/visual-design.md').read_text()
    assert "GitHub's default" in text and 'figures only' in text
    assert 'navigation colors' in text

def test_presentation_change_preserves_math_sources():
    import importlib.util
    spec=importlib.util.spec_from_file_location('style_preservation_builder',ROOT/'website/build.py')
    builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)
    result=builder.verify_baseline()
    assert result['passed']
    assert result['approved_graphical_artifacts_unchanged']==27
    assert result['accepted_reader_svgs_unchanged']==3
