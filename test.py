import pandas as pd
import math
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.linear_model import LinearRegression


X, y = np.arange(200).reshape((100,2)), range(100)
# print(X)
# print(list(y))
X_train, X_test, y_train,y_test =  model_selection.train_test_split(X,y,test_size=0.2)


clf = LinearRegression()
clf.fit(X_train,y_train)
accu = clf.score(X_test,y_test)
print(accu)
print(X_train)
# print(X_test)
#
print(y_train)
# print(y_test)

# ds = pd.read_csv('C:/ML/Data/breastc.data')
#
# print(len(ds))
# print(ds.size)
# print(ds.shape)
# print(math.ceil(0.01*len(ds)))
# print(ds.head())