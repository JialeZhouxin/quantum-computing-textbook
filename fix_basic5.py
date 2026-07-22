"""
修复：$|0\r 被注入到每个 LaTeX $ 前。
模式为 $|0\r + 命令名 + $，其中 \r 是 0x0d（回车），命令名是 angle, langle, theta, frac, alpha 等。
修复策略：
  1. 重复替换 $|0\r + 非空白字母序列 + $ 为 $\字母序列$
  2. 清除所有剩余 $|0
"""
import os, re

BASE = "E:/02_Projects/AI/quantum-computing-textbook"

files = []
for root, dirs, fnames in os.walk(BASE):
    for f in fnames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))
files.sort()

total_pat1 = 0
for fp in files:
    with open(fp, 'rb') as fh:
        data = fh.read()
    
    orig_len = len(data)
    
    # 模式：$|0\r + 字母序列 + $ → $\字母序列$
    # 反复替换，直到不再变化
    prev = None
    while prev is None or prev != data:
        prev = data
        data = re.sub(rb'\$\|0\r([a-zA-Z]+)\$', rb'$\\\1$', data)
    
    pat1 = data.count(b'$|0')
    
    # 检查是否有其他 $|0 模式残留
    leftover = data.count(b'$|0')
    
    if orig_len != len(data) or pat1 > 0:
        rel = os.path.relpath(fp, BASE)
        print(f"  {rel}: {'有残留' if leftover else '干净'}, {orig_len//1024}KB → {len(data)//1024}KB")
        with open(fp, 'wb') as fh:
            fh.write(data)

print("\n替换完毕。检查各文件状态：")
for fp in files:
    with open(fp, 'rb') as fh:
        data = fh.read()
    leftover = data.count(b'$|0')
    if leftover:
        rel = os.path.relpath(fp, BASE)
        print(f"  ⚠ {rel}: 还有 {leftover} 个 $|0 残留")
