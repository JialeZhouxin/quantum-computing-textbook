"""修复：$|0\r\rangle$ → $ （每个 $ 被替换成了 $|0\r\rangle$）"""
import os

BASE = "E:/02_Projects/AI/quantum-computing-textbook"
# 原始字节: 24 7c 30 0d 61 6e 67 6c 65 24
# 即 $|0\r\rangle$
PAT = b'$|0\r\rangle$'
REPL = b'$'

files = []
for root, dirs, fnames in os.walk(BASE):
    for f in fnames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))
files.sort()

total_fixed = 0
for fp in files:
    with open(fp, 'rb') as fh:
        data = fh.read()
    
    before = data.count(PAT)
    if before == 0:
        continue
    
    # 反复替换直到全部清除
    passes = 0
    while True:
        new_data = data.replace(PAT, REPL)
        passes += 1
        if len(new_data) == len(data):
            break
        data = new_data
    
    after = data.count(PAT)
    total_fixed += before
    
    leftover = data.count(b'$|0')
    old_sz = os.path.getsize(fp)
    rel = os.path.relpath(fp, BASE)
    sz_mb = f"{old_sz/1024/1024:.1f}MB" if old_sz > 1024*1024 else f"{old_sz/1024:.0f}KB"
    new_sz_mb = f"{len(data)/1024/1024:.1f}MB" if len(data) > 1024*1024 else f"{len(data)/1024:.0f}KB"
    print(f"  {rel}: {before} \u5904\u4fee\u590d, \u6b8b\u7559 $|0: {leftover}, {sz_mb} \u2192 {new_sz_mb} ({passes} \u8f6e)")
    
    with open(fp, 'wb') as fh:
        fh.write(data)

print(f"\n\u603b\u8ba1\u4fee\u590d {total_fixed} \u5904 $|0\\r\\rangle$ \u635f\u574f")
