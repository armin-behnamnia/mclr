# Session 2 — In-Class Solutions (discussion guide)

## C1 — The Surprise Zoo

**Actual verdicts (verified by running cell C1):**

| Animal | (weight, ear) | Tree verdict | Fair? |
|---|---|---|---|
| خرگوش rabbit | (2, 10) | سگ کوچک (small dog) | the famous failure — cat-weight, dog-ears |
| روباه fox | (8, 4) | گربه (cat) | defensible: small, short ears |
| همستر hamster | (0.5, 3) | گربه (cat) | defensible-but-funny: the smallest "cat" ever |
| گنجشک sparrow | (0.03, 2) | گربه (cat) | the class laughs: a 30-gram "cat" |
| شیر lion | (160, 20) | سگ بزرگ (big dog) | defensible: heavy, long ears |

**Where the discussion should land:** every verdict is the room the animal's two numbers walk into. The tree never saw a rabbit, a sparrow, or a lion — its rooms were built from 11 cats-and-dogs only. Trace each failure path aloud: which question sent the animal the wrong way? (For ALL of them: the first question — weight — is doing the sorting; ear length only separates the light side.)

## C2 — Tree Surgery

**Actual verdicts (verified):** with `max_depth=5` AND with 4 extra small dogs, the rabbit still lands in سگ کوچک. No verdict in the zoo changes at all.

**Why depth doesn't fix it:** deeper trees add MORE questions, but every question is still about the same two numbers. The rabbit (2, 10) and the poodle (4, 11) are nearly identical in this feature space — any fence on weight or ear length that keeps the poodle with the small dogs keeps the rabbit there too.

**Why more examples don't fix it:** the extra dogs only move WHERE the fences sit (threshold 14 → 15.5, ear 8.25 → 7.5), not WHAT the fences measure.

**The closing insight (write on board):** the fix is a question about something we never measured — "does it hop? does it bark?" — i.e., a NEW FEATURE. The tree can only ask about columns in its table. Who decides which questions are available — and which one the machine picks — is Session 3.

## C3 — Paper Tree vs Machine Tree

**Discussion outcomes to steer toward:**
- Most students' first question will also be about weight (it's the visually dominant clue) — but their threshold may be 7, 10, or 20, not the machine's 14. All of those trees WORK.
- Any first question whose threshold lies between the heaviest cat (6 kg) and the lightest big dog (22 kg) separates cats from big dogs. That's a wide corridor of valid choices — infinitely many valid trees.
- So "the machine's tree" is one tree among many. The interesting question — what RULE makes the machine pick `weight ≥ 14` (and ear ≥ 8.25) — is exactly Session 3's opener. (For the instructor's own curiosity: the machine picks the question that makes the two sides purest — the gini/entropy story — but do NOT teach this now.)
