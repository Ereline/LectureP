# -*- coding: utf-8 -*-
"""audio-processing-system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x8kQkhzz-c78PNZt1ZO581J4p2OolS9r
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install git+https://github.com/openai/whisper.git
# %pip install git+https://github.com/explosion/spacy-models/releases/download/ru_core_news_sm-3.7.0/ru_core_news_sm-3.7.0-py3-none-any.whl
# %pip install tensorflow
# %pip install nltk
# %pip install langid
# %pip install spacy
# %pip install whisper
# %pip install pytorch_lightning
# %pip install torch

import spacy
import torch
import tensorflow as tf
import requests
from bs4 import BeautifulSoup
from collections import Counter
import whisper
import IPython
from pytorch_lightning import LightningModule

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("medium")

name=input("Введите путь к файлу: ")
IPython.display.Audio(name)

result = model.transcribe(name, language="ru")
text = open(f"{name}-lecture-transcript.txt", "w")
text.write(result["text"])
text.close()
print(result["text"])

nlp = spacy.load("ru_core_web_sm")

doc = nlp(result["text"]) # Обработка текста

token_vectors = [token.vector for token in doc] # Получение вектора для каждого токена

# Извлекаем термины
complex_terms = [entity.txt for entity in doc.entitys]
glossary = list(set(complex_terms)) # Формирование списка терминов для глоссария
print("Glossary:")
for term in glossary:
    print(term)

# Test processing
model_text_processing = Sequential()
model_text_processing.add(Embedding(input_dim = len(glossary), output_dim = 10, input_length = len(doc), input_shape = (len(doc))))
model_text_processing.add(Flatten())
model_text_processing.add(Dense(1, activation = 'sigmoid'))

#  Compiling model
model_text_processing.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model_text_processing.summary()

# Training
model_text_processing.fit(X_train, y_train, epochs = 100000, batch_size = 32, validation_data = (X_test, y_test))

# Model evaluation
loss, accuracy = model_text_processing.evaluate(X_test, y_test)
print(f"Loss: {loss}, Accuracy: {accuracy}")