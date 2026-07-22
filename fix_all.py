"""
修复：
  1. $|0\rangle$ → $
  2. /cmd → \cmd （所有已知 LaTeX 命令）
"""
import os, re

BASE = "E:/02_Projects/AI/quantum-computing-textbook"

LATEX_COMMANDS = [
    'rangle', 'langle', 'theta', 'frac', 'alpha', 'beta', 'gamma', 'delta',
    'epsilon', 'zeta', 'eta', 'iota', 'kappa', 'lambda', 'mu', 'nu',
    'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi',
    'chi', 'psi', 'omega',
    'Gamma', 'Delta', 'Theta', 'Lambda', 'Xi', 'Pi', 'Sigma', 'Phi', 'Psi', 'Omega',
    'sum', 'prod', 'int', 'sqrt', 'partial', 'infty',
    'otimes', 'oplus', 'dagger', 'cdot', 'cdots', 'vdots', 'ddots',
    'begin', 'end', 'text', 'operatorname', 'mbox',
    'mathcal', 'mathbb', 'mathbf', 'mathrm',
    'tilde', 'bar', 'dot',
    'quad', 'qquad',
    'vert', 'Vert',
    'lvert', 'rvert', 'lbrace', 'rbrace',
    'lgroup', 'rgroup', 'lfloor', 'rfloor', 'lceil', 'rceil',
    'arrowvert', 'Arrowvert', 'bracevert',
    'newcommand', 'renewcommand', 'def',
    'choose',
]

files = []
for root, dirs, fnames in os.walk(BASE):
    for f in fnames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))
files.sort()

# 步骤1: $|0\rangle$ → $
print("=== 步骤1: 修复 $ 定界符 ===")
PAT_DOLLAR = b'$|0\rangle$'

total_dollar = 0
for fp in files:
    with open(fp, 'rb') as fh:
        data = fh.read()
    
    before = data.count(PAT_DOLLAR)
    if before == 0:
        continue
    
    passes = 0
    while True:
        new_data = data.replace(PAT_DOLLAR, b'$')
        passes += 1
        if len(new_data) == len(data):
            break
        data = new_data
    
    total_dollar += before
    rel = os.path.relpath(fp, BASE)
    old_kb = os.path.getsize(fp) // 1024
    new_kb = len(data) // 1024
    print(f"  {rel}: {before}处, {old_kb}KB → {new_kb}KB ({passes}轮)")
    
    with open(fp, 'wb') as fh:
        fh.write(data)

print(f"\n  → 总计修复 {total_dollar} 处\n")

# 步骤2: 恢复 LaTeX 反斜杠
print("=== 步骤2: 恢复 LaTeX 反斜杠 ===")
total_bs = 0
for fp in files:
    with open(fp, 'rb') as fh:
        data = fh.read()
    
    count = 0
    for cmd in LATEX_COMMANDS:
        pat = b'/' + cmd.encode()
        repl = b'\\' + cmd.encode()
        n = data.count(pat)
        if n:
            data = data.replace(pat, repl)
            count += n
    
    if count:
        total_bs += count
        rel = os.path.relpath(fp, BASE)
        print(f"  {rel}: {count}个命令")
        with open(fp, 'wb') as fh:
            fh.write(data)

print(f"\n  → 总计恢复 {total_bs} 个反斜杠\n")

# 步骤3: 最终检查
print("=== 最终检查 ===")
for fp in files:
    with open(fp, 'rb') as fh:
        data = fh.read()
    
    issues = []
    n1 = data.count(b'$|0')
    if n1:
        issues.append(f"{n1}个$|0残留")
    n2 = data.count(b'/rangle') + data.count(b'/langle') + data.count(b'/frac') + data.count(b'/theta')
    if n2:
        issues.append(f"{n2}个未恢复命令")
    sz_mb = f"{len(data)/1024/1024:.1f}MB" if len(data) > 1024*1024 else f"{len(data)/1024:.0f}KB"
    
    rel = os.path.relpath(fp, BASE)
    if issues:
        print(f"  ⚠ {rel} ({sz_mb}): {'; '.join(issues)}")
    else:
        print(f"  ✓ {rel} ({sz_mb})")
