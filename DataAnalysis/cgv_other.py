from bs4 import BeautifulSoup
import urllib.request as req
import os.path
url="http://www.cgv.co.kr/movies/"
savename="movie.xml"
if not os.path.exists(savename) :
    req.urlretrieve(url,savename)
xml=open(savename,mode="r",encoding="utf-8")
soup=BeautifulSoup(xml,"html.parser")
info ={}
i=0
chart=soup.find("div", "wrap-movie-chart")
for i in range(len(chart.find_all("strong","rank"))):
    rank=chart.find_all("strong","rank")[i].text
    name=chart.find_all("strong","title")[i].text
    percent=chart.find_all("span","percent")[i].text
    if not(rank in info):
        info[rank]=[]
    info[rank].append(name)
    info[rank].append(percent)
    i+=1
for locW in info :
    print("+",locW)
    for name in info[locW]:
        print("|-",name)