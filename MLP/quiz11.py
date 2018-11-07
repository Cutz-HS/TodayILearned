### Q11: 마트 연관규칙 A priori algorithm ###
### Q11+: 마트 데이터 기반 추천시스템(협업필터링) ###
### Q11+: 마트 데이터 클러스터링 K-means ###
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## Q11 ##
## 파일 전처리 ##
file_open = open("d:/data/prac/groceries.csv", 'r')

all_data = []
for i in file_open.readlines():
    all_data.append(i.strip('\n').split(','))

all_data = np.array(all_data) # shape(9835, None)
all_transaction = len(all_data) # 전체 거래수 9835건
all_dict = {}

## product를 dict에 넣으면서 numbering ##
k = 1
for buy in all_data:
    for product in buy:
        if product in all_dict:
            continue
        else:
            all_dict[product] = k
        k += 1
        
## numbering 적용 ##
max_num = 0
for i in all_data:
    for k in range(len(i)):
        i[k] = all_dict[i[k]]
        if max_num < len(i):
            max_num = len(i) # max_num = 32 --> 조합 32개 까지

## 함수 선언 ##
# n번 빈번 항목 집합 함수 #
def self_join_1():
    ## 1번 빈번 항목 집합 생성 ##
    global all_dict
    data = all_dict.values()
    res = [[i] for i in data]
    return res

def self_join(data, k):
    ## 가지치기 완료된 조합에 다음 빈번 항목 집합을 생성하는 함수 ##
    global category_1
    try:
        data = np.array(data)[:, 0]
        data_base = np.array(category_1)[:, 0]
    except: 
        print("해당 서포트에서 combination_num의 조합이 존재하지 않습니다.")
        return
    res_list = []
    print("data 개수: ", len(data))
    for i in range(len(data)):
        if i % 500 == 1: print("self_join continue.. ", i)
        data_tmp = data[i].copy()
        for j in range(len(data_base)):
            if data_base[j][0] not in data_tmp:
                data_tmp.append(data_base[j][0])
                if set(data_tmp) not in res_list:
                    res_list.append((set(data_tmp)))
            data_tmp = data[i].copy()
    print("complete, self_join")
    return res_list
               
def count_prune(data, pruning_num):
    ## 해당 상품 조합을 count하면서, prune num을 넘지 못하면, 비포함 ##
    # count & 가지치기 # 
    global all_data
    res_list = []
    print("data 개수: ", len(data))
    for pairs in data:
        k = 0
        for buy in all_data:
            switch = 0
            for product in pairs:
                if product not in buy:
                    switch = 1
            if switch == 1:
                continue
            else:
                k += 1
        if k >= pruning_num:
            res_list.append([list(pairs), k])
    print("complete, count_prune")
    return res_list

def a_priori(pruning_num, comb_num):
    ## main 실행 함수: 1번 빈번항목을 구한 뒤 for 문으로 2번 ~ k(comb_num)번까지 반복 ##
    global category_1, category_2
    product = self_join_1() # 1번 빈번 항목
    category_1 = count_prune(product, pruning_num) # count
    product_2 = self_join(category_1, 2)
    category_2 = count_prune(product_2, pruning_num)
    category = category_2.copy()
    for i in range(comb_num-2):
        product = self_join(category, i+3)
        if product == None: break
        category = count_prune(product, pruning_num)
    return category

def df(category):
    ## 도출된 결론 category count를 dataFrame 화 ##
    category = np.array(category)
    product = category[:, 0]
    num_df = pd.DataFrame(product.copy(), columns=['prod_num'])
    product_list = list(all_dict.keys())
    for i in range(len(product)):
        tmp_list = []
        for j in product[i]:
            tmp_list.append(product_list[j-1])
        category[i, 0] = tmp_list
    category = pd.DataFrame(category)
    category.columns = ['product', 'transaction']
    category = pd.concat((num_df, category), axis=1)
#    category = category.sort_values(by='transaction', ascending=False)
    return pd.DataFrame(category)

def support(res):
    ## support %를 구하는 함수 ##
    global all_transaction, category_1
    res['support'] = res['transaction'] / all_transaction # support = 교집합 / 전체거래수
    return res

def confidence_lift(row, index_num):
    ## 결과 df에서 특정 행의 특정 상품 confidence와 lift를 구하는 함수 ##
    ## 해당 행에서의 생성 가능한 상품 조합(k=2)의 confidence & lift를 연산 ##
    global category_1, category_2, all_transaction
    confidence = []
    product_num = row['prod_num']
    for i in category_1:
        if product_num[index_num] in i[0]:
            B_prob = i[1] / all_transaction
    for i in product_num:
        if i == product_num[index_num]:
            continue
        for j in category_1:
            if i in j[0]:
                x_prob = j[1]
                break
        for k in category_2:
            if set([product_num[index_num],i]) == set(k[0]):
                xy_prob = k[1]
                confidence.append(("%s -> %s" %(row['product'][product_num.index(i)], row['product'][index_num]), xy_prob / x_prob))
    confidence = np.array(confidence)
    lift = np.divide(np.array(confidence[:,[1]], dtype=np.float32), B_prob, dtype=np.float32)
    res = np.concatenate((confidence, lift), axis=1)
    res = pd.DataFrame(res, columns=["product", "confidence", "lift"])
    return res

## 전역 변수 ##
category_1 = [] # 1번 빈번 항목 저장 리스트
category_2 = [] # 2번 빈번 항목 저장 리스트 --> support와 confidence를 위해

## main ##
if __name__ == "__main__":
    category = a_priori(100, 3)
    result_3 = df(category)
    result_3 = support(result_3)
    ## lift : 선택한 상품과 짝 상품이 주어지지 않았을 때와 비교해 주어졌을 때 선택상품의 증가 비율 ##
    print(result_3.iloc[25]) # (특이: 우유, 야채, 소시지의 조합)
    sasauge_res = confidence_lift(result_3.iloc[25], 1)
    print(sasauge_res)
    print(result_3.iloc[26]) # (특이: 우유, 야채, 돼지고기의 조합)
    pork_res = confidence_lift(result_3.iloc[26], 1)
    print(pork_res)
    
    
    
    
    
    
    
    
    