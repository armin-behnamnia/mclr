---
marp: true
theme: mlcourse-blue-fa
paginate: true
class: ltr
---

<!-- _class: lead -->

# Teach Guide — Session 3

## How the Tree Picks Its Questions

*8 short slides. Full script: teaching-notes.md.*

---

# Prep checklist (night before)

- PHYSICAL props: three grab-bags — 8 same-color; 4+4; 3+3+2 (or magnets + two drawn boxes)
- PART 0 demo cell runs fresh (the machine's gain leaderboard)
- Judge green: `python judge/run.py notebook/s03_notebook_solution.ipynb` → 3/3
- Board space for the score-card table: question | sides | surprise after | score

---

# Run of show (60 min)

| Time | Segment | Where |
|---|---|---|
| 0–5 | Hook: two boxes, one question | board/props |
| 5–15 | Purity: sorted boxes | slides 5–8 |
| 15–25 | Grab-bags → surprise number | props + A2 |
| 25–35 | THE GAME: teams score questions | board + hands |
| 35–45 | Titanic gains | A4–A5 |
| 45–50 | You be the machine (`best_question`) | A6 |
| 50–55 | Consolidation quiz | slides |
| 55–60 | Ship + handout (one slide) | B1–B3 |

---

# The one rule of this session

**Experience before the name.** The team game comes FIRST, the words "information gain" AFTER.

- Slide 12 is the game; slide 13 names it. Never swap them.
- Wait for a team to notice the TIE themselves: `weight ≥ 14` and `ear ≥ 8.25` both score 0.95.
- The tie break is boring and mechanical (column order) — say so. Honesty beats drama.

---

# Key lines to say verbatim

- "A good question doesn't just cut the box — it SORTS."
- On the bad question: "One door IS pure — but it holds one animal out of eleven. The score cares about the whole box."
- On Titanic: "Session 1 you VOTED that gender matters. Today the machine put a number on your vote."
- The dark slide: "«Does it hop?» can never be asked — it isn't a column. Features are OUR job."

---

# Misconceptions to catch

| They think | You show |
|---|---|
| Splitting evenly is the goal | The 1-vs-10 split: a perfect side that earns almost nothing (0.14) |
| Entropy is the machine thinking | It's counting colors. The least magical number in the course |
| The champion is the purest side | The champion is the biggest surprise-DROP for the whole box |
| Gain shows causes | Gain measures sorting — one sentence; Session 9 opens fairness |

---

# Live-demo protocol

- PART 0 (leaderboard print), A2/A2b (bag numbers + 11-animal box: 1.57), A3 (the machine's leaderboard), A3b (light-box champion), A4–A5 (Titanic 0.97 → `is_female` 0.21), A6 (the loop).
- If a cell breaks: the same numbers are committed in the solution notebook's outputs and in the slide pictures (split_bad, split_champion_tree, leaderboard_animals, titanic_champion).
- Never debug live longer than 60 seconds.

---

# Judge + homework + cliffhanger

- At-home: B1 (three bags' surprises: 0, 1, 0.47 — **don't round**), B2 (light-box champion), B3 (Titanic leaderboard + hand-annotated plot). ~20–30 min.
- Judge command is ON the closing slide: `python judge/run.py s03_notebook.ipynb`
- **Ship:** the annotated Titanic map, `s03_titanic_map.png` — "my Session 1 vote got its number today."
- Cliffhanger: "What if a question is only 'good' on passengers it has SEEN? Next: the exam cheat test."

**Within 48h:** retro block in the session README.
