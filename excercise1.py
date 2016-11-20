import pandas as pd
import numpy as np
import sklearn.model_selection as sms
import sklearn.linear_model as sl
import sklearn.metrics as sm

ds = pd.read_csv('c:/ML/Data/weeklyDrivers.csv', sep=';',names=['label','x1','x2','x3','x4','x5','x6'],skipinitialspace=True)
ds.drop(['x5','x6'],1,inplace=True)
ds.dropna(inplace=True)

# print(ds.dtypes)
# print(ds.head())

X = ds.drop('label',1)
y = ds['label']

X_train, X_test, y_train, y_test = sms.train_test_split(X,y,test_size=0.2)

clf = sl.LinearRegression()
clf.fit(X_train,y_train)
scr = clf.score(X_test,y_test)
expected = y_test
predicted = clf.predict(X_test)

print(sm.classification_report(expected,predicted,target_names=['class 0', 'class 1', 'class 2']))
print(scr)