import random
import pandas as pd
import numpy as np

random.seed(777)
a=[random.randrange(100) for _ in range(10)]
#print(a)
#b=[i for i in range(1,10,2)]
#print(b)
#print([i for i in a])
#print([i for i in a if i % 2][::-1])
#print([i for i in a[::-1] if i % 2])
#print([i for i in reversed(a) if i%2])

a1=[random.randrange(100) for _ in range(10)]
a2=[random.randrange(100) for _ in range(10)]
a3=[random.randrange(100) for _ in range(10)]
b=[a1,a2,a3]
#print(b)
#print(pd.DataFrame(b))
#print(sum([1,3,5]))
#print([sum(i) for i in b])
#print(sum([sum(i) for i in b]))
#
#print([0 for i in b for j in i])
#print([[j for j in i if j%2] for i in b])
#print(len(str(2**1000)))


# Q1. 2**1000에 들어가는 숫자들의 합을 구하시오.
print(sum([int(i) for i in str(2**1000)]))

# Q2. 1~100000 사이에 있는 7의 개수
print(sum([str(i).count('7') for i in range(1, 100001)]))

maria={'kor':94, 'eng':91, 'math':89, 'sci':83}
# maria의 평균
print(sum(maria.values())/len(maria))

# Q3
numList=[i for i in range(1, 5000)]
for i in range(1,5000):
    result=0
    # d(n) 구하기
    for j in str(i):
        result+=int(j)
    result+=i
    # d(n) 제거
    if result <= len(numList):
        if result in numList:
            numList.remove(result)
            # remove 잘못 된 값.
# self number 합
print(sum(numList))