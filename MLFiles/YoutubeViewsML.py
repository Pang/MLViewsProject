# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:00:16 2020

@author: Pang
"""

import numpy as np
import matplotlib as plt
import pandas as pd

dataset = pd.read_csv('../YoutubeStatData/USvideos.csv')

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(x)
