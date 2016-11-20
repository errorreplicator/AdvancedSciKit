from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import numpy as np

days = [1,2,3,4,5,6,7]

sleeping = [7,6,7,8,5,9,10]
eating = [2,3,1,1,2,2,3]
playing = [7,6,9,9,7,12,11]
working = [8,9,7,9,10,1,0]

eage = np.random.random_integers(low=5,high=100,size=50)
eage2 = np.random.random_integers(low=101,high=200,size=50)

#index of integers from 0 to len(eage) or this can be ranve(any_number_in_here) range(100)
ids = [x for x in range(len(eage))]

buckets = [0,10,20,30,40,50,60,70,80,90,100]
# plt.hist(eage,buckets,histtype='bar')
# plt.scatter(eage,ids,color='b',marker='*',s=30)
# plt.scatter(eage2,ids,color='r',marker='+',s=50)

# plt.stackplot(days,sleeping,eating,playing,working,colors=['y','g','b','c'])

# pie chart
slices = [4,5,1,11]
act = ['act1','act2','act3','act4']
plt.pie(slices,labels=act,colors=['c','m','w','y'])

# plt.bar(eage,ids)
plt.show()

