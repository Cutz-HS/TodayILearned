from bs4 import BeautifulSoup
from selenium import webdriver
import time

#http://www.cgv.co.kr/movies/
#contents > div.wrap-movie-chart > div.sect-movie-chart > ol:nth-child(2) > li:nth-child(1) > div.box-contents > a > strong
#//*[@id="contents"]/div[1]/div[3]/button

# 동적 페이지(더보기) 포함 스크래핑
url="http://www.cgv.co.kr/movies/"

# selenium drvier (chromedriver download)
path="D:/DataAnalysis/chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get(url)
time.sleep(3)

# 더보기 누르기 // xpath_copy(chrome)
driver.find_element_by_xpath("//*[@id='contents']/div[1]/div[3]/button").click()
time.sleep(1)

# html 가져오기
html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
#print(soup)

# 영화정보 가져오기
htmlList=soup.select("ol > li > div.box-contents")
res={}
for i in range(len(htmlList)):
    movie=htmlList[i].select_one("strong[class='title']").text
    per=htmlList[i].select_one("strong[class='percent']").text
    thumbsup=htmlList[i].select_one("span.count > strong > i").text
    release=htmlList[i].select_one("span.txt-info > strong").text
    res[movie]=(per, thumbsup+"명이 좋아요", release.strip().replace("\n","").replace(" ",""))
#print(res)

# 출력(영화제목 // 예매율, 좋아요, 개봉일)
for info in res:
    print(info, "\n >", " / ".join(res[info]))