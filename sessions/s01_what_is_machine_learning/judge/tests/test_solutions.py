"""Session 1 judge tests — grades the at-home problems (B1–B4).

Each test prints a friendly, specific verdict and awards points.
Not run directly; imported by run.py.
"""
import json, os
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
EXPECTED = json.load(open(os.path.join(HERE, "..", "data", "expected.json")))
TOTAL_POINTS = 4


def grade(ns):
    """ns: namespace dict from executing the student notebook."""
    results = []  # (passed: bool, points: int, message: str)

    # ---- B1: The Feature Detective (1 pt)
    try:
        ans = ns["B1_good_features"]
        exp = set(EXPECTED["B1_good_features"])
        got = set(str(a).strip().lower() for a in ans)
        if got == exp:
            results.append((True, 1, "PASS: Problem B1 passed (1/1)"))
        else:
            missing, extra = exp - got, got - exp
            hint = []
            if missing:
                hint.append(f"you are missing {sorted(missing)}")
            if extra:
                hint.append(f"'{sorted(extra)[0]}' carries no signal about passing a test — ask: would a NEW student's value of this feature tell you anything?")
            results.append((False, 0, f"FAIL: Problem B1: {' and '.join(hint)}. Re-check which clues actually predict test success."))
    except KeyError:
        results.append((False, 0, "FAIL: Problem B1: variable B1_good_features not found — did you fill in cell B1?"))
    except Exception as e:
        results.append((False, 0, f"FAIL: Problem B1: B1_good_features should be a list of strings ({e})."))

    # ---- B2: Build Your Own Dataset (1 pt)
    try:
        df = ns["B2_animals"]
        if not isinstance(df, pd.DataFrame):
            raise TypeError("B2_animals must be a pandas DataFrame")
        cols = set(df.columns)
        if cols != {"size", "can_fly", "animal"}:
            results.append((False, 0, f"FAIL: Problem B2: columns must be exactly ['size','can_fly','animal'] — you have {sorted(cols)}. In real pipelines, column-name mismatches are the #1 silent bug!"))
        elif len(df) < 4:
            results.append((False, 0, f"FAIL: Problem B2: need at least 4 animals — you have {len(df)}."))
        elif not df["size"].isin(["small", "medium", "large"]).all():
            results.append((False, 0, "FAIL: Problem B2: 'size' values must be 'small', 'medium' or 'large'."))
        elif not df["can_fly"].isin([0, 1]).all():
            results.append((False, 0, "FAIL: Problem B2: 'can_fly' values must be 0 or 1."))
        elif df["animal"].nunique() < 4:
            results.append((False, 0, "FAIL: Problem B2: use 4 DIFFERENT animals — the model needs distinct examples."))
        else:
            results.append((True, 1, "PASS: Problem B2 passed (1/1)"))
    except KeyError:
        results.append((False, 0, "FAIL: Problem B2: variable B2_animals not found — did you fill in cell B2?"))
    except Exception as e:
        results.append((False, 0, f"FAIL: Problem B2: {e}"))

    # ---- B3: The 3 Magic Lines (1 pt)
    try:
        model = ns["B3_model"]
        # check fitted BEFORE probing: an unfitted tree raises NotFittedError at
        # predict time, which would bury the specific help below.
        if not hasattr(model, "tree_"):
            results.append((False, 0, "FAIL: Problem B3: B3_model is not a fitted decision tree — did you call .fit(B3_X, B3_y)?"))
        else:
            pred = model.predict(ns["B3_X"].head(1))  # model must accept its own training feature space
            exp_probe = pd.DataFrame([{c: v for c, v in zip(ns["B3_X"].columns, [1, 0])}])
            got = ns.get("B3_prediction", ...)
            if got is ...:
                results.append((False, 0, "FAIL: Problem B3: B3_prediction is missing — line 3 of the cell asks the model about a medium, non-flying animal."))
            elif str(got) != str(model.predict(exp_probe)[0]):
                results.append((False, 0, "FAIL: Problem B3: B3_prediction must be YOUR model's answer for size_num=1, can_fly=0 — call .predict on that exact case."))
            else:
                results.append((True, 1, "PASS: Problem B3 passed (1/1)"))
    except KeyError as e:
        which = str(e).strip("'")
        if which == "B3_model":
            results.append((False, 0, "FAIL: Problem B3: variable B3_model not found — did you complete cell B3?"))
        else:
            results.append((False, 0, f"FAIL: Problem B3: variable {which} not found — cell B3 defines B3_X, B3_y, B3_model and B3_prediction. Complete the whole cell."))
    except Exception as e:
        results.append((False, 0, f"FAIL: Problem B3: the model could not make a prediction ({e}). Check the 3 magic lines: create, fit, predict."))

    # ---- B4: The Survival Predictor (1 pt)
    try:
        if ns["B4_answer"] is ...:
            results.append((False, 0, "FAIL: Problem B4: the ... placeholders are still there — train your tree (max_depth=3, random_state=42) and put its 0/1 verdict into B4_answer."))
            return results, TOTAL_POINTS
        ans = int(ns["B4_answer"])
        exp = EXPECTED["B4_answer"]
        if ans == exp:
            results.append((True, 1, "PASS: Problem B4 passed (1/1)"))
        else:
            results.append((False, 0, f"FAIL: Problem B4: expected {exp} but got {ans}. Did you train with max_depth=3 and random_state=42, on the same X and y as cell A7?"))
    except KeyError:
        results.append((False, 0, "FAIL: Problem B4: variable B4_answer not found — did you fill in cell B4?"))
    except Exception as e:
        results.append((False, 0, f"FAIL: Problem B4: B4_answer should be 1 or 0 ({e})."))

    return results, TOTAL_POINTS
