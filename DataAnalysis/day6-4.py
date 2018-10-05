import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

# W2V

fp=codecs.open("BEXX0003.txt", "r", encoding='utf-16')
soup=BeautifulSoup(fp, 'html.parser')
#print(soup)

# html > text
body=soup.select_one("body > text")
text=body.getText()

twit=Twitter()

# /r/n 제거
lines=text.split("\r\n")
result=[]
# word List comprehension // 필요오소만
#wordList=[i for line in lines for i,j in twit.pos(line, norm=True, stem=True) if not j in ["Josa", "Eomi", "Punctuation", "Foreign"]]
for line in lines:
    resList=twit.pos(line, norm=True, stem=True)
    res=[]
    for word in resList:
        if not word[1] in ["Josa", "Eomi", "Punctuation", "Foreign"]:
            res.append(word[0])
    r1=(" ".join(res))
    result.append(r1)
#print(result)   
    
# word embedding
toji="toji.data"
with open(toji, "w", encoding="utf-8") as fp:
    fp.write("\n".join(result))

# W2V
data=word2vec.LineSentence(toji)
model=word2vec.Word2Vec(data, size=200, window=2, min_count=5, sg=1, iter=10)
model.save("toji.mode")

# W2V 모델 불러오기
model=word2vec.Word2Vec.load("toji.mode")
print(model.most_similar(positive=["집"]))