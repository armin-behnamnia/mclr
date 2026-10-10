"""Session 2 judge tests — grades B1, B2, B3 from the student's namespace."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
EXPECTED = json.load(open(os.path.join(os.path.dirname(HERE), "data", "expected.json")))


def grade(ns):
    results = []

    # ---- B1: The Leaf Counter (1 pt) ----
    if "B1_num_questions" not in ns or "B1_num_leaves" not in ns:
        if "B1_model" not in ns:
            results.append((False, 0, "FAIL: Problem B1: variables B1_num_questions / B1_num_leaves not found — did you fill in cell B1?"))
        else:
            results.append((False, 0, "FAIL: Problem B1: you trained the model but forgot to fill B1_num_questions and B1_num_leaves with numbers."))
    else:
        q, l = ns["B1_num_questions"], ns["B1_num_leaves"]
        ok_q = q == EXPECTED["B1_num_questions"]
        ok_l = l == EXPECTED["B1_num_leaves"]
        if ok_q and ok_l:
            results.append((True, 1, " PASS: Problem B1 (1/1) — 2 questions, 3 leaves. You can read a tree's shape."))
        elif not ok_q and not ok_l:
            hint = "4 leaves is the MAXIMUM for depth 2 — count THIS tree's actual rooms (two paths can share a room)." if l == 4 else "Re-trace each animal's path on the tree picture."
            results.append((False, 0, f" FAIL: Problem B1: expected questions={EXPECTED['B1_num_questions']}, leaves={EXPECTED['B1_num_leaves']}, got {q} and {l}. {hint}"))
        elif not ok_q:
            results.append((False, 0, f" FAIL: Problem B1: expected {EXPECTED['B1_num_questions']} questions (root to deepest leaf), got {q}. Check yourself with B1_model.get_depth() if you built the model."))
        else:
            results.append((False, 0, f" FAIL: Problem B1: expected {EXPECTED['B1_num_leaves']} leaves, got {l}. Check yourself with B1_model.get_n_leaves() if you built the model."))

    # ---- B2: The Elephant's Room (1 pt) ----
    if "B2_elephant_room" not in ns or not isinstance(ns.get("B2_elephant_room"), str) or not ns["B2_elephant_room"]:
        results.append((False, 0, "FAIL: Problem B2: variable B2_elephant_room not found (or not a word) — did you fill in cell B2?"))
    else:
        ans = ns["B2_elephant_room"].strip()
        if ans == EXPECTED["B2_elephant_room"]:
            results.append((True, 1, " PASS: Problem B2 (1/1) — the elephant gets the big-dog room. A leaf says one word for everything that reaches it."))
        else:
            results.append((False, 0, f" FAIL: Problem B2: expected \"{EXPECTED['B2_elephant_room']}\", got \"{ans}\". Trace the path: the elephant answers only ONE question — 3000 > 14 sends it straight into a leaf. The ear question (8.25) is only asked on the LIGHT side. Which room did it land in? (Copy the exact string from model.predict, don't type by hand.)"))

    # ---- B3: The Smallest Perfect Depth (1 pt) ----
    if "B3_min_depth" not in ns:
        results.append((False, 0, "FAIL: Problem B3: variable B3_min_depth not found — did you fill in cell B3?"))
    else:
        ans = ns["B3_min_depth"]
        if ans == EXPECTED["B3_min_depth"]:
            results.append((True, 1, " PASS: Problem B3 (1/1) — depth 2 is the smallest perfect tree. One question wasn't enough; two is exactly enough."))
        elif ans in (1,):
            results.append((False, 0, " FAIL: Problem B3: got 1 — at depth 1 the small dogs all land in the cat room. Run the loop and print the accuracy at each depth."))
        elif ans in (3, 4, 5):
            results.append((False, 0, " FAIL: Problem B3: got %d — that depth IS perfect, but it's not the SMALLEST one. The loop breaks at the first perfect depth; read it again." % ans))
        else:
            results.append((False, 0, f" FAIL: Problem B3: expected {EXPECTED['B3_min_depth']}, got {ans!r}. The loop stops at the first depth where ALL 11 animals are correct — complete the TODO condition in cell B3 (the hint line above the TODO is the condition)."))

    return results, 3
