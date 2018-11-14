### Q1: SNS data: K-means ###
### Q1+: PCA -> K-means ###
### Q1+: SNS data 결측치 대체(KNN) ###
### Q1+: SNS data 결측치 대체(deep learning) ###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import cdist, pdist
from sklearn.metrics import classification_report

### Q1: SNS data Kmeans ###
## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/snsdata.csv") # shape(30000, 40)
X = all_data.iloc[:, 4:] # NA값이 많은 age feature 제거 # NA값이 많은 gender 제거

## Scaling ##
mm = MinMaxScaler()
X_scale = mm.fit_transform(X)

## K-Means ## --> 클러스터 숫자 5
kmeans = KMeans(n_clusters=5, max_iter=3000, random_state=77)
kmeans.fit(X_scale)
X_cluster = kmeans.predict(X_scale)

# 클러스터링 & 분석 #
all_data['cluster'] = X_cluster

A = all_data[all_data['cluster'] == 0] # 5983 --> Shopping cluster: shopping 지식에는 관심이 많지만, beuaty 제품은 제외
B = all_data[all_data['cluster'] == 1] # 712 --> Beuaty cluster: 친구수가 가장 많고, beauty 제품의 빈도수가 높다.
C = all_data[all_data['cluster'] == 2] # 1899 --> Sports cluster: sport 관련 단어수가 가장 높다.
D = all_data[all_data['cluster'] == 3] # 19807  --> Non-character: 친구수도 가장 적고, 별다른 특징이 없는 그룹
E = all_data[all_data['cluster'] == 4] # 1599 --> Violence cluster: 선정적인 단어 빈도수가 가장 높다.(drug)
#print(len(A)) ;print(len(B)) ;print(len(C)) ;print(len(D)) ;print(len(E))

## groupby sum --> 각 클러스터별 빈도단어 평균 파악 ##
cluster_sum = all_data.groupby(['cluster'], as_index=False).mean()
# silhouette_score: 클러스터의 밀집도 측정, -1~1 --> 값이 클수록 클러스터끼리 분리 #
ss = silhouette_score(X_scale, kmeans.labels_, metric='euclidean')
#print(ss) # 0.1989

## 최적의 k값 찾기 ##
for k in range(3,11):
    kmeans_k = KMeans(n_clusters=k, max_iter=2000)
    kmeans_k.fit(X_scale)
    print("%i's siloutte score: " %(k), silhouette_score(X_scale, kmeans_k.labels_, metric='euclidean'))
    
# 엘보 그래프 #
K = range(3,21,2)
KM = [KMeans(n_clusters=k).fit(X_scale) for k in K]
centroids = [k.cluster_centers_ for k in KM]
D_k = [cdist(X_scale, centrds, 'euclidean') for centrds in centroids] # 각 클러스터의 센터와 구성원 거리
cIdx = [np.argmin(D, axis=1) for D in D_k] # 거리 중 최소
dist = [np.min(D, axis=1) for D in D_k]
avgWithinSS = [sum(d) / X_scale.shape[0] for d in dist] # sum of square dist
wcss = [sum(d**2) for d in dist]
tss = sum(pdist(X_scale)**2) / X_scale.shape[0]
bss = tss - wcss
# 엘보그래프 시각화 #
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, avgWithinSS, 'b*-')
plt.grid(True)
plt.xlabel('K')
plt.ylabel('Avg SS')
plt.show()
# 해석된 분산 percentage 엘보 커브 #
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(K, bss/tss*100, 'b*-')
plt.grid(True)
plt.xlabel('K')
plt.ylabel('Per of variance explained')
plt.show()
# =================================================================================== #



# =================================================================================== #
### Q1+: PCA -> K-means ###
from sklearn.decomposition import PCA

# PCA: 설명된 분산 그래프 # --> 증가폭이 감소하는 구간 혹은 설명된 분산 80% 이상을 PCA n 마지노선으로 판단
max_pca_n = 36
pcs = []
tot_expvar = []

for i in range(max_pca_n):
    pca = PCA(n_components=i+1, random_state=77) # 0부터 시작하기에 1
    reduced_X = pca.fit_transform(X_scale)
    tot_var = pca.explained_variance_ratio_.sum() # 설명된 분산 합
    pcs.append(i+1)
    tot_expvar.append(tot_var)
# 시각화 #
plt.figure()
plt.plot(pcs, tot_expvar, 'r')
plt.plot(pcs, tot_expvar, 'bs')
plt.xlabel('# of PCn')
plt.ylabel('exp var')
plt.xticks(pcs)
plt.show() # --> 설명된 분산의 증가폭이 감소하면서 0.8에 근접한 n=15으로 결정
# 36개의 feature --> 15 features로 차원 축소 #
pca = PCA(n_components=15, random_state=77)
X_pca = pca.fit_transform(X_scale)
#print(pca.explained_variance_ratio_.sum()) # 0.7584 --> 75% 설명

## PCA k-means ##
kmeans = KMeans(n_clusters=5, max_iter=3000, random_state=77)
kmeans.fit(X_pca)
pca_cluster = kmeans.predict(X_pca)

# group_by #
all_data['cluster_pca'] = pca_cluster

A = all_data[all_data['cluster_pca'] == 0] # 19527 --> Non-character cluster (대다수 이전의 D 클러스터)
B = all_data[all_data['cluster_pca'] == 1] # 2720 --> Sports&Violence cluster (혼재)
C = all_data[all_data['cluster_pca'] == 2] # 5649 --> Shooping cluster (대다수 이전의 A 클러스터)
D = all_data[all_data['cluster_pca'] == 3] # 712  --> Beuaty cluster (대다수 이전의 B 클러스터)
E = all_data[all_data['cluster_pca'] == 4] # 1392 --> Sports cluster (대다수 이전의 C 클러스터)
#print(len(A)) ;print(len(B)) ;print(len(C)) ;print(len(D)) ;print(len(E))

## groupby sum --> 각 클러스터별 빈도단어 평균 파악 ##
cluster_sum = all_data.groupby(['cluster_pca'], as_index=False).mean()
# silhouette_score: 클러스터의 밀집도 측정, -1~1 --> 값이 클수록 클러스터끼리 분리 #
ss = silhouette_score(X_scale, kmeans.labels_, metric='euclidean')
print(ss) # 0.200

# =================================================================================== #


# =================================================================================== #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

## Q1+: KNN 결측치 대체 ##
## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/snsdata.csv") # shape(30000, 40)
all_data = all_data.drop(['age'], axis=1) # NA값이 많은 age feature 제거
gender_na = all_data['gender'].isna() # gender na 추출
gender = all_data[gender_na == False] # gender NA값 제외 --> shape(27276, 40)
gender_na = all_data[gender_na] # shape(2724, 40)

## gender 결측치 채우기: KNN ##
X = gender.iloc[:, 2:] # shape(27276, 38)
y = gender[['gender']] # shape(27276, 1)

# scaling #
mm = MinMaxScaler()
X_scale = mm.fit_transform(X)

# split #
x_train, x_test, y_train, y_test = train_test_split(X_scale, y, train_size=0.7, test_size=0.3, random_state=77)

# KNN #
### Q1+: k tuning graph ###
k_chart = np.zeros((10, 2)) # K_value, acc
k_chart = pd.DataFrame(k_chart)
k_chart.columns = ["K_value", "acc"]
k_list = [3,5,7,9,15,17,19,25,31,41]

## train ##
for i in range(len(k_list)): # [1,3,5,7,9,11,13,15,17,19]로 각각의 k 모델링
    knn = KNeighborsClassifier(n_neighbors=k_list[i], p=2, metric='minkowski')
    knn.fit(x_train, y_train)
    predict = knn.predict(x_test).reshape(len(x_test), 1)
    acc = np.equal(y_test, predict)
    accuracy = len(predict[acc]) / len(y_test)
    k_chart.iloc[i, 0] = k_list[i]
    k_chart.iloc[i, 1] = accuracy

## 시각화 ##
plt.figure(figsize=(13,5))
plt.xlabel("K-value")
plt.ylabel("accuracy")
plt.plot(k_chart["K_value"], k_chart["acc"], "r-") # k값이 커짐에 따라 82% 정도에 수렴
plt.show()

knn = KNeighborsClassifier(n_neighbors=21, p=2, metric='minkowski')
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test).reshape(len(x_test), 1)
predict = np.equal(y_pred, y_test)
acc = len(y_pred[predict]) / len(y_test)
#print(acc) # 0.82

# confusion matrix #
print("\nKNN - <confusion matrics>\n", pd.crosstab(np.array(y_test).flatten(), np.array(y_pred).flatten(), rownames=["Actual"], colnames=["Predict"]))
print("\nKNN - <classification matrics>\n", classification_report(y_test, y_pred))
## confusion matrix와 classfication의 결과에 따라, 남성 재현율이 굉장히 낮음을 확인: 0.24 ##
# =================================================================================== #


# =================================================================================== #
# ANN: 예측 시도 ##
### Q1+: deep learning (logistic) ###

# one-hot #
y_train[y_train=='F'] = 1
y_train[y_train=='M'] = 0
y_test[y_test=='F'] = 1
y_test[y_test=='M'] = 0
y_train = np.array(y_train).reshape(len(y_train), 1)
y_test = np.array(y_test).reshape(len(y_test), 1)
x_train = np.array(x_train)
x_test = np.array(x_test)

# parameter #
learning_rate = 0.3
epochs = 600
keep_prob = tf.placeholder(dtype=tf.float32)
batch_size = 256

## tensorflow building ##
X = tf.placeholder(dtype=tf.float32, shape=[None, 37])  # shape (398, 30)
y = tf.placeholder(dtype=tf.float32, shape=[None, 1]) # shape (398, 1)

# 초기값: he #
init = tf.keras.initializers.he_normal(seed=7)
W1 = tf.Variable(init([37, 50]), name="W1")
b1 = tf.Variable(init([50]), name='b1')
logits = tf.matmul(X, W1) + b1
l1 = tf.nn.relu(logits)
L1 = tf.nn.dropout(l1, keep_prob=keep_prob)

W2 = tf.Variable(init([50, 25]), name="W2")
b2 = tf.Variable(init([25]), name='b2')
logits = tf.matmul(L1, W2) + b2
l2 = tf.nn.relu(logits)
L2 = tf.nn.dropout(l2, keep_prob=keep_prob)

W3 = tf.Variable(init([25, 1]), name="W3")
b3 = tf.Variable(init([1]), name='b3')
logits = tf.matmul(L2, W3) + b3
hypothesis = tf.nn.sigmoid(logits)

# cost #
cost = tf.reduce_mean(tf.square(hypothesis - y))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

# acc #
predicted = tf.cast(hypothesis > 0.5, tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.float32))

## session ##
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.5)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
sess.run(tf.global_variables_initializer())

for i in range(epochs):
    cost_sum = 0
    total_batch = int(len(x_train) / batch_size) # batch
    train_idx = pd.Series([i for i in range(len(x_train))])
    for j in range(total_batch):
        if j == total_batch-2:
            x_batch, y_batch = x_train[train_idx], y_train[train_idx]
        else:
            idx = np.random.choice(train_idx, size=batch_size)
            x_batch, y_batch = x_train[idx], y_train[idx]
            train_idx = train_idx.drop(idx)
        cost_val, _,= sess.run([cost, train], feed_dict={X: x_batch, y: y_batch, keep_prob: 0.5})
        cost_sum += cost_val
    if i % 30 == 0:
        print(cost_sum)
        
acc, y_hat = sess.run([accuracy, hypothesis], feed_dict={X: x_test, y: y_test, keep_prob: 1.0})
print(acc) # 딥러닝 binary classification의 정확성도 0.8319 --> 낮다. 불가능
sess.close()
# =================================================================================== #


# =================================================================================== #