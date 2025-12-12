# 1. What Are Word Embeddings?

Word embeddings are **numerical vector representations of words**.
Instead of representing a word as a one-hot vector (sparse, huge, no meaning), embeddings represent each word as a **dense vector** like:

```
good  →  [3.1, 4.4, 2.0, 6.0, … , 7.2]
great →  [3.1, 4.2, 1.9, 6.0, … , 7.1]
```

These vectors capture **semantic meaning**.
Because “good” and “great” have similar meanings, their vectors are also **similar**.

> Similar words have similar vectors.

---

# 2. Why Do We Use Word Embeddings?

Classical methods like **Bag-of-Words** or **TF-IDF** cannot understand:

* meaning
* context
* similarity between words
* synonyms

Word embeddings solve this by learning patterns from large corpora.

Example:
The model learns that:

* king is close to queen
* man is close to woman
* Paris is close to France

Embeddings allow machine learning models to work with the **meaning** of words, not just their frequencies.

---

# 3. Properties of Embeddings

1. **Dense vectors** (small numbers, typically 100–768 dimensions)

2. **Continuous space** (mathematical operations allowed)

3. **Semantic similarity** preserved

   * Cosine Similarity(good, great) → high

4. **Allow arithmetic reasoning** (Word2Vec property)

   * vector(king) − vector(man) + vector(woman) ≈ vector(queen)

---

# 4. How Word Embeddings Are Learned

Embeddings are not manually written.
They are **learned by training neural networks** on massive text corpora.

Different architectures learn embeddings differently:

---

# 5. Types of Word Embedding Techniques


## A. Based on CBOW / Skip-gram (Word2Vec family)

### 1. Word2Vec

Learns embeddings by predicting:

* Skip-gram: predict context from target word
* CBOW: predict target word from context

It learns relationships like:
king − man + woman ≈ queen

### 2. GloVe

Uses global word co-occurrence statistics.
Better captures global structure than Word2Vec.

### 3. FastText

Represents words as **subword units** (character n-grams).
Good for:

* rare words
* out-of-vocabulary words
* languages with rich morphology

Example:
“playing” → “play”, “lay”, “ing”, “playin”, etc.

---

## B. Based on Transformer Architecture

These produce **contextual embeddings**, meaning the vector depends on the sentence.

### 1. BERT

Bidirectional Transformer.
The word “bank” has different embeddings in:

* “He sat by the river bank”
* “I need to open a bank account”

Because meaning depends on context.

### 2. GPT

Autoregressive Transformer.
Generates contextual embeddings from left to right.
Used in generative tasks and large language models.

---

## C. Based on LSTM

### 1. ELMo

Produces contextual embeddings using deep bidirectional LSTMs.
Earlier than BERT but still important historically.

---

# 6. Static vs Contextual Embeddings

### Static Embeddings (Word2Vec, GloVe, FastText)

One fixed vector per word
Example: the word “bank” always has the same vector.

### Contextual Embeddings (ELMo, BERT, GPT)

The vector of a word **changes depending on the sentence**.

Example:
Sentence 1: “river bank”
Sentence 2: “money bank”

The embedding of “bank” is different in each sentence.

---

# 7. Why Embeddings Are Better Than TF-IDF

TF-IDF limitations:

* No meaning
* No relation between words
* Cannot capture synonyms
* Produces large sparse vectors

Embeddings solve all of these:

* Capture meaning
* Low-dimensional dense vectors
* More powerful for neural networks
* Used in modern NLP (transformers)

---

# 8. Visual Summary

Similar words → similar vectors
Different words → different vectors
Contextual models → vectors change depending on sentence meaning

