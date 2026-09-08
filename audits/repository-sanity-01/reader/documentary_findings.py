"""Reproduce narrowly scoped stale-path and local-preview documentation findings."""
from pathlib import Path
import argparse, json, re, subprocess, sys
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--baseline',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args(); root=args.baseline.resolve(); out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)

text=(root/'figures/FIGURE_SPECIFICATIONS.md').read_text()
paths=sorted(set(re.findall(r'`(data/[^`]+)`',text)))
mislocated=[]
for rel in paths:
    if '/' in rel[5:]:continue
    current='data/figures/'+rel[5:]
    if not (root/rel).exists() and (root/current).is_file():
        mislocated.append(dict(displayed_path=rel,exists=False,actual_path=current,actual_exists=True,
            lines=[n for n,line in enumerate(text.splitlines(),1) if '`'+rel+'`' in line]))
helptext=subprocess.check_output([sys.executable,'-m','http.server','--help'],text=True)
commands=[dict(line=n,command=line) for n,line in enumerate((root/'WEBSITE.md').read_text().splitlines(),1)
          if 'python -m http.server' in line and '--bind' not in line]
assert commands and 'default: all interfaces' in helptext
stale=[dict(line=n,text=line) for n,line in enumerate((root/'docs/MODEL_AND_CLAIMS.md').read_text().splitlines(),1)
       if 'no remote repository has been created' in line]
result=dict(baseline=str(root),missing_documented_paths=mislocated,
            website_commands_without_loopback_binding=commands,
            python_http_server_help=helptext,stale_current_remote_repository_statement=stale,
            classification='minor documentation defects; no source/output edits performed; no external disclosure claimed')
(out/'DOCUMENTARY_FINDINGS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
