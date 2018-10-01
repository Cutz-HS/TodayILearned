import random

random.seed(777)

# Q1

# 변수
resDict= {}
rNum = 0
currentRank = 1
totalRank = 1

# main
for i in range(1000):
    rNum = random.randint(1,100)
    if rNum in resDict:
        resDict[rNum] += 1
    else:
        resDict[rNum] = 1

sortList = sorted(resDict.items(), key=lambda value: value[1], reverse=True)

print(sortList[0][0], '\t', sortList[0][1], '\t', currentRank)
for i in range(1, len(sortList)):
    totalRank += 1
    if sortList[i][1] == sortList[i-1][1]:
        pass
    else:
        currentRank = totalRank
    print(sortList[i][0], '\t', sortList[i][1], '\t', currentRank)