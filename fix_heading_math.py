from pathlib import Path
import re

# heading 内的 $...$ 映射为纯文本，避免侧栏 TOC 显示未渲染公式
RULES = [
    (r"\$\\mathbb\{R\}\^n\$", "Rⁿ"),
    (r"\$\\mathbb\{C\}\^n\$", "Cⁿ"),
    (r"\$\\mathbb\{R\}\^2\$", "R²"),
    (r"\$\\mathbb\{R\}\^3\$", "R³"),
    (r"\$\\mathbb\{C\}\^2\$", "C²"),
    (r"\$\\text\{Tr\}\(\\rho\^2\)\$", "Tr(ρ²)"),
    (r"\$O\(1\)\$", "O(1)"),
    (r"\$O\(\\log n\)\$", "O(log n)"),
    (r"\$O\(n\)\$", "O(n)"),
    (r"\$O\(n \\log n\)\$", "O(n log n)"),
    (r"\$O\(n\^2\)\$", "O(n²)"),
    (r"\$O\(2\^n\)\$", "O(2ⁿ)"),
    (r"\$R_x\(\\theta\)\$", "Rx(θ)"),
    (r"\$R_y\(\\theta\)\$", "Ry(θ)"),
    (r"\$R_z\(\\theta\)\$", "Rz(θ)"),
    (r"\$\|\\+\\rangle\$", "|+⟩"),
    (r"\$Z\$", "Z"),
    (r"\$\{R_Z, X, CZ\}\$", "{Rz, X, CZ}"),
    (r"\$U\^\{2\^k\}\$", "U^(2^k)"),
    (r"\$N=15\$", "N=15"),
    (r"\$2\^n\$", "2ⁿ"),
    (r"\$\|s\\rangle\$", "|s⟩"),
    (r"\$\|t\\rangle\$", "|t⟩"),
    (r"\$2 \\times 2\$", "2×2"),
    (r"\$\(n, k, d\)\$", "(n, k, d)"),
    (r"\$X\$", "X"),
    (r"\$\[7,4,3\]\$", "[7,4,3]"),
    (r"\$d\$", "d"),
    (r"\$E_C\$", "Ec"),
    (r"\$E_J\$", "Ej"),
    (r"\$E_J/E_C\$", "Ej/Ec"),
]

HEADING_RE = re.compile(r"^(#{1,6}\s+)(.*)$", re.M)


def strip_math(inner: str) -> str:
    inner = inner.replace(r"\mathbb{R}", "R").replace(r"\mathbb{C}", "C")
    inner = inner.replace(r"\times", "×").replace(r"\theta", "θ")
    inner = inner.replace(r"\rho", "ρ").replace(r"\log", "log")
    inner = re.sub(r"\\[a-zA-Z]+", "", inner)
    return inner.replace("{", "").replace("}", "").replace("\\", "")


def fix_heading(match: re.Match) -> str:
    prefix, title = match.group(1), match.group(2)
    if "$" not in title:
        return match.group(0)
    new_title = title
    for pat, rep in RULES:
        new_title = re.sub(pat, rep, new_title)
    if "$" in new_title:
        new_title = re.sub(r"\$([^$]+)\$", lambda m: strip_math(m.group(1)), new_title)
    return prefix + new_title


def main() -> None:
    changed = []
    for path in Path("docs").rglob("*.md"):
        old = path.read_text(encoding="utf-8")
        new = HEADING_RE.sub(fix_heading, old)
        if new != old:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed.append(str(path))

    print(f"files_changed={len(changed)}")
    for p in changed:
        print(p)

    left = []
    for path in Path("docs").rglob("*.md"):
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if re.match(r"^#{1,6}\s+", line) and "$" in line:
                left.append(f"{path}:{i}:{line}")
    print(f"remaining={len(left)}")
    for item in left:
        print(item)


if __name__ == "__main__":
    main()
