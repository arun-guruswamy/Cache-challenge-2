import numpy as np
import pandas as pd
from sklearn import linear_model
# from sklearn.model_selection import GroupKFold
# from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestRegressor
from collections import defaultdict
import os

directory = 'enamine_fingerprints'
test_fingerprints = np.load('fingerprints.npy')
test_scores = np.load('ml_data/CNNVS_scores.npy')
test_scores = test_scores.astype('float64')

for filename in os.listdir(directory):
    with open(filename, 'rt') as fin:
        model = linear_model.LassoCV(cv=3, random_state=0)
        
        model.fit()


