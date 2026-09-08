import json, os, pathlib, resource, subprocess, sys, time, datetime
root=pathlib.Path(__file__).resolve().parent
name=sys.argv[1]; cmd=sys.argv[2:]
start=time.monotonic(); when=datetime.datetime.now(datetime.timezone.utc).isoformat()
env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','MPLBACKEND':'Agg','PYTHONUNBUFFERED':'1'}
assert not (root/(name+'.log')).exists() and not (root/(name+'.json')).exists(), 'Fresh command record required'
with (root/(name+'.log')).open('x') as f:
    p=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,env=env)
rec={'name':name,'command':cmd,'cwd':os.getcwd(),'started_utc':when,'duration_seconds':time.monotonic()-start,'returncode':p.returncode,'maxrss_children_kib':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,'env_overrides':{k:env[k] for k in ['PYTHONDONTWRITEBYTECODE','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MPLBACKEND','PYTHONUNBUFFERED']},'python_optimized':bool(sys.flags.optimize)}
(root/(name+'.json')).write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec),flush=True)
sys.exit(p.returncode)
