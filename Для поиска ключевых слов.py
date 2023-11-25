!pip install keybert
from keybert import KeyBERT
kw_model = KeyBERT()

doc = open("name_file.txt", "r")
doc = doc.readline()
keywords = kw_model.extract_keywords(doc)

kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words=None)