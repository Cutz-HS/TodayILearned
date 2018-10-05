import re
import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup

# 도서목록&가격 가져오기

#http://book.daum.net/search/bookSearch.do?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC
#http://book.daum.net/search/bookSearch.do?query=%EC%9E%90%EB%B0%94
##page_body > form:nth-child(6) > ul > li:nth-child(1) > dl > dd.price > div > span.prc > strong
#page_body > form:nth-child(6) > ul > li:nth-child(1) > dl > dt > a
#page_body > form:nth-child(6) > ul > li:nth-child(5) > dl > dd.price > div > span.prc
#page_body > form:nth-child(6) > ul > li:nth-child(24) > dl > dt > a

sumData=[]
price=[]
name=[]
word=["파이썬","자바","HTML"]
for i in word:
    base="http://book.daum.net/search/bookSearch.do?query="
    plus="&tab=&sortType=0&viewType=01&saleStatusType=exclusion&bookType=&author=&publisher=&categoryID=&authorID=&advancedSearchYN=n&additionalQuery="
    word_enc=urllib.parse.quote(i)
    url=base+word_enc+plus
    resp=req.urlopen(url).read()
    data=BeautifulSoup(resp, 'html.parser')
    res=data.select("strong.num")
    price+=res
    res1=data.select("dl > dt > a[href]")
    name+=res1
    
# dict{name: price} / price: comma 삭제 후 int type 전환
allData=[(name[i].string,price[i].string) for i in range(len(price))]
#print(allData)
for name, price in allData:
    print("책:"+name,price+"원")