"""Session 3 judge tests — grades B1, B2, B3 from the student's namespace."""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
EXPECTED = json.load(open(os.path.join(os.path.dirname(HERE), "data", "expected.json")))


def _close(a, b, tol=1e-6):
    try:
        return abs(float(a) - float(b)) <= tol
    except (TypeError, ValueError):
        return False


def grade(ns):
    results = []

    # ---- B1: The Surprise of Three Bags (1 pt) ----
    b1_vars = ["B1_surprise_a", "B1_surprise_b", "B1_surprise_c"]
    missing = [v for v in b1_vars if v not in ns or ns[v] is None]
    if missing:
        results.append((False, 0, f"FAIL: Problem B1: variable(s) {', '.join(missing)} not found — did you fill in cell B1?"))
    else:
        checks = [
            (_close(ns["B1_surprise_a"], EXPECTED["B1_surprise_a"]), "the pure bag (all one color) has surprise exactly 0"),
            (_close(ns["B1_surprise_b"], EXPECTED["B1_surprise_b"]), "the 5+5 bag is the most mixed two-color bag — surprise 1.0"),
            (_close(ns["B1_surprise_c"], EXPECTED["B1_surprise_c"]), "the 1+9 bag has a dominant color — surprise ≈ 0.47"),
        ]
        fails = [hint for ok, hint in checks if not ok]
        if not fails:
            results.append((True, 1, " PASS: Problem B1 (1/1) — pure = 0, even mix = 1, dominant-color ≈ 0.47. You can measure surprise."))
        else:
            results.append((False, 0, f" FAIL: Problem B1: {'; '.join(fails)}. Call surprise() on each bag — do not type numbers by hand."))

    # ---- B2: The Champion of the Light Box (1 pt) ----
    if "B2_champion" not in ns or not isinstance(ns.get("B2_champion"), str) or not ns["B2_champion"]:
        results.append((False, 0, "FAIL: Problem B2: variable B2_champion not found (or not a word) — did you fill in cell B2?"))
    else:
        champ = ns["B2_champion"].strip()
        gains_ok = all(_close(ns.get(v, -1), EXPECTED[v], tol=1e-4) for v in
                       ("B2_gain_ears_825", "B2_gain_ears_70", "B2_gain_weight_375"))
        if champ == EXPECTED["B2_champion"] and gains_ok:
            results.append((True, 1, " PASS: Problem B2 (1/1) — طول_گوش ≥ 8.25 sorts the light box completely. You derived the machine's second question."))
        elif champ == EXPECTED["B2_champion"] and not gains_ok:
            results.append((False, 0, " FAIL: Problem B2: champion is right, but the three gain numbers do not match — recompute each with gain_light() and keep the printed value."))
        else:
            hint = ("a smaller gain won — the champion's gain equals the WHOLE surprise of the box (0.985)."
                    if ns.get("B2_gain_ears_825", 0) < ns.get("B2_gain_weight_375", 0)
                    else "the champion is the biggest surprise-drop, not the most even split — print both sides of each question and look which one ends up pure.")
            results.append((False, 0, f" FAIL: Problem B2: expected champion \"{EXPECTED['B2_champion']}\", got \"{champ}\". {hint}"))

    # ---- B3: The Titanic Champion + Split Plot (1 pt) ----
    if "B3_champion_feature" not in ns or not ns.get("B3_champion_feature"):
        results.append((False, 0, "FAIL: Problem B3: variable B3_champion_feature not found — did you fill in cell B3?"))
    else:
        feat = str(ns["B3_champion_feature"]).strip()
        gain = ns.get("B3_champion_gain")
        if feat == EXPECTED["B3_champion_feature"] and _close(gain, EXPECTED["B3_champion_gain"], tol=1e-3):
            results.append((True, 1, " PASS: Problem B3 (1/1) — is_female wins with gain 0.214, the same feature you voted for in Session 1. Commit your split plot!"))
        elif feat == EXPECTED["B3_champion_feature"]:
            results.append((False, 0, f" FAIL: Problem B3: champion feature is right, but the gain is off (expected ≈ {EXPECTED['B3_champion_gain']:.3f}, got {gain!r}). Copy the top row of your A5-style leaderboard."))
        else:
            results.append((False, 0, f" FAIL: Problem B3: expected champion \"is_female\", got \"{feat}\". Re-run the leaderboard — the champion's gain should be about triple the runner-up's."))

    return results, 3
