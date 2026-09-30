#!/usr/bin/env python3
"""Build an editable PPTX (slides.pptx) from the Marp slides.md source.

Parses slides.md (Marp markdown), renders each slide as native PowerPoint
text boxes with the course theme (gradient background, purple headings,
Vazirmatn font, RTL), and attaches presenter notes to every slide.

This is the editable Persian deck — text is real text (simplifiable in
PowerPoint), NOT images.

Run from the slides directory:  python3 build_pptx.py
Requires: python-pptx, Vazirmatn.ttf in this directory.
"""
import os, re, sys
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "slides.md")
OUT = os.path.join(HERE, "slides.pptx")
FONT_FILE = os.path.join(HERE, "Vazirmatn.ttf")

# ---- theme constants (must match slide-theme/mlcourse-blue-fa.css — "Editorial Blue") ----
FONT = "Vazirmatn"
TITLE_COLOR = RGBColor(0x3C, 0x40, 0x43)   # dark gray flat titles
TEXT_COLOR = RGBColor(0x3C, 0x40, 0x43)    # sample's dark gray ink
ACCENT = RGBColor(0x6F, 0xA8, 0xDC)        # medium blue
BG_TOP = RGBColor(0xED, 0xF4, 0xFB)        # light bluish canvas
BG_BOTTOM = RGBColor(0xED, 0xF4, 0xFB)     # flat — same solid color
WOW_TITLE = RGBColor(0x2B, 0x6C, 0xB0)     # blue for wow slides
FOCUS_TITLE = RGBColor(0x34, 0x49, 0x5E)   # blue-gray for focus slides
HOOK_TITLE = RGBColor(0x2B, 0x6C, 0xB0)    # blue for hook slides
LEAD_BG = RGBColor(0xA9, 0xCC, 0xE8)       # soft blue lead background

SLIDE_W, SLIDE_H = Inches(13.333), Inches(7.5)

def parse_slides(md_text):
    """Split marp markdown into slides; return list of (html_classes, blocks, notes)."""
    md_text = re.sub(r"^---.*?---\s*", "", md_text, count=1, flags=re.S)  # frontmatter
    raw = re.split(r"\n---\n", md_text)
    slides = []
    for chunk in raw:
        chunk = chunk.strip()
        if not chunk:
            continue
        classes = []
        m = re.search(r"<!--\s*_class:\s*([^>]+?)\s*-->", chunk)
        if m:
            classes = [c.strip() for c in m.group(1).split() if not c.startswith("_")]
        # extract presenter note (last <!-- ... --> without directives)
        note = ""
        all_notes = re.findall(r"<!--(.*?)-->", chunk, flags=re.S)
        for n in all_notes:
            if "_class" not in n and "_paginate" not in n:
                note = n.strip()
        # strip all html comments from visible content
        visible = re.sub(r"<!--.*?-->", "", chunk, flags=re.S).strip()
        # build blocks: (kind, text, indent) from markdown lines
        blocks = []
        for line in visible.splitlines():
            line = line.rstrip()
            if not line.strip():
                continue
            if line.startswith("# "):
                blocks.append(("h1", line[2:].strip()))
            elif line.startswith("## "):
                blocks.append(("h2", line[3:].strip()))
            elif line.startswith("### "):
                blocks.append(("h3", line[4:].strip()))
            elif re.match(r"^\s*[-*] ", line):
                blocks.append(("li", re.sub(r"^\s*[-*] ", "", line)))
            elif re.match(r"^\s*\d+\. ", line):
                blocks.append(("li", re.sub(r"^\s*\d+\. ", "", line)))
            elif line.startswith("```"):
                blocks.append(("code_start", ""))
            elif line.startswith("|"):
                blocks.append(("table", line))
            elif line.startswith("!["):
                m2 = re.search(r"\(([^)]+)\)", line)
                blocks.append(("img", m2.group(1) if m2 else ""))
            else:
                blocks.append(("p", line))
        # merge code_start..code lines
        merged, in_code, code_lines = [], False, []
        for kind, text in blocks:
            if kind == "code_start":
                in_code, code_lines = True, []
                continue
            if in_code:
                if text.strip() == "```":
                    merged.append(("code", "\n".join(code_lines)))
                    in_code = False
                else:
                    code_lines.append(text)
                continue
            merged.append((kind, text))
        # merge consecutive table rows
        final, prev_table = [], None
        for kind, text in merged:
            if kind == "table":
                cells = [c.strip() for c in text.strip("|").split("|")]
                if all(re.match(r"^[-: ]+$", c) for c in cells if c):
                    continue
                if prev_table is not None:
                    prev_table.append(cells)
                else:
                    prev_table = [cells]
                    final.append(("table_rows", prev_table))
            else:
                prev_table = None
                final.append((kind, text))
        slides.append((classes, final, note))
    return slides

def md_inline(text):
    """Strip markdown emphasis markers for pptx runs (keep it simple)."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    return text

def set_rtl(paragraph):
    paragraph.alignment = PP_ALIGN.RIGHT
    pPr = paragraph._p.get_or_add_pPr()
    pPr.set("rtl", "1")

def add_gradient_bg(slide, dark=False, wow=False, lead=False):
    # flat editorial style: solid fill, per-class canvas tints
    bg = slide.background
    fill = bg.fill
    fill.solid()
    if lead:
        fill.fore_color.rgb = LEAD_BG          # soft blue lead canvas
    elif dark:
        fill.fore_color.rgb = RGBColor(0xE3, 0xE9, 0xF0)  # focus blue-gray
    elif wow:
        fill.fore_color.rgb = RGBColor(0xDC, 0xEB, 0xF8)  # wow pale blue
    else:
        fill.fore_color.rgb = BG_TOP

def add_table(slide, rows, top, height):
    n_r, n_c = len(rows), max(len(r) for r in rows)
    tbl = slide.shapes.add_table(n_r, n_c, Inches(1.0), top, SLIDE_W - Inches(2.0), height).table
    # RTL table
    tblPr = tbl._tbl.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}tblPr')
    if tblPr is not None:
        tblPr.set("rtl", "1")
    for i, row in enumerate(rows):
        for j in range(n_c):
            cell = tbl.cell(i, j)
            cell.text = md_inline(row[j]) if j < len(row) else ""
            cell.text_frame.paragraphs[0].alignment = PP_ALIGN.RIGHT
            cell.text_frame.paragraphs[0].font.name = FONT
            cell.text_frame.paragraphs[0].font.size = Pt(16)
            if i == 0:
                cell.text_frame.paragraphs[0].font.bold = True
                cell.text_frame.paragraphs[0].font.color.rgb = TITLE_COLOR
    return tbl

def main():
    if not os.path.exists(FONT_FILE):
        sys.exit(f"ERROR: {FONT_FILE} missing (render.sh copies it)")
    md = open(SRC, encoding="utf-8").read()
    slides = parse_slides(md)

    prs = Presentation()
    prs.slide_width, prs.slide_height = SLIDE_W, SLIDE_H
    blank = prs.slide_layouts[6]

    for idx, (classes, blocks, note) in enumerate(slides, 1):
        slide = prs.slides.add_slide(blank)
        dark, wow, lead = "dark" in classes or "focus" in classes, "wow" in classes, "lead" in classes
        hook = "hook" in classes
        add_gradient_bg(slide, dark=dark, wow=wow, lead=lead)

        # course-name label, top of every slide (sample style)
        lb = slide.shapes.add_textbox(Inches(0.55), Inches(0.18), Inches(3.5), Inches(0.3))
        lp = lb.text_frame.paragraphs[0]; set_rtl(lp)
        lr = lp.add_run(); lr.text = "دورهٔ یادگیری ماشین"
        lr.font.size = Pt(11); lr.font.name = FONT; lr.font.color.rgb = TEXT_COLOR

        # image shapes: place centered, upper half
        img_tops = []
        y_cursor = Inches(0.5)
        if dark:   title_color = FOCUS_TITLE
        elif wow:  title_color = WOW_TITLE
        elif hook: title_color = HOOK_TITLE
        else:      title_color = TITLE_COLOR
        body_color = TEXT_COLOR

        for kind, text in blocks:
            if kind == "h1":
                tb = slide.shapes.add_textbox(Inches(0.8), y_cursor, SLIDE_W - Inches(1.6), Inches(1.2))
                tf = tb.text_frame; tf.word_wrap = True
                p = tf.paragraphs[0]; set_rtl(p)
                r = p.add_run(); r.text = md_inline(text)
                r.font.size = Pt(40 if lead else 34); r.font.bold = True
                r.font.name = FONT; r.font.color.rgb = title_color
                y_cursor += Inches(1.1)
            elif kind == "h2":
                tb = slide.shapes.add_textbox(Inches(0.8), y_cursor, SLIDE_W - Inches(1.6), Inches(0.9))
                tf = tb.text_frame; tf.word_wrap = True
                p = tf.paragraphs[0]; set_rtl(p)
                r = p.add_run(); r.text = md_inline(text)
                r.font.size = Pt(28 if not lead else 24); r.font.bold = True
                r.font.name = FONT; r.font.color.rgb = title_color if not lead else TEXT_COLOR
                y_cursor += Inches(0.8)
            elif kind in ("h3", "p"):
                tb = slide.shapes.add_textbox(Inches(0.8), y_cursor, SLIDE_W - Inches(1.6), Inches(0.7))
                tf = tb.text_frame; tf.word_wrap = True
                p = tf.paragraphs[0]; set_rtl(p)
                r = p.add_run(); r.text = md_inline(text)
                r.font.size = Pt(20 if kind == "h3" else 18)
                r.font.name = FONT; r.font.color.rgb = body_color
                y_cursor += Inches(0.55)
            elif kind == "li":
                tb = slide.shapes.add_textbox(Inches(0.8), y_cursor, SLIDE_W - Inches(1.6), Inches(0.55))
                tf = tb.text_frame; tf.word_wrap = True
                p = tf.paragraphs[0]; set_rtl(p)
                r = p.add_run(); r.text = "• " + md_inline(text)
                r.font.size = Pt(19); r.font.name = FONT; r.font.color.rgb = body_color
                y_cursor += Inches(0.45)
            elif kind == "code":
                tb = slide.shapes.add_textbox(Inches(0.8), y_cursor, SLIDE_W - Inches(1.6), Inches(1.6))
                tf = tb.text_frame; tf.word_wrap = False
                p = tf.paragraphs[0]; p.alignment = PP_ALIGN.LEFT  # code stays LTR
                r = p.add_run(); r.text = text
                r.font.size = Pt(13); r.font.name = "Consolas"
                r.font.color.rgb = body_color
                y_cursor += Inches(0.28) * max(1, text.count("\n") + 1) + Inches(0.25)
            elif kind == "img":
                if os.path.exists(text):
                    from PIL import Image as PILImage
                    try:
                        with PILImage.open(text) as im:
                            w, h = im.size
                    except Exception:
                        w, h = 1024, 512
                    max_w, max_h = Inches(8.2), Inches(4.6)
                    scale = min(max_w / w, max_h / h)
                    pw, ph = int(w * scale), int(h * scale)
                    left = int((SLIDE_W - pw) / 2)
                    slide.shapes.add_picture(text, left, Inches(1.1), width=pw, height=ph)
            elif kind == "table_rows":
                add_table(slide, text, y_cursor, Inches(0.4) * len(text) + Inches(0.2))
                y_cursor += Inches(0.4) * len(text) + Inches(0.35)

        # presenter note
        if note:
            ntf = slide.notes_slide.notes_text_frame
            ntf.text = note
            for p in ntf.paragraphs:
                for r in p.runs:
                    r.font.name = FONT

        # page number (bottom-left for RTL)
        pn = slide.shapes.add_textbox(Inches(0.3), SLIDE_H - Inches(0.5), Inches(1.2), Inches(0.35))
        p = pn.text_frame.paragraphs[0]; p.alignment = PP_ALIGN.LEFT
        r = p.add_run(); r.text = f"{idx} / {len(slides)}"
        r.font.size = Pt(12); r.font.name = FONT
        r.font.color.rgb = TEXT_COLOR

    prs.save(OUT)
    print(f"wrote {OUT} — {len(slides)} slides, editable text, notes attached")

if __name__ == "__main__":
    main()
