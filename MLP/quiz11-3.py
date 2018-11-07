## Q13: K-means ##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import cdist, pdist

## 파일 전처리 ##
def file_open(file_name):
    ## file_open --> np.array ##
    file_open = open(file_name, 'r')
    all_data = []
    for i in file_open.readlines():
        all_data.append(i.strip('\n').split(','))
    all_data = np.array(all_data) # shape(9835, None)
    return all_data

all_data = file_open("d:/data/prac/groceries.csv")

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

all_transaction = len(all_data) # 전체 거래수 9835건
all_item_num = 0 # 169개
all_data, all_dict = numbering(all_data) # 전체 아이템 개수 169개

## one-hot ##
def one_hot(data):
    ## 구매자마다 벡터화 시키기 위해 one-hot-encoding ## --> X: shape(9835, 169)
    one_hot = np.zeros([all_transaction, all_item_num], dtype=np.int32)
    for i in range(len(all_data)):
        for j in all_data[i]:
            one_hot[i,j] = 1
    return one_hot

x_one_hot = one_hot(all_data) # one-hot

## split ##
x_train, x_test = x_one_hot[:9800, :], x_one_hot[9800:, :]

## Kmeans ##
# n_cluster = 10, max_iter=3000 #
k_means = KMeans(n_clusters=10, max_iter=3000, random_state=77)
k_means.fit(x_train)
k_cluster = k_means.predict(x_test)
ss = silhouette_score(x_train, k_means.labels_, metric='euclidean')
print("테스트 데이터 35명의 클러스터: \n", k_cluster)
print("\nsilhouette_score: ", ss)          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          