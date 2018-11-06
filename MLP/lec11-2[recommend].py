### 추천 시스템 ###
## 협업 필터링 ##
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

mpl.rcParams['axes.unicode_minus'] = False
font_name = font_manager.FontProperties(fname="c:/windows/fonts/malgun.ttf").get_name()
rc('font', family=font_name)


critics = {
    '조용필': {
        '택시운전사': 2.5,
        '겨울왕국': 3.5,
        '리빙라스베가스': 3.0,
        '넘버3': 3.5,
        '사랑과전쟁': 2.5,
        '세계대전': 3.0,
    },
    'BTS': {
        '택시운전사': 1.0,
        '겨울왕국': 4.5,
        '리빙라스베가스': 0.5,
        '넘버3': 1.5,
        '사랑과전쟁': 4.5,
        '세계대전': 5.0,
    },
    '강감찬': {
        '택시운전사': 3.0,
        '겨울왕국': 3.5,
        '리빙라스베가스': 1.5,
        '넘버3': 5.0,
        '세계대전': 3.0,
        '사랑과전쟁': 3.5,
    },
    '을지문덕': {
        '택시운전사': 2.5,
        '겨울왕국': 3.0,
        '넘버3': 3.5,
        '세계대전': 4.0,
    },
    '김유신': {
        '겨울왕국': 3.5,
        '리빙라스베가스': 3.0,
        '세계대전': 4.5,
        '넘버3': 4.0,
        '사랑과전쟁': 2.5,
    },
    '유성룡': {
        '택시운전사': 3.0,
        '겨울왕국': 4.0,
        '리빙라스베가스': 2.0,
        '넘버3': 3.0,
        '세계대전': 3.5,
        '사랑과전쟁': 2.0,
    },
    '이황': {
        '택시운전사': 3.0,
        '겨울왕국': 4.0,
        '세계대전': 3.0,
        '넘버3': 5.0,
        '사랑과전쟁': 3.5,
    },
    '이이': {'겨울왕국': 4.5, '사랑과전쟁': 1.0,
             '넘버3': 4.0},
}
    
def draw(data, name1, name2):
    plt.figure(figsize=(14,8))
    for i in data[name1]:
        if i in data[name2]:
            plt.plot(i, data[name1][i], 'ro')
            plt.text(i, data[name1][i], name1)
            plt.plot(i, data[name2][i], 'bo')
            plt.text(i, data[name2][i], name2)
    plt.axis([-1, 6, 0, 6])
#    plt.yticks(ticks=0.5, lables="score")
    plt.xlabel(name1)
    plt.show()
    
#    
#draw(critics, 'BTS', '유성룡')
#draw(critics, '이황', '조용필')
    
    
def p_cov(data, name1, name2):
    mean_x = [data[name1][i] for i in data[name1] if i in data[name2]]
    mean_y = [data[name2][i] for i in data[name1] if i in data[name2]]
    x_mean = sum(mean_x) / len(mean_x)
    y_mean = sum(mean_y) / len(mean_y)
    xy_cov = sum([(mean_x[i] - x_mean) * (mean_y[i] - y_mean) for i in range(len(mean_x))])
    x_cov = sum([(i - x_mean)**2 for i in mean_x])**0.5
    y_cov = sum([(i - y_mean)**2 for i in mean_y])**0.5
    return xy_cov / (x_cov * y_cov)
    
    
#print(p_cov(critics, 'BTS', '유성룡'))
#print(p_cov(critics, '이황', '조용필'))    
    
def top_match(data, name, index=2, sim_function=p_cov):
    li = []
    for i in data:
        if name != i:
            li.append((p_cov(critics, name, i), i))
    li.sort()
    li.reverse()
    return li[:index]
    

#print(top_match(critics, '조용필', 5))

def getRecom(data, person, sim_function=p_cov):
    li = []
    score_dict = {}
    sim_dict = {}
    score = 0
    result = top_match(data, person, len(data))
    for sim, name in result:
        if sim < 0: continue
        for movie in data[name]:
            if movie not in data[person]:
                score += sim * data[name][movie]
                score_dict.setdefault(movie, 0)
                score_dict[movie] += score
                sim_dict.setdefault(movie, 0)
                sim_dict[movie] += sim
    for key in score_dict:
        score_dict[key] = score_dict[key] / sim_dict[key]
        li.append((score_dict[key], key))
    li.sort()
    li.reverse()
    return li
    
print(getRecom(critics, '이이'))  
    
    
    
    
    
    
    
    
    