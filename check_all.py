"""检查所有文件当前损坏状态"""
import os, re, sys

BASE = "E:/02_Projects/AI/quantum-computing-textbook"
files = []
for root, dirs, fnames in os.walk(BASE):
    for f in fnames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))
files.sort()

for fp in files:
    with open(fp, 'rb') as f:
        d = f.read()
    sz = len(d)
    dl = d.count(b'$|0')
    mis = (d.count(b'/rangle') + d.count(b'/langle') + d.count(b'/theta') + 
           d.count(b'/frac') + d.count(b'/alpha') + d.count(b'/beta') + d.count(b'/psi'))
    garbage = len(re.findall(rb'\|11\\angle\$\|10', d)) + len(re.findall(rb'\|11\\angle\$\|11', d))
    
    rel = os.path.relpath(fp, BASE)
    sz_str = f"{sz/1024/1024:.1f}MB" if sz > 1024*1024 else f"{sz/1024:.0f}KB"
    issues = []
    if dl: issues.append(f"dollar_pipe:{dl}")
    if mis: issues.append(f"mis_cmd:{mis}")
    if garbage: issues.append(f"garbage:{garbage}")
    flag = " *" if dl or mis or garbage else " ok"
    detail = " | " + " ".join(issues) if issues else ""
    print(f"  {flag} {sz_str:>7s}  {rel}{detail}")
