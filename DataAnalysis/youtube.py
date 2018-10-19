from bs4 import BeautifulSoup
from selenium import webdriver
import time

#http://www.cgv.co.kr/movies/
#contents > div.wrap-movie-chart > div.sect-movie-chart > ol:nth-child(2) > li:nth-child(1) > div.box-contents > a > strong
#//*[@id="contents"]/div[1]/div[3]/button

# 동적 페이지(더보기) 포함 스크래핑
url="https://www.youtube.com/watch?v=BzYnNdJhZQw"

# selenium drvier (chromedriver download)
path="D:/data/chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get(url)
time.sleep(5)

# 더보기 누르기 // xpath_copy(chrome)
#driver.find_element_by_xpath("//*[@id='contents']/div[1]/div[3]/button").click()
#time.sleep(1)

# html 가져오기
html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
#print(soup)

# 정보 가져오기
htmlList=soup.select("div[id='info']")
res={}
for i in htmlList:
    print(i.text)
#print(res)