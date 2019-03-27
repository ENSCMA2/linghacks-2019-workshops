import os
import math
import random
import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC, SVC, NuSVC
from pprint import pprint
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import numpy as np
import time
from scipy.sparse import csr_matrix
import pandas as pd
from collections import Counter

data = list(csv.reader(open("formspring_data.csv", mode="r+")))[1:]

answers = []
print(data[0])
for i in range(len(data)):
	votes = Counter([data[i][5],data[i][8],data[i][11]])
	print(votes)
	if votes["Yes"] > 1:
		answers.append(1)
	else:
		answers.append(0)
answers = np.array(answers)
text = np.array([point[1] for point in data])
train_data, test_data , train_labels, test_labels = train_test_split(text,answers,test_size=.2)

vectorizer = TfidfVectorizer()
vectorised_train_data = vectorizer.fit_transform(train_data)

classifier = LinearSVC()
classifier.fit(vectorised_train_data, train_labels)

vectorised_test_data = vectorizer.transform(test_data)

predictions = classifier.predict(vectorised_test_data)

accuracy = accuracy_score(test_labels, predictions)
precision = precision_score(test_labels, predictions, pos_label = 1)
recall = recall_score(test_labels, predictions, pos_label = 1)
f1 = f1_score(test_labels, predictions, pos_label = 1)


print(str(accuracy))
print(str(precision))
print(str(recall))
print(str(f1))


user_input = input("Send me a message!\n")
user_data = np.array([user_input])
vectorised_user_data = vectorizer.transform(user_data)

while(user_input != "quit"):
	prediction = classifier.predict(vectorised_user_data)
	print(prediction)
	user_input = input("Send me a message!\n")
	user_data = np.array([user_input])
	vectorised_user_data = vectorizer.transform(user_data)
print("Bye!")
