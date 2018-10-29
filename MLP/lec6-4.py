import numpy as np

np.random.seed(777)


x_data = [[1, 2, 1, 1], # shape (8, 5)
          [2, 1, 3, 2],
          [3, 1, 3, 4],
          [4, 1, 5, 5],
          [1, 7, 5, 5],
          [1, 2, 5, 6],
          [1, 6, 6, 6],
          [1, 7, 7, 7]]
y_data = [[0, 0, 1],#2 # shape (8, 3)
          [0, 0, 1],#2
          [0, 0, 1],#2
          [0, 1, 0],#1
          [0, 1, 0],#1
          [0, 1, 0],#1
          [1, 0, 0],#0
          [1, 0, 0]]#0
x_test = [[1, 1, 11, 7, 9], # shape (3, 5)
          [1, 1, 3, 4, 3],
          [1, 1, 1, 0, 1]]

# 데이터 전처리 #
x_data = np.array(x_data)
y_data = np.array(y_data)
x_test = np.array(x_test)
x_data = np.insert(x_data, 0, 1, axis=1)

## hyper parameter ##
learning_rate = 0.1
epochs = 2001
m = x_data.shape[0]
init_W = np.random.normal(size=[5, 3])

def logits(W, X):
    return np.matmul(X, W)

def sigmoid(W, X):
    return 1. / (1 + np.exp(-logits(W, X)))

def softmax(y):
    y = -np.log(1./y - 1)
    return np.exp(y) / (np.sum(np.exp(y), axis=1)).reshape(len(y), 1)

def hypothesis(W, X):
    return softmax(sigmoid(W, X))

def cost(W, X, y):
    global m
    return np.mean(np.sum(y * -np.log(hypothesis(W, X)), axis=1))

def gradientDescent(X, W, y):
    global m, learning_rate
    m = len(X)
    costList = []
    wList = []
    w_tmp = W.copy()
    for i in range(epochs):
        cost_tmp = cost(W, X, y)
        costList.append(cost_tmp)
        if i % 100 == 0:
            print(cost_tmp)
        wList.append(W)
        for j in range(0, len(w_tmp)): # feature(W)의 개수 + 1 (bias)
            w_tmp[j] = W[j] - ((learning_rate / m) * (np.sum((hypothesis(W, X) - y) * X[:, [j]], axis=0)))
        W = w_tmp.copy()
    return W, costList

W, costList = gradientDescent(x_data, init_W, y_data)
yhat = hypothesis(W, x_data)

def predict(X, W, y):
    y_hat = hypothesis(W, X)
    y_hat_arg = np.argmax(y_hat, axis=1)
    equal = np.equal(y_hat_arg, np.argmax(y, axis=1))
    return y_hat_arg, len(equal[equal==True]) / len(y)

y_hat, acc = predict(x_data, W, y_data)
predicted = np.argmax(hypothesis(W, x_test), axis=1)

#import tensorflow as tf
#
## tf building #
#X = tf.placeholder(dtype=tf.float32, shape=[None, 4])
#Y = tf.placeholder(dtype=tf.float32, shape=[None, 3])
#
#W1 = tf.Variable(tf.random_normal([4, 3]), name='weight')
#b = tf.Variable(tf.random_normal([3]), name='bias')
#logit = tf.matmul(X, W1) + b
#hypothesis1 = tf.nn.softmax(logit)
#
#cost1 = tf.reduce_mean(tf.reduce_sum(Y * -tf.log(hypothesis1), axis=1))
#train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost1)
#
#sess = tf.Session()
#sess.run(tf.global_variables_initializer())
#
#
#for i in range(epochs):
#    wval, y_hat, cost_val, _ = sess.run([W1, hypothesis1, cost1, train], feed_dict={X: x_data[:, 1:], Y: y_data})
#    if i % 100 == 0:
#        print(cost_val)
#
#sess.close()
#







