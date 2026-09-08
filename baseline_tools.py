"""Packaging/orchestration helpers. No scientific entropy evaluator lives here."""
from __future__ import annotations
import ast,hashlib,json,re
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def sha(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path:Path):return json.loads(path.read_text(encoding='utf-8'))
def write_json(path:Path,value):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
def require(condition,msg):
 if not condition:raise ValueError(msg)

def segment(path:Path,anchor:str):
 lines=path.read_text().splitlines(keepends=True)
 hits=[i for i,l in enumerate(lines) if l.strip()==f'<a id="{anchor}"></a>']
 require(len(hits)==1,'missing/repeated canonical anchor: '+anchor)
 start=hits[0];end=len(lines)
 for j in range(start+1,len(lines)):
  if re.fullmatch(r'<a id="(?:m\d{2}|p\d{2})"></a>',lines[j].strip()):end=j;break
 return start+1,end,''.join(lines[start:end]).encode()

def check_provenance(root=ROOT):
 reg=read(root/'provenance/SOURCE_REGISTER.json');data={}
 for s in reg['sources']:
  p=root/s['original_local_path'];require(p.is_file(),'missing exact source: '+s['id'])
  require(sha(p)==s['sha256'],'source hash: '+s['id']);data[s['id']]=p.read_bytes()
  if s.get('baseline_path'):require((root/s['baseline_path']).is_file(),'missing active mapped source: '+s['id'])
 count=0;units={}
 for u in read(root/'provenance/SECTION_LEDGER.json')['units']:
  l,r,raw=segment(root/u['canonical_file'],u['canonical_anchor'])
  require((l,r)==(u['canonical_line_start'],u['canonical_line_end']),'canonical line range changed: '+u['canonical_id'])
  require(hashlib.sha256(raw).hexdigest()==u['canonical_fragment_sha256'],'canonical fragment changed: '+u['canonical_id'])
  for s in u['sources']:
   b=data[s['source_id']];require(hashlib.sha256(b).hexdigest()==s['source_file_sha256'],'original source identity mismatch')
   lines=b.decode().splitlines(keepends=True);l,r=s['line_start'],s['line_end']
   require(1<=l<=r<=len(lines),'invalid source line span')
   require(hashlib.sha256(''.join(lines[l-1:r]).encode()).hexdigest()==s['fragment_sha256'],'source fragment changed: '+s['source_id'])
   count+=1
  units[u['canonical_id']]=u
 require(len(units)==23,'canonical proof/model unit count')
 claims=read(root/'provenance/CLAIM_COVERAGE.json')['claims']
 require({c['id'] for c in claims}=={f'C{i}'for i in range(1,8)},'claim map coverage')
 for c in claims:
  require(all(p in units for p in c['canonical_proof_sections']),'absent proof dependency')
 graph=read(root/'provenance/PROOF_GRAPH.json')['dependencies'];active=set();done=set()
 def visit(v):
  require(v not in active,'cyclic proof graph')
  if v in done:return
  require(v in units,'missing graph unit');active.add(v)
  for child in graph[v]:visit(child)
  active.remove(v);done.add(v)
 for v in graph:visit(v)
 require((root/'docs/FROZEN_ARGUMENT.md').read_bytes()==data['S1'],'frozen argument changed')
 return {'source_identities':len(data),'canonical_units':len(units),'source_fragments':count,'claims':len(claims),'proof_graph_acyclic':True}

def check_protected(root=ROOT):
 protected=read(root/'provenance/APPROVED_FIGURE_HASHES.json')['files']
 for rel,digest in protected.items():
  require((root/rel).is_file() and sha(root/rel)==digest,'approved artifact changed: '+rel)
 return len(protected)

def check_inputs(root=ROOT):
 for file,nested in [('provenance/CANONICAL_INPUTS.json',True),('provenance/FIGURE_INPUTS.json',False)]:
  m=read(root/file);m=m['files']if nested else m
  for rel,h in m.items():require((root/rel).is_file() and sha(root/rel)==h,'input identity mismatch: '+rel)
 return True

def check_links(root=ROOT):
 total=0
 # Provenance snapshots have historical links; they are not current instructions.
 current=list(root.glob('*.md'))+list((root/'docs').glob('*.md'))+list((root/'figures').glob('*.md'))
 for p in current:
  if p.name=='FROZEN_ARGUMENT.md':continue
  for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
   if re.match(r'^(https?://|mailto:)',target):continue
   path,sep,anchor=target.partition('#');dest=(p.parent/path)if path else p
   require(dest.exists(),f'broken link {p.relative_to(root)} -> {target}')
   if sep and anchor and dest.suffix=='.md':
    require(f'<a id="{anchor}"></a>' in dest.read_text(),f'broken explicit anchor {target}')
   total+=1
 return total

def code_boundaries(root=ROOT):
 # Independent arithmetic routes must not import one another's packages/files.
 algorithms={'integer':{'dyadic_interval'},'mpmath':{'mpmath','witness_formula'},'decimal':{'decimal_interval'}}
 cross={'integer':{'decimal_interval','cross_backend','verify_certificate'},'mpmath':{'decimal_interval','dyadic_interval','certify_all_noise','verify_certificate'},'decimal':{'mpmath','dyadic_interval','cross_backend','certify_all_noise'}}
 for group in algorithms:
  for p in (root/'verification'/group).glob('*.py'):
   names=[]
   for node in ast.walk(ast.parse(p.read_text())):
    if isinstance(node,ast.Import):names.extend(a.name.split('.')[0]for a in node.names)
    elif isinstance(node,ast.ImportFrom) and node.module:names.append(node.module.split('.')[0])
   require(not cross[group].intersection(names),'checker independence collapsed: '+str(p))
 for top in ('verification','numerics','figures/code'):
  for p in (root/top).rglob('*.py'):
   text=p.read_text()
   require('/mnt/data/' not in text and '/home/oai/' not in text,'runtime-specific path: '+str(p))
   # Active source/code may state historical origins, but may not load ZIPs or
   # cross back into an old source tree as an operational dependency.
   for node in ast.walk(ast.parse(text)):
    if isinstance(node,ast.Call):
     fn=node.func
     name=fn.attr if isinstance(fn,ast.Attribute) else fn.id if isinstance(fn,ast.Name) else ''
     require(name not in {'ZipFile','extractall'},'archive extraction in active runtime: '+str(p))
 return True

def integrity(root=ROOT,manifest=True):
 p=check_provenance(root);n=check_protected(root);check_inputs(root);links=check_links(root);code_boundaries(root)
 forbidden=[]
 for x in root.rglob('*'):
  if x.is_file() and not any(v in x.parts for v in ('build','.venv','__pycache__','.pytest_cache','.git')) and x.suffix.lower() in {'.zip','.tar','.gz','.tex','.tikz','.ttf','.otf','.woff','.woff2'}:forbidden.append(str(x.relative_to(root)))
 require(not forbidden,'historical archive or forbidden file types: '+str(forbidden))
 m=root/'BASELINE_MANIFEST.json';entries=0
 if manifest:
  require(m.is_file(),'baseline manifest missing')
  for rel,h in read(m)['files'].items():require((root/rel).is_file() and sha(root/rel)==h,'baseline member changed: '+rel);entries+=1
 return {'passed':True,**p,'approved_artifacts_unchanged':n,'current_document_links':links,'independent_verifier_boundaries':True,'nested_archives_required':False,'baseline_manifest_files':entries,'scope':'Packaging/provenance integrity, not mathematical entropy verification.'}

def compare_figure_reproduction(out:Path,root=ROOT):
 protected=read(root/'provenance/APPROVED_FIGURE_HASHES.json')['files'];records=[]
 for rel,digest in protected.items():
  sub=Path(rel).relative_to('figures/approved');path=out/sub
  require(path.is_file() and sha(path)==digest,'rendered approved figure differs: '+str(sub))
  records.append(str(sub))
 return {'passed':True,'artifacts_byte_identical':len(records),'files':records}

def compare_data(out:Path,root=ROOT):
 records=[]
 for p in (root/'data/figures').iterdir():
  if p.is_file():
   require((out/p.name).is_file() and p.read_bytes()==(out/p.name).read_bytes(),'rebuilt figure input changed: '+p.name);records.append(p.name)
 return {'passed':True,'files_byte_identical':len(records),'files':sorted(records)}
