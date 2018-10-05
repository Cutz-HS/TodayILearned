import requests
import urllib.request as req
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re

# 로그인 후 내 정보 출력
# http://www.hanbit.co.kr
# http://www.hanbit.co.kr/member/login.html
# http://www.hanbit.co.kr/myhanbit/myhanbit.html
# login box: id="m_id", pw="m_passwd"
# login_proc.php(검증)

url="http://www.hanbit.co.kr/member/login_proc.php"
user="cutz"
pw="cutz9031!"

info={}
info["m_id"]=user
info["m_passwd"]=pw

# Session 생성
session=requests.session()
# session 연결시도
res=session.post(url, data=info)
print(res)
res=session.get(urljoin(url, "../../myhanbit/myhanbit.html"))
print(res)
#print(res.text) # text가져오기
soup=BeautifulSoup(res.text, 'html.parser')
##container > div > div.sm_mymileage > dl.mileage_section1 > dd > span
##container > div > div.sm_mymileage > dl.mileage_section2 > dd > span
num=soup.select_one('#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span')
num2=soup.select_one('#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span')

pattern=r'[^\w]'
res=re.sub(pattern, "", num.string)

print("my mileage:",res)
print("my e-coin:",int(num2.string))