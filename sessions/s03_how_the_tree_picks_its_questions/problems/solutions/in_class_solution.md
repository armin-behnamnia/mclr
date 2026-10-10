# Session 3 — In-Class Solutions (discussion guide)

## C1 — The Fixed-Threshold Game

**What the plot shows (verified):** the gain of `weight ≥ t` is zero below ~4 (one side empty — the question splits nothing), jumps at the cat/small-dog boundary, stays on a flat plateau for every t between 6 and 22 (all such thresholds produce the SAME two groups: 4 cats + 3 small dogs vs 4 big dogs — same sides, same gain 0.95), and crashes to zero above ~38.

**Where the discussion should land:** the machine's `14` is one point on a plateau, not a magic number. Any threshold in the corridor builds the same tree. S2's C3 question ("how many valid trees exist?") now has a picture: infinitely many thresholds, all equally champion — the machine keeps the first one it measured.

**Board moment:** draw the plateau; label the corridor 6–22; write `14` as one dot on it.

## C2 — The One-Animal Champion

**Actual numbers (verified, bits):** box = 10 big dogs + 1 cat, surprise 0.439.
- `weight ≥ 20` (moves ONE animal out of eleven; leaves a pure cat box and a pure big-dog box): gain 0.439 — the ENTIRE surprise.
- `weight ≥ 34` (moves FIVE animals; both sides still mixed — 1 cat + 5 dogs vs 5 dogs): gain ≈ 0.085.
- `weight ≥ 44` (moves TWO animals; cat still mixed with 8 dogs on the left): gain ≈ 0.028.
- `weight ≥ 55`: one side empty — gain 0.

**Where the discussion should land:** the machine wants SORTED, not SPLIT-EVENLY. The one-animal question wins because it finishes the box. "A good question halves the data" is now dead — bury it loudly.

## C3 — Titanic, Round Two

**Actual numbers (verified):** inside the women's box (259 passengers, 75% survived, surprise 0.807): best gain `pclass` 0.223, `fare` 0.100, `age` 0.013. The champion of round two is **pclass** — and the S1 tree (cell A9) indeed asks `pclass ≤ 2.5` as its second question on the women's side. The leaderboard the class computes IS the tree the machine built — the whole black box is now open.

**Where the discussion should land:** the machine shops only among the table's columns. A hypothetical "lifeboat number" column would have dominated everything — nobody measured it. Feature choice is a human decision; scoring is the machine's. (This is the seed of Session 7 — Garbage In, Garbage Out — say one honest sentence about it and stop.)
