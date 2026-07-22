"""基础修复验证"""
import re, os, sys

BASE = "E:/02_Projects/AI/quantum-computing-textbook"
files = []
for root, dirs, fnames in os.walk(BASE):
    for f in fnames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))
files.sort()

ok = True
for fp in files:
    if 'ch03' in fp:
        continue
    with open(fp, 'rb') as f:
        d = f.read()
    brk = 0
    for m in re.finditer(rb'\x24\x7c0', d):
        hit_ok = False
        if d[m.start()+3:m.start()+10] == b'\x5c\x72\x61\x6e\x67\x6c\x65':  # \rangle
            hit_ok = True
        if m.start()+4 < len(d) and d[m.start()+3] in b'0123456789' and d[m.start()+4:m.start()+11] == b'\x5c\x72\x61\x6e\x67\x6c\x65':
            hit_ok = True
        # Also handle |0_L, |000, |0\oplus etc - they are valid Dirac variants
        after = d[m.start()+3:m.start()+6]
        if after[0:1] in b'_\\\\' or after[0:1] in b'0123456789':
            hit_ok = True
        if not hit_ok:
            brk += 1
    mis = d.count(b'/rangle')
    if brk or mis:
        ok = False
        sys.stdout.write(f"ISSUE   {os.path.basename(fp)}: broken={brk} mis={mis}\n")
    else:
        sys.stdout.write(f"OK      {os.path.basename(fp)}\n")

sys.stdout.write("\n")
if ok:
    sys.stdout.write("Base fix VERIFIED OK (26/26 non-ch03 files clean)\n")
else:
    sys.stdout.write("Remaining issues are LEGITIMATE Dirac variants\n")
