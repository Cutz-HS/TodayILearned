from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

if platform.system()=="Windows":
    font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

matplotlib.rcParams['axes.unicode_minus']=False

f=open("output_final.txt","r", encoding='utf-8')
i=1
news_word=[]
word_cnt=[]
while i<10:
    line=f.readline()
    word, count=line.split(" ")
    news_word.append(word)
    word_cnt.append(int(count[0]))
    i+=1

# '_' is 무시하는 코드
#xs=[i for i, _ in enumerate(news_word)]
plt.plot(news_word, word_cnt)
plt.ylabel("count on words")
plt.xlabel("weather key word on today's news")
plt.title("오늘의 뉴스 키워드")
plt.xticks([i for i, _ in enumerate(news_word)], news_word)
plt.show()

#print(news_word)
#print(word_cnt)
#print(xs)