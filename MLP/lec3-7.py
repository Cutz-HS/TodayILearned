import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as pp

tf.set_random_seed(777)

x_data = [[280, 310, 250],
          [270, 277, 310],
          [300, 225, 267],
          [307, 270, 325],
          [205, 290, 277]]

y_data = [[299],
          [327], 
          [240], 
          [270], 
          [290]]

X = tf.placeholder(tf.float32, [None, 3])
y = tf.placeholder(tf.float32, [None, 1])

W = tf.Variable(tf.random_normal([3, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = tf.matmul(X, W) + b

cost = tf.reduce_mean(tf.square(hypothesis - y))
train = tf.train.GradientDescentOptimizer(learning_rate=0.000003).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5000):
        _, cost_val, y_hat = sess.run([train, cost, hypothesis], 
                               feed_dict={X: x_data, y: y_data})
        if i % 100 == 0:
            print(cost_val) 