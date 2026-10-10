"""Generate the student and solution notebooks for Session 1 (source of truth).

Run:  python build_notebooks.py
Outputs: s01_notebook.ipynb (student — PART B cells are TODO starters)
         s01_notebook_solution.ipynb (instructor — full answers)

After regenerating, commit outputs into BOTH notebooks once:
    jupyter nbconvert --to notebook --execute --inplace s01_notebook.ipynb
    jupyter nbconvert --to notebook --execute --inplace s01_notebook_solution.ipynb
Then strip the PART 0 demo outputs from the STUDENT notebook only
(the hook must stay a surprise):  python build_notebooks.py --strip-demo-output

The judge must score 4/4 on the solution notebook and 0/4 (helpful messages,
no crash) on the untouched student notebook — verify after every change.
"""
import json, os, sys

STABLE = []  # running counter for stable cell ids


def _cid():
    STABLE.append(1)
    return f"s01-{len(STABLE):02d}"


def md(src):
    return {"cell_type": "markdown", "id": _cid(),
            "metadata": {}, "source": src.splitlines(keepends=True)}


def code(src):
    return {"cell_type": "code", "id": _cid(),
            "execution_count": None, "metadata": {}, "outputs": [],
            "source": src.splitlines(keepends=True)}


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
    STABLE.clear()
    with open(path, "w") as f:
        json.dump(nb(cells), f, indent=1, ensure_ascii=False)
    print("wrote", path)


# ---------------------------------------------------------------- PART 0 (hook demo)
# ONE demo, four printed beats. The slide presenter notes and teaching-notes.md
# reference these exact «مرحلهٔ N» markers — if you change the beats, change
# slides.md slide 3/4/5 notes and teaching-notes.md in the same commit.
DEMO0 = md("""\
# PART 0 — نمایش ویژهٔ هوش مصنوعی

**بازیِ حیوانات.** ماشین فقط ۸ حیوان با برچسب می‌بیند؛ بعد خودش یک خط می‌کشد و به حیواناتی که هرگز ندیده جواب می‌دهد.
""")

DEMO0_CELL = code("""\
# دمو: بازیِ حیوانات — ماشین از ۸ مثال یک قانون یاد می‌گیرد
%pip -q install arabic-reshaper python-bidi  # needed on Colab; already installed locally
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

def fa(text):
    # Persian text for matplotlib: shapes + orders it correctly
    return get_display(arabic_reshaper.reshape(str(text)))

# مرحلهٔ ۱: همهٔ چیزی که ماشین می‌بیند — ۸ حیوان، هر کدام دو عدد و یک برچسب
print("——— مرحلهٔ ۱ · جدول ———")
animals = pd.DataFrame({
    "وزن": [4.5, 3.0, 6.0, 5.0, 22, 32, 28, 38],      # کیلوگرم
    "طول_گوش": [5, 7, 4, 6, 9, 12, 11, 13],            # سانتی‌متر
    "برچسب": ["گربه", "گربه", "گربه", "گربه", "سگ", "سگ", "سگ", "سگ"],
}, index=["پرشین", "سیامی", "گارفیلد", "شارتز", "بولداگ", "آلمانی", "گلدن", "دابلمان"])
print("همهٔ چیزی که ماشین می‌بیند (فقط ۸ سطر):")
print(animals, "\\n")

# مرحلهٔ ۲: یاد بگیر — ماشین خودش قانون را پیدا می‌کند (بی‌سروصدا!)
model = DecisionTreeClassifier(max_depth=1, random_state=42)
model.fit(animals[["وزن", "طول_گوش"]], animals["برچسب"])

# مرحلهٔ ۳: خطِ ماشین را ببین — هیچ انسانی این خط را نداد
print("——— مرحلهٔ ۳ · خطِ ماشین ———")
plt.figure(figsize=(8, 4))
cats = animals[animals["برچسب"] == "گربه"]; dogs = animals[animals["برچسب"] == "سگ"]
plt.scatter(cats["وزن"], cats["طول_گوش"], c="steelblue", s=130, label="گربه")
plt.scatter(dogs["وزن"], dogs["طول_گوش"], c="darkorange", s=130, label="سگ")
plt.axvline(14, color="crimson", lw=2, ls="--")
plt.text(15, 12.2, fa("خطی که ماشین خودش کشید"), color="crimson")
plt.xlabel(fa("وزن (کیلوگرم)")); plt.ylabel(fa("طول گوش (سانتی‌متر)")); plt.legend()
plt.show()

# مرحلهٔ ۴: امتحان! حیواناتی که ماشین هرگز ندیده است
print("——— مرحلهٔ ۴ · امتحان با حیوانات ندیده ———")
new_animals = pd.DataFrame({
    "وزن": [35, 7, 2, 3000],
    "طول_گوش": [10, 5, 10, 20],
}, index=["گرگ", "گربهٔ همسایه", "توله‌سگ", "فیل"])
print("پاسخ ماشین به حیواناتی که هرگز ندیده بود:")
answers = model.predict(new_animals[["وزن", "طول_گوش"]])
for name, ans in zip(new_animals.index, answers):
    print(f"  {name:12} ← {ans}")

# کل رازِ مرحلهٔ ۲ فقط یک سؤال بود: «وزن ⁦≤ ۱۴⁩ کیلوگرم؟» — این کلمهٔ کلیدی جلسه‌های ۲ و ۳ است.
print("\\nکل رازِ ماشین فقط یک سؤال بود: «وزن ⁦≤ ۱۴⁩ کیلوگرم؟»")
""")

# ---------------------------------------------------------------- setup cell
SETUP_MD = None  # setup cell arrives right after the PART A header
SETUP = code("""\
# COURSE SETUP — identical in every session. Just run it. (5 seconds)
%matplotlib inline
%pip -q install arabic-reshaper python-bidi  # needed on Colab; already installed locally
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
""")

HEADER_A = md("""\
# جلسهٔ ۱ — یادگیری ماشین چیست؟
## روز اول — تو یک هوش مصنوعی می‌سازی

**هدف امروز تو:** *«تا پایان امروز، تو می‌توانی یک مدل یادگیری ماشین آموزش بدهی و به خانواده‌ات نشان بدهی.»*

**تحویل امشب:** یک مخزن گیت‌هاب با این نت‌بوک + مدلی که جواب می‌دهد: **«آیا من در تایتانیک زنده می‌ماندم؟»**

---

# PART A — جلسهٔ تدریس
*(این بخش را با هم در کلاس پر می‌کنیم)*
""")

# ---------------------------------------------------------------- PART A
part_a = [
SETUP,
md("""\
## A1 — بازی میوه: ویژگی‌ها و برچسب‌ها

هر نمونهٔ یادگیری ماشین با **ویژگی (Feature)** — یعنی سرنخ — و یک **برچسب (Label)** — یعنی پاسخ — توصیف می‌شود.
هر سطر (ویژگی‌ها + برچسب) یک **نمونه (Example)** است.

سلول را اجرا کن و بازی کن: ستون پاسخ را بپوشان و فقط از سرنخ‌ها میوه را حدس بزن.
"""),
code("""\
fruits = pd.DataFrame({
    "color":   ["red", "yellow", "purple", "yellow", "red", "green"],
    "size":    ["medium", "long", "small", "medium", "round", "medium"],
    "texture": ["smooth", "smooth", "wrinkly", "curved", "smooth", "smooth"],
    "fruit":   ["apple", "banana", "grape", "banana", "apple", "apple"],
})
fruits
"""),
md("""\
## A2 — کدام ویژگی مهم‌تر است؟

به جدول نگاه کن. **کدام سرنخ** برای حدس زدن میوه مفیدتر است: `color`، `size` یا `texture`؟

یک دقیقه بحث کن، بعد حدست را پایین بنویس. *(هنوز جواب غلطی وجود ندارد — جلسهٔ ۹ یاد می‌گیریم این را حساب کنیم!)*
"""),
code("""\
most_useful_feature = "color"   # <-- change to your guess: "color", "size" or "texture"
print(f"I think '{most_useful_feature}' is the most useful clue.")
"""),
md("""\
## A3 — یادگیری نظارت‌شده: پنهان‌کردن پاسخ

یادگیری نظارت‌شده (Supervised Learning) = یادگیری از نمونه‌هایی **که پاسخ دارند**.
مدل جدول کامل را درس می‌خواند... بعد **برچسب را پنهان می‌کنیم** و با نمونه‌های جدید ازش امتحان می‌گیریم.
"""),
code("""\
study_table = fruits.copy()          # what the model studies WITH answers
quiz_table = fruits.drop(columns=["fruit"])  # what the model sees at quiz time

print("درس (ویژگی + برچسب):")
display(study_table.head(3))
print("امتحان (فقط ویژگی — برچسب پنهان است!):")
display(quiz_table.head(3))
"""),
md("""\
## A4 — تایتانیک: ۸۹۱ مسافر

هر سطر یک زندگی است. هر ستون یک سرنخ. برچسب `survived` است (۱ = زنده ماند، ۰ = مرد).

«تنها» ریسکِ دیتای واقعی: بعضی سطرها اطلاعات ناقص دارند — پایین می‌بینی که فقط سطرهای کامل به مدل می‌رسند.
"""),
code("""\
# دیتاست در پوشهٔ assets دوره ذخیره شده؛ اگر نبود، از روی اینترنت تازه می‌شود.
for _src in ("assets/titanic.csv", "../assets/titanic.csv",
             "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"):
    try:
        titanic = pd.read_csv(_src)
        break
    except Exception:
        continue
titanic = titanic.rename(columns=str.lower)
titanic = titanic[["survived", "pclass", "sex", "age", "fare", "embarked"]].dropna()
print(f"از ۸۹۱ مسافر، {len(titanic)} نفر اطلاعات کامل دارند؛ فقط همین‌ها مدل را آموزش می‌دهند.")
titanic.head()
"""),
md("""\
## A5 — داده به‌صورت عکس: چه کسی زنده ماند؟

*همیشه قبل از هر کاری، داده‌ات را ببین.*
"""),
code("""\
titanic["survived"].map({1: "survived", 0: "did not"}).value_counts().plot(
    kind="bar", color=["tomato", "seagreen"], rot=0)
plt.title(fa("تعداد بازماندگان تایتانیک")); plt.ylabel(fa("مسافر"))
plt.show()
"""),
md("""\
## A6 — دو نمودار ضربهٔ نهایی
"""),
code("""\
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
titanic.groupby("sex")["survived"].mean().plot(kind="bar", ax=axes[0], color="orchid", rot=0)
axes[0].set_title(fa("نرخ بقا بر حسب جنسیت")); axes[0].set_ylabel(fa("سهم زندگان"))
titanic.groupby("pclass")["survived"].mean().plot(kind="bar", ax=axes[1], color="steelblue", rot=0)
axes[1].set_title(fa("نرخ بقا بر حسب کلاس مسافر"))
plt.show()
# زنِ کلاس-۱ بودن در سال ۱۹۱۲ تقریباً بلیتِ بقا بود — نگاه کن: ۷۵٪ در برابر ۲۰٪!
"""),
md("""\
## A7 تا A9 — لحظهٔ جادویی: ساخت هوش مصنوعی در ۳ خط

با من تایپ کن. سه خط. همین یک هوش مصنوعی کامل است.
"""),
code("""\
# خط صفر (جادو نیست، فقط آماده‌سازی): سرنخ‌ها را به عددی که مدل می‌فهمد تبدیل کن
X = titanic[["pclass", "age", "fare"]].copy()
X["is_female"] = (titanic["sex"] == "female").astype(int)
y = titanic["survived"]
X.head(3)
"""),
code("""\
# A8 — سه خط جادویی. شمرده یک دو سه، همه بگویید: یاد بگیر!
# «model» یعنی مدل (Model): دانش‌آموزی که مثال‌های حل‌شده را می‌خواند
model = DecisionTreeClassifier(max_depth=3, random_state=42)  # ۱. انتخاب دانش‌آموز (مدل)
model.fit(X, y)                                               # ۲. درس خواندن
print(f"تمام. مدل همین الان {len(X)} زندگی را در کمتر از یک ثانیه خواند.")
"""),
code("""\
# A9 — ازش سؤال بپرس: آیا خودِ تو زنده می‌ماندی؟
me = pd.DataFrame([{"pclass": 2, "age": 13, "fare": 30, "is_female": 0}])  # <-- این را خودت کن!
verdict = model.predict(me)[0]
print("زنده می‌ماند" if verdict == 1 else "زنده نمی‌ماند")

# و نگاه کن — قاعده‌هایی که پیدا کرد فقط چند سؤال است. خودت هم می‌توانستی بکشی.
plt.figure(figsize=(14, 7))
plot_tree(model, feature_names=list(X.columns),
          class_names=[fa("زنده نمی‌ماند"), fa("زنده می‌ماند")],
          filled=True, fontsize=10, impurity=False)
plt.title(fa("قاعده‌هایی که ماشین یاد گرفت — فقط چند سؤال است!"))
plt.show()
"""),
]

# ---------------------------------------------------------------- PART B (at-home)
# TWO variants: student starter (TODO — judge scores 0/4 untouched) and solution
# (judge scores 4/4). The starter must stay runnable-but-unsolved: variables the
# judge grades are left UNDEFINED (named in comments) so the judge answers
# "did you fill in cell BN?" instead of crashing or passing.
part_b_head = md("""\
---

# PART B — تمرین‌های خانه
**مهلت: قبل از جلسهٔ حل مسئله.** پاسخ‌ها را همین‌جا در همین سلول‌ها بنویس. (حدود ۲۰ تا ۳۰ دقیقه طول می‌کشد.)
هر وقت خواستی خودت را نمره بده: `python judge/run.py s01_notebook.ipynb`
اولین اجرا همهٔ تمرین‌ها را قرمز نشان می‌دهد — عادی است! آن را با پاسخ‌های خودت سبز کن.

**چه چیزی باید یاد بگیری:** این تمرین‌ها مطمئن می‌شوند که خودت، تنها، می‌توانی دیتاست بسازی،
مدل آموزش بدهی و پیش‌بینی کنی.
""")

B1_MD = md("""\
## تمرین B1 — کارآگاه ویژگی‌ها (۱ نمره)

یک دوست می‌خواهد **قبولی یک دانش‌آموز در آزمون** را پیش‌بینی کند و این ویژگی‌ها را پیشنهاد می‌دهد:

`["name", "hours_studied", "favorite_color", "previous_score", "shoe_size"]`

فقط ویژگی‌هایی را که واقعاً می‌توانند به پیش‌بینی قبولی کمک کنند، به‌صورت یک **لیست** پایتونی بنویس.
(راهنما: آیا مدل از اسمِ کسی چیزی مفید یاد می‌گیرد؟)
""")

B1_STU = code("""\
# پاسخ تو این‌جا — خط زیر را از توضیح بیرون بیاور و خودت کاملش کن:
# B1_good_features = ["..."]   # <-- فقط سرنخ‌هایی که واقعاً قبولی را پیش‌بینی می‌کنند
""")

B1_SOL = code("""\
# answer key: only these two carry real signal about passing a test
B1_good_features = ["hours_studied", "previous_score"]  # پاسخ نهایی
""")

B2_MD = md("""\
## تمرین B2 — دیتاست خودت را بساز (۱ نمره)

حالا تو معلمی. یک دیتاست کوچک (یک DataFrame پانداسی) از **حداقل ۴ حیوان** بساز
با ویژگی‌های `["size", "can_fly"]` و برچسب `"animal"`. شرایط:

- دقیقاً همین ۳ ستون،
- حداقل ۴ سطر، هر کدام یک حیوان متفاوت،
- `size` یکی از `"small"`، `"medium"`، `"large"` باشد و `can_fly` عدد `0` یا `1`.
""")

B2_STU = code("""\
# پاسخ تو این‌جا — الگوی زیر را از توضیح بیرون بیاور و با حیواناتِ خودت پرش کن:
# B2_animals = pd.DataFrame({
#     "size":    ["small", "large", "medium", "small"],   # فقط: "small" یا "medium" یا "large"
#     "can_fly": [0, 0, 0, 1],                            # فقط 0 یا 1
#     "animal":  ["cat", "elephant", "dog", "sparrow"],   # ۴ حیوان متفاوت (یا بیشتر)
# })
""")

B2_SOL = code("""\
B2_animals = pd.DataFrame({
    "size":     ["small", "large", "medium", "small"],
    "can_fly":  [0, 0, 0, 1],
    "animal":   ["cat", "elephant", "dog", "sparrow"],
})
# اسم ستون‌ها دقیقاً همین بماند: size, can_fly, animal
B2_animals
""")

B3_MD = md("""\
## تمرین B3 — سه خط جادویی (۱ نمره)

برای آموزش یک درخت تصمیم روی دیتاست حیواناتِ خودت، سه جای `...` را کامل کن
(اگر تمرین B2 را نکرده‌ای، اول برگرد سراغش — این سلول به آن نیاز دارد).
""")

B3_STU = code("""\
if "B2_animals" not in dir():
    print("اول تمرین B2 را کامل کن — این سلول به دیتاست تو (B2_animals) نیاز دارد.")
else:
    B2_animals_num = B2_animals.copy()
    B2_animals_num["size_num"] = B2_animals_num["size"].map({"small": 0, "medium": 1, "large": 2})

    B3_X = B2_animals_num[["size_num", "can_fly"]]     # ویژگی‌ها
    B3_y = B2_animals_num["animal"]                    # برچسب

    B3_model = ...      # TODO: یک DecisionTreeClassifier بساز (random_state=42)
    ...                 # TODO: آن را با B3_X و B3_y درسش بده — همان دستور fit
    B3_prediction = ... # TODO: با .predict بپرس: اندازهٔ متوسط (size_num=1)، پرواز ندارد (can_fly=0) ← چه حیوانی؟
    print("مدل می‌گوید حیوان متوسطِ بی‌پرواز این است:", B3_prediction)
""")

B3_SOL = code("""\
B2_animals_num = B2_animals.copy()
B2_animals_num["size_num"] = B2_animals_num["size"].map({"small": 0, "medium": 1, "large": 2})

B3_X = B2_animals_num[["size_num", "can_fly"]]     # ویژگی‌ها
B3_y = B2_animals_num["animal"]                    # برچسب

B3_model = DecisionTreeClassifier(random_state=42)  # ۱. انتخاب دانش‌آموز
B3_model.fit(B3_X, B3_y)                            # ۲. درس خواندن
B3_prediction = B3_model.predict(pd.DataFrame([{"size_num": 1, "can_fly": 0}]))[0]  # ۳. سؤال
print("مدل می‌گوید حیوان متوسطِ بی‌پرواز این است:", B3_prediction)
""")

B4_MD = md("""\
## تمرین B4 — پیش‌بینی‌گر بقا (۱ نمره)

مدل تایتانیکِ خودت را آموزش بده (مثل کلاس، با `max_depth=3` و `random_state=42`)
و بقا را برای این مسافر پیش‌بینی کن: **کلاس ۳، پسر ۱۲ ساله، کرایهٔ ۷.۵.**

بعد جواب بده: او زنده ماند؟ عدد `1` (زنده ماند) یا `0` (نماند) را در `B4_answer` بگذار.
""")

B4_STU = code("""\
# داده از قبل بارگذاری شده (titanic). مثل سلول A7، دقیقاً X و y را بساز:
B4_X = ...   # TODO: همان ۴ ستونِ A7 (pclass, age, fare, is_female)
B4_y = ...   # TODO: ستون پاسخ (survived)

B4_model = ...   # TODO: بساز (max_depth=3, random_state=42) و با B4_X و B4_y درسش بده

new_passenger = pd.DataFrame([{"pclass": 3, "age": 12, "fare": 7.5, "is_female": 0}])
B4_answer = ...  # TODO: int( پیش‌بینی مدل برای مسافر تازه ) — باید 0 یا 1 باشد
""")

B4_SOL = code("""\
# داده از قبل بارگذاری شده (titanic). مثل سلول A7:
B4_X = X.copy()
B4_y = y.copy()

B4_model = DecisionTreeClassifier(max_depth=3, random_state=42)
B4_model.fit(B4_X, B4_y)

new_passenger = pd.DataFrame([{"pclass": 3, "age": 12, "fare": 7.5, "is_female": 0}])
B4_answer = int(B4_model.predict(new_passenger)[0])   # باید 1 یا 0 باشد (جواب درست: 0)
print("مدل می‌گوید:", "زنده می‌ماند" if B4_answer == 1 else "زنده نمی‌ماند")
""")

SHIP_MD = md("""\
---

# تحویل بده!

وقتی هر چهار تمرین از داوری سربلند بیرون آمد:
1. این نت‌بوک را ذخیره کن.
2. آن را در مخزن گیت‌هاب دوره‌ات commit کن — در پوشهٔ جلسه این سه دستور:
   `git add .` ← `git commit -m "S1: my first model"` ← `git push`
3. به خانواده‌ات نشان بده: *«امروز یک هوش مصنوعی ساختم.»* — چون واقعاً ساختی.
""")

SOL_NOTE = md("""\
> **یادداشت مدرس (نسخهٔ پاسخ):** سلول‌های B پاسخ کامل دارند.
> در نسخهٔ دانش‌آموز همین سلول‌ها الگوی TODO با `...` هستند.
""")

# ---------------------------------------------------------------- PART C
part_c = [
md("""\
---

# PART C — جلسهٔ حل مسئله
*(اول تمرین‌های خانه را زنده حل می‌کنیم — بعد این‌ها را)*
"""),
md("""\
## C1 — موتور خیال

**مسافرهای خودت را اختراع کن** (هر کلاس، سن، کرایه و جنسیتی که دوست داری) و ببین مدل چه می‌گوید.
می‌توانی مسافری پیدا کنی که مدل در او *اشتباه* کند؟ می‌توانی مدل را بشکنی؟
"""),
code("""\
my_passengers = pd.DataFrame([
    {"pclass": 1, "age": 40, "fare": 500, "is_female": 1},
    {"pclass": 3, "age": 30, "fare": 5,  "is_female": 0},
    # سطرهای خودت را اینجا اضافه کن!
])
preds = model.predict(my_passengers)
for i, p in enumerate(preds):
    print(f"مسافر {i+1}: {'زنده می‌ماند' if p else 'زنده نمی‌ماند'}")
"""),
md("""\
## C2 — انسان را شکست بده

قبل از اجرای سلول بعدی، بقا هر یک از این ۵ مسافر را خودت حدس بزن.
۵ حدست را بنویس (مثلاً `"01100"`)، بعد اجرا کن. **می‌توانی از ماشین جلو بزنی؟**
"""),
code("""\
challenge = pd.DataFrame([
    {"pclass": 1, "age": 35, "fare": 80,  "is_female": 1},
    {"pclass": 2, "age": 29, "fare": 26,  "is_female": 0},
    {"pclass": 3, "age": 21, "fare": 7,   "is_female": 0},
    {"pclass": 1, "age": 60, "fare": 90,  "is_female": 0},
    {"pclass": 3, "age": 6,  "fare": 12,  "is_female": 1},
])
my_guesses = "00000"  # <-- ۵ حدس تو، یک کاراکتر برای هر مسافر، قبل از اجرای predict
machine = "".join(str(p) for p in model.predict(challenge))
print("تو:    ", my_guesses)
print("ماشین:", machine)
score = sum(a == b for a, b in zip(my_guesses, machine))
print(f"تو {score}/5 بار با ماشین هم‌نظر بودی.")
"""),
md("""\
## C3 — بحث: دانشِ ماشین کجا زندگی می‌کند؟

دوباره به عکس درخت در سلول A9 نگاه کن. مدل هیچ‌وقت کتاب تاریخ نخوانده.
هیچ‌وقت از کوه یخ نشنیده. **«دانش» او از کجا آمده؟**

*(جوابت را به جمع‌بندی بیاور — این، بذرِ همهٔ کارهای جلسهٔ ۲ است.)*
"""),
]

student_cells = ([DEMO0, DEMO0_CELL, HEADER_A] + part_a
                 + [part_b_head, B1_MD, B1_STU, B2_MD, B2_STU, B3_MD, B3_STU,
                    B4_MD, B4_STU, SHIP_MD] + part_c)
solution_cells = ([DEMO0, DEMO0_CELL, HEADER_A] + part_a
                  + [part_b_head, SOL_NOTE, B1_MD, B1_SOL, B2_MD, B2_SOL,
                     B3_MD, B3_SOL, B4_MD, B4_SOL, SHIP_MD] + part_c)

out_dir = os.path.dirname(os.path.abspath(__file__))
write(os.path.join(out_dir, "s01_notebook.ipynb"), student_cells)
write(os.path.join(out_dir, "s01_notebook_solution.ipynb"), solution_cells)

if "--strip-demo-output" in sys.argv:
    for name in ("s01_notebook.ipynb",):
        p = os.path.join(out_dir, name)
        d = json.load(open(p))
        cell = d["cells"][1]  # the PART 0 demo cell — hook must stay a surprise
        cell["outputs"] = []
        cell["execution_count"] = None
        json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
        print("stripped PART 0 outputs from", name)
