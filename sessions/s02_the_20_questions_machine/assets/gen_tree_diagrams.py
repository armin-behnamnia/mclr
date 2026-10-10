"""Session 2 — polished tree diagrams (plotly twins of notebook cells A1/A2).

Same trees, same thresholds, same data as the notebook (random_state=42);
rendered as presentation-grade diagrams. Notebook keeps its authentic
matplotlib plot_tree outputs; these are the slide versions.

RUN:  python3 assets/gen_tree_diagrams.py      (from anywhere; paths are absolute)

Prereqs: plotly + kaleido v1 (needs the course headless Chrome — the same one
render.sh uses). The script exports BROWSER_PATH itself.

RTL RULE (course-wide): a comparison operator inside Persian text gets mirrored
by the bidi algorithm (≥ renders as ≤). Wrap LTR math fragments in Unicode
bidi isolates: LTR(isolate below) — see the LRI/PDI constants. Every label in
this file uses them; never write a bare ≥/≤ inside Persian text anywhere
(slides, diagrams, notes). Verify the rendered PNG with your eyes after regen.
"""
import glob
import os

import pandas as pd
import plotly.graph_objects as go
from sklearn.tree import DecisionTreeClassifier

HERE = os.path.dirname(os.path.abspath(__file__))

# kaleido v1 drives a real Chrome; point it at the course's chrome-headless-shell
# (same binary render.sh uses). Libraries come from the extracted chrome-libs dir.
if not os.environ.get("BROWSER_PATH"):
    _shells = sorted(glob.glob(os.path.expanduser(
        "~/.cache/puppeteer/chrome-headless-shell/*/chrome-headless-shell-linux64/chrome-headless-shell")))
    if _shells:
        os.environ["BROWSER_PATH"] = _shells[-1]
os.environ.setdefault("LD_LIBRARY_PATH",
                      "/tmp/opencode/chrome-libs/usr/lib/x86_64-linux-gnu")

# RTL fix for plotly/kaleido: bidi isolates do NOT work in this renderer
# (verified: they get ignored and ≥ still mirrors). What works is the LRM mark
# (U+200E) around the math fragment. Different from Marp decks, where the
# browser honors isolates (U+2066..U+2069). Verify visually after regen.
import re

LRM = "‎"  # LEFT-TO-RIGHT MARK


def qlabel(text):
    """Wrap operator+number fragments in LRM so Persian context can't mirror/reorder."""
    return re.sub(r"([≥≤<>]+\s*[\d۰-۹.]+)", lambda m: LRM + m.group(1) + LRM, text)

CLASS_COLORS = {"گربه": "#E8A33D", "سگ بزرگ": "#1F6FEB", "سگ کوچک": "#2D7FF9"}
Q_LINE = "#1F6FEB"


def rounded_rect(x0, y0, x1, y1, r):
    return (f"M {x0+r},{y0} L {x1-r},{y0} Q {x1},{y0} {x1},{y0+r} "
            f"L {x1},{y1-r} Q {x1},{y1} {x1-r},{y1} L {x0+r},{y1} "
            f"Q {x0},{y1} {x0},{y1-r} L {x0},{y0+r} Q {x0},{y0} {x0+r},{y0} Z")


def draw_tree(nodes, edges, out, title=None, width=980, height=560):
    fig = go.Figure()
    for a, b, ans in edges:
        na, nb = nodes[a], nodes[b]
        fig.add_shape(type="line", x0=na["x"], y0=na["y"], x1=nb["x"], y1=nb["y"],
                      line=dict(color="#9CC0FF", width=3))
        mx = na["x"] + 0.45 * (nb["x"] - na["x"])
        my = na["y"] + 0.45 * (nb["y"] - na["y"])
        fig.add_annotation(x=mx, y=my, text=ans, showarrow=False,
                           font=dict(family="Vazirmatn", size=19, color="#E8590C"),
                           bgcolor="#FFFFFF", borderpad=4)
    for n in nodes:
        x0, x1 = n["x"] - n["w"] / 2, n["x"] + n["w"] / 2
        y0, y1 = n["y"] - n["h"] / 2, n["y"] + n["h"] / 2
        if n["kind"] == "q":
            fig.add_shape(type="path", path=rounded_rect(x0, y0, x1, y1, 0.035),
                          fillcolor="#FFFFFF", line=dict(color=Q_LINE, width=3), layer="below")
            size, color = 19, "#1A3A66"
        else:
            fig.add_shape(type="path", path=rounded_rect(x0, y0, x1, y1, 0.07),
                          fillcolor=CLASS_COLORS[n["label"]] + "33",
                          line=dict(color=CLASS_COLORS[n["label"]], width=3), layer="below")
            size, color = 21, "#1D4E89"
        fig.add_annotation(x=n["x"], y=n["y"], text=n["label"], showarrow=False,
                           font=dict(family="Vazirmatn", size=size, color=color))
    fig.update_xaxes(range=[-0.02, 1.02], visible=False)
    fig.update_yaxes(range=[0, 1.03], visible=False)
    fig.update_layout(width=width, height=height,
                      paper_bgcolor="#EAF3FE", plot_bgcolor="#EAF3FE",
                      margin=dict(l=10, r=10, t=10, b=10), font=dict(family="Vazirmatn"))
    fig.write_image(out, scale=2)
    print("wrote", out)


animals = pd.DataFrame({
    "وزن": [4.5, 3.0, 6.0, 5.0, 22, 32, 28, 38, 4, 3.5, 4.5],
    "طول_گوش": [5, 7, 4, 6, 9, 12, 11, 13, 11, 9.5, 10],
    "گروه": ["گربه"] * 4 + ["سگ بزرگ"] * 4 + ["سگ کوچک"] * 3})
X, y = animals[["وزن", "طول_گوش"]], animals["گروه"]

# depth 1 (mirrors cell A1): وزن >= 14 -> right: سگ (small dogs lumped with cats by depth-1 classes)
# NOTE: depth-1 tree on 3 classes predicts گربه on the light side (majority) and سگ بزرگ on heavy side.
nodes_d1 = [
    dict(x=0.5, y=0.78, w=0.30, h=0.16, label=qlabel("وزن ≥ ۱۴؟"), kind="q"),
    dict(x=0.22, y=0.25, w=0.24, h=0.17, label="گربه", kind="leaf"),
    dict(x=0.78, y=0.25, w=0.26, h=0.17, label="سگ بزرگ", kind="leaf"),
]
edges_d1 = [(0, 1, "نه"), (0, 2, "بله")]
draw_tree(nodes_d1, edges_d1, os.path.join(HERE, "decision_tree_s02_d1.png"), width=880, height=520)

# depth 2 (mirrors cell A2): root وزن>=14; heavy side -> سگ بزرگ; light side -> گوش >= 8.25?
nodes_d2 = [
    dict(x=0.5,  y=0.85, w=0.30, h=0.15, label=qlabel("وزن ≥ ۱۴؟"), kind="q"),
    dict(x=0.30, y=0.44, w=0.30, h=0.15, label=qlabel("گوش ≥ ۸.۲۵؟"), kind="q"),
    dict(x=0.72, y=0.44, w=0.26, h=0.17, label="سگ بزرگ", kind="leaf"),
    dict(x=0.14, y=0.10, w=0.24, h=0.17, label="گربه", kind="leaf"),
    dict(x=0.50, y=0.10, w=0.27, h=0.17, label="سگ کوچک", kind="leaf"),
]
edges_d2 = [(0, 1, "نه"), (0, 2, "بله"), (1, 3, "نه"), (1, 4, "بله")]
draw_tree(nodes_d2, edges_d2, os.path.join(HERE, "decision_tree_s02_d2.png"))
