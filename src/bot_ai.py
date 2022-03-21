# surpress tensorflow warning
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import json 
import numpy as np
from tensorflow import keras
import pickle

# load data(QA pair)
with open("database/intents.json") as file:
    data = json.load(file)

# load trained model
model = keras.models.load_model('chat_model')

# load tokenizer object
with open('database/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# load label encoder object
with open('database/label_encoder.pickle', 'rb') as enc:
    lbl_encoder = pickle.load(enc)

def getAiAnswer(chatText):
    # parameters
    max_len = 20

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([chatText]), truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            return np.random.choice(i['responses'])
