# Session 2 — Teaching Session Content

*Content layer (presentation-neutral). Decks are generated from this file; edit here, then regenerate — never hand-patch decks for content changes.*

## Session goal
- **Syllabus:** nodes, branches, leaves; splits partition data; visualize trees with `plot_tree`; build a tree on paper to classify animals and test classmates' trees on surprise examples.
- **Student language:** "By the end of today, YOU will be able to read, draw, and hand-build a decision tree."

## Analogy map (this session)

| Concept | Analogy | Where it honestly breaks (later teaching moment) |
|---|---|---|
| Decision tree | the 20-questions game — questions narrow down the answer | a game player can jump anywhere; a tree always asks the SAME questions in the same order, and cannot change its mind mid-game (surfaced this session, Segment C) |
| Node (گره) | a fork in the road with a signpost | a real fork has two roads; a node's "roads" only exist after the question is fixed — and a tree never returns to a fork it passed (surfaced this session) |
| Leaf (برگ) | the final room the game ends in — the verdict | a leaf always says the same answer no matter which animal arrives there; it cannot look at anything else (surfaced when the elephant lands in the dog room) |
| Split / partition | a fence that separates the animals into two pens | a fence is permanent and one-directional: animals on the wrong side of a bad fence stay wrong — only a NEW fence fixes it (surfaced this session, Segment D) |
| max_depth | a limit on how many questions you may ask | a real player stops when they are sure; a tree stops because we TOLD it to — it has no judgment of its own (surfaced in Block 2 when depth vs overfitting returns) |

One analogy per concept, reused across the whole course — no ad-hoc metaphors in decks or narration. The tree = 20-questions analogy continues for the whole course (S3: who picks the questions; S8+: forests = many players voting).

## Ship showcase plan (capability picture)

The Ship is the student's **hand-drawn decision tree** (paper, photographed, committed to the repo) — built in the lab segment, battle-tested on classmates' surprise animals, with the funniest failure celebrated. The showcase moment: their paper tree next to the machine's `plot_tree` output — "you and the machine drew the same kind of thing; yours you can tape to the wall." The closing slide carries the capability picture (a hand-drawn tree on paper + "the tree is YOURS — on paper AND in code").

## Cliffhanger script (multi-session)

Final line, delivered after the at-home handout, pointing at Session 3 (How the Tree Picks Its Questions):
> "Your paper tree asked smart questions. But WHO taught the MACHINE to pick its questions? It read the same 11 animals and chose `weight ≥ 14` — not `ear ≥ 8.25`. Why that one? Next time: you become the question-picker."

---

## 1. Hook script — "20 Questions" (0:00–5:00)

**Form: J4 (you-be-the-model) — the class IS the algorithm before it is named.** Played live with the whole class, then instantly mirrored by the machine in the notebook. Zero-terminal rule: one PART 0 cell carries the machine's side.

| # | Beat | Script | Expected reaction |
|---|------|--------|-------------------|
| 1 | **The human game** — instructor thinks of an animal (a wolf); class asks only yes/no questions; count the questions aloud | "I'm thinking of an animal. You may only ask questions I can answer with yes or no. Let's count how many you need." | Shouting, rapid-fire questions; the counter on the board climbs |
| 2 | **The reveal** — the question path is drawn on the board as it happened: `heavier than 10 kg? → yes` → `has long ears? → no` → `wolf` | "Look at what you just did. You played a game of questions. Each answer sent you down a path. THIS SHAPE has a name — and the machine from last session plays exactly this game." | "Wait — last session's line was just ONE question!" |
| 3 | **The machine plays** — run the single PART 0 demo cell: same animals as Session 1 plus three small dogs; depth-1 tree still calls the puppy a cat; then a SECOND question (ear length) fixes it | "Last session the machine asked one question and got the puppy wrong. Watch what happens when it's allowed to ask TWO." | "It got the puppy right?!" — the Session 1 failure is redeemed |

Closing line (memorize this):
> "You have been playing decision trees your whole life. Today you learn to draw them — on paper and in code."

**Fallback if environment fails:** the human game (beats 1–2) needs nothing but a board; narrate beat 3 from the demo slide while showing the printed tree picture. Never skip the hook.

---

## 2. Segment-by-segment teaching script

### Segment A — The anatomy of a question tree (5:00–15:00)
- **One idea:** a decision tree is just nested yes/no questions: one question at a time, each answer opens two doors, and the game ends in a verdict.
- **Experience first:** the hook's board path is still on the board. Point at it and name its parts using the game the class JUST played — no new example needed.
- **Visual (slides: anatomy + tree pictures):** the wolf-question path drawn as a real tree: circles for questions, two arrows out of each, boxes for verdicts. Then the same picture with the vocabulary stamped on: node, branch, leaf.
- **Vocabulary (write on the board, keep for the whole course):**
  - **Node (گره)** = a question — a fork with a signpost
  - **Branch (شاخه)** = one answer's door (yes/no)
  - **Leaf (برگ)** = the final room — where the game ends and the verdict is said
- **Notebook cell A1:** the class's own game replayed in code — the same 11 animals, the machine's ONE question (weight ≥ 14) shown as a depth-1 tree picture. "Last session's red line and this picture are the SAME thing."
- **Use-it step:** the elephant quiz slide — AFTER the depth-2 tree picture is shown (the quiz needs the picture; showing it earlier spoils the reveal): the class traces the elephant door by door and discovers it answers only ONE question.
- **Misconception to pre-empt:** *"the tree thinks/changes its questions based on the answer."* No — the whole path is fixed in advance; every animal walks the same corridors. A tree cannot change its mind mid-game.
- **Check question:** "Point at the nodes, the branches, and the leaves in this tree. How many leaves does a 2-question tree have, at most?" (4)

### Segment B — Reading the machine's tree (15:00–25:00)
- **One idea:** `plot_tree` shows the machine's exact question path — and we can read it like any picture.
- **Experience first (live coding, cells A2–A3):** train the depth-2 tree on the 11 animals (4 cats, 4 big dogs, 3 small dogs), show `plot_tree` — the class reads the questions aloud, door by door, for a wolf. Note the tree's honest asymmetry: the heavy side needed only ONE question (the big-dog room is right there), the light side needed a second one (ears) — the tree only asks a second question where animals are still mixed.
- **Visual:** the `plot_tree` output (real data visualization — never replaced by art).
- **Name now:** the machine's first question is called the **root (ریشه)** — the first fork every animal meets. "The machine chose `weight ≥ 14` — exactly the question YOU asked first in the game. Coincidence? No. We'll see why next session."
- **Use-it step (cell A3):** students predict, before running, which room the puppy ends in — then run and check. Then the elephant: it walks the same corridors and lands in the big-dog room — after just ONE question, because on the heavy side the big-dog room is already the very next door. "A leaf says ONE answer no matter what arrives. The elephant doesn't get a special room."
- **Misconception to pre-empt:** *"the tree can answer anything about the animal."* It only knows what its questions ask. The elephant's trunk never comes up — a tree can only ask about the features in its data.
- **Check question:** "Why does the puppy reach the right leaf in the depth-2 tree but not in the depth-1 one?" (the second question — ear length — separates it from cats) ... and "Why doesn't the WOLF get asked a second question?" (the heavy side is already pure — all big dogs — so the tree stops asking)

### Segment C — Trees in code: the depth knob (25:00–35:00)
- **One idea:** `max_depth` = how many questions the machine is allowed to ask. One question wasn't enough; more questions give finer verdicts.
- **Experience first (live coding, cells A4–A5):** retrain with `max_depth=1` (the puppy fails — Session 1's mistake), then `max_depth=2` (fixed). The two `plot_tree` pictures side by side. Then `max_depth=10` — the tree grows a jungle of questions. "More questions is not always better — but WHY is a story for later." (Plants Block-2 overfitting; do not teach it now.)
- **Name now:** **Depth (عمق)** = the longest path from root to leaf = the most questions any animal gets asked.
- **Use-it step (cell A5, the knob):** students change `max_depth` themselves and re-run; each finds the smallest depth that gets all 11 animals right (answer: 2). First one to find it shouts.
- **Misconception to pre-empt:** *"more depth = smarter."* More depth = more questions = finer splits, but the machine has no judgment about when to stop — WE turn the knob. (The honest full story arrives in Block 2.)
- **Check question:** "With max_depth=1, how many leaves? With 2? With 3, at most?" (2 / 4 / 8)

### Segment D — THE LAB: draw your own tree (35:00–50:00)
*The emotional core of the session — students become tree-builders on paper.*
- **One idea:** you can build a question tree by hand, and the machine's tree is built the same way — question by question, each one splitting the animals into two groups.
- **Setup:** every student gets the animal sheet (paper handout: the 11 animals as a table) and a blank page. Rule of the game: only yes/no questions about the table's numbers.
- **Play (10 min):** each student draws their own tree to sort the 11 animals into the 3 rooms (cat / big dog / small dog). Any tree that works, wins. Circulate; help stuck students with one hint: "which question would split the cats away from the dogs first?"
- **Battle (5 min):** pairs swap papers and test each other's trees on surprise animals from the notebook's cell C2 list (rabbit, fox, hamster, sparrow, lion — exactly those five). The tree's verdict is read door-by-door, out loud. **The funniest failure gets applause** — the elephant in the dog room, the hamster classified as a cat — and each failure is diagnosed: "WHICH question let you down?"
- **Connect to code (cell A6):** the machine's depth-2 tree next to a student's paper tree (photographed under the projector if the room allows). "Same game. Same shape. Yours is on paper; the machine's is in memory."
- **Ship:** students photograph their paper tree and commit it to their repo — `s02_tree.jpg` in their session-2 folder. The instructor shows the commit command.
- **Misconception to pre-empt:** *"there is ONE correct tree."* No — many different trees can sort the same animals correctly. (The machine picks its questions by a rule we learn next session; humans pick by intuition.)
- **Check question:** "Was your first question the same as the machine's (`weight ≥ 14`)? Why or why not?"

### Consolidation — oral quiz (50:00–55:00)
Ask these to random students (cold call, friendly):
1. What are the three parts of a tree? (node/question, branch/door, leaf/verdict-room)
2. Why did the depth-2 tree fix the puppy? (second question separates small dogs from cats)
3. What does `max_depth` mean? (how many questions the machine may ask)
4. Can two different trees both sort the 11 animals correctly? (yes — many valid trees)

### Segment E — At-home handout (55:00–60:00)
- Project `problems/at_home.md`.
- Walk through each problem's story in one sentence; make clear what to submit (notebook cells B1–B3) and how the judge grades.
- Announce the deadline: **before the next problem-solving session**.
- Show the judge command on screen: `python judge/run.py s02_notebook.ipynb`.
- State the Ship: "Tonight your paper tree goes into your repo. Photo + commit."
- **Cliffhanger** (last 30 seconds, per the cliffhanger script above): who taught the machine to pick `weight ≥ 14`? Next session — you become the question-picker.

---

## 3. Board/notes plan
- The hook's question path (wolf game) stays on the board ALL session — Segment A names its parts on this exact drawing.
- Vocabulary column on the right side of the board: node, branch, leaf, root, depth. Never erased.
- The question counter from the hook game stays visible (the class's record: how many questions they needed).
- From Segment C: the two `plot_tree` pictures (depth 1 vs depth 2) stay projected or printed side by side.

## 4. Post-session (within 48h) — retro note
- [ ] What confused students:
- [ ] What dragged:
- [ ] What delighted:
