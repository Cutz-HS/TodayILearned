import tensorflow as tf
import numpy as np

xy = np.loadtxt('d:/data/prac/diabetes.csv', delimiter=',', dtype=np.float32)

x_data = xy[:, :-1] # shape(759, 8)
y_data = xy[:, [-1]] # shape(759, 1)

#print(x_data.shape, y_data.shape)

## tf building ##
X = tf.placeholder(tf.float32, shape=[None, 8])
y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([8, 1]), name='weight')
b = tf.Variable(tf.random_normal([1], name='bias'))
hypothesis = tf.nn.sigmoid(tf.matmul(X, W) + b)

cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1 - y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5000):
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, y: y_data})
        if i % 100 == 0:
            print(cost_val)
    predict, acc, y_hat = sess.run([predicted, accuracy, hypothesis],
                                   feed_dict={X: x_data, y: y_data})
    print("acc: ", acc)
    
