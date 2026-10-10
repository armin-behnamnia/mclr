---
marp: true
theme: mlcourse-blue-fa
paginate: true
---

<!-- _class: lead -->
<!-- _paginate: false -->

# What is Machine Learning?

## Day One — You Build an AI

**Block 1 · Session 1**

*By the end of today, YOU will train a working ML model.*

![hero](shared_hero.png)

<!--
INSTRUCTOR — Session 1 of 32. 60 min teaching + 60 min problem-solving.
BEFORE CLASS: test PART 0 demo cells; notebook runs top-to-bottom; assets exist.
TIMING: hook 0-5, big question 5-10, fruit game 10-20, supervised 20-30, Titanic 30-40, magic lines 40-50, quiz 50-55, handout 55-60.
-->

---
<!-- _class: hook -->

# The AI Special

# One demo. One red line. One question.

*Watch closely.*

<!--
[0:00] THE HOOK — run the single PART 0 demo cell, showmanship, dim lights.
SAY: "By the end of today, YOU will build what you are about to see."
FALLBACK: narrate from notes, never skip the hook.
-->

---
<!-- _class: hook -->

# The Animal Game

The machine sees only this: **8 labeled animals.**

Each animal = two numbers (weight, ear length) + one answer

*No rules were given to it. None.*

<!--
[RUN: PART 0 demo cell — مرحلهٔ ۱, the «جدول» marker] The 8-row table is ALL the machine sees.
SAY: "8 animals. Two numbers each, plus the answer. Nobody wrote a single rule."
EXPECT: "so what? it's just a table" — perfect, let them underestimate it.
-->

---
<!-- _class: hook -->

# The Machine's Line

From those 8 rows, the machine drew a line **all by itself.**

Behind the line: cats. In front: dogs.

**"Who drew this line?!"**

![art](../../assets/animal_game.png)

<!--
[RUN: PART 0 demo cell — مرحلهٔ ۳, the «خطِ ماشین» marker] The scatter: the machine's own red dashed line.
(مرحلهٔ ۲ was the silent .fit() — one invisible line of code.)
SAY: "No human drew this line. The machine found it hiding in those 8 rows."
EXPECT: "where did the line come from?!" — do NOT explain yet.
-->

---
<!-- _class: hook -->

# Now Let's Test It

Animals the machine has **never seen:**

Wolf ← dog. Neighbor's cat ← cat. **Correct!**

Puppy ← cat?! Elephant ← dog?!

**Its whole secret: one question — "weight ≤ 14 kg?"**

<!--
[RUN: PART 0 demo cell — مرحلهٔ ۴, the «امتحان» marker] Verdicts on unseen animals.
Let the puppy/elephant errors land as LAUGHS, then the cell prints the reveal: one question, weight ≤ 14 kg.
SAY: "It learned ONE question from 8 rows — and it still gets the puppy wrong. Learning is a guess."
SEED: "How does the machine pick that ONE question? Session 3 answers it — but first, Session 2."
-->

---

# The Big Question

How do we make computers smart?

<!--
[5:00] Segment A: rules vs learning. DRAW both boxes on the board — they stay ALL session.
Next slide's interaction is the core; don't lecture through it.
-->

---

# Way 1 — The Old Way: RULES

`data + RULES → answers`

Humans write every rule by hand.

"IF whiskers AND purrs THEN cat"

<!--
Board box 1: data + RULES = answers.
SAY: "For 50 years, smart people wrote thousands of IF-THEN rules. Worked... until it didn't."
Transition: "Let's try it ourselves. Cats. Easy, right?"
-->

---

# The Problem with Rules 

**You try: write rules to recognize a cat.**

Counterexamples welcome: hairless cats? cats in costumes? corgis?!

**Humans can't write enough rules.**

![cat rules](../../assets/cat_rules.png)

<!--
INTERACTION (3-4 min): students propose cat rules, you counter each.
"has fur" = hairless cat; "whiskers" = walrus; "small cute" = corgi puppy.
Concede: "This is why we don't write rules. We show examples."
-->

---

# Way 2 — Machine Learning

`data + answers → RULES`

**We show examples. The machine finds the rules.**

**That red line at the start? This.**

<!--
Board box 2 under box 1: data + answers = RULES — point silently, let it land.
REVEAL: the 8 animals WERE the examples; the red line WAS the rule.
CHECK (cold call): "What does the machine get and produce?" — examples with answers = rules.
Point back to these boxes at least 5 times today.
-->

---

<!-- _class: definition -->

# AI vs ML

**AI** = the dream (machines acting smart)

**ML** = the main way we get there (learning from data)

<!--
[~7:00] 60 seconds max. [MISCONCEPTION] AI and ML are NOT synonyms.
Analogy: AI = becoming a doctor (dream); ML = medical school (how).
-->

---

# The Fruit Game 

| Color | Size | Texture | ← Fruit |
|--------|-------|---------|---------|
| red | medium | smooth | ? |
| yellow | long | smooth | ? |
| purple | small | wrinkly | ? |

*Cover the answer column. Guess the fruit from the clues alone.*

<!--
[10:00] Segment B: fruit game. Cover the fruit column, read clues, class shouts labels. 2 min, high energy.
RUN cell A1: this table IS a DataFrame.
Next: which clue is most useful — vote.
-->

---
<!-- _class: definition -->

# New Vocabulary 

**Feature** = a clue *(a column)*

**Label** = the answer *(the column we predict)*

**Example** = one row = clues + answer

<!--
WRITE on board (never erased): feature, label, example.
Hooks (from the analogy map, nothing ad-hoc): feature = a clue; label = the answer; example = one solved exercise.
[MISCONCEPTION] the label is hidden at quiz time, not read by the model.
CHECK: "3 Titanic features + the label?"
-->

---

# Which Feature Matters?

Color? Size? Texture?

**Which clue is most useful for guessing the fruit?**

*(Vote. Debate. There is no wrong answer — yet.)*

<!--
INTERACTION: hands-up vote per feature, quick debate.
SAY: "You just did data science. Session 9 computes this as feature importance."
RUN cell A2 — students record their guess (revisited in Session 9).
-->

---

# Questions in a Chain

Line your guesses up into a chain:

ask color first, then size.

*A decision map — by hand, no code anywhere.*

<!--
EXPERIENCE before code: the class chains its own guesses.
DRAW with them: "red? apple. not red, long? banana. else grapes."
The decision tree arrives INTUITIVELY. The NAME is withheld until Session 2.
-->

---
<!-- _class: wow -->

# The Fruit Decision Map

![fruit decision map](../../assets/fruit_tree.png)

Your own guesses — just tidied up.

<!--
SHOW the fruit decision map. TRACE one fruit together: purple, small, wrinkly -> grapes.
[HONESTY BEAT — do it!] The map MISJUDGES 2 of the 6 fruits in A1's own table:
the green medium apple (map says grapes) and the yellow medium banana (map says grapes).
Trace the green apple on purpose, hit the wrong room, and SAY: "Our hand-drawn rules
already fail on 2 fruits out of 6 — now imagine 8 million pictures. THIS is why
the machine learns the map FROM the data instead." (This seed becomes Session 2's hook.)
SAY: "A human drew this. Next session: the MACHINE draws its own map — by itself."
DO NOT say "decision tree" yet.
-->

---

# Supervised Learning 

Learning from examples **that include the answers**.

![study with answer key, exam with hidden answers](../../assets/supervised_study_exam.png)

<!--
[20:00] Segment C. LIVE MINI-GAME: 4 solved fruit examples, then a 5th with hidden label — class predicts.
The picture IS the concept: RIGHT table = study with the answer key, LEFT = the new exam, answers hidden (RTL reading order).
SAY: "You just did supervised learning. Personally."
RUN cell A3: study table vs quiz table — the code version of exactly this picture.
-->

---

# Why "Supervised"?

No human is watching the model!

It means the **data contains the answers**.

*(History picked a weird word. )*

<!--
[MISCONCEPTION] "supervised" does NOT mean a person watches the model — the data has answers.
Use the laugh, then CHECK: "Why 'supervised'?" — examples come with answers.
-->

---

# The Titanic

![art](../../assets/titanic_ship.png)

891 passengers. 891 rows.

Every row is a life. Every column is a clue.

**Would YOU have survived?**

<!--
[30:00] Segment D: Titanic as pictures. Students follow cells A4-A6.
NARRATE THE HISTORY while plotting — the story is the engine.
A4: 891 passengers in the raw file; the cell prints that only the 712 rows with
COMPLETE info teach the model. 10-second beat: "real data has holes — we keep the complete rows."
-->

---

# Data as Pictures 

![bar chart: survival counts](../../assets/survival_counts.png)

*Always look at your data before doing anything with it.*

<!--
[RUN cell A5] More died than survived — 424 vs 288 of the 712 complete rows.
RULE (course-wide): every dataset gets PLOTTED before MODELED.
-->

---
<!-- _class: wow -->

# Survival by Sex & Class 

![survival by sex and class](../../assets/survival_by_sex_class.png)

**~75% of women lived. Only ~20% of men did.**

<!--
[RUN cell A6] THE PUNCHLINE PLOTS. Let students read the bars first.
ASK: "Which feature matters for survival?" — gender, then class.
SAY: "A rich woman in 1912 had close to a survival ticket."
-->

---

<!-- _class: hook -->

# THE MOMENT

Train an AI in 3 lines

![art](../../assets/magic_lines.png)

*Type with me. Really — open the notebook and type.*

<!--
[40:00] Segment E — emotional peak. Students TYPE ALONG cells A7-A9 (not just watch).
A7: X and y separated — "line 0 is setup, not magic."
CEREMONY before fit(): "On three, everyone say LEARN."
-->

---
<!-- _class: codespot wow -->

# The 3 Magic Lines 

```python
model = DecisionTreeClassifier(max_depth=3) # 1. pick a student ← this IS the model
model.fit(X, y) # 2. let it study
model.predict(new_passengers) # 3. ask it questions
```

**create → fit → predict**

*This rhythm is ALL of ML. Not just today.*

<!--
[RUN cell A8, students typing] Write the 3 lines LARGE on the board.
create = pick a student; fit = let it study; predict = ask, label hidden.
SAY: "Every model you'll ever meet follows these three lines."
-->

---

# What It Learned

![decision tree](../../assets/decision_tree.png)

**It's just questions. You could draw this.**

<!--
[RUN cell A9] Predict for a volunteer: "Would Sara, 2nd class, age 13, survive?"
Tree picture: "Your fruit map from 15 minutes ago? Same shape — the machine drew its own."
Who chose the questions? The machine did — cliffhanger for Session 2.
-->

---
<!-- _class: dark -->

# One Last Thing

The model is **not a brain**.

It found question-patterns matching survival.

**That's already amazing enough.**

<!--
Slow, quiet, honest moment.
SAY: "A mirror of 712 examples. Good data, good mirror. Unfair data, unfair mirror."
Then snap energy back up for the quiz.
-->

---
<!-- _class: quiz -->

![band](shared_band.png)

# Today You Learned 

- Rules → answers, or answers → **rules**
- **Features** (clues) & **labels** (answers)
- **Supervised** learning = examples with answers
- 3 magic lines: **create → fit → predict**

<!--
[50:00] CONSOLIDATION — cold call, friendly. One question per student:
get+produce? feature/label? 3 magic lines? why women survived?
If anyone stumbles on Q1-3, re-explain NOW.
-->

---

# Your Ship Tonight

Your first ML notebook → **your GitHub repo**

**"Would I have survived the Titanic?"** — an app you built

<!--
[55:00] THE SHIP + handout. Explain the loop OUT LOUD:
4 problems tonight (20-30 min) = next session we solve them TOGETHER from YOUR attempts.
Judge: python judge/run.py s01_notebook.ipynb
-->

---
<!-- _class: handout -->

# At-Home Problems (4)

1. **B1** The Feature Detective
2. **B2** Build Your Own Dataset
3. **B3** The 3 Magic Lines on YOUR animals
4. **B4** The Survival Predictor

`python judge/run.py s01_notebook.ipynb` ← instant score, anytime

<!--
One sentence of story per problem:
B1 dumb features under scrutiny; B2 invent your own dataset; B3 magic lines on YOUR data; B4 the 12-year-old boy verdict.
Deadline: before the problem-solving session. ~20-30 min total. First judge run is all-red — that's normal.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Next Time

## We solve YOUR problems — live.

**Bring your attempts. Bring your bugs.**

*They are the fuel of the next session.*

![rocket](shared_closing.png)

<!--
[60:00 — end on time] "Tonight your repo goes live. Show your family: I built an AI today."
CLIFFHANGER: "Who chose the tree's questions? Next time: you fix the machine's mistakes."
AFTER CLASS (48h): fill the retro note in the session README.
-->
