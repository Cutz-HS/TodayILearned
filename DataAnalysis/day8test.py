from bs4 import BeautifulSoup
import urllib.request as req
import re
from konlpy.tag import Twitter
from collections import Counter
from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

if platform.system()=="Windows":
    font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

matplotlib.rcParams['axes.unicode_minus']=False

url="https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=100&oid=052&aid=0001181609"
#div#articleBodyContents

def crawl(url):
    data=req.urlopen(url)
    html=BeautifulSoup(data, 'html.parser')
    textList=html.find_all("div", id="articleBodyContents")
    res=""
    for line in textList:
        if line.find("script") in line:
            res+=line.text.replace(line.find("script").text, "")
        if line.find("a") in line:
            for a in line.find_all("a"):
                res=res.replace(a.text, "")
    return res
    
def clean_text(text):
    pattern1=r'\s{3,}[\w\s]{6}\s{3,}'
    pattern2=r'[[\[][\w\W\s]{1,50}[\]]'
    text=re.sub(pattern1, " ", text)
    text=re.sub(pattern2, " ", text)
    return text

def get_noun(text):
    twit=Twitter()
    noun=twit.nouns(text)
    return noun

def rank(sequence):
    rank=Counter(sequence)
    return rank.most_common()
    
def plot(sequence, maxnum):
    name=[]
    count=[]
    for i, j in sequence:
        name.append(i)
        count.append(j)
    plt.bar(name[:maxnum], count[:maxnum])
    plt.xlabel("name")
    plt.ylabel("count")
    plt.title("문재인 대통령 광복절 경축사 사용단어 빈도")
    plt.show()
    
def main():
    text=clean_text(crawl(url))
    rankList=rank(get_noun(text))
    plot(rankList, 10)

if __name__=='__main__':
    main()
