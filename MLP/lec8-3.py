import tensorflow as tf
import pandas as pd
import numpy as np

data = np.loadtxt("d:/data/data.csv", delimiter=",", dtype=np.float32, encoding='utf-8')

xdata=np.transpose(data[0:2])
ydata=np.transpose(data[2:])

global_step = tf.Variable(0, trainable=False, name='global_step')

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_uniform([2, 10], -1., 1.), name='weight1')
b1 = tf.Variable(tf.random_uniform([10], -1., 1.), name='bias1')
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.truncated_normal([10, 20], stddev=0.1), name='weight2')
b2 = tf.Variable(tf.truncated_normal([20]), name='bias2')
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(tf.truncated_normal([20, 3], stddev=0.1), name='weight3')
b3 = tf.Variable(tf.random_normal([3]), name='bias3')
logits = tf.matmul(L2, W3) + b3
hypothesis = tf.nn.softmax(logits)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))
opt = tf.train.AdamOptimizer(learning_rate=0.1)
train = opt.minimize(cost, global_step=global_step)

with tf.Session() as sess:
    saver = tf.train.Saver(tf.global_variables())
    ckpt = tf.train.get_checkpoint_state('d:/data/')
    if ckpt and tf.train.checkpoint_exists(ckpt.model_checkpoint_path):
        saver.restore(sess, ckpt.model_checkpoint_path)
    else:
        sess.run(tf.global_variables_initializer())
    
    