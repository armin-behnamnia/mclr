"""Generate assets/supervised_study_exam.png — the Session 1 "study vs exam" diagram.

Code-generated (course rule): edit THIS script, never the PNG by hand.
Run from the session root:  python3 assets/gen_supervised_diagram.py
Recorded in assets/images-manifest.md.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import font_manager
import arabic_reshaper
from bidi.algorithm import get_display


def fa(text):
    return get_display(arabic_reshaper.reshape(str(text)))


HERE = os.path.dirname(os.path.abspath(__file__))
COURSE_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

# slide-craft rule: generated graphics use the SAME font as the slide theme
font_manager.fontManager.addfont(os.path.join(COURSE_ROOT, "slide-theme", "Vazirmatn.ttf"))
plt.rcParams["font.family"] = "Vazirmatn"

# palette: course "Editorial Blue" identity
INK = "#1e2a38"
BLUE = "#2f6fed"
LIGHT = "#eaf1fd"
GREEN = "#1f9d6b"
AMBER = "#f59e0b"
BOX = "#ffffff"

fig, ax = plt.subplots(figsize=(10.4, 4.4), dpi=150)
ax.set_xlim(0, 96)
ax.set_ylim(0, 40)
ax.axis("off")


def mini_table(x0, title, title_color, answers_visible):
    cols = [fa("رنگ"), fa("اندازه"), fa("بافت"), fa("میوه؟" if not answers_visible else "میوه")]
    rows = [
        [fa("قرمز"), fa("متوسط"), fa("صاف"), fa("سیب") if answers_visible else "؟"],
        [fa("زرد"), fa("دراز"), fa("صاف"), fa("موز") if answers_visible else "؟"],
        [fa("بنفش"), fa("ریز"), fa("چروک"), fa("انگور") if answers_visible else "؟"],
    ]
    w, cw, rh = 30, 7.5, 4.6
    y0 = 4
    table_top = y0 + 20 + rh            # top of the header row
    card_top = table_top + 7.6          # title zone fully INSIDE the card
    # outer card
    ax.add_patch(mpatches.FancyBboxPatch((x0 - 1.5, y0 - 2.2), w + 3, card_top - y0 + 2.2,
                 boxstyle="round,pad=0.6,rounding_size=1.2",
                 fc=BOX, ec=title_color, lw=2.2))
    # title band (pale tint) with the title centered inside it — never on the border
    ax.add_patch(mpatches.Rectangle((x0 - 1.5, table_top + 0.6), w + 3, card_top - table_top - 0.6,
                 fc=title_color, alpha=0.12, ec="none"))
    ax.text(x0 + w / 2, (table_top + 0.6 + card_top) / 2, fa(title), ha="center", va="center",
            fontsize=15, fontweight="bold", color=title_color)
    # header row
    ax.add_patch(mpatches.Rectangle((x0, y0 + 20), w, rh, fc=LIGHT, ec="none"))
    for j, c in enumerate(cols):
        ax.text(x0 + j * cw + cw / 2, y0 + 20 + rh / 2, c, ha="center", va="center",
                fontsize=12, fontweight="bold", color=INK)
    for i, row in enumerate(rows):
        ry = y0 + 20 - (i + 1) * rh
        for j, cell in enumerate(row):
            color = INK
            weight = "normal"
            if j == 3:
                color = GREEN if answers_visible else AMBER
                weight = "bold"
            ax.text(x0 + j * cw + cw / 2, ry + rh / 2, cell, ha="center", va="center",
                    fontsize=12.5, color=color, fontweight=weight)
        if i < 2:
            ax.plot([x0, x0 + w], [ry, ry], color="#dfe7f3", lw=1)
    # column separators
    for j in range(5):
        ax.plot([x0 + j * cw, x0 + j * cw], [y0, y0 + 20 + rh], color="#dfe7f3", lw=1)
    ax.add_patch(mpatches.Rectangle((x0, y0), w, 20 + rh, fill=False, ec="#c9d6ea", lw=1.4))


mini_table(62, "درس خواندن — با پاسخ‌نامه", BLUE, answers_visible=True)
mini_table(4, "امتحان — پاسخ‌ها پنهان!", AMBER, answers_visible=False)

# arrow: study (right) → exam (left), following RTL reading order
ax.annotate("", xy=(37.5, 16), xytext=(58.5, 16),
            arrowprops=dict(arrowstyle="-|>", lw=3, color=INK))
ax.text(48, 20.5, fa("بعد برچسب را"), ha="center", fontsize=13, color=INK)
ax.text(48, 11.5, fa("پنهان می‌کنیم"), ha="center", fontsize=13, color=INK)

plt.tight_layout(pad=0.4)
out = os.path.join(HERE, "supervised_study_exam.png")
plt.savefig(out, bbox_inches="tight", facecolor="white")
print("wrote", out)
