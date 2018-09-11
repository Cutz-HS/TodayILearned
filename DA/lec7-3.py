import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from datetime import datetime

df=DataFrame(np.random.randn(5,4), columns=['c1','c2','c3','c4'])

df.loc[2,'c2']=np.nan
df.loc[[0,1],['c1']]=None

df_drop_row=df.dropna(axis=0)
#print(df_drop_row)
df_drop_column=df.dropna(axis=1)
#print(df_drop_column)

#print(df[['c1','c2','c3']].dropna(axis=1))
#print(df)
#print(df.loc[[2,4],['c1','c2','c3']].dropna(axis=0))

datestrs=['9/11/2018','9/12/2018','9/13/2018','9/14/2018']
dates=pd.to_datetime(datestrs)
#print(dates)

ts=Series([1,np.nan, np.nan, 10], index=dates)
#print(ts)
ts_linear=ts.interpolate(method='time')
#print(ts_linear)

df=DataFrame({'c1':[1, np.nan, np.nan, 10],
              'c2':[1, 3, np.nan, 10]})
df_v=df.interpolate(method='values')
#print(df)
#print(df_v)

ser=Series([1,2,3,4,np.nan])
#ser=ser.replace(2,20)
#print(ser)
#print(ser.replace([1,2,3,4,np.nan], [6,7,8,9,10]))
#print(ser.replace({1:6, 2:8, 3:9, 4:7, np.nan:10}))

df=DataFrame({'c1':['a_old', 'b', 'c', 'd', 'e'],
              'c2':[1,2,3,4,5],
              'c3':[6,7,8,9,np.nan]})


#print(df.replace({'c1':'a_old'}, {'c1':'a_new'}))

'''
duplicates
'''

data={'key1':['a','b','b','c','c'],
      'key2':['v','w','w','x','y'],
      'col':[1,2,3,4,5]}

data_df=DataFrame(data)
#print(data_df)
#print(data_df.duplicated(['key1'],keep=False))

print(data_df.drop_duplicates(['key1'], keep='first'))




























