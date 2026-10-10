#!/usr/bin/env bash
# Render the slide decks from slides.md (Persian, primary) and slides_en.md
# (English, simple version). Outputs:
#   slides.pdf / slides_en.pdf            — student decks (clean)
#   slides_with_notes.pdf                 — instructor deck (notes as PDF annotations)
#   slides.pptx                           — EDITABLE PowerPoint (real Persian text,
#                                           RTL, Vazirmatn font, notes attached) —
#                                           built by build_pptx.py, for simplifying
#                                           unfamiliar keywords in PowerPoint.
# Uses the puppeteer headless Chrome plus locally-extracted shared libraries
# (no root needed).
# Requires: marp CLI (npm i -g @marp-team/marp-cli), python-pptx for the pptx.

# Theme + Persian font are resolved from the course-level slide-theme/ dir.
# Requires: Vazirmatn.ttf and mlcourse-blue-fa.css in slide-theme/ (course root).
set -e
SLIDES_DIR="$(cd "$(dirname "$0")" && pwd)"
COURSE_ROOT="$(cd "$SLIDES_DIR/../../../.." && pwd)"
THEME="$COURSE_ROOT/slide-theme/mlcourse-blue-fa.css"
CHROME="$HOME/.cache/puppeteer/chrome-headless-shell/linux-131.0.6778.204/chrome-headless-shell-linux64/chrome-headless-shell"
LIBS="/tmp/opencode/chrome-libs/usr/lib/x86_64-linux-gnu"

if [ ! -x "$CHROME" ]; then
  echo "ERROR: headless Chrome not found at $CHROME" >&2
  echo "Install one via: npx puppeteer browsers install chrome-headless-shell" >&2
  exit 1
fi
if [ ! -d "$LIBS" ]; then
  echo "ERROR: extracted chrome libraries not found at $LIBS" >&2
  echo "Recreate them with: apt-get download libatk1.0-0 libatk-bridge2.0-0 libatspi2.0-0 libasound2 libgbm1 libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libxi6 libxext6 libx11-6 libxcb1 libxrender1 libdrm2 libwayland-server0 libxcb-randr0 && dpkg-deb -x each.deb chrome-libs/" >&2
  exit 1
fi

if [ ! -f "$THEME" ]; then
  echo "ERROR: course theme not found at $THEME" >&2
  exit 1
fi

# Persian font: the theme font URL resolves relative to the markdown file,
# so the font must sit next to the decks. Copy it from the course root if missing.
if [ ! -f "$SLIDES_DIR/Vazirmatn.ttf" ]; then
  cp "$COURSE_ROOT/slide-theme/Vazirmatn.ttf" "$SLIDES_DIR/Vazirmatn.ttf"
fi

# Shared template art (hero / closing / band) used by every session's decks.
for art in shared_hero.png shared_closing.png shared_band.png; do
  if [ ! -f "$SLIDES_DIR/$art" ]; then
    cp "$COURSE_ROOT/slide-theme/shared/$art" "$SLIDES_DIR/$art"
  fi
done

export LD_LIBRARY_PATH="$LIBS"
export CHROME_PATH="$CHROME"
cd "$SLIDES_DIR"

# Persian deck (primary)
marp slides.md --pdf --allow-local-files --theme-set "$THEME" -o slides.pdf
marp slides.md --pdf --pdf-notes --allow-local-files --theme-set "$THEME" -o slides_with_notes.pdf

# English deck (simple version) — Latin text falls back cleanly in the same theme
marp slides_en.md --pdf --allow-local-files --theme-set "$THEME" -o slides_en.pdf

# Editable PPTX (Persian, real text, RTL, Vazirmatn, presenter notes)
python3 build_pptx.py
