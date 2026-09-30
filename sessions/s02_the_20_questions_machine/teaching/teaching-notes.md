# Session 2 — Full Teaching Notes (comprehensive per-slide guide)

*The complete instructor guideline: what to say, what to run, what to expect, on every slide. The slide decks carry only short cue-card notes; THIS document is the full teaching script. Rendered to `slides_teaching_notes.pdf` (one page per slide).*

---

## Course context

- **Session 2 of 32.** 60 min teaching + 60 min problem-solving (separate meeting).
- **Goal (student language):** "By the end of today, YOU will be able to read, draw, and hand-build a decision tree."
- **Before class — verify all of this:**
  - notebook `s02_notebook.ipynb` runs top-to-bottom (PART 0 demo cell is the hook's machine beat)
  - `assets/animals_table.pdf` printed — one copy per student (the paper lab depends on it)
  - blank paper for every student; pencils
  - the judge passes on the solution notebook (3/3)
- **Session timing map:** hook 0–5 · anatomy 5–15 · reading trees 15–25 · depth knob 25–35 · paper lab 35–50 · quiz 50–55 · handout 55–60.
- **Board plan:** the hook game's question path stays up ALL session (Segment A names its parts on it); vocabulary column on the right (node, branch, leaf, root, depth — never erased); the question counter from the game stays visible.

---

## Slide 1 — Title: ماشینِ ۲۰ سؤالی (lead)

Welcome them back like a show is about to continue, because it is.

**Say:** "Last time you watched a machine learn. Today you become the machine — and then you beat it at its own game, on paper."

**Do:** notebook open at PART 0; animals_table.pdf stack ready; check every student can see the board (the hook is a BOARD game, not a screen game).

---

## Slide 2 — بازیِ ۲۰ سؤالی (hook, beat 1)

**[0:00] The human game.** You think of a **wolf**. The class asks only yes/no questions. Count the questions on the board, aloud, in big numbers — the counter is a prop for slide 3.

**Rules to state:** any yes/no question about the animal; no letter-guessing (keep it in question form).

**Steer if needed:** if the class flails, hint with structure — "is it heavier than 10 kilos?" Good groups naturally ask weight and ear questions; both will be used later.

**When they get it:** do NOT clear the board. The question path drawn as it happened is slide 3's raw material.

**Fallback:** this beat needs nothing but a board. Never skip it.

---

## Slide 3 — شما همین الان یک درخت بودید (hook, beat 2)

**[~3:00] The reveal.** Redraw the game's path on the board as a proper diagram: circle for the first question, two arrows out, circle for the second, arrows into the verdict "گرگ".

**Say (verbatim):** "Every answer was a door. Every door opened a new path. You just walked a tree — a decision tree. And the machine from last session? It plays exactly this game. Its red line was ONE question. One circle, two doors."

**Expect:** "Wait — the red line was a question?!" — that connection is the whole point. Let a STUDENT say it if possible.

---

## Slide 4 — حالا ماشین بازی کند (hook, beat 3)

**[RUN: PART 0 demo cell]** — one cell, both trees side by side: depth 1 (the puppy → گربه, last session's failure) and depth 2 (puppy → سگ کوچک, fixed).

**Say:** "Last session the machine was allowed ONE question and got the puppy wrong. Watch what happens when it's allowed TWO."

**Expect:** "It fixed it?!" Then close the hook: **"You've been playing decision trees your whole life. Today you learn to draw them — on paper and in code."**

**Fallback if the cell fails:** slides 7 and 10 carry the same tree pictures — narrate from them. Never skip the hook's story.

---

## Slide 5 — کالبدشکافی درخت (definition)

**[5:00] Segment A.** The NAME slide — the experience (the game) already happened, so this lands warm.

**Do:** point at the BOARD path while reading each definition — node = question circle, branch = arrow door, leaf = verdict room. The slide's vocabulary must be written into the board's vocabulary column and never erased.

**[MISCONCEPTION]:** the tree does NOT think or adapt mid-game. The whole path is fixed in advance; every animal walks the same corridors. Say it explicitly: "A tree cannot change its mind. The wolf and the elephant walk the same hallways."

**CHECK (cold call):** "How many leaves can a 2-question tree have, at most?" (4 — 2×2. This tree has 3.)

---

## Slide 6 — فیل کدام در را می‌گذرد؟ (quiz)

**INTERACTION (2 min).** The elephant (3000 kg, ears 20): the class shouts the door at each node on the projected depth-2 tree.

**Trace:** `وزن ≥ ۱۴؟` yes → dog corridor. `گوش ≥ ۸.۲۵؟` yes → big-dog room.

**Say:** "The elephant walks the same corridors as everyone. A leaf says ONE word for whatever reaches it — even a 3-ton elephant gets called a big dog. The tree has no other room for it."

---

## Slide 7 — ماشینِ جلسهٔ ۱ = یک سؤال

**[RUN: notebook cell A1]** — the depth-1 tree picture. Visually identical mechanic to last session's red line.

**Say:** "Last session's line and this picture are the SAME thing — a single question with two doors. Only the drawing changed."

**Why this slide exists:** it seals the continuity. Session 1's model was a tree all along; today they learn its language.

---

## Slide 8 — ریشه: اولین سؤال (definition)

**[15:00] Segment B.** NAME: **ریشه (root)** — the first fork every animal meets.

**[RUN: notebook cell A2]** — the depth-2 `plot_tree`. Read the two questions aloud together, door by door, for a wolf: weight ≥ 14? yes → ear ≥ 8.25? no → big dog.

**Interaction:** compare with the class's own first questions from the hook game. Most asked weight first too — but with different thresholds (7, 10, 20). Park that observation: "the machine picked exactly 14. Why 14 and not 7? Next session." (This is the cliffhanger's seed — plant it here, water it at the end.)

---

## Slide 9 — دو سؤال، سه اتاق (wow)

**The punchline picture** — real `plot_tree` output; never replaced by art (its authenticity is part of the lesson).

**Say:** "One question split light from heavy. The second question split cats from small dogs. Three rooms, all 11 animals correctly sorted."

**ASK before running cell A3:** "Which room does the puppy reach now?" — they already know from PART 0; let them say it out loud for the satisfaction.

---

## Slide 10 — مسیر را بخوان: توله‌سگ (quiz)

**[RUN: notebook cell A3]** — visitors: wolf, puppy, elephant. Students trace each path BEFORE the machine answers.

**Trace the puppy:** `وزن ≥ ۱۴؟` no → light corridor. `گوش ≥ ۸.۲۵؟` yes → small-dog room. Correct!

**Say:** "The second question — ears — is what separates small dogs from cats. Last session's mistake had a cure: one more question."

**USE-IT landed here:** every student has now traced a path and predicted before checking. That is "reading a tree."

---

## Slide 11 — پیچِ عمق (definition)

**[25:00] Segment C.** NAME: **عمق (depth)** — the longest question path. `max_depth` = the knob that limits it.

**[RUN: notebook cell A4]** — depth 1 vs depth 2 comparison with accuracy printed: 73% → 100%.

**[MISCONCEPTION]:** more depth is NOT automatically smarter. The machine has no judgment about when to stop — WE turn the knob. The honest full story (overfitting) arrives in Block 2; do not teach it now, but do not lie about it either — "more questions is not always better; WHY is a story for later" is the exact scripted line.

**CHECK:** "Depth 1: how many leaves? Depth 2? Depth 3, at most?" (2 / 4 / 8)

---

## Slide 12 — دستت را روی پیچ بگذار (codespot)

**[RUN: notebook cell A5 — students change the number THEMSELVES and re-run]**

**The race:** first student to find the smallest perfect depth (2) shouts it. Then run `max_depth=10` together — the tree becomes an unreadable jungle; let them laugh at it.

**Say:** "More questions, finer rooms — but would YOU trust a tree that asks 10 questions about 11 animals? Hold that feeling. Block 2 will name it."

---

## Slide 13 — آزمایشگاه: درختِ خودت را بکش (hook — the Lab)

**[35:00] THE LAB — this session's Ship.** Hand out `animals_table.pdf` + blank paper.

**Rules (state exactly):** only yes/no questions about the table's two numbers (weight, ear length). Goal: every animal reaches the right room (cat / big dog / small dog). Any tree that works, wins.

**Circulate.** Stuck student hint: "which question would split the cats away from the dogs first?"

**Timing:** ~10 minutes drawing. Do not rush this — it is the emotional core of the session.

**[MISCONCEPTION] (say it during circulation):** there is no single correct tree. Two students with different first thresholds both have valid trees.

---

## Slide 14 — نبردِ درخت‌ها (quiz)

**[~45:00] The battle.** Pairs swap papers. Test each other's trees on the surprise zoo: rabbit, fox, hamster, sparrow, lion (the cell C1 list — read them out).

**Protocol:** verdicts read door-by-door, out loud. **The funniest failure gets applause** (a sparrow called a cat; a rabbit called a small dog). Each failure is diagnosed with one question: "WHICH question let you down?"

**Verified verdicts to expect (depth-2 machine tree):** rabbit → سگ کوچک, fox → گربه, hamster → گربه, sparrow → گربه, lion → سگ بزرگ. Student trees will vary — that's the point.

---

## Slide 15 — درختِ تو = درختِ ماشین (dark)

**[~48:00] Connect.** [RUN: notebook cell A6] — the machine's depth-2 tree. If the room allows, photograph one student's paper tree and project it next to the machine's.

**Say:** "Same game. Same shape. Yours is on paper; the machine's is in memory. And yours — you can tape it to a wall."

**Ship logistics (show on screen):** photo the tree → `s02_tree.jpg` → commit to their repo tonight.

---

## Slide 16 — امروز یاد گرفتی (quiz)

**[50:00] CONSOLIDATION — cold call, one question per student:**
1. Parts of a tree? (node/question, branch/door, leaf/room)
2. Why did depth-2 fix the puppy? (the ear question separates small dogs from cats)
3. What is max_depth? (the most questions the machine may ask)
4. Can two different trees both be correct? (yes — many valid trees)

If anyone stumbles on Q1–3, re-explain NOW, not at home.

---

## Slide 17 — تحویل امشب (handout)

**[55:00]** The Ship + the loop, said OUT LOUD: photo of the paper tree committed tonight; three small notebook problems (20–30 min); next session opens by solving them TOGETHER from their attempts.

**Show the judge command:** `python judge/run.py s02_notebook.ipynb`

---

## Slide 18 — تمرین‌های خانه (handout)

One sentence of story per problem:
- **B1** — count the tree's questions and rooms (reading a tree's shape)
- **B2** — which room does the elephant reach? (tracing a path)
- **B3** — the smallest perfect depth (the knob, measured)

Deadline: before the problem-solving session.

---

## Slide 19 — جلسهٔ بعد (lead, cliffhanger)

**[60:00 — end on time.]**

**Cliffhanger (verbatim):** "Your paper tree asked smart questions. But WHO taught the MACHINE to pick its questions? It read the same 11 animals and chose `weight ≥ 14` — not 7, not 20. Why that one? Next time: you become the question-picker."

**After class (48h):** fill the retro note in the session README.
