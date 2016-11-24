import numpy as np
import pandas as pd
# Random floats
# sampl = np.random.uniform(low=1,high=130,size=40)

# Random Ints
# sampl = np.random.random_integers(low=1,high=130,size=30)
# print(sampl)

table1 = [1,2,3,4,5,66,78,78,32,1,2]

table2 = [x for x in range(len(table1))]

# print(table2)
# x = 1
# for x in range(15):
#     print(x, '\t')
#     print(x**x)

# x = 2
# myarray = list()
# while (x<=10):
#     myarray.append(x)
#     x+=1
#     if(x == 5):
#         print('Jest piec')


myarray = np.arange(0,10)
myarray2 = np.arange(0,15)

print(myarray.mean())

df = pd.DataFrame({'Col1': pd.Series(myarray),
                   'Co;2': pd.Series(myarray2)})

# print(df.applymap(lambda x: x>=5))

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
             'Netherlands', 'Germany', 'Switzerland', 'Belarus',
             'Austria', 'France', 'Poland', 'China', 'Korea',
             'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
             'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
             'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_medal_counts = {'country_name': pd.Series(countries),
                        'gold': pd.Series(gold),
                        'silver': pd.Series(silver),
                        'bronze': pd.Series(bronze)}
df = pd.DataFrame(olympic_medal_counts)
df2 = pd.DataFrame()
df2['bronze'] = df['bronze'][df['gold'] >= 1]
avg_bronze_at_least_one_gold = np.mean(df2['bronze'])

print(avg_bronze_at_least_one_gold)
