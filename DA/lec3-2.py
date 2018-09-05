#결측치 처리 & 데이터프레임 사용

from pandas import DataFrame, Series
import pandas as pd
import numpy as np
#pd.DataFrame()

#print(np.random.randn(5,3))
#표준정규분포, 평균(기댓값):0, 표준편차:1
df=pd.DataFrame(np.random.randn(5,4),
['A','B','C','D','E'],['W','X','Y','Z'])
#print(df)
#print(type(df))
#print(type(df['W']))
#print(type(df))

#df=df.drop('E')
#print(df)

# print(df.shape)
# print(df.loc['A'])
# print(df.iloc[0])
#print(df.loc[['A','B']])
print(df.loc[['A','B'], ['X','Y']])

d={'A':[1,2,np.nan],'B':[5,np.nan, np.nan],
 'C':[1,2,3]}
print(d)
df=pd.DataFrame(d)
print(df)
print(type(df))

#print(df.dropna(axis=1))
#rint(df.dropna())

#print(df['A'].fillna(value="imsi"))
#print(df.fillna(value="imsi"))
print(df)
#A열에 대해서 na값을 A열의 평균으로 대체
#print(df['A'].mean())

print(df['A'].fillna(value=df['A'].mean()))