# nums_g=[]
# for i in range(1,5000):
#     num_g = i + sum(int(t) for t in str(i))
#     nums_g.append(num_g)
# result = set(range(1,5000)) - set(nums_g)
# print(sum(result))
#
# #d(91) = 9 + 1 +91 = 101, 91(100)은 101의 제너레이터
# # for i in range(1234,1235):
# #     num_g = i + sum(int(t) for t in str(i))
# #     print(num_g) #sum([1,2,3,4]) '4'   '1234'
# # 1+2+3+4+1234=1244

# path="example.txt"
# data=open(path).readline()
# print(data)

import json
path="example.txt"
records=[json.loads(line) for line in open(path, encoding='utf-8')]
#print(records[0])
#print(records[0]['tz'])

time_zones=[rec['tz'] for rec in records if 'tz' in rec]
#print(time_zones)

#print(time_zones[:20])


def get_counts(sequence):
    counts={} #빈 딕셔너리
    for x in sequence:#'America/New_York'
        if x in counts: #도시명이 저장되어 있는 경우
            counts[x]+=1
        else: #저장 안되어 있는 경우
            counts[x]=1
    return counts

from collections import defaultdict
def get_counts2(sequence):
    counts=defaultdict(int)#0 초기화
    for x in sequence:
        counts[x]+=1
    return counts

counts=get_counts2(time_zones)
#print(counts)
# print(type(counts))
# print(counts['America/New_York'])
# print(len(counts))#도시의 개수(97)
# print(len(time_zones))#'tz'가 있는 행의 개수(3440)
# #가장 많이 등장한 10개를 출력

def top_counts(count_dict, n=10):
    value_key_pairs=[(value,key) for key,value in count_dict.items()]
    #print(value_key_pairs)
    value_key_pairs.sort()
   # print(value_key_pairs[-n:])
top_counts(counts,3)#상위 10개 도시 출력

from collections import Counter
counts=Counter(time_zones)
#print(counts.most_common(10))
#print(counts)

eng="sadklfdsalijsdfajkdd"
#print(Counter(eng))

#Pandas:
# 데이터분석 패키지(모듈(.py;함수,변수 등 구성요소 묶음) 또는 패키지의 묶음)

from pandas import DataFrame, Series
import pandas as pd
frame=DataFrame(records)#데이터를 표형태로 변환
#print(frame)
#print(frame.info())
#print(frame['tz'][:10])

tz_counts=frame['tz'].value_counts()
#print(tz_counts[:10])

#'tz':''
#'tz'키가 없음

#tz 키가 존재하지 않는 경우
clean_tz=frame['tz'].fillna('Missing')
#print(clean_tz)

#na:Not Available(결측값)
#tz키는 있지만, 값이 없는 경우(결측값)
clean_tz[clean_tz=='']='Unknown' #NA라고도 함
#print(type(clean_tz))
tz_counts=clean_tz.value_counts()

#print(tz_counts)

import matplotlib.pyplot as plt

tz_counts[:10].plot(kind='barh')
#plt.show()

#print(frame.a.dropna())#na행 제거

results=Series([x.split()[0] for x in frame.a.dropna()])#na행 제거
#print(type(results))
#print(results.value_counts()[:5])
#print(results)
# x="test1*te*st2*tes*t3"
# print(x.split())
#help()


#print(frame[frame.a.notnull()])
#print(len(frame)) #3560
cframe=frame[frame.a.notnull()]#120개 제거됨
#print(cframe)#'a' 키가 없는 행은 제거된 상태
#print(len(cframe)) #3440

#print(cframe.a)  # <=> print(cframe['a'])

import numpy as np
#print(cframe.a.str.contains('Windows'))
os=np.where(cframe.a.str.contains('Windows'),
         'Windows','Not Windows')
#print(os[:5])
by_tz_os=cframe.groupby(['tz',os])
#cframe을 os별로 'tz'값에 따라 그룹화
#print(by_tz_os)
agg_counts=by_tz_os.size().unstack().fillna(0)
#print(agg_counts.sum(1).argsort())


indexer=agg_counts.sum(1).argsort()
print(indexer[-10:])


count_subset=agg_counts.take(indexer)[-10:]
print(count_subset)

# normed_subset=count_subset.div\
#     (count_subset.sum(1), axis=0)
# normed_subset.plot(kind='barh', stacked=True)
count_subset.plot(kind='barh', stacked=True)
plt.show()


# s="My OS is Windows."
# print(s.contains('Linux'))

































