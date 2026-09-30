"""STALE — do not run. The Session 1 notebooks were hand-refined after the single-demo hook
rewrite (Animal Game) and the Persian-matplotlib fa() fix; this generator predates those changes
and would overwrite them. The .ipynb files are the artifacts of record. Regenerating this script
to match is deferred until the next content-level change to Session 1 (regeneration workflow §14).

Original purpose: Generate the student and solution notebooks for Session 1.

Run:  python build_notebooks.py
Outputs: notebook/s01_notebook.ipynb (student)
         notebook/s01_notebook_solution.ipynb (instructor)
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
        json.dump(nb(cells), f, indent=1)
    print("wrote", path)


# ---------------------------------------------------------------- setup cell
SETUP = """\
# COURSE SETUP — identical in every session. Just run it. (5 seconds)
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

plt.rcParams["figure.figsize"] = (8, 4)
print("Setup OK — let's build some AI.")
"""

# ---------------------------------------------------------------- PART 0 (demos)
part_0 = [
md("""\
# PART 0 — نمایش ویژهٔ هوش مصنوعی
*(دموهای شروع جلسه — مدرس این سلول‌ها را در ۵ دقیقهٔ اول اجرا می‌کند. به‌ترتیب، با اجرای نمایشی!)*
"""),
md("""\
## دمو ۱ — ذهن‌خوان
عددی بین ۱ تا ۲۰ فکر کن... ماشین می‌گوید کوچک است یا بزرگ.
"""),
code("""\
# دمو ۱: ذهن‌خوان — عدد به کوچک/بزرگ
import numpy as np
from sklearn.tree import DecisionTreeClassifier

X = [[n] for n in range(1, 21)]
y = ["small" if n <= 7 else "big" for n in range(1, 21)]
mind_reader = DecisionTreeClassifier().fit(X, y)

print("عددی بین ۱ تا ۲۰ فکر کن. ماشین می‌گوید: کوچک یا بزرگ؟")
for n in (3, 12, 19, 7, 20):
    verdict = "کوچک" if mind_reader.predict([[n]])[0] == "small" else "بزرگ"
    print(f"  {n:>2} → {verdict}")
"""),
md("""\
## دمو ۲ — هنرمند فوری
همان تصویر، از چشم ماشین: عدد خام ← لبه ← تار ← خطوط.
"""),
code("""\
# دمو ۲: چهار چشمِ ماشین روی یک تصویر
import matplotlib.pyplot as plt
from scipy import ndimage

rng = np.random.default_rng(42)
img = ndimage.gaussian_filter(rng.random((64, 64)), 3)

fig, axes = plt.subplots(1, 4, figsize=(14, 3.5))
views = [(img, "عدد خام"), (ndimage.sobel(img), "فیلتر لبه"),
         (ndimage.gaussian_filter(img, 1), "فیلتر تار"),
         (np.abs(ndimage.laplace(img)), "فیلتر خطوط")]
for ax, (im, title) in zip(axes, views):
    ax.imshow(im, cmap="viridis"); ax.set_title(title); ax.axis("off")
plt.suptitle("این همان چیزی است که ماشین می‌بیند", y=1.02)
plt.tight_layout(); plt.show()
"""),
md("""\
## دمو ۳ — فالگیر
ماشینی که ۸۹۱ مسافر واقعی سال ۱۹۱۲ را مطالعه کرده. ازش بپرس کی زنده می‌ماند!
"""),
code("""\
# دمو ۳: فالگیر تایتانیک — از قبل آموزش دیده است
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

titanic_demo = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
).rename(columns=str.lower).dropna(subset=["age", "embarked"])
titanic_demo["is_female"] = (titanic_demo["sex"] == "female").astype(int)

fortune_teller = DecisionTreeClassifier(max_depth=3, random_state=42).fit(
    titanic_demo[["pclass", "is_female", "age", "fare"]], titanic_demo["survived"])

cases = [(1, 1, 17, 100, "دختر ۱۷ سالهٔ کلاس ۱، کرایهٔ ۱۰۰ دلار"),
         (3, 0, 25, 7,   "پسر ۲۵ سالهٔ کلاس ۳، کرایهٔ ۷ دلار"),
         (1, 0, 50, 60,  "مرد ۵۰ سالهٔ کلاس ۱، کرایهٔ ۶۰ دلار"),
         (3, 1, 5, 20,   "دختر ۵ سالهٔ کلاس ۳، کرایهٔ ۲۰ دلار")]
for pclass, is_female, age, fare, desc in cases:
    pred = fortune_teller.predict([[pclass, is_female, age, fare]])[0]
    print(f"{desc} → {'زنده می‌ماند' if pred else 'زنده نمی‌ماند'}")
"""),
]

# ---------------------------------------------------------------- PART A
part_a = [
md("""\
# جلسهٔ ۱ — یادگیری ماشین چیست؟
## روز اول — تو یک هوش مصنوعی می‌سازی

**هدف امروز تو:** *«تا پایان امروز، تو می‌توانی یک مدل یادگیری ماشین آموزش بدهی و به خانواده‌ات نشان بدهی.»*

**تحویل امشب:** یک مخزن گیت‌هاب با این نت‌بوک + مدلی که جواب می‌دهد: **«آیا من در تایتانیک زنده می‌ماندم؟»**

---

# PART A — جلسهٔ تدریس
*(این بخش را با هم در کلاس پر می‌کنیم)*
"""),
code(SETUP),
md("""\
## A1 — بازی میوه: ویژگی‌ها و برچسب‌ها

هر نمونهٔ یادگیری ماشین با **ویژگی‌ها** (سرنخ‌ها) و یک **برچسب** (پاسخ) توصیف می‌شود.
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

یادگیری نظارت‌شده = یادگیری از نمونه‌هایی **که پاسخ دارند**.
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
## A4 — تایتانیک: ۸۹۱ مسافر، ۸۹۱ سطر

هر سطر یک زندگی است. هر ستون یک سرنخ. برچسب `survived` است (۱ = زنده ماند، ۰ = مرد).
"""),
code("""\
titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")\\
           .rename(columns=str.lower)
titanic = titanic[["survived", "pclass", "sex", "age", "fare", "embarked"]].dropna()
print(f"{len(titanic)} passengers are ready to teach our model.")
titanic.head()
"""),
md("""\
## A5 — داده به‌صورت عکس: چه کسی زنده ماند؟

*همیشه قبل از هر کاری، داده‌ات را ببین.*
"""),
code("""\
titanic["survived"].map({1: "survived", 0: "did not"}).value_counts().plot(
    kind="bar", color=["tomato", "seagreen"], rot=0)
plt.title("تعداد بازماندگان تایتانیک"); plt.ylabel("مسافر")
plt.show()
"""),
md("""\
## A6 — دو نمودار ضربهٔ نهایی
"""),
code("""\
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
titanic.groupby("sex")["survived"].mean().plot(kind="bar", ax=axes[0], color="orchid", rot=0)
axes[0].set_title("نرخ بقا بر حسب جنسیت"); axes[0].set_ylabel("سهم زندگان")
titanic.groupby("pclass")["survived"].mean().plot(kind="bar", ax=axes[1], color="steelblue", rot=0)
axes[1].set_title("نرخ بقا بر حسب کلاس مسافر")
plt.show()
# زنِ کلاس-۱ بودن در سال ۱۹۱۲ تقریباً بلیتِ بقا بود.
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
model = DecisionTreeClassifier(max_depth=3, random_state=42)  # ۱. انتخاب دانش‌آموز
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
plot_tree(model, feature_names=list(X.columns), class_names=["mord", "zande"],
          filled=True, fontsize=10, impurity=False)
plt.title("قاعده‌هایی که ماشین یاد گرفت — فقط چند سؤال است!")
plt.show()
"""),
]

# ---------------------------------------------------------------- PART B (at-home)
part_b_student = [
md("""\
---

# PART B — تمرین‌های خانه
**مهلت: قبل از جلسهٔ حل مسئله.** پاسخ‌ها را همین‌جا در همین سلول‌ها بنویس.
هر وقت خواستی خودت را نمره بده: `python judge/run.py s01_notebook.ipynb`

**چه چیزی باید یاد بگیری:** این تمرین‌ها مطمئن می‌شوند که خودت، تنها، می‌توانی دیتاست بسازی،
مدل آموزش بدهی و پیش‌بینی کنی.
"""),
md("""\
## تمرین B1 — کارآگاه ویژگی‌ها (۱ نمره)

یک دوست می‌خواهد **قبولی یک دانش‌آموز در آزمون** را پیش‌بینی کند و این ویژگی‌ها را پیشنهاد می‌دهد:

`["name", "hours_studied", "favorite_color", "previous_score", "shoe_size"]`

فقط ویژگی‌هایی را که واقعاً می‌توانند به پیش‌بینی قبولی کمک کنند، به‌صورت یک **لیست** پایتونی بنویس.
(راهنما: آیا مدل از اسمِ کسی چیزی مفید یاد می‌گیرد؟)
"""),
code("""\
B1_good_features = ["hours_studied", "previous_score"]  # <-- پاسخ تو (لیستی از رشته‌ها)
"""),
md("""\
## تمرین B2 — دیتاست خودت را بساز (۱ نمره)

حالا تو معلمی. یک دیتاست کوچک (یک DataFrame پانداسی) از **حداقل ۴ حیوان** بساز
با ویژگی‌های `["size", "can_fly"]` و برچسب `"animal"`. شرایط:

- دقیقاً همین ۳ ستون،
- حداقل ۴ سطر، هر کدام یک حیوان متفاوت،
- `size` یکی از `"small"`، `"medium"`، `"large"` باشد و `can_fly` عدد `0` یا `1`.
"""),
code("""\
B2_animals = pd.DataFrame({
    "size":     ["small", "large", "medium", "small"],
    "can_fly":  [0, 0, 0, 1],
    "animal":   ["cat", "elephant", "dog", "sparrow"],
})
# ^^^ با حیواناتِ خودت جایگزین کن. اسم ستون‌ها دقیقاً همین بماند: size, can_fly, animal
"""),
md("""\
## تمرین B3 — سه خط جادویی (۱ نمره)

برای آموزش یک درخت تصمیم روی دیتاست حیواناتِ خودت، جاهای خالی را کامل کن.
"""),
code("""\
B2_animals_num = B2_animals.copy()
B2_animals_num["size_num"] = B2_animals_num["size"].map({"small": 0, "medium": 1, "large": 2})

B3_X = B2_animals_num[["size_num", "can_fly"]]     # ویژگی‌ها
B3_y = B2_animals_num["animal"]                    # برچسب

B3_model = DecisionTreeClassifier(random_state=42)  # ۱. انتخاب دانش‌آموز
B3_model.fit(B3_X, B3_y)                            # ۲. درس خواندن
B3_prediction = B3_model.predict([[1, 0]])[0]       # ۳. سؤال: اندازه=متوسط، پرواز=۰ ← ؟
print("مدل می‌گوید حیوان متوسطِ بی‌پرواز این است:", B3_prediction)
"""),
md("""\
## تمرین B4 — فالگیر بقا (۱ نمره)

مدل تایتانیکِ خودت را آموزش بده (مثل کلاس، با `max_depth=3` و `random_state=42`)
و بقا را برای این مسافر پیش‌بینی کن: **کلاس ۳، پسر ۱۲ ساله، کرایهٔ ۷.۵.**

بعد جواب بده: او زنده ماند؟ عدد `1` (زنده ماند) یا `0` (نماند) را در `B4_answer` بگذار.
"""),
code("""\
# داده از قبل بارگذاری شده (titanic). مثل سلول A7، دقیقاً X و y را بساز.
B4_X = X.copy()
B4_y = y.copy()

B4_model = DecisionTreeClassifier(max_depth=3, random_state=42)
B4_model.fit(B4_X, B4_y)

new_passenger = pd.DataFrame([{"pclass": 3, "age": 12, "fare": 7.5, "is_female": 0}])
B4_answer = int(B4_model.predict(new_passenger)[0])   # باید 1 یا 0 باشد
print("فالگیر می‌گوید:", "زنده می‌ماند" if B4_answer == 1 else "زنده نمی‌ماند")
"""),
md("""\
---

# تحویل بده!

وقتی هر چهار تمرین از داوری سربلند بیرون آمد:
1. این نت‌بوک را ذخیره کن.
2. آن را در مخزن گیت‌هاب دوره‌ات commit کن (معلمت نشانت می‌دهد، یا راهنمای کلاس را ببین).
3. به خانواده‌ات نشان بده: *«امروز یک هوش مصنوعی ساختم.»* — چون واقعاً ساختی.
"""),
]

part_b_solution_note = md("""\
> **یادداشت مدرس (نسخهٔ پاسخ):** سلول‌های زیر پاسخ درست را دارند.
> در نسخهٔ دانش‌آموز همین سلول‌ها TODOهای راهنما دارند.
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

notebook_cells = part_0 + part_a + part_b_student + part_c
solution_cells = part_0 + part_a + [part_b_solution_note] + part_b_student + part_c

write(os.path.join(os.path.dirname(__file__), "s01_notebook.ipynb"), notebook_cells)
write(os.path.join(os.path.dirname(__file__), "s01_notebook_solution.ipynb"), solution_cells)
