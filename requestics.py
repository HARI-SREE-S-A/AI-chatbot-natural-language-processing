import random
import json
import numpy as np
import nltk

from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import seqential
from tensorflow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.optimizers import SGD


lemmetizer = WordNetLemmatizer

intents = json.loads(open('intents.json').read())
words = []
classes = []
documents = []
ignore_letters = []
