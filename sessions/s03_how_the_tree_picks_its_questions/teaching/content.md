# Session 3 — Teaching Session Content

*Content layer (presentation-neutral). Decks are generated from this file; edit here, then regenerate — never hand-patch decks for content changes.*

## Session goal
- **Syllabus:** purity as "sorted-ness"; entropy as surprise (with a slot-machine visual); information gain. 5-minute split-ranking game, then verify instantly in code on a bigger dataset.
- **Student language:** "By the end of today, YOU will be able to explain why one question is better than another."

## Analogy map (this session)

| Concept | Analogy | Where it honestly breaks (later teaching moment) |
|---|---|---|
| Purity / sorted-ness (خلوص) | a box of balls after sorting — one color left per box | real data is never perfectly sortable; the last mixed box always stays a bit mixed (surfaced this session, Segment D — the cats' box is already pure, that's WHY the tree stopped asking) |
| Impurity / surprise (آنتروپی) | a mystery grab-bag: the more colors inside, the more SURPRISE when you pull one out blind | entropy is a number, not a feeling — and it is measured in "bits", which have nothing to do with fun (surfaced the moment the formula appears; we keep the formula out of today and stay with counting colors) |
| Information gain (بهرهٔ اطلاعاتی) | surprise REMOVED by a question — how much calmer the bags get | "gain" sounds like winning points; a question with big gain doesn't WIN anything, it just sorts better (surfaced in Segment D when a big gain still leaves a mixed box) |
| The machine's question choice | the machine plays the split-ranking game on EVERY possible question, and picks the champion — millions of times per tree | the machine doesn't "think" about which question is smart — it measures, like a scale, and takes the max; no cleverness, just arithmetic (surfaced this session, Segment E) |

One analogy per concept, reused across the whole course. The tree = 20-questions game continues (S2); today answers the question S2 ended on: WHO picks the questions. Balls-in-boxes is a NEW cast member — it returns in S8 (a forest = many boxes voters) and S18 (clustering = sorting balls with NO labels).

## Ship showcase plan (capability picture)

The Ship is the student's **annotated best-split plot** — the Titanic root question drawn as before/after boxes with the survival counts and the surprise numbers written on (notebook cell B3), committed to their repo. The showcase moment: their S1 vote ("which feature matters for survival?") returns as a MEASURED number — "back in Session 1 you voted; today your vote has a number on it, and you computed it yourself." The closing slide carries the capability picture (their annotated split plot + "you are now the question-picker").

## Cliffhanger script (multi-session)

Final line, delivered after the at-home handout, pointing at Session 4 (The Exam Cheat Test):
> "Today the machine picked its questions by measuring surprise. But here is a trap: what if a question is only 'good' on the animals it has already seen? Tomorrow: a student who memorizes every exam answer — and a machine that fools itself the same way. You'll learn to catch it."

---

## 1. Hook script — "Two Boxes, One Question" (0:00–5:00)

**Form: J2 (guess-the-rule) — the class ranks questions BEFORE any theory.** Played live with the whole class, then instantly mirrored by the machine in the notebook. Zero-terminal rule: one PART 0 cell carries the machine's side.

**Setup:** two big boxes drawn on the board (or two trays of colored magnets). Box A: 4 blue + 4 red balls mixed. Box B: 8 blue balls. "One question — one chance to split a box into two — and you want each side to end up ONE color. Which box do you choose to fix first?"

| # | Beat | Script | Expected reaction |
|---|------|--------|-------------------|
| 1 | **The two boxes** — Box A (4 blue + 4 red), Box B (8 blue, already one color) | "These are boxes of balls. Your goal: get every box to be ONE color. Which box needs help — and which is already done?" | "Box A is mixed, Box B is fine!" — they will say it instantly |
| 2 | **The question game** — offer the class THREE candidate questions for a NEW mixed box (2 blue + 2 red, all big/small mix): "is it red?", "is it big?", "is it round?" — the class votes on which question un-mixes best | "One question, two doors. Vote: which question sorts the balls best?" | Shouting and votes; "is it red?" obviously wins — half the class wonders why we even asked |
| 3 | **The machine's punchline** — run PART 0 demo cell: the machine plays the SAME game on the 11 animals, trying every question, and prints its ranking — `weight ≥ 14` wins with a number attached | "Last session the machine picked `weight ≥ 14` and I promised you'd learn WHY. Watch it shop for questions — and score them." | "It tried ALL the questions?!" — the mystery from S2 is answered |

Closing line (memorize this):
> "You just ranked questions by how well they SORT. The machine does exactly this — with a number. Today you learn its ruler."

**Fallback if environment fails:** the game (beats 1–2) needs nothing but the board; narrate beat 3 from the ranking slide while showing the printed table. Never skip the hook.

---

## 2. Segment-by-segment teaching script

### Segment A — Sorted-ness: some questions sort better (5:00–15:00)
- **One idea:** a good question leaves each side mostly ONE thing. That property — how sorted a box is — has a NAME, and the machine can MEASURE it.
- **Experience first:** the hook's votes are still on the board. Take the losing question ("is it big?") and walk it: 2 blue + 2 red on each side — the box got SPLIT but not SORTED. Walk the winner ("is it red?"): blue side all blue, red side all red. The class FEELS the difference before any word is given.
- **Visual (slides):** before/after box diagrams — question A (mixed→mixed) vs question B (mixed→two pure boxes). Then the same two pictures stamped with the vocabulary.
- **Vocabulary (write on the board, keep for the whole course):**
  - **Purity (خلوص)** = how close a box is to ONE color — one thing per room
  - **The goal of every question:** raise purity on BOTH sides
- **Notebook cell A1:** the class's game in code — the 11 animals, the machine prints each side of `weight ≥ 14` and each side of `ear ≥ 4.5` (a deliberately bad question): cats-and-small-dogs vs big dogs (sorted-ish) against a pure mix on both sides (useless). "Look at the two printouts. Which question sorted?"
- **Use-it step:** project a third question (`weight ≥ 30`) — class votes SORTED or NOT SORTED before running; check together. (It splits big dogs from everything else — partially sorted, one pure side.)
- **Misconception to pre-empt:** *"a split that halves the data is a good split."* No — splitting evenly is easy; sorting is the goal. A question can cut the box exactly in half and leave both sides as mixed as before.
- **Check question:** "The elephant's side of our tree — `weight ≥ 14 → yes` — was it mixed or pure?" (pure — all big dogs; that's exactly why the tree stopped asking. The S2 mystery of the one-question corridor gets its answer TODAY.)

### Segment B — Surprise: measuring mixed-ness with a number (15:00–25:00)
- **One idea:** "mixed" needs a NUMBER so the machine can compare questions. The number: how surprised you are drawing one ball blind.
- **Experience first (the grab-bag game, 3 min):** three paper bags on the teacher's desk — Bag 1: 8 blue. Bag 2: 4 blue + 4 red. Bag 3: 3 blue + 3 red + 2 green. A volunteer draws blind from each; before each draw the class SHOUTS its prediction; after each draw, rate the surprise 0–2 with fingers.
  - Bag 1: no surprise at all (you KNOW it's blue). Bag 3: maximum surprise. The class just invented the ranking: pure box = 0 surprise, mixed box = big surprise.
- **Visual:** the slot-machine / grab-bag picture — the more symbols on the wheel, the less you can predict, the bigger the surprise. (Slide art; the honest note: real entropy averages over many draws — our "surprise rating" is its cousin.)
- **Name now:** **Entropy (آنتروپی)** = the surprise level of a box — 0 for a pure box, bigger as the mix grows. On the board: the three bags get their numbers (0, 1, 1.56) — the numbers are computed BY COUNTING COLORS, not by the formula; the formula stays out of today.
- **Notebook cell A2:** the machine's ruler — `entropy` computed for the three bags and printed next to their color counts. The class checks the machine's numbers against their finger-ratings: same ranking.
- **Use-it step (cell A2b):** the 11 animals root box: 4 cats, 4 big dogs, 3 small dogs — the class predicts the surprise level ("middle?"), runs, checks (1.57 — nearly the same as the 3-color bag, because it's the same kind of mix: three things, none dominating).
- **Misconception to pre-empt:** *"entropy is how much the machine thinks."* No — it's just a number from counting colors in a box. Nothing thinks anywhere. (Say it plainly: this is the LEAST magical part of the whole course.)
- **Check question:** "Two boxes: one with 2 blue + 2 red, one with 1 blue + 3 red. Which has the bigger surprise number? Can you rank them without any formula?" (2+2 is more mixed than 1+3 — closer to an even split, less predictable.)

### Segment C — The game: rank the questions (25:00–35:00)
- **One idea:** a question's score = surprise BEFORE − surprise AFTER (averaged over the two sides). Best question = biggest drop. This is the split-ranking game the machine plays on every node.
- **Experience first (the 5-minute game, J2):** the 11 animals' box (surprise 1.57) is on the board. Four candidate questions, each written with its two doors and what lands on each side:
  1. `weight ≥ 14` → left: 4 cats + 3 small dogs · right: 4 big dogs (surprise after: 0.63)
  2. `weight ≥ 3.25` → left: 1 cat · right: everything else (surprise after: 1.43 — barely moved)
  3. `ear ≥ 8.25` → left: 4 cats · right: 3 small dogs + 4 big dogs (surprise after: 0.63 — **the class must trace this one by hand, door by door; it's sneaky**)
  4. `ear ≥ 4.5` → left: 1 cat · right: everything else (surprise after: 1.43)
  - Teams of two compute each question's score card: surprise before (1.57), surprise after, which question wins. **First team with the right champion shouts.**
  - Result: `weight ≥ 14` and `ear ≥ 8.25` TIE at the top (both drop 1.57 → 0.63, gain 0.95) — a tie the machine breaks mechanically (see Segment E). The losing "even splits" barely move the surprise. The tie itself is the teachable moment: both champions do the same amount of sorting.
- **Name now:** **Information gain (بهرهٔ اطلاعاتی)** = surprise removed by a question = before − after (weighted by how many animals land on each side). The champion question = the biggest gain.
- **Visual:** the score card as a table — question | left box | right box | surprise after | gain — with the champion row highlighted.
- **Notebook cell A3:** the machine's leaderboard — every candidate question with its gain, sorted; `weight ≥ 14` on top (its tie with `ear ≥ 8.25` printed side by side). "You played its game. It plays this game on EVERY node of EVERY tree — millions of times."
- **Use-it step (cell A3b):** run the leaderboard for the LIGHT side only (7 animals: 4 cats + 3 small dogs, surprise 0.99) — the class predicts the winner BEFORE running: `ear ≥ 8.25`, which takes the box to ZERO surprise (4 cats | 3 small dogs). The depth-2 tree's second question is derived live, from the game they just played.
- **Misconception to pre-empt:** *"the machine asks the question that sorts the MOST animals out."* No — it asks the question with the biggest surprise-drop. A question can move just ONE animal and win, if that one animal was the only mixed one.
- **Check question:** "Why did the machine pick `weight ≥ 14` and not `weight ≥ 20`?" (same sides, same gain — the corridor of valid thresholds from S2's C3 returns with a reason: every threshold between the heaviest cat and the lightest big dog sorts identically.)

### Segment D — THE MOMENT: the machine plays it on Titanic (35:00–45:00)
- **One idea:** the game generalizes: on Titanic, the machine plays the same question-shopping game and the class can predict the winner — because they already VOTED on it in Session 1.
- **Experience first (live coding, cells A4–A5, students code along):**
  - A4: the Titanic box (712 passengers, 288 survived / 424 did not — after dropping missing ages) — surprise number printed (0.97). "Is this box sorted? What's our surprise?"
  - A5: the leaderboard — every feature's best question with its gain: `is_female` wins by a landslide (gain 0.214 vs 0.083 for pclass, 0.069 for fare, 0.018 for age). "Now raise your hand if you voted 'gender matters most' in Session 1 — you beat the machine to it. It just put a NUMBER on your vote."
- **Visual:** the before/after boxes for `is_female`: mixed box (surprise 0.97) → men box (453 passengers, survival 21%) + women box (259 passengers, survival 75%) — with the S1 punchline plot recalled next to it.
- **Notebook cell A5 output is the anchor:** the leaderboard table, gains to 3 decimals, `is_female` highlighted.
- **Misconception to pre-empt:** *"the gain number means gender CAUSES survival."* No — the tree measures sorting, not causes. (One sentence only; the fairness door opens properly in Session 9. Do not open it now.)
- **Check question:** "The machine's first Titanic question — predict it before we run: which feature won the leaderboard?" (is_female — and their S1 vote predicted it.)

### Segment E — You be the machine (45:00–50:00)
- **One idea:** the whole mystery of S2 is now one sentence: the machine shops every question, scores each by surprise-drop, takes the champion — recursively.
- **Interaction:** replay the depth-2 animal tree's construction AS A CLASS on the board: root box → champion question (`weight ≥ 14`) → left box still mixed → shop again → `ear ≥ 8.25`. The tree from S2 is REBUILT by the class in 90 seconds using only the score card.
- **Honest beat (say it plainly):** the machine doesn't "think" — it measures and takes the max, like a scale weighing fruit. When `weight ≥ 14` and `ear ≥ 8.25` tie (both gain 0.95 on these animals), the tie-break is boring: it keeps whichever it measured first (weight is the first column). No cleverness — arithmetic. (This deflates the magic HONESTLY and sets up Block 2's "then why does it work so well?")
- **Notebook cell A6:** the full loop in 3 lines — `for` over questions, compute gain, take max — the machine's game written out as plain Python. "There is no line 4. That's the whole secret."
- **Misconception to pre-empt:** *"the machine considers smart questions we didn't list."* No — it only shops among the columns in the table. (C2 from S2's problem hour returns: the rabbit could only be fixed by a NEW FEATURE — a question about something never measured. Feature choice is OUR job; scoring is the machine's.)
- **Check question:** "Why can't the animal tree ever ask 'does it hop?'" (hopping is not a column — the machine only shops among the numbers it was given.)

### Consolidation — oral quiz (50:00–55:00)
Ask these to random students (cold call, friendly):
1. What does a "good" question do? (raises purity — leaves each side mostly one thing)
2. What is entropy, in kid words? (the surprise level of a box — 0 when pure)
3. How does the machine score a question? (surprise before − surprise after; biggest drop wins)
4. Why did the machine pick `weight ≥ 14` for the animals? (biggest gain: 1.57 → 0.63, the surprise drops by more than half)
5. What won on Titanic? (is_female — the same feature the class voted for in S1)

### Segment F — At-home handout (55:00–60:00)
- Project `problems/at_home.md`.
- Walk through each problem's story in one sentence; make clear what to submit (notebook cells B1–B3) and how the judge grades.
- Announce the deadline: **before the next problem-solving session**.
- Show the judge command on screen: `python judge/run.py s03_notebook.ipynb`.
- State the Ship: "Tonight your annotated best-split plot goes into your repo — the Titanic question, measured by YOU."
- **Cliffhanger** (last 30 seconds, per the cliffhanger script above): the machine scores its questions on the animals it has SEEN... what if it's fooling itself? Tomorrow: the exam cheat test.

---

## 3. Board/notes plan
- The two boxes from the hook (mixed vs pure) stay drawn on the board ALL session — Segment A names purity on this exact drawing.
- Vocabulary column on the right side of the board: purity, entropy, information gain. Never erased.
- The score card from Segment C's game stays up: question | sides | surprise after | gain — Segment D's Titanic leaderboard lands right under it, same shape.
- The grab-bag ratings (0, 1, 1.56) from Segment B stay visible next to the bags.

## 4. Post-session (within 48h) — retro note
- [ ] What confused students:
- [ ] What dragged:
- [ ] What delighted:
