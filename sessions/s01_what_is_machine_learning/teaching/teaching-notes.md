# Session 1 — Full Teaching Notes (comprehensive per-slide guide)

*The complete instructor guideline: what to say, what to run, what to expect, on every slide. The slide decks carry only short cue-card notes; THIS document is the full teaching script. Rendered to `slides_teaching_notes.pdf` (one page per slide).*

---

## Course context

- **Session 1 of 32.** 60 min teaching + 60 min problem-solving (separate meeting).
- **Goal (student language):** "By the end of today, YOU will be able to train a working ML model and show it to your family."
- **Before class — verify all of this:**
  - notebook `s01_notebook.ipynb` runs top-to-bottom (Colab or Jupyter)
  - PART 0 demo cells 1–3 work (the whole hook depends on them)
  - slide assets exist in `assets/`
  - the judge passes on the solution notebook
- **Session timing map:** hook 0–5 · big question 5–10 · fruit game 10–20 · supervised 20–30 · Titanic 30–40 · magic lines 40–50 · quiz 50–55 · handout 55–60.
- **Board plan (draw at the start, keep ALL session):** two boxes — `data + RULES → answers` / `data + answers → RULES` — plus a right-column vocabulary wall (feature, label, example) and, from Segment E, the 3 magic lines written large in the center.

---

## Slide 1 — Title: یادگیری ماشین چیست؟ (lead)

The first minute sets the tone for the whole course. Welcome them like a show is about to start, because it is.

**Say:** "This is session one of thirty-two. Today — in one hour — you will train a real AI. Not watch me do it. YOU will."

**Do:** have the notebook open in another tab, PART 0 ready. Check the room: projector visible from every seat, sound works (not needed today, but set the habit).

**Expect:** excitement mixed with disbelief. The disbelief is your fuel — you will resolve it at slide 20.

---

## Slide 2 — نمایش ویژهٔ هوش مصنوعی (hook)

[0:00–5:00] THE HOOK. One demo, three beats: the table → the line → the quiz. Run the single PART 0 demo cell from the notebook, with maximum showmanship. Dim the lights if possible.

**Say:** "By the end of today, you will build what you are about to see."

**How to run:** open the notebook, PART 0, run the demo cell once. The output carries the whole story: 8-row table → scatter plot with the red dashed line → verdicts on 4 unseen animals. Narrate between beats in under 15 seconds.

**Fallback if environment fails:** narrate from the demo description while showing slides 3–5; if the cell errors, re-run once, then move on. NEVER skip the hook — it is the fuel for the whole session.

---

## Slide 3 — بازیِ حیوانات: جدول (hook)

**[RUN: PART 0 demo cell, beat 1]** — the machine's entire world: 8 animals, each with two numbers (weight, ear length) and a label (cat/dog).

**Say:** "This table is ALL the machine gets. Eight rows. Nobody wrote a single rule."

**Expect:** "So what? It's just a table." — perfect. Let them underestimate it. The next beat exists to punish that.

---

## Slide 4 — بازیِ حیوانات: خطِ ماشین (hook)

**[RUN: PART 0 demo cell, beat 3 — the scatter plot]** — from those 8 rows, the machine drew a red dashed line: cats behind it, dogs in front.

**Say:** "No human drew this line. The machine found it hiding in those 8 rows."

**Expect:** "Where did the line come from?!" — let it hang. Slide 9 (Way 2) answers it: examples in, rules out.

**Do NOT explain yet.** Mystery first, explanation later — the reveal is worth more than the minutes.

---

## Slide 5 — بازیِ حیوانات: امتحان (hook)

**[RUN: PART 0 demo cell, beat 4]** — verdicts on animals the machine has NEVER seen:
- گرگ (35 kg) → سگ. Correct.
- گربهٔ همسایه (7 kg) → گربه. Correct.
- فیل (3000 kg) → سگ. The machine only knows two words — let the class laugh.

**Say:** "The machine didn't memorize. It learned one question from 8 examples and guesses beyond them. Sometimes it guesses wrong — Session 2 is about fixing exactly that."

**Closing line (memorize):** "One idea behind everything you just saw. You'll know it in 30 minutes, and you'll build your own before you leave today."

---

## Slide 6 — سؤال بزرگ (6)

[5:00–10:00] Segment A — rules vs learning. **Draw the two boxes on the board as you talk; they stay there ALL session.**

Frame the question: "How do you make a computer smart?" Two answers exist in history. The interaction on slide 8 is the core of this segment — do not lecture through it.

---

## Slide 7 — راه اول: نوشتن قاعده‌ها

**Board: box 1.** `data + RULES → answers`

**Say:** "For 50 years this was the only way. Smart people wrote thousands of IF-THEN rules. It worked... until it didn't."

**Transition:** "Let's try it ourselves. Cats. Easy, right?"

---

## Slide 8 — مشکل نوشتن قاعده (interaction)

**INTERACTION (3–4 min):** students propose cat-recognition rules; YOU counter each with a counterexample:
- "has fur" → hairless cat
- "has whiskers" → walrus
- "small and cute" → corgi puppy
- "meows" → cat in a costume / silent cat

**After 3–4 rounds, concede:** "And that's just CATS. Now imagine handwriting, or spam, or 'will this passenger survive'. This is why we don't write rules. We show examples."

**Energy note:** play the counterexamples for laughs — the absurdity IS the argument.

---

## Slide 9 — راه دوم: یادگیری ماشین

**Board: box 2, directly under box 1.** `data + answers → RULES`

Point at it silently for two seconds. Let it land.

**Check question (cold call):** "In ML, what does the machine get, and what does it produce?" — expected: *examples with answers → rules*.

These two boxes stay on the board all session; you will point back at them at least 5 times (slides 12, 14, 17, 20, 21).

---

## Slide 10 — AI در برابر ML (definition)

[~7:00] 60 seconds, no more.

**[MISCONCEPTION] Students think AI and ML are synonyms.** They are not:
- AI = the dream (machines acting smart) — "becoming a doctor"
- ML = the main way to get there (learning from data) — "medical school"

**Transition:** "To talk about examples, we need vocabulary. Game time."

---

## Slide 11 — بازی میوه (game)

[10:00–20:00] Segment B — features & labels.

**PLAY (2 min, high energy):** cover the fruit column, read the clues aloud, class shouts the label.

**[RUN: notebook cell A1]** — the same table as a DataFrame: "Pictures and data are the same thing."

**Then flip it (slide 13):** which clue is MOST useful? Vote.

This game is the foundation of Session 2 (decision trees as 20-questions) — plant it well.

---

## Slide 12 — واژگان جدید (definition)

**Write on the board (right column, never erased):** ویژگی (feature), برچسب (label), نمونه (example).

Memory hooks:
- feature = "fingerprint of the thing"
- label = "the answer we want"
- example = "one solved exercise"

**[MISCONCEPTION]** The label is NOT part of what the model reads at quiz time — it is what we HIDE. "The model studies with the answers. Then we take the answers away and quiz it."

**Check question:** "For predicting Titanic survival — name 3 possible features and the label." (features: class, sex, age, fare...; label: survived)

---

## Slide 13 — کدام ویژگی مهم است؟ (vote)

**INTERACTION:** hands-up vote per feature, quick debate.

**Say:** "Congratulations, you just did data science. In Session 9 we'll compute the answer instead of voting — with a number called feature importance."

**[RUN: cell A2]** — students record their own guess; these guesses are revisited in Session 9 (say so — it creates a long-term thread).

**Timing check:** it should now be ~20:00.

---

## Slide 14 — یادگیری نظارت‌شده

[20:00–30:00] Segment C — one paradigm today only (unsupervised = 30-second teaser, nothing more).

**LIVE MINI-GAME:** show 4 solved fruit examples, then a 5th with the label hidden — class predicts.

**Say:** "You just did supervised learning. Personally. Your brain is a very good one."

**[RUN: cell A3]** — the "hide the label" mechanic: study table vs quiz table, side by side.

---

## Slide 15 — چرا «نظارت‌شده»؟ (definition)

**[MISCONCEPTION]** "Supervised" does NOT mean a person watches the model learn. It means the training data comes with answer labels — like a teacher's answer key.

The absurdity of the word choice usually gets a laugh — use it.

**Optional 30-second teaser (do NOT go deeper):** "There's also UNSUPERVISED learning — finding patterns with no answers. Session 18."

**Check question:** "Why do we say 'supervised'?" — the examples come with answers.

---

## Slide 16 — تایتانیک

[30:00–40:00] Segment D — Titanic as PICTURES, not tables. Students follow along in notebook cells A4–A6.

**Narrate the history while plotting** — iceberg, lifeboats for only half, "women and children first". The story is the engagement engine; the plots are the evidence.

**[RUN: cell A4]** — read the CSV, `df.head()`: "891 passengers. Each row is a life."

**[MISCONCEPTION]** the model reads only the columns we give it. Whatever we don't give does not exist for the model.

---

## Slide 17 — داده به‌صورت عکس

**[RUN: cell A5]** — survival counts bar chart.

**Say:** "More died than survived — 549 vs 342. Remember this imbalance; it becomes a whole lesson in Session 9."

**Course-wide rule, stated here for the first time:** every dataset gets PLOTTED before it gets MODELED. Students will hear this ~100 times by Session 32.

---

## Slide 18 — بقا بر حسب جنسیت و کلاس

**[RUN: cell A6]** — the two punchline plots. **Let students read the bars themselves before you speak.**

**Ask:** "Which feature seems to matter for survival?" — sex, then class.

**Say:** "Being a rich woman in 1912 was close to a survival ticket. A machine trained on this data will learn exactly what these pictures show — no more, no less."

This foreshadows the fairness discussions (Session 9) — do not open that door yet, just leave the sentence standing.

---

## Slide 19 — لحظهٔ جادویی (codespot)

[40:00–50:00] Segment E — **the emotional peak of Session 1.** Slow down.

**CRITICAL: students TYPE ALONG in cells A7–A9.** Do not just demo on the projector — typing it themselves is what makes it THEIRS.

**[RUN: cell A7]** — X and y separated: "Line 0 is not magic, just setup: clues here, answers there."

**Ceremony before running fit():** "On the count of three, everyone say LEARN. One, two, three — LEARN." (Run it. It takes under a second.) "It just studied 891 lives in under a second."

---

## Slide 20 — سه خط جادویی (codespot wow)

**[RUN: cell A8, students typing]** — write the three lines LARGE on the board (center); they stay there.

1. `create` = pick a student (an empty brain, ready to learn)
2. `fit` = let it study (the supervised part: X are the clues, y the answers)
3. `predict` = ask it questions (label hidden!)

**Say:** "Every model you will ever meet — spam filters, face recognition, ChatGPT's ancestors — follows these three lines. That's the whole secret."

---

## Slide 21 — چه چیزی یاد گرفت

**[RUN: cell A9]** — predict for a volunteer from the class: "Sara, 2nd class, 13 years old, fare 30 — would Sara have survived?" Personal = memorable.

Then show the tree picture: **"This picture IS the rules it found. No magic — just yes/no questions. You could have drawn this yourself. Who chose these questions? Not us. The machine picked them."**

That last question is the cliffhanger seed for Session 2.

---

## Slide 22 — یک حرف آخر (focus)

This slide is deliberately slow and quiet — the one honest, serious moment of the session.

**Say:** "I want you to be impressed by what we did AND clear-eyed about what it is. A mirror of 714 examples. When the data is good, the mirror is good. When the data is unfair — the mirror is unfair. We'll come back to that."

Then snap the energy back up for the quiz.

---

## Slide 23 — امروز یاد گرفتی (quiz)

[50:00–55:00] CONSOLIDATION — oral quiz, cold call, FRIENDLY. One question per random student:

1. What does the machine get, and what does it produce? (*examples+answers → rules*)
2. What's a feature? A label? (*clue / answer*)
3. The 3 magic lines? (*create, fit, predict*)
4. Why did women survive more? (*learned from real examples*)

**If anyone stumbles on Q1–3, re-explain NOW, not at home** — this is the safety net before the at-home problems.

---

## Slide 24 — تحویل امشب (handout)

[55:00–60:00] THE SHIP + at-home handout. Project `problems/at_home.md`.

**Explain the loop OUT LOUD (the course's core ritual):**
1. NOW: you get 4 at-home problems (notebook PART B)
2. TONIGHT: you try them — 20–30 minutes
3. NEXT SESSION (problem-solving hour): we solve them TOGETHER, live, starting from YOUR attempts
4. The judge grades you anytime: `python judge/run.py s01_notebook.ipynb`

**Emphasize:** attempts beat solutions. A wrong attempt we fix together is worth more than a copied answer.

---

## Slide 25 — تمرین‌های خانه (handout)

One sentence of story per problem (details live in `at_home.md` — do not read it all aloud):

- **B1:** "A friend picked dumb features for predicting test-passing. Which ones survive your scrutiny?"
- **B2:** "Build a dataset of 4+ animals. Yes, invent it — that's what dataset creation is."
- **B3:** "The 3 magic lines — on YOUR OWN dataset this time."
- **B4:** "3rd-class, 12-year-old boy, fare 7.5. Does he live? The machine is waiting for your verdict."

**Deadline: before the problem-solving session.**

---

## Slide 26 — جلسهٔ بعد (closing)

[60:00 — end exactly on time]

**Final words:** "Tonight your repo goes live. First commit of your ML career. Show your family: 'I built an AI today' — because you did."

**CLIFFHANGER:** "Your tree asks questions — but WHO chose the questions? Next time: you catch the machine making dumb mistakes, and you become the one who fixes it."

**After class (within 48h):** fill the retro note at the bottom of the session README — what confused students, what dragged, what delighted. The Session 2 author reads it.
