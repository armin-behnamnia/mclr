# Session 1 — Teaching Session Content

*Content layer (presentation-neutral). Decks are generated from this file; edit here, then regenerate — never hand-patch decks for content changes.*

## Session goal
- **Syllabus:** rules vs learning from examples; features & labels; supervised learning; Titanic as pictures; train a tree in 3 lines.
- **Student language:** "By the end of today, YOU will be able to train a working ML model and show it to your family."

## Analogy map (this session)

| Concept | Analogy | Where it honestly breaks (later teaching moment) |
|---|---|---|
| Model / training | a student studying solved examples with an answer key | a student gets tired; a model can read millions of examples — and a model never "understands" what it studies (surfaced in Session 1 Segment E and again in Block 2) |
| Features / labels | clues and the answer in a guessing game | in real datasets nobody hands you tidy "clues" — feature *engineering* is work (surfaced in Session 2) |
| Supervised learning | studying with the teacher's answer key, then the exam with answers hidden | no teacher "watches" the model — the word is historical (surfaced the moment it is introduced) |
| The trained tree | the red line the machine drew in the animal game | the line looks like magic but is just one learned question — no magic at all (surfaced at the end of this session) |
| The model's limits | a mirror of its 712 examples — good data, good mirror; unfair data, unfair mirror | a mirror is passive; the model also GUESSES beyond its examples (the puppy) — that guessing is the point and the danger (S1 closer, then S4 overfitting) |

One analogy per concept, reused across the whole course — no ad-hoc metaphors in decks or narration.

## Ship showcase plan (capability picture)

The Ship is the student's own Titanic survival model (trained in class in cells A7–A9, then re-trained solo in at-home cell B4) plus their first portfolio commit. The showcase moment: the hook's animal game returns in Segment E as *the same thing they just built* — "the red line from the start of class? fit() drew it. You just did that yourself, on real data." The closing slide carries the capability picture (magic-lines art + "the model is YOURS tonight").

## Cliffhanger script (multi-session)

Final line, delivered after the at-home handout, pointing at Session 2:
> "Your tree asks questions — but WHO chose the questions? Next time: you catch the machine making dumb mistakes, and you become the one who fixes it."

---

## 1. Hook script — "The Animal Game" (0:00–5:00)

Run the single PART 0 demo cell (zero-terminal rule — no scripts, no terminal), with maximum showmanship. Dim the lights if possible. One cell, four beats — the cell prints a «——— مرحلهٔ N · … ———» marker before each beat, and slide/notes references use those exact markers.

| # | Beat (printed marker) | Script | Expected reaction |
|---|------|--------|-------------------|
| 1 | **The table** («مرحلهٔ ۱ · جدول») — the machine's entire world: 8 animals, two numbers each (weight, ear length) + a label (cat/dog) | "This table is ALL the machine gets. Eight rows. Nobody wrote a single rule." | "So what? It's just a table." — let them underestimate it |
| 2 | **The silent fit** («مرحلهٔ ۲» — one line of code, nothing prints) | "Watch: it just studied. That's it. That's the whole spell." | "Wait — that was it?" |
| 3 | **The line** («مرحلهٔ ۳ · خطِ ماشین») — the scatter plot: the machine's own red dashed line, cats behind, dogs in front | "No human drew this line. The machine found it hiding in those 8 rows." | "Where did the line come from?!" — let it hang until slide 9 |
| 4 | **The quiz + the reveal** («مرحلهٔ ۴ · امتحان») — verdicts on animals it has NEVER seen: wolf→dog (right), neighbor's cat→cat (right), puppy→cat (WRONG — a 2 kg dog!), elephant→dog (it only knows two words); the cell then prints the reveal: the whole secret is ONE question, «وزن ⁦≤ ۱۴⁩ کیلوگرم؟» | "The line is a guess from 8 examples. Near the line, the guess breaks. And the whole machine is one question — HOW it picked that question is Session 3's mystery." | Laughter at the elephant + "Why did it get the puppy wrong?!" |

Closing line (memorize this): 
> "One idea behind everything you just saw. You'll know it in 30 minutes, and you'll build your own before you leave today."

**Fallback if environment fails:** narrate from the demo descriptions above while showing the relevant slide; if a cell errors, re-run it once, then move on. Never skip the hook — it is the fuel for the whole session.

---

## 2. Segment-by-segment teaching script

### Segment A — The Big Question: rules vs learning (5:00–10:00)
- **One idea:** traditional programming = humans write the rules; machine learning = the machine finds the rules from examples.
- **Visual:** the two-box diagram (slides 2–3): 
  - Traditional: `data + rules → answers`
  - ML: `data + answers → rules`
- **On the board:** draw both boxes live, arrow by arrow, while narrating.
- **Interaction:** "How would YOU write rules to recognize a cat? Try." Let students propose rules; counter each with a counterexample (hairless cat, cat in a costume, big dog that's small...). After 3–4 rounds: "This is why we don't write rules. We show examples."
- **Misconception to pre-empt:** *"AI and ML are the same thing."* — AI is the big dream (machines acting smart); ML is the main modern way of getting there (learning from data). Say this explicitly.
- **Check question:** "In ML, what does the machine get, and what does it produce?" (data + answers → rules)

### Segment B — Features & labels: the fruit game (10:00–20:00)
- **One idea:** every ML example is described by **features** (the clues) and a **label** (the answer).
- **Interactive game** (slides 4–6 + notebook cells A1–A2): 
  1. Project the fruit table (5 fruits × 3 features: color, size, texture).
  2. Play "guess the fruit": read features aloud, class shouts the label.
  3. Then flip it: "Which ONE feature is most useful? Which is useless?" — vote, discuss. This is their first taste of *feature importance*, planted 8 sessions before we name it.
  4. **Chain the guesses into a decision map (slides 14–15):** the class lines its own questions up — "red? → apple · not red, long? → banana · else grapes" — first drawn on the board together, then shown as the tidy fruit decision map. This is the decision tree met INTUITIVELY, by hand, with zero code; the NAME is deliberately withheld until Session 2, and Segment E's callback ("your fruit map? the machine drew its own") turns `DecisionTreeClassifier` into "the machine's version of what we did by hand."
- **Visual:** the fruit table colorized (slides), then the same table as a pandas DataFrame in cell A1 so students connect "pictures" and "data".
- **Vocabulary (write on the board, keep for the whole course):**
  - **Feature** = a clue (a column)
  - **Label** = the answer (the column we want to predict)
  - **Example** = one row = one set of clues + its answer
- **Misconception to pre-empt:** students often think the label is "part of the data the model reads". No — the label is what we *hide* from the model at test time. Tease this: "The model studies with the answers. Then we take the answers away and quiz it."
- **Check question:** "For predicting Titanic survival, name 3 possible features and the label."

### Segment C — Supervised learning: studying with the answer key (20:00–30:00)
- **One idea:** supervised learning = learning from examples that include the answers. (Just this one paradigm today; unsupervised gets a 30-second teaser slide, nothing more.)
- **Visual:** slide 8 — the classroom analogy: a student studying solved examples (features + labels), then facing a new exam (features only). 
- **Interaction:** show 4 solved fruit examples, then a 5th with the label hidden — class predicts. "You just did supervised learning. Personally."
- **Notebook cell A3:** the "hide the label" mechanic in code — DataFrame with and without the answer column shown side by side.
- **Misconception to pre-empt:** "supervised" does NOT mean a human watches the model. It means the *data* contains the answers. (The word choice is historical — students find this funny, use the laugh.)
- **Check question:** "Why do we say 'supervised'?" (examples come with answers / a teacher's answer key)

### Segment D — Titanic as pictures, not tables (30:00–40:00)
- **One idea:** before any modeling, you *look* at data. Data has shape, color, and stories.
- **Live coding** (students follow along in notebook cells A4–A6):
  - A4: read the CSV, `df.head()` — "891 passengers in the raw file, each a row, each row a life"; the cell prints that only the 712 rows with complete info teach the model (10-second "real data has holes" beat).
  - A5: survival counts as a bar chart — "more died than survived: 424 vs 288; the model must fight this imbalance."
  - A6: survival by `sex` and by `pclass` — the two punchline plots: "being a woman in 1st class ≈ survival ticket". 
- **Narrate the history while plotting** — the Titanic story carries this segment; the plots are the evidence.
- **Misconception to pre-empt:** "the model reads names/tickets." — it only sees the columns we give it. Whatever we don't give, does not exist for the model.
- **Check question:** "From these pictures, which feature seems to matter for survival?"

### Segment E — THE MOMENT: train an AI in 3 lines (40:00–50:00)
This is the emotional peak of the session. Slow down. Make students type with you.
- **One idea:** training = giving the machine solved examples so it finds the rules.
- **Live coding** (notebook cells A7–A9, students code along):
  ```python
  model = DecisionTreeClassifier(max_depth=3)   # line 1: pick a student
  model.fit(X, y)                               # line 2: let it study
  model.predict(new_passengers)                 # line 3: ask it questions
  ```
- Before running `fit`: class ceremony — "on the count of three, everyone say LEARN. ... That took less than a second. It studied 712 lives in less than a second."
- Run predictions on a few invented passengers (rich woman 1st class vs poor man 3rd class) and show the tree picture (cell A9, `plot_tree`) — "this picture IS the rules it found. You could have drawn this yourself. It's just questions."
- **Misconception to pre-empt:** the model is NOT a brain and does not "understand" Titanic, history, or death. It found question-patterns that match survival. Say it plainly; it increases trust rather than killing wonder.
- **Check question:** "What are the 3 lines doing, in your own words?"

### Consolidation — oral quiz (50:00–55:00)
Ask these to random students (cold call, friendly):
1. What does an ML model get as input, and what does it learn? (features+labels → rules)
2. What is a feature? A label? (clue / answer)
3. What are the 3 magic lines? (create, fit, predict)
4. Why did our model predict women survived more? (it learned from real examples)

### Segment F — At-home handout (55:00–60:00)
- Project `problems/at_home.md`.
- Walk through each problem's story in one sentence; make clear what to submit (notebook cells B1–B4) and how the judge grades.
- Announce the deadline: **before the next problem-solving session**.
- Show the judge command on screen: `python judge/run.py s01_notebook.ipynb`.
- State the Ship: "Tonight your repo goes live. First commit of your ML career."
- **Cliffhanger** (last 30 seconds, per the cliffhanger script above): who chose the tree's questions? Next session — you fix the machine's dumb mistakes.

---

## 3. Board/notes plan
- Keep the two-box diagram (`rules → answers` vs `answers → rules`) on the board for the ENTIRE session — point back to it in every segment.
- Vocabulary column on the right side of the board: feature, label, example, train, predict, model. Never erased.
- The 3 magic lines get written large in the center when Segment E starts, and stay up.

## 4. Post-session (within 48h) — retro note
- [ ] What confused students:
- [ ] What dragged:
- [ ] What delighted:
