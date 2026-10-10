# Session 2 — At-Home Problems

**Deadline:** before the next problem-solving session. **Time budget:** ~20–30 minutes.
**What to submit:** your `s02_notebook.ipynb` with cells B1–B3 filled — AND your Ship: a photo of your hand-drawn paper tree, committed as `s02_tree.jpg`.
**Judge:** `python judge/run.py s02_notebook.ipynb` — friendly feedback, partial credit, no tricks.

---

## Problem B1 — The Leaf Counter (1 pt)

**Story:** the machine's depth-2 tree (cell A2) asks some questions and ends in some rooms. Count them.
**Task:** in cell `B1`, train the depth-2 tree exactly like in class (`max_depth=2`, `random_state=42`, on `X` and `y` from PART A), then fill:
- `B1_num_questions` — how many questions does this tree ask? (look at the tree picture: count the question-circles you pass from root to the deepest leaf)
- `B1_num_leaves` — how many leaves (final rooms)?

**Expected:** two integers. (Check yourself: `B1_model.get_depth()` and `B1_model.get_n_leaves()` should agree.)
**What you should learn:** reading a tree's structure — questions and rooms are countable facts, not vibes.

---

## Problem B2 — The Elephant's Room (1 pt)

**Story:** the elephant (3000 kg, ears 20 cm) walks the tree's corridors like everyone else. Which room does it end in?
**Task:** in cell `B2`, build the depth-2 tree again and predict for the elephant. Store the verdict string in:
- `B2_elephant_room` — one of `"گربه"`, `"سگ بزرگ"`, `"سگ کوچک"`

**Expected:** the exact verdict string (copy it from the prediction, don't type from memory).
**What you should learn:** a leaf says ONE word for everything that reaches it — even an elephant.

---

## Problem B3 — The Smallest Perfect Depth (1 pt)

**Story:** one question misclassifies the small dogs; two questions fix everything. Is two the SMALLEST perfect depth? Prove it with a loop.
**Task:** in cell `B3`, loop `depth` from 1 to 5; find the smallest depth where the tree classifies all 11 animals correctly. Store it in:
- `B3_min_depth` — the smallest perfect depth (integer)

**Expected:** one integer. The starter cell gives you the loop — you complete the TODO: the condition that stops at the first depth where all 11 animals are correct (the hint line above the TODO tells you the exact expression).
**What you should learn:** depth is a knob with a measurable effect — the smallest sufficient depth is a fact you can find, not a guess.

---

## Hint appendix (try without it first)

- B1: `plot_tree` draws question-circles and room-boxes; `get_depth()` counts the longest question-path.
- B2: `pd.DataFrame({"وزن": [3000], "طول_گوش": [20]})` — and the prediction comes back as a string.
- B3: the loop breaks at the first depth where `(m.predict(X) == y).all()` is true.
