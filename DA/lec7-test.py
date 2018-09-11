import numpy as np
import pandas as pd
from pandas import DataFrame, Series

np.random.seed(777)

'''
1. 두 개의 데이터프레임을 만들고 merge 명령으로 합친다. 단 데이터프레임은 다음 조건을 만족해야 한다.
1.각각 5 x 5 이상의 크기를 가진다.
2.공통 열을 하나 이상 가진다. 다만 공통 열의 이름은 서로 다르다.
'''
# to do 
idx=[1,2,3,4,5]
common_col=[1,2,3,4,5]
x=DataFrame(np.random.randint(1,100,[5,5]), index=idx, columns=['c1','c2','c3','c4','c5'])
x['c5']=common_col
y=DataFrame(np.random.randint(1,100,[5,5]), index=idx, columns=['c5','c7','c8','c9','c10'])
y['c5']=common_col

xy=pd.merge(x, y, on='c5')
xy

'''
2.어느 회사의 전반기(1월 ~ 6월) 실적을 나타내는 데이터프레임과 후반기(7월 ~ 12월) 실적을 나타내는
 데이터프레임을 만든 뒤 합친다. 실적 정보는 "매출", "비용", "이익" 으로 이루어진다. 
(이익 = 매출 - 비용).
또한 1년간의 총 실적을 마지막 행으로 덧붙인다.
'''
# to do
sales=np.random.randint(2000000,7000000, [12])
cost=np.random.randint(1000000,5000000, [12])
profit=sales-cost

first_half=DataFrame([sales[:6], cost[:6], profit[:6]], 
                     columns=['1','2','3','4','5','6'], index=['sales','cost','profit'])
second_half=DataFrame([sales[6:], cost[6:], profit[6:]], 
                      columns=['7','8','9','10','11','12'], index=['sales','cost','profit'])
all_data=pd.concat([first_half, second_half], axis=1)
all_data.loc['cum_sum']=np.cumsum(profit)
all_data

'''
3. 다음 행렬과 같은 배열이 있다.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
1.이 배열에서 3의 배수를 찾아라.
2.이 배열에서 4로 나누면 1이 남는 수를 찾아라.
3.이 배열에서 3으로 나누면 나누어지고 4로 나누면 1이 남는 수를 찾아라.
'''
# to do
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# Q1
print(x[x%3==0])

# Q2
print(x[x%4==1])

# Q3
a=x[x%3==0]
print(a[a%4==1])