# Session 1 — Generated Image Manifest

Regenerate any image with `slide-theme/gen_image.sh <output> <size> <seed> <<'EOF' ...prompt... EOF`

All prompts use the course art-style keywords (§9.3 of the session creation guide).
Shared template art (hero/closing/band) is documented at `slide-theme/shared/README.md`.

| File | Size | Seed | Prompt |
|------|------|------|--------|
| animal_game.png | 512x384 | 209 | A cute cartoon machine drawing a red dashed line on a chart between a group of small blue cats and large orange dogs, a wolf and a tiny puppy standing near the line looking puzzled, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |
| fortune_teller.png | 512x512 | 202 | A magical fortune teller crystal ball machine with gears, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |
| cat_rules.png | 512x512 | 204 | A confused cartoon scientist writing rules on a giant scroll while a playful cat sits nearby, floating question marks, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |
| mind_reader.png | 512x384 | 205 | A cartoon magic mirror robot guessing thoughts, glowing lightbulbs and numbers floating around, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |
| fruit_table.png | 512x384 | 206 | A cheerful cartoon table with colorful fruits apple banana and grapes, magnifying glass examining them, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |
| titanic_ship.png | 512x384 | 207 | A cute cartoon style historic ocean ship on calm sea, gentle waves, lifeboats visible, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |
| magic_lines.png | 512x384 | 208 | Three glowing magical lines of light transforming into a small friendly robot, sparkles, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |

## Notebook-plot screenshots (used on slides, reproducible from the notebook)

These are NOT gen_image.sh art; they are exports of committed notebook outputs. To refresh: open `notebook/s01_notebook_solution.ipynb`, `Runtime → Run all`, then re-save the plot from the named cell.

| File | Source cell | What it shows |
|------|-------------|---------------|
| decision_tree.png | A9 (solution) | the fitted Titanic tree, Persian class names via `fa()` |
| survival_counts.png | A5 (solution) | survived vs did-not bar chart (424 vs 288) |
| survival_by_sex_class.png | A6 (solution) | survival rate by sex and by pclass (~75% vs ~20%) |

## Dataset
| File | Source |
|------|--------|
| titanic.csv | snapshot of github.com/datasciencedojo/datasets titanic.csv (891 rows); the notebook reads this first, falls back to the URL |

## Code-generated diagrams
| File | Generator |
|------|-----------|
| supervised_study_exam.png | `assets/gen_supervised_diagram.py` (matplotlib + fa() shaping, Vazirmatn registered from slide-theme; run from anywhere) |

Superseded (dark theme v2, kept for history): hero_robot_ai.png (seed 101).
Superseded (single-demo hook v4): mind_reader.png (seed 205) and fortune_teller.png (seed 202) — the three-demo hook was replaced by the single Animal Game demo.

Restyled to the blue editorial theme (v3, was cream/yellow): all images regenerated with new seeds and blue style keywords; old cream-family seeds superseded.
Slide diagram (presentation twin of the Segment B fruit game):
- fruit_tree.png — fruit decision map (red? apple / not red, long? banana / else grape),
  matplotlib + fa() shaping, Vazirmatn, text-measured boxes, border-anchored arrows.
  Regenerate: `python3 assets/gen_fruit_tree.py` (committed generator, run from anywhere).
