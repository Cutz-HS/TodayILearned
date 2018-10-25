import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

tf.set_random_seed(777)

x_data = [[1,2], [2,3], [3,1], [4,3], [5,3], [6,2]]
x_data = np.array(x_data)
y_data = [[0],[0],[0],[1],[1],[1]]
y_data = np.array(y_data)

X = tf.placeholder(dtype=tf.float32, shape=[None, 2])
y = tf.placeholder(dtype=tf.float32, shape=[None, 1])

W = tf.Variable(tf.zeros([2, 1]), name='weight')
b = tf.Variable(tf.zeros([1]), name='bias')
hypothesis = tf.nn.sigmoid(tf.matmul(X, W) + b)

cost = tf.reduce_mean(-y * tf.log(hypothesis) - (1 - y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=1.1).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(8000):
    cost_val, _, y_hat, w_val, b_val = sess.run([cost, train, hypothesis, W, b], feed_dict={X: x_data, y: y_data})
    if i % 50 == 0:
        print(cost_val)

plt.figure()
all_data = np.hstack((x_data, y_data))
x_0 = all_data[all_data[:, 2] == 0]
x_1 = all_data[all_data[:, 2] == 1]
plt.plot(x_0[:, 0], x_0[:, 1], 'rx')
plt.plot(x_1[:, 0], x_1[:, 1], 'bo')
boundary_x = np.array([np.min(x_data[:,0]), np.max(x_data[:,0])])
boundary_y = (- 1. / w_val[1][0]) * (b_val[0] + w_val[0][0] * boundary_x)
plt.plot(boundary_x, boundary_y, 'y-')
plt.grid(True)
plt.show()



sess.close()