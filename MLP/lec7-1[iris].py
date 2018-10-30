import tensorflow as tf
import numpy as np

all_data = np.loadtxt("d:/data/prac/iris_softmax.csv", delimiter=",", dtype=np.float32)

x_data = all_data[:, 1:-3]
y_data = all_data[:, -3:]
y_data = np.array(y_data, dtype=np.int32)

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 3])

W = tf.Variable(tf.random_normal([4, 3]), name='weight')
b = tf.Variable(tf.random_normal([3]), name='bias')
logits = tf.matmul(X, W) + b
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
train = tf.train.AdamOptimizer(learning_rate=0.3).minimize(cost)

predict = tf.cast(tf.argmax(hypothesis, axis=1), dtype=tf.int64)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, axis=1)), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1500):
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
        if i % 100 == 0:
            print(cost_val)
        
        acc, y_hat, pred = sess.run([accuracy, hypothesis, predict], feed_dict = {X: x_data, Y: y_data})
    
    
