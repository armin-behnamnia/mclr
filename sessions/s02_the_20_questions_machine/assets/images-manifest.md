# Session 2 — Generated Image Manifest

Regenerate any image with `slide-theme/gen_image.sh <output> <size> <seed> <<'EOF' ...prompt... EOF`

All prompts use the course art-style keywords (§9.3 of the session creation guide).
Shared template art (hero/closing/band) is documented at `slide-theme/shared/README.md`.

| File | Size | Seed | Prompt |
|------|------|------|--------|
| twenty_questions.png | 512x384 | 210 | Cartoon kids playing a guessing game, one child thinking of a wolf while thought bubble shows a wolf silhouette, other kids asking questions with floating question marks, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |
| tree_anatomy.png | 512x384 | 211 | A friendly cartoon decision tree diagram with circular question nodes, two branching doors on each node, and room-like box leaves at the bottom, small cat and dog figures walking down the paths, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |
| paper_tree.png | 512x384 | 212 | A proud kid holding up a hand-drawn decision tree on paper next to a laptop showing the same tree shape on screen, pencil and eraser nearby, flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text |

Real data visualizations (NOT generated art — rendered from the actual sklearn trees, mirroring notebook cells A1/A2):
- decision_tree_s02_d1.png — depth-1 tree, mirrors notebook cell A1 (matplotlib, dpi=150)
- decision_tree_s02_d2.png — depth-2 tree, mirrors notebook cell A2 (matplotlib, dpi=150)
