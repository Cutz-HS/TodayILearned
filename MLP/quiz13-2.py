# =================================================================================== #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

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
#for i in range(len(k_list)): # [1,3,5,7,9,11,13,15,17,19]로 각각의 k 모델링
#    knn = KNeighborsClassifier(n_neighbors=k_list[i], p=2, metric='minkowski')
#    knn.fit(x_train, y_train)
#    predict = knn.predict(x_test).reshape(len(x_test), 1)
#    acc = np.equal(y_test, predict)
#    accuracy = len(predict[acc]) / len(y_test)
#    k_chart.iloc[i, 0] = k_list[i]
#    k_chart.iloc[i, 1] = accuracy
#    
## 시각화 ##
#plt.figure(figsize=(13,5))
#plt.xlabel("K-value")
#plt.ylabel("accuracy")
#plt.plot(k_chart["K_value"], k_chart["acc"], "r-") # k값이 커짐에 따라 82% 정도에 수렴

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
sess = tf.Session()
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