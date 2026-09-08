#!/usr/bin/env python3
from pathlib import Path
import json,argparse
from rational_endpoint_constants import run
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 r=run();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n');print(r)
