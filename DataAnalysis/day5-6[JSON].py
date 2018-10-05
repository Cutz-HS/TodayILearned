import urllib.request as req
from bs4 import BeautifulSoup
import os.path

url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnID=108"
saveName="forecast.xml"
if not os.path.exists(saveName):
    req.urlretrieve(url, saveName)

xml=open(saveName, "r", encoding='utf-8').read()
soup=BeautifulSoup(xml, 'html.parser')

## <wf> <city>
#loc=soup.find_all("location")[0]
#print(loc)
cloudDict={}
wf=[]
# 하나로 합치기 for문
for location in soup.find_all("location"):
    name=location.find('city').string
    weather=location.find('wf').string
    if weather in cloudDict:
        cloudDict[weather].append(name)
    else:
        wf.append(name)
        cloudDict[weather]=wf
        wf=[]
print(cloudDict)

for locW in cloudDict:
    print("+", locW)
    for name in cloudDict[locW]:
        print("|-", name,"-", end="|")
    print("")