import pandas as pd
from pandas import DataFrame
# dict practice

a_dict={}
a_list=['a','b','c','d','e']
b_list=[1,2,3,4,5]

for name in a_list:
    for i in range(0,5):
        if name not in a_dict:
            a_dict[name]={i:b_list[i]}
        else:
            a_dict[name][i]=b_list[i]
        
        