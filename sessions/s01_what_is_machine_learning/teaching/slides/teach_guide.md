---
marp: true
theme: mlcourse-blue-fa
paginate: true
class: ltr
---

<!-- _class: lead -->

# Teach Guide — Session 1

## What Is Machine Learning?

*8 short slides. Read in 10 minutes before class. Full script: teaching-notes.md.*

<!--
This deck is the instructor's cockpit README. It compresses the full per-slide
script into run-order, key lines, misconceptions, and fallbacks.
-->

---

# Prep checklist (night before)

- PART 0 demo cell runs fresh (Kernel → Restart & run up to it)
- Judge green on the solution notebook: `python judge/run.py notebook/s01_notebook_solution.ipynb` → 4/4
- `assets/titanic.csv` is in place (offline fallback)
- Print the fruit-table handout for the fruit game
- Lights dimmable for the hook if you can

---

# Run of show (60 min)

| Time | Segment | Where |
|---|---|---|
| 0–5 | Hook: the animal game, 4 beats | PART 0 demo cell |
| 5–10 | Rules vs learning (the two ways) | slides, fruit story |
| 10–20 | Features & labels (fruit game) | A1–A2 code-along |
| 20–30 | Supervised learning, study/exam | slides + A3 |
| 30–40 | Titanic as pictures | A4–A6 |
| 40–50 | THE MOMENT: `fit()` in 3 lines | A7–A9 |
| 50–55 | Oral quiz | slides |
| 55–60 | Handout + Ship + judge command | B1–B4 announced |

---

# The hook — protect the 4 beats

The demo cell prints «——— مرحلهٔ N ———» before each beat. Wait for the marker, then say the line.

1. **The table** — "This is ALL the machine gets." Let them shrug.
2. **The silent fit** — one line, nothing prints. "That was the whole spell."
3. **The line** — "No human drew this." Do NOT explain how until slide 9.
4. **The quiz + reveal** — puppy wrong, elephant silly, then: the whole secret = ONE question.

HONESTY BEAT (fruit map, later): 2 of 6 rows defeat hand rules — data, not cleverness, is the point.

<!--
Fallback if the demo breaks: narrate from the slide pictures; the reveal line
is printed in the notes. Never debug live longer than 60 seconds — show the
committed solution notebook's outputs instead.
-->

---

# The moment to protect (40–50)

Cell A7–A9: `DecisionTreeClassifier` + `fit` + `predict` on 712 Titanic rows.

- Ceremony: count down, class says "LEARN", run. Under a second for 712 lives.
- Name it: "This object is a **مدل (Model)** — the student that studied."
- Let them see the tree plot (A9) — THEIR machine, not yours.

Watch for: students copying without running. Everyone runs the three lines.

---

# Misconceptions to catch

| They say | You say |
|---|---|
| "The machine understands cats" | It reads numbers in a table — nothing more |
| "The red line is magic" | One question it picked from the columns — Session 3 shows HOW |
| "More examples always fix it" | Near the line, guesses still break (the puppy) |
| "fit() is slow magic" | It just ran — in under a second |

---

# Judge + homework handoff

- At-home: B1–B4 in the same notebook; ~20–30 min; due before the problem-solving session.
- The judge command is ON the at-home slide: `python judge/run.py s01_notebook.ipynb`
- First run is all red — **say this out loud**, or half the class panics.
- Judge reads undefined starters ("did you fill in cell B2?") and broken files kindly.

---

# Ship + cliffhanger + retro

**Ship tonight:** notebook committed to their repo — `git add . && git commit -m "S1: my first model" && git push`. Then the family demo: "I trained an AI today."

**Cliffhanger (verbatim):** the machine asked ONE question — *why THAT one?* Next session: the 20-questions machine.

**Within 48h:** fill the retro block in the session README (confused / dragged / delighted).
