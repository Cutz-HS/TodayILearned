import re

# N-gram
class Ngram:
    def __init__(self):
        self.r=[]

    def split(self, text, n):
        pattern=re.compile("[\W\w\s]{1,%d}" %n)
        res=pattern.findall(text)
        if len(res[-1])!=n:
            res[-1]=text[len(text)-n:len(text)+1]
        return res
    
    def gram(self, sa, sb, num):
        saList=self.split(sa, num)
        sbList=self.split(sb, num)
        cnt=0
        for i in saList:
            for j in sbList:
                if i==j:
                    cnt+=1
                    self.r.append(i)
        return cnt/len(saList), self.r
#    if len(saList) > len(sbList):
#        return cnt/len(saList)
#    else: return cnt/len(sbList)



if __name__=="__main__":
    a="오늘 상공회의소에서 문자 비교 알고리즘을 배웠다"
    b="문자간 비교하는 알고리즘을 상공회의소에서 오늘 배웠다"
    # 2-gram
    ngram=Ngram()
    print(ngram.gram(a,b,2))
    # 3-gram
    print(ngram.gram(a,b,3))