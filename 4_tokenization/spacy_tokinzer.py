import spacy

nlp = spacy.blank("en")

with open("students.txt") as f:
    text = f.readlines()

text = " ".join(text)


nlp.add_pipe("sentencizer")

doc = nlp(text)

for sentence in doc.sents:
    print(sentence)

from spacy.symbols import ORTH

nlp = spacy.blank("en")
doc = nlp("gimme double cheese extra large healthy pizza")
tokens = [token.text for token in doc]
tokens


nlp.tokenizer.add_special_case("gimme", [
    {ORTH: "gim"},
    {ORTH: "me"},
])
doc = nlp("gimme double cheese extra large healthy pizza")
tokens = [token.text for token in doc]
tokens


nlp.pipeline

doc = nlp("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of delhi")
for sentence in doc.sents:
    print(sentence)
    
    
    
nlp.add_pipe('sentencizer')

doc = nlp("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of delhi")
for sentence in doc.sents:
    print(sentence)
    
    
nlp.pipeline

