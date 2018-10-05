from bs4 import BeautifulSoup
import urllib.request as rq
import re

# N-gram 클래스 불러오기
from Ngram import Ngram
ngram=Ngram()

# N-gram // bmw 기사 2개 // N=2
url1="http://news.hankyung.com/article/201808140286g"
url2="http://www.yonhapnews.co.kr/bulletin/2018/08/14/0200000000AKR20180814075800003.HTML?input=1195m"
#newsView
##articleWrap > div.article > p:nth-child(3)

page1=rq.urlopen(url1).read()
page2=rq.urlopen(url2).read()

soup1=BeautifulSoup(page1, 'html.parser')
soup2=BeautifulSoup(page2, 'html.parser')

# 한경 기사 전처리
read1=soup1.select("div#newsView")
read1_a=read1[0].select("a")
read1_p=read1[0].select("p")
read1_div=read1[0].select("div")
read1=read1[0].text

for i in range(len(read1_a)):
    read1=read1.replace(read1_a[i].text,"")
for i in range(len(read1_p)):
    read1=read1.replace(read1_p[i].text,"")
for i in range(len(read1_div)):
    read1=read1.replace(read1_div[i].text,"")

pattern1=r"[^가-힣BMW\s]"
pattern2=r"[\s]{2,}"
pattern3=r"[\n]"
res1=re.sub(pattern1,"",read1)
read1=re.sub(pattern2, "", res1)

# 연합뉴스 기사 전처리
read2=soup2.select("div.article > p")
resList=[i.text for i in read2]
res2="".join(resList)
res2=re.sub(pattern1,"",res2)
read2=re.sub(pattern2, " ", res2)
read2=re.sub(pattern3, "", read2)

# N-gram // 출력
value, cList=ngram.gram(read1, read2, 3)
print("similarity value: %f" %value, "\ncommon word: ", cList)