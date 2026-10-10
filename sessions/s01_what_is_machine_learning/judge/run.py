#!/usr/bin/env python3
"""Session 1 judge — grades the at-home problems of a student notebook.

Usage:  python judge/run.py <student_notebook.ipynb>

Executes the notebook, then grades variables B1–B4. Prints a friendly report.
Exits 0 if all points earned, 1 otherwise. Never crashes on empty/broken
submissions — reports what it can.
"""
import json, os, sys, io, contextlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "tests"))
import test_solutions  # noqa: E402


def load_namespace(nb_path):
    """Execute all code cells of the notebook and return the final namespace."""
    with open(nb_path, encoding="utf-8") as f:
        nb = json.load(f)
    cells = nb.get("cells", [])
    if not isinstance(cells, list):
        raise ValueError("no cells list found")
    ns = {}
    for i, cell in enumerate(cells):
        if not isinstance(cell, dict) or cell.get("cell_type") != "code":
            continue
        src = "".join(cell.get("source", ""))
        # strip notebook magics and shell lines — safe for pure-python grading
        src = "\n".join(l for l in src.splitlines()
                        if not l.strip().startswith(("%", "!")))
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(src, f"<cell {i}>", "exec"), ns)
        except Exception:
            pass  # a broken cell must not sink the whole grading
    return ns


def main():
    if len(sys.argv) < 2:
        print("Usage: python judge/run.py <student_notebook.ipynb>")
        sys.exit(1)
    nb_path = sys.argv[1]
    if not os.path.exists(nb_path):
        print(f"X Cannot find notebook: {nb_path}")
        sys.exit(1)

    try:
        ns = load_namespace(nb_path)
    except Exception:
        print("=" * 52)
        print("  Session 1 Judge — At-Home Problems")
        print("=" * 52)
        print("X This file is not a readable notebook (.ipynb).")
        print("  Re-download your notebook (File > Download) and try again,")
        print("  or ask your teacher for help.")
        sys.exit(1)
    results, total = test_solutions.grade(ns)

    print("=" * 52)
    print("  Session 1 Judge — At-Home Problems")
    print("=" * 52)
    for passed, pts, msg in results:
        print(msg)
    score = sum(pts for _, pts, _ in results)
    print("-" * 52)
    if score == total:
        print(f"  SCORE: {score}/{total} — perfect! Ship it: commit your notebook")
    elif score > 0:
        print(f"  SCORE: {score}/{total} — good progress! Re-read the X hints above and retry.")
    else:
        print(f"  SCORE: {score}/{total} — start from cell B1 and work down. You can do this!")
    print("=" * 52)
    sys.exit(0 if score == total else 1)


if __name__ == "__main__":
    main()
