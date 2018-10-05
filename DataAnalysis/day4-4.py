from bs4 import BeautifulSoup
import urllib.request as req
import re

fp=open("color.html", "r", encoding="utf-8")
soup=BeautifulSoup(fp, 'html.parser')

res = lambda be: soup.select_one(be).text
#res("#gr") #id
#res("li#gr") #li 내 id의 내용 출력
#res("ul > li#gr")
#res("#mycolor")  # 해당 모두
#print(res("#mycolor #gr"))
#res("#mycolor > #gr")
#res("ul#mycolor > li#gr")
#print(res("li[id='gr']")) # 직접지정
#print(res("li:nth-of-type(4)")) # 인덱스 지정
#print(soup.find_all("li")[3].string)
#print(soup.select("li")[3].string)

#mw-content-text > div > ul:nth-child(6) > li > ul > li:nth-child(1) > a

#url="https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
#data=req.urlopen(url).read().decode('utf-8')
##print(data)
#soup=BeautifulSoup(data, 'html.parser')
##print(soup)
#poetList=soup.select("#mw-content-text > div > ul > li > ul > li > a")
#for i in poetList:
#    print(i.string)

# naver 댓글은 막혀있다.
#contents_layer_1 > div.end_content._endContents > div._endContentsText
#contents_layer_0 > div.end_content._endContents > div
#contents_layer_0 > div.end_content._endContents > div

url="https://kin.naver.com/qna/detail.nhn?d1id=1&dirId=10801&docId=307433299&qb=67mF642w7J207YSw&enc=utf8&section=kin&rank=6&search_sort=0&spq=1"
data=req.urlopen(url).read().decode('utf-8')
soup=BeautifulSoup(data,'html.parser')
article=soup.select("div.end_content._endContents > div")
#print(article)
pattern=r'[^ 가-힣ㄱ-ㅎㅏ-ㅣ]'
resList=[]
for i in article:
    res=re.sub(pattern, "", i.text)
    resList.append(res)

print("\n".join(resList))