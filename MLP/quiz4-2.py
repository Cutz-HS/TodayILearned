import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

### Q2 ###
## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/creditcard.csv", sep=",")
print(all_data.head(5)) # shape (284807, 31)

X = all_data.iloc[:, 1:-2] # Time, Amount 변수 제거
y = all_data.iloc[:, [-1]]
y = np.array(y)
X = np.insert(np.array(X), 0, 1, axis=1)

## 학습&검증 데이터 split ##
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=77)
sample_X_train = X_train[:1500, :] # 샘플 데이터로 미니 학습
sample_y_train = y_train[:1500, :]
sample_X_test = X_test[:1500, :]
sample_y_test = y_test[:1500, :]

## hyper parameter ##
learning_rate = 0.1
epochs = 4000

## function ##
def sigmoid(z):
    return (1. / (1 + np.exp(-z)))

def hypothesis(W, X):
    ''' 
    가설 함수 
    '''
    return sigmoid(np.dot(X, W))

def cost(W, X, y): 
    global m
    ''' 
    cost 
    '''
    m = y.size
    term1 = np.dot(- np.array(y).T, np.log(hypothesis(W, X))) # y = 1
    term2 = np.dot((1 - np.array(y)).T, np.log(1 - hypothesis(W, X))) # y = 0
    return float((1./m) * (np.sum(term1 - term2)))

def gradientDescent(W, X, y):
    global m, iteration, learning_rate
    costList = []
    wList = []
    w_tmp = W.copy()
    for i in range(epochs):
        cost_tmp = cost(W, X, y)
        costList.append(cost_tmp)
        if i % 50 == 0:
            print(cost_tmp)
        wList.append(W)
        for j in range(0, len(w_tmp)): # feature(W)의 개수 + 1 (bias)
            w_tmp[j] = W[j] - (learning_rate / m) * np.sum((hypothesis(W, X) - y).T * X[:, j].reshape(m, 1))
        W = w_tmp.copy()
    return W, costList

initial_W = np.zeros(shape=[X.shape[1], 1]) # (29, 1)
W, mincost = gradientDescent(initial_W, sample_X_train, sample_y_train)
y_hat = hypothesis(W, sample_X_test)

## 정확도 검증 ##
def accuracy(y, y_hat):
    '''
    정확도 검증을 위한 함수
    '''
    cr_val = 0.5 # 임계치
    y_hat[y_hat > 0.5] = 1
    y_hat[y_hat <= 0.5] = 0
    predicted = np.equal(sample_y_test, y_hat)
    return len(predicted[predicted == True]) / len(sample_y_test) # 전체에서 True 정확도 (Acc)

print(accuracy(y, y_hat))


## tf로 나머지 처리 ##
# sample 학습으로 learning_rate, learning ==> 0.1, 4000 확인 #
# 학습 데이터: (199364, ), 검증 데이터: (85443, )
import tensorflow as tf
from sklearn.metrics import classification_report

## 전처리 ##
X_train, X_test = X_train[:, 1:], X_test[:, 1:] # X0항 제거

## tf buliding ##
X = tf.placeholder(dtype=tf.float32, shape=[None, 28])
y = tf.placeholder(dtype=tf.float32, shape=[None, 1])

W = tf.Variable(tf.zeros([28, 1]), name="weight") # 랜덤일 때 NaN 발생
b = tf.Variable(tf.zeros([1]), name='bias')
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

cost = tf.reduce_mean(-y * tf.log(hypothesis) - (1 - y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

# 예측 % 정확도 tf building #
predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(epochs):
        cost_val, _ = sess.run([cost, train], feed_dict={X: X_train, y: y_train})
        if i % 400 == 0:
            print(cost_val)
    
    # predict #
    y_hat_test, acc_test, pr_test = sess.run([hypothesis, accuracy, predict], 
                          feed_dict={X: X_test, y:y_test})

print("검증 정확도: ", acc_test)

## Confusion matrix ##
both_test = pd.concat([pd.Series(y_test[:, 0]), pd.Series(y_hat_test[:, 0])], axis=1)
both_test.columns = ["y_test", "probs"]
both_test["y_pred"] = 0
both_test.loc[both_test["probs"] > 0.5, "y_pred"] = 1
print("\n<<Confusion Matrix>>\n\n", pd.crosstab(both_test['y_test'], both_test['y_pred'],
      rownames = ["Actual"], colnames = ["Predicted"]))
print("\n<<Classfication report>>\n\n", classification_report(y_test, pr_test))













