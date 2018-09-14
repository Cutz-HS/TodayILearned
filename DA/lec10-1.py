import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

''' apply '''
df=DataFrame({'id':[1,2,10,20,100,200],
           'name':['aaa','bbb','ccc','ddd','eee','fff']})
#print(df)
df['id_2']=df['id'].apply(lambda x:"{:0>5d}".format(x))

x=3.141592
#print("{:+.2f}".format(x))
x=333
#print("{:0>5d}".format(x))
#print("{:,}".format(x))

df['id_name']=df[['id_2', 'name']].apply(lambda x:'_'.join(x), axis=1)
#print(df)

df['id_3']=df['id'].apply(lambda x:"{:.2f}".format(x))
#print(df)
df['name_3']=df['name'].apply(lambda x:x.upper())

#df['id_name_3']=df[['name_3', 'id']].apply(lambda x, y:":".join(x,"{:0>3d}".format(y)), axis=1)
#print(df)

''' groupby '''
# 딕셔너리를 이용한 그룹화
df=DataFrame(data=np.arange(20).reshape(4,5),
             columns=['c1','c2','c3','c4','c5'],
             index=['r1','r2','r3','r4'])

mdr={'r1':'row_g1',
     'r2':'row_g1',
     'r3':'row_g2',
     'r4':'row_g2'}

gbr=df.groupby(mdr)
#print(gbr.sum())

mdc={'c1':'col_g1',
     'c2':'col_g1',
     'c3':'col_g2',
     'c4':'col_g2',
     'c5':'col_g2'}
gbc=df.groupby(mdc, axis=1)
#print(gbc.sum())

# Series를 이용한 그룹화
msr=Series(mdr)
#print(df.groupby(msr).sum())
msc=Series(mdc)
print(df.groupby(msc, axis=1).sum())

# function
def rgf(x):
    if x=='r1' or x=='r2':
        rg='row_g1'
    else:
        rg='row_g2'
    return rg




























