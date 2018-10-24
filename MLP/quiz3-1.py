### Q1: 점수 예측: tensorflow ###
### Q2: Tree volume 예측: without tf ###
### Q3: Alphabet 주가 예측 ###
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.preprocessing as pp

tf.set_random_seed(777)
np.random.seed(777)

### Q1 ###
## 데이터 전처리 ##
xy = np.loadtxt("d:/data/prac_data/test-score.csv", delimiter=",", dtype=np.float32)

xdata = xy[:, :-1] # shape(25,3)
ydata = xy[:, -1].reshape(len(xy), 1) # shape(25,1)

xtest = [[100, 70, 102],
         [60, 70, 100],
         [80, 90, 95]]

## hyper parameter ##
learning_rate = 0.00005
iteration = 10000

## tf building ##
X = tf.placeholder(dtype=tf.float32, shape=[None, 3])
y = tf.placeholder(dtype=tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([3, 1], name='weight'))
b = tf.Variable(tf.random_normal([1], name='bias'))
hypothesis = tf.matmul(X, W) + b

# cost #
cost = tf.reduce_mean(tf.square(hypothesis - y))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

## learning ##
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(iteration):
        _, cost_val = sess.run([train, cost], feed_dict={X: xdata, y: ydata})
#        if i % 100 == 0:
#            print(cost_val) # 8.58
    ## 예측 ##
    predict = sess.run(hypothesis, feed_dict={X: xtest})
    print("learning_rate: ", learning_rate, "\nlearn: ", iteration, "\ncost: ", cost_val)
    print("3명의 점수, predict :", predict[0], predict[1], predict[2])
        

### Q2 ###
## 데이터 전처리 ##
tree = np.loadtxt("d:/data/prac_data/trees.csv", skiprows=1, delimiter=",") # (31, 3)
x_data = tree[:, :-1].reshape(31, 2) # shape(31, 2)
y_data = tree[:, -1].reshape(31, 1) # shape(31, 1)
X = np.insert(x_data, 0, 1, axis=1) # 경사도 하강 행렬 계산을 위해 0열에 x0 추가 (value = 1) (31, 3)

## 식 building ##
m = len(x_data) # 데이터의 개수
initialW = np.random.normal(size=(3, 1)) # b포함

## hyper parameter ##
learning_rate = 0.0003
iteration = 6000 

def hypothesis(W, X):
    '''
    가설 함수
    '''
    global m
    return np.dot(X, W)

def cost(X, W, y):
    '''
    cost 함수
    '''
    global m
    return float(1 / (2 * m) * np.sum(np.square(hypothesis(W, X) - y)))

def gradientDescent(X, W, y):
    '''
    descent
    '''
    global m, learning_rate
    for i in range(iteration):
        w_tmp = W.copy()
        cost_val = cost(X, W, y)
#        if i % 200 == 0:
#            print(cost_val)
        for j in range(len(w_tmp)): # w의 j만큼 각각 학습
            # gradient descent 학습 --> 미분
            w_tmp[j] = W[j] - (learning_rate / m) * np.sum((hypothesis(W, X) - y) * X[:, j].reshape(m, 1))
        W = w_tmp.copy()
    return W, cost_val

## 실행 ##
W_new, cost_val = gradientDescent(X, initialW, y_data)
print("learning_rate: ", learning_rate, "\nlearn: ", iteration, "\ncost: ", cost_val)
## 예측 ##
predict = hypothesis(W_new, [[1, 13, 90]])
print("x = [13, 90]일 때, predict: ", predict[0, 0])


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
