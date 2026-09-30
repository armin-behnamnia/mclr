---
marp: true
theme: mlcourse-blue-fa
paginate: true
---

<!-- _class: lead -->
<!-- _paginate: false -->

# یادگیری ماشین چیست؟

## روز اول — تو یک هوش مصنوعی می‌سازی

**بخش ۱ · جلسهٔ ۱**

*تا پایان امروز، تو یک مدل یادگیری ماشین آموزش می‌دهی.*

![hero](shared_hero.png)

<!--
INSTRUCTOR — Session 1 of 32. 60 min teaching + 60 min problem-solving.
BEFORE CLASS: test PART 0 demo cells; notebook runs top-to-bottom; assets exist.
TIMING: hook 0-5, big question 5-10, fruit game 10-20, supervised 20-30, Titanic 30-40, magic lines 40-50, quiz 50-55, handout 55-60.
-->

---
<!-- _class: hook -->

# نمایش ویژهٔ هوش مصنوعی

# یک دمو. یک خط. یک سؤال.

*خوب نگاه کن.*

<!--
[0:00] THE HOOK — run the single PART 0 demo cell, showmanship, dim lights.
SAY: "By the end of today, YOU will build what you are about to see."
FALLBACK: narrate from notes, never skip the hook.
-->

---
<!-- _class: hook -->

# بازیِ حیوانات

ماشین فقط این را می‌بیند: **۸ حیوان با برچسب**

هر حیوان = دو عدد (وزن، طول گوش) + یک پاسخ

*هیچ قانونی به آن داده نشده. هیچ.*

<!--
[RUN: PART 0 demo cell, stage 1] Show the 8-row table — this is ALL the machine sees.
SAY: "8 animals. Two numbers each, plus the answer. Nobody wrote a single rule."
EXPECT: "so what? it's just a table" — perfect, let them underestimate it.
-->

---
<!-- _class: hook -->

# خطِ ماشین

از دلِ همان ۸ سطر، ماشین **خودش** یک خط کشید.

پشتِ خط: گربه‌ها. جلوی خط: سگ‌ها.

**«این خط را چه کسی کشید؟!»**

![art](../../assets/animal_game.png)

<!--
[RUN: PART 0 demo cell, stage 3 — the scatter plot] The machine draws its own red dashed line.
SAY: "No human drew this line. The machine found it in those 8 rows."
EXPECT: "where did the line come from?!" — do NOT explain yet. Slide 9 answers it.
-->

---
<!-- _class: hook -->

# حالا امتحانش کنیم

حیواناتی که ماشین **هرگز ندیده:**

گرگ ← سگ. گربهٔ همسایه ← گربه. **درست!**

توله‌سگ ← گربه؟! فیل ← سگ؟!

*یک سؤال ساده، جاهای خالیِ خط را پر می‌کند.*

<!--
[RUN: PART 0 demo cell, stage 4] Wolf right, neighbor cat right... PUPPY = cat (WRONG! it's a 2kg dog). ELEPHANT = dog (it only knows two words — laugh).
THE MONEY MOMENT: "The line is a GUESS from 8 examples. Near the line, the guess breaks. More examples = better line — that's Session 2."
CLOSING: "One idea behind all of this. You'll build your own before you leave today."
-->

---

# سؤال بزرگ

چطور یک کامپیوتر را باهوش کنیم؟

<!--
[5:00] Segment A: rules vs learning. DRAW both boxes on the board — they stay ALL session.
Next slide's interaction is the core; don't lecture through it.
-->

---

راه اول — روش قدیمی: نوشتن قاعده‌ها

`داده + قاعده‌ها ← پاسخ`

انسان هر قاعده را با دست می‌نویسد.

«اگر سبیل داشت و خرخر می‌کرد، پس گربه است»

<!--
Board box 1: data + RULES = answers.
SAY: "For 50 years, smart people wrote thousands of IF-THEN rules. Worked... until it didn't."
Transition: "Let's try it ourselves. Cats. Easy, right?"
-->

---

# مشکل نوشتن قاعده

حالا نوبت شماست: قاعده‌هایی بنویسید که گربه را بشناسد.

گربهٔ بدون مو؟ گربه در لباس؟ حیوان کوچک؟!

هیچ‌کس نمی‌تواند به‌اندازهٔ کافی قاعده بنویسد!

![cat rules](../../assets/cat_rules.png)

<!--
INTERACTION (3-4 min): students propose cat rules, you counter each.
"has fur" = hairless cat; "whiskers" = walrus; "small cute" = corgi puppy.
Concede: "This is why we don't write rules. We show examples."
-->

---

# راه ۲ — یادگیری ماشین

`داده + پاسخ‌ها ← قاعده‌ها`

ماشین قاعده را کشف می‌کند.

**همان خطِ قرمزِ اولِ جلسه.**

<!--
THE REVEAL — point back at the hook: those 8 animals WERE the examples with answers; the red line WAS the rule it discovered. The mystery is solved.
Board box 2 under box 1: data + answers = RULES.
CHECK (cold call): "What does the machine get and produce?" — examples with answers = rules.
Point back to the red line at least 5 times today.
-->

---

<!-- _class: definition -->

# هوش مصنوعی در برابر یادگیری ماشین

**هوش مصنوعی** یعنی آرزوی بزرگ: ماشین‌هایی که هوشمندانه رفتار می‌کنند

**یادگیری ماشین** یعنی راه اصلی رسیدن به آن آرزو: یادگیری از روی داده‌ها

<!--
[~7:00] 60 seconds max. [MISCONCEPTION] AI and ML are NOT synonyms.
Analogy: AI = becoming a doctor (dream); ML = medical school (how).
-->

---

# بازی میوه 

| رنگ | اندازه | بافت | ← میوه |
|------|-------|---------|--------|
| قرمز | متوسط | صاف | ؟ |
| زرد | دراز | صاف | ؟ |
| بنفش | ریز | چروک | ؟ |

*ستون پاسخ را بپوشان. از سرنخ‌ها میوه را حدس بزن.*

<!--
[10:00] Segment B: fruit game. Cover the fruit column, read clues, class shouts labels. 2 min, high energy.
RUN cell A1: this table IS a DataFrame.
Next: which clue is most useful — vote.
-->

---
<!-- _class: definition -->

# واژگان جدید 

**ویژگی** = یک سرنخ *(یک ستون)*

**برچسب** = پاسخ *(ستونی که می‌خواهیم پیش‌بینی کنیم)*

**نمونه** = یک سطر = سرنخ‌ها + پاسخ

<!--
WRITE on board (never erased): feature, label, example.
Hooks: feature = fingerprint; label = the answer; example = one solved exercise.
[MISCONCEPTION] the label is hidden at quiz time, not read by the model.
CHECK: "3 Titanic features + the label?"
-->

---

# کدام ویژگی مهم است؟

رنگ؟ اندازه؟ بافت؟

کدام سرنخ برای حدس زدن میوه بهتر جواب می‌دهد؟

*(رأی بدهید. مناقشه کنید. جواب غلطی وجود ندارد — هنوز.)*

<!--
INTERACTION: hands-up vote per feature, quick debate.
SAY: "You just did data science. Session 9 computes this as feature importance."
RUN cell A2 — students record their guess (revisited in Session 9).
-->

---

# یادگیری نظارت‌شده 

یادگیری از نمونه‌هایی **که پاسخ دارند.**

مثل درس خواندن با پاسخ‌نامه —
بعد رفتن سر **آزمون جدید.**

<!--
[20:00] Segment C. LIVE MINI-GAME: 4 solved fruit examples, then a 5th with hidden label — class predicts.
SAY: "You just did supervised learning. Personally."
RUN cell A3: study table vs quiz table.
-->

---

# چرا «نظارت‌شده»؟

هیچ انسانی مدل را تماشا نمی‌کند!

یعنی **داده‌ها پاسخ دارند.**

*(تاریخ یک کلمهٔ عجیب انتخاب کرده. )*

<!--
[MISCONCEPTION] "supervised" does NOT mean a person watches the model — the data has answers.
Use the laugh, then CHECK: "Why 'supervised'?" — examples come with answers.
-->

---

# تایتانیک

۸۹۱ مسافر، ۸۹۱ سطر.

![art](../../assets/titanic_ship.png)

هر سطر، یک زندگی است؛ هر ستون، یک سرنخ.

اگر جای آن‌ها بودی، زنده می‌ماندی؟

<!--
[30:00] Segment D: Titanic as pictures. Students follow cells A4-A6.
NARRATE THE HISTORY while plotting — the story is the engine.
A4: 891 passengers, each row a life.
-->

---

# داده به‌صورت عکس 

![نمودار میله‌ای: تعداد بقا](../../assets/survival_counts.png)

*همیشه قبل از هر کاری، داده‌ات را ببین.*

<!--
[RUN cell A5] More died than survived — 549 vs 342.
RULE (course-wide): every dataset gets PLOTTED before MODELED.
-->

---
<!-- _class: wow -->

# بقا بر حسب جنسیت و کلاس 

![بقا بر حسب جنسیت و کلاس](../../assets/survival_by_sex_class.png)

حدود ۷۴٪ زنان زنده ماندند؛ اما فقط ۱۹٪ از مردان کلاس ۳.

<!--
[RUN cell A6] THE PUNCHLINE PLOTS. Let students read the bars first.
ASK: "Which feature matters for survival?" — sex, then class.
SAY: "A rich woman in 1912 had close to a survival ticket."
-->

---
<!-- _class: hook -->

# لحظهٔ جادویی

در ۳ خط، یک هوش مصنوعی بساز

![art](../../assets/magic_lines.png)

*با من تایپ کن. واقعاً — نت‌بوک را باز کن و تایپ کن.*

<!--
[40:00] Segment E — emotional peak. Students TYPE ALONG cells A7-A9 (not just watch).
A7: X and y separated — "line 0 is setup, not magic."
CEREMONY before fit(): "On three, everyone say LEARN."
-->

---
<!-- _class: codespot wow -->

# سه خط جادویی 

```python
model = DecisionTreeClassifier(max_depth=3) # ۱. انتخاب دانش‌آموز
model.fit(X, y) # ۲. درس خواندن
model.predict(new_passengers) # ۳. سؤال پرسیدن
```

**بساز ← یاد بده ← پیش‌بینی کن**

*این ریتم، کل یادگیری ماشین است. نه فقط امروز.*

<!--
[RUN cell A8, students typing] Write the 3 lines LARGE on the board.
create = pick a student; fit = let it study; predict = ask, label hidden.
SAY: "Every model you'll ever meet follows these three lines."
-->

---

چه چیزی یاد گرفت؟

![درخت تصمیم](../../assets/decision_tree.png)

همان طور که می‌بینی فقط چند سؤال ساده است؛ حتی خودت هم می‌توانستی بکشیش.

<!--
[RUN cell A9] Predict for a volunteer: "Would Sara, 2nd class, age 13, survive?"
Then the tree picture: "Just yes/no questions. You could draw this.
Who chose the questions? The machine did."
-->

---
<!-- _class: dark -->

یک حرف آخر

این مدل یک **مغز نیست.**

فقط الگویی از سؤال‌ها پیدا کرده که با بقا جور در می‌آید.

و همین، خودش شگفت‌انگیز است.

<!--
Slow, quiet, honest moment.
SAY: "A mirror of 714 examples. Good data, good mirror. Unfair data, unfair mirror."
Then snap energy back up for the quiz.
-->

---
<!-- _class: quiz -->

![band](shared_band.png)

# امروز یاد گرفتی 

- قاعده ← پاسخ، یا پاسخ ← **قاعده**
- **ویژگی** (سرنخ) و **برچسب** (پاسخ)
- **یادگیری نظارت‌شده** = نمونه‌های همراه با پاسخ
- سه خط جادویی: **بساز ← یاد بده ← پیش‌بینی کن**

<!--
[50:00] CONSOLIDATION — cold call, friendly. One question per student:
get+produce? feature/label? 3 magic lines? why women survived?
If anyone stumbles on Q1-3, re-explain NOW.
-->

---

# تحویل امشب

اولین نت‌بوک یادگیری ماشین‌ات ← **مخزن گیت‌هاب تو**

«اگر آن روز سرِ تایتانیک بودم، زنده می‌ماندم؟» — مدلی که خودت ساختی جواب می‌دهد

<!--
[55:00] THE SHIP + handout. Explain the loop OUT LOUD:
4 problems tonight (20-30 min) = next session we solve them TOGETHER from YOUR attempts.
Judge: python judge/run.py s01_notebook.ipynb
-->

---
<!-- _class: handout -->

# تمرین‌های خانه (۴ تا)

1. **B1** کارآگاه ویژگی‌ها
2. **B2** دیتاست خودت را بساز
3. **B3** سه خط جادویی — طبقه‌بند حیوانات خودت
4. **B4** پیش‌بینی‌گر بقا

مهلت: قبل از جلسهٔ بعدی (حل مسئله).

<!--
One sentence of story per problem:
B1 dumb features under scrutiny; B2 invent your own dataset; B3 magic lines on YOUR data; B4 the 12-year-old boy verdict.
Deadline: before the problem-solving session.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->

# جلسهٔ بعد

تمرین‌هایتان را همان‌جا، با هم حل می‌کنیم.

هر کاری که امتحان کردید را بیاورید؛ حتی کدهای خراب را.

آن‌ها سوخت جلسهٔ بعدی ما هستند. 

![rocket](shared_closing.png)

<!--
[60:00 — end on time] "Tonight your repo goes live. Show your family: I built an AI today."
CLIFFHANGER: "Who chose the tree's questions? Next time: you fix the machine's mistakes."
AFTER CLASS (48h): fill the retro note in the session README.
-->
