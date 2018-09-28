# 변수
trainList = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에일리', 5),
             ('토마스', 4), ('헨리', 7), ('토마스', 3), ('에일리', 8),
             ('퍼시', 5), ('고든', 13)]
trainDic = {}
tmpTup = None
totalRank , currentRank = 1, 1

# 메인 코드
for tmpTup in trainList:
    tName = tmpTup[0]
    tWeight = tmpTup[1]
    if tName in trainDic:
        trainDic[tName] += tWeight
    else:
        trainDic[tName] = tWeight
print(trainDic)

resList = sorted(trainDic.items(), key=lambda value: value[1], reverse=True)
print(resList)
#trainList = sorted(trainDic.items(), key=operator.itemgetter(1), reverse=True)
#print(trainList)

print(resList[0][0], '\t', resList[0][1], '\t', currentRank)
for i in range(1, len(resList)):
    totalRank += 1
    if resList[i][1] == resList[i-1][1]:
        pass
    else:
        currentRank = totalRank
    print(resList[i][0], '\t', resList[i][1], '\t', currentRank)