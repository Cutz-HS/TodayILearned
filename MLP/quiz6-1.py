### Q1: xdata, ydata without tf ###
### Q2: 독버섯 데이터 ###
### Q3: wine 데이터 ###
import numpy as np

### Q1 ###
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
init_W = np.random.normal(size=[5, 3]) # shape([5(feature), 3(class)])

## 함수 buliding ##
def logits(W, X):
    # 행렬 곱 --> Wx + b #
    return np.matmul(X, W)

def sigmoid(W, X):
    # 하나의 class 마다 sigmoid #
    return 1. / (1 + np.exp(-logits(W, X)))

def softmax(y):
    # 각각의 sigmoid 확률을 -L 로 만들어 준 뒤, softmax [0, 1]로 #
    y = -np.log((1. / y) - 1)
    return np.exp(y) / (np.sum(np.exp(y), axis=1)).reshape(len(y), 1)

def hypothesis(W, X):
    # 가설 함수: sigmoid -> -ln(1/p -1) -> softmax #
    return softmax(sigmoid(W, X))

def cost(W, X, y):
    # cost --> -ln(h(x)) 그래프 #
    global m
    return np.mean(np.sum(y * -np.log(hypothesis(W, X)), axis=1))

def gradientDescent(X, W, y):
    # softmax의 cost함수의 편미분의 식도 linear, sigmoid와 같다 #
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

## 학습 ##
W, costList = gradientDescent(x_data, init_W, y_data)
yhat = hypothesis(W, x_data)

## 예측 ##
def predict(X, W, y):
    # argmax를 이용한 예측 #
    y_hat = hypothesis(W, X)
    y_hat_arg = np.argmax(y_hat, axis=1)
    equal = np.equal(y_hat_arg, np.argmax(y, axis=1))
    return y_hat_arg, len(equal[equal==True]) / len(y)

y_hat, acc = predict(x_data, W, y_data)
predicted = np.argmax(hypothesis(W, x_test), axis=1)
print("learning_rate: ", learning_rate, "\nlearn: ", epochs, "\ncost: %0.3f" %costList[-1])
print("정확도: ", acc, "\n x_test데이터의 예측결과: ", predicted)








