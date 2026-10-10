"""Session 2 — tree anatomy diagram (replaces the AI-generated tree_anatomy.png,
whose "no text" prompt still produced garbled labels).

A single question node, two branches, two leaves — with callout labels naming
گره (Node) / شاخه (Branch) / برگ (Leaf), matching the slide's three definitions.

RUN:  python3 assets/gen_anatomy_diagram.py   (works from anywhere)

Slide-craft rules enforced: Vazirmatn registered from the course slide-theme,
boxes sized from MEASURED text extents, edges anchored to box outlines, callout
leader lines end OUTSIDE the shapes at border points. Eyeball the PNG after regen.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

import arabic_reshaper
from bidi.algorithm import get_display

HERE = os.path.dirname(os.path.abspath(__file__))
COURSE_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "tree_anatomy.png")  # same slot the decks already reference

font_manager.fontManager.addfont(os.path.join(COURSE_ROOT, "slide-theme", "Vazirmatn.ttf"))
plt.rcParams["font.family"] = "Vazirmatn"

BLUE, AMBER, INK = "#1F6FEB", "#E8590C", "#123A6E"
GREY, LEAD = "#5F6B7A", "#8FA3BF"

fig = plt.figure(figsize=(8.0, 6.0), dpi=150)  # 1200x900 px
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.patch.set_facecolor("#EAF3FE")

_renderer = fig.canvas.get_renderer()
_fw, _fh = fig.get_size_inches() * fig.dpi


def fa(s):
    return get_display(arabic_reshaper.reshape(str(s)))


def measure(s, fs, weight="bold"):
    t = ax.text(0.5, 0.5, fa(s), fontsize=fs, fontweight=weight, ha="center", va="center")
    bb = t.get_window_extent(renderer=_renderer)
    t.remove()
    return bb.width / _fw, bb.height / _fh


def border_point(c, hw, hh, toward, gap=0.012):
    dx, dy = toward[0] - c[0], toward[1] - c[1]
    sx = hw / abs(dx) if dx else float("inf")
    sy = hh / abs(dy) if dy else float("inf")
    s = min(sx, sy)
    x, y = c[0] + dx * s, c[1] + dy * s
    L = (dx * dx + dy * dy) ** 0.5
    return x + dx / L * gap, y + dy / L * gap


def node(c, text, fs, kind, color):
    tw, th = measure(text, fs)
    hw, hh = tw / 2 + 0.030, th / 2 + 0.026
    if kind == "q":
        box = FancyBboxPatch((c[0] - hw, c[1] - hh), 2 * hw, 2 * hh,
                             boxstyle="round,pad=0,rounding_size=0.020",
                             facecolor="#FFFFFF", edgecolor=BLUE, linewidth=2.6)
        tc = INK
    else:
        box = FancyBboxPatch((c[0] - hw, c[1] - hh), 2 * hw, 2 * hh,
                             boxstyle="round,pad=0,rounding_size=0.045",
                             facecolor=color, edgecolor=color, linewidth=2.6)
        tc = "#FFFFFF"
    ax.add_patch(box)
    ax.text(c[0], c[1], fa(text), fontsize=fs, fontweight="bold",
            ha="center", va="center", color=tc)
    return c, hw, hh


def edge(parent, child, label, label_color):
    p0 = border_point(parent[0], parent[1], parent[2], child[0])
    p1 = border_point(child[0], child[1], child[2], parent[0])
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=24,
                                 linewidth=2.6, color="#9CC0FF", zorder=1))
    lx, ly = p0[0] + (p1[0] - p0[0]) * 0.25, p0[1] + (p1[1] - p0[1]) * 0.25
    ax.text(lx, ly - 0.006, fa(label), fontsize=22, fontweight="bold",
            ha="center", va="top", color=label_color,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFFFFF", edgecolor="none"),
            zorder=3)
    return (p0[0] + (p1[0] - p0[0]) * 0.55, p0[1] + (p1[1] - p0[1]) * 0.55)


def callout(c, term, en, target, fs=26):
    """Label text with a thin leader line to a border point on the target part."""
    ax.text(c[0], c[1], fa(f"{term} ({en})"), fontsize=fs, fontweight="bold",
            ha="center", va="center", color=INK)
    if len(target) == 3:  # a box: hit its outline
        p = border_point((target[0][0], target[0][1]), target[1], target[2], c, gap=0.004)
    else:                  # a bare point (edge midpoint)
        p = target
    x0, y0 = c
    # start the leader a little toward the label of the text
    ax.plot([x0, p[0]], [y0, p[1]], color=LEAD, lw=1.6, zorder=2)
    ax.add_patch(Circle(p, 0.007, color=LEAD, zorder=2))


root = node((0.34, 0.68), "وزنش زیاد است؟", 27, "q", None)
dog = node((0.56, 0.18), "سگ بزرگ", 29, "leaf", BLUE)
cat = node((0.13, 0.18), "گربه", 29, "leaf", AMBER)

mid_no = edge(root, cat, "نه", GREY)
mid_yes = edge(root, dog, "بله", BLUE)

callout((0.79, 0.88), "گره", "Node", root)
callout((0.79, 0.50), "شاخه", "Branch", mid_yes)
callout((0.79, 0.10), "برگ", "Leaf", dog)

fig.savefig(OUT, dpi=150, facecolor=fig.get_facecolor())
print("wrote", OUT)
