import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt

mnist = input_data.read_data_sets("d:/data/prac/mnist/data/", one_hot=True)

# hyper parameter #
classes = 10
learning_rate = 0.0001
epochs = 15
batch_size = 100
l2norm = 0.1
keep_prob = tf.placeholder(dtype=tf.float32)

## tf building ##
X = tf.placeholder(tf.float32, [None, 28*28])
Y = tf.placeholder(tf.float32, [None, classes])

# xavier init #
init = tf.contrib.layers.xavier_initializer(seed=77)

W1 = tf.Variable(init([28*28, 512]), name='weight1')
b1 = tf.Variable(init([512]), name='bias1')
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(layer1, keep_prob=keep_prob, seed=77, name='drop1')

W2 = tf.Variable(init([512, 256]), name='weight2')
b2 = tf.Variable(init([256]), name='bias2')
layer2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
L2 = tf.nn.dropout(layer2, keep_prob=keep_prob, seed=77, name='drop2')

W3 = tf.Variable(init([256, 10]), name='weight3')
b3 = tf.Variable(init([10]), name='bias3')
logits = tf.matmul(L2, W3) + b3
hypothesis= tf.nn.softmax(logits)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
opt = tf.train.AdamOptimizer(learning_rate=learning_rate)
train = opt.minimize(cost)

predict = tf.cast(tf.argmax(hypothesis, axis=1), dtype=tf.int64)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, axis=1)), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(epochs):
        total_batch = int(mnist.train.num_examples / batch_size)
        avg_cost = 0
        for j in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            cost_val, _ = sess.run([cost, train], 
                                   feed_dict={X: batch_x, Y: batch_y, keep_prob: 0.7})
            avg_cost += (cost_val / total_batch)
        plt.plot(i, avg_cost, "r*-")
        print(avg_cost)
    plt.show()
    acc = sess.run(accuracy, feed_dict={X:mnist.test.images, Y: mnist.test.labels, keep_prob: 1.0})
    print(acc)


