# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:00:16 2020

@author: Pang
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('../CleanedData/USvideosLikesDislikes.csv')

x = dataset.iloc[:, 1:].values #features (likes/dislikes)
y = dataset.iloc[:, 0].values #dependent variable / label (views)

# Train model
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Create predictions
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

# Print
np.set_printoptions(precision=0)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))
print(regressor.score(x_test, y_test))