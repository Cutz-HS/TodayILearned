import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

np.random.seed(777)

''' stat '''
df=DataFrame({'group':['a','a','a','b','b','b'],
              'value_1':np.arange(6),
              'value_2':np.random.randn(6)})

grouped=df.groupby('group')
#print(grouped.sum()['value_2'])
df2=DataFrame(grouped.sum()['value_2'])
#print(grouped.describe()['value_2'].loc['a'].apply(lambda x:"{:.2f}".format(x)))

''' agg(aggregate) '''

def iqr_func(x):
    q3, q1=np.percentile(x, [75, 25])
    iqr_mm=q3-q1
    return iqr_mm

#print(grouped.aggregate(iqr_func))
#print(grouped.agg(iqr_func))
    

''' get '''
df=DataFrame({'name':['KIM','Kim','kim','LEE','Lee','lee','park','choi', 'cho'],
               'value':[1,2,3,4,5,6,7,8,9],
               'value_2':[100,300,200,100,100,300,50,80,70]})
#print(df)
# name 컬럼 -> new col (범주형)

name_mapping={'KIM':'kim',
              'Kim':'kim',
              'LEE':'lee',
              'Lee':'lee',
              'park':'others',
              'choi':'others',
              'cho':'others'}

func=lambda x: name_mapping.get(x,x)

df['name_2']=df.name.map(func)

#print(df.groupby('name_2').sum())
print(df.groupby(['name_2','name'])['value_2'].sum())























