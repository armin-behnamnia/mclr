# Session 3 — At-Home Problems

**Deadline:** before the next problem-solving session. **Time budget:** ~20–30 minutes.
**What to submit:** your `s03_notebook.ipynb` with cells B1–B3 filled — B3's hand-annotated split plot is your Ship (commit it as `s03_titanic_map.png` next to the notebook).
**Judge:** `python judge/run.py s03_notebook.ipynb` — friendly feedback, partial credit, no tricks.

---

## Problem B1 — The Surprise of Three Bags (1 pt)

**Story:** in class you rated surprise with your fingers; now you compute it. Three bags: all-red (10), 5 red + 5 blue, 1 red + 9 blue.
**Task:** in cell `B1`, use the `surprise` function (from the setup cell) on each bag and store:
- `B1_surprise_a` — surprise of the all-red bag
- `B1_surprise_b` — surprise of the 5+5 bag
- `B1_surprise_c` — surprise of the 1+9 bag

**Expected:** three numbers (they print with full decimals — keep them as they come). Check yourself: the pure bag must be exactly 0, and the 5+5 bag is the most surprising.
**What you should learn:** the surprise number is computable from counts alone — no formula memorized, just counting colors.

---

## Problem B2 — The Champion of the Light Box (1 pt)

**Story:** the machine already picked the root question (`weight ≥ 14`). Now the light box (7 animals: 4 cats + 3 small dogs) needs its question. Three candidates are on the table.
**Task:** in cell `B2`, compute the gain of each candidate question on the light box, then store:
- `B2_gain_ears_825`, `B2_gain_ears_70`, `B2_gain_weight_375` — the three gains (numbers)
- `B2_champion` — the winning question, as the exact string `"ear_length >= 8.25"` / `"ear_length >= 7.0"` / `"weight >= 3.75"`

**Expected:** the champion is the question whose gain equals the ENTIRE surprise of the box — it sorts it completely.
**What you should learn:** the champion is the biggest surprise-drop, not the biggest group moved. You just derived the machine's second question yourself.

---

## Problem B3 — The Titanic Champion + the Split Plot (1 pt — tonight's Ship)

**Story:** Session 1, you voted on which feature matters for Titanic survival. Tonight your vote gets a number.
**Task:** in cell `B3`, build the gain leaderboard for the four features (`pclass`, `age`, `fare`, `is_female`) exactly like cell A5, then store:
- `B3_champion_feature` — the winning feature name (one of `"is_female"`, `"pclass"`, `"fare"`, `"age"`)
- `B3_champion_gain` — its gain (number)

Then complete the TODO plot lines: the full box (survived 288 / did not 424) next to the two boxes after the champion question (men 453, 21% survived · women 259, 75% survived). Save the notebook with the plot visible — this annotated plot is the Ship.
**Expected:** the champion matches what the class voted in Session 1 — and what the machine asked first.
**What you should learn:** feature importance is not a vibe — it is a measured number, and you can compute it.

---

## Hint appendix (try without it first)

- B1: `surprise(["red"] * 10)` — the function is already in your setup cell.
- B2: the `gain_light` helper from cell A3b is written in the starter cell — call it with the three candidate questions.
- B3: copy the `gain_feature` loop from A5; the champion is the top row of your leaderboard. For the plot, two `bar` calls with English labels and a title.
