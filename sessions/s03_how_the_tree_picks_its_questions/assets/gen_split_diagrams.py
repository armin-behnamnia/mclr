"""Session 3 — polished split-score diagrams (plotly twins of notebook cells A1/A3/A5).

Same animals table, same thresholds, same surprise numbers (base-2 bits) as the
notebook (random_state-independent: everything derives from counts). The notebook
keeps its authentic printed tables; these are the slide versions.

RUN:  python3 assets/gen_split_diagrams.py    (works from anywhere)

Prereqs: plotly + kaleido v1 (this script locates the course headless Chrome and
exports BROWSER_PATH itself). RTL rule: wrap ≥/≤ math fragments in LRM marks —
isolates (U+2066/2069) are IGNORED by this renderer (verified); LRM works.
"""
import glob
import os

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import entropy as _ent

LRM = "\u200e"  # LEFT-TO-RIGHT MARK — wrap ≥/≤ + number runs in Persian text
import re as _re


def rtl(text):
    if isinstance(text, str):
        return _re.sub(r"([≥≤<>]+[\s\d۰-۹.٫]+)", lambda m: LRM + m.group(1) + LRM, text)
    return text


CANVAS = "#EAF3FE"
Q_LINE = "#1F6FEB"
CAT, BIG, SMALL = "#E8A33D", "#1F6FEB", "#2D7FF9"
CLASS_COLORS = {"گربه": CAT, "سگ بزرگ": BIG, "سگ کوچک": SMALL}

HERE = os.path.dirname(os.path.abspath(__file__))
if not os.environ.get("BROWSER_PATH"):
    _shells = sorted(glob.glob(os.path.expanduser(
        "~/.cache/puppeteer/chrome-headless-shell/*/chrome-headless-shell-linux64/chrome-headless-shell")))
    if _shells:
        os.environ["BROWSER_PATH"] = _shells[-1]
os.environ.setdefault("LD_LIBRARY_PATH",
                      "/tmp/opencode/chrome-libs/usr/lib/x86_64-linux-gnu")


def surprise(labels):
    _, counts = np.unique(labels, return_counts=True)
    return float(_ent(counts, base=2))


animals = pd.DataFrame({
    "وزن": [4.5, 3.0, 6.0, 5.0, 22, 32, 28, 38, 4, 3.5, 4.5],
    "طول_گوش": [5, 7, 4, 6, 9, 12, 11, 13, 11, 9.5, 10],
    "گروه": ["گربه"] * 4 + ["سگ بزرگ"] * 4 + ["سگ کوچک"] * 3})
y = animals["گروه"]


def label_of(gr):
    return f"{dict(gr)}".replace("'", "")


def ball_radius(w, h, total):
    """Radius the balls would get in a box of size (w x h) holding `total` balls."""
    import math
    per_row = min(max(1, math.ceil(math.sqrt(total * (w / h) * 1.4))), total)
    rows = math.ceil(total / per_row)
    gx = (w - 2 * 0.08 * w) / per_row
    gy = (h - 0.22 * h - 0.06 * h) / rows
    return 0.42 * min(gx, gy)


def draw_box(fig, x0, y0, x1, y1, groups, title, subtitle, tsize=20, ssize=17, r=None):
    """Draw a box showing each animal as a colored ball.

    Balls MUST stay inside the box: grid spacing is derived from the box size
    and ball count (never hard-coded). Pass `r` (from ball_radius of the fullest
    box) so ball size stays CONSTANT across all boxes of one figure — a 1-ball
    box must not grow a giant ball. Verify visually after regen.
    """
    import math
    fig.add_shape(type="rect", x0=x0, y0=y0, x1=x1, y1=y1,
                  fillcolor="#FFFFFF", line=dict(color="#9CC0FF", width=3), layer="below")
    names = [n for n, k in groups.items() for _ in range(k)]
    total = len(names)
    w, h = x1 - x0, y1 - y0
    # choose columns so balls form the widest tidy grid that fits
    per_row = max(1, math.ceil(math.sqrt(total * (w / h) * 1.4)))
    per_row = min(per_row, total)
    rows = math.ceil(total / per_row)
    top_pad, side_pad = 0.22 * h, 0.08 * w   # reserve title space at the top
    gx = (w - 2 * side_pad) / per_row        # per-ball column width
    gy = (h - top_pad - 0.06 * h) / rows     # per-ball row height
    if r is None:
        r = 0.42 * min(gx, gy)               # ball radius, never overflows
    for i, name in enumerate(names):
        rr, c = divmod(i, per_row)
        bx = x0 + side_pad + gx * (c + 0.5)
        by = y1 - top_pad - gy * (rr + 0.5)
        fig.add_shape(type="circle", x0=bx - r, y0=by - r, x1=bx + r, y1=by + r,
                      fillcolor=CLASS_COLORS[name], line=dict(color="#FFFFFF", width=2), layer="below")
    fig.add_annotation(x=(x0 + x1) / 2, y=y1 + 0.045, text=title, showarrow=False,
                       font=dict(family="Vazirmatn", size=tsize, color="#1A3A66"))
    fig.add_annotation(x=(x0 + x1) / 2, y=y0 - 0.05, text=subtitle, showarrow=False,
                       font=dict(family="Vazirmatn", size=ssize, color="#3C4043"))


def finish(fig, out, width=980, height=560):
    fig.update_xaxes(range=[0, 1], visible=False)
    fig.update_yaxes(range=[0, 1], visible=False)
    fig.update_layout(width=width, height=height, paper_bgcolor=CANVAS, plot_bgcolor=CANVAS,
                      margin=dict(l=10, r=10, t=10, b=10), font=dict(family="Vazirmatn"))
    fig.write_image(out, scale=2)
    print("wrote", out)


# ---------------------------------------------------------------- diagram 1
# A bad question (ear >= 4.5): box splits, both sides stay mixed
fig = go.Figure()
fig.add_annotation(x=0.5, y=0.97, text=rtl("سؤالِ بیهوده: طول_گوش ≥ ۴٫۵؟"), showarrow=False,
                   font=dict(family="Vazirmatn", size=24, color="#B03030"))
root_counts = y.value_counts().to_dict()
RHO = ball_radius(0.36, 0.28, sum(root_counts.values()))  # same size everywhere in this figure
draw_box(fig, 0.06, 0.62, 0.42, 0.90, root_counts, "جعبهٔ اصلی", "غافلگیری ۱٫۵۷", r=RHO)
L = y[animals["طول_گوش"] < 4.5].value_counts().to_dict()
R = y[animals["طول_گوش"] >= 4.5].value_counts().to_dict()
draw_box(fig, 0.06, 0.14, 0.42, 0.42, L, "درِ نه (۱ حیوان)", "خالص! ولی فقط ۱ حیوان", r=RHO)
draw_box(fig, 0.56, 0.14, 0.94, 0.42, R, "درِ بله (۱۰ حیوان)", "هنوز همان قاطی — ۱۰ تا از ۱۱", r=RHO)
fig.add_annotation(x=0.49, y=0.52, text="→", showarrow=False,
                   font=dict(size=40, color="#B03030"))
finish(fig, os.path.join(HERE, "split_bad.png"), width=880, height=560)

# ---------------------------------------------------------------- diagram 2
# The champion question (weight >= 14): heavy side pure
fig = go.Figure()
fig.add_annotation(x=0.5, y=0.97, text=rtl("سؤالِ قهرمان: وزن ≥ ۱۴؟"), showarrow=False,
                   font=dict(family="Vazirmatn", size=24, color="#1F6FEB"))
draw_box(fig, 0.06, 0.62, 0.42, 0.90, root_counts, "جعبهٔ اصلی", "غافلگیری ۱٫۵۷", r=RHO)
L = y[animals["وزن"] < 14].value_counts().to_dict()
R = y[animals["وزن"] >= 14].value_counts().to_dict()
draw_box(fig, 0.06, 0.14, 0.42, 0.42, L, "درِ نه (۷ حیوان)", "کمی قاطی", r=RHO)
draw_box(fig, 0.56, 0.14, 0.94, 0.42, R, "درِ بله (۴ حیوان)", "خالص!", r=RHO)
fig.add_annotation(x=0.49, y=0.52, text="→", showarrow=False,
                   font=dict(size=40, color="#1F6FEB"))
finish(fig, os.path.join(HERE, "split_champion_tree.png"), width=880, height=560)

# ---------------------------------------------------------------- diagram 3
# The leaderboard (score card) — animals
rows = []
def gain_of(feature, th):
    left = y[animals[feature] < th]
    right = y[animals[feature] >= th]
    if len(left) == 0 or len(right) == 0:
        return 0.0
    after = (len(left) * surprise(left) + len(right) * surprise(right)) / len(y)
    return surprise(y) - after

for feature, th in [("وزن", 14), ("طول_گوش", 8.25), ("وزن", 30), ("طول_گوش", 4.5), ("وزن", 3.25)]:
    rows.append((rtl(f"{feature} ≥ {th}"), gain_of(feature, th)))
rows.sort(key=lambda r: -r[1])

fig = go.Figure()
labels = [r[0] for r in rows]
gains = [r[1] for r in rows]
colors = ["#1F6FEB" if i == 0 else "#A9D0FF" for i in range(len(rows))]
fig.add_bar(x=gains[::-1], y=labels[::-1], orientation="h",
            marker_color=colors[::-1], text=[f"{g:.2f}" for g in gains[::-1]],
            textposition="outside", textfont=dict(family="Vazirmatn", size=19, color="#1A3A66"))
fig.update_xaxes(range=[0, 1.15], visible=False)
fig.update_yaxes(tickfont=dict(family="Vazirmatn", size=20, color="#3C4043"))
fig.add_annotation(x=0.5, y=1.06, xref="paper", yref="paper",
                   text="بهرهٔ هر سؤال — قهرمان بالا", showarrow=False,
                   font=dict(family="Vazirmatn", size=23, color="#1A3A66"))
fig.update_layout(width=880, height=460, paper_bgcolor=CANVAS, plot_bgcolor=CANVAS,
                  margin=dict(l=10, r=10, t=40, b=10), font=dict(family="Vazirmatn"),
                  showlegend=False)
fig.write_image(os.path.join(HERE, "leaderboard_animals.png"), scale=2)
print("wrote", os.path.join(HERE, "leaderboard_animals.png"))

# ---------------------------------------------------------------- diagram 4
# Titanic champion: is_female before/after
SURV, NOT_SURV = "#4A8F6C", "#C0C8D0"


def draw_box_counts(fig, x0, y0, x1, y1, groups, colors, title, subtitle, tsize=18, ssize=16, r=None):
    """Same ball-grid geometry as draw_box, with caller-provided colors."""
    import math
    fig.add_shape(type="rect", x0=x0, y0=y0, x1=x1, y1=y1,
                  fillcolor="#FFFFFF", line=dict(color="#9CC0FF", width=3), layer="below")
    names = [n for n, k in groups.items() for _ in range(k)]
    total = len(names)
    w, h = x1 - x0, y1 - y0
    per_row = max(1, math.ceil(math.sqrt(total * (w / h) * 1.4)))
    per_row = min(per_row, total)
    rows = math.ceil(total / per_row)
    top_pad, side_pad = 0.22 * h, 0.08 * w
    gx = (w - 2 * side_pad) / per_row
    gy = (h - top_pad - 0.06 * h) / rows
    if r is None:
        r = 0.42 * min(gx, gy)
    for i, name in enumerate(names):
        rr, c = divmod(i, per_row)
        bx = x0 + side_pad + gx * (c + 0.5)
        by = y1 - top_pad - gy * (rr + 0.5)
        fig.add_shape(type="circle", x0=bx - r, y0=by - r, x1=bx + r, y1=by + r,
                      fillcolor=colors[name], line=dict(color="#FFFFFF", width=2), layer="below")
    fig.add_annotation(x=(x0 + x1) / 2, y=y1 + 0.045, text=title, showarrow=False,
                       font=dict(family="Vazirmatn", size=tsize, color="#1A3A66"))
    fig.add_annotation(x=(x0 + x1) / 2, y=y0 - 0.05, text=subtitle, showarrow=False,
                       font=dict(family="Vazirmatn", size=ssize, color="#3C4043"))


fig = go.Figure()
fig.add_annotation(x=0.5, y=0.97, text="قهرمانِ تایتانیک: is_female؟", showarrow=False,
                   font=dict(family="Vazirmatn", size=23, color="#1F6FEB"))
RHO_T = ball_radius(0.36, 0.28, 7)
draw_box_counts(fig, 0.06, 0.62, 0.42, 0.90,
                {"s": 3, "n": 4}, {"s": SURV, "n": NOT_SURV},
                "جعبهٔ کامل (۷۱۲)", "غافلگیری ۰٫۹۷", r=RHO_T)
draw_box_counts(fig, 0.06, 0.14, 0.42, 0.42,
                {"s": 1, "n": 3}, {"s": SURV, "n": NOT_SURV},
                "مردها (۴۵۳) — ۲۱٪ زنده", "نسبتاً یک‌رنگ", r=RHO_T)
draw_box_counts(fig, 0.56, 0.14, 0.94, 0.42,
                {"s": 3, "n": 1}, {"s": SURV, "n": NOT_SURV},
                "زن‌ها (۲۵۹) — ۷۵٪ زنده", "نسبتاً یک‌رنگ", r=RHO_T)
fig.add_annotation(x=0.5, y=0.015,
                   text=rtl("توپ‌ها نمادین‌اند: هر توپ ≈ ۱۰۰ مسافر؛ نسبت‌ها واقعی"),
                   showarrow=False, font=dict(family="Vazirmatn", size=15, color="#5F6368"))
fig.add_annotation(x=0.49, y=0.52, text="→", showarrow=False,
                   font=dict(size=40, color="#1F6FEB"))
finish(fig, os.path.join(HERE, "titanic_champion.png"), width=880, height=560)
