# Slides Live Preview & Editing Guide

How to edit session slide decks yourself and see the result instantly — no
build commands, no waiting, no AI in the loop.

---

## 30-second quickstart

```bash
cd sessions/<session>/teaching/slides
./edit.sh          # Persian deck (or: ./edit.sh en for the English deck)
```

(`preview.sh` also still works — `edit.sh` is the friendlier wrapper.)

Open `http://localhost:8080/teaching/slides/slides.md` in your browser
(for the English deck: `.../slides_en.md`). Now edit that file in any
editor — VS Code, vim, Notepad, anything — and **every save re-renders the
deck in about a second**, live in the browser.

Stop with `Ctrl+C`. When you are happy with the result, run `./render.sh` to
produce the final files (`slides.pdf`, `slides_with_notes.pdf`,
`slides_en.pdf`, `slides.pptx`).

---

## The editing model

`slides.md` (and `slides_en.md`) are plain [Marp](https://marp.app/)
markdown files and are the **source of truth** for the deck. Everything you
see on the slides is in this file; the PDFs and PPTX are generated from it.
Never edit a PDF — edit the markdown and re-render.

Each deck is a sequence of slides separated by `---`:

```markdown
---
<!-- _class: definition -->
<!-- note: introduce the word feature. 60 seconds. -->
# ویژگی (Feature)

**ویژگی** = یک سرنخ *(یک ستون)*
```

What each part does:

| You write | You get |
|---|---|
| `# Title` / `## Subtitle` | slide heading / subheading |
| `**bold**`, `*italic*` | emphasis |
| `- item` lists | bullet cards |
| `![art](../../assets/my_image.png)` | framed image from the session assets |
| `![hero](shared_hero.png)` | shared template art (hero/closing/band) |
| ``` ```python code``` ``` | LTR code block with terminal styling |
| `<!-- _class: lead -->` | slide look (see class table below) |
| `<!-- note: ... -->` or any bare `<!-- ... -->` | presenter note (English) |
| `---` | slide separator |

### Slide classes (the deck's "moods")

| Class | Use for |
|---|---|
| `lead` | session title & closing slides |
| `hook` | hook / live-demo slides |
| `wow` | surprise moments |
| `definition` | new vocabulary |
| `quiz` | check questions |
| `handout` | at-home problems |
| `codespot` | code spotlights (combine: `codespot wow`) |
| `focus` | deep-attention beats |

Put them as a comment at the top of the slide: `<!-- _class: hook -->`.

### Images

- Session art lives in the session's `assets/` folder — reference it as
  `![art](../../assets/name.png)` (relative path, two levels up).
- Shared course art (`shared_hero.png`, `shared_closing.png`,
  `shared_band.png`) sits next to the deck after the first run of
  `preview.sh`/`render.sh` — reference it by bare filename.
- To add a new image: drop the file in `assets/`, add an entry to
  `assets/images-manifest.md`, reference it from the deck.
- Missing image = broken-image box in the PDF. If you see one, check the
  path (watch the `../../` prefix for session art).

### Presenter notes

Notes are written in **English** (Persian breaks in PDF annotations) and go
in an HTML comment on the slide. In the browser, press **P** to open the
presenter view and see them next to the slide — the same notes end up in
`slides_with_notes.pdf` and the PPTX.

---

## Commands reference

| Command | What it does |
|---|---|
| `./preview.sh` | live server at `http://localhost:8080/teaching/slides/slides.md`, watch mode, Persian deck |
| `./preview.sh slides_en.md` | same, English deck (`.../slides_en.md`) |
| `./render.sh` | final build: all 3 PDFs + editable PPTX |

Inside the browser preview:

| Key | Action |
|---|---|
| `P` | presenter view (notes + next-slide preview) |
| `T` | toggle theme of the presenter view |
| arrows / space | navigate slides |

---

## Editing the PPTX instead

`slides.pptx` is a real, editable PowerPoint (editable text, RTL, Vazirmatn,
notes attached) for quick tweaks in PowerPoint itself. But the PPTX is a
**generated artifact** — if you change the markdown later and re-render,
your PPTX edits are overwritten. For anything more than a one-off fix,
edit `slides.md` and re-render; that keeps all four outputs in sync.

---

## Rules that keep the course consistent

1. `slides.md` and `slides_en.md` must stay in lockstep — a change to one
   deck is mirrored in the other before rendering.
2. All visible slide text is Persian (English deck: simple English); all
   presenter notes are English.
3. No emojis anywhere (Golden Rule 0 in `session-creation-guide.md`).
4. Keep slides visual-first (~20 words max); images carry the content.
5. The theme (`slide-theme/mlcourse-blue-fa.css`) is shared by all 32 sessions —
   never add per-session fonts, colors, or inline styles.
6. Deck budget: the final PDF stays under ~8 MB; downscale images if needed.

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Broken-image box in PDF | image path wrong — check `../../assets/...` prefix and that the file exists |
| Literal `**` visible on a slide | an unbalanced `**` pair (often split across an image line) — every `**` needs its closing `**` in the same text block |
| Port 8080 busy | another preview server is running; stop it, or `marp -s -w -I ../.. --theme-set <theme> -p 8081` |
| Deck does not update on save | make sure you are editing the file the server serves (the one shown in the URL) |
| Persian looks wrong in PDF | `Vazirmatn.ttf` missing next to the deck — re-run `./render.sh` |
| Preview shows theme without font | same as above; preview copies the font on startup |
