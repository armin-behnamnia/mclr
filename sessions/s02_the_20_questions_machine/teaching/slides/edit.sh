#!/usr/bin/env bash
# THE ONE-COMMAND SLIDE EDITOR — edit slides, see them update live.
#
#   ./edit.sh            Persian deck (slides.md)
#   ./edit.sh en         English deck (slides_en.md)
#
# HOW IT WORKS:
#   1. This starts a live server and opens the deck in your browser.
#   2. Edit slides.md (Persian) in ANY editor — VS Code, vim, Notepad.
#   3. Every time you SAVE, the browser updates in about 1 second.
#   4. Press P in the browser to see presenter notes.
#   5. When done: Ctrl+C here, then run ./render.sh to produce the final
#      PDFs and PPTX from your edits.
#
# WHAT TO EDIT (mini cheat-sheet):
#   # Title            -> slide title
#   **bold**  *italic* -> emphasis
#   - item             -> bullet
#   ![art](img.png)    -> image
#   <!-- ... -->       -> presenter note (English)
#   ---                -> new slide
#   <!-- _class: wow -->-> slide mood (lead/hook/wow/definition/quiz/handout/codespot/focus)
set -e
SLIDES_DIR="$(cd "$(dirname "$0")" && pwd)"
COURSE_ROOT="$(cd "$SLIDES_DIR/../../../.." && pwd)"
THEME="$COURSE_ROOT/slide-theme/mlcourse-blue-fa.css"
if [ "${1:-}" = "en" ]; then DECK="slides_en.md"; else DECK="slides.md"; fi

# font + shared art next to the deck (theme needs them)
[ -f "$SLIDES_DIR/Vazirmatn.ttf" ] || cp "$COURSE_ROOT/slide-theme/Vazirmatn.ttf" "$SLIDES_DIR/"
for art in shared_hero.png shared_closing.png shared_band.png; do
  [ -f "$SLIDES_DIR/$art" ] || cp "$COURSE_ROOT/slide-theme/shared/$art" "$SLIDES_DIR/"
done

# make sure the deck frontmatter names the theme (font loading depends on it)
grep -q "^theme: mlcourse-blue-fa" "$SLIDES_DIR/$DECK" || \
  sed -i "s/^theme: .*/theme: mlcourse-blue-fa/" "$SLIDES_DIR/$DECK"

CHROME="$HOME/.cache/puppeteer/chrome-headless-shell/linux-131.0.6778.204/chrome-headless-shell-linux64/chrome-headless-shell"
[ -x "$CHROME" ] && export CHROME_PATH="$CHROME"
[ -d /tmp/opencode/chrome-libs/usr/lib/x86_64-linux-gnu ] && \
  export LD_LIBRARY_PATH="/tmp/opencode/chrome-libs/usr/lib/x86_64-linux-gnu${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

cd "$SLIDES_DIR"
URL="http://localhost:8080/teaching/slides/$DECK"
echo ""
echo "============================================================"
echo "  SLIDE EDITOR — live preview"
echo "============================================================"
echo "  1. Open in your browser:  $URL"
echo "     (presenter notes: press P inside the browser)"
echo "  2. Edit this file in any editor:"
echo "     $SLIDES_DIR/$DECK"
echo "  3. SAVE the file -> browser updates in ~1 second"
echo "  4. Done? Ctrl+C here, then run:  ./render.sh"
echo "============================================================"
echo ""
exec marp -s -w -I ../.. --theme-set "$THEME" --allow-local-files
