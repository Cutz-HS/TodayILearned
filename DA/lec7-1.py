import numpy as np
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pylab as plt

'''
df + df
concat
'''

df_1=df({'a':['a0','a1','a2'],
         'b':['b0','b1','b2'],
         'c':['c0','c1','c2'],
         'd':['d0','d1','d2']})

df_2=df({'a':['a3','a4','a5'],
         'b':['b3','b4','b5'],
         'c':['c3','c4','c5'],
         'd':['d3','d4','d5']}, index=['r3','r4','r5'])

df_12=pd.concat([df_1, df_2], ignore_index=False, keys=['df1', 'df2'], names=['df_name','row_number'])
#print(df_12.ix['df1'][:2])

df_7=df({'a':['a0','a1','a2'],
         'b':['b0','b1','b2'],
         'c':['c0','c1','c2'],
         'd':['d0','d1','d2']}, index=['r0','r1','r2'])

df_8=df({'a':['a3','a4','a5'],
         'b':['b3','b4','b5'],
         'c':['c3','c4','c5'],
         'd':['d3','d4','d5']}, index=['r2','r3','r4'])

df_78=pd.concat([df_7, df_8], verify_integrity=False)
#print(df_78)

'''
df+series
'''

series_1=pd.Series(['S1','S2','S3'], name='S')

#print(pd.concat([df_1, series_1], axis=1, ignore_index=True))

'''
series
'''
series_1=pd.Series(['S1','S2','S3'], name='S')
series_2=pd.Series([0,1,2])
series_3=pd.Series([3,4,5])
#print(pd.concat([series_1, series_2, series_3], axis=1, keys=['C0','C1','C2']))

series_4=pd.Series(['S1','S2','S3','S4'], index=['a','b','c','w'])
#print(series_4)

#print(df_1.append(series_4, ignore_index=True))

'''
Join/Merge
'''
df_left=df({'KEY':['a0','a1','a2','a3'],
            'b':['b0','b1','b2','b1'],
            'c':['c0','c1','c2','c3']})
df_right=df({'KEY':['a2','a3','a4','a5'],
            'd':['d0','d1','d2','d1'],
            'e':['e0','e1','e2','e3']})
#print(df_left)
#print(df_right)

df_merge=pd.merge(df_left, df_right, how="left", on='KEY')
#print(df_merge)

df_merge_outer=pd.merge(df_left, df_right, how="outer", on='KEY', indicator=True)
#print(df_merge_outer)

df_left_2=df({'KEY':['a0','a1','a2','a3'],
              'a':['b0','b1','b2','b3'],
            'b':['b0','b1','b2','b1'],
            'c':['c0','c1','c2','c3']})
df_right_2=df({'KEY':['a2','a3','a4','a5'],
               'b':['b0','b1','b2','b3'],
            'd':['d0','d1','d2','d1'],
            'e':['e0','e1','e2','e3']})

pdf_merge_2=pd.merge(df_left_2, df_right_2,how='inner', on='KEY')
#print(pdf_merge_2)

df_left=df({'a':['c0','c1','c2','c3'],
             'b':['d0','d1','d2','d3']}, index=['k0','k1','k2','k3'])

df_right=df({'c':['c0','c1','c2','c3'],
             'd':['d0','d1','d2','d3']}, index=['k2','k3','k4','k5'])

print(pd.merge(df_left, df_right, left_index=True, right_index=True))
print(df_left.join(df_right, how='inner'))























