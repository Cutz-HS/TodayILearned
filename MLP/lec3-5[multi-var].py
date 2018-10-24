import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.preprocessing as pp

def not_used():
    x1 = [1,0,3,0,5]
    x2 = [0,2,0,4,0]
    y = [1,2,3,4,5]
    
    w1 = tf.Variable(tf.random_uniform([1], -1, 1))
    w2 = tf.Variable(tf.random_uniform([1], -1, 1))
    b = tf.Variable(tf.random_uniform([1], -1, 1))
    
    hypothesis = x1 * w1 + x2 * w2 + b
    cost = tf.reduce_mean(tf.square(hypothesis - y))
    train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        for i in range(1000):
            cost_val, _, y_hat = sess.run([cost, train, hypothesis])
            if i % 100 == 0:
                print(i, cost_val)
    print(y_hat)
    
def not_used_2():
    X = [[1.,0.,3.,0.,5.],  # (2 x 5)
         [0.,2.,0.,4.,0.]] 
    y = [1.,2.,3.,4.,5.] # (1 x 5)
    
    W = tf.Variable(tf.random_uniform([1, 2], -1, 1)) # (2 x 1)
    b = tf.Variable(tf.random_uniform([1], -1, 1))
    
    hypothesis = tf.matmul(W, X) + b
    cost = tf.reduce_mean(tf.square(hypothesis - y))
    train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        for i in range(1000):
            cost_val, _, y_hat = sess.run([cost, train, hypothesis])
            if i % 100 == 0:
                print(i, cost_val)
    print(y_hat)
    
def not_used_3():
    X = [[1.,1.,1.,1.,1.],  # (3 x 5)
         [1.,0.,3.,0.,5.],
         [0.,2.,0.,4.,0.]] 
    y = [1.,2.,3.,4.,5.] # (1 x 5)
    
    W = tf.Variable(tf.random_uniform([1, 3], -1, 1)) # (2 x 1)
    b = tf.Variable(tf.random_uniform([1], -1, 1))
    
    hypothesis = tf.matmul(W, X) + b
    cost = tf.reduce_mean(tf.square(hypothesis - y))
    train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        
        for i in range(1000):
            W_val, cost_val, _, y_hat = sess.run([W, cost, train, hypothesis])
            plt.plot(W_val, cost_val, 'rx')
            if i % 100 == 0:
                print(i, cost_val)
    y = np.array(y).reshape(1, 5)
    plt.show()
    print(y_hat)
    
def not_used_4():
    tree = np.loadtxt("d:/data/prac_data/trees.csv", skiprows=1, delimiter=",") # (31, 3)
    x_data = tree[:, :-1].reshape(31, 2)
    y_data = tree[:, -1].reshape(31, 1)
    
    X = tf.placeholder(dtype=tf.float32, shape=[None, 2])
    y = tf.placeholder(dtype=tf.float32, shape=[None, 1])
    
    W = tf.Variable(tf.random_normal([2, 1]))
    b = tf.Variable(tf.random_normal([1]))
    hypothesis = tf.matmul(X, W) + b
    
    cost = tf.reduce_mean(tf.square(hypothesis - y))
    train = tf.train.GradientDescentOptimizer(learning_rate=0.00015).minimize(cost)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(6000):
            _, cost_val, y_hat = sess.run([train, cost, hypothesis],
                                      feed_dict={X: x_data, y: y_data})
            if i % 10 == 0:
                print(cost_val)
        predict = sess.run(hypothesis, feed_dict={X: [[13., 90.]]})
        print(predict)
        
        

    
    return    
    
    
## main ##
if __name__ == "__main__":
    not_used_4()
















