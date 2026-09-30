"""Generate the student and solution notebooks for Session 2.

Run:  python build_notebooks.py
Outputs: notebook/s02_notebook.ipynb (student)
         notebook/s02_notebook_solution.ipynb (instructor)
"""
import json, os, uuid


def md(src):
    return {"cell_type": "markdown", "id": uuid.uuid4().hex[:8],
            "metadata": {}, "source": src}


def code(src):
    return {"cell_type": "code", "id": uuid.uuid4().hex[:8],
            "execution_count": None, "metadata": {}, "outputs": [], "source": src}


def nb(cells):
    return {
        "nbformat": 4, "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.10"},
        },
        "cells": cells,
    }


def write(path, cells):
    with open(path, "w") as f:
        json.dump(nb(cells), f, indent=1, ensure_ascii=False)
    print("wrote", path)


HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- setup cell
SETUP = """\
# COURSE SETUP — identical in every session. Just run it. (5 seconds)
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
import arabic_reshaper
from bidi.algorithm import get_display

def fa(text):
    # Persian text for matplotlib: shapes + orders it correctly
    return get_display(arabic_reshaper.reshape(str(text)))

plt.rcParams["figure.figsize"] = (8, 4)
print("Setup OK — let's build some AI.")
"""

# ---------------------------------------------------------------- shared data
# The 11 animals from Session 1's animal game + 3 small dogs. Same numbers,
# same story: the puppy that broke the one-question machine is IN this
# table as a small dog — so the depth-2 tree can learn to fix its own mistake.
ANIMALS = """\
animals = pd.DataFrame({
    "وزن": [4.5, 3.0, 6.0, 5.0,   22, 32, 28, 38,   4, 3.5, 4.5],
    "طول_گوش": [5, 7, 4, 6,        9, 12, 11, 13,    11, 9.5, 10],
    "گروه": ["گربه", "گربه", "گربه", "گربه",
             "سگ بزرگ", "سگ بزرگ", "سگ بزرگ", "سگ بزرگ",
             "سگ کوچک", "سگ کوچک", "سگ کوچک"],
}, index=["پرشین", "سیامی", "گره‌فیلد", "شارتز",
          "بولداگ", "آلمانی", "گلدن", "دابلمان",
          "پودل", "یورکشایر", "پاپیلون"])
X = animals[["وزن", "طول_گوش"]]
y = animals["گروه"]
"""

# ---------------------------------------------------------------- PART 0 (hook)
PART0_MD = """\
# PART 0 — نمایش: ماشین بازیِ ۲۰ سؤالی را انجام می‌دهد

جلسهٔ قبل، ماشین با **یک سؤال** بازی کرد و توله‌سگ را گربه گفت.
حالا اجازه بدهیم **دو سؤال** بپرسد.
"""

PART0_CODE = """\
# دمو: یک سؤال در برابر دو سؤال — توله‌سگ نجات پیدا می‌کند؟
""" + ANIMALS + """\
# ماشینِ جلسهٔ ۱: فقط ۱ سؤال (عمق ۱)
one_q = DecisionTreeClassifier(max_depth=1, random_state=42).fit(X, y)

# ماشینِ امروز: ۲ سؤال (عمق ۲)
two_q = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)

# همان دشمن قدیمی: توله‌سگ (۲ کیلو، گوش بلند — سگ کوچک است!)
puppy = pd.DataFrame({"وزن": [2], "طول_گوش": [10]})
print("یک سؤال:  توله‌سگ ←", one_q.predict(puppy[X.columns])[0])
print("دو سؤال:  توله‌سگ ←", two_q.predict(puppy[X.columns])[0])

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
for ax, model, title in [(axes[0], one_q, "عمق ۱ — فقط یک سؤال"),
                         (axes[1], two_q, "عمق ۲ — دو سؤال")]:
    plot_tree(model, feature_names=[fa(c) for c in X.columns],
              class_names=[fa(c) for c in sorted(y.unique())],
              filled=True, fontsize=9, impurity=False, ax=ax)
    ax.set_title(fa(title))
plt.tight_layout(); plt.show()
"""

# ---------------------------------------------------------------- PART A
A_MD_1 = """\
## A1 — بازی خودمان، این بار با چشم ماشین

همان حیوانات همیشگی. ماشینِ جلسهٔ ۱ فقط **یک سؤال** می‌پرسید:
«وزن بیشتر از ۱۴؟» — همان خطِ قرمز. حالا کل بازی را می‌بینیم.
"""

A_CODE_1 = """\
# A1 — درختِ تک‌سؤالی: خطِ قرمزِ جلسهٔ ۱، به شکل درخت
""" + ANIMALS + """\
model = DecisionTreeClassifier(max_depth=1, random_state=42).fit(X, y)
plt.figure(figsize=(8, 4))
plot_tree(model, feature_names=[fa(c) for c in X.columns],
          class_names=[fa(c) for c in sorted(y.unique())],
          filled=True, fontsize=10, impurity=False)
plt.title(fa("یک سؤال، دو در، دو حکم"))
plt.show()
# خطِ قرمزِ جلسهٔ ۱ و این تصویر، یکی هستند — فقط شکلِ نمایششان فرق دارد.
"""

A_MD_2 = """\
## A2 — ماشین با دو سؤال بازی می‌کند

سه گروه داریم: گربه، سگ بزرگ، سگ کوچک. یک سؤال برای سه گروه کافی نیست.
"""

A_CODE_2 = """\
# A2 — درختِ دو سؤالی: سؤال اول، سؤال دوم، سه اتاق نهایی
""" + ANIMALS + """\
model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)
plt.figure(figsize=(12, 6))
plot_tree(model, feature_names=[fa(c) for c in X.columns],
          class_names=[fa(c) for c in sorted(y.unique())],
          filled=True, fontsize=10, impurity=False)
plt.title(fa("دو سؤال = سه اتاق درست"))
plt.show()
"""

A_MD_3 = """\
## A3 — درخت را بخوان: مسیر هر حیوان

قانون بازی: از بالای درخت شروع کن، به جوابِ هر سؤال، دنبالِ درِ مناسب را برو.
در آخرین اتاق (برگ)، حکم گفته می‌شود.
"""

A_CODE_3 = """\
# A3 — مسیر چند حیوان را دنبال کن. قبل از اجرا حدس بزن، بعد چک کن!
""" + ANIMALS + """\
model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)

visitors = pd.DataFrame({
    "وزن": [35, 2, 3000],
    "طول_گوش": [10, 10, 20],
}, index=["گرگ", "توله‌سگ", "فیل"])

answers = model.predict(visitors[X.columns])
for name, ans in zip(visitors.index, answers):
    print(f"  {name:10} ← {ans}")

# فیل هم از همین راهروها رد می‌شود و به اتاقِ «سگ بزرگ» می‌رسد.
# برگ همیشه فقط یک حکم می‌گوید — برای هر کسی که به آن برسد.
"""

A_MD_4 = """\
## A4 — پیچ عمق: چند سؤال اجازه داریم؟

`max_depth` یعنی حداکثر تعداد سؤالی که ماشین اجازه دارد بپرسد.
با ۱ سؤال توله‌سگ گربه می‌شود. با ۲ سؤال درست می‌شود. خودت ببین.
"""

A_CODE_4 = """\
# A4 — عمق ۱ در برابر عمق ۲: اشتباهِ توله‌سگ و درمانش
""" + ANIMALS + """\
puppy = pd.DataFrame({"وزن": [2], "طول_گوش": [10]})

for depth in (1, 2):
    model = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X, y)
    verdict = model.predict(puppy[X.columns])[0]
    correct = (model.predict(X) == y).mean()
    print(f"عمق {depth}: توله‌سگ ← {verdict}   |   درست روی ۱۱ حیوان: {correct:.0%}")
"""

A_MD_5 = """\
## A5 — دستت را روی پیچ بگذار

عمق را خودت عوض کن و دوباره اجرا کن. کوچک‌ترین عمقی که **هر ۱۱ حیوان را درست** دسته‌بندی می‌کند چیست؟
"""

A_CODE_5 = """\
# A5 — پیچِ عمق: عدد را عوض کن، اجرا کن، ببین
""" + ANIMALS + """\
max_depth = 2   # <-- این را عوض کن: 1، 2، 3، 5، 10

model = DecisionTreeClassifier(max_depth=max_depth, random_state=42).fit(X, y)
correct = (model.predict(X) == y).mean()
leaves = model.get_n_leaves()
print(f"عمق {max_depth}: {leaves} برگ، دقتِ روی ۱۱ حیوان: {correct:.0%}")

plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=[fa(c) for c in X.columns],
          class_names=[fa(c) for c in sorted(y.unique())],
          filled=True, fontsize=8, impurity=False)
plt.title(fa(f"درخت با عمق {max_depth}"))
plt.show()
"""

A_MD_6 = """\
## A6 — درختِ تو، درختِ ماشین

درختت را روی کاغذ کشیدی؟ حالا کنارِ درخت ماشین بگذارش.
هر دو یک کار می‌کنند: سؤال، در، سؤال، در، حکم.
"""

A_CODE_6 = """\
# A6 — درخت نهایی ماشین، کنار درختِ کاغذی تو
""" + ANIMALS + """\
model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)
plt.figure(figsize=(12, 6))
plot_tree(model, feature_names=[fa(c) for c in X.columns],
          class_names=[fa(c) for c in sorted(y.unique())],
          filled=True, fontsize=10, impurity=False)
plt.title(fa("درختِ ماشین — با درختِ کاغذیِ خودت مقایسه کن"))
plt.show()
print("شبیه‌شان را بنویس: اولین سؤالِ تو چه بود؟ همانِ ماشین؟")
"""

# ---------------------------------------------------------------- PART B (at-home)
B_MD_1 = """\
---

# PART B — تمرین‌های خانه (قبل از جلسهٔ حل مسئله)

## تمرین B1 — شمارندهٔ برگ و سؤال (۱ نمره)

به درختِ عمق ۲ نگاه کن (سلول A2). چند سؤال می‌پرسد؟ چند برگ دارد؟
"""

B_CODE_1 = """\
# B1 — درخت عمق ۲ را بساز و بشمار
from sklearn.tree import DecisionTreeClassifier

B1_model = DecisionTreeClassifier(max_depth=2, random_state=42)
# TODO: با X و y (از PART A) مدل را آموزش بده (fit)
# TODO: B1_num_questions و B1_num_leaves را پر کن (عدد صحیح)

B1_num_questions = 0   # <-- پاسخ تو
B1_num_leaves = 0      # <-- پاسخ تو
print(f"سؤال‌ها: {B1_num_questions}، برگ‌ها: {B1_num_leaves}")
"""

B_MD_2 = """\
## تمرین B2 — پیش‌بینی مسیر فیل (۱ نمره)

فیل (۳۰۰۰ کیلو، گوش ۲۰) از درختِ عمق ۲ رد می‌شود. به کدام اتاق می‌رسد؟
"""

B_CODE_2 = """\
# B2 — حکمِ درخت دربارهٔ فیل چیست؟
# TODO: درخت عمق ۲ را دوباره بساز و پیش‌بینی فیل را در B2_elephant_room بگذار
# (یکی از: "گربه"، "سگ بزرگ"، "سگ کوچک")

B2_elephant_room = ""   # <-- پاسخ تو
print("فیل به این اتاق می‌رسد:", B2_elephant_room)
"""

B_MD_3 = """\
## تمرین B3 — عمقِ درست را پیدا کن (۱ نمره)

کوچک‌ترین عمقی که هر ۱۱ حیوان را درست دسته‌بندی می‌کند چند است؟
"""

B_CODE_3 = """\
# B3 — حلقه بزن و پیدا کن: کوچک‌ترین عمقِ بی‌نقص
best_depth = None
for depth in range(1, 6):
    m = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X, y)
    # TODO: شرط را کامل کن: اگر مدل همهٔ ۱۱ حیوان را درست گفت، این عمق جواب است
    # (راهنما: (m.predict(X) == y).all() یعنی «همه درست»)
    if False:
        best_depth = depth
        break

B3_min_depth = best_depth   # <-- پاسخ تو
print("کوچک‌ترین عمقِ بی‌نقص:", B3_min_depth)
"""

# ---------------------------------------------------------------- PART C (in-class)
C_MD_1 = """\
---

# PART C — جلسهٔ حل مسئله

## C1 — باغ‌وحشِ غافلگیر: درختت را به آزمون بگذار

حیواناتی که در جدول نیستند. حکمِ درخت را قبل از اجرا حدس بزن — بعد چک کن.
کدام حیوانات قربانی اتاق‌های درخت می‌شوند؟
"""

C_CODE_1 = """\
# C1 — باغ‌وحش غافلگیر: مسافرانِ جدید
""" + ANIMALS + """\
model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)

surprise_zoo = pd.DataFrame({
    "وزن": [2, 8, 0.5, 0.03, 160],
    "طول_گوش": [10, 4, 3, 2, 20],
}, index=["خرگوش", "روباه", "همستر", "گنجشک", "شیر"])

guesses = model.predict(surprise_zoo[X.columns])
for name, ans in zip(surprise_zoo.index, guesses):
    print(f"  {name:8} ← {ans}")
# بحث: کدام حکم‌ها خنده‌دارند؟ چرا؟ کدام سؤالِ درخت ما را به دردسر انداخت؟
"""

C_MD_2 = """\
## C2 — جراحی درخت: دو عمل جراحی، یک نتیجهٔ غافلگیرکن

خرگوش به اتاقِ «سگ کوچک» رفت. دو جراحی امتحان می‌کنیم:
جراحی اول: سؤال‌های بیشتری اجازه بده (عمق بیشتر).
جراحی دوم: مثال‌های بیشتری به ماشین بده (سگ‌های کوچکِ بیشتر).
هر دو را اجرا کن و ببین حکمِ خرگوش عوض می‌شود یا نه.
"""

C_CODE_2 = """\
# C2 — دو جراحی: عمق بیشتر؟ مثال بیشتر؟
""" + ANIMALS + """\
surprise_zoo = pd.DataFrame({
    "وزن": [2, 8, 0.5, 0.03, 160],
    "طول_گوش": [10, 4, 3, 2, 20],
}, index=["خرگوش", "روباه", "همستر", "گنجشک", "شیر"])

# جراحی ۱: عمق بیشتر — سؤال‌های ریزتر
deep = DecisionTreeClassifier(max_depth=5, random_state=42).fit(X, y)

# جراحی ۲: مثال بیشتر — ۴ سگِ کوچکِ تازه به جدول اضافه کن
extra_dogs = pd.DataFrame({"وزن": [7, 8, 6.5, 9], "طول_گوش": [8.5, 9, 8, 9.5],
                           "گروه": ["سگ کوچک"] * 4})
X_fed = pd.concat([X, extra_dogs[["وزن", "طول_گوش"]]])
y_fed = pd.concat([y, extra_dogs["گروه"]])
fed = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X_fed, y_fed)

base = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)
print(f"{'حیوان':10} | عادی     | عمق‌بیشتر | مثال‌بیشتر")
for name, a, b, c in zip(surprise_zoo.index,
                         base.predict(surprise_zoo),
                         deep.predict(surprise_zoo),
                         fed.predict(surprise_zoo)):
    print(f"  {name:8} | {a:8} | {b:8} | {c}")
print()
print("خرگوش در هر سه جراحی: سگ کوچک. چرا؟ چون هیچ سؤالی دربارهٔ «وزن» و «گوش»")
print("خرگوش را از پودل جدا نمی‌کند. این دو عدد برای این کار کافی نیستند.")
print("درمانِ واقعی: سؤالِ بهتر دربارهٔ چیزی که اندازه نگرفته‌ایم — جلسهٔ بعد.")
"""

C_MD_3 = """\
## C3 — بحث: درختِ کاغذیِ تو در برابر درختِ ماشین

اولین سؤالِ تو همانِ ماشین بود؟ اگر نه، درختِ تو هم درست کار می‌کرد؟
پس چند «درختِ درست» برای این جدول وجود دارد؟
"""

# ---------------------------------------------------------------- assemble
part0 = [md(PART0_MD), code(PART0_CODE)]
partA = [md(A_MD_1), code(A_CODE_1), md(A_MD_2), code(A_CODE_2),
         md(A_MD_3), code(A_CODE_3), md(A_MD_4), code(A_CODE_4),
         md(A_MD_5), code(A_CODE_5), md(A_MD_6), code(A_CODE_6)]
partB = [md(B_MD_1), code(B_CODE_1), md(B_MD_2), code(B_CODE_2),
         md(B_MD_3), code(B_CODE_3)]
partC = [md(C_MD_1), code(C_CODE_1), md(C_MD_2), code(C_CODE_2), md(C_MD_3)]

student_cells = (
    [md("# جلسهٔ ۲ — ماشینِ ۲۰ سؤالی\n\n*درخت تصمیم را بخوان، بکش، و خودت بساز.*")]
    + [code(SETUP)]
    + part0
    + [md("# PART A — جلسهٔ تدریس\n\n*(این بخش را با معلم، در کلاس پر می‌کنیم.)*")]
    + partA
    + partB
    + partC
)

# ---- solution variants of the B cells (answers filled in) ----
B_CODE_1_SOL = """\
# B1 — درخت عمق ۲ را بساز و بشمار (پاسخ)
from sklearn.tree import DecisionTreeClassifier

B1_model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)
# سؤال‌های واقعی درخت: ۲ (ریشه + یک سؤال داخل شاخهٔ سگ‌ها)
# برگ‌های درخت: ۳ (گربه، سگ کوچک، سگ بزرگ)
B1_num_questions = 2
B1_num_leaves = 3
print(f"سؤال‌ها: {B1_num_questions}، برگ‌ها: {B1_num_leaves}")
# راه چک: model.get_depth() و model.get_n_leaves()
print("چک:", B1_model.get_depth(), B1_model.get_n_leaves())
"""

B_CODE_2_SOL = """\
# B2 — حکمِ درخت دربارهٔ فیل (پاسخ)
model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X, y)
elephant = pd.DataFrame({"وزن": [3000], "طول_گوش": [20]})
B2_elephant_room = model.predict(elephant[X.columns])[0]
print("فیل به این اتاق می‌رسد:", B2_elephant_room)
# چرا؟ وزن ۳۰۰۰ > ۱۴ پس سمت سگ‌ها؛ گوش ۲۰ >= ۸.۲۵ پس اتاقِ سگ بزرگ.
"""

B_CODE_3_SOL = """\
# B3 — کوچک‌ترین عمقِ بی‌نقص (پاسخ)
best_depth = None
for depth in range(1, 6):
    m = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X, y)
    if (m.predict(X) == y).all():
        best_depth = depth
        break

B3_min_depth = best_depth
print("کوچک‌ترین عمقِ بی‌نقص:", B3_min_depth)
# عمق ۱ فقط گربه/سگ می‌بیند (سگ‌های کوچک را گربه می‌گوید) — عمق ۲ هر سه گروه را جدا می‌کند.
"""

partB_sol = [md(B_MD_1), code(B_CODE_1_SOL), md(B_MD_2), code(B_CODE_2_SOL),
             md(B_MD_3), code(B_CODE_3_SOL)]

solution_cells = (
    [md("# جلسهٔ ۲ — ماشینِ ۲۰ سؤالی (نسخهٔ کامل)\n\n*راهنمای معلم — با پاسخ‌های پرشده.*")]
    + [code(SETUP)]
    + part0
    + [md("# PART A — جلسهٔ تدریس (پاسخ‌ها)")]
    + partA
    + partB_sol
    + partC
)

write(os.path.join(HERE, "s02_notebook.ipynb"), student_cells)
write(os.path.join(HERE, "s02_notebook_solution.ipynb"), solution_cells)
