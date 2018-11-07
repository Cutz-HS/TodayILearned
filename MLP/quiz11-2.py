## Q12 ##
import numpy as np
import pandas as pd


## 함수 선언 ##
def file_open(file_name):
    ## file_open --> np.array ##
    file_open = open(file_name, 'r')
    all_data = []
    for i in file_open.readlines():
        all_data.append(i.strip('\n').split(','))
    all_data = np.array(all_data) # shape(9835, None)
    return all_data
    
def numbering(all_data):
    ## product를 dict에 넣으면서 numbering ##
    global all_item_num
    k = 0
    all_dict = {}
    for buy in all_data:
        for product in buy:
            if product in all_dict:
                continue
            else:
                all_dict[product] = k
            k += 1
    all_item_num = k
    for i in all_data:
        for k in range(len(i)):
            i[k] = all_dict[i[k]]
    return all_data, all_dict

def one_hot(data):
    ## 구매자마다 벡터화 시키기 위해 one-hot-encoding ## --> X: shape(9835, 169)
    one_hot = np.zeros([all_transaction, all_item_num], dtype=np.int32)
    for i in range(len(all_data)):
        for j in all_data[i]:
            one_hot[i,j] = 1
    return one_hot + 0.001 ## 연산시 0을 방지하기 위해 +

        
def cosine_sim(x, y):
    ## 코사인 유사도 ##
    return np.dot(x, y) / (np.sqrt(np.dot(x, x)) * np.sqrt(np.dot(y, y)))
    
def top_match(data, person_num, index=2, sim_function=cosine_sim):
    li = []
    for i in range(len(data)):
        if person_num != i:
            li.append((i, cosine_sim(data[person_num], data[i])))
    li = pd.DataFrame(li)
    li.columns = ['person_num', 'sim']
    li = li.sort_values(by=['sim'], ascending=False)
    return li.iloc[:index]

def getRecommend(data, person, sim_function=cosine_sim):
    global all_dict, all_data
    li = []
    score_dict = {}
    sim_dict = {}
    item_list = list(all_dict.keys())
    result = top_match(data, person, len(data))
    for i in range(len(result)):
        num = result['person_num'].iloc[i]
        sim = result['sim'].iloc[i]
        score = 0
        if sim < 0.5: continue
        for item in all_data[num]:
            if item not in all_data[person]:
                score += sim * data[i][item]
                score_dict.setdefault(item_list[item], 0)
                score_dict[item_list[item]] += score
                sim_dict.setdefault(item_list[item], 0)
                sim_dict[item_list[item]] += sim
    for key in score_dict:
        score_dict[key] = score_dict[key] / sim_dict[key]
        li.append((score_dict[key], key))
    li = np.array(li)
    li[:,0].sort()
    li = li[::-1]
    return li
    
## 전역 변수 ##
all_item_num = 0

if __name__ == "__main__":
    ## 파일 전처리 ##
    all_data = file_open("d:/data/prac/groceries.csv")
    all_transaction = len(all_data) # 전체 거래수 9835건
    all_data, all_dict = numbering(all_data) # 전체 아이템 개수 169개
    x_one_hot = one_hot(all_data)
#    match_1 = top_match(x_one_hot, 0, index=10)
    score = getRecommend(x_one_hot, 5)
    print("## 6번 손님에게 추천하는 item ##\n", score[:3])
