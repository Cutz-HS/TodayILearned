import numpy as np
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt

'''
load
'''

csv_test=pd.read_csv("d:/data/test_csv_file.csv")
#print(csv_test)
#print(csv_test.shape)

text_test=pd.read_csv("d:/data/test_text_file.txt" , sep="|", index_col=0)
#print(text_test)

test2=pd.read_csv("d:/data/text_without_column_name.txt", sep="|", header=None,
                  names=["ID", "A", "B","C", "D"], index_col='ID')
#test2.columns=["A", "B", "C","D", "E"]
print(test2)

'''
save
'''
data={'id':['a1','a2','a3','a4','a5'],
      'x1':[1,2,3,4,5],
      'x2':[3.0,4.5,3.2,4.0,3.5]}
#df=DataFrame(data)
#print(df)

#df=DataFrame(data)
#df.index=df['id']
#df.pop('id')
#print(df)


df_1 = df(data=np.arange(12).reshape(3,4), index=['r0','r1','r2'], dtype='int',
   columns=['c0','c1','c2','c3'])
df_2 = df({
        'class_1':['a','a','b','b','c'],
        'var_1':np.arange(5),
        'var_2':np.random.randn(5)},
        index=['r0','r1','r2','r3','r4'])
#print(df_2)

#print(df_2.columns)
#print(df_2[['class_1', 'var_2']])

idx=['r0','r1','r2','r3','r4']
df_1=df({'c1':np.arange(5),
         'c2':np.arange(5,10),
         'c3':np.arange(10,15)}, index=idx)

new_idx=['r0','r1','r2','r5','r6']
df_1=df_1.reindex(new_idx, fill_value='missing')
#print(df_1)
#df_1=df_1.fillna(0)
#print(df_1)

'''
시계열
'''
date=pd.date_range("2018-9-10", periods=10, freq='D')
#print(date)
df_2=df({'c1':[10,20,30,40,50,10,20,30,40,50]}, index=date)
print(df_2)

date2=pd.date_range("09/05/2018", periods=20, freq='D')
df_3=df_2.reindex(date2, method='bfill')
print(df_3)








































