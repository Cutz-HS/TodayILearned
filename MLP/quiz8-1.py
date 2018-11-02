### Q1: mnist deep learning ###
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import random
import matplotlib.pyplot as plt

tf.set_random_seed(777)
np.random.seed(777)

## hyper parameter ##
learning_rate = 0.01
training_epochs = 15
batch_size = 100
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

## tf building ##
X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, 10])

# W&b --> layer 4 // 초기화: he #
init = tf.keras.initializers.he_normal()
W1 = tf.Variable(init([784, 512]))
b1 = tf.Variable(init([512]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(init([512, 256]))
b2 = tf.Variable(init([256]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(init([256, 128]))
b3 = tf.Variable(init([128]))
L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)

W4 = tf.Variable(init([128, 10]))
b4 = tf.Variable(init([10]))
hypothesis = tf.matmul(L3, W4) + b4

# cost/loss opt #
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# acc #
predict = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

## training ##
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)
    
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        cost_val, _ = sess.run([cost, train],
                        feed_dict = {X: batch_xs, Y: batch_ys})
        avg_cost += cost_val / total_batch
    
    print('cost =', '{:.12f}'.format(avg_cost))

# accruacy #
for i in range(10):
    r = random.randint(0, mnist.test.num_examples - 1)
    print("Label: ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
    print("Prediction: ", sess.run(tf.argmax(hypothesis, 1), feed_dict={X: mnist.test.images[r:r + 1]}))

print("learning_rate: ", learning_rate, "\nlearn: ", training_epochs, "\ncost: %0.3f" %cost_val)
print("검증 정확도: ", sess.run(accuracy, feed_dict={X:mnist.test.images, Y: mnist.test.labels}))

sess.close()