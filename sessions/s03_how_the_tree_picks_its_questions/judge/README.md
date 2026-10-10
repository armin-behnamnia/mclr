# Session 3 Judge

## How to run
```
python judge/run.py <student_notebook.ipynb>
```
(from the session root, with the student's `s03_notebook.ipynb`).

## Rubric — 3 points
| Problem | Points | Checks |
|---|---|---|
| B1 Surprise of Three Bags | 1 | `B1_surprise_a/b/c` match the fixture (tolerance 1e-6) |
| B2 Champion of the Light Box | 1 | `B2_champion` is the exact winning question string AND the three gains match (tolerance 1e-4) |
| B3 Titanic Champion | 1 | `B3_champion_feature` is `is_female` AND `B3_champion_gain` matches (tolerance 1e-3) |

Expected values live in `judge/data/expected.json` (fixtures only — no plaintext answers in student files).

## Determinism
The bags are fixed lists; the animals table is the same as Session 2; Titanic is the same public CSV with the same dropna as Session 1 (`[survived, pclass, sex, age, fare, embarked]`, 712 rows). Entropy uses `scipy.stats.entropy(..., base=2)` — bits, matching the numbers used on the board. Two runs on the same notebook give identical scores.

## Deadline / policy
At-home problems are due **before the problem-solving session**. Late or partial attempts still get graded and are used as the live-solving fuel — attempt everything, commit often.
