from pathlib import Path
import re


def fix_text(text: str) -> str:
    # \rvertA / \rvert A -> \vert A
    text = re.sub(r"\\rvert\s*([A-Za-z\\])", r"\\vert \1", text)
    # <u \rvert v> -> <u \vert v>
    text = re.sub(
        r"\\langle\s*([^\\{}]+?)\\rvert\s*([^\\{}]+?)\\rangle",
        r"\\langle \1 \\vert \2\\rangle",
        text,
    )
    # <u\vert A\lvert v> -> <u\vert A\vert v>
    text = re.sub(
        r"\\langle\s*([^\\{}]+?)\\vert\s*([^\\{}]+?)\\lvert\s*([^\\{}]+?)\\rangle",
        r"\\langle \1\\vert \2\\vert \3\\rangle",
        text,
    )
    text = text.replace(r"\rvertA", r"\vert A")
    text = text.replace(r"\rvert A", r"\vert A")
    return text


def main() -> None:
    n = 0
    for path in Path("docs").rglob("*.md"):
        old = path.read_text(encoding="utf-8")
        new = fix_text(old)
        if new != old:
            path.write_text(new, encoding="utf-8", newline="\n")
            n += 1
    print(f"files_changed={n}")
    lines = Path(
        "docs/module-01-mathematical-foundations/ch01-linear-algebra.md"
    ).read_text(encoding="utf-8").splitlines()
    for i in range(629, 638):
        print(f"{i+1}: {lines[i]}")


if __name__ == "__main__":
    main()
