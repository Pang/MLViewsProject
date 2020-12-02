# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:00:16 2020

@author: Pang
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('../CleanedData/USvideosClean.csv')

x = dataset.iloc[:, 2].values #features
y = dataset.iloc[:, 0].values #dependent variable / label (views)


from sklearn.feature_extraction.text import CountVectorizer  
cv = CountVectorizer()
xVector = cv.fit_transform(x)


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(xVector, y, test_size = 0.2, random_state = 1)

from sklearn.naive_bayes import MultinomialNB
nv = MultinomialNB()
nv.fit(x_train, y_train)

print(nv.score(x_test, y_test))