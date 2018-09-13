import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pylab as plt
import matplotlib as mpl

pdf=pd.DataFrame({'seq':[1,3, np.nan],
              'name':['park','lee','choi'],
              'age':[30,20,40]})

#print(pdf)
#print(pdf.sort_values(by=['seq'], axis=0, ascending=True))
#print(pdf.sort(axis=1))

#pdf.sort_values(by=['seq'], axis=0, inplace=True)

#pdf.sort_values(by=['seq'], axis=0, inplace=True, na_position='first')

pt=[(1,'park',30),(3,'lee',20),(2,'choi',40)]
#print(sorted(pt, key=lambda ptf: ptf[0], reverse=True))
#print(sorted(pt, key=lambda ptf: ptf[1]))
#print(sorted(pt, key=lambda ptf: ptf[2]))

mlist=[9,4,1,2,7]
mlist.sort()
#print(mlist)

sr=Series([10.,11.,12.,13.,14.])
#print(sr[sr>sr.mean()])
#print(sr[[3,4,2]])

sr=pd.Series([10.,11.,12.,13.,14.],
             index=['a','b','c','d','e'])
#print(sr[['c','b','d']])
#print(sr.get(['c','d','b']))

sr['c']=100
#print('c' in sr)

sr=Series(np.nan, index=[19,18,17,16,15,1,2,3,4,5])
#print(sr)
#print(sr.iloc[:3])
#print(sr.loc[:3])

df=DataFrame({'c1':[0,1,2,3],
              'c2':[4,5,6,7],
              'c3':[8,9,10,np.nan]},
              index=['r1','r2','r3','r4'])

df_r1=DataFrame(df, index=['r1','r3'])
#print(df_r1)

df_ex=DataFrame(df, index=['r3','r1'], columns=['c3','c1'])

#print(df[['c1','c3']])
df['csum']=df['c1']+df['c2']

df=df.assign(cmul=df['c1']*df['c2'])
df=df.assign(cmul2=lambda x: x.c1*x.c2)

print(df.drop(['cmul','cmul2'],1))

del df['csum']
#print(df['c1'][0:2])
#print(df.c1[0:2])
#print(df.loc[['r1','r2']])
#print(df.iloc[0:2], "\n",df[0:2])

s=['c1','c2']
#print(df[s])
























