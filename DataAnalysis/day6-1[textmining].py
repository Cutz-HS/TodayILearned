from konlpy.tag import Twitter
import codecs
from bs4 import BeautifulSoup

twit=Twitter()
#test=twit.pos("아버지가방에들어가신", norm=True, stem=True)
#print(test)

#toji=open("toji1.txt", "r")
# Codecs 활용
toji=codecs.open("TOJI1.txt", "r", encoding="ms949")

# BS
soup=BeautifulSoup(toji, "html.parser")
#print(soup)

# 형태소 분석 & Noun만 추가
text=soup.getText()
lines=text.split("\r\n")
resDict={}

#resList=[(i,j) for text in lines for i, j in twit.pos(text, norm=True, stem=True) if j=='Noun']

for text in lines:
    for i, j in twit.pos(text, norm=True, stem=True):
        if j=='Noun':
            if i not in resDict:
                resDict[i]=1
            else:
                resDict[i]+=1

rankList=sorted(resDict.items(), key=lambda value: value[1], reverse=True)
print(rankList[0])