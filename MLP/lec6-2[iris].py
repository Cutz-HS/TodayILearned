import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

tf.set_random_seed(777)
np.random.seed(777)


## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/iris_softmax.csv", sep=",", header=None)
X_data = all_data.iloc[:, :-3] # shape (150, 5)
Y_data = all_data.iloc[:, -3:] # shape (150, 3)

## train-test split ##
def split(data, percent):
    num = int(percent * len(data))
    data = np.array(data)
    np.random.shuffle(data)
    return data[:num, :], data[num:, :]

x_train, x_test = split(X_data, 0.7)
y_train, y_test = split(Y_data, 0.7)

## hyper parameter ##
learning_rate = 0.1
epochs = 1500
m = X_data.shape[0]
init_W = np.random.normal(size=[5, 3])

def sigmoid(z):
    return 1. / (1. + np.exp(-z))

def hypothesis(W, X):
    return softmax(sigmoid(np.matmul(X, W)))

def softmax(y):
    return np.exp(y) / (np.sum(np.exp(y), axis=1).reshape(len(y), 1))

def cost(W, X, y):
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
            w_tmp[j] = W[j] - (learning_rate / m) * np.sum((hypothesis(W, X) - y) * X[:, j].reshape(m, 1), axis=0)
        W = w_tmp.copy()
    return wList, costList

wList, costList = gradientDescent(x_train, init_W, y_train)

#def predict(X, W, y):
    
    

























