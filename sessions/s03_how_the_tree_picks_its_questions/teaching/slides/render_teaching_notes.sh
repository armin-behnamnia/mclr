#!/usr/bin/env bash
# render_teaching_notes.sh — render teaching/teaching-notes.md (the comprehensive
# per-slide instructor guide) as slides_teaching_notes.pdf: A4 portrait document,
# one page per slide-heading, note text as visible content (not annotations).
# RTL, Vazirmatn, Editorial Blue palette.
set -e
SLIDES_DIR="$(cd "$(dirname "$0")" && pwd)"
COURSE_ROOT="$(cd "$SLIDES_DIR/../../../.." && pwd)"
THEME="$COURSE_ROOT/slide-theme/teaching-notes.css"
NOTES="$SLIDES_DIR/../teaching-notes.md"
OUT="$SLIDES_DIR/slides_teaching_notes.pdf"

CHROME="$HOME/.cache/puppeteer/chrome-headless-shell/linux-131.0.6778.204/chrome-headless-shell-linux64/chrome-headless-shell"
LIBS="/tmp/opencode/chrome-libs/usr/lib/x86_64-linux-gnu"
[ -x "$CHROME" ] && export CHROME_PATH="$CHROME"
[ -d "$LIBS" ] && export LD_LIBRARY_PATH="$LIBS"

if [ ! -f "$SLIDES_DIR/Vazirmatn.ttf" ]; then
  cp "$COURSE_ROOT/slide-theme/Vazirmatn.ttf" "$SLIDES_DIR/Vazirmatn.ttf"
fi

cd "$SLIDES_DIR"
# the generated deck lives in /tmp — the font must sit NEXT TO IT for the
# theme's @font-face url to resolve (relative to the markdown, not the theme)
cp "$COURSE_ROOT/slide-theme/Vazirmatn.ttf" /tmp/Vazirmatn.ttf
python3 - "$NOTES" > /tmp/teaching_notes_deck.md <<'PY'
import sys, re
src = open(sys.argv[1], encoding="utf-8").read()
# strip horizontal rules (---) — marp would treat them as page breaks
src = re.sub(r"^---\s*$", "", src, flags=re.M)
# Build a marp deck: frontmatter + one page per "## ..." heading.
# The cover title comes from the SOURCE document's own H1 (line starting
# with "# ") — never hard-coded, so every session renders its own title.
parts = re.split(r"\n(?=## )", src)
m = re.search(r"^#\s+(.+)$", parts[0], flags=re.M)
title = m.group(1).strip() if m else "Teaching Notes"
out = ["---", "marp: true", "theme: teaching-notes", "paginate: true",
       "---", "", "<!-- _class: lead -->", "", "# Full Teaching Notes", "",
       f"## {title}", "",
       "*The comprehensive per-slide instructor guide — English, LTR*", "", "---", ""]
for p in parts[1:]:
    p = p.strip()
    if not p:
        continue
    p = re.sub(r"\n### ", "\n#### ", p)  # demote inner headings
    out.append(p)
    out.append("\n---\n")  # page break AFTER each slide section
deck = "\n".join(out).rstrip()
if deck.endswith("---"):
    deck = deck[:-3].rstrip()  # no trailing separator = no empty last page
print(deck)
PY

marp /tmp/teaching_notes_deck.md --pdf --allow-local-files --theme-set "$THEME" -o "$OUT"
echo "wrote $OUT"
