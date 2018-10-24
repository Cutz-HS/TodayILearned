import tensorflow as tf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

tf.set_random_seed(777)

x1_data = [280, 310, 250, 270, 277]
x2_data = [310, 300, 225, 267, 307]
x3_data = [270, 325, 205, 290, 277]
y_data = [299, 327, 240, 270, 290]

x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_normal([1]), name='weight1')
w2 = tf.Variable(tf.random_normal([1]), name='weight2')
w3 = tf.Variable(tf.random_normal([1]), name='weight3')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = (x1 * w1) + (x2 * w2) + (x3 * w3) + b

cost = tf.reduce_mean(tf.square(hypothesis - y))
train = tf.train.GradientDescentOptimizer(learning_rate=0.000003).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    plt.figure()
    for i in range(5000):
        _, cost_val, y_hat = sess.run([train, cost, hypothesis], 
                               feed_dict={x1: x1_data, x2: x2_data, x3: x3_data, y: y_data})
        if i % 100 == 0:
            print(cost_val)
#            plt.plot(w1_val[0], cost_val, 'rx')

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot(x1_data, x2_data, y_data, 'rx')
#ax.plot(x1_data, x2_data, y_hat, 'b-')   
    
    