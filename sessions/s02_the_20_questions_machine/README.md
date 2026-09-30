# Session 2 — The 20-Questions Machine

**Block:** 1 (ML through Random Forest)
**Syllabus goal:** *Nodes, branches, leaves; splits partition data; visualize trees with `plot_tree`. Build a tree on paper to classify animals, then test classmates' trees on surprise examples — celebrate the funniest failures.*
**Student goal:** "By the end of today, YOU will be able to read, draw, and hand-build a decision tree."
**Ship:** A photo of your hand-drawn animal tree, committed to your repo (`s02_tree.jpg`) — battle-tested on surprise animals.
**Hook:** The class plays 20-questions to guess a wolf — then the teacher reveals the class was playing a decision tree all along, and the notebook machine plays the same game, fixing last session's puppy mistake with a second question.

---

## Teaching session (60 min)

| Time | Segment | Mode | Notebook cells |
|------|---------|------|----------------|
| 0–5 | Hook: 20 Questions — you ARE the tree | live game + demo | PART 0 cell 1 |
| 5–15 | Anatomy: node, branch, leaf | board + slides | A1 |
| 15–25 | Reading the machine's tree | live coding | A2–A3 |
| 25–35 | The depth knob: max_depth | live coding, students code along | A4–A5 |
| 35–50 | THE LAB: draw your own tree + battle | paper lab (the Ship) | A6 |
| 50–55 | Consolidation: check questions | oral quiz | — |
| 55–60 | At-home handout + goal recap | walkthrough | B1–B3 |

## Problem-solving session (60 min)

| Time | Segment | Notebook cells |
|------|---------|----------------|
| 0–30 | Solve at-home problems live (PRIORITY) | B1–B3 |
| 30–55 | In-class: the surprise-zoo gauntlet + tree surgery | C1–C3 |
| 55–60 | Ship: photo-commit paper trees, wrap-up | — |

## Prerequisites recap
- Session 1: features/labels, the 3 magic lines (`fit`/`predict`), the animal game and its puppy failure

## Judge
Run `python judge/run.py <student_notebook.ipynb>` — see `judge/README.md` for rubric.

## Instructor runbook (open in this order)
1. `teaching/slides/slides.pdf` (or `slides_with_notes.pdf` for the annotated deck)
2. The notebook, scrolled to PART 0 — the hook's machine beat is cell 1
3. Paper handouts ready BEFORE class: the 11-animal table, one per student (print from `assets/animals_table.pdf` or copy from the notebook)
4. Full per-slide script: `teaching/teaching-notes.md` (rendered: `teaching/slides/slides_teaching_notes.pdf`)
