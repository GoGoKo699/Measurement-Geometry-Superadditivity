"""Fetch every unique linked local site resource over real loopback HTTP.

This is an HTTP/download check, not a browser-rendering or JavaScript test.
The review server always binds to 127.0.0.1 and closes on completion.
"""
from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlsplit, unquote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse, hashlib, json, threading

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--site',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args(); site=args.site.resolve(); out=args.output.resolve(); out.mkdir(parents=True,exist_ok=True)

class Handler(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass

resources={p.name for p in site.glob('*.html')}
for p in site.glob('*.html'):
    soup=BeautifulSoup(p.read_text(),'html.parser')
    for tag,attributes in [('a',['href']),('img',['src','data-themed','data-original']),('script',['src']),('link',['href'])]:
        for el in soup.find_all(tag):
            for attribute in attributes:
                u=urlsplit(el.get(attribute,''))
                if u.scheme or u.netloc or not u.path:continue
                target=(p.parent/unquote(u.path)).resolve()
                assert target.is_relative_to(site) and target.is_file()
                resources.add(target.relative_to(site).as_posix())

server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(site)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
base='http://127.0.0.1:'+str(server.server_address[1]); records=[]
try:
    for relative in sorted(resources):
        with urlopen(base+'/'+relative,timeout=10) as response:
            raw=response.read()
            assert response.status==200
        expected=(site/relative).read_bytes(); assert raw==expected
        records.append(dict(resource=relative,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),http_status=200))
finally:
    server.shutdown();server.server_close();thread.join()

result=dict(passed=True,mode='actual loopback HTTP; no browser or JavaScript execution',
            bound_host='127.0.0.1',resources_checked=len(records),
            returned_bytes=sum(r['bytes'] for r in records),every_response_byte_identical_to_local_file=True,
            third_party_requests=0,records=records)
(out/'HTTP_LINK_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
