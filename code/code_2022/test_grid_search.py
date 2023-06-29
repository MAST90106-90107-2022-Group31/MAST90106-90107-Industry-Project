import pandas as pd
import numpy as np
import datetime as dt
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import RandomizedSearchCV
from joblib import dump, load
import math 
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


# if model = 'lr':

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

## Training: BSGS, AMDTSS, E-MTAB, Denmark
## Testing: E-Risk
test_data_ERISK = pd.read_csv('Data/ERISK_ALL.csv')
y_ERISK = test_data_ERISK['zygosity']
y_ERISK = y_ERISK.replace(['MZ','DZ'],[1,0])
x_ERISK = test_data_ERISK.drop(columns = ["zygosity"])
print("##################\n result ERISK tested over all datasets")
clf = load('Models/clf_rf_gridSearch_ERISKAgainstAll.joblib') 
print('Testing AUC:',roc_auc_score(y_ERISK, clf.predict_proba(x_ERISK)[:, 1]))