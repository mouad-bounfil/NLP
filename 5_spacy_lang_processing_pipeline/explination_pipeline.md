# 🔍 spaCy Pipeline Components Explained

Below is what each component **does inside the NLP pipeline**:

---

## 1️⃣ **tok2vec**

**What it does:**

* Converts raw tokens (words) into **dense vector representations** (embeddings).
* These embeddings are used by other components (tagger, parser, NER).
* It is the *feature extraction* layer.

**In simple words:**
➡️ Takes the text and turns each word into a numerical vector so the model understands meaning.

---

## 2️⃣ **tagger** (Part-of-Speech Tagger)

**What it does:**

* Assigns **POS tags** to each word: NOUN, VERB, ADJ, ADV, etc.
* Helps models understand **grammar** and **syntactic roles**.

**Example:**
“Apple is looking at buying a startup.” →

* Apple (PROPN)
* looking (VERB)
* startup (NOUN)

---

## 3️⃣ **parser**

**What it does:**

* Builds the **dependency parse tree**.
* Shows how words relate to each other (subject, object, modifier, etc.).

**Example:**

* “Mouad wrote a book.”

  * “Mouad” → subject of “wrote”
  * “book” → object of “wrote”

➡️ Useful for relation extraction, question answering, syntax understanding.

---

## 4️⃣ **attribute_ruler**

**What it does:**

* Lets you **add rule-based corrections** to attributes like `lemma`, `pos`, `morph`.
* Used to fix special cases the model can’t guess.

**Example:**

* Forcing “lol” to be tagged as interjection
* Correcting lemma of "goes" to “go”

➡️ Helpful when preparing custom datasets or domain-specific language.

---

## 5️⃣ **lemmatizer**

**What it does:**

* Reduces words to their **base form** (lemma).

**Examples:**

* “running” → “run”
* “better” → “good”
* “cars” → “car”

➡️ Important for: search engines, text normalization, matching, embeddings.

---

## 6️⃣ **ner** (Named Entity Recognizer)

**What it does:**

* Detects named entities in text:

  * PERSON
  * ORG
  * GPE (countries/cities)
  * DATE
  * MONEY
  * PRODUCT
  * etc.

**Example:**
“Mouad lives in Morocco and works at Geeks Institute.”

* Mouad → PERSON
* Morocco → GPE
* Geeks Institute → ORG

➡️ Used for information extraction, chatbots, finance, healthcare, etc.

---

# ✅ Summary Table (Quick Review)

| Component           | Main Job                         |
| ------------------- | -------------------------------- |
| **tok2vec**         | Convert tokens → vectors         |
| **tagger**          | Assign POS tags                  |
| **parser**          | Build dependency tree            |
| **attribute_ruler** | Rule-based attributes correction |
| **lemmatizer**      | Base form of words               |
| **ner**             | Detect entities in text          |
