# Session 2 — At-Home Solutions (worked reasoning)

## B1 — The Leaf Counter (1 pt)

**Reasoning:** the depth-2 tree on the 11 animals asks a first question (`weight ≤ 14`?) and, **on the LIGHT side only**, a second question (`ear length ≤ 8.25`?) that separates the cats from the small dogs. The heavy side needs no second question — all four big dogs land straight in the big-dog leaf. So the tree has 2 question-nodes and 3 leaves (cat room, small-dog room, big-dog room). Nicer check: `model.get_depth()` and `model.get_n_leaves()`.

**Common wrong approach:** assuming every branch asks the same questions. A tree asks the *next* question only where it is needed — branches can have different depths (here: heavy animals get their verdict after ONE question).

**Answer:**
```python
B1_model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)
B1_num_questions = 2
B1_num_leaves = 3
```

**Self-check:** `B1_model.get_depth() == 2` and `B1_model.get_n_leaves() == 3`.

**Common wrong approach:** counting 2 as "questions per animal visited" vs "questions the tree contains" — the tree CONTAINS 2 question nodes total here. A student who answers `B1_num_leaves = 4` is thinking "max leaves of depth-2" (2² = 4) instead of counting THIS tree's actual leaves (3): have them re-trace each animal's path and notice two paths end in the same room.

## B2 — The Elephant's Room (1 pt)

**Reasoning:** trace the path: `weight ≤ 14`? 3000 ≤ 14 → NO, the heavy corridor — and that corridor IS already the big-dog leaf. **The elephant hears only ONE question** (the ear question lives on the light side: that's where cats and small dogs still need separating). The elephant is not a dog, but the tree only knows rooms, not animals.

**Answer:**
```python
model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)
elephant = pd.DataFrame({"وزن": [3000], "طول_گوش": [20]})
B2_elephant_room = model.predict(elephant[X.columns])[0]   # "سگ بزرگ"
```

**Common wrong approach:** typing `"فیل"` or `"سگ"` by hand — the verdict must be the exact string the tree can say, copied from the prediction. The tree's vocabulary is only its three room names.

## B3 — The Smallest Perfect Depth (1 pt)

**Reasoning:** at depth 1 the tree separates light from heavy animals only — the three small dogs (poodle, yorkshire, papillon) all land in the cat room with the puppy (73% correct). At depth 2 the ear-length question separates cats from small dogs: 100%. So the smallest perfect depth is 2.

**Answer:**
```python
best_depth = None
for depth in range(1, 6):
    m = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X, y)
    if (m.predict(X) == y).all():
        best_depth = depth
        break
B3_min_depth = best_depth   # 2
```

**Common wrong approach:** answering 3 or 5 "because more is safer" — the loop's `break` stops at the FIRST perfect depth; have them print the accuracy at each depth and watch it hit 100% at 2 and stay there. (Why it doesn't drop again — overfitting — is deliberately NOT this session's topic; it returns in Block 2.)
