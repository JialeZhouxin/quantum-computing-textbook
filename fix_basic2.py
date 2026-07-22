"""修复：$|0\r...$ → $\...$ ，并清理 ch03/ch27 中的大块垃圾"""
import os, re

BASE = "E:/02_Projects/AI/quantum-computing-textbook"

files = []
for root, dirs, fnames in os.walk(BASE):
    for f in fnames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))
files.sort()

# 第1步：修复 $|0\r 开头的 LaTeX 损坏
# 模式：$|0\r 后面跟 LaTeX 命令名，直到下一个 $
# 原始 LaTeX 命令被替换为 |0\r + 命令名
# 需要恢复为 \ + 命令名
total_rangle = 0
total_other = 0

for fp in files:
    with open(fp, 'rb') as fh:
        data = fh.read()
    
    orig_len = len(data)
    
    # 替换模式 1: $|0\r + 字母序列 + $ → $\ + 字母序列 + $
    # 即 $|0\r(X)$ → $\X$ (其中 X 是字母序列)
    data, n1 = re.subn(rb'\$\|0\r([a-zA-Z]+)\$', rb'$\\\1$', data)
    total_rangle += n1
    
    # 替换模式 2: $|0\r + 字母序列 + ... 直到不是字母
    # 处理类似 $|0\rtheta$ 等情况
    # 实际上上面已经覆盖了所有 \r[字母] 模式
    
    # 替换模式 3: $|0 但后面没有 \r 的特殊情况
    # 先统计
    remaining = data.count(b'$|0')
    
    rel = os.path.relpath(fp, BASE)
    if n1 > 0 or remaining > 0:
        print(f"  {rel}: 修复 {n1} 处 LaTeX 命令, 仍有 {remaining} 处 $|0")
        with open(fp, 'wb') as fh:
            fh.write(data)
    else:
        print(f"  {rel}: 无变化")

print(f"\n共修复 {total_rangle} 处 LaTeX 命令损坏")

# 第2步：统计所有文件大小，标记需要额外处理的
print("\n--- 文件大小检查 ---")
for fp in files:
    sz = os.path.getsize(fp)
    rel = os.path.relpath(fp, BASE)
    print(f"  {sz:>10,} B  {rel}")
