from bs4 import BeautifulSoup
import urllib.request

html="""
<html><body>
<div id="test">
<h1> 빅데이터 분석 </h1>
<ul class="lec">
<li>파이썬</li>
<li>머신러닝</li>
<li>통계분석</li>
</ul>
</div>
</body></html>
"""

soup=BeautifulSoup(html, 'html.parser')
print(soup)
res=soup.select_one("div#test > h1").string
print(res)
res=soup.select_one("div#test > ul.lec > li").string
print(res)
res=soup.li
res2=res.next_sibling.next_sibling
res3=res2.next_sibling.next_sibling
print(res.string)
print(res2.string)
print(res3.string)

res=soup.select("div#test > ul.lec > li ")
for li in res:
    print(li.string)