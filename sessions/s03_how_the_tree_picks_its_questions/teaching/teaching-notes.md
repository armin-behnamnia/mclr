# Session 3 — Full Teaching Notes (comprehensive per-slide guide)

*The complete instructor guideline: what to say, what to run, what to expect, on every slide. The slide decks carry only short cue-card notes; THIS document is the full teaching script. Rendered to `slides_teaching_notes.pdf` (one page per slide).*

---

## Course context

- **Session 3 of 32.** 60 min teaching + 60 min problem-solving (separate meeting).
- **Goal (student language):** "By the end of today, YOU will be able to explain why one question is better than another."
- **Before class — verify all of this:**
  - notebook `s03_notebook.ipynb` runs top-to-bottom (PART 0 demo cell is the hook's machine beat)
  - three grab bags prepared: Bag 1 = 8 blue balls; Bag 2 = 4 blue + 4 red; Bag 3 = 3 blue + 3 red + 2 green (or colored magnets + two drawn boxes)
  - slide assets exist in `assets/`
  - the judge passes on the solution notebook (3/3)
- **Session timing map:** hook 0–5 · sortedness 5–15 · surprise 15–25 · the ranking game 25–35 · Titanic 35–45 · you-be-the-machine 45–50 · quiz 50–55 · handout 55–60.
- **Board plan:** the hook's two boxes stay drawn ALL session (Segment A names purity on them); vocabulary column on the right (purity, entropy, information gain — never erased); the grab-bag ratings (0, 1, 1.56) stay visible; the score card from Segment C stays up so Segment D's Titanic leaderboard lands under it, same shape.
- **The session's big move:** S2 ended on a mystery (WHO chose `weight ≥ 14`?). Today the class plays the machine's game by hand, then watches the machine play it — and the mystery dissolves into arithmetic.

---

## Slide 1 — Title: درخت چطور سؤالش را انتخاب می‌کند؟ (lead)

Welcome them back as a show that keeps revealing its tricks.

**Say:** "Last time you drew trees by hand and the machine's tree asked `weight ≥ 14`. Today you find out where that question CAME from — and by the end, you'll be the one who can explain it."

**Do:** notebook open at PART 0; grab bags within reach but hidden; board clean except the top half (the hook needs it).

---

## Slide 2 — دو جعبه، یک سؤال (hook, beat 1)

**[0:00] The two boxes.** Draw (or place) Box A: 4 blue + 4 red mixed. Box B: 8 blue.

**Say:** "The goal of today's whole game: get every box to be ONE color. Quick — which box needs help, and which one is already done?"

**Expect:** instant answers. "Box B is done" — that intuition IS purity; you are 40 minutes from naming it.

**Do NOT** say "sorted" or "pure" yet. Experience first, name later.

---

## Slide 3 — کدام سؤال بهتر مرتب می‌کند؟ (hook, beat 2)

**The vote.** A new box: 2 blue + 2 red (mixed big/small). Three candidate questions on the slide: "is it red?", "is it big?", "is it round?". Hands up for each.

**Say:** "One question. Two doors. Which question gets this box to one color per side?"

**Expect:** "is it red?" wins obviously — good. Some will ask why we're voting on something so easy. Answer: "Because the machine has to vote on MILLIONS of these — and it can't go by gut."

**Keep the votes on the board.** The losing questions return on slide 6.

---

## Slide 4 — ماشین به سؤال‌هایش نمره می‌دهد (hook, beat 3)

**[RUN: PART 0 demo cell]** — the leaderboard: every candidate question on the 11 animals with its score; `weight ≥ 14` on top.

**Say:** "Last session I promised you'd learn why 14. Here it is: the machine SHOPS. It tries every question on the menu, scores each one, and the champion gets asked. Same game you just played — with a number on it."

**Expect:** "It tried ALL the questions?!" — yes. The S2 mystery is answered in front of them.

**Fallback if the cell fails:** slide 13 carries the leaderboard picture — narrate from it. Never skip the story.

---

## Slide 5 — خلوص (Purity) (definition)

**[5:00] Segment A. NAME slide** — the experience (two boxes + the vote) already happened.

**Do:** point at Box A and Box B on the board while reading: the good question leaves each side as one thing; the useless question cuts without sorting.

**Write on the board (vocabulary column, never erased):** خلوص (Purity) = how close a box is to ONE thing per room.

**[MISCONCEPTION]:** "a good question splits the data evenly" — NO. Splitting evenly is easy and worthless; SORTING is the goal. A question can halve the box and leave both sides as mixed as before (slide 6 shows exactly this).

**CHECK (cold call):** "The elephant's side of our S2 tree — the `weight ≥ 14 → yes` corridor — was it mixed or pure?" (Pure — all big dogs. THAT's why the tree stopped asking after one question. S2's asymmetry mystery gets its answer right here.)

---

## Slide 6 — سؤالِ بیهوده (wow)

**SHOW** the useless question: `ear ≥ 4.5` → left: 1 cat · right: 10 animals, all three groups.

**Say:** "The box got CUT — one animal on one side, ten on the other. Did anything get SORTED? Look at the balls: both sides are exactly as mixed as before. We drew a line inside the mess."

**Point back at the slide-3 votes:** "the 'is it round?' votes — this is them, in the machine's world."

---

## Slide 7 — سؤالِ قهرمان (wow)

**SHOW** the champion: `weight ≥ 14` → left: 7 animals (4 cats + 3 small dogs) · right: 4 big dogs, PURE.

**Say:** "Same box, same two doors — but THIS question sorted. The yes-side is one thing: big dogs, pure, done. The no-side is still mixed — and that's exactly why the tree asks a SECOND question there (slide 14: you will pick it yourselves)."

**Do:** trace the champion with your finger, door by door. Let the difference between slides 6 and 7 sink in — this difference is what the machine measures.

---

## Slide 8 — مرتب شد یا نه؟ (quiz)

**USE-IT (2 min).** Before commenting: the class votes on `weight ≥ 30` (no: 9 mixed animals · yes: 2 big dogs) — sorted, or just cut?

**Answer:** PARTIALLY sorted — the yes-side is pure (2 big dogs), the no-side stays mixed. A real question, just not the champion: its gain is 0.32 against 0.95.

**Why this slide exists:** "partially sorted" is the honest middle — most real questions live there. Purity is a scale, not a yes/no.

---

## Slide 9 — کیسه‌های غافلگیری (hook — the grab-bag game)

**[15:00] Segment B. THE GAME (3 min, high energy).** Three paper bags: 8 blue · 4 blue + 4 red · 3 blue + 3 red + 2 green. A volunteer draws ONE ball blind from each. Before each draw, the class SHOUTS its prediction. After each draw, everyone rates their surprise with fingers: 0, 1, or 2.

**Expect:** Bag 1 = zero surprise (you know it's blue). Bag 3 = maximum surprise. The class just invented the ranking: pure = 0, mixed = big.

**Energy note:** play it fast and loud. This beat carries the whole concept.

---

## Slide 10 — غافلگیری (آنتروپی) (definition)

**NAME slide.** Write the three bags' numbers on the board: 0, 1, 1.56. (From counting colors — no formula today.)

**Say:** "That feeling you rated with fingers — the machine needs it as a NUMBER. Here it is: pure box = 0, the even red/blue mix = 1, the three-color bag = 1.56. The messier the box, the bigger the number."

**[MISCONCEPTION]:** entropy is NOT the machine thinking. It is a number from counting colors. Nothing thinks anywhere — this is the LEAST magical part of the whole course, and saying so plainly increases trust.

**[RUN: cell A2]** — the machine prints the same three numbers next to the color counts. Check them together against the finger-ratings: same ranking.

---

## Slide 11 — جعبهٔ ۱۱ حیوان: چند؟ (quiz)

**USE-IT (cell A2b).** The 11-animal box: 4 cats, 4 big dogs, 3 small dogs. The class predicts the surprise level — "middle?" — then runs.

**Answer:** 1.57 — nearly the three-color bag. Same kind of mix: three things, none dominating.

**Say:** "Every box has its number now. And a question's quality is just... how much it LOWERS that number. Which brings us to the game."

---

## Slide 12 — بازی: تو امتیاز بده (hook — EXPERIENCE first)

**[25:00] Segment C. THE GAME (5 min, teams of two).** No vocabulary on this slide — the class plays first.
Candidate questions on the 11 animals (in `content.md` Segment C): `weight ≥ 14`, `weight ≥ 3.25`, `ear ≥ 8.25`, `ear ≥ 4.5` — each with its two doors written out on the board.
Teams compute the score card (mess before − mess after); first team with the right champion shouts.

**Result:** a TIE — `weight ≥ 14` and `ear ≥ 8.25` both drop 1.57 → 0.63 (gain 0.95). The "even splits" barely move the surprise (1.43 after).

**Why the tie is gold:** both champions do the same amount of sorting. The machine breaks the tie mechanically — first column measured wins (weight). Honest and boring — say so.

---

## Slide 13 — نمرهٔ سؤال: بهرهٔ اطلاعاتی (definition — NAME after play)

**[~32:00] NAME slide — AFTER the game, never before.** What the teams just computed by hand is called بهرهٔ اطلاعاتی (Information Gain): غافلگیریِ قبل منهای غافلگیریِ بعد — weighted by how many animals land on each side. Champion = biggest gain.

**[MISCONCEPTION]:** the champion is NOT the purest side — it is the biggest surprise-drop for the WHOLE box. Point BACK to the bad question (slide 6): its «no» door was perfectly pure yet scored only 0.14, because it held one animal. Corrected sentence, with the class: "a good question makes BIG groups purer."

---

## Slide 14 — جدول امتیازها (wow)

**[RUN: cell A3]** — the machine's leaderboard, sorted, champion on top — the same ranking the class computed by hand.

**Say:** "You played its game. It plays this game on EVERY node of EVERY tree — millions of times per tree. There is no committee, no committee meeting. Just this table."

**Point at the tie:** "Both champions gain 0.95. The machine keeps the first one it measured — weight is column one. Boring. Honest. Arithmetic."

---

## Slide 15 — راند دوم: جعبهٔ سبک (quiz)

**USE-IT (cell A3b).** The light box: 7 animals (4 cats + 3 small dogs), surprise 0.99. The class predicts the champion BEFORE running.

**Answer:** `ear ≥ 8.25` — takes the box to ZERO surprise (4 cats | 3 small dogs, both sides pure).

**The payoff moment:** "That is the SECOND question of Session 2's tree. You just derived it yourselves — the machine's tree was never magic; it was this game, played twice."

---

## Slide 16 — ماشین این بازی را روی تایتانیک هم می‌کند (hook)

**[35:00] Segment D — THE MOMENT.** Students code along cells A4–A5 (typing, not watching).

**[RUN: cell A4]** — the Titanic box: 712 passengers, 288 survived, 424 did not. Surprise: 0.97.

**Say:** "Session 1's data, back on screen. A very mixed box — barely better than a coin flip. If you were the machine, where would you start sorting?"

---

## Slide 17 — قهرمانِ تایتانیک (wow)

**[RUN: cell A5]** — the leaderboard: `is_female` 0.214 · `pclass` 0.083 · `fare` 0.069 · `age` 0.018.

**SHOW** the before/after boxes: men (453 passengers, 21% survived) and women (259 passengers, 75% survived) — both far more one-color than the full box.

**THE CALLBACK (say it warmly):** "Session 1, I had you VOTE on which feature matters for survival. Most of you said gender. You beat the machine to it — it just put a NUMBER on your vote: 0.21, triple the runner-up."

**[MISCONCEPTION] (one sentence only):** the gain number means gender SORTS the passengers — it does not mean gender CAUSED survival. Causes are a different door (Session 9 opens it properly). Do not open it now.

---

## Slide 18 — کلِ راز (codespot)

**[45:00] Segment E — you be the machine.**

**[RUN: cell A6]** — the whole secret in plain Python: loop over every question, compute the gain, take the max. Then the same call on the light box. The S2 tree's two questions come out.

**REBUILD the S2 tree on the board, as a class:** root box → champion (`weight ≥ 14`) → light box still mixed → shop again → `ear ≥ 8.25`. Ninety seconds, door by door, from nothing but the score card.

**HONEST BEAT (say it plainly):** "The machine doesn't think. It measures and takes the max — like a scale weighing fruit. When two questions tie, it keeps the first one it measured. No cleverness anywhere. And still — this is the engine inside every tree you'll ever train. THAT is the surprise: how far simple arithmetic goes."

---

## Slide 19 — انتخابِ سؤال، کارِ ماست (dark)

**The C2 rabbit returns.** In Session 2's problem hour, no amount of depth or extra examples fixed the rabbit — because the fix was a question about something never measured.

**Say:** "The machine only shops among the table's columns. 'Does it hop?' is never asked — it isn't a column. WE choose what goes on the menu; the machine picks from it. Feature choice is a human job — and when we feed garbage, the champion of garbage is still garbage. (That story has its own session: Session 7.)"

**Energy note:** this slide is deliberately slow and serious — one minute, then back up for the quiz.

---

## Slide 20 — امروز یاد گرفتی (quiz)

**[50:00] CONSOLIDATION — cold call, one question per student:**

1. What does a "good" question do? (raises purity — leaves each side mostly one thing)
2. What is entropy, in kid words? (the surprise level of a box — 0 when pure)
3. How does the machine score a question? (surprise before − after; biggest drop wins)
4. Why did the machine pick `weight ≥ 14` for the animals? (biggest gain: 1.57 → 0.63)
5. What won on Titanic? (is_female — the class's own S1 vote, with a number on it)

If anyone stumbles on Q1–3, re-explain NOW, not at home.

---

## Slide 21 — تحویل امشب + تمرین‌های خانه (handout)


**[55:00] THE SHIP + at-home handout in one slide.** The Ship is the annotated Titanic split plot — cell B3's leaderboard + before/after boxes, in their own hand, committed tonight. The slide shows the Ship art AND the live judge command.

**Explain the loop OUT LOUD:** 3 problems tonight (20–30 min); the next session opens by solving them TOGETHER from their attempts. First judge run is all-red — that is normal; say it.

**The judge command is visible on the slide:** `python judge/run.py s03_notebook.ipynb`

One sentence of story per problem:
- **B1** — the three bags get their numbers (0, 1, 0.47)
- **B2** — derive the light box champion (you did it in class — now alone)
- **B3** — Titanic's leaderboard + the annotated plot (the Ship)

Deadline: before the problem-solving session.

---


## Slide 22 — جلسهٔ بعد (lead, cliffhanger)

**[60:00 — end on time.]**

**Cliffhanger (verbatim):** "Today the machine picked its questions by measuring surprise — on the animals it has SEEN. But here is a trap: what if a question is only 'good' on the passengers it studied? A student who memorizes every exam answer looks brilliant — until the new exam. Tomorrow: you catch the machine fooling itself."

**After class (48h):** fill the retro note in the session README.
