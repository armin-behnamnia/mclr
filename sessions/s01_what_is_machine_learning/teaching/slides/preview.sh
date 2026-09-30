#!/usr/bin/env bash
# LIVE PREVIEW — edit slides.md in any editor and see the deck update instantly.
#
# This is the course-level TEMPLATE. Every session's teaching/slides/ folder
# gets an identical copy (the guide requires it). Do not fork per session;
# improvements go here and are re-copied.
#
# Usage:  ./preview.sh                 (Persian deck, slides.md)
#         ./preview.sh slides_en.md    (English deck)
#
# What it does:
#   - starts a local Marp server with the course theme, RTL and Vazirmatn
#   - serves http://localhost:8080 — open your browser at
#     http://localhost:8080/teaching/slides/slides.md
#   - the SERVER ROOT is the session root, so image paths like
#     ../../assets/name.png resolve exactly like in the final PDF
#   - every save of the deck re-renders in ~1 second (live reload)
#   - presenter notes: press P in the browser (presenter view with notes
#     and next-slide preview — same notes as slides_with_notes.pdf)
#
# When you're happy: press Ctrl+C, then run ./render.sh to produce the final
# PDFs and PPTX.
set -e
SLIDES_DIR="$(cd "$(dirname "$0")" && pwd)"
COURSE_ROOT="$(cd "$SLIDES_DIR/../../../.." && pwd)"
THEME="$COURSE_ROOT/slide-theme/mlcourse-blue-fa.css"
DECK="${1:-slides.md}"

# font must sit next to the deck for the theme to load it
if [ ! -f "$SLIDES_DIR/Vazirmatn.ttf" ]; then
  cp "$COURSE_ROOT/slide-theme/Vazirmatn.ttf" "$SLIDES_DIR/Vazirmatn.ttf"
fi
# shared art must sit next to the deck
for art in shared_hero.png shared_closing.png shared_band.png; do
  if [ ! -f "$SLIDES_DIR/$art" ]; then
    cp "$COURSE_ROOT/slide-theme/shared/$art" "$SLIDES_DIR/$art"
  fi
done

cd "$SLIDES_DIR"
DECK_URL="http://localhost:8080/teaching/slides/$DECK"
echo "Live preview starting -> open $DECK_URL in your browser"
echo "Edit $DECK and save; the browser updates within a second."
echo "Press P in the browser for presenter view (notes + next slide)."
echo "Ctrl+C to stop. Then run ./render.sh for final outputs."
exec marp -s -w -I ../.. --theme-set "$THEME" --allow-local-files
