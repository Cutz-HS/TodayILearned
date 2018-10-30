### mnist ###
import tensorflow as tf
import random
import matplotlib.pyplot as plt
## mnist load ##
from tensorflow.examples.tutorials.mnist import input_data

## random seed ##
random.seed(777)
tf.set_random_seed(777)

#input_data.read_data_sets("d:/data/prac/", one_hot=True)
mnist = input_data.read_data_sets("d:/data/prac/", one_hot=True)


## hyper parameter ##
nb_classes = 10
learning_rate = 0.1
epochs = 15
batch_size = 100 # batch

## tf building ##
X = tf.placeholder(tf.float32, [None, 28*28])
Y = tf.placeholder(tf.float32, [None, nb_classes])

W = tf.Variable(tf.random_normal([28*28, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

predict = tf.cast(tf.argmax(hypothesis, axis=1), dtype=tf.int64)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, axis=1)), dtype=tf.float32))

plt.figure()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(epochs):
        avg_cost = 0
        total_batch = int(mnist.train.num_examples / batch_size) # 550
        for i in range(total_batch): # 550
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            cost_val, _ = sess.run([cost, train], 
                                   feed_dict={X: batch_x, Y: batch_y})
            avg_cost += cost_val / total_batch
        acc, pred = sess.run([accuracy, predict], 
                         feed_dict={X: mnist.test.images, Y: mnist.test.labels})
        plt.plot(epoch, acc, 'r*-')
        print(avg_cost)
    plt.show()
    acc, pred = sess.run([accuracy, predict], 
                         feed_dict={X: mnist.test.images, Y: mnist.test.labels})
    print(acc)
    plt.figure()
    for i in range(5):
        r = random.randint(0, mnist.test.num_examples-1)
        plt.imshow(mnist.test.images[r:r+1].reshape(28,28))
#        print("test: ", sess.run(tf.argmax(mnist.test.labels[r:r+1], axis=1)))
        print("y hat: ", sess.run(tf.argmax(hypothesis, 1), feed_dict={X: mnist.test.images[r:r + 1]}))
    plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
