import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import random

random.seed(777)

num=np.array(['3.14', '-2.7','30'], dtype=np.string_)
num=num.astype(float).astype(np.int32)
#print(num)

arr=np.arange(32).reshape(8,4)
#print(arr)
#print(arr[[1,5,7,2],[0,3,1,2]])
#print(arr[[1,5,7,2]][:,[0,3,1,2]])

'''
계단 sim
'''
def walk():
    steps=1000
    position=0
    walklist=[position]
    for i in range(steps):
        step=1 if random.randint(0,1) else -1
        position += step
        walklist.append(position)
    walklist=np.array(walklist)
#    print(np.abs(walklist).cumsum())
    walklist=np.abs(walklist).cumsum()
    plt.plot(walk())
    plt.show()
    return walklist
    
'''
pd.Series
''' 
obj=Series([1,2,-3,4], index=['x','y','z','w'])
#print(obj['z'])
#print(obj[['x','y','z']])
#print(obj[obj>0])

sdata={'Ohio':35000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
states=['California', 'Ohio', 'Oregon', 'Texas']
obj3=Series(sdata)
#print(obj3)
#print(type(obj3))
obj4=Series(sdata, index=states)
#print(obj4)
#print(pd.isnull(obj4))

'''
pd.DataFrame
'''
data={'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
      'year':[2000, 2001, 2002, 2001, 2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
df=DataFrame(data)
#print(df)

df=DataFrame(data, columns=['year', 'state', 'pop','debt'], index=[1,2,3,4,5])
#print(df)
#print(df['state'])

#print(df.loc[[3, 5]])
df['debt']=np.arange(5)
#print(df)

val=Series([-1.2, -1.5, -1.7], index=[2,4,5])
df['debt']=val
#print(df)

df['eastern']=df['state']=='Ohio'
#print(df)

del df['eastern']
#print(df)

'''
multi dict
'''
pop={'Nevada':{2001:2.4, 2002:2.9},
     'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
df1=DataFrame(pop)
print(df1)
#print(df1.T)
df2=DataFrame(df1, index=[2001,2002,2003])
#print(df2)

pdata={'Ohio':df1['Ohio'][:-1],
       'Nevada':df1['Nevada'][:-1]}
df3=DataFrame(pdata)
print(df3)












