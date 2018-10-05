# 날씨
from bs4 import BeautifulSoup
import urllib.request as req
import codecs

url="https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=103&oid=422&aid=0000333483"
output_File='output.txt'
    
def get_text(url):
    site=req.urlopen(url)
    soup=BeautifulSoup(site, 'lxml')
    res=""
    for i in soup.find_all("div", id="articleBodyContents"):
        res+=i.text.replace(i.find("script").text, "")
        for j in i.find_all("a"):
            res=res.replace(j.text, "")
    return res

def main(file):
#    if not os.path.exists(file):
    openFile=codecs.open(file, "w", encoding='utf-8')
    openFile.write(get_text(url))
    openFile.close()

if __name__=="__main__":
    main(output_File)
