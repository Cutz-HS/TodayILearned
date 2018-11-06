### recommender system ###
## collaborative filtering ##
import numpy as np
import matplotlib as mpl
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

# 한글 폰트 깨지는 문제 #
mpl.rcParams['axes.unicode_minus'] = False
font_name = font_manager.FontProperties(fname="c:/windows/fonts/malgun.ttf").get_name()
rc('font', family=font_name)


critics = {
    'BTS':{'암수살인':5, '바울':4, '할로윈':1.5},
    '손흥민':{'바울':5, '할로윈':2},
    '조용필':{'암수살인':2.5, '바울':2, '할로윈':1},
    '나훈아':{'암수살인':3.5, '바울':4, '할로윈':5}}

#print(critics['BTS']['바울'])

def vector(dic):
    return [list(dic[value].values()) for value in dic]

vector_list = vector(critics)

def dist_sim(i, j):
    dist_vec = np.array(i) - np.array(j)
    return np.sqrt(np.dot(dist_vec, dist_vec))
#c_d = dist_sim(vector_list[2], vector_list[3])
#b_d = dist_sim(vector_list[1], vector_list[3][1:])

def cos_sim(i, j):
    i, j = np.array(i), np.array(j)
    a = np.dot(i, j)
    b = np.sqrt(np.dot(i, i)) * np.sqrt(np.dot(j, j))
    return a / b       

def p_cov(i, j):
    i, j = np.array(i), np.array(j)
    mean_i = np.mean(i)
    mean_j = np.mean(j)
    a = np.sum((i - mean_i) * (j - mean_j))
    b = np.sqrt(np.sum(np.square(i - mean_i))) * np.sqrt(np.sum(np.square(j - mean_j)))
    return a / b

c_d = cos_sim(vector_list[2], vector_list[3])
c_d_p = p_cov(vector_list[2], vector_list[3])

#for i in range(len(critics)):
#    if i != 1:
#        print(list(critics.keys())[i], "and bts sim: ", dist_sim(vector_list[0], vector_list[i]))
#
#for i in range(len(critics)):
#    if i != 1:
#        print(list(critics.keys())[i], "and bts sim: ", cos_sim(vector_list[0], vector_list[i]))
#        
#for i in range(len(critics)):
#    if i != 1:
#        print(list(critics.keys())[i], "and bts sim: ", p_cov(vector_list[0], vector_list[i]))
        
def sim_dist(data, name1, name2):
    summation = 0
    for i in data[name1]:
        if i in data[name2]:
            summation += pow(data[name1][i] - data[name2][i], 2)
    return summation**0.5


#for i in critics:
#    if i != 'BTS':
#        print(i, "and bts sim: ", sim_dist(critics, i, 'BTS'))

def matchf(data, name, idx=3, sim=sim_dist):
    myList=[]
    for i in data:
        if i!=name: #본인이 아닌경우라면
            myList.append((sim(data, name, i),i))#유사도,이름
            myList.sort()
#            print("정렬:", myList)
            myList.reverse()
#            print("역순:", myList)
#    print(len(myList))
    return myList[:idx]

#print(matchf(critics, '손흥민'))
#손흥민과 나머지 전체 관객과의 평점간 거리를 내림차순 정렬
li=matchf(critics, '손흥민')

def barchart(data, labels):
    positions = range(len(data))
    plt.barh(positions, data, height=0.5, color='r')
    plt.yticks(positions, labels)
    plt.xlabel('similarity')
    plt.ylabel('name')
    plt.show()
    
score = []
names = []
for i in li:
    score.append(i[0])
    names.append(i[1])
#barchart(score, names)

plt.figure(figsize=(14,8))
plt.plot([1,2,3], [1,2,3], 'g^')
plt.text(1,1,'자동차')
plt.text(2,2, '버스')
plt.text(3,3, '열차')
plt.axis([0,6,0,6])
plt.show()










