---
marp: true
theme: mlcourse-blue-fa
paginate: true
class: ltr
---

<!-- _class: lead -->

# Teach Guide — Session 2

## The 20-Questions Machine

*8 short slides. Full script: teaching-notes.md.*

---

# Prep checklist (night before)

- PART 0 demo cell runs fresh (depth-1 vs depth-2, the puppy verdict)
- Judge green: `python judge/run.py notebook/s02_notebook_solution.ipynb` → 3/3
- Print `assets/animals_table.pdf` — one per student (the lab needs it)
- Blank paper + pencils on desks
- Decide your wolf-answer path in advance (the hook game)

---

# Run of show (60 min)

| Time | Segment | Where |
|---|---|---|
| 0–5 | Hook: class plays 20 questions (you are the tree) | board |
| 5–15 | Anatomy: node, branch, leaf | board + slides 5–7 |
| 15–25 | Reading the machine's tree | A2–A3 |
| 25–35 | The depth knob | A4–A5 |
| 35–50 | THE LAB: draw your own tree on paper | paper + tables |
| 50–55 | Tree battle (surprise animals) | pairs |
| 55–60 | Handout + Ship (tree photo) | B1–B3 |

---

# The hook — you ARE the tree

- Think of a WOLF. Yes/no only. Count questions on the board, aloud.
- When they guess: "Every answer was a **door**. You walked a **decision tree**."
- Do NOT clear the board — that path becomes the anatomy diagram.
- Then the machine plays: PART 0 demo, once. "One question failed the puppy. Watch two."

Failure mode to avoid: letting the game run past 5 minutes. Cut a stalling question: "I can only say yes or no — pick sharper ones!"

---

# Key lines to say verbatim

- "A leaf says ONE word for whatever reaches it — even a 3-ton elephant, after a single question." (elephant quiz, AFTER the depth-2 picture)
- "The ear question lives only on the light side — the tree asks where animals are still mixed."
- "Depth is a knob WE turn — more questions is not automatically smarter."
- The dark slide: "Your paper tree and the machine's tree are the SAME THING."

---

# Misconceptions to catch

| They think | You show |
|---|---|
| A tree can change its questions mid-game | Path is fixed; every animal walks the same corridors |
| Every branch gets the same questions | The elephant answers ONE question — the heavy side was already pure |
| Deeper is always better | Turn the knob to 10: a jungle. Session 4 explains when it hurts |

---

# The lab (35–50) — the Ship source

- Students hand-draw a tree on paper for the 11 animals (table in front of them).
- Target: 2–3 questions, ends in pure rooms.
- Battle: pairs swap surprise animals (the notebook's C2 five: rabbit, fox, hamster, sparrow, lion).
- Collect the funniest failure — the rabbit lands with the small dogs; that rabbit RETURNS next session (a feature is missing).

**Ship:** photo of the paper tree → `s02_tree.jpg`, battle-tested.

---

# Judge + homework + cliffhanger

- At-home: B1 (count questions/leaves), B2 (elephant's room), B3 (smallest perfect depth). ~20–30 min.
- Judge command is ON the handout slide: `python judge/run.py s02_notebook.ipynb`
- Judge is specific: B2's failure teaches the one-question elephant path.
- Cliffhanger: "WHY did the machine ask `weight ≥ 14` first — and not ears? Next session: the machine's shopping game."

**Within 48h:** retro block in the session README.
