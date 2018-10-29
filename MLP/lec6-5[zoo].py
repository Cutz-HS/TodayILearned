### zoo ###
import numpy as np
import tensorflow as tf

xy = np.loadtxt("d:/data/prac/zoo.csv", delimiter=",", dtype=np.float32)
xdata = xy[:, 0:-1]
ydata = xy[:, [-1]]
nb_classes = 7

X = tf.placeholder(tf.float32, [None, 16])
y = tf.placeholder(tf.int32, [None, 1])
y_one_hot = tf.one_hot(y, nb_classes) # --> (none, 1, 7)
y_one_hot = tf.reshape(y_one_hot, [-1, nb_classes])

W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')
logit = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logit)

cost = tf.reduce_mean(-tf.reduce_sum(y_one_hot * tf.log(hypothesis), axis=1))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1500):
        cost_val, _ = sess.run([cost, train], feed_dict={X: xdata, y: ydata})
        if i % 100 == 0:
            print(cost_val)