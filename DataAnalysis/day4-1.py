from bs4 import BeautifulSoup

html="""
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

soup=BeautifulSoup(html, 'html.parser')
link=soup.find_all("a")
print(link)

# for i in link:
#     print(i)

for i in link:
    myhref=i.attrs['href'] # 내부에 명령어 value를 출력
    print(myhref)

html2="""
<html><body>
<h1>빅데이터 분석</h1>
<p>데이터 수집</p>
<p>데이터 전처리</p>
<p>데이터 마이닝</p>
</body></html>
"""

soup=BeautifulSoup(html, "html.parser")
# soup.find
h1=soup.body.h1
print(h1)
p1= soup.html.body.p  #처음 만나는 p2태그가 계속 참조
# print(p2.string)
p2=p1.next_sibling.next_sibling
p3=p2.next_sibling.next_sibling