import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

abalone=pd.read_csv("d:/data/abalone.data.txt", sep=",",
            names=["sex", "length", "diameter", "height", "whole_weight", "shucked_weight",
                  "viscera_weight", "shell_weight", "rings"],
            header=None)

#print(np.sum(pd.isnull(abalone)))
#print(abalone.describe())

grouped=abalone['whole_weight'].groupby(abalone['sex'])
#print(grouped.size())
#print(grouped.mean())

#print(abalone.groupby(abalone['sex']).mean())

abalone['length_cat']=np.where(abalone.length > np.median(abalone.length),'long', 'short')
#print(abalone[['length_cat','length']])

'''
sex length_cat
F   L_L:평균값(whole_weight)
    L_S:평균값(whole_weight)
'''
group1=abalone['whole_weight'].groupby([abalone.sex,abalone.length_cat])
#print(abalone.groupby(['sex','length_cat'])['whole_weight'].mean())

# 성별로 그룹화, 그룹 이름 별 출력
group2=abalone[['sex','length_cat','whole_weight','rings']].groupby(abalone.sex)
#for _, group_data in group2:
#    print(sex)
#    print(group_data[:10])
#    
group3=abalone.groupby(['sex','length_cat'])
#for (i,j), data in group3:
#    print(i)
#    print(j)
#    print(data)
    
df=DataFrame([[1.4, np.nan],
              [7.1,-4.5],
              [np.nan, np.nan],
              [0.75, -1.3]], index=['a','b','c','d'], columns=['one','two'])
#print(df)
#print(df.sum(axis=1))
#print(df.mean(axis=1, skipna=False))
#print(df.idxmax())







































