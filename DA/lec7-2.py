import numpy as np
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pylab as plt

df_left=DataFrame({
        'a':['a0','a1','a2','a3'],
        'b':[0.5, 2.2, 3.6, 0.4],
        'key':['k0','k1','k2','k3']})
df_right=DataFrame({
        'c':['c0','c1','c2','c3'],
        'd':['d0', 'd1', 'd2', 'd3'],
        'key':['k2','k3','k4','k5']})

df_lr=pd.merge(df_left, df_right, how='outer')
#print(df_lr)
#print(df_lr.notnull())
df_lr.loc[[0,1], ['a','b']]=None
#print(df_lr)

#print(df_lr[['a','b']].isnull())
#print(df_lr.notnull().sum(1))
df_lr['NaN_cnt']=df_lr.isnull().sum(1)
df_lr['NotNull_cnt']=df_lr.notnull().sum(1)
#print(df_lr)

df_n=DataFrame(np.arange(10).reshape(5,2), index=['a','b','c','d','e'], columns=['c1','c2'])
#print(df_n)

df_n.loc[['b','e'],['c1']]=None
df_n.loc[['b','c'],['c2']]=None
#print(df_n)
#print(df_n.sum())
#print(df_n['c1'].cumsum())
#print(df_n.mean(1))
#
df_n['c3']=df_n['c1']+df_n['c2']
#print(df_n)

#df2=DataFrame({'c1':[1,1,1,1,1],
#               'c4':[1,1,1,1,1]}, index=['a','b','c','d','e'])

#df2['c3']=df2['c1']+df2['c2']
#print(df_n+df2)

df_n=df(np.random.randn(5,3), columns=['c1','c2','c3'])

df_n.iloc[0,0]=None
df_n.loc[1,['c1','c3']]=np.nan
df_n.loc[2,'c2']=np.nan
df_n.loc[3,'c2']=np.nan
df_n.loc[4,'c3']=np.nan

#df_missing=df_n.fillna('missing')
#print(df_missing)
#print(df_n)
#print(df_n.fillna(method='pad', limit=1))
#print(df_n.mean())
#print(df_n.fillna(df_n.mean()))
##print(df_n)
#print(df_n.where(df_n.notnull(), df_n.mean(), axis='columns'))
#print(df_n)
#print(df_n.mean()['c1':'c2'])
#print(df_n.fillna(df_n.mean()['c1':'c2']))
df_2=df({'c1':[1,2,3,4,5],
         'c2':[6,7,8,9,10]})
df_2.loc[[1,3],['c2']]=np.nan
print(df_2)

df_2['c2_new']=np.where(pd.notnull(df_2['c2']), df_2['c2'], df_2['c1'])
print(df_2)






















