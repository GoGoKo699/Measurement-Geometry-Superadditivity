"""Read-only audit command recorder, separate from pinned repository sources."""
from pathlib import Path
import argparse, datetime, hashlib, json, os, subprocess, sys, time

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
PY = sys.executable

def run(name, args, timeout=180):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    tick = time.monotonic()
    p = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    log = OUT / (name+'.log')
    log.write_text(p.stdout+'\nSTDERR:\n'+p.stderr)
    result = dict(name=name, command=args, cwd=str(ROOT), started_utc=start,
                  returncode=p.returncode, duration_seconds=time.monotonic()-tick,
                  timeout_seconds=timeout, log=log.name,
                  log_sha256=hashlib.sha256(log.read_bytes()).hexdigest())
    with (OUT/'COMMANDS.jsonl').open('a') as stream:
        stream.write(json.dumps(result)+'\n')
    print(json.dumps(result), flush=True)
    return p.returncode

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline',type=Path,default=Path.cwd())
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--python',default=sys.executable)
    parser.add_argument('--site-output',default='build/audit-site')
    parser.add_argument('name',nargs='?')
    parser.add_argument('command',nargs=argparse.REMAINDER)
    args=parser.parse_args()
    ROOT=args.baseline.resolve(); OUT=args.output.resolve(); OUT.mkdir(parents=True,exist_ok=True); PY=args.python
    if args.name:
        raise SystemExit(run(args.name, args.command, timeout=600))
    commands = [
        ('reader-generated-check', [PY,'website/repository_preview.py','--check']),
        ('site-build', [PY,'website/build.py','--output',args.site_output]),
        ('site-static-check', [PY,'website/check.py','--site',args.site_output,
                               '--report',str(OUT/'SITE_CHECK.json')]),
    ]
    for name, args in commands:
        if run(name,args):
            raise SystemExit(1)
