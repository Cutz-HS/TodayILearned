import random

random.seed(777)

# Q3

# 변수선언
rNum = 0
resList = []

# main
for i in range(100):
    rNum = str(random.randint(1,999))
    while len(rNum) < 3:
        rNum = '0' + rNum    
    resList.append(rNum)

#print(resList)
        
sortList = sorted(resList, key=lambda value: int(value[1]), reverse=True)

print(sortList)