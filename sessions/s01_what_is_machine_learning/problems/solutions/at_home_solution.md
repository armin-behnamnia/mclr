# Session 1 — At-Home Solutions (instructor only)

## B1 — The Feature Detective (1 pt)
**Answer:** `["hours_studied", "previous_score"]`
**Reasoning:** only these two features carry signal about passing. `name` identifies a person but predicts nothing about a *new* person; `favorite_color` and `shoe_size` have no connection to test performance.
**Common wrong approach:** including `name` ("because smart kids have names we know!") — address it live: *whatever we don't give the model does not exist for the model; and whatever we give it that carries no signal only adds noise.*

## B2 — Build Your Own Dataset (1 pt)
**Answer (example):**
```python
B2_animals = pd.DataFrame({
 "size": ["small", "large", "medium", "small", "large"],
 "can_fly": [1, 0, 0, 0, 1],
 "animal": ["sparrow", "elephant", "dog", "cat", "eagle"],
})
```
**Reasoning:** 5 rows, exact column names, correct value types. Any 4+ distinct animals pass.
**Common wrong approach:** reusing the classroom fruit table or swapping column names (`"animal"` vs `"animals"`). The judge checks column names exactly — in real pipelines, column-name mismatches are the #1 silent bug. Say this out loud.

## B3 — The 3 Magic Lines (1 pt)
**Answer:**
```python
B3_model = DecisionTreeClassifier(random_state=42) # 1. pick a student
B3_model.fit(B3_X, B3_y) # 2. let it study
B3_prediction = B3_model.predict([[1, 0]])[0] # 3. ask a question
```
**Reasoning:** create → fit → predict, on the student's own B2 dataset. `size` is mapped to numbers (`small=0, medium=1, large=2`) because sklearn needs numeric inputs — this mapping is a first taste of *encoding*, formally taught in Session 7.
**Common wrong approach:** swapping `fit` arguments (`fit(y, X)`); it errors with a confusing message — show the error on screen and decode it together. Reading error messages is a course skill.

## B4 — The Survival Predictor (1 pt)
**Answer:** `B4_answer = 0` (does not survive)
**Reasoning:** rebuild `X`/`y` as in A7, train `DecisionTreeClassifier(max_depth=3, random_state=42)`, predict on `{"pclass": 3, "age": 12, "fare": 7.5, "is_female": 0}`. The 3rd-class boy does not survive — the tree's first question (`is_female`) sends him down the harsher branch, and within the male branch, class and age dominate.
**Common wrong approach:** training on `titanic` directly with the string `sex` column → sklearn raises a ValueError about strings. Solution shown live: the `is_female` numeric trick from A7. This is *encoding* again — the problem will be solved properly with one-hot encoding in Session 7; today students just need the workaround.

## Judge answer key (for `judge/data/expected.json`)
```json
{
 "B1_good_features": ["hours_studied", "previous_score"],
 "B4_answer": 0
}
```
B2 and B3 are validated structurally (columns, row count, fitted model, correct prediction on a probe) — see `judge/tests/test_solutions.py`.
