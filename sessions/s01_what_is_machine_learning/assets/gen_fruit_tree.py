"""Session 1 — fruit decision map diagram (slide twin of the Segment B fruit game).

The hand map the class builds: red? apple / not red, long? banana / else grape.

RUN:  python3 assets/gen_fruit_tree.py   (works from anywhere)

Diagram rules enforced here (slide-craft knowledge):
- Font: Vazirmatn, registered from the course root slide-theme/ copy — SAME font
  as the slide theme. Persian shaping via fa().
- Every box is SIZED FROM THE MEASURED TEXT (renderer extents), never eyeballed —
  text can never touch or cross a border.
- Arrows connect box OUTLINES: endpoints are computed rect-border intersections
  with a small outward gap; node positions keep clear corridors so no edge
  crosses a box.
- Minimum readable sizes adjusted for projection: question text 24pt-equiv,
  answers 26pt-equiv at this canvas — verify the PNG with your eyes after regen.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

import arabic_reshaper
from bidi.algorithm import get_display

HERE = os.path.dirname(os.path.abspath(__file__))
COURSE_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "fruit_tree.png")

font_manager.fontManager.addfont(os.path.join(COURSE_ROOT, "slide-theme", "Vazirmatn.ttf"))
plt.rcParams["font.family"] = "Vazirmatn"

BLUE, INK = "#1F6FEB", "#123A6E"
GREY = "#5F6B7A"

fig = plt.figure(figsize=(11.2, 7.0), dpi=150)  # 1680x1050 px
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.patch.set_facecolor("#EAF3FE")

_renderer = fig.canvas.get_renderer()
_fw_in, _fh_in = fig.get_size_inches() * fig.dpi


def fa(s):
    return get_display(arabic_reshaper.reshape(str(s)))


def measure(s, fs, weight="normal"):
    """Text size as a fraction of the canvas (w, h)."""
    t = ax.text(0.5, 0.5, fa(s), fontsize=fs, fontweight=weight, ha="center", va="center")
    bb = t.get_window_extent(renderer=_renderer)
    t.remove()
    return bb.width / _fw_in, bb.height / _fh_in


def border_point(c, hw, hh, toward, gap=0.012):
    """Point on the rect outline in the direction of `toward`, plus an outward gap."""
    dx, dy = toward[0] - c[0], toward[1] - c[1]
    sx = hw / abs(dx) if dx else float("inf")
    sy = hh / abs(dy) if dy else float("inf")
    s = min(sx, sy)
    x, y = c[0] + dx * s, c[1] + dy * s
    length = (dx * dx + dy * dy) ** 0.5
    return x + dx / length * gap, y + dy / length * gap


def node(c, text, fs, kind):
    """A box sized to its measured text; returns (center, half_w, half_h)."""
    weight = "bold"
    tw, th = measure(text, fs, weight)
    pad_x, pad_y = 0.030, 0.028
    hw, hh = tw / 2 + pad_x, th / 2 + pad_y
    if kind == "q":
        box = FancyBboxPatch((c[0] - hw, c[1] - hh), 2 * hw, 2 * hh,
                             boxstyle="round,pad=0,rounding_size=0.020",
                             facecolor="#FFFFFF", edgecolor=BLUE, linewidth=2.6)
        color = INK
    else:  # answer pill
        box = FancyBboxPatch((c[0] - hw, c[1] - hh), 2 * hw, 2 * hh,
                             boxstyle="round,pad=0,rounding_size=0.045",
                             facecolor=BLUE, edgecolor=BLUE, linewidth=2.6)
        color = "#FFFFFF"
    ax.add_patch(box)
    ax.text(c[0], c[1], fa(text), fontsize=fs, fontweight=weight,
            ha="center", va="center", color=color)
    return c, hw, hh


def edge(parent, child, label, label_color):
    """Arrow from parent outline to child outline + a chip label near the parent."""
    p0 = border_point(parent[0], parent[1], parent[2], child[0])
    p1 = border_point(child[0], child[1], child[2], parent[0])
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=26,
                                 linewidth=2.8, color="#9CC0FF", zorder=1))
    # label chip near the parent endpoint
    lx, ly = p0[0] + (p1[0] - p0[0]) * 0.22, p0[1] + (p1[1] - p0[1]) * 0.22
    ax.text(lx, ly - 0.008, fa(label), fontsize=21, fontweight="bold",
            ha="center", va="top", color=label_color,
            bbox=dict(boxstyle="round,pad=0.32", facecolor="#FFFFFF",
                      edgecolor="none"), zorder=3)


# layout — corridors kept clear so no edge crosses any box
root = node((0.50, 0.80), "رنگش قرمز است؟", 26, "q")
apple = node((0.16, 0.42), "سیب", 30, "leaf")
q2 = node((0.76, 0.50), "اندازهاش دراز است؟", 26, "q")
banana = node((0.60, 0.13), "موز", 30, "leaf")
grape = node((0.89, 0.13), "انگور", 30, "leaf")

edge(root, apple, "بله", BLUE)
edge(root, q2, "نه", GREY)
edge(q2, banana, "بله", BLUE)
edge(q2, grape, "نه", GREY)

fig.savefig(OUT, dpi=150, facecolor=fig.get_facecolor())
print("wrote", OUT)
