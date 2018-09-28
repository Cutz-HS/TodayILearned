from konlpy.tag import Twitter

# Q1

# 변수
resDict = {}
wordCount = 1
totalRank, currentRank = 1, 1
instr = '''
자화상

산모퉁이를 돌아 논가 외딴 우물을 홀로
찾아가선 가만히 들여다봅니다.

우물 속에는 달이 밝고 구름이 흐르고
하늘이 펼치고 파아란 바람이 불고 가을이 있습니다.

그리고 한 사나이가 있습니다.
어쩐지 그 사나이가 미워져 돌아갑니다.

돌아가다 생각하니 그 사나이가 가엾어집니다. 도로 가 들여다보니 사나이는 그대로 있습니다.

다시 그 사나이가 미워져 돌아갑니다.
돌아가다 생각하니 그 사나이가 그리워집니다.

우물 속에는 달이 밝고 구름이 흐르고 하늘이 펼치고 파아란 바람이 불고 가을이 있고 추억처럼 사나이가 있습니다.
'''

# 메인코드
instr = instr.strip()
instr = instr.replace(' ', '')
instr = instr.replace('\n', '')
instr = instr.replace('.', '')
for letter in instr:
    if letter in resDict:
        resDict[letter] += wordCount
    else:
        resDict[letter] = wordCount

resList = sorted(resDict.items(), key=lambda value: value[1], reverse=True)
#print(resList)

print(resList[0][0], '\t', resList[0][1], '\t', currentRank)
for i in range(1, len(resList)):
    totalRank += 1
    if resList[i][1] == resList[i-1][1]:
        pass
    else:
        currentRank = totalRank
    print(resList[i][0], '\t', resList[i][1], '\t', currentRank)


# Q1+

# 변수
resDict = {}
wordCount = 1
totalRank, currentRank = 1, 1
instr = '''
자화상

산모퉁이를 돌아 논가 외딴 우물을 홀로
찾아가선 가만히 들여다봅니다.

우물 속에는 달이 밝고 구름이 흐르고
하늘이 펼치고 파아란 바람이 불고 가을이 있습니다.

그리고 한 사나이가 있습니다.
어쩐지 그 사나이가 미워져 돌아갑니다.

돌아가다 생각하니 그 사나이가 가엾어집니다. 도로 가 들여다보니 사나이는 그대로 있습니다.

다시 그 사나이가 미워져 돌아갑니다.
돌아가다 생각하니 그 사나이가 그리워집니다.

우물 속에는 달이 밝고 구름이 흐르고 하늘이 펼치고 파아란 바람이 불고 가을이 있고 추억처럼 사나이가 있습니다.
'''

# 메인코드
wordList = instr.split()
for data in wordList:
    if data[-1] in ['.', ',', '가', '은', '는', '이', '을', '를']:
        data = data[:-1]
    if data not in resDict:
        resDict[data]=1
    else:
        resDict[data]+=1


#twit = Twitter()
#word = twit.pos(instr, norm=True, stem=True)
        
resList=sorted(resDict.items(), key=lambda value: value[1], reverse=True)

print(resList[0][0], '\t', resList[0][1], '\t', currentRank)
for i in range(1, len(resList)):
    totalRank += 1
    if resList[i][1] == resList[i-1][1]:
        pass
    else:
        currentRank = totalRank
    print(resList[i][0], '\t', resList[i][1], '\t', currentRank)
