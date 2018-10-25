## Logistic classification ##
import tensorflow as tf
import numpy as np
import math

xx = [[1,1,1,1,1,1],
      [2,3,3,5,7,2],
      [1,2,5,5,5,5]]

yy = np.array([0, 0, 0, 1, 1, 1])

X = tf.placeholder(tf.float32, [3,None])
y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_normal([5, 3]))
#z = tf.matmul(W, X) # (1 x 3) (3 x 6)
layer1 = tf.nn.sigmoid(tf.matmul(W, X))

W2 = tf.Variable(tf.random_normal([1, 5]))
hypothesis = tf.nn.sigmoid(tf.matmul(W2, layer1))


cost = tf.reduce_mean(-y * tf.log(hypothesis) - (1 - y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.3).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(5000):
    cost_val, _ = sess.run([cost, train], feed_dict={X: xx, y: yy})
    if i % 50 == 0:
        print(cost_val)
        
predict = sess.run(hypothesis, feed_dict={X: [[1, 1], [3, 7], [8, 2]]})
print(predict)

def sigmoid(z):
    return 1/(1+math.e**-z)

ww = sess.run(W)
z=np.dot(ww, xx)
print(sigmoid(z))


sess.close()