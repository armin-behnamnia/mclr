# Session 3 — How the Tree Picks Its Questions

**Block:** 1 (ML through Random Forest)
**Syllabus goal:** *Purity as "sorted-ness"; entropy as surprise (with a slot-machine visual); information gain. 5-minute split-ranking game (which question wins?), then verify instantly in code on a bigger dataset.*
**Student goal:** "By the end of today, YOU will be able to explain why one question is better than another."
**Ship:** An annotated best-split plot — the Titanic root question as before/after boxes with survival counts and surprise numbers, computed by you (notebook cell B3) — committed to your repo.
**Hook:** Two boxes of balls — which single question un-mixes them fastest? The class ranks candidate questions by gut; the machine then shows its own ranking — with a number on it — and the S2 mystery ("who chose `weight ≥ 14`?") is solved.

---

## Teaching session (60 min)

| Time | Segment | Mode | Notebook cells |
|------|---------|------|----------------|
| 0–5 | Hook: Two Boxes, One Question — the class ranks questions | live game + demo | PART 0 cell 1 |
| 5–15 | Sorted-ness: some questions sort better | board + slides + vote | A1 |
| 15–25 | Surprise: measuring mixed-ness (grab-bag game) | live game + live coding | A2 |
| 25–35 | The split-ranking game + information gain | team game + live coding | A3 |
| 35–45 | THE MOMENT: the machine plays it on Titanic | live coding, students code along | A4–A5 |
| 45–50 | You be the machine: rebuild the S2 tree | board interaction + code | A6 |
| 50–55 | Consolidation: check questions | oral quiz | — |
| 55–60 | At-home handout + goal recap | walkthrough | B1–B3 |

## Problem-solving session (60 min)

| Time | Segment | Notebook cells |
|------|---------|----------------|
| 0–30 | Solve at-home problems live (PRIORITY) | B1–B3 |
| 30–55 | In-class: the fixed-threshold game + the one-animal champion + Titanic round two | C1–C3 |
| 55–60 | Ship: commit the annotated split plot, wrap-up | — |

## Prerequisites recap
- Session 1: features/labels; the feature vote on Titanic (revisited today with numbers)
- Session 2: tree anatomy (node/branch/leaf/root/depth); the machine's `weight ≥ 14` choice (today's mystery to solve); S2's C3 "corridor of valid thresholds"

## Judge
Run `python judge/run.py <student_notebook.ipynb>` — see judge/README.md for rubric.

## Instructor runbook (open in this order)
1. `teaching/slides/slides.pdf` (or `slides_with_notes.pdf` for the annotated deck)
2. The notebook, scrolled to PART 0 — the hook's machine beat is the demo cell printing the gain leaderboard
3. Props ready BEFORE class: three paper bags with colored balls (8 blue; 4 blue + 4 red; 3 blue + 3 red + 2 green) — or colored magnets and two drawn boxes
4. Full per-slide script: `teaching/teaching-notes.md` (rendered: `teaching/slides/slides_teaching_notes.pdf`)

## Post-session retro (fill within 48h of teaching)
- What confused students:
- What dragged:
- What delighted:
