import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import spacy
import numpy as np

model = spacy.load("en_core_web_lg")

# Select a few words to visualize
words = ["king", "queen", "man", "woman", "boy", "monkey"]
vectors = np.array([model.vocab[word].vector for word in words])

# Reduce dimensionality using t-SNE
# Perplexity must be less than n_samples (6 in this case)
tsne = TSNE(n_components=2, random_state=42, perplexity=min(5, len(words) - 1))
vectors_2d = tsne.fit_transform(vectors)

# Plot the embeddings
plt.figure(figsize=(8, 6))
for i, word in enumerate(words):
    plt.scatter(vectors_2d[i, 0], vectors_2d[i, 1])
    plt.text(vectors_2d[i, 0] + 0.1, vectors_2d[i, 1] + 0.1, word, fontsize=12)
plt.title("Word Embeddings Visualization")
plt.show()
