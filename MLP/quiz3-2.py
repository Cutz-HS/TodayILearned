### Q3 ###
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac_data/stock.csv", sep=",")
X = all_data.iloc[:, :-1]
y = pd.DataFrame(all_data.iloc[:, -1])
memoryList = []

# scaling & rollback #
def standard(x):
    global memoryList
    memoryList.append((np.mean(x), np.std(x)))
    return (x - np.mean(x)) / np.std(x)

def rollback(x, num):
    mean, std = memoryList[num][0], memoryList[num][1]
    return x * std + mean

# scaling #
X_scale = X.copy()
for i in range(len(X.iloc[0])):
    X_scale.iloc[:,i] = standard(X.iloc[:, i])
y_scale = standard(y)

## Variable & hyper parameter ##
learning_rate = 0.03
iteration = 10000

## train & test set 나누기 ##
X_train, X_test, y_train, y_test = train_test_split(X_scale, y_scale, train_size=0.7, random_state=77)
#y_train = np.array(y_train).reshape(len(y_train), 1)
#y_test = np.array(y_test).reshape(len(y_test), 1)

## 이상치 처리 ##
#print(X_scale.describe())
X_train.boxplot() # Volume 칼럼에서만 이상치 발견
q1, q3 = np.percentile(X_train['Volume'], (25, 75))
iqr = q3 - q1
#print(X_scale[X_scale['Volume'] > q3 + (1.5 * iqr)]) # 70개의 이상치 제거
X_iqr = X_train[X_train['Volume'] < q3 + (1.5 * iqr)] # (1002, 4)
idx = X_iqr.index
y_train = y_train[idx] # shape (1440, 1)

## tf building ##
X = tf.placeholder(dtype=tf.float32, shape=[None, 4])
y = tf.placeholder(dtype=tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([4, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]),  name='bias')
hypothesis = tf.matmul(X, W) + b

cost = tf.reduce_mean(tf.square(hypothesis - y))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

## learning ##
for i in range(iteration):
    _, cost_val = sess.run([train, cost],
                           feed_dict={X: X_train, y: y_train})
#    if i % 100 == 0:
#        print(cost_val)

## 예측 ##
y_hat = sess.run(hypothesis, feed_dict={X: X_test})
y_hat_back = rollback(y_hat, 4) # 표준화 데이터를 원 데이터 scale로 복구
y_test_back = rollback(y_test, 4) # 표준화 데이터를 원 데이터 sclae로 복구
error = (1 / len(y_hat_back)) * np.sum(np.square(y_hat_back - y_test_back))
sess.close()

print("learning_rate: ", learning_rate, "\nlearn: ", iteration, "\ncost: ", cost_val)
## 시각화 ##
plt.figure()
plt.plot(y_test_back, 'bo')
plt.legend("testdata")
#plt.show()
#plt.figure()
plt.plot(y_hat_back, 'rx')
plt.legend("predict")
plt.show()

print("검증데이터와 예측데이터의 오차: ", error)





















