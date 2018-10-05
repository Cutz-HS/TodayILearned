import math, sys
from konlpy.tag import Okt

class BayesianFilter:
    def __init__(self):
        self.words=set()
        self.word_dict={}
        self.category_dict={}
        
    def fit(self, text, category):
        '''
        텍스트를 읽어 학습
        '''
        pos=self.split(text)
        for word in pos:
            self.inc_word(word, category)
        self.inc_category(category)
        
    def split(self, text):
        '''
        형태소 분석
        '''
        twit=Okt()
        posList=twit.pos(text, norm=True, stem=True)
        for word in posList:
            if word[1] in ["Josa", "Eomi", "Punctuation"]:
                posList.remove(word)
        return posList
    
    def inc_word(self, word, category):
        '''
        카테고리 분류기
        '''
        if not category in self.word_dict:
            self.word_dict[category]={}
        if not word in self.word_dict[category]:
            self.word_dict[category][word]=0
        self.word_dict[category][word]+=1
        self.words.add(word)
        return
    
    def inc_category(self, category):
        '''
        카테고리 수치 dict 생성
        '''
        
        if not category in self.category_dict:
            self.category_dict[category]=0
        self.category_dict[category]+=1
        print(self.category_dict)
        
    def predict(self, text):
        '''
        새로운 텍스트를 받아 카테고리 예측
        '''
        best_category=None
        global gword
        gword=self.split(text)
        score_List=[]
        max_score=-sys.maxsize
        for category in self.category_dict.keys():
            score=self.score(gword, category)
            score_List.append((category, score))
            if score>max_score:
                max_score=score
                best_category=category
        return best_category, max_score


    def score(self, words, category):
        '''
        카테고리마다 점수(확률) 리턴
        '''
        score=math.log(self.category_prob(category))
        for word in words:
            score+=math.log(self.word_prob(word, category))
        return score
            
            
    def category_prob(self, category):
        '''
        카테고리 점수 계산
        '''
        sum_categories=sum(self.category_dict.values())
        category_v=self.category_dict[category] 
        return category_v / sum_categories
    
    def word_prob(self, word, category):
        '''
        단어 확률 계산
        '''
        n=self.get_word_count(word, category)+1
        # 광고에 속하는 등장횟수 총합 + 분류 대상 단어 총합
        d=sum(self.word_dict[category].values())+len(gword)
        # 총합 확률??
        return n/d
        
    
    def get_word_count(self, word, category):
        '''
        예측단어와 데이터셋 간 공통단어들의 카운트 계산
        '''
        if word in self.word_dict[category]:
            return self.word_dict[category][word]
        else:
            return 0
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    