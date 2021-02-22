import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

data = pd.read_csv('Train.csv')

data = data.fillna(data.mean())
# o = data.isnull().sum()
# print(o)
# columns = data['Item_Fat_Content']
# for var in columns:
#     le = preprocessing.LabelEncoder()
#     data[var] = le.fit_transform(data[var].astype('str'))



X_feat = data.iloc[:, :4]
y_feat = data.iloc[:, -1]

# def turn_to_int(word):
#     dict_ = {'Low Fat':1, 'Regular':2, 'low fat':3, 'LF':4, 'reg':5}
#     return dict_[word]

# X_feat['Item_Weight'] = X_feat['Item_Weight'].apply(lambda x : turn_to_int(X_feat))


from sklearn.ensemble import RandomForestRegressor
Rfr = RandomForestRegressor()
Rfr.fit(X_feat,y_feat)

import pickle
from sklearn.externals import joblib
filename = 'prediction.sav'
pickle.dump(Rfr, open(filename, 'wb'))

# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_feat, y_feat)
# print(result)