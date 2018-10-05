# 웹 콘텐츠 가져오기
import urllib.request as req
import urllib.parse

# 1
url="http://www.kccistc.net/images/layout/logo_09000_1.png"
req.urlretrieve(url, "test.png")
print("save pic")

# 2
saveName="test2.png"
mem=req.urlopen(url).read()
print(type(mem))
with open(saveName, mode="wb") as f:
    f.write(mem)
    print("saved")

url="http://www.kccistc.net"
mem=req.urlopen(url).read()
text=mem.decode("utf-8")
print(text)


api="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values={
    'stnId':'108'
}
params=urllib.parse.urlencode(values)
url=api+"?"+params

data=req.urlopen(url).read().decode("utf-8")
print(data)
