import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

html="""
<ul>
    <li> <a href="www.naver.com">naver</a></li> 
    <li> <a href="https://www.naver.com">naver</a></li>
    <li> <a href="https://www.daum.net">daum</a></li>
    <li> <a href="http://www.naver.com">naver</a></li>
</ul>
"""
# 정규식 포함하여 뽑아오기
soup=BeautifulSoup(html, 'html.parser')
res=soup.find_all(href=re.compile("^https://"))
print(res)

# 상대경로
base="http://example.com/html/a.html"
print(urljoin(base, "b.html"))
"http://example.com/html/sub/c.html"
print(urljoin(base, "sub/c.html"))
"http://example.com/index.html"
print(urljoin(base, "../index.html"))
"http://example.com/img/sky.png"
print(urljoin(base, "../img/sky.png"))
print(urljoin(base, "http://other.com/test"))