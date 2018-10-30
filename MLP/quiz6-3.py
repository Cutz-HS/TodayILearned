### Q3 ###
import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import numpy as np

## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/wine.data.txt", sep=",", header=None)
X_data = all_data.iloc[:, 1:] # shape(178, 13)
y_data = all_data.iloc[:, [0]] # shape(178,)

# min-max 정규화 #
mms = MinMaxScaler()
X_scale = mms.fit_transform(X_data)

# one-hot #
y_dummy = pd.get_dummies(y_data.astype(np.str))

# split #
X_train, X_test, y_train, y_test = train_test_split(X_scale, y_dummy, train_size=0.7, random_state=77)

## parameter ##
learning_rate = 0.1
epochs = 3000
classes = 3

## tf building ##
X = tf.placeholder(dtype=tf.float32, shape=[None, 13])
Y = tf.placeholder(dtype=tf.int32, shape=[None, classes])

W = tf.Variable(tf.random_normal([13, classes]), name='weight')
b = tf.Variable(tf.random_normal([classes]), name='bias')
logits = tf.matmul(X, W)
hypothesis = tf.nn.softmax(logits)

cost_i=tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y)

cost = tf.reduce_mean(cost_i)
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# 정확도 tf #
predict = tf.cast(tf.argmax(hypothesis, axis=1), dtype=tf.int64)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, axis=1)), dtype=tf.float32))

# training #
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(epochs):
        cost_val, _, y_hat= sess.run([cost, train, hypothesis], feed_dict={X: X_train, Y: y_train})
        if i % 100 == 0:
            print(cost_val)
    
    # predict #
    y_hat, acc, pred = sess.run([hypothesis, accuracy, predict],
                          feed_dict={X: X_test, Y: y_test})
    
print("learning_rate: ", learning_rate, "\nlearn: ", epochs, "\ncost: %0.3f" %cost_val)
print("검증 정확도: ", acc)
    
for p, y in zip(pred, np.argmax(np.array(y_test), axis=1)):
        print("[{}] Prediction: {} True Y: {}".format(p == int(y), p, int(y)))


















