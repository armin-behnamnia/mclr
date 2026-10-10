# Session 3 — At-Home Solutions (worked reasoning)

## B1 — The Surprise of Three Bags (1 pt)

**Reasoning:** the surprise number comes from the color counts alone. Bag A is pure (one color) — zero surprise, you cannot be surprised by a draw you can predict. Bag B (5+5) is the most mixed two-color bag possible — maximum surprise for two colors: exactly 1.0 in bits. Bag C (1+9) has a dominant color — draws are fairly predictable, so the surprise sits well below 1.

**Answer:**
```python
B1_surprise_a = surprise(["قرمز"] * 10)                      # 0.0
B1_surprise_b = surprise(["قرمز"] * 5 + ["آبی"] * 5)         # 1.0
B1_surprise_c = surprise(["قرمز"] * 1 + ["آبی"] * 9)         # 0.469
```

**Common wrong approach:** expecting bag C to score higher than bag B "because it has more balls of one color" — more of ONE color is exactly what makes it MORE predictable (LESS surprise). The even split is always the most surprising box for its number of colors.

## B2 — The Champion of the Light Box (1 pt)

**Reasoning:** the light box holds 4 cats + 3 small dogs (surprise 0.985). Compute each candidate's gain:
- `طول_گوش ≥ 8.25`: left = 4 cats, right = 3 small dogs — BOTH sides pure. Gain = 0.985 — the entire surprise of the box, removed.
- `طول_گوش ≥ 7.0`: left = 3 cats, right = 1 cat + 3 small dogs — still mixed on the right. Gain ≈ 0.522.
- `وزن ≥ 3.75`: left = 1 cat + 1 small dog, right = 3 cats + 2 small dogs — both sides as mixed as before. Gain ≈ 0.006 — a door that moves animals but sorts nothing.

**Answer:**
```python
B2_gain_ears_825 = 0.985   # (gain_light("طول_گوش", 8.25))
B2_gain_ears_70  = 0.522
B2_gain_weight_375 = 0.006
B2_champion = "طول_گوش ≥ 8.25"
```

**Common wrong approach:** picking `وزن ≥ 3.75` because it "splits the box more evenly" — evenness is not the goal, sorted-ness is. Have the student print the two sides of each split; the champion is the one where both printouts show a single group.

## B3 — The Titanic Champion + the Split Plot (1 pt)

**Reasoning:** build each feature's best question and its gain (same loop as A5): `is_female` 0.214, `pclass` 0.083, `fare` 0.069, `age` 0.018. The champion is `is_female` — the same feature the class voted for in Session 1. After the champion question: men's box 453 passengers with 21% survival, women's box 259 passengers with 75% survival — far more sorted than the original 288/424 box.

**Answer:**
```python
B3_champion_feature = "is_female"
B3_champion_gain = 0.214
# plot: full box bars (288 / 424) next to men-vs-women survival bars (21% / 75%)
```

**Common wrong approach:** reading the champion's gain from the wrong row of the leaderboard (the DataFrame is sorted descending — row 1 is the champion), or normalizing gains to percentages. Have them re-run cell A5 and compare the printed table with their stored value.
