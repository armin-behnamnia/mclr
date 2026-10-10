# Session Creation Guide — ML Course

**Purpose:** This is the single rulebook for creating any session of the course. Every session, without exception, must be built by following this document end-to-end. If a session violates any rule here, it is not finished.

**Companion doc:** `curriculum.md` (the syllabus — the source of truth for *what* each session must deliver).

**Pedagogy layer:** this course follows the **junior-tutor** skill (`/home/pardis_ai/skills/junior-tutor/SKILL.md`), which extends the slide-craft skill. Junior-tutor's laws apply on top of everything below: (1) learn without pain, (2) instructor effortlessness, (3) student intrigue. Its EXPERIENCE → NAME → USE pattern (§3.1), analogy-map discipline (§3.1), misconception alerts (§3.2), J-format demos (§3), and Layer J verification (`/home/pardis_ai/skills/junior-tutor/assets/scripts/verify_junior.sh`) are mandatory for every session. Where this guide is more specific (course theme, judge, two-hour structure), this guide wins; where junior-tutor is more specific (kid-word budgets, demo formats, pedagogy checks), junior-tutor wins.

**Content/presentation separation (the build contract):** `curriculum.md` + each session's `teaching/content.md` are the **user-owned content layer** — all wording, examples, analogies, story beats, problems. Decks (`teaching/slides/`) are **generated artifacts** of that layer, exactly like the PDFs and PPTX built from them. Sessions are always built content-first: content slice approved → presentation generated → verified. When content changes (edited here or supplied from anywhere else), decks are **regenerated** from content (see §14) — never hand-patched into divergence.

---

## 1. Golden Rules (non-negotiable)

0. **No emojis in any student- or instructor-facing content** — slides, notebooks, problems, judge messages, docs. Emojis in text are a strong tell of AI-generated content. Visual personality comes from the theme, layout, and generated illustrations instead — never from emoji characters. (The terminal dots `● ● ●` on code blocks are part of the macOS-window visual metaphor and are allowed.)

1. **Goal fidelity:** The session must deliver the exact goal defined for it in `curriculum.md` — nothing more, nothing less. No bonus topics, no "while we're at it" tangents. If a prerequisite is missing, it becomes a 5-minute recap, not a new lesson.
2. **Two-hour structure:** Every session = 60 min Teaching + 60 min Problem-Solving, delivered as two separate actual meetings.
3. **At-home problem loop (the core loop of the course):**
 - At-home problems are **created and assigned during the teaching session** (handed out at its end, committed to the session folder).
 - The problem-solving session **opens by solving these exact problems with highest priority**, live, before anything else. Students' at-home attempts are the fuel of the problem-solving hour.
 - Only after the at-home problems are fully solved may the problem-solving session continue with any additional in-class problems.
4. **One goal, one Ship:** the session has exactly one stated goal in student language ("By the end of today, YOU will be able to ___") and produces exactly one portfolio artifact (the Ship).
5. **Hook first:** the teaching session opens with a 5-minute hook (wow-demo, game, or challenge) *before* any theory. No exceptions.
6. **The 15-minute rule:** no continuous lecture segment longer than 15 minutes without a visual, interaction, poll, or live demo.
7. **Visual-first:** every dataset is plotted before it is modeled; every model behavior (tree, boundary, curve, embedding) is drawn or animated. If a concept cannot be visualized, it must be re-explained until it can.
7b. **EXPERIENCE → NAME → USE (junior-tutor §3.1):** no concept is named before it is felt. Every new term arrives as a game/demo/story first, gets its «فارسی (English Term)» name only after the experience, and is used immediately (a guess, a vote, a line of code). Definitions end paragraphs; they never start them.
7c. **One analogy per concept (junior-tutor analogy map):** every concept teaches through ONE consistent concrete analogy, recorded in the session's `teaching/content.md` and reused across the whole course (e.g., the fortune teller = the trained model). The analogy's honest breaking point is recorded too and surfaced in a later session as a teaching moment. No ad-hoc metaphors.
8. **Notebook-driven:** the single session notebook is partially taught in the teaching session and partially worked in the problem-solving session (split defined in §4).
9. **Everything in the folder:** if it isn't in the session folder, it doesn't exist. Slides, notebook, demos, solutions, and the judge are all committed before the teaching session is delivered.
10. **Tested before taught:** every demo, notebook cell, and judge test must be executed end-to-end by the session creator *before* delivery. A live demo that fails is worse than no demo.

---

## 2. Session Folder Structure (mandatory)

```
sessions/
└── s07_garbage_in_garbage_out/          # sNN + short snake_case name from syllabus
    ├── README.md                        # session card (§3) — the entry point
    ├── teaching/
    │   ├── content.md                   # full teaching session content/script (§5)
    │   └── slides/                      # Marp slides (see §9 for the full rules)
    │       ├── slides.md                # source — Persian, RTL, course theme, presenter notes
    │       ├── slides_en.md             # English simple version of the same deck
    │       ├── slides.pdf               # rendered Persian student deck (clean)
    │       ├── slides_en.pdf            # rendered English student deck
    │       ├── slides_with_notes.pdf    # rendered instructor deck (notes as PDF annotations)
    │       ├── slides.pptx              # EDITABLE PowerPoint — Persian, real text, RTL
    │       ├── build_pptx.py            # builds slides.pptx from slides.md (python-pptx)
    │       ├── render.sh                # renders ALL decks (copies font + shared art, finds Chrome)
    │       ├── preview.sh               # live preview server for instant edit-see workflow (copy of slide-theme/preview.sh)
    │       └── Vazirmatn.ttf            # copied automatically by render.sh (do not edit)
    ├── notebook/
    │   ├── build_notebooks.py           # regenerates both notebooks deterministically
    │   ├── s07_notebook.ipynb           # THE session notebook (student-facing, partially guided)
    │   └── s07_notebook_solution.ipynb  # fully filled version (instructor-only, not handed out)
    ├── demos/                           # self-contained HTML demos only (see §10); most demos live in PART 0 of the notebook
    ├── problems/
    │   ├── at_home.md                   # at-home problems (assigned at end of teaching session)
    │   ├── in_class.md                  # additional in-class problems for problem-solving hour
    │   └── solutions/
    │       ├── at_home_solution.md      # worked solutions with reasoning, not just answers
    │       └── in_class_solution.md
    ├── judge/
    │   ├── tests/                       # autograder tests (pytest or nbgrader-style)
    │   ├── data/                        # hidden test fixtures the judge needs
    │   └── README.md                    # how to run the judge, grading rubric, points
    └── assets/                          # generated art, datasets, session images
        └── images-manifest.md           # prompt + seed + size for every generated image
```

Rules:
- **Naming:** `sNN_snake_case_name` derived from the syllabus session title. Consistent numbering, zero gaps.
- The student receives: `README.md`, `notebook/s07_notebook.ipynb`, `problems/at_home.md`, and the judge runner. **Never** the solutions folder or solution notebook.
- `demos/` and `assets/` are separate: demos are *executable wow-moments*, assets are passive files.

---

## 3. README.md — the Session Card (mandatory template)

Every session folder opens with this card, filled completely:

```markdown
# Session 7 — Garbage In, Garbage Out

**Block:** 1 (ML through Random Forest) | **Syllabus goal:** <verbatim from curriculum.md>
**Student goal:** "By the end of today, YOU will be able to clean a messy dataset
and avoid data leakage."
**Ship:** A data-cleaning checklist + before/after model comparison.
**Hook:** A riddle dataset riddled with missing values and typos — "would you trust this?"

## Teaching session (60 min)
| Time | Segment | Mode | Notebook cells |
|------|---------|------|----------------|
| 0–5 | Hook: ... | live demo | — |
| 5–20 | ... | lecture + visuals | 1–3 |
| ... | ... | ... | ... |
| 55–60| At-home problem handout + goal recap | — | — |

## Problem-solving session (60 min)
| Time | Segment | Notebook cells |
|------|---------|----------------|
| 0–30 | Solve at-home problems live (PRIORITY) | 4–7 |
| 30–55| In-class problem(s) | 8–10 |
| 55–60| Ship + wrap-up | 11 |

## Prerequisites recap
- <one or two bullet points from earlier sessions this session leans on>

## Judge
Run `python judge/run.py` — see judge/README.md for rubric.
```

---

## 4. The Two Hours — required anatomy

### 4.1 Teaching session (60 min)
| Segment | Duration | Requirement |
|---|---|---|
| **Hook** | 0–5 | A wow-demo or game from `demos/`. Must be tested. Creates the question the session answers. |
| **Core teaching** | 5–45 | Deliver the syllabus goal in ≤15-min segments, each with a visual or interaction. Follows `content.md`. Parts of the notebook are taught live here (students code along). |
| **Consolidation** | 45–52 | Quick recap + 2–3 oral check-questions to the class (every student should be able to answer; if not, this is caught now, not at home). |
| **At-home handout** | 52–60 | Present `at_home.md` problems, clarify expectations, state the judge rules and deadline. Students push their first attempt *before* the problem-solving session. |

### 4.2 Problem-solving session (60 min)
| Segment | Duration | Requirement |
|---|---|---|
| **At-home solutions — TOP PRIORITY** | 0–~30 | Solve the at-home problems live, step by step, *starting from students' own attempts* (ask who solved what, what they tried, where they got stuck). Full reasoning shown, not just the final code. Compare with `at_home_solution.md`. |
| **In-class problems** | ~30–55 | One or a few deeper problems from `in_class.md` solved *for and with* the students — these go beyond the at-home set: edge cases, "break the model" challenges, or a mini-competition. |
| **Ship + wrap-up** | 55–60 | Complete the session's Ship artifact, push to portfolio repos, one-sentence recap of the goal achieved. |

Timing is a guide; **priority is not**: at-home problems are always fully solved first, even if it consumes the entire hour. In-class problems are the flexible part and may be cut.

---

## 5. `teaching/content.md` — required structure

`teaching/content.md` is the session's **content-layer slice**: presentation-neutral (structure + narrative, no slide markup), the source from which the deck is generated. It must contain:

1. **Session goal** (verbatim from syllabus + student-language version)
2. **Analogy map for this session** — each new concept → its ONE analogy (consistent with prior sessions) → where the analogy honestly breaks
3. **Hook script** — exact steps of the demo, what to say, expected reaction, fallback if it fails
4. **Segment-by-segment teaching script** — for each ≤15-min segment, following EXPERIENCE → NAME → USE per new concept:
 - The one idea of the segment
 - The **experience** (game/demo/vote/story) that comes BEFORE any naming
 - The visual/demo used and when to show it
 - Notebook cells covered
 - Common misconception to pre-empt (every segment names one: e.g., "students think accuracy = quality") — these become `[MISCONCEPTION]` lines on the definition slides' notes
 - Check-question to ask the class
 - The **use-it step**: where students use the just-named concept in the same session
5. **Ship showcase plan** — the capability picture/moment (junior-tutor J5): what students see of what they'll walk out with
6. **At-home problem handout script** — how the problems are introduced
7. **Cliffhanger script** (multi-session) — the one-line tease for the next session
8. **Board/notes plan** — what gets written or drawn live

---

## 6. Problems — design rules

### 6.1 At-home problems (`at_home.md`)
- **2–4 problems**, solvable in **20–40 minutes total** by an average student at home.
- **Directly serve the session goal** — each problem maps to one bullet of the goal; no filler.
- **Difficulty ladder:** problem 1 is a confidence-builder (near-copy of what was taught), the last one requires one genuine step of transfer.
- **Self-contained:** everything needed is in the session notebook or the problem statement; no external lookups required.
- **Judge-gradable:** every at-home problem must be automatically gradeable by the judge (§7). If a part is conceptual (explain/choose), it takes the form of a function/variable the judge checks (e.g., `answer_1 = "B"` or `def explain_overfit(): return "..."` checked against keywords).
- **Format per problem:** title, story/context (relatable!), starter code cell reference in the notebook, expected input → output, points, hint (collapsed/appendix), and "what you should learn from this" one-liner.

### 6.2 In-class problems (`in_class.md`)
- 1–3 **deeper** problems: multi-step, edge-case hunting, "break the model" challenges, or team competitions with a live leaderboard.
- Solved *by the instructor with the class* — designed for discussion, not silent work.

### 6.3 Solutions (`solutions/`)
- Full reasoning written out — *why*, not just *what*. A solution that only shows code is rejected.
- Each solution notes the **most common wrong approach** and how to address it live.
- Solutions reference notebook cell numbers where the work lands.

---

## 7. Judge (autograder) — rules

- **Scope:** grades the at-home problems only. Runs against the student's copy of the session notebook (or a submitted `.py`/function file, per the session's judge README).
- **Stack:** `pytest` with a thin `run.py` runner producing a friendly, color-coded report. (nbgrader is permitted as an alternative — but the runner interface must stay: `python judge/run.py <submission>`.)
- **Student-facing output must be encouraging and specific:**
 - ` Problem 2.1 passed (3/3)` — with points
 - ` Problem 2.2: expected survival prediction for passenger #14 to be 0, got 1. Re-check your tree depth.` — a message that tells the student *what to re-examine*, never just "FAILED".
- **No hidden answers leak:** expected values live in `judge/data/` as fixtures, not in plaintext inside the notebook. Never commit solution values into student-visible files.
- **Partial credit:** each problem worth points per the rubric in `judge/README.md`; the runner prints a total `/ N`.
- **Determinism:** seeded randomness everywhere; two runs on the same submission give identical scores.
- **Tested on:** (a) the solution — must score full marks; (b) a deliberately broken attempt — must fail with helpful messages; (c) an empty submission — must not crash, must report 0; (d) a **malformed (non-notebook) file** — `run.py` must print a friendly "not a readable notebook" message and exit 1, never a traceback (wrap notebook loading in try/except; see S1–S3's `run.py`).
- **Blank-starter interplay:** the untouched student starter must score 0 with a *specific* per-problem hint ("did you fill in cell B2?"). This requires the starter to leave graded variables undefined/commented (see §8). Sort checks inside the judge so cheap probes (e.g. `hasattr`) run before failure-raising probes.
- **Judge reads the notebook itself:** strip `%magic` and `!shell` lines before `exec` (they are valid in Colab, syntax errors in plain Python).
- `judge/README.md` contains: how to run, the point rubric, and the deadline/submission policy.

---

## 8. Notebook — rules

- **One notebook per session.** Students keep a single growing artifact per session in their portfolio.
- **Explicitly split and labeled:**
 - `# PART 0 — نمایش` (hook/classroom demos as runnable cells — see §10.1; the instructor opens the notebook and runs cells, nothing else)
 - `# PART A — Teaching session` (cells worked live in the teaching hour, guided, with TODOs resolved together)
 - `# PART B — At-home problems` (starter cells for each at-home problem — these are what the judge inspects)
 - `# PART C — Problem-solving session` (cells for in-class problems, completed together)
- **Student-facing language: Persian** for all markdown and printed output. Code, variable names, and column names stay in English (they must match the judge).
- Every cell that plots something keeps its plot in the committed solution notebook.
- **Generator is the source of truth:** each session has `notebook/build_notebooks.py` that emits BOTH the student starter and the solution notebook. Never hand-edit the `.ipynb` files — fix the generator and regenerate. Before overwriting, regenerate to a scratch dir and diff cell-by-cell: drift means someone hand-patched (recover by rebasing the generator, then regen). Deterministic cell ids make diffs readable.
- **Student starter is runnable-but-unsolved:** graded cells contain TODO scaffolding with graded variables left undefined, so the starter executes clean AND scores 0/4 with specific "did you fill in cell BN?" hints from the judge.
- **Strip the PART 0 hook outputs from the student starter** (the reveal must stay a surprise in class); the solution notebook keeps ALL outputs committed.
- **Colab-installed deps:** any non-stdlib import (e.g. `arabic-reshaper`, `python-bidi`) gets a `%pip -q install ...` line at the top of the setup cell AND the PART 0 demo cell (the demo may run before setup).
- **Local data fallback:** notebooks that read a CSV ship it in `assets/` and fall back to the URL — class wifi is not a dependency.
- Notebooks must run top-to-bottom in Google Colab with only the provided `assets/` and standard course installs (one setup cell at the top, identical across all sessions).
- Markdown between cells always states *why* before *what* — a student reopening the notebook a month later should be able to follow it alone.

---

## 9. Slides — rules

### 9.1 Language, theme, and format (mandatory)
- **Language: Persian.** All visible slide content is written in Persian.
- **RTL:** the course theme handles `direction: rtl` globally. Code blocks automatically stay LTR — never force RTL on code.
- **RTL math mirroring (hard-won rule):** a `≤`/`≥` sitting inside Persian text gets **mirrored** by the bidi algorithm («وزن ≤ ۱۴» displays as ≥ — silently inverting the lesson!). The fix depends on the target (both verified on rendered output):
 - **Marp slides, plain prose:** wrap the math fragment in bidi isolates: `وزن ⁦≤ ۱۴⁩ کیلوگرم` (U+2066 / U+2069).
 - **Marp code spans AND plotly/kaleido diagram labels:** isolates do NOT survive — wrap the operator+number fragment in **LRM marks (U+200E)** instead: `` `وزن ‎≥ ۱۴‎؟` `` resp. `rtl(f"وزن ≥ ۱۴؟")` helpers in the gen scripts.
 - **Always LOOK at the rendered PNG/PDF** after adding an operator near Persian text — this bug is invisible in the source.
- **English decks with tables:** use `class: ltr` in front matter (theme class added in the S1–S3 production round) so tables/lists align LTR.
- **Course theme:** every deck uses `slide-theme/mlcourse-blue-fa.css` at the course root — the **Editorial Blue** theme: flat light-bluish canvas (style extracted from the previous "Data Analysis" course sample.pptx, palette remapped yellow → light blue), small course-name label on every slide, big dark semi-bold flat titles with a blue underline bar, flat tables/callouts, no gradients or glows, and color-coded slide classes (`lead`, `hook`, `wow`, `definition`, `quiz`, `handout`, `codespot`, `focus`). Real page numbers render bottom-left via the theme. **No session may define its own fonts, colors, or layout.** Consistency across all 32 sessions is the point.
- **Font: Vazirmatn** via `Vazirmatn.ttf` (canonical copy at `slide-theme/Vazirmatn.ttf`, course root). Vazirmatn has complete Persian glyph coverage (letters, ZWNJ, Persian digits) — B Nazanin produced malformed characters in Chrome rendering and is no longer used. `render.sh` copies the font next to the slides automatically — do not commit per-session font edits.
- **Deck anatomy per slide:** visible Persian content + a Marp presenter-note comment (`<!-- ... -->`) containing the instructor script: timing, what to say (key lines verbatim), which notebook cell/demo to run, expected reactions, misconception alerts, check questions, and fallbacks. A slide without a note is not done — the instructor must never wonder what a slide refers to.
- **Language simplicity rule:** Persian slides must use simple, familiar wording. Persian technical keywords that middle-schoolers won't know (e.g., «ویژگی»، «برچسب») are introduced with the English ML term in parentheses on first use (e.g., «ویژگی (Feature)») and explained via the everyday analogy in the presenter note. The English deck doubles as the terminology reference.
- **English companion deck (mandatory):** every session has `slides_en.md` — a simple-English version of the same deck (same slides, same notes, same order). Persian terminology may be unfamiliar; the English deck is the fallback both for instructors and for students who know the English terms from games/docs. Kept in lockstep: a change to one deck must be mirrored in the other.
- **Presenter notes are written in English** in BOTH decks. Persian text inside PDF annotations renders with broken bidi/shaping — the notes are instructor-facing, so English avoids the problem entirely. (The PPTX notes likewise use the English note text.)
- **Editable PPTX (mandatory):** every session has `slides.pptx`, built by `build_pptx.py` from `slides.md` — real editable text (NOT slide images), RTL paragraphs, Vazirmatn font, gradient backgrounds, presenter notes attached. Purpose: the instructor can simplify or swap unfamiliar Persian keywords directly in PowerPoint without touching the build chain.
- **Four outputs are produced** via `./render.sh` in the session's `teaching/slides/` folder (it locates headless Chrome, sets up local libraries, copies the Persian font, applies the course theme):
 1. `slides.pdf` — Persian student deck (clean)
 2. `slides_with_notes.pdf` — instructor deck with notes as PDF annotations
 3. `slides_en.pdf` — English student deck
 4. `slides.pptx` — editable Persian PowerPoint (via `build_pptx.py`)
- The instructor never installs anything to render or present.
- **Live preview (mandatory tool):** every session's `teaching/slides/` folder contains `preview.sh` — an identical copy of the course-level template `slide-theme/preview.sh` (do not fork per session; improvements go into the template and are re-copied). Running `./preview.sh` starts a Marp watch-mode server at `http://localhost:8080` (set `PORT=8081` etc. to run several sessions side by side — the Marp server reads the `PORT` env): save `slides.md` (or `slides_en.md`) in any editor and the deck re-renders in about a second; press **P** in the browser for the presenter view (notes + next-slide preview). This is the instructor's self-service editing loop — the markdown is the source of truth, PDFs/PPTX are generated artifacts. Full editing instructions for humans: `slide-theme/PREVIEW-GUIDE.md` (ship it with the course; it documents the markdown mini-language, slide classes, image paths, notes, and troubleshooting).

### 9.2 Content rules
- Visual-first: a slide full of text is a bug. Maximum **~12 words** per slide (junior-tutor budget; 30 is the hard fail line checked by Layer J); diagrams, plots, and animations carry the content.
- The hook gets its own dramatic slide (or none — pure demo).
- Slide count guide: **10–20 slides** per teaching session.
- **Session skeleton (junior-tutor §5, verified by Layer J):** mystery hook → experience the concept (game/vote/demo) → name it (`definition` + `[MISCONCEPTION]` in note) → use it (quiz/vote/code) → **Ship slide** (capability picture: what THEY can do now) → at-home problems (`handout`) → cliffhanger (`wow`) for the next session.
- End slides, always in this order: the session goal (re-stated), the Ship, the at-home problems, and the judge command.
- **The judge command must be VISIBLE on a slide**, not only in a note — students photograph slides, not notes.
- **Quizzes that consume a reveal come AFTER the reveal.** If a quiz asks students to trace something on a picture (tree, plot), that picture must appear on a slide BEFORE the quiz — otherwise the quiz spoils the reveal and doubles as its own answer key.
- **Honest captions:** a caption must survive contact with the data. If a split's "pure" side holds exactly one animal, say so — the weighted-average lesson depends on it. Never write "both sides stay mixed" when one side is pure.
- **Recompute every number in every artifact** (slides, notes, problems, solutions, diagrams) against the actual notebook before delivery — and grep for the numbers' other homes afterwards. "1.58 vs 1.57" and "three vs two-and-a-half times" class errors are found by recomputation, not by re-reading.
- Theme custom classes (Neural Playground theme):
 - `<!-- _class: lead -->` — session title & closing
 - `<!-- _class: hook -->` — hook/demo slides (pink energy)
 - `<!-- _class: definition -->` — new-vocabulary slides (green frame)
 - `<!-- _class: wow -->` — wow-moment slides (amber burst)
 - `<!-- _class: codespot wow -->` — the "magic lines" code spotlight
 - `<!-- _class: dark -->` — serious/dramatic beats
 - `<!-- _class: quiz -->` — consolidation/quiz slides (dashed frame)
 - `<!-- _class: handout -->` — at-home problem slides (light-blue frame)
 - `<!-- _class: ltr -->` — LTR escape hatch for English decks (left-aligned text, LTR tables/lists); usable as global `class: ltr` in front matter or composed per slide (`<!-- _class: ltr lead -->`)
- **Code blocks:** always tag the fence with a language (```` ```python ````) so the theme's hljs palette renders syntax colors (the theme ships the code-card chrome: tint, accent bar, dots, `~/ml-course`). A flat single-color code block is a bug.

### 9.3 AI-generated slide art (mandatory tool, use it)

Slides become visually rich with generated illustrations. The course has an image-generation API and a helper script; every session MUST use it to add hero/section illustrations.

**Tool:** `slide-theme/gen_image.sh` — run from the course root:
- pass output path, size (e.g. 1024x512), seed, then the prompt on stdin (or as a prompt-file 4th argument)
- API behind it: model `flux2-dev` at `http://192.168.1.153:30083/v1/images/generations`

**Rules:**
1. **One visual identity across all 32 sessions** — every prompt MUST include these course art-style keywords (LIGHT theme, **blue editorial identity** — the theme is `mlcourse-blue-fa`, the older cream/purple keyword set is superseded, see §13):
 `flat editorial illustration, light blue background, soft blue and teal accents, clean vector shapes, minimal shading, no text`
2. **No text in images** — slide text is rendered by the theme; generated text renders badly. Append `no text` to every prompt.
3. **Deterministic:** always pass an explicit seed. Save the prompt + seed + size of every generated image in `assets/images-manifest.md` so any image can be regenerated or restyled later.
4. **Shared template art (used by every session, copied by render.sh):** `slide-theme/shared/` holds `shared_hero.png` (lead slides), `shared_closing.png` (closing slides), and `shared_band.png` (goal/recap slides). Decks reference them as `![hero](shared_hero.png)` etc. — never copy them into `assets/` manually; render.sh handles it. Manifest with prompts/seeds: `slide-theme/shared/README.md`.
5. **Per-session art (minimum):**
 - an illustration for the **hook** slide(s)
 - an illustration for at least one concept slide where a metaphor needs a picture (e.g., the "fortune teller", the "overfitting monster")
 - plus any slide where a picture replaces three bullets
 - matplotlib plots and notebook outputs are NOT replaced — those are real data visualizations, and their authenticity is part of the lesson
5. Images land in the session's `assets/` folder, are referenced from `slides.md` like any image, and inherit the theme's framed/glowing image style automatically.
6. Keep generated art **supportive, not decorative noise**: one strong image per slide, never more.
7. **Deck weight budget:** the full PDF deck must stay **under ~8 MB**. Generated images at 512-width PNG are fine; avoid 1024x1024+ art unless the lead slide needs it (use the shared hero instead). If a deck exceeds the budget, downscale images before re-rendering.
8. **If a figure carries labels, it is not AI art** — the API garbles text even with `no text` in the prompt (S2's tree_anatomy lesson). Labelled figures are code-generated diagrams (§9.4).

### 9.4 Code-generated diagrams on slides (mandatory rules)

Flowcharts, anatomy figures, data tables, box-and-balls figures — anything with exact text — is generated by a **committed script** (`assets/gen_<name>.py`) recorded in `assets/images-manifest.md`. Rules (learned from S1–S3 review):
- **Font:** Vazirmatn, EVERYWHERE. matplotlib: register from file (`font_manager.fontManager.addfont(<course root>/slide-theme/Vazirmatn.ttf)` + `rcParams["font.family"]`). plotly/kaleido: `font_family="Vazirmatn"` resolves from the system fontconfig.
- **Boxes are sized from MEASURED text** (renderer extents) with padding — never eyeballed widths; text must never touch or cross a border.
- **Titles/labels sit in a reserved zone INSIDE their card** (e.g. a tinted title band) — text placed at the card-top coordinate lands on the border line.
- **Arrows connect box OUTLINES** (border-intersection points + small gap), and node positions keep clear corridors so no edge or leader line crosses a box.
- **The readability floor applies INSIDE images:** judge text size and line weight on the rendered PDF page at presentation zoom, not on the export canvas; fix the generator, re-render.
- **RTL math in images:** bidi isolates are silently ignored by plotly/kaleido AND matplotlib — use LRM marks (U+200E) around operator+number fragments, then inspect the PNG.
- Superseded assets stay listed in the manifest as superseded (with why), never silently deleted or orphaned.

---

## 10. Demos & visualizations — rules

### 10.1 Zero-terminal rule (mandatory)
**The instructor must never need a terminal, a Python environment, or a build step to run a demo.** Every demo used in the teaching session or the hook is delivered in one of exactly two forms:

1. **Embedded in the session notebook** (preferred): a `PART 0 — نمایش` section at the top of the notebook holds one cell per demo. Running the demo = running a notebook cell. Demos are numbered and titled in Persian, run in order, and must execute in Google Colab with only the standard course setup cell.
2. **Pre-built HTML** (for demos that can't live in a notebook — e.g., interactive games, third-party widgets): a single self-contained `.html` file in `demos/` that opens directly in a browser by double-click. No server, no `npm install`, no build. All assets inlined or relative to that one file.

The `demos/` folder exists only for form 2 and for raw demo assets (recordings, fallback screenshots). If a demo exists only as a `.py` script requiring `python demos/foo.py`, it is **not done**.

### 10.2 General demo rules
- Every hook is a runnable artifact with a one-line way to run it (a cell, or a double-clicked HTML file).
- Prefer live data from the students (their voices, their photos, their votes) over static files whenever the session allows.
- Each demo has a **stated fallback** in `content.md` (screenshot/video) in case of environment failure.
- Every animation used in teaching is reproducible (matplotlib `FuncAnimation` embedded in the notebook or similar) — no orphan GIFs whose source is lost.

### 10.3 J-format demos (junior-tutor) — the kid-demo vocabulary

Beyond base demo forms, sessions use the junior-tutor J-formats (templates at `/home/pardis_ai/skills/junior-tutor/assets/demos/`):

| Format | Use for |
|---|---|
| J1 mystery hook | opening a session; the reveal IS the lesson |
| J2 guess-the-rule | inducing a concept BEFORE naming it |
| J3 battle arena | two strategies compete; learning as a race |
| J4 you-be-the-model | student plays the algorithm before coding it |
| J5 capability showcase | the Ship — the app students will build, shown first |
| J6 sandbox playground | free exploration, early finishers, homework play |

Rules: kid-usable (big buttons ≥44px, one tap per action, no typing unless the topic is typing, instant feedback); offline single-file HTML matching the course theme; **format choice is presented to the course owner as a shortlist with pros/cons — never picked silently**; every demo verified with the base `verify_demo.py --rtl` and carries a `RUN DEMO:` slide note. J1/J5 hooks may alternatively live as notebook cells in PART 0 per §10.1.

---

## 11. Quality bar & Definition of Done

A session is **done** only when every box is checked:

- [ ] Folder follows the §2 structure exactly; naming matches syllabus
- [ ] README session card complete (timetables, cell-mapping, prerequisites)
- [ ] Syllabus goal delivered; no extra topics smuggled in
- [ ] Hook tested end-to-end; fallback written
- [ ] Demos follow the zero-terminal rule (§10.1): embedded notebook cells in PART 0 or self-contained HTML — no `python ...` required by the instructor
- [ ] Slides: Persian + RTL + course theme (`mlcourse-blue-fa`), every slide has a presenter note; `render.sh` produces `slides.pdf`, `slides_with_notes.pdf`, `slides_en.pdf` (English companion in lockstep), and `slides.pptx` (editable, real text, RTL, Vazirmatn, notes attached); Vazirmatn embedded, zero malformed Persian characters
- [ ] `preview.sh` present in `teaching/slides/` (identical to `slide-theme/preview.sh`) and verified working: `./preview.sh` serves the deck at `http://localhost:8080` and re-renders on save; image paths correct in the browser preview (no broken-image boxes — session art is referenced as `../../assets/<name>.png`)
- [ ] Zero overflow: no image or text block extends past the slide box on any page of `slides.pdf`, `slides_en.pdf`, or `slides_with_notes.pdf` (verify programmatically: every image bbox and text block must lie within the 960x540 page rect). The theme enforces image max-heights and a flex overflow guard, but a slide that stacks a heading + table + image + caption can still overflow — if it does, cut content (e.g., drop a redundant image), never shrink the font. One strong visual per slide
- [ ] AI-generated art: hero + hook + at least one concept illustration, all with course style keywords and `no text`, seeds pinned and recorded in `assets/images-manifest.md` (see §9.3)
- [ ] Teaching content.md: segments ≤15 min, each with a visual, a misconception, and a check-question
- [ ] Slides exported, visual-first, ending with goal/Ship/at-home/judge slides
- [ ] Notebook: A/B/C split, runs top-to-bottom in Colab, solution version complete with plots
- [ ] At-home problems: 2–4, 20–40 min, difficulty ladder, all judge-gradable, handed out at end of teaching hour
- [ ] Solutions: full reasoning + common wrong approaches, for both at-home and in-class sets
- [ ] Judge: passes the three tests (solution = full marks, broken = helpful failures, empty = 0); deterministic; no answer leakage
- [ ] Problem-solving plan puts at-home solutions first, before any in-class problem
- [ ] Ship artifact defined and producible within the problem-solving hour
- [ ] **Layer J passed:** `/home/pardis_ai/skills/junior-tutor/assets/scripts/verify_junior.sh <session-dir>` is clean — session skeleton complete (hook, interactive segment, definition+misconception, use-it, Ship slide, handout, cliffhanger), word budget respected (~12 target, 30 hard line), every slide has a note, RUN DEMO references resolve
- [ ] EXPERIENCE → NAME → USE audit: no definition slide whose concept wasn't experienced first in the same session
- [ ] All files committed; solutions excluded from the student-facing bundle
- [ ] A dry-run of the full two hours has been performed (by the author or a reviewer) against this checklist

---

## 12. Review workflow

1. **Author** builds the session against this guide.
2. **Self dry-run:** author executes the full checklist in §11 and fixes everything.
3. **Peer review:** a second person reviews the folder against §11 only (this doc is the entire rubric — no reviewer discretion needed) and dry-runs the problem-solving hour.
4. **Deliver**, then within 48h write a short retro note (3 lines max) at the bottom of the session README: what confused students, what dragged, what delighted. The next session's author reads it.

---

## 13. Course-level consistency extras

- **Setup cell identical everywhere** — same imports/install pattern across all notebooks; students never debug environments.
- **Slide theme shared everywhere** — `slide-theme/mlcourse-blue-fa.css` + `Vazirmatn.ttf` at the course root are the single source of styling for all 32 sessions (the superseded cream theme `mlcourse-fa.css` is kept for history); candidate themes reviewed during course design are archived in `slide-theme/candidates/` for reference only. Style provenance: extracted from the previous "Data Analysis" course sample.pptx per the slide-craft style-extraction protocol, palette remapped to light blue at the course owner's request.
- **Recurring cast:** use the same running datasets/characters across sessions (e.g., the Titanic passengers, the class friendship graph) so familiarity does cognitive work instead of novelty.
- **Vocabulary wall:** one canonical glossary (`GLOSSARY.md` at course root); every new term introduced in a session must be added there by the session author, with the kid-friendly definition used in that session.
- **Energy audit:** when planning a block, verify the alternating heavy/visual pacing from the syllabus; if two consecutive sessions are both theory-heavy, redesign one.
- **Prerequisite chain:** each session card lists its prerequisites; if you must assume something not yet taught, stop and redesign the session.

---

## 14. Regeneration — updating presentations from content

The content layer (curriculum.md + sessions/*/teaching/content.md) is the source of truth; decks are generated artifacts. This is the workflow when content changes — whether edited in this repo or supplied from anywhere else (a doc, notes, another course's materials):

1. **Ingest the new content** — diff it against the session's current `teaching/content.md`. If it came from an external source, parse it into the §5 structure first.
2. **Present the change summary** — which sessions/slides/demos/problems are affected — and get approval (**Checkpoint R**) before rebuilding anything.
3. **Regenerate only what's affected** — never touch unaffected sessions. Port over still-valid presentation decisions: generated art with pinned seeds (from `assets/images-manifest.md`) is REUSED, not regenerated, unless the content change invalidates it.
4. **Re-verify everything regenerated** — full Layer A–D (deck checks, overflow, notes) + `verify_demo.py` on affected demos + Layer J (§11) on the session.
5. **Hand back a changelog** — content changes → deck changes, one line each.

What lives where:

| Change | Edit | Then |
|---|---|---|
| wording, examples, analogies, story | the content layer | regenerate decks (this section) |
| theme, colors, fonts | `slide-theme/mlcourse-fa.css` (course root) | re-render all decks |
| a quick slide-level fix | the deck `.md` via `preview.sh` | fine for one-offs; port lasting changes into `teaching/content.md` — a regeneration overwrites deck tweaks |
| new problem / demo | content layer + demo file | regenerate affected slides |

Instructor runbook: each session README must carry the one-page run order (what to open: slides PDF → demos → notebook; per-demo runbook lines; fallbacks). The instructor never assembles this themselves.
