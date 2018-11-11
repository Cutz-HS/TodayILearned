### Q1: cancer KNN & confusion matrix ###
### Q1+: k tuning graph ###
### Q1+: cancer data PCA -> KNN ###
### Q1+: deep learing ###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import tensorflow as tf

### Q1: KNN ###
## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/wisc_bc_data.csv", sep=",", index_col=0) # shape(569, 31)
X = all_data.iloc[:, 1:] # X shape (569, 30)
y = all_data.iloc[:, 0] # y shape (569, 1) --> B: benigh, M: malignancy
# y -> 이산수치로 변환 # --> binary classification --> 0, 1일 때 sklearn knn이 되지 않는다.
#y[y=='M'] = 2
#y[y=='B'] = 1

## scaling ## --> K-NN은 거리에 민감하므로, 표준화
ss = StandardScaler()
X_scale = ss.fit_transform(X)
#plt.boxplot(X_scale) # boxplot으로 이상치 파악

# split #
x_train, x_test, y_train, y_test = train_test_split(X_scale, y, train_size=0.7, test_size=0.3, random_state=77)

## K-NN 적용 ## : p: 2norm(minkowski, diagonal) --> 1: manhatten(square)
knn = KNeighborsClassifier(n_neighbors=3, p=2, metric='minkowski')
knn.fit(x_train, y_train)
predict = knn.predict(x_test)
acc = np.equal(y_test, predict)
accuracy = len(predict[acc]) / len(y_test)
#print("acc: ", accuracy)

## confusion matrix ## --> f1 score 0.99 / 0.98
print("\nKNN - <confusion matrics>\n", pd.crosstab(y_test, predict, rownames=["Actual"], colnames=["Predict"]))
print("\nKNN - <accruacy_score>: ", round(accuracy, 3))
print("\nKNN - <classification report>\n\n", classification_report(y_test, predict))  

### Q1+: k tuning graph ###
k_chart = np.zeros((10, 2)) # K_value, acc
k_chart = pd.DataFrame(k_chart)
k_chart.columns = ["K_value", "acc"]
k_list = [1,3,5,7,9,11,13,15,17,19]

## train ##
for i in range(len(k_list)): # [1,3,5,7,9,11,13,15,17,19]로 각각의 k 모델링
    knn = KNeighborsClassifier(n_neighbors=k_list[i], p=2, metric='minkowski')
    knn.fit(x_train, y_train)
    predict = knn.predict(x_test)
    acc = np.equal(y_test, predict)
    accuracy = len(predict[acc]) / len(y_test)
    k_chart.iloc[i, 0] = k_list[i]
    k_chart.iloc[i, 1] = accuracy

## 시각화 ##
plt.figure(figsize=(13,5))
plt.xlabel("K-value")
plt.ylabel("accuracy")
plt.plot(k_chart["K_value"], k_chart["acc"], "r-")

# text 붙이기 #
for a, b in zip(k_chart["K_value"], k_chart["acc"]):
    plt.text(a, b, "k%i: %0.3f" %(a, b), fontsize=10)

plt.legend(loc="upper right")
plt.show()

### Q1+: SVD -> PCA -> KNN ###
## 공분산 행렬 ##
features = X_scale.T
cov = np.cov(features)

## 고유벡터, 고유값 ##
eig_value, eig_vector = np.linalg.eig(cov)
projected_X = np.dot(X_scale, eig_vector[0].T) # 고윳값이 가장 큰 벡터로 정사영
print(eig_value[0]/sum(eig_value)) # o.44% --> 낮다

# split #
x_train1, x_test1, y_train1, y_test1 = train_test_split(projected_X, y, train_size=0.7, test_size=0.3, random_state=77)
x_train1, x_test1 = x_train1.reshape(len(x_train1), 1), x_test1.reshape(len(x_test1))

## PCA KNN ##
knn = KNeighborsClassifier(n_neighbors=3, p=2, metric='minkowski')
knn.fit(x_train1, y_train1)
predict = knn.predict(x_test1.reshape(len(x_test), 1))
acc = np.equal(y_test1, predict)
accuracy = len(predict[acc]) / len(y_test1)
#print("acc: ", accuracy)

## confusion matrix ## --> f1 score 0.99 / 0.98
print("\nKNN - <confusion matrics>\n", pd.crosstab(y_test1, predict, rownames=["Actual"], colnames=["Predict"]))
print("\nKNN - <accruacy_score>: ", round(accuracy, 3))
print("\nKNN - <classification report>\n\n", classification_report(y_test1, predict))  

### Q1+: deep learning (logistic) ###

# one-hot #
y_train[y_train=='M'] = 1
y_train[y_train=='B'] = 0
y_test[y_test=='M'] = 1
y_test[y_test=='B'] = 0
y_train = np.array(y_train).reshape(len(y_train), 1)
y_test = np.array(y_test).reshape(len(y_test), 1)

# parameter #
learning_rate = 0.1
iteration = 5000
keep_prob = tf.placeholder(dtype=tf.float32)

## tensorflow building ##
X = tf.placeholder(dtype=tf.float32, shape=[None, 30])  # shape (398, 30)
y = tf.placeholder(dtype=tf.float32, shape=[None, 1]) # shape (398, 1)


# 초기값: xavier #
init = tf.keras.initializers.he_normal(seed=7)
W1 = tf.Variable(init([30, 50]), name="W1")
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
#cost = tf.reduce_mean(-y * tf.log(hypothesis) - (1 - y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

# acc #
predicted = tf.cast(hypothesis > 0.5, tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.float32))

## session ##
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(iteration):
    cost_val, _,= sess.run([cost, train], feed_dict={X: x_train, y: y_train, keep_prob: 0.5})
    if i % 500 == 0:
        print(cost_val)
        
acc, y_hat = sess.run([accuracy, hypothesis], feed_dict={X: x_test, y: y_test, keep_prob: 1.0})
print(acc)

sess.close()
