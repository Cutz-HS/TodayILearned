import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

np.random.seed(777)

'''numerical var -> cartegorical var'''

df=DataFrame({'c1':np.random.randn(20),
              'c2':['a','a','a','a','a','a','a','a','a','a',
                    'b','b','b','b','b','b','b','b','b','b']})

#print(np.linspace(df.c1.min(),df.c1.max(),10))

bins=np.linspace(df.c1.min(), df.c1.max(), 10)
df['c1_bin']=np.digitize(df['c1'], bins)
#print(df)

#print(df.groupby(df.c1_bin).size())
#print(df.groupby(df.c1_bin)['c2'].value_counts())

#print(pd.get_dummies(df['c1_bin'],prefix='c1'))

df['high_low']=np.where(df['c1']>=df.c1.mean(), 'high', 'low')
#print(df)
#print(df.groupby('high_low'))

Q1=np.percentile(df['c1'], 25)
Q3=np.percentile(df['c1'], 75)

#plt.boxplot(df['c1'])
#plt.show()
df['IQR']=np.where(df['c1']>=Q3*1.5, '01_high', np.where(df['c1']<=Q1*1.5, '01_low', df['c1']))
#print(df)

'''data reshaping: pivot, stack, melt'''

data=DataFrame({'cust_id': ['c1', 'c1', 'c1', 'c2', 'c2', 'c2', 'c3', 'c3', 'c3'], 
'prod_cd': ['p1', 'p2', 'p3', 'p1', 'p2', 'p3', 'p1', 'p2', 'p3'],
'grade' : ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'], 
'pch_amt': [30, 10, 0, 40, 15, 30, 0, 0, 10]})

# 행 고객id, 열-상품코드, 데이터-구매금액
dp=data.pivot(index='cust_id', columns='prod_cd',values='pch_amt')
#print(dp)
dp=pd.pivot_table(data, index='cust_id', columns=['prod_cd', 'grade'],values='pch_amt')
#print(dp)

mul_index=pd.MultiIndex.from_tuples(
        [('cust_1','2018'),
         ('cust_1','2019'),
         ('cust_2','2018'),
         ('cust_2','2019')])
#print(mul_index)

data=DataFrame(data=np.arange(16).reshape(4,4),
               index=mul_index,
               columns=['prd_1','prd_2','prd_3','prd_4'])
#print(data.loc['cust_1'])
# cust_1 2018 prd_1 0
data_stacked=data.stack()
#print(data_stacked['cust_2']['2018']['prd_2'])
#print(data_stacked.unstack(level=0))
data_stacked_unstacked=data_stacked.unstack(level=-1)

dsu_df=data_stacked_unstacked.reset_index()
dsu_df=dsu_df.rename(columns={'level_0':'custID',
                              'level_1':'year'})
#print(dsu_df)

data=DataFrame({
        'cust_id': ['c1', 'c1', 'c2', 'c2'], 
        'prod_cd': ['p1', 'p2', 'p1', 'p2'],
        'pch_cnt' : [1,2,3,4], 
        'pch_amt': [100,200,300,400]})
#print(data)
#print(pd.melt(data))
data_melt=pd.melt(data,id_vars=['cust_id','prod_cd'],
              var_name='pch_cd',
              value_name='pch_value')

#print(data_melt)
#print(data_melt.index)
#print(data_melt.columns)

data_melt_pivot=pd.pivot_table(
        data_melt, index=['cust_id', 'prod_cd'],
        columns='pch_cd',
        values='pch_value')
print(data_melt_pivot)

































