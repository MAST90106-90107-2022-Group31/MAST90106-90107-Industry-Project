import pandas as pd
import numpy as np
import datetime as dt
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import RandomizedSearchCV
from joblib import dump, load
import math
from sklearn.metrics import roc_auc_score
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def grid_search(train_data):
  # Training 75% developing 25%
  x_train, x_dev, y_train, y_dev = train_test_split(train_data.drop(columns=['zygosity']), train_data['zygosity'])
  print("train shape, test shape",x_train.shape, x_dev.shape)
  # random forest
  # The number of trees in the forest.
  n_estimators = [ 2000, 2500, 3000, 3500]
  # max number of random feature selected for each tree
 # max_features = [math.sqrt(x_train.shape[1]), 1.5*math.sqrt(x_train.shape[1]) , 2*math.sqrt(x_train.shape[1])]
  # The function to measure the quality of a split
  criterion = ["gini", "entropy"]
  # A node will be split if this split induces a decrease of the impurity greater than or equal to this value.
  min_impurity_decrease = [0.1, 0.000001, 0.00001]
  # The maximum depth of the tree.
  max_depth = [20, 50, 100, 500, 1000]

  param_distributions = dict( n_estimators = n_estimators,criterion = criterion, min_impurity_decrease = min_impurity_decrease, max_depth = max_depth)
  rf = RandomForestClassifier()
  grid = RandomizedSearchCV(estimator = rf, param_distributions = param_distributions, scoring = "roc_auc", verbose = 1, n_jobs = -1)
  grid_result = grid.fit(x_train, y_train)

  print('Best train Score: ', grid_result.best_score_)
  print('Best train Params: ', grid_result.best_params_)
  print('Testing AUC:',roc_auc_score(y_dev, grid_result.predict_proba(x_dev)[:, 1]))

  return grid_result

 #train_data_EMTAB = pd.read_csv('Data/4vs1Datasets/EMTAB_Against_All.csv')
#print("##################\n result EMAT")
#grid_search_rf_EMTAB = grid_search(train_data_EMTAB)
#dump(grid_search_rf_EMTAB, 'Models/clf_rf_gridSearch_EMTABAgainstAll.joblib') 

# Training: E-Risk, BSGS, Denmark, E-MTAB
# Testing: AMDTSS
#train_data_AMDTSS = pd.read_csv('Data/4vs1Datasets/AMDTSS_Against_All.csv')
#print("##################\n result AMDTSS")
#grid_search_rf_AMDTSS = grid_search(train_data_AMDTSS)
#dump(selected_feat_rf_AMDTSS, 'Models/clf_rf_gridSearch_AMDTSSAgainstAll.joblib') 

## Training: E-Risk, BSGS, AMDTSS, E-MTAB
## Testing: Denmark

#train_data_DENMARK = pd.read_csv('Data/4vs1Datasets/DENMARK_Against_All.csv')
#print("##################\n result Denmark")
#grid_search_rf_DENMARK = grid_search(train_data_DENMARK)
#dump(selected_feat_rf_DENMARK, 'Models/clf_rf_gridSearch_DENMARKAgainstAll.joblib') 

## Training: E-Risk, AMDTSS, E-MTAB, Denmark
## Testing: BSGS

#train_data_BSGS = pd.read_csv('Data/4vs1Datasets/BSGS_Against_All.csv')
#print("##################\n result BSGS")
#grid_search_rf_BSGS = grid_search(train_data_BSGS)
#dump(selected_feat_rf_BSG, 'Models/clf_rf_gridSearch_BSGSAgainstAll.joblib') 


# Read Datasets
data_ERISK = pd.read_csv('Data/ERISK_ALL.csv')
data_BSGS = pd.read_csv('Data/BSGS_ALL.csv')
data_BSGS = data_BSGS.fillna(data_BSGS.mean())
data_DENMARK = pd.read_csv('Data/DENMARK_ALL.csv')
data_AMDTSS = pd.read_csv('Data/AMDTSS_ALL.csv')
data_EMTAB = pd.read_csv('Data/EMTAB_ALL.csv')
data_EMTAB = data_EMTAB.fillna(data_EMTAB.mean())


### Training: E-Risk, BSGS, Denmark, AMDTSS
## Testing: E-MTAB
train_data_EMTAB = pd.concat([data_ERISK, data_BSGS, data_DENMARK, data_AMDTSS])
print("##################\n result EMTAB")
grid_search_rf_EMTAB = grid_search(train_data_EMTAB)
dump(grid_search_rf_EMTAB, 'Models/clf_rf_gridSearch_EMTABAgainstAll.joblib')

## Training: E-Risk, BSGS, Denmark, E-MTAB
## Testing: AMDTSS
train_data_AMDTSS = pd.concat([data_ERISK, data_BSGS, data_DENMARK, data_EMTAB])
print("##################\n result AMDTSS")
grid_search_rf_AMDTSS = grid_search(train_data_AMDTSS)
dump(grid_search_rf_AMDTSS, 'Models/clf_rf_gridSearch_AMDTSSAgainstAll.joblib')

## Training: E-Risk, BSGS, AMDTSS, E-MTAB
## Testing: Denmark
train_data_DENMARK = pd.concat([data_ERISK, data_BSGS, data_AMDTSS, data_EMTAB])
print("##################\n result DENMARK")
grid_search_rf_DENMARK = grid_search(train_data_DENMARK)
dump(grid_search_rf_DENMARK, 'Models/clf_rf_gridSearch_DENMARKAgainstAll.joblib')

## Training: E-Risk, AMDTSS, E-MTAB, Denmark
## Testing: BSGS
train_data_BSGS = pd.concat([data_ERISK, data_DENMARK, data_AMDTSS, data_EMTAB])
print("##################\n result BSGS")
grid_search_rf_BSGS = grid_search(train_data_BSGS)
dump(grid_search_rf_BSGS, 'Models/clf_rf_gridSearch_BSGSAgainstAll.joblib')

## Training: BSGS, AMDTSS, E-MTAB, Denmark
## Testing: E-Risk
#  
train_data_ERISK = pd.concat([data_BSGS, data_DENMARK, data_AMDTSS, data_EMTAB])
print("##################\n result ERISK")
grid_search_rf_ERISK = grid_search(train_data_ERISK)
dump(grid_search_rf_ERISK, 'Models/clf_rf_gridSearch_ERISKAgainstAll.joblib')