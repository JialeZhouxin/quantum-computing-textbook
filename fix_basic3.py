"""修复：$|0\rangle$ → $ （每个 $ 被替换成了 $|0\rangle$）"""
import os, re

BASE = "E:/02_Projects/AI/quantum-computing-textbook"
PAT = b'$|0\rangle$'  # 24 7c 30 0d 61 6e 67 6c 65 24
REPL = b'$'

files = []
for root, dirs, fnames in os.walk(BASE):
    for f in fnames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))
files.sort()

total_fixed = 0
total_remaining = 0
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
    fixed = before
    total_fixed += fixed
    
    # 同时检查是否还有残留 $|0 模式
    leftover = data.count(b'$|0')
    
    rel = os.path.relpath(fp, BASE)
    old_sz = os.path.getsize(fp)
    print(f"  {rel}: 修复 {fixed} 处, 残留 $|0: {leftover}, {old_sz//1024}KB → {len(data)//1024}KB ({passes} 轮)")
    
    with open(fp, 'wb') as fh:
        fh.write(data)

print(f"\n总计修复 {total_fixed} 处 $|0\\rangle$ 损坏")
