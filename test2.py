import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)

# ds = pd.read_csv('https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/titanic_data.csv')
# ds.to_pickle('Titan.data')
ds = pd.read_pickle('Titan.data')
ds = pd.DataFrame(ds)
ds_titan = ds[['PassengerId','Sex']]
ds_titan = pd.DataFrame(ds_titan)
# ds_titan['Prediction'] = ""

def funkcja (c):
    if c['Sex'] == 'male':
        return 1
    else:
        return 0

def realF (a):
    if (a['Sex'] == 'female' or a['Pclass'] == 3 or a['Age'] < 18):
        return 1
    else:
        return 0

ds_titan['Prediction'] = ds_titan.apply(funkcja,axis=1)
ds_titan['Pclass'] = ds['Pclass']
ds['Age'].fillna(0,inplace=True)
ds_titan['Age'] = ds['Age'].astype(np.int16)
ds_titan['SurvivalRate'] = ds_titan.apply(realF,axis=1)
print(ds_titan.head(15))
# ds_titan = pd.DataFrame(ds[['PassengerID','Sex']])

# print(ds_titan.head())