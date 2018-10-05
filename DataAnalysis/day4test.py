import re
from bs4 import BeautifulSoup
import urllib.request as req

# Q1 (지식인)
url="https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10405&docId=307066785&qb=67mF642w7J207YSw&enc=utf8&section=kin&rank=4&search_sort=0&spq=1"
data=req.urlopen(url).read().decode('utf-8')
soup=BeautifulSoup(data,'html.parser')
#contents_layer_0 > div.end_content._endContents > div
article=soup.select("div.end_content._endContents > div")
#print(article)
pattern=r'[^ 가-힣ㄱ-ㅎㅏ-ㅣ]'
resList=[]
for i in article:
    res=re.sub(pattern, "", i.text)
    resList.append(res)

print("\n".join(resList))

# Q2 (연습문제)
fileOpen=open("lentest.txt", "r", encoding='utf-8')
textList=fileOpen.readlines()
answer=0
for i in textList:
    i=i.rstrip()
#    print(i, len(i))
    if len(i) <= 10:
        answer+=1
print(answer)

# Q3 (연습문제)
inputNum=int(input("num?"))
inputText=input("text?")
#test = "Python is a programming language that lets you work quickly"

pattern=r"[A-za-z]+"
res=re.findall(pattern, inputText)

if len(res) < inputNum:
    print ("Wrong")
else:
    for i in range(len(res)-inputNum+1):
        for j in range(inputNum):
            print(res[j+i], end=" ")
        print("")

