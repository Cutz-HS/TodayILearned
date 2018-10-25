### Q1: diabetes logistic ###
### Q2: credit card, without tf ###
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report

tf.set_random_seed(777)
np.random.seed(777)

## 데이터 전처리 ##
all_data = pd.read_csv("d:/data/prac/diabetes.csv", sep=",", header=None)
#np.random.shuffle(all_data)
all_data.boxplot() # boxplot

## learn & test split ##
idx = all_data.index
idx = idx.values
np.random.shuffle(idx) # shuffle index
all_data.index = idx
m = int(len(all_data) * (7 / 10)) # 70% --> 531
# shape (531, 7) , (228, 1)
x_train, x_test = all_data.iloc[:m, :-1], all_data.iloc[m:, :-1]
# shape (531, 1) , (228, 1)
y_train, y_test = all_data.iloc[:m, -1], all_data.iloc[m:, -1]
y_train = np.array(y_train, dtype=np.float32).reshape(len(y_train), 1)
y_test = np.array(y_test, dtype=np.float32).reshape(len(y_test), 1)

## hyper parameter ##
learning_rate = 0.3
epochs = 5000

## tf building ##
X = tf.placeholder(dtype=tf.float32, shape=[None, 8])
y = tf.placeholder(dtype=tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([8, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = tf.nn.sigmoid(tf.matmul(X, W) + b)

# cost #
cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1 - y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 예측 % 정확도 tf building #
predict = tf.cast(hypothesis > 0.7, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y), dtype=tf.float32))

# learning #
for i in range(epochs):
    cost_var, _ = sess.run([cost, train], feed_dict={X: x_train, y: y_train})
    if i % 100 == 0:
        print(cost_var) # 0.48

# predict #
y_hat_train, acc_train, pr_train = sess.run([hypothesis, accuracy, predict], 
                                            feed_dict={X: x_train, y: y_train})
y_hat_test, acc_test, pr_test = sess.run([hypothesis, accuracy, predict], 
                          feed_dict={X: x_test, y:y_test})

print("훈련 정확도: ",acc_train) # 0.7627119 --> 76%
print("검증 정확도: ",acc_test) # 0.78070176 --> 78% -> underfit?

## 최대 정확도 임계치 정하기 ##
for i in list(np.arange(0, 1, 0.1)):
    predict = tf.cast(hypothesis > i, dtype=tf.float32)
    accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, y), dtype=tf.float32))
    acc_test = sess.run([accuracy], feed_dict={X: x_test, y:y_test})
    print("임계치 %.1f" % (i), " / acc: ", acc_test) # 임계치 0.7 --> highest

## Confusion matrix ##
both_test = pd.concat([pd.Series(y_test[:, 0]), pd.Series(y_hat_test[:, 0])], axis=1)
both_test.columns = ["y_test", "probs"]
both_test["y_pred"] = 0
both_test.loc[both_test["probs"] > 0.5, "y_pred"] = 1
print("\n<<Confusion Matrix>>\n\n", pd.crosstab(both_test['y_test'], both_test['y_pred'],
      rownames = ["Actual"], colnames = ["Predicted"]))
print("\n<<Classfication report>>\n\n", classification_report(y_test, pr_test))
 # 0일 때의 f1-score 0.74 // 1일 때의 f1-score 0.83 #
sess.close()


















