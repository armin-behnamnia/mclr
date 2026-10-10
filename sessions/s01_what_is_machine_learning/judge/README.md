# Session 1 Judge

Grades the 4 at-home problems (B1–B4) from the student's `s01_notebook.ipynb`.

## Run
```bash
python judge/run.py <path/to/s01_notebook.ipynb>
```
Exits 0 on a perfect score, 1 otherwise.

## What it does
1. Executes every code cell of the notebook (magics and `!shell` lines stripped; a broken cell does not stop grading). A non-notebook or malformed file gets a friendly message, not a traceback.
2. Grades the four student variables against fixtures and structural checks.

## Rubric (4 points)
| Problem | Points | Check |
|---|---|---|
| B1 Feature Detective | 1 | exact set of signal features (fixture: `data/expected.json`) |
| B2 Own Dataset | 1 | structural: exact columns, ≥4 distinct animals, valid values |
| B3 Magic Lines | 1 | `B3_model` is a fitted tree that predicts; `B3_prediction` is that model's own answer for the medium, non-flying probe |
| B4 Survival Predictor | 1 | `B4_answer` equals fixture value |

## Notes
- No plaintext answer appears in any student-visible file; expected values live in `judge/data/expected.json`.
- Deterministic: student code is required to seed with `random_state=42`; two runs give identical scores.
- Feedback is specific: every failure names the problem and what to re-examine.

## Verified against
- the solution notebook → 4/4
- the untouched student starter → `SCORE: 0/4` with a "did you fill in cell BN?" hint per problem
- a deliberately broken notebook → helpful messages
- an empty notebook → `SCORE: 0/4`, no crash
- a malformed (non-JSON) file → friendly message, no traceback

## Collection & deadline
Students submit the notebook in their course GitHub repo, **due before the problem-solving session** (~20–30 min of work). Late submissions still get full feedback from the judge; grading policy on lateness is the instructor's call.
