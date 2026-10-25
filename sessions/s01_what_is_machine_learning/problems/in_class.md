# Session 1 — In-Class Problems (problem-solving session)

Solved *with* the class, AFTER the at-home problems are fully solved. Designed for discussion, not silent work.

## C1 — The Imagination Engine
Students invent their own passengers and interrogate the model.
**Discussion goal:** the model's answers follow the patterns of 1912, not common sense — who finds a prediction that feels unfair or strange? (e.g., a poor 3rd-class *girl* vs a rich 1st-class *boy*.) That strangeness is the model reflecting the data — plant this seed for Session 9 (fairness) and Session 4 (train vs test).

## C2 — Beat the human 
5 challenge passengers; students guess first, then the machine.
**Discussion goal:** where did the student's own "predictions" come from? (Their own internal examples — they are also a supervised learner.) The scoreboard is fun; the debrief is the lesson.

## C3 — Where does the machine's knowledge live?
**Discussion goal:** the model never read a history book, never heard of icebergs. Its entire "knowledge" is 714 rows of examples. Where exactly is it stored? *(In the questions/splits of the tree — which is exactly where Session 2 begins.)*

**Cut line:** if time runs short, cut C2's debrief, never C3 — C3 is the bridge to Session 2.

## Enrichment — teacher-led deep dive (`notebook/s01_deep_dive.ipynb`)

If the at-home problems (B1–B4) are already solved or the group is hungry for more, the teacher
can run the deep-dive notebook instead of/after C1–C3. It is teacher-run, ten stops, and every
stop asks the student to predict before the reveal:

- **Act I — open the box:** the animal machine's one question, the Titanic tree's own rules +
  feature importances, its confident guesses on impossible passengers, and the mirror-of-data
  effect (train on men only, ask about a first-class woman).
- **Act II — same three lines, any world:** study→pass, the same recipe *seeing* digits and
  *reading* spam.
- **Act III — how it chooses + the road ahead:** surprise/entropy and information gain measured
  live (the bridge into Session 2/3), then a roadmap figure to the course.

It ends on the same cliffhanger that opens Session 2: *who told the machine to ask about gender
first?* Load on the teacher's machine only; it is a tour, not graded work.
