import json

jsonDic = {}
csvList = []

filereader = open('lec7-1.json', 'r', encoding='utf-8')
jsonDic = json.load(filereader)
csvName = list(jsonDic.keys())
jsonList = jsonDic[csvName[0]]

# 헤더
header_list = list(jsonList[0].keys())
csvList.append(header_list)

# 내용
for dic in jsonList:
    tempList = []
    for key in header_list:
        tempList.append(dic[key])
    csvList.append(tempList)
    
        
filereader.close()