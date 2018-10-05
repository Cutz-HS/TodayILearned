from konlpy.tag import Twitter
from collections import Counter
import codecs


def get_Noun(text, count=30):
    twit=Twitter()
    noun=twit.nouns(text)
    return noun
    
def rank(list):
    rank=Counter(list)
    rankList=rank.most_common(20)
    return_list=[{'tag':word, 'count':cnt} for word, cnt in rankList]
    return return_list
    
def main():
    text_File="output2.txt"
    noun_Count=30
    outputFile="output_final.txt"
    openFile=codecs.open(text_File, "r", encoding="utf-8")
    text=openFile.read()
    word=get_Noun(text, noun_Count)
    wordList=rank(word)
    openFile.close()
    
    saveFile=codecs.open(outputFile, "w", encoding="utf-8")
    for data in wordList:
        noun=data['tag']
        count=data['count']
        saveFile.write("{} {}\n".format(noun, count))
    saveFile.close()

if __name__=='__main__':
    main()

#colors=['r','b','r','g','b','b','b','g','r','b','r','g','g','g','g']
#cnt=Counter(colors)
#print(cnt)
#print(cnt.most_common(2))