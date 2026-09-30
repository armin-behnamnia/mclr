# Machine Learning Course for Middle-School Students

**Audience:** Middle-school students who have completed Python and Data Analytics courses
**Duration:** 32 sessions × 2 hours (1 hour teaching + 1 hour hands-on lab)
**Course motto:** *"Don't just learn ML. Ship ML."*

---

## The Four Pillars (design rules behind every session)

### 1. Attention & Enjoyment — "Never a boring minute"
- **Every session opens with a Hook** — a 5-minute wow-demo, game, or challenge *before* any theory. Curiosity first, explanation second.
- **The 15-minute rule:** no lecture segment longer than 15 minutes without a visual, interaction, or live demo.
- **Energy pacing:** heavy-theory sessions always alternate with visual/play sessions (see pacing map below). Never two "dry" sessions in a row.
- **No hand-drudgery:** hand computation is capped at 5 minutes and always as a game; the computer takes over the moment the concept lands.
- **Visual everything:** every dataset is plotted before it's modeled. Every model's decision boundary, tree, or embedding space is *drawn*. Students should always be able to *see* what the model is doing.
- **Relatable data only:** no abstract datasets. Sports, games, music, social media, school life, movies.
- **Failure is fun:** we celebrate the funniest model failures (a tree that thinks all passengers died, a classifier fooled by a banana) — debugging is framed as detective work, not punishment.

### 2. Solid Flow & Specific Goals
- **Course narrative arc:** *Player → Builder → Specialist → Engineer*. The course tells one continuous story: "you play with AI (S1), you build AI (S2–20), you specialize (S21–30), you deploy AI like a professional (S31–32)."
- **Every session has exactly one goal**, stated at the start in student language: *"By the end of today, YOU will be able to ___."*
- **Every session ends with a Ship** — a small concrete artifact (a plot, a working model, a deployed demo link) committed to the student's growing portfolio.
- **Each block has one flagship outcome** (below) and opens with a "map session" showing where students are and what's next.
- **Concepts spiral:** each new concept is introduced exactly when it solves a *felt problem* from the previous session. Nothing is taught "for later."

### 3. Industry Readiness — practical expertise
- **Portfolio-first:** from Session 1, every student works in their own GitHub repo. Weekly commits build a public portfolio of 25+ artifacts by Session 32.
- **Professional workflow, kid-scale:** notebooks for exploring, small scripts for running, Git for saving, README for explaining. Done every session, so it becomes muscle memory.
- **Real tools, not toys:** scikit-learn, pandas, matplotlib, Hugging Face, Streamlit, n8n, RAGFlow — the same tools used in industry.
- **Deployment from day 10:** models are not just trained — they are *deployed* as shareable web apps (Streamlit / Hugging Face Spaces) that students show to family and friends.
- **Communication:** every project ends with a short written + spoken explanation. Industry insight: *the person who explains best wins.*

### 4. The Feeling of Power — overwhelmed by what AI can do
- **Scheduled wow moments** (at least one per session, major ones flagged below ): live speech recognition on their own voice, an AI that reads their handwriting, image generation, a chatbot answering questions from their own documents, models beating human guesses.
- **"Beat the human" challenges:** students predict labels by hand, then watch the model beat them — feeling the power viscerally.
- **Personal relevance:** they build AI for *their* world — a music genre classifier, a meme categorizer, a "will I pass?" predictor, a voice-controlled gadget.
- **Demo Day finale:** the course ends with a public showcase where students demo real deployed AI products.

---

## Course Map (one story, four acts)

| Block | Story role | Flagship outcome |
|---|---|---|
| **1 (S1–10)** — ML through Random Forest | *"You can build a working AI in one afternoon"* | A deployed, shareable prediction web app + a GitHub portfolio underway |
| **2 (S11–20)** — Classical models & theory | *"Now you understand WHY it works — and can beat your first model"* | A rigorous model bake-off with a professional-style experiment report |
| **3 (S21–30)** — Applications | *"AI sees, hears, reads, and connects — and so do you"* | 3 deployed domain projects + a capstone in the student's chosen domain |
| **4 (S31–32)** — Workflows & frontier | *"You can wire AI into the real world"* | A live n8n automation + a RAGFlow chatbot over their own docs + Demo Day |

---

## Block 1 — All of ML Through One Model: Decision Tree → Random Forest (Sessions 1–10)

**Block goal:** Learn every core ML concept by building, breaking, and deploying one intuitive model. **Flagship: a deployed prediction web app + GitHub portfolio.**

**S1 — Day One, You Build an AI **
- **Goal:** I can train a working ML model and show it to my family.
- **Hook:** The Animal Game — the machine sees 8 labeled animals (weight, ear length → cat/dog), draws its own separating line, then answers animals it has never seen — getting the chihuahua hilariously wrong. "By the end of today, you build this yourself."
- **Teaching:** Rules vs learning from examples; features & labels; supervised learning (just this one idea today). Titanic dataset shown as pictures, not tables.
- **Lab:** Train a decision tree in 3 lines of sklearn on Titanic; test it on imaginary passengers they invent; **create their GitHub repo and push their first notebook**.
- **Ship:** Repo link + a model that answers "would I have survived the Titanic?"

**S2 — The 20-Questions Machine **
- **Goal:** I can read, draw, and hand-build a decision tree.
- **Hook:** Class plays 20-questions; teacher reveals they were a decision tree in disguise all along.
- **Teaching:** Nodes, branches, leaves; splits partition data; visualize trees with `plot_tree`.
- **Lab:** Build a tree on paper to classify animals, then test classmates' trees on surprise examples — celebrate the funniest failures.
- **Ship:** Photo of their hand-drawn tree (committed to the repo).

**S3 — How the Tree Picks Its Questions**
- **Goal:** I can explain why one question is better than another.
- **Hook:** Two boxes of mixed colored balls — which single question un-mixes them fastest?
- **Teaching:** Purity as "sorted-ness"; entropy as surprise (with a slot-machine visual); information gain.
- **Lab:** 5-minute split-ranking game (which question wins?), then verify instantly in code on a bigger dataset.
- **Ship:** An annotated plot showing the tree's best first split.

**S4 — The Exam Cheat Test (Train vs Test) **
- **Goal:** I can prove whether my model actually learned or just memorized.
- **Hook:** A "student" who memorizes all exam answers — will they pass a *new* exam?
- **Teaching:** Train/test split; learning = performing on unseen data.
- **Lab:** "Beat the human" — students predict Titanic survival by intuition, model beats them; they compute train vs test accuracy and explain the gap.
- **Ship:** Accuracy comparison chart, human vs model.

**S5 — The Overfitting Monster **
- **Goal:** I can diagnose and cure overfitting.
- **Hook:** Live experiment projected on screen: a tree growing deeper and deeper, accuracy climbing to 100%... then collapsing on new data. Class predicts the collapse.
- **Teaching:** Deep vs shallow trees; bias/variance via cartoons (blind sniper vs wobbly sniper).
- **Lab:** The depth experiment — students run `max_depth` 1→20, plot train/test curves, find the sweet spot themselves.
- **Ship:** The famous overfitting curve, made by them.

**S6 — Practice Exams (Hyperparameters & Cross-Validation)**
- **Goal:** I can tune a model fairly.
- **Hook:** "Your model's settings are dials. Who turns the dials? You. But how do you know you turned them right?"
- **Teaching:** Parameters vs hyperparameters; k-fold CV as several practice exams.
- **Lab:** Tune the Titanic forest with `GridSearchCV`; leaderboard on screen — best score wins bragging rights.
- **Ship:** A tuned model + their chosen settings with a one-paragraph defense.

**S7 — Garbage In, Garbage Out**
- **Goal:** I can clean data like a professional and avoid data leakage.
- **Hook:** Show a dataset riddled with missing values and typos — "would you trust a model trained on this?"
- **Teaching:** Missing values, one-hot encoding, outliers; data leakage as "accidentally studying the answer key."
- **Lab:** Clean a messy real dataset end-to-end; retrain; before/after comparison on screen.
- **Ship:** A cleaning checklist (their own, written by them) added to their repo.

**S8 — The Wisdom of the Crowd **
- **Goal:** I can build a Random Forest and explain why it beats one tree.
- **Hook:** Guess-the-jellybeans-in-the-jar: one guess vs the class average. The crowd wins.
- **Teaching:** Bootstrap sampling; random feature choice; averaging kills wobble.
- **Lab:** One tree vs 100 trees; watch the accuracy and stability jump; animate individual trees voting.
- **Ship:** "1 tree vs N trees" performance chart.

**S9 — When Accuracy Lies **
- **Goal:** I can evaluate a model beyond accuracy and explain it to a non-expert.
- **Hook:** A "99% accurate" fraud detector that catches zero frauds. How?
- **Teaching:** Confusion matrix; precision/recall with doctor & fire-alarm analogies; feature importance.
- **Lab:** Imbalanced fraud dataset: build the confusion matrix, fix the lying metric, interrogate feature importances ("does ticket price *really* matter?").
- **Ship:** An evaluation one-pager for their fraud model.

**S10 — SHIP IT: Your First Deployed AI Product (map session)**
- **Goal:** I can take a model from raw data to a live web app anyone can use.
- **Hook:** Show last year's student apps / a live deployed example. "Yours goes live today."
- **Teaching:** The full ML workflow in one recap; deploying with Streamlit Cloud / Hugging Face Spaces; writing a README that sells your project.
- **Lab:** Deploy their Titanic (or student-performance) predictor as a shareable web app with sliders and buttons; write the README; final push.
- **Ship:** **A live URL to their first AI product + portfolio with 10 artifacts. Show family and friends tonight.**

**Energy pacing check:** heavy sessions (3, 6, 7) are sandwiched between visual/game sessions. Every session has a projected live element.

---

## Block 2 — Classical Models & Theory: Why It All Works (Sessions 11–20)

**Block goal:** Generalize every Block-1 concept; master the classical model toolbox; run experiments like a professional. **Flagship: the Model Bake-Off with a full experiment report.**

**S11 — The Straight Line That Predicts (Linear Regression)**
- **Goal:** I can fit a line to data and use it to predict numbers.
- **Hook:** Predict the price of a house / the score of the next football match from one number. Can a straight line do it?
- **Teaching:** Loss as "total miss distance"; predictions as weighted sums (straight from math class).
- **Lab:** Fit-and-see: interactively drag a line until the loss stops shrinking, then let `LinearRegression` do it; plot residuals.
- **Ship:** House-price (or game-score) predictor notebook.

**S12 — Learning by Walking Downhill **
- **Goal:** I can implement gradient descent — the engine inside almost all of AI.
- **Hook:** A blind hiker in foggy mountains, feeling the slope with their feet — that's how ChatGPT learned. Today you build that hiker.
- **Teaching:** Loss landscape; step size (learning rate); too big = leap over the valley, too small = never arrive.
- **Lab:** 15 lines of code: gradient descent on a line; animate the descent; break it with a huge learning rate (on purpose — the explosion is the fun part).
- **Ship:** An animated descent GIF in their repo.

**S13 — The Probability Machine (Logistic Regression)**
- **Goal:** I can build a classifier that outputs calibrated confidence.
- **Hook:** "The tree says YES or NO. Wouldn't you rather know it's 87% sure?"
- **Teaching:** Sigmoid squashing; decision boundary; cross-entropy as punishing confident wrong answers.
- **Lab:** Train logistic regression on their Block-1 dataset; draw the boundary; tree vs line — interpretability debate.
- **Ship:** Decision-boundary plot + 3-sentence comparison of tree vs logistic regression.

**S14 — Keep It Simple (Regularization & Bias–Variance)**
- **Goal:** I can cure overfitting with math instead of pruning.
- **Hook:** Return of the overfitting monster — but now you fight it with a dial called λ.
- **Teaching:** General bias-variance picture (S5, now formal); L1/L2 as fines for complicated models.
- **Lab:** Sweep regularization on logistic regression; plot the U-shaped validation curve; connect it back to tree depth.
- **Ship:** "One disease, two cures" mini-poster (depth vs λ).

**S15 — You Are Your Neighbors (k-NN) **
- **Goal:** I can use similarity to classify and explain when scaling matters.
- **Hook:** The class seating chart predicts your favorite game — "tell me who your neighbors are."
- **Teaching:** Distance in feature space; the k dial; why trees ignore scale but neighbors don't.
- **Lab:** The scaling disaster: run k-NN on unscaled data (it fails hilariously), then scaled (it works); paint decision regions with matplotlib.
- **Ship:** Before/after scaling decision-region maps.

**S16 — Drawing the Widest Street (SVM)**
- **Goal:** I can explain margins and why kernels unlock impossible problems.
- **Hook:** Two rival groups on a field — separate them with the widest possible no-man's-land.
- **Teaching:** Maximum margin; support vectors; kernels as lifting data into 3D where a flat knife separates them (visual demo with paper sheets rising).
- **Lab:** Linear vs RBF kernel on moons and circles datasets; draw the margin street.
- **Ship:** The "impossible dataset, solved" plot.

**S17 — The Spam Detective (Naive Bayes) **
- **Goal:** I can build a working spam filter from scratch reasoning.
- **Hook:** Real spam messages on screen — can they spot the pattern? The computer does it in milliseconds.
- **Teaching:** Probability as counting fractions; Bayes rule via the classic doctor-test puzzle; the naive assumption.
- **Lab:** Build a spam classifier; extract the top "spam-screaming" words; try to fool each other's filters with tricky messages.
- **Ship:** Working spam filter + a screenshot of the words that gave spam away.

**S18 — Nobody Labeled the Data (k-Means Clustering) **
- **Goal:** I can discover hidden groups without any labels.
- **Hook:** Hand the class 200 uncategorized songs or customers — "find the natural tribes." No answer key exists.
- **Teaching:** Unsupervised learning; assign-move-repeat loop (animated); elbow method.
- **Lab:** Cluster songs/customers/colors; name the clusters themselves; find where clustering fails (elongated shapes).
- **Ship:** Their named-cluster visualization + cluster interpretations.

**S19 — Professional Pipelines & Fair Experiments**
- **Goal:** I can run a leakage-free, reproducible experiment — the industry way.
- **Hook:** Reveal a shocking fact: a famous model scored 99% because of leakage. Could yours be cheating too?
- **Teaching:** scikit-learn `Pipeline`; preprocessing *inside* CV; reproducibility (random seeds); comparing models fairly.
- **Lab:** Build imputer+scaler+model pipelines; run a fair bake-off of every model from S11–S18 on one dataset.
- **Ship:** Bake-off leaderboard table in a proper experiment notebook.

**S20 — THE BAKE-OFF (project session) (map session)**
- **Goal:** I can design, run, and communicate a complete ML experiment.
- **Hook:** "Same data. Same rules. Different teams, different models. One winner — chosen by fair evaluation AND quality of explanation."
- **Teaching:** How to write an experiment report: question, data, method, results, conclusion — with examples of good and bad write-ups.
- **Lab:** Teams defend their model choices; class leaderboard; votes for best result *and* best explanation.
- **Ship:** **A professional experiment report in the portfolio — the artifact that most resembles real industry work.**

---

## Block 3 — Applications: AI That Sees, Hears, Reads, and Connects (Sessions 21–30)

**Block goal:** Transfer all skills to text, images, audio, and graphs; build deployed products in each domain. **Flagship: 3 domain products + capstone kickoff.**
*Pacing rule for this block: every domain = one "understand the data" session + one "ship the product" session. Students deploy something every other session.*

**S21 — Teaching a Computer to Read (Text → Numbers) **
- **Goal:** I can turn text into numbers that models understand.
- **Hook:** An AI sorts 10,000 movie reviews into positive/negative — students race it and lose.
- **Teaching:** Tokenization; bag of words; TF-IDF; reusing Naive Bayes (S17).
- **Lab:** TF-IDF by hand on 3 sentences, then at scale; find each review's most "influential" words, highlighted.
- **Ship:** Sentiment classifier on their favorite thing (games, songs, movies).

**S22 — Words That Know Their Meaning **
- **Goal:** I can use embeddings and explain why "king − man + woman ≈ queen".
- **Hook:** The king/queen vector magic trick on screen; then: type any two words, watch their similarity score — students test their own theories live.
- **Teaching:** Meaning as location; nearest neighbors; from static embeddings to LLM embeddings (conceptual bridge to ChatGPT).
- **Lab:** Explore an embedding space (neighbors, analogies); classify with embeddings vs TF-IDF; "does meaning beat counting?"
- **Ship:** Their embedding exploration notebook + a written answer to "which works better and why."

**S23 — Stacked Neurons: A Tiny Brain **
- **Goal:** I can build and train a neural network and connect it to gradient descent.
- **Hook:** TensorFlow Playground live on the projector — a network learning a spiral in front of their eyes.
- **Teaching:** Neuron = weighted sum + squash; layers build features from features; S12's gradient descent, applied through layers.
- **Lab:** Students solve spiral & circle datasets themselves in the Playground by designing architectures; then train a tiny real network in Keras.
- **Ship:** Screenshot of their solved spiral + their architecture description.

**S24 — How AI Sees (Images → Grids of Numbers) **
- **Goal:** I can explain convolutions and process images in code.
- **Hook:** Project a photo, then its raw pixel numbers, then progressively blur/edge-detect it live — "this is what the machine sees."
- **Teaching:** Pixels & channels; filters as pattern detectors; pooling; CNN hierarchy (edges → shapes → objects).
- **Lab:** Apply and *see* filters on their own photos; build and count the parameters of a tiny CNN.
- **Ship:** Their photo through 4 different filters, side by side.

**S25 — SHIP: The Image Classifier (product session)**
- **Goal:** I can fine-tune a pretrained CNN and deploy an image classifier app.
- **Hook:** Show a deployed "hotdog / not hotdog"-style app. "Yours can be anything you want."
- **Teaching:** Transfer learning as borrowing a trained network's eyes; freezing layers; evaluation with Block-1 metrics (confusion matrix returns!).
- **Lab:** Fine-tune on two student-chosen classes (cats/dogs, memes, shoes...); plot training curves; **deploy to Hugging Face Spaces**.
- **Ship:** **Live image classifier URL — point your phone camera at it.**

**S26 — How AI Hears (Sound → Numbers) **
- **Goal:** I can turn audio into spectrograms and read them.
- **Hook:** The teacher's voice becomes a picture on screen; different words make visibly different patterns — students match spectrograms to words like a quiz game.
- **Teaching:** Waves → samples; spectrograms as sound pictures; MFCC fingerprints; "audio becomes vision, so we reuse CNNs."
- **Lab:** Record their own voices; plot spectrograms; play the spectrogram-matching game; find their own voice's signature.
- **Ship:** Their voice's spectrogram + a gallery of the class's voices.

**S27 — SHIP: The Speech Command Recognizer (product session)**
- **Goal:** I can build and deploy a model that understands spoken commands.
- **Hook:** A live voice-controlled demo — clap-on/clap-off for a virtual light. "Voice assistants: demystified today."
- **Teaching:** Full pipeline: audio → spectrogram → CNN → command; where Siri/Alexa live in this picture.
- **Lab:** Train on Google Speech Commands (yes/no/up/down/stop/go); test with their *own voices*; deploy a demo.
- **Ship:** **A recognizer that obeys their voice — and breaks on their friend's accent (great discussion material).**

**S28 — The World Is a Network (Graphs) **
- **Goal:** I can represent networks as data and measure importance.
- **Hook:** The class builds its real friendship graph live on screen; the "most connected person" is computed in front of them.
- **Teaching:** Nodes, edges, adjacency matrices; social networks, maps, the web; PageRank as importance flowing along edges.
- **Lab:** Build and analyze the class friendship graph; degree, PageRank; predict future friendships by intuition.
- **Ship:** Their class network visualization.

**S29 — Machine Learning on Networks**
- **Goal:** I can run node classification and explain message passing.
- **Hook:** "If your friends all love a game, the network predicts you will too. TikTok does this to you every day."
- **Teaching:** Node features + structure; message passing (friends influence friends); a one-paragraph conceptual tour of GNNs.
- **Lab:** Zachary's karate club with a tiny GNN; watch predictions spread along the graph as they add/remove edges.
- **Ship:** Karate-club experiment notebook.

**S30 — Capstone Kickoff: Choose Your Power (map session)**
- **Goal:** I can scope a real ML project from my own life or interests.
- **Hook:** Recap reel: everything they've shipped this course (their own URLs). "One last build. Your choice of superpower: text, vision, sound, or networks."
- **Teaching:** Project scoping the industry way: a question narrow enough to answer in 4 sessions; picking data; defining success before starting.
- **Lab:** Teams pick domain + question; teacher "greenlights" scopes (too big → shrink it); data sourced; plan written.
- **Ship:** Approved capstone proposal (1 page).

---

## Block 4 — Wiring AI Into the World + The Frontier (Sessions 31–32)

**S31 — AI Workflows: n8n + RAGFlow **
- **Goal:** I can automate real tasks by wiring LLMs into workflows and chatbots.
- **Hook:** A live n8n automation runs during class: an email arrives → AI summarizes and files it → notification — zero human clicks. "This took 10 minutes to build."
- **Teaching:** Workflow thinking (triggers → steps → outputs); n8n hands-on; RAGFlow = LLM + *your* documents (reusing S22 embeddings: "the chatbot searches before it speaks").
- **Lab:** Build a working n8n flow (e.g., text in → AI processes → sheet logs it); then upload their capstone docs (or school notes) to RAGFlow and grill it with questions answerable *only* from the docs.
- **Ship:** **A live automation + a chatbot over their own documents.**

**S32 — DEMO DAY: The Frontier & Your Next Step **
- **Goal:** I can present a finished AI product like a professional, and I know what to explore next.
- **Hook:** A rapid-fire tour of the frontier: multimodal models, agents, on-device AI, open problems — plus honest talk about hallucinations, limits, and responsible use.
- **Main event — Demo Day:** capstone presentations, 8–10 min each: live product demo, results, what they'd improve. Audience: classmates (+ invited parents/teachers — the wow is contagious). Class vote: most useful, most impressive, best explained.
- **Closing:** every student writes **one research question they're genuinely curious about** — their first step beyond this course. Graduation: portfolio link with 25+ artifacts, 5 deployed products, 1 experiment report.
- **Ship:** **The complete portfolio. The demo. The question.**

---

## Assessment (mirrors industry values)
| Component | Weight | Industry parallel |
|---|---|---|
| Weekly Ships (portfolio artifacts) | 30% | Consistent shipping |
| Block projects (S10, S20, S25, S27) | 30% | Deliverables & quality |
| Capstone + Demo Day (S30–32) | 30% | Product + communication |
| Peer review & best-explanation votes | 10% | Collaboration & communication |

## Datasets (relatable, visual, age-appropriate)
Titanic · student performance · sports & game stats · music genres · memes · spam SMS · cats vs dogs · Google Speech Commands · class friendship graphs (self-generated) · students' own photos and voice recordings

## Instructor checklist (run before every session)
1. Hook demo tested and ready? (5 min)
2. Can every concept be *drawn*? If not, redesign.
3. Lab artifact clearly defined and pushed to repo?
4. Live leaderboard / competition element where fitting?
5. Any student falling behind → pair them up during lab, not extra lecture.
