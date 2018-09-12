import pandas as pd
import numpy as np
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import scipy.stats as ss
from sklearn.preprocessing import StandardScaler, RobustScaler

np.random.seed(777)

df=DataFrame({'a':['a1','a1','a2','a2','a3','a3'],
              'b':['b1','b1','b1','b1','b2',np.nan],
              'c':[1,1,3,4,4,4]})

df_random=DataFrame()

#print(df['a'].unique())
#print(df['b'].unique())
#print(df['a'].value_counts())
#print(df['b'].value_counts(normalize=True))
#print(df['c'].value_counts(bins=[0,1,2,3,4,5], sort=False))

data=np.random.randint(30, size=(6,5))

def standard(data):
    return (data - np.mean(data, axis=0)) / np.std(data, axis=0)

def MinMaxScaler(data):
    return (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))

#print(data)
#print(standard(data))
#print(MinMaxScaler(data))

#print(ss.zscore(data))
#print(ss.describe(data))
    
sk=StandardScaler()
#print(sk.fit_transform(data))

rs=RobustScaler()
mu, sigma=10, 2
x=mu+sigma*np.random.randn(100)

x[98:100]=100
#print(x)

#plt.hist(x, bins=np.arange(0,102,2))
#plt.show()

x=x.reshape(-1,1)
xss=StandardScaler()
xsst=xss.fit_transform(x)
#print(xsst)
plt.hist(xsst)
plt.show()

























