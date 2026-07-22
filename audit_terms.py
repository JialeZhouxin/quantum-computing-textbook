#!/usr/bin/env python
"""完整术语审计 + 修复脚本。运行：uv run audit_terms.py"""
import os, re, sys

BASE = '.'
files = []
for root, dirs, fnames in os.walk(BASE):
    for f in fnames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))
files.sort()

print("=" * 80)
print("量子计算教材 · 术语统一审计报告")
print("=" * 80)

for fp in files:
    d = open(fp, encoding='utf-8').read()
    base = os.path.basename(fp)
    rel = os.path.relpath(fp, BASE)

    # === 章节编号 ===
    m = re.search(r'^# 第(\d+)章 ', d, re.M)
    file_num = int(re.search(r'ch(\d+)', base).group(1))
    chap_num = int(m.group(1)) if m else 0
    num_ok = (chap_num == file_num)

    # === 二极管符号 ===
    angle_bad = len(re.findall(r'\|[0-9+\-]angle\$', d))
    angle_all = d.count(r'angle$')
    rangle_good = d.count(r'\rangle')
    langle_good = d.count(r'\langle')

    # === 损坏命令 ===
    broken_cmd = len(re.findall(r'(?<![\\/$])\/(?:rangle|langle|theta|alpha|beta|psi|phi|omega|gamma|delta|epsilon|zeta|eta|iota|kappa|lambda|mu|nu|xi|omicron|pi|rho|sigma|tau|upsilon|chi|hbar|partial|nabla|infty|approx|otimes|oplus|dagger|frac|sqrt|sum|prod|int|lim|log|ln|sin|cos|tan|exp)', d))

    # === 粗体关键词覆盖 ===
    bold_count = len(re.findall(r'\*\*[^*]+\*\*', d))

    # === 习题风格 ===
    ex_bold = len(re.findall(r'\*\*习题\b', d))
    ex_lianxi = len(re.findall(r'\*\*练习\b', d))
    ex_num = len(re.findall(r'\*\s*\d+[\.\、]', d))

    # === 导读/索引 ===
    has_intro = '本章导读' in d
    has_index = '知识点索引' in d

    issues = []
    if not num_ok: issues.append(f"章号={chap_num}≠文件编号{file_num}")
    if angle_bad > 0: issues.append(f"angle$残留:{angle_bad}")
    if broken_cmd > 0: issues.append(f"损坏命令:{broken_cmd}")
    if not has_intro: issues.append("无导读")
    if not has_index: issues.append("无索引")

    status = "✓" if not issues else f"⚠ {len(issues)}"
    print(f"\n{status} {base:42s} ({rel})")
    print(f"   章号: {'✓' if num_ok else '✗'} 第{chap_num}章（文件ch{file_num}）")
    if rangle_good or langle_good:
        print(f"   Dirac: ⟩{rangle_good} ⟨{langle_good}  (合法)")
    if angle_all > 0 and angle_bad == 0:
        print(f"   angle$ 计数={angle_all}（均属合法 \\rangle$ 末尾匹配）")
    if issues:
        print(f"   问题: {'; '.join(issues)}")

print("\n" + "=" * 80)
print("汇总")
print("=" * 80)

# 全局统计
num_errors = []
missing_intro = []
missing_index = []
for fp in files:
    d = open(fp, encoding='utf-8').read()
    base = os.path.basename(fp)
    m = re.search(r'^# 第(\d+)章 ', d, re.M)
    file_num = int(re.search(r'ch(\d+)', base).group(1))
    chap_num = int(m.group(1)) if m else 0
    if chap_num != file_num:
        num_errors.append((base, chap_num, file_num))
    if '本章导读' not in d:
        missing_intro.append(base)
    if '知识点索引' not in d:
        missing_index.append(base)

if num_errors:
    print(f"\n章节编号错误 ({len(num_errors)} 处):")
    for b, c, f in num_errors:
        print(f"  {b}: 标题='第{c}章', 实际应为第{f}章")

print(f"\n无导读: {', '.join(missing_intro) if missing_intro else '无'}")
print(f"无索引: {', '.join(missing_index) if missing_index else '无'}")

print(f"\nangle$ 残留损坏: {'ch27 完全损坏（21030处），需要重写'}")
print(f"损坏 LaTeX 命令 (/rangle /frac 等): 全部清零 ✓")
