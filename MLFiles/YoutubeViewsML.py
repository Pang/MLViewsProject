# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:00:16 2020

@author: Pang
"""

import numpy as np
import pandas as pd
import tensorflow as tf

dataset = pd.read_csv('../CleanedData/USvideosLikesDislikes.csv')

x = dataset.iloc[:, 1:].values #features (likes/dislikes)
y = dataset.iloc[:, 0].values #dependent variable / label (views)

# Split into training model
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

"""
# Create predictions
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

# Print
np.set_printoptions(precision=0)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))
print(regressor.score(x_test, y_test))
"""

# Part 2 - Building the ANN
# Initializing the ANN
ann = tf.keras.models.Sequential()


# Adding the input layer and the first hidden layer & the second hidden layer (relu = rectifier)
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Adding the output layer
ann.add(tf.keras.layers.Dense(units=1))

# Part 3 - Training the ANN
# Compiling the ANN
ann.compile(optimizer='adam', loss='mean_squared_error')

# Training the ANN on the Training set
ann.fit(x_train, y_train, batch_size=32, epochs=100)


y_pred = ann.predict(x_test)

# Print
np.set_printoptions(precision=0)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))