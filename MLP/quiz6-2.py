### Q2 ###
import tensorflow as tf
import pandas as pd
import numpy as np
import sklearn.preprocessing as pp
from sklearn.model_selection import train_test_split

tf.set_random_seed(777)

## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/agaricus-lepiota.data.txt", sep=",", header=None)
X_data = all_data.iloc[:, 1:] # shape(8124, 22)
y_data = all_data.iloc[:, [0]] # shape(8124, 1)

# 숫자 변환 #
def number(v):
    return ord(v) #글자 -> 숫자 변환

def preprocess_x_data(df):
    for c in df.columns[0:]:
        #print(c)
        df[c] = df[c].apply(number) # 열적용 
        
preprocess_x_data(X_data)  # 수 변환
y_data[y_data=='p'] = 1 # 독이 있으면 1, 없으면 0으로 변환
y_data[y_data=='e'] = 0

# 표준화 scaling #
sc = pp.StandardScaler()
X_scale = sc.fit_transform(X_data)

# train, test split #
x_train, x_test, y_train, y_test = train_test_split(X_scale, y_data, train_size=0.7, random_state=77)

# hyper parameter #
learning_rate = 0.01
epochs = 4000

## tf buliding ## --> binary logistic
X = tf.placeholder(dtype=tf.float32, shape=[None, 22])
y = tf.placeholder(dtype=tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([22, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = tf.nn.sigmoid(tf.matmul(X, W) + b)

cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1 - y) * (tf.log(1 - hypothesis)))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

predict = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y), dtype=tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 학습 #
for i in range(epochs):
    cost_val, _ = sess.run([cost, train], feed_dict={X: x_train, y: y_train})
    if i % 100 == 0:
        print(cost_val)

## 예측 ##
predicted_train, acc_train, y_hat_train = sess.run([predict, accuracy, hypothesis], 
                                 feed_dict={X: x_train, y: y_train})
predicted, acc, y_hat = sess.run([predict, accuracy, hypothesis], 
                                 feed_dict={X: x_test, y: y_test})
        
# 최적 임계치 찾기 #
for i in list(np.arange(0, 1, 0.1)):
    predict = tf.cast(hypothesis > i, dtype=tf.float32)
    accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y), dtype=tf.float32))
    acc_test = sess.run([accuracy], feed_dict={X: x_test, y:y_test})
    print("임계치 %.1f" % (i), " / acc: ", acc_test) # 0.3 ~ 0.7 거의 비슷

print("learning_rate: ", learning_rate, "\nlearn: ", epochs, "\ncost: %0.3f" %cost_val)
print("훈련 정확도: ", acc_train)
print("검증 정확도: ", acc)

sess.close()
