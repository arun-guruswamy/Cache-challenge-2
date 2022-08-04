import numpy as np
import pandas as pd
from sklearn import linear_model
# from sklearn.model_selection import GroupKFold
# from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestRegressor
from collections import defaultdict
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingRegressor
import sys
from sklearn.linear_model import RidgeClassifier




results_list = []
param_grid = {}
optimal_paramaters = [] 

#Precalculate fingerprints in pickle files

fingerprints = np.load('ml_data/CNNscore_fingerprints.npy')
print(fingerprints.dtype)
if sys.argv[2] == "0": 
    scores = np.load('torch_CNNscores.npy')
elif sys.argv[2] == "1": 
    scores = np.load('ml_data/CNNaffinity_scores.npy')
elif sys.argv[2] == "2": 
    scores = np.load('ml_data/CNNscore_scores.npy')
elif sys.argv[2] == "3": 
    scores = np.load('ml_data/CNNVS_scores.npy')
elif sys.argv[2] == "4": 
    scores = np.load('ml_data/MinimizationAffinity_scores.npy')
scores = scores.astype('float64')
weights = np.load('ml_data/mol_weights.npy')
weights = weights.astype('float64')
new_scores = scores/weights
weights = weights.reshape(-1, 1)

# fingerprints = fingerprints[0:200]
# new_scores = scores[0:200]
# weights = weights[0:200]


def cross_val(model_number):
    # Linear Regression Model
    if model_number == "0":
        model = linear_model.LinearRegression()

    # lasso regression
    elif model_number == "1":
        model = linear_model.LassoCV(cv=3, random_state=0)

    # support vector machines
    # elif model_number == "2":
    #     model = svm.SVR() 
    #     kernel = ["linear", "rbf", "sigmoid", "poly"]
    #     tolerance = [1e-3, 1e-4, 1e-5, 1e-6]
    #     C = [1, 1.5, 2, 2.5, 3]
    #     param_grid = dict(kernel=kernel, tol=tolerance, C=C)

    # random forrest
    elif model_number == "3":
        model = RandomForestRegressor()

    # gradient boosted trees 
    elif model_number == "4":
        model = GradientBoostingRegressor(max_depth=3)
        param_grid={'n_estimators':[500,1000,2000],
                    'learning_rate':[.001,0.01,.1],
                    'max_depth':[1,2,4],
                    'subsample':[.5,.75,1],
                    'random_state':[1]}



        
    scoring = ['r2', 'neg_root_mean_squared_error']

    # r_model = RandomizedSearchCV(model, param_grid, scoring='r2', cv=3, n_iter=80)
    # results = r_model.fit(fingerprints, scores)


    index = ['Linear Regression', 'LassoCV', 'SVR', 'Random Forrest', 'GradientBoostingRegressor']
    labels = ['logit', 'CNNaffinity', 'CNNscore', 'CNNVS', 'MinAffinity' ]
    # print(index[model_number])
    # print(results.best_params_)
    # print(results.best_score_)

    
    # splitter = GroupKFold(n_splits=3)
    # split_iterator = splitter.split(fingerprints, scores, scaffold_groups)
    results = cross_validate(model, fingerprints, new_scores, cv=3, scoring=scoring)

    # results = cross_val_predict(model, fingerprints, scores, cv=3)

    # np.save(f'ml_results/{index[int(model_number)]}.npy', results)

    # print(results)

    crossval_means = {}

    for x, y in results.items():
        crossval_means[x] = np.mean(y)

    crossval_means['r2_stdev'] = np.std(results['test_r2'])

    print(index[int(sys.argv[1])])
    print(labels[int(sys.argv[2])])
    print(crossval_means)

    results_list.append(crossval_means)


# Run all models
if sys.argv[1] == "all":
    for i in range(5):
        cross_val(f"{i}")
    df = pd.DataFrame(results_list, index=['Linear Regression', 'LassoCV', 'SVR', 'Random Forrest', 'GradientBoostingRegressor'])
    np.set_printoptions(threshold=np.inf)
    print(df)
#Run model based on Command Line number
else:
    cross_val(sys.argv[1])

