import pandas as pd
import numpy as np
import datetime as dt
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.feature_selection import SelectFromModel
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def variable_selection(train_data):
    # Training 75% developing 25%
    x_train, x_dev, y_train, y_dev = train_test_split(train_data.drop(columns=['zygosity']), train_data['zygosity'])
    x_train.shape, x_dev.shape, y_train.shape, y_dev.shape

    # Variable selection by random forest
    rf_selection = SelectFromModel(RandomForestClassifier(n_estimators = 3000, min_impurity_decrease = 1e-05, max_depth =  100, criterion = 'entropy'), threshold = "9*mean")
    rf_selection.fit(x_train, y_train)

    # selected variables
    selected_feat_rf = x_train.columns[(rf_selection.get_support())]

    return selected_feat_rf

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
selected_feat_rf_EMTAB = variable_selection(train_data_EMTAB)
np.savetxt('selected_feat_rf_EMTAB.txt', selected_feat_rf_EMTAB,fmt='%s')
train_EMTAB = train_data_EMTAB.loc[:,[i for i in selected_feat_rf_EMTAB]]
train_EMTAB['label'] = train_data_EMTAB['zygosity']
train_EMTAB.to_csv("train_EMTAB.csv")
test_EMTAB = data_AMDTSS.loc[:,[i for i in selected_feat_rf_EMTAB]]
test_EMTAB['label'] = data_AMDTSS['zygosity']
test_EMTAB.to_csv('test_EMTAB.csv')



## Training: E-Risk, BSGS, Denmark, E-MTAB
## Testing: AMDTSS

train_data_AMDTSS = pd.concat([data_ERISK, data_BSGS, data_DENMARK, data_EMTAB])
selected_feat_rf_AMDTSS = variable_selection(train_data_AMDTSS)
#np.savetxt('selected_feat_rf_AMDTSS.txt', selected_feat_rf_AMDTSS,fmt='%s')
train_AMDTSS = train_data_AMDTSS.loc[:,[i for i in selected_feat_rf_AMDTSS]]
train_AMDTSS['label'] = train_data_AMDTSS['zygosity']
train_AMDTSS.to_csv("train_AMDTSS.csv")
test_AMDTSS = data_AMDTSS.loc[:,[i for i in selected_feat_rf_AMDTSS]]
test_AMDTSS['label'] = data_AMDTSS['zygosity']
test_AMDTSS.to_csv('test_AMDTSS.csv')



## Training: E-Risk, BSGS, AMDTSS, E-MTAB
## Testing: Denmark

train_data_DENMARK = pd.concat([data_ERISK, data_BSGS, data_AMDTSS, data_EMTAB])
selected_feat_rf_DENMARK = variable_selection(train_data_DENMARK)
#np.savetxt('selected_feat_rf_DENMARK.txt', selected_feat_rf_DENMARK,fmt='%s')
train_DENMARK = train_data_DENMARK.loc[:,[i for i in selected_feat_rf_DENMARK]]
train_DENMARK['label'] = train_data_DENMARK['zygosity']
train_DENMARK.to_csv("train_DENMARK.csv")
test_DENMARK = data_DENMARK.loc[:,[i for i in selected_feat_rf_DENMARK]]
test_DENMARK['label'] = data_DENMARK['zygosity']
test_DENMARK.to_csv('test_DENMARK.csv')

## Training: E-Risk, AMDTSS, E-MTAB, Denmark
## Testing: BSGS

train_data_BSGS = pd.concat([data_ERISK, data_DENMARK, data_AMDTSS, data_EMTAB])
selected_feat_rf_BSGS = variable_selection(train_data_BSGS)
#np.savetxt('selected_feat_rf_BSGS.txt', selected_feat_rf_BSGS,fmt='%s')
train_BSGS = train_data_BSGS.loc[:,[i for i in selected_feat_rf_BSGS]]
train_BSGS['label'] = train_data_BSGS['zygosity']
train_BSGS.to_csv("train_BSGS.csv")
test_BSGS = data_BSGS.loc[:,[i for i in selected_feat_rf_BSGS]]
test_BSGS['label'] = data_BSGS['zygosity']
test_BSGS.to_csv('test_BSGS.csv')

## Training: BSGS, AMDTSS, E-MTAB, Denmark
## Testing: E-Risk

train_data_ERISK = pd.concat([data_BSGS, data_DENMARK, data_AMDTSS, data_EMTAB])
selected_feat_rf_ERISK = variable_selection(train_data_ERISK)
#np.savetxt('selected_feat_rf_ERISK.txt', selected_feat_rf_ERISK,fmt='%s')
train_ERISK = train_data_ERISK.loc[:,[i for i in selected_feat_rf_ERISK]]
train_ERISK['label'] = train_data_ERISK['zygosity']
train_ERISK.to_csv("train_ERISK.csv")
test_ERISK = data_ERISK.loc[:,[i for i in selected_feat_rf_ERISK]]
test_ERISK['label'] = data_ERISK['zygosity']
test_ERISK.to_csv('test_ERISK.csv')
