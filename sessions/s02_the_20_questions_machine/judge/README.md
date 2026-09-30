# Session 2 Judge

## How to run
```
python judge/run.py <student_notebook.ipynb>
```
(from the session root, with the student's `s02_notebook.ipynb`).

## Rubric — 3 points
| Problem | Points | Checks |
|---|---|---|
| B1 Leaf Counter | 1 | `B1_num_questions` == fixture, `B1_num_leaves` == fixture |
| B2 Elephant's Room | 1 | `B2_elephant_room` equals the exact verdict string |
| B3 Smallest Perfect Depth | 1 | `B3_min_depth` equals the smallest depth with 100% training accuracy |

Expected values live in `judge/data/expected.json` (fixtures only — no plaintext answers in student files).

## Determinism
All trees use `random_state=42`; the loop search is deterministic. Two runs on the same notebook give identical scores.

## Deadline / policy
At-home problems are due **before the problem-solving session**. Late or partial attempts still get graded and are used as the live-solving fuel — attempt everything, commit often.
