### Q11: 마트 연관규칙 A priori algorithm ###
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## 파일 전처리 ##
file_open = open("d:/data/prac/groceries.csv", 'r')

all_data = []
for i in file_open.readlines():
    all_data.append(i.strip('\n').split(','))

all_data = np.array(all_data) # shape(9835, None)

all_dict = {}

## product를 dict에 넣으면서 numbering ##
k = 1
for buy in all_data:
    for product in buy:
        if product in all_dict:
            continue
        else:
            all_dict[product] = k
        k += 1
        
## numbering 적용 ##
max_num = 0
for i in all_data:
    for k in range(len(i)):
        i[k] = all_dict[i[k]]
        if max_num < len(i):
            max_num = len(i) # max_num = 32 --> 조합 32개 까지

## n빈번항목집합 함수 ##
def self_join(c_num):
    global all_dict
    data = all_dict.values()
    if c_num == 1:
        res = [i for i in data]
        
    return res

def count(join_list):
    return 
    
product_1 = self_join(1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    