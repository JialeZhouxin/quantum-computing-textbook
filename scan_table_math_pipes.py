from pathlib import Path
import re


def is_sep(line: str) -> bool:
    s = line.strip().strip("|")
    return bool(s) and set(s.replace(" ", "")) <= set("-:")


def table_blocks(lines: list[str]):
    i = 0
    n = len(lines)
    while i < n - 1:
        if "|" in lines[i] and is_sep(lines[i + 1]):
            start = i
            j = i + 2
            while j < n and "|" in lines[j] and lines[j].strip():
                j += 1
            yield start, j, lines[start:j]
            i = j
            continue
        i += 1


def main() -> None:
    suspect = []
    for path in Path("docs").rglob("*.md"):
        lines = path.read_text(encoding="utf-8").splitlines()
        for start, end, rows in table_blocks(lines):
            for k, row in enumerate(rows):
                if is_sep(row):
                    continue
                for m in re.finditer(r"\$([^$]*\|[^$]*)\$", row):
                    seg = m.group(1)
                    if any(x in seg for x in (r"\vert", r"\lvert", r"\rvert", r"\|")):
                        # still may contain bare | elsewhere
                        pass
                    if re.search(r"(?<!\\)\|", seg.replace(r"\|", "")):
                        # remove known safe commands then check
                        cleaned = seg
                        for safe in (r"\vert", r"\lvert", r"\rvert"):
                            cleaned = cleaned.replace(safe, "")
                        cleaned = cleaned.replace(r"\|", "")
                        if "|" in cleaned:
                            suspect.append((str(path), start + k + 1, row, m.group(0)))

    print(f"suspect_count={len(suspect)}")
    for p, ln, row, math in suspect[:80]:
        print(f"{p}:{ln}")
        print(f"  row: {row}")
        print(f"  math: {math}")


if __name__ == "__main__":
    main()
