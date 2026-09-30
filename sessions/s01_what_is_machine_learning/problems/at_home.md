# Session 1 — At-Home Problems 

**Due: before the problem-solving session.** Solve directly in `s01_notebook.ipynb`, PART B.
Grade yourself: `python judge/run.py s01_notebook.ipynb`

**What you should learn:** building a dataset, training a model, and predicting with it — on your own.

---

## Problem B1 — The Feature Detective (1 pt)
A friend wants to predict **whether a student passes a test** and proposes these features:

`["name", "hours_studied", "favorite_color", "previous_score", "shoe_size"]`

**Task:** in cell `B1`, write as a Python list only the features that could actually help.

> *What you should learn from this:* a model can only be as smart as its features. If the clue carries no signal, the model is blind to it — whatever we don't give it does not exist for the model.

## Problem B2 — Build Your Own Dataset (1 pt)
**Task:** in cell `B2`, build a DataFrame of **at least 4 animals** with exactly the columns
`["size", "can_fly", "animal"]`, where `size` is `"small"`/`"medium"`/`"large"` and `can_fly` is `0`/`1`.

> *What you should learn:* you can create training data from the world around you. Every ML project starts exactly here.

## Problem B3 — The 3 Magic Lines (1 pt)
**Task:** in cell `B3`, complete the three `...` spots to train a decision tree on your animals
and predict what a medium-sized non-flying animal is.

> *What you should learn:* create → fit → predict is the rhythm of ALL of ML, not just today's model.

## Problem B4 — The Survival Predictor (1 pt)
**Task:** in cell `B4`, train your own Titanic model (`max_depth=3`, `random_state=42`) exactly like in class,
and predict survival for a **3rd-class, 12-year-old boy, fare 7.5**. Store `1` or `0` in `B4_answer`.

> *What you should learn:* you can reproduce the whole class pipeline from memory. That's the point.

---

### Stuck? 
- Re-run PART A in order — cell A7 builds `X` and `y` that B4 needs.
- The `fruits` and `titanic` tables already exist in your notebook — don't reload them.
- Ask a classmate first, then bring your **attempt** (not your emptiness ) to the problem-solving session.

### Ship 
When the judge says `4/4` — commit your notebook to your GitHub repo. That's your first Ship.
