---
marp: true
theme: mlcourse-blue-fa
paginate: true
---

<!-- _class: lead -->
<!-- _paginate: false -->

# How the Tree Picks Its Questions

## Day Three — You Become the Question-Picker

**Block 1 · Session 3**

*Today you learn which question is better — and why.*

![hero](shared_hero.png)

<!--
INSTRUCTOR — Session 3 of 32. 60 min teaching + 60 min problem-solving.
BEFORE CLASS: PART 0 demo tested; three grab-bags prepared (8 blue; 4+4; 3+3+2); slides assets exist.
TIMING: hook 0-5, sortedness 5-15, surprise 15-25, the game 25-35, Titanic 35-45, you-be-the-machine 45-50, quiz 50-55, handout 55-60.
-->

---
<!-- _class: hook -->

# Two Boxes, One Question

Goal: every box becomes **one color.**

Which box needs help? Which one is done?

![art](../../assets/two_boxes.png)

<!--
[0:00] HOOK beat 1 — two boxes on the board (or magnets).
Box A: 4 blue + 4 red mixed. Box B: 8 blue.
ASK: "Which box needs help?" — they answer instantly: A.
The word "sorted" arrives TODAY. Do not name it yet.
-->

---
<!-- _class: hook -->

# Which Question Sorts Best?

A new box: 2 blue + 2 red.

Vote: "is it red?" or "is it big?"

*Keep your votes — the machine plays this exact game.*

<!--
HOOK beat 2 — the vote. Class votes on the TWO candidate questions on the slide.
"Is it red?" obviously wins — half the class wonders why we even asked.
Keep the votes on the board: the losing questions return on slide 6.
-->

---
<!-- _class: hook -->

# The Machine Scores Its Questions

Last session the machine asked `weight >= 14`. **Why 14?**

Watch: it tries every question and gives each a score.

![art](../../assets/split_champion.png)

<!--
[RUN: PART 0 demo cell] The leaderboard prints: every candidate question with its gain.
SAY: "It SHOPS for questions. It scores each one. The champion gets asked."
EXPECT: "It tried ALL the questions?!" — the S2 mystery is answered.
FALLBACK: narrate from the leaderboard slide (the committed picture in assets).
-->

---
<!-- _class: definition -->

# Sorted-ness (Purity)

A good question leaves each side as **one thing.**

A useless question cuts the box but keeps the mess.

<!--
[5:00] NAME slide — experience already happened (the votes).
[MISCONCEPTION] splitting evenly is NOT the goal — sorting is. A question can halve the box and sort nothing.
CHECK: "The elephant's side of our S2 tree — mixed or pure?" (pure — that's why the tree stopped asking.)
-->

---
<!-- _class: wow -->

# The Useless Question

![useless question](../../assets/split_bad.png)

The no-door IS pure — but holds only 1 animal! The other 10 stay just as mixed.

<!--
SHOW the useless question: ear >= 4.5 splits off ONE cat (a pure but tiny side); the other 10 stay just as mixed.
POINT at the balls: "One side IS pure — but it holds only 1 of the 11. The score cares about the WHOLE box."
This slide teaches the weighted average WITHOUT the word — why a "perfectly pure" side can still earn almost nothing (gain 0.14).
-->

---
<!-- _class: wow -->

# The Champion Question

![champion question](../../assets/split_champion_tree.png)

The yes-door: only big dogs. **Pure!**

<!--
SHOW the champion: weight >= 14 — heavy side is PURE (4 big dogs).
TRACE: left side still has cats + small dogs mixed — a question for IT comes later (the light-box round).
SAY: "Same box, same two doors — but THIS question sorted. THAT difference is what the machine measures."
-->

---
<!-- _class: quiz -->

# Sorted or Just Cut?

`weight >= 30` ← no: 9 mixed animals · yes: 2 big dogs

*Did it sort — or only cut?*

<!--
USE-IT (2 min): class votes on weight >= 30 before you comment.
Answer: PARTIALLY sorted — the yes-side is pure (2 big dogs), the no-side stays mixed.
So it is a real question, just not the champion — its gain is smaller (0.32 vs 0.95).
-->

---
<!-- _class: hook -->

# The Grab Bags

Three bags, one blind draw each.

Before every draw: say your guess. Then: how surprised were you?

![art](../../assets/grab_bag.png)

<!--
[15:00] Segment B — the grab-bag game. 3 min, high energy.
Bag 1 (8 blue): no surprise. Bag 2 (4+4): coin-flip. Bag 3 (3+3+2): maximum.
Volunteer draws blind; class rates surprise 0-2 with fingers BEFORE each draw.
They just invented the ranking: pure = 0, mixed = big.
-->

---
<!-- _class: definition -->

# Surprise (Entropy)

The box's messiness number:

- pure box ← **0**
- more mixed ← bigger number

*It comes from counting colors. No formula needed.*

![art](../../assets/slot_machine.png)

<!--
NAME slide. Write on board: the three bags get their numbers (0, 1, 1.56).
[MISCONCEPTION] entropy is NOT the machine thinking — it's a number from counting colors. The least magical part of the course.
[RUN: cell A2] machine prints the same ranking — check together.
-->

---
<!-- _class: quiz -->

# The 11-Animal Box: How Much?

4 cats, 4 big dogs, 3 small dogs.

Guess the surprise first, then check.

<!--
USE-IT (cell A2b): class predicts "middle?" then runs.
Answer: 1.57 — almost the 3-color bag (same kind of mix: three things, none dominating).
-->

---
<!-- _class: definition -->

# Game: You Give the Scores

On the board: each question → two doors → who stands on each side?

Teams of two: compute "mess before minus mess after" for every question.

**Shout the champion!**

<!--
[25:00] Segment C — THE game, EXPERIENCE first. No vocabulary yet.
The score card on the board: question | sides | surprise after | score.
Teams of two compute the 5 candidate questions (content.md Segment C). First correct champion shouts.
Watch for the TIE: weight >= 14 and ear >= 8.25 both score 0.95 — let a team notice it themselves.
-->

---
<!-- _class: definition -->

# A Question's Score: Information Gain

**gain = surprise before − surprise after**

The champion question: the biggest gain.

<!--
NAME slide — what the teams just computed BY HAND has a name: information gain.
[MISCONCEPTION] the champion is NOT the purest side — it is the biggest surprise-drop for the WHOLE box
(the bad question's one-animal pure side won almost nothing).
-->

---
<!-- _class: wow -->

# The Leaderboard

![animals leaderboard](../../assets/leaderboard_animals.png)

The champions TIE: `weight >= 14` and `ears >= 8.25`.

<!--
[RUN: cell A3] the machine's leaderboard — same ranking the class computed.
THE TIE: both champions gain 0.95. The machine breaks ties by column order (weight first) — boring, honest.
SAY: "It plays this game on EVERY node — millions of times per tree."
-->

---
<!-- _class: quiz -->

# Round Two: The Light Box

7 animals: 4 cats + 3 small dogs. Surprise: 0.99

Who is THIS box's champion?

<!--
USE-IT (cell A3b): class predicts BEFORE running.
Answer: ear >= 8.25 — takes the box to ZERO surprise (both sides pure).
SAY: "You just derived the S2 tree's second question yourselves."
-->

---
<!-- _class: hook -->

# The Machine Plays It on Titanic

712 passengers. A mixed box: 288 survived, 424 did not.

*Session 1's data — this time with a score.*

<!--
[35:00] Segment D — THE MOMENT. Students code along cells A4-A5.
A4: the Titanic box, surprise 0.97.
ASK: "Is this box sorted? What's our surprise?"
-->

---
<!-- _class: wow -->

# Titanic's Champion

![titanic champion](../../assets/titanic_champion.png)

`is_female` — gain 0.21, nearly three times the runner-up (0.08).

<!--
[RUN: cell A5] the leaderboard: is_female 0.214 > pclass 0.083 > fare 0.069 > age 0.018.
CALLBACK: "Session 1, you voted gender matters most. You beat the machine to it — it just put a NUMBER on your vote."
[MISCONCEPTION] gain measures sorting, not CAUSES. One sentence only (Session 9 opens the fairness door properly).
-->

---
<!-- _class: codespot wow -->

# The Whole Secret

```python
for every possible question:
    score = surprise_before - surprise_after
champion = the biggest score
```

*There is no line four.*

<!--
[45:00] Segment E — you be the machine.
[RUN: cell A6] the loop in plain Python — best_question() on the full box, then on the light box.
REBUILD the S2 tree on the board AS A CLASS: root champion -> light box -> second champion.
HONEST BEAT: the machine doesn't think — it measures and takes the max, like a scale. Ties broken by column order.
-->

---
<!-- _class: dark -->

# Choosing Features Is OUR Job

The machine only shops among the table's columns.

"Does it hop?" is never asked — it isn't a column.

<!--
The C2 rabbit returns: no depth, no examples could fix it — the FIX was a new feature.
Feature choice is OUR job; scoring is the machine's. (Seed of Session 7 — one sentence, then stop.)
-->

---
<!-- _class: quiz -->

![band](shared_band.png)

# What You Learned Today

- **Purity** = one-color boxes
- **Entropy** = the surprise number
- **Gain** = before − after; champion = biggest gain
- Titanic's champion: `is_female` — Session 1's vote

<!--
[50:00] CONSOLIDATION — cold call, one question per student:
what does a good question do? what is entropy in kid words? how is a question scored?
why weight >= 14? what won on Titanic?
If anyone stumbles on Q1-3, re-explain NOW.
-->

---
<!-- _class: handout -->

# Tonight's Delivery + At-Home (3)

1. **B1** The surprise of three bags  2. **B2** The light box champion  3. **B3** Titanic's champion + the split plot ⛴️

`python judge/run.py s03_notebook.ipynb` ← instant score, anytime

"My Session 1 vote got its number today." — **your third Ship**

![ship](../../assets/annotated_plot.png)

<!--
[55:00] THE SHIP + handout in one. The annotated split plot IS the Ship (cell B3) — YOUR hand-analyzed Titanic map.
One sentence of story per problem:
B1 compute the bags' surprise numbers; B2 derive the light box champion; B3 the Titanic leaderboard + the annotated plot.
~20-30 min; deadline before the problem-solving session; next session solves them TOGETHER from their attempts.
First judge run is all-red — that's normal.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Next Session

The machine scored its questions on passengers it has SEEN...

What if it only memorized them?

Next time: the exam cheat test.

![rocket](shared_closing.png)

<!--
[60:00 — end on time.] CLIFFHANGER verbatim:
"What if a question is only 'good' on the animals it has SEEN?
Tomorrow: a student who memorized every exam answer — and how to catch a machine fooling itself."
NEXT SESSION: train vs test (S4).
AFTER CLASS (48h): fill the retro note in the session README.
-->
