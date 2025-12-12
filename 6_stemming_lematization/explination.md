# 🔍 spaCy vs NLTK in **Stemming** & **Lemmatization**

---

# 1️⃣ **Stemming**

### 📌 **NLTK**

* NLTK **supports stemming** through algorithms like:

  * **PorterStemmer**
  * **SnowballStemmer**
  * **LancasterStemmer**
* Stemming is **rule-based and aggressive** → cuts words blindly.

**Example (NLTK Stemmer):**

* “studies” → “studi”
* “running” → “run”
* “better” → “bett”

➡️ NLTK is **good for basic stemming**, fast but **not accurate linguistically**.

### 📌 **spaCy**

* **spaCy does NOT support stemming.**
* The authors intentionally removed stemming because it produces **unnatural** word forms.

➡️ spaCy = **No stemming at all**.

---

# 2️⃣ **Lemmatization**

### 📌 **spaCy**

* spaCy uses a **rule-based + context-based lemmatizer**.
* It uses:

  * POS tags
  * Morphological features
  * Lookup tables
  * Language-specific rules
* **Very accurate**, because it uses the entire NLP pipeline.

**Example (spaCy Lemmatizer):**

* “studies” → “study”
* “running” → “run” (verb), “running” (noun stays the same)
* “better” → “good”

➡️ spaCy lemmatization is **modern, intelligent, and context-aware**.

---

### 📌 **NLTK**

* NLTK uses **WordNet Lemmatizer**.
* It requires you to **manually specify POS tag** for best results.

**Example (NLTK without POS):**

* “running” → “running” ❌
* “studies” → “study” ✔️

**Example (NLTK with POS):**

* “running” (verb) → “run” ✔️

➡️ NLTK is **less accurate** unless POS is provided manually.

---

# 🎯 Summary Table

| Feature                | **spaCy**                       | **NLTK**                                  |
| ---------------------- | ------------------------------- | ----------------------------------------- |
| **Stemming**           | ❌ Not supported                 | ✔️ Yes (Porter, Snowball, Lancaster)      |
| **Lemmatization**      | ✔️ Very accurate, context-aware | ✔️ Good but requires POS tag for accuracy |
| **Needs POS Tagging?** | Automatically handled           | You must specify it manually              |
| **Speed**              | Faster                          | Slower                                    |
| **Best for**           | Production NLP, accuracy        | Education, prototypes, basic NLP          |

---

# 🧠 Final Explanation (1 sentence)

**spaCy uses advanced, accurate lemmatization (no stemming), while NLTK uses simple rule-based stemming and older lemmatization that needs POS tags to work well.**

