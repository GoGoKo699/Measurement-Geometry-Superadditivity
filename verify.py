#!/usr/bin/env python3
"""Verify package identity; --full executes the documented full reproduction."""
import argparse,json
from pathlib import Path
from baseline_tools import ROOT,integrity,write_json

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--report',type=Path);p.add_argument('--full',action='store_true');p.add_argument('--output',type=Path);a=p.parse_args()
 if a.full:
  if a.output is None:p.error('--full requires a fresh --output directory')
  import reproduce
  reproduce.run(a.output,full=True)
 else:
  r=integrity()
  if a.report:write_json(a.report,r)
  print(json.dumps(r,indent=2))
if __name__=='__main__':main()
