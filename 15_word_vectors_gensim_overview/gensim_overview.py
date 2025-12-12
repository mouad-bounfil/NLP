import gensim.downloader as api

model = api.load("word2vec-google-news-300")


model.similarity(w1="great", w2="good")


# women + king - man = queen
model.most_similar(positive=["woman", "king"], negative=["man"], topn=4)

model.most_similar(positive=["france", "berlin"], negative=["paris"], topn=4)

model.doesnt_match(["facebook", "cat", "google", "microsoft"])

model.doesnt_match(["dog", "cat", "google", "mouse"])


glv = api.load("glove-twitter-25")

glv.most_similar("arabic", topn=10)
