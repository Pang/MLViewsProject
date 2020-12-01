# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:00:16 2020

@author: Pang
"""

import numpy as np
import matplotlib as plt
import pandas as pd

dataset = pd.read_csv('../CleanedData/USvideosClean.csv')

x = dataset.iloc[:, 1:].values #features
y = dataset.iloc[:, 0].values #dependent variable (views)

print(x[0])
print("--------------------------------")


""" *Model could assume higher/lower ids affect outcome
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='drop')
x = np.array(ct.fit_transform(x))

print(x)

"""

"""
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)


# Standardisation feature scaling on views
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:, 0] = sc.fit_transform(x_train[:, 0])
"""