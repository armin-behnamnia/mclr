# Session 3 — In-Class Problems (problem-solving hour)

*Solved together, instructor with the class — after the at-home set is fully solved. Discussion problems, not silent work.*

## C1 — The Fixed-Threshold Game (10 min)

Cell C1 plots the gain of `weight ≥ t` for every t from 1 to 30.

**The game:** before running, each student draws (with a finger in the air) the shape of the curve. Run. Compare.

**Discussion:**
- Why is every threshold between 6 and 22 equally champion? (all of them split the same two groups: cats + small dogs on one side, big dogs on the other — same sides, same surprise-drop)
- Why does the gain crash to zero below ~4 and above ~38? (the question stops splitting anything — one side becomes empty; a door nobody walks through sorts nothing)
- Connect to S2's C3: the "corridor of valid thresholds" now has a picture — a flat plateau at the top.

**The point:** the machine's `14` is not magic — it is one point on a plateau. ANY threshold in the corridor would have built the same tree.

## C2 — The One-Animal Champion (10 min)

A new box: 10 big dogs + 1 cat (3 kg). Cell C2 computes gains.

**Discussion:**
- `weight ≥ 20` moves exactly ONE animal out of eleven — yet its gain is the biggest (it makes the box pure). The mid-dogs split `weight ≥ 34` moves five animals and leaves both sides mixed.
- So: does the machine want to move MANY animals or to SORT the box? (sort — always sort)
- Misconception killed live: "a good question splits the data in half" is now obviously false.

**The point:** gain measures sorted-ness gained, not animals moved. This is why a one-animal question could still beat a fancy five-animal split.

## C3 — Titanic, Round Two (15 min)

The root question was `is_female`. Cell C3 reruns the game INSIDE the women's box (259 passengers, 75% survived).

**Discussion:**
- Predict first: what wins round two inside the women's box? (class — its gain 0.22 beats fare's 0.10 and age's 0.01; richer women survived more)
- The tree from S1's cell A9 asked exactly this as its second question on the women's side (`pclass ≤ 2.5`) — check the old picture.
- Final discussion: what if the table had a column for "which lifeboat"? (its gain would dwarf everything — and the tree would ask it first). But nobody measured lifeboats. **The machine only shops among the columns we hand it.** Feature choice is OUR job.

**The point (honest ML):** the question-picker is powerful, but it can only pick from the menu we write. Good features come from understanding the problem — that is a human job (and returns in Session 7: Garbage In, Garbage Out).
