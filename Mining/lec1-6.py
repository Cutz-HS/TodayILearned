import random

random.seed(777)

# list
myList=[]

myList.append(10)
myList.append('20')
myList.append(30)
myList.append([1,2,3])

#print(myList)

# Lotto
lotto = [] # 45 ----> 6

while True:
    lottoNum = random.randint(1, 45)
    if lotto.count(lottoNum) > 0:
        continue
    lotto.append(lottoNum)
    if len(lotto) == 6:
        break

lotto.sort()
print(lotto)