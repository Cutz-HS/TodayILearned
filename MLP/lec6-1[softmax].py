import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

## 데이터 전처리 ##
all_data = np.loadtxt("d:/data/prac/softmax.txt", delimiter=" ")

X_data = all_data[:, :-3] # shape(8, 3)
Y_data = all_data[:, -3:] # shape(8, 3)

## hyper parameter ##
learning_rate = 0.1
epochs = 1500

## tf buliding ##
X = tf.placeholder(dtype=tf.float32, shape=[None, 3])
Y = tf.placeholder(dtype=tf.float32, shape=[None, 3])

W = tf.Variable(tf.random_normal([3, 3]), name='weight') # b 추가되어 있다.
logit = tf.matmul(X, W)
hypothesis = tf.nn.softmax(logit) # softmax hypothesis

cost = tf.reduce_sum(Y * -tf.log(hypothesis), axis=1) # softmax cost
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

# predict & acc #
predict = tf.cast(tf.argmax(hypothesis, axis=1), dtype=tf.int32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y, axis=1, output_type=tf.int32)), dtype=tf.float32))

# train #
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(epochs):
    _, cost_val = sess.run([train, cost], feed_dict={X: X_data, Y: Y_data})
    if i % 50 == 0:
        print(cost_val)
        
y_hat, predicted, acc = sess.run([hypothesis, predict, accuracy], feed_dict={X: X_data, Y: Y_data})
print(acc)
grades = np.array(['A', 'B', 'C'])
print(grades[predicted])

sess.close()