import spacy

# Download the model if it's not already installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spacy model 'en_core_web_sm'...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

doc = nlp(
    "I arrived in Casablanca yesterday. Today I will start my NLP course. The weather is beautiful and I feel motivated!"
)

for sentence in doc.sents:
    print(sentence)

for sentence in doc.sents:
    for word in sentence:
        print(word)


from nltk.tokenize import sent_tokenize
import nltk

nltk.download("punkt")

sent_tokenize(
    "I arrived in Casablanca yesterday. Today I will start my NLP course. The weather is beautiful and I feel motivated!"
)
