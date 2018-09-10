import numpy as np
import pandas as pd
from pandas import DataFrame as df
import matplotlib.pyplot as plt

df_1=df({'a':['a0','a1','a2'],
         'b':['b0','b1','b2'],
         'c':['c0','c1','c2'],
         'd':['d0','d1','d2']}, index=[0,1,2])

df_2=df({'a':['a3','a4','a5'],
         'b':['b3','b4','b5'],
         'c':['c3','c4','c5'],
         'd':['d4','d4','d5']}, index=[3,4,5])

df_3=df({'e':['e0','e1','e2'],
         'f':['f0','f1','f2'],
         'g':['g0','g1','g2'],
         'h':['h0','h1','h2']}, index=[0,1,2])

df_13_axis1=pd.concat([df_1, df_3], axis=1)
#print(df_13_axis1)

df_4=df({'a':['a0','a1','a2'],
         'b':['b0','b1','b2'],
         'c':['c0','c1','c2'],
         'e':['e0','e1','e2']}, index=[0,1,3])

'''
outer_join
'''
print(df_1)
print(df_4)
print(pd.concat([df_1, df_4], axis=1, join_axes=[df_1.index]))
#pd.concat()