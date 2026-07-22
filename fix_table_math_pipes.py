from pathlib import Path
import re


def is_sep(line: str) -> bool:
    # 兼容 |:---:|:---:| 与 :--- | ---:
    s = line.strip()
    if not s:
        return False
    # 去掉首尾 pipe 后，只允许 - : | 空格
    core = s.strip("|")
    return bool(core) and set(core.replace(" ", "")) <= set("-:|")


def table_blocks(lines: list[str]):
    i = 0
    n = len(lines)
    while i < n - 1:
        # 支持标准 pipe 表：header 下一行是 :--- 分隔行
        if "|" in lines[i] and is_sep(lines[i + 1].replace(" ", "")):
            start = i
            j = i + 2
            while j < n and "|" in lines[j] and lines[j].strip():
                j += 1
            yield start, j, lines[start:j]
            i = j
            continue
        i += 1


def fix_math_segment(seg: str) -> str:
    """把公式片段中的裸 | 换成 LaTeX 竖线命令。"""
    # 已转义/命令化的先保护
    tokens: list[str] = []

    def protect(m: re.Match) -> str:
        tokens.append(m.group(0))
        return f"@@TOK{len(tokens)-1}@@"

    # 保护 \| \vert \lvert \rvert \big| \Big| 等
    protected = re.sub(
        r"\\(?:vert|lvert|rvert|lVert|rVert|mid|nmid)|\\\|",
        protect,
        seg,
    )

    # 常见狄拉克模式
    protected = protected.replace(r"|0\rangle", r"\lvert 0\rangle")
    protected = protected.replace(r"|1\rangle", r"\lvert 1\rangle")
    protected = protected.replace(r"|+\rangle", r"\lvert +\rangle")
    protected = protected.replace(r"|-\rangle", r"\lvert -\rangle")
    protected = protected.replace(r"|v\rangle", r"\lvert v\rangle")
    protected = protected.replace(r"|u\rangle", r"\lvert u\rangle")
    protected = protected.replace(r"|s\rangle", r"\lvert s\rangle")
    protected = protected.replace(r"|t\rangle", r"\lvert t\rangle")
    protected = protected.replace(r"|psi\rangle", r"\lvert \psi\rangle")
    protected = protected.replace(r"|\psi\rangle", r"\lvert \psi\rangle")
    protected = protected.replace(r"|phi\rangle", r"\lvert \phi\rangle")
    protected = protected.replace(r"|\phi\rangle", r"\lvert \phi\rangle")

    # 左矢 <x|
    protected = re.sub(r"\\langle\s*([^|\\]+)\|", r"\\langle \1\\rvert", protected)
    # 右矢 |x>
    protected = re.sub(r"\|([^|\\]+)\\rangle", r"\\lvert \1\\rangle", protected)
    # 内积 <u | v>
    protected = re.sub(
        r"\\langle\s*([^|\\]+)\s*\|\s*([^|\\]+)\\rangle",
        r"\\langle \1 \\vert \2\\rangle",
        protected,
    )
    # 矩阵元 <u|A|v>
    protected = re.sub(
        r"\\langle\s*([^|\\]+)\|([^|\\]+)\|([^|\\]+)\\rangle",
        r"\\langle \1\\vert \2\\vert \3\\rangle",
        protected,
    )

    # 剩余裸 |
    protected = protected.replace("|", r"\vert ")

    # 还原保护 token
    def restore(m: re.Match) -> str:
        return tokens[int(m.group(1))]

    return re.sub(r"@@TOK(\d+)@@", restore, protected)


def fix_row(row: str) -> str:
    def repl(m: re.Match) -> str:
        return f"${fix_math_segment(m.group(1))}$"

    return re.sub(r"\$([^$]+)\$", repl, row)


def main() -> None:
    changed_files = []
    total_rows = 0
    for path in Path("docs").rglob("*.md"):
        lines = path.read_text(encoding="utf-8").splitlines()
        new_lines = lines[:]
        touched = False
        for start, end, rows in table_blocks(lines):
            for k, row in enumerate(rows):
                if is_sep(row):
                    continue
                if "$" not in row or "|" not in row:
                    continue
                # 只处理单元格公式里含 |
                if not re.search(r"\$[^$]*\|[^$]*\$", row):
                    continue
                fixed = fix_row(row)
                if fixed != row:
                    new_lines[start + k] = fixed
                    touched = True
                    total_rows += 1
        if touched:
            path.write_text("\n".join(new_lines) + "\n", encoding="utf-8", newline="\n")
            changed_files.append(str(path))

    print(f"files_changed={len(changed_files)}")
    print(f"rows_changed={total_rows}")
    for p in changed_files:
        print(p)


if __name__ == "__main__":
    main()
