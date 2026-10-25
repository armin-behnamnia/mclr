# Session 1 — What is Machine Learning? Day One, You Build an AI 

**Block:** 1 (ML through Random Forest)
**Syllabus goal:** *Rules vs learning from examples; features & labels; supervised learning (just this one idea today). Titanic dataset shown as pictures, not tables. Live demo: train a tree in 3 lines of sklearn.*
**Student goal:** "By the end of today, YOU will be able to train a working ML model and show it to your family."
**Ship:** A GitHub repo with your first ML notebook + a model that answers "would I have survived the Titanic?"
**Hook:** The Animal Game — one demo cell, three beats: the machine sees 8 labeled animals, draws its own separating line, then answers animals it has never seen (and gets the puppy wrong — generalization is a guess). "By the end of today, you build this yourself."

---

## Teaching session (60 min)

| Time | Segment | Mode | Notebook cells |
|------|---------|------|----------------|
| 0–5 | Hook: The Animal Game (1 demo, 4 beats) | live demo | PART 0 |
| 5–10 | The Big Question: rules vs learning | lecture + discussion | — |
| 10–20 | Features & labels (fruit game) | interactive game | A1–A2 |
| 20–30 | Supervised learning: showing examples | lecture + visuals | A3 |
| 30–40 | Titanic as pictures, not tables | live coding + plots | A4–A6 |
| 40–50 | THE MOMENT: train an AI in 3 lines | live coding, students code along | A7–A9 |
| 50–55 | Consolidation: check questions | oral quiz | — |
| 55–60 | At-home handout + GitHub repo + goal recap | walkthrough | B1–B4 |

## Problem-solving session (60 min)

| Time | Segment | Notebook cells |
|------|---------|----------------|
| 0–30 | Solve at-home problems live (PRIORITY) | B1–B4 |
| 30–55 | In-class: the Imagination Engine (invent passengers) + beat-the-human | C1–C3 |
| 55–60 | Ship: push to GitHub, wrap-up | — |

### Teacher-led deep dive (enrichment, `notebook/s01_deep_dive.ipynb`)

A separate, **teacher-run** notebook for when the at-home problems are already solved or for a
spark-hungry group. The teacher executes each cell live and the student **predicts before every
reveal** — ten stops, under half an hour, no student editing. It goes deep on what Session 1's
three lines actually learned (opens the animal machine and the Titanic tree, shows the confident
guesses, the mirror-of-data effect) and then reels forward: the same three lines on study habits,
on seeing digits, on reading spam — plus the entropy/gain bridge that Session 3 will formalize and
a roadmap figure to the whole course. Generator: `notebook/build_deep_dive.py` (source of truth).

## Prerequisites recap
- Python: variables, lists, dictionaries, functions (`pandas` basics: reading a CSV, `head()`)

## Judge
Run `python judge/run.py <student_notebook.ipynb>` — see `judge/README.md` for rubric.

## Post-session retro (fill within 48h of teaching)
- What confused students:
- What dragged:
- What delighted:
