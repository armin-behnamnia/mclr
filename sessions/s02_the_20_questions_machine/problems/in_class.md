# Session 2 — In-Class Problems (problem-solving hour)

*Solved together, instructor with the class — after the at-home set is fully solved. Discussion problems, not silent work.*

## C1 — The Surprise Zoo (10 min)

Cell C1 runs the depth-2 tree on five animals it has never seen: rabbit, fox, hamster, sparrow, lion.

**The game:** before running, every student writes their predicted verdict for each animal. Run. Score yourself.

**Discussion:**
- Which verdicts are defensible? (lion → big dog: fine — it IS big; fox → cat: it's small with short ears)
- Which verdict is the funniest failure? (rabbit → small dog)
- For each failure: WHICH question let us down? Trace the path out loud, door by door.

**The point:** a tree can only sort newcomers into rooms it built. The rooms came from 11 animals that were all cats or dogs — nothing else ever existed for this tree.

## C2 — Tree Surgery (15 min)

The rabbit's verdict is wrong. Two surgeries are attempted in cell C2:
1. **More questions** — `max_depth=5` (a jungle of finer questions)
2. **More examples** — four extra small dogs added to the training table

**Run it.** The rabbit stays a small dog in every version.

**Discussion:**
- Why can't more depth fix it? (the second question about ear length separates cats from small dogs — the rabbit has cat-weight and dog-ears; every split on these two numbers sends it to the same side as the poodle)
- Why can't more examples fix it? (the extra dogs only move WHERE the fence goes, not WHAT the fence measures)
- So what WOULD fix it? (a question about something we never measured — "does it hop? does it bark?" — the tree can only ask about numbers in its table)

**The point (honest ML):** when the features can't separate two things, no amount of tree-growing saves you. The fix is a better question — WHICH question the machine picks and how, is exactly the next session.

## C3 — Paper Tree vs Machine Tree (10 min)

Students fetch their hand-drawn trees (from the lab, or redraw from memory).

**Discussion:**
- Was your first question `weight ≥ 14` (the machine's)? If not — did your tree still work?
- How many DIFFERENT valid first-questions can this table have? (any threshold between 6 and 22 that separates cats from big dogs works: 7, 8, 10, 14, 20...)
- So how many valid trees exist for 11 animals? (many — the machine picks ONE of them by a rule; which rule is the next session's story)

**The point:** there is no single correct tree. "Who picks the questions" is a real design decision — next session you become the picker.
