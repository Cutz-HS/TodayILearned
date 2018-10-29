import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

tf.set_random_seed(777)
np.random.seed(777)


## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/iris_softmax.csv", sep=",", header=None)
X_data = all_data.iloc[:, :-3] # shape (150, 5)
Y_data = all_data.iloc[:, -3:] # shape (150, 3)

## train-test split ##
def split(data, percent):
    num = int(percent * len(data))
    data = np.array(data)
    np.random.shuffle(data)
    return data[:num, :], data[num:, :]

x_train, x_test = split(X_data, 0.7)
y_train, y_test = split(Y_data, 0.7)

## hyper parameter ##
learning_rate = 0.1
epochs = 1500
m = X_data.shape[0]

# tf building #
X = tf.placeholder(dtype=tf.float32, shape=[None, 5])
Y = tf.placeholder(dtype=tf.float32, shape=[None, 3])

W = tf.Variable(tf.random_normal([5, 3]))
logit = tf.matmul(X, W)
hypothesis = tf.nn.softmax(logit)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())


for i in range(epochs):
    cost_val, _ = sess.run([cost, train], feed_dict={X: x_train, Y: y_train})
    if i % 100 == 0:
        print(cost_val)

sess.close()


















