---
name: md-to-styled-html
description: Convert markdown to styled HTML with KaTeX; includes math/table/heading pitfalls from textbook ops
---

# Markdown to Styled HTML

## Quick start

1. Read the markdown file to understand content type (academic tutorial, API docs, course notes)
2. Locate awesome-design-md style library (see below)
3. Scan 3-5 candidate DESIGN.md files, pick best match
4. **Preflight markdown for math/table/heading traps** (see "Hard-won pitfalls")
5. Generate single-file HTML with KaTeX for math, responsive layout, sidebar nav
6. Write to same directory as source .md file
7. Verify: open HTML, check display math, headings-with-symbols, and any table that contains `|`

## Locate style library

Check in order:
- User-provided path
- `./design-md/` or `./awesome-design-md/` in cwd
- `~/.agents/skills/awesome-design-md/` or similar
- Ask user to clone from `https://github.com/VoltAgent/awesome-design-md`

Use `ls design-md/` to list available styles. Use `head -20 design-md/<style>/DESIGN.md` to preview.

## Style matching

Read the markdown first. Then match content to style:

| Content type | Good matches | Avoid |
|---|---|---|
| Academic tutorial, long-form teaching | WIRED, Notion, IBM | Binance, Ferrari, Stripe |
| Developer docs, API reference | Mintlify, IBM, Expo | Apple, Nike, Airbnb |
| Technical blog, engineering notes | Cursor, Vercel, Warp | Mastercard, Starbucks |
| Course notes with code | Cursor, Mintlify, Supabase | Lamborghini, Bugatti |

Read full DESIGN.md of top 2 candidates. Present recommendation with 1-sentence reason. Wait for user confirmation.

## HTML structure

Single file, no external CSS/JS dependencies except:
- Google Fonts (load via `<link>`)
- KaTeX CSS+JS (load via CDN `<link>` + `<script defer>`)

Required sections:
- `<head>` with meta charset, viewport, cache-control, title
- Fixed sidebar with hierarchical nav (h1/h2/h3 links)
- Main content: masthead (category + title + meta) → sections → appendix → footer
- KaTeX auto-render on DOMContentLoaded
- Active nav highlighting on scroll

## Typography mapping

Map DESIGN.md tokens to available fonts:
- Display/hero: Playfair Display → WiredDisplay, NotionSerif
- Body serif: Lora → BreveText, Tiempos
- Structure sans: Inter → Apercu, Geist, Plex Sans
- Code/mono: JetBrains Mono → Geist Mono, Plex Mono

## Formula handling

Use KaTeX `renderMathInElement` with delimiters:
- `$$...$$` for display math (centered, numbered optional)
- `$...$` for inline math

Also accept `\(...\)` / `\[...\]` if source already uses them.

### Display math format (strict)

Always emit / require:

```md
前文

$$
公式
$$

后文
```

Never glue display fence to previous text:

```md
前文：
$$
公式
$$
```

Never insert blank lines **inside** the `$$` fence only to "make space":

```md
$$

公式

$$
```

That can split one math block into bare paragraphs.

### Renderer rules

- Prefer wrapping converted math nodes with a dedicated class, e.g. `class="arithmatex"`, **or** run KaTeX auto-render over the whole content root.
- If using "process only this class" mode, every math node must get that class; bare `$$...$$` left in HTML shows as raw text.
- Load KaTeX CSS + auto-render; call `renderMathInElement(document.body, {...})` after DOM ready.
- For SPA / Instant Navigation page swaps: re-typeset after content replace. Single-file static HTML usually only needs first load.

### Heading math (sidebar-safe)

**Do not put `$...$` in headings if the sidebar/TOC strips HTML.**

Why:
1. Body heading may become `<span class="math">\(\mathbb{R}^n\)</span>`
2. TOC generators often keep **text only** → sidebar shows raw `\(\mathbb{R}^n\)`
3. KaTeX will not re-scan stripped TOC text unless you explicitly typeset the nav

Rule:
- Headings → Unicode / plain ASCII symbols
- Body prose/formulas → keep full LaTeX

Examples:

| Bad heading | Good heading |
|---|---|
| `### 1.2.2 $\mathbb{R}^n$ 和 $\mathbb{C}^n$` | `### 1.2.2 Rⁿ 和 Cⁿ` |
| `#### $O(n^2)$ 平方时间` | `#### O(n²) 平方时间` |
| `### $R_x(\theta)$ 门` | `### Rx(θ) 门` |
| `### $\lvert +\rangle$ 态` | `### \|+⟩ 态` |

Common Unicode replacements:
- `^n` → `ⁿ`, `^2` → `²`, `^3` → `³`
- `\theta` → `θ`, `\rho` → `ρ`
- `\times` → `×`
- `\mathbb{R}` → `R`, `\mathbb{C}` → `C`
- titles with kets → `|+⟩` / `|ψ⟩`

## Tables

Use hairline borders (`1px solid #e0e0e0`), header with bottom border (`2px solid #000`), hover state on rows. No vertical borders.

### Pipe tables + math (critical)

Markdown pipe tables treat **every bare `|` as a column separator**, including `|` inside `$...$`.

They do **not** protect math first.

Bad (columns explode):

```md
| 狄拉克 | 说明 |
|:---:|:---|
| $|v\rangle$ | 右矢 |
| $\langle u|A|v\rangle$ | 矩阵元 |
```

Good (table-safe LaTeX):

```md
| 狄拉克 | 说明 |
|:---:|:---|
| $\lvert v\rangle$ | 右矢 |
| $\langle u\vert A\vert v\rangle$ | 矩阵元 |
```

Replacement map for cell math:

| Meaning | Do not write in tables | Write instead |
|---|---|---|
| ket \|ψ⟩ | `$|ψ\rangle$` | `$\lvert ψ\rangle$` |
| bra ⟨ψ\| | `$\langle ψ|$` | `$\langle ψ\rvert$` |
| single bar | bare `|` | `\vert` |
| norm / double bar | `$\|v\|$` / bare | `$\lVert v\rVert$` |

Parser note for custom HTML emitters:
- Detect pipe table with **two-phase** rule: header line with `|` **and** next line matching separator `|---|` / `|:---:|`
- Only then enter table mode
- Skip separator line
- Exit on first non-pipe line
- When serializing cells, still prefer `\vert` forms so source remains portable to MkDocs/GitHub/Pandoc

## Responsive

- Desktop: sidebar fixed 280px, main content max-width 800px
- Mobile (<1024px): sidebar hidden, full-width content
- Print: hide sidebar, black links

## Hard-won pitfalls (quantum textbook / MkDocs ops)

These look like "renderer bugs" but are usually **source shape + pipeline** issues.

### Pitfall A — Display math shows raw `$$`

**Symptom:** page shows `$$ a+bi=... $$` as plain text; inline `$z$` works.

**Cause:**
1. No blank line before/after display `$$` block → pipeline does not promote it to a math node
2. Or auto-render limited to a class (e.g. only `.arithmatex`) and the block never got that class

**Fix:**
1. Normalize all display blocks to blank-line-wrapped `$$\n...\n$$`
2. Ensure renderer processes whole content root, or every math node has the expected class
3. Verify HTML: good nodes look like `\[ ... \]` / math spans; bad nodes still contain literal `$$`

### Pitfall B — Heading / TOC looks unrendered

**Symptom:** body title maybe OK, sidebar shows `1.2.2 \(\mathbb{R}^n\) ...`

**Cause:** TOC text extraction strips tags; leftover `\(...\)` is not typeset.

**Fix:**
1. Prefer math-free headings (Unicode)
2. Or explicitly run KaTeX/`MathJax.typeset` on sidebar after build/navigation

### Pitfall C — Table columns misaligned around Dirac notation

**Symptom:** symbol tables shatter; one logical row becomes many columns.

**Cause:** bare `|` inside cell math is a pipe delimiter.

**Fix:** rewrite cell math with `\lvert` / `\rvert` / `\vert` / `\lVert` / `\rVert` before convert.
Scan rule: table row contains `$...$` and that math segment contains bare `|`.

### Pitfall D — "Fixing" math by blank lines inside `$$`

**Symptom:** after batch edit, formulas become:

```html
<p>$$</p><p>formula</p><p>$$</p>
```

**Cause:** blank lines added **inside** the fence, so markdown sees three paragraphs, not one math block.

**Fix:** only ensure blank lines **outside** fences; keep body compact:

```md
$$
formula
$$
```

### Pitfall E — Missing assets / pseudo-links look like content bugs

**Symptom:** build warnings; page holes; weird autolinks.

**Cause:**
1. referenced assets never existed (e.g. `figures/routing-example.png`)
2. Huffman-style labels written as markdown links: `[不及格+优](0.15)` → broken link targets `0.15`

**Fix:**
1. Replace fake image with short text placeholder or real asset
2. Avoid link shape for non-links: use `` `{不及格+优}`(0.15) `` or plain parentheses

### Pitfall F — Site builders vs single-file skill

This skill targets **single-file HTML**. If source is also used by MkDocs/Material:

| Topic | Single-file KaTeX HTML | MkDocs + arithmatex/MathJax |
|---|---|---|
| Display `$$` blank lines | still required for clean md | required for generic arithmatex |
| Heading math | TOC often plain text | Material TOC also strips tags |
| Table `|` | same markdown pipe rules | same |
| Instant navigation | N/A | must re-typeset after page change |
| `docs_dir: .` | N/A | MkDocs may forbid docs_dir = config parent |

When maintaining dual delivery, fix problems **in markdown source**, not only in one exporter.

## Preflight checklist (run before generate)

1. **Display math:** no `$$` glued to previous non-empty line; no empty-only interior between fences without formula lines
2. **Headings:** no `$...$` in `#`/`##`/`###` if sidebar is text-only
3. **Tables:** no bare `|` inside cell math; use `\vert` family
4. **Pseudo-links:** no `[label](0.15)` unless real URL/path
5. **Assets:** every `![](path)` exists or is removed
6. **Smoke test after write:**
   - one inline formula
   - one display formula
   - one heading that used to contain symbols
   - one Dirac table row

## Bug prevention

- Always blank line **before/after** `$$` blocks; never turn one fence into three paragraphs with interior blanks alone
- Escape backslashes carefully in Python strings when writing HTML / batch-fix scripts
- Verify with `read` after `write` or `edit`
- Add `<meta http-equiv="Cache-Control" content="no-cache">` to prevent stale renders during iteration
- **表格内 LaTeX 不能出现裸 `|`**：用 `\vert`（单竖线）、`\lvert`/`\rvert`（左/右定界）、`\lVert`/`\rVert`（双竖线/范数）代替 `|` 和 `\|`
- Pipe 表解析采用两阶段检测：`| 表头 |` + 下一行 `|---|` 才进入表模式，跳过分隔行，遇到非 `|` 行才关闭
- Prefer fixing markdown source so GitHub / MkDocs / this skill all render consistently
- After batch regex fixes, rebuild/open HTML and inspect snippets; do not trust "files changed" alone
