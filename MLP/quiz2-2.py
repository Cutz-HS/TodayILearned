### 과제: 속도가 30일때와 50일때의 제동거리를 예측 ###
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 데이터 전처리 #
all_data = pd.read_csv("d:/data/prac/cars.csv", sep=",")
all_data.columns = ["speed", "dist"]
x_data = all_data["speed"]
y_data = all_data["dist"]

# 변수 #
learning_rate = 0.003
iteration = 2000
costList, wList = [], []

# tf building #
X = tf.placeholder(dtype=tf.float32, shape=[None])
Y = tf.placeholder(dtype=tf.float32, shape=[None])

W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")
hypothesis = W * X + b # h(x)

cost = tf.reduce_mean(tf.square(hypothesis - Y)) # cost
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost) # gradeint

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # 변수 초기화
    
    for i in range(iteration):
        cost_val, y_hat, _, w_val = sess.run([cost, hypothesis, train, W],
                                             feed_dict={X: x_data, Y: y_data})
        costList.append(cost_val)
        wList.append(w_val[0])
        if i % 100 == 0:
            print(cost_val)
    
    predict = sess.run(hypothesis, feed_dict={X: [30, 50]})

w_sort_list = sorted(wList)

print("속도 30일 때의 제동거리: ", predict[0])
print("속도 50일 때의 제동거리: ", predict[1])
plt.figure()
plt.plot(x_data, y_data, 'rx')
plt.plot(x_data, y_hat, 'b-')
plt.show()

plt.figure()
plt.plot(w_sort_list, costList, 'y-')


