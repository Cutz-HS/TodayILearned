import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
#from tensorflow.python.client import device_lib

np.random.seed(777)
tf.set_random_seed(777)

mnist = input_data.read_data_sets('d:/data/', one_hot=True)

## parameter ##
num_filters1 = 32
x = tf.placeholder(tf.float32, [None, 784]) # 28*28*1
x_image = tf.reshape(x, [-1, 28, 28, 1]) # [None, 28, 28, 1]
w_conv1 = tf.Variable(tf.random_normal([5, 5, 1, num_filters1]))

# 필터에 이미지 적용 #
h_conv1 = tf.nn.conv2d(x_image, w_conv1, strides=[1,1,1,1], padding="SAME") ## stride 행렬 생성
## padding --> shape이 감소하는 상황을 padding을 통해 원복 ##
# bias #
b_conv1 = tf.Variable(tf.constant(0.1, shape=[num_filters1]))

# 활성화 함수 # (CNN - ReLU 함수)
h_conv1_cutoff = tf.nn.relu(h_conv1 + b_conv1)

# POOLing # : max filter (2x2)
h_pool1 = tf.nn.max_pool(h_conv1_cutoff, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")

## 2nd convolutionary layer ##
num_filters2 = num_filters1 * 2
w_conv2 = tf.Variable(tf.random_normal([5, 5, num_filters1, num_filters2]))
h_conv2 = tf.nn.conv2d(h_pool1, w_conv2, strides=[1,1,1,1], padding="SAME")
b_conv2 = tf.Variable(tf.constant(0.1, shape=[num_filters2]))
h_conv2_cutoff = tf.nn.relu(h_conv2 + b_conv2)
h_pool2 = tf.nn.max_pool(h_conv2_cutoff, ksize=[1,2,2,1], strides=[1,2,2,1], padding="SAME")

## fully-connected ## 64 --> 10
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*num_filters2]) # flatten
num_units1 = 7*7*num_filters2
num_units2 = 1024

w2 = tf.Variable(tf.random_normal([num_units1, num_units2]))
b2 = tf.Variable(tf.random_normal([num_units2]))
logits = tf.matmul(h_pool2_flat, w2) + b2
layer1 = tf.nn.relu(logits)

# drop-out #
keep_prob = tf.placeholder(tf.float32)
L1 = tf.nn.dropout(layer1, keep_prob=keep_prob)

# 최종 matmul #
w0 = tf.Variable(tf.zeros([num_units2, 10]))
b0 = tf.Variable(tf.zeros([10]))
logits2 = tf.matmul(L1, w0) + b0
hypothesis = tf.nn.softmax(logits2)

## cost ##
t = tf.placeholder(tf.float32, [None, 10])
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits2, labels=t))
opt = tf.train.AdamOptimizer(learning_rate=0.0001)
train = opt.minimize(cost)

## acc ##
predict = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(t, axis=1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

## learning ##
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(10000):
    batch_x, batch_y = mnist.train.next_batch(50)
    cost_val, _ =  sess.run([cost, train], feed_dict={x: batch_x, t: batch_y, keep_prob:0.5})
    if i % 500 == 0:
        print("cost: ", cost_val)
        loss_list, acc_list = [], []
        for c in range(4): # 중간과정에서 test
            start = int(len(mnist.test.labels)/4 * c)
            end = int(len(mnist.test.labels)/4 * (c+1))
            loss_val, acc_vals = sess.run([cost, accuracy], feed_dict={x: mnist.test.images[start:end], t:mnist.test.labels[start:end], keep_prob:1.0})
            loss_list.append(loss_val)
            acc_list.append(acc_vals)

            loss_val = np.sum(loss_list)
            acc_vals = np.mean(acc_list)

            print(loss_val, acc_vals)


sess.close()