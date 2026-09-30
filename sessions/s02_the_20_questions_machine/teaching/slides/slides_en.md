---
marp: true
theme: mlcourse-blue-fa
paginate: true
---

<!-- _class: lead -->
<!-- _paginate: false -->

# The 20-Questions Machine

## Day Two — You Draw a Decision Tree

**Block 1 · Session 2**

*By the end of today, YOU will draw a decision tree by hand.*

![hero](shared_hero.png)

<!--
INSTRUCTOR — Session 2 of 32. 60 min teaching + 60 min problem-solving.
BEFORE CLASS: PART 0 demo tested; animals_table.pdf printed per student; blank paper; judge 3/3.
TIMING: hook 0-5, anatomy 5-15, reading 15-25, depth 25-35, lab 35-50, quiz 50-55, handout 55-60.
-->

---
<!-- _class: hook -->

# The Game of 20 Questions

I'm thinking of an animal.

You may only ask **yes/no** questions.

*The counter climbs...*

![art](../../assets/twenty_questions.png)

<!--
[0:00] HOOK beat 1 — human game, no notebook yet.
You think of a WOLF. Class asks yes/no only. Count questions on the board, aloud.
When they get it: do NOT clear the board — the path feeds slide 3.
Never skip.
-->

---
<!-- _class: hook -->

# You Were a Tree Just Now

Every answer was a **door** — every door, a new path.

This shape is **a decision tree** — Session 1's machine plays it too.

<!--
[~3:00] Redraw the game's path as a diagram: question circles, answer doors, verdict.
SAY: "Every answer was a door. You just walked a decision tree. Last session's red line? ONE question, ONE door."
EXPECT a student to make the red-line connection themselves.
-->

---
<!-- _class: hook -->

# Now Let the Machine Play

Last session: one question ← the puppy became a cat!

Today: it is allowed **two questions.**

<!--
[RUN: PART 0 demo cell] Depth-1 vs depth-2, puppy verdict under each.
SAY: "One question got the puppy wrong. Watch what a second question does."
EXPECT: "It fixed it?!" Close: "You've played decision trees your whole life."
FALLBACK: narrate from slides 7 and 10.
-->

---
<!-- _class: definition -->

# Tree Anatomy

**Node** = a question — a fork with a signpost

**Branch** = one answer's door (yes/no)

**Leaf** = the final room — where the verdict is said

![art](../../assets/tree_anatomy.png)

<!--
[5:00] NAME slide — experience already happened.
Point at the BOARD path: node = question, branch = door, leaf = verdict room.
[MISCONCEPTION] the tree cannot change questions mid-game — path is fixed.
CHECK: "Max leaves of a 2-question tree?" (4)
-->

---
<!-- _class: quiz -->

# Which Door Does the Elephant Take?

`weight >= 14?` ← yes

`ears >= 8.25?` ← yes

*Verdict: big dog!*

<!--
INTERACTION (2 min): class shouts the elephant's door at each node on the projected tree.
Trace: weight >= 14 yes, ears >= 8.25 yes, big-dog room.
SAY: "A leaf says ONE word for whatever reaches it — even a 3-ton elephant." 
-->

---

# Session 1's Machine = One Question

![depth-1 tree](../../assets/decision_tree_s02_d1.png)

Last session's red line, drawn as a tree.

*One question, two doors, two verdicts.*

<!--
[RUN: cell A1] Depth-1 tree picture — same mechanic as last session's red line.
SAY: "The line and this picture are the SAME thing. Only the drawing changed."
Seals continuity: Session 1's model was a tree all along.
-->

---
<!-- _class: definition -->

# The Root: The First Question

The machine chose `weight >= 14`.

What did YOU ask first in the game?

<!--
[15:00] Segment B. NAME: root = the first fork.
[RUN: cell A2] class reads both questions aloud for a wolf.
INTERACTION: their first questions from the hook — most asked weight too.
Plant: "the machine picked exactly 14. Why? Next session." 
-->

---
<!-- _class: wow -->

# Two Questions, Three Rooms

![depth-2 tree](../../assets/decision_tree_s02_d2.png)

Cats, big dogs, small dogs — each gets its own room.

<!--
[RUN: cell A2] THE punchline picture — real plot_tree output.
SAY: "One question split light from heavy. The second split cats from small dogs."
ASK before running: "Which room does the puppy reach now?" — let them say it.
-->

---
<!-- _class: quiz -->

# Read the Path: puppy

`weight >= 14?` ← no

`ears >= 8.25?` ← yes

*Verdict: small dog — correct!*

<!--
[RUN: cell A3] visitors: wolf, puppy, elephant — students trace BEFORE the machine answers.
puppy: weight no, ears yes, small-dog room — correct.
SAY: "The second question — ears — is the cure for last session's mistake." 
-->

---
<!-- _class: definition -->

# The Depth Knob (max_depth)

`max_depth` = the maximum number of questions

Depth 1: the puppy becomes a cat — 73% correct

Depth 2: everything correct — 100%

<!--
[25:00] Segment C. NAME: depth = longest question path.
[RUN: cell A4] depth 1 vs 2, accuracy 73% then 100%.
[MISCONCEPTION] more depth is not automatically smarter — WE turn the knob.
CHECK: "Leaves at depth 1 / 2 / 3?" (2/4/8)
-->

---
<!-- _class: codespot wow -->

# Put Your Hand on the Knob

```python
max_depth = 2   # change the number

model = DecisionTreeClassifier(max_depth=max_depth)
model.fit(X, y)
```

*What is the smallest perfect depth?*

<!--
[RUN: cell A5 — students change the number THEMSELVES]
RACE: first to find the smallest perfect depth (2) shouts it.
Then max_depth=10 — the tree becomes a jungle; let them laugh.
"More questions is not always better — WHY is a story for later." 
-->

---
<!-- _class: hook -->

# Lab: Draw Your Own Tree

11 animals. Three rooms. Yes/no questions only.

*Paper and pencil. Any tree that works, wins.*

![art](../../assets/paper_tree.png)

<!--
[35:00] THE LAB — the Ship. Hand out animals_table.pdf + blank paper.
RULES: yes/no questions about weight and ears only. Any tree that works, wins.
CIRCULATE. Stuck hint: "which question splits cats from dogs first?"
~10 minutes — the session's emotional core. Do not rush.
-->

---
<!-- _class: quiz -->

# The Tree Battle

Swap papers.

Surprise animals: **rabbit. fox. hamster. sparrow. lion.**

*Funniest failure gets applause!*

<!--
[~45:00] BATTLE: pairs swap papers; test on the surprise zoo (rabbit, fox, hamster, sparrow, lion).
Verdicts read door-by-door, out loud. Funniest failure gets applause.
Diagnose each failure: "WHICH question let you down?"
[MISCONCEPTION] there is no single correct tree.
-->

---
<!-- _class: dark -->

# Your Tree = The Machine's Tree

Your paper tree and `plot_tree` are the same shape.

Question, door, question, door, verdict.

*Tonight: commit a photo of your tree.*

<!--
[~48:00] Connect. [RUN: cell A6] machine tree; project a student's paper tree next to it if possible.
SAY: "Same game, same shape. Yours you can tape to a wall."
SHIP logistics on screen: photo -> s02_tree.jpg -> commit tonight.
-->

---
<!-- _class: quiz -->

![band](shared_band.png)

# What You Learned Today

- A tree = **node, branch, leaf**
- **Root** = the first question; **depth** = the most questions
- Depth 2 cured the puppy mistake
- Different trees can all be correct

<!--
[50:00] CONSOLIDATION — cold call, one question per student:
tree parts? why did depth-2 fix the puppy? what is max_depth? can two trees both be right?
If anyone stumbles on Q1-3, re-explain NOW.
-->

---

# Tonight's Delivery

A photo of your paper tree ← `s02_tree.jpg` ← your GitHub repo

Three small notebook problems: count, predict, find the right depth

<!--
[55:00] SHIP + loop OUT LOUD: photo committed tonight; 3 problems (20-30 min); next session opens by solving them TOGETHER from their attempts.
Show the judge command: python judge/run.py s02_notebook.ipynb
-->

---
<!-- _class: handout -->

# At-Home Problems (3)

1. **B1** The question and leaf counter
2. **B2** Which room does the elephant reach?
3. **B3** The smallest perfect depth

Deadline: before the next (problem-solving) session.

<!--
One sentence of story per problem:
B1 count the tree's questions and rooms; B2 trace the elephant's path; B3 find the smallest perfect depth with the loop.
Deadline: before the problem-solving session.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Next Session

Where did the machine get `weight >= 14`?

**WHO chooses the questions?**

Next time: you become the question-picker.

![rocket](shared_closing.png)

<!--
[60:00 — end on time.] CLIFFHANGER verbatim:
"WHO taught the MACHINE to pick its questions? Why weight >= 14 and not 7?
Next time: you become the question-picker."
AFTER CLASS (48h): fill the retro note in the session README.
-->
