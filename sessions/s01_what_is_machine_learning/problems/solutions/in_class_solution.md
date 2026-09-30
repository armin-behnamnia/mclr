# Session 1 — In-Class Solutions (instructor only)

## C1 — The Imagination Engine
Run students' invented passengers through `model.predict`. Good probes to have ready:
- 1st-class, age 40, fare 500, female → SURVIVES (model very confident)
- 3rd-class, age 30, fare 5, male → does not survive
- 3rd-class, age 6, female → SURVIVES (children get partial rescue in the tree's logic)
- 2nd-class, age 13, male → does not survive (interesting: a *child* male in 2nd class — discuss "women and children first" as data, not opinion)

**Debrief line:** "The machine is a mirror of 1912. If the data is unfair, the mirror is unfair. Remember this — it becomes a whole topic in Session 9."

## C2 — Beat the human 
Reference machine answers (max_depth=3, random_state=42, trained as in A8):
| Passenger | Machine |
|---|---|
| 1st, 35, 80, female | 1 |
| 2nd, 29, 26, male | 0 |
| 3rd, 21, 7, male | 0 |
| 1st, 60, 90, male | 0 |
| 3rd, 6, 12, female | 1 |

Students typically score 3–4/5 matching the machine. **Debrief:** "Where did YOUR predictions come from? You've also been trained — on movies and stories. You are also a supervised learner."

## C3 — Where does the knowledge live?
**Expected student answers:** "in the data", "in the model", "in the cloud" 
**Steer to:** the knowledge is *compressed into the tree's questions* — 714 examples distilled into ~15 yes/no questions. Nothing else is stored: no history, no words, no meaning.
**Closing bridge to Session 2:** "Those questions in the picture — who chose them? Not us. The machine picked them itself. *How*? That's next session."
