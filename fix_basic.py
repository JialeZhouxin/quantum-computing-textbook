"""基础修复：重复替换 $|0角度$ → $，直到全部清除。"""
import os, re

BASE = "E:/02_Projects/AI/quantum-computing-textbook"
files = []
for root, dirs, fnames in os.walk(BASE):
    for f in fnames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))

files.sort()
print(f"找到 {len(files)} 个 .md 文件")

total_fixed = 0
for fp in files:
    with open(fp, 'r', encoding='utf-8') as fh:
        data = fh.read()
    
    # 记录原始 $|0角度$ 出现次数
    before = data.count('$|0角度$')
    if before == 0:
        continue
    
    # 反复替换直到不再变化
    prev = None
    passes = 0
    while prev is None or prev != data:
        prev = data
        data = data.replace('$|0角度$', '$')
        passes += 1
    
    after = data.count('$|0角度$')
    fixed = before
    total_fixed += fixed
    
    rel = os.path.relpath(fp, BASE)
    print(f"  {rel}: 替换 {fixed} 处 (共 {passes} 轮)")
    
    with open(fp, 'w', encoding='utf-8') as fh:
        fh.write(data)

print(f"\n总计修复 {total_fixed} 处 $|0角度$ 损坏")
