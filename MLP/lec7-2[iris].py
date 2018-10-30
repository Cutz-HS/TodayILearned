import pandas as pd
import csv
import tensorflow as tf
import numpy as np

### preprocessing ###
data = pd.read_csv("d:/data/prac/iris.csv", sep=",", index_col=0)

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# one-hot #
y_onehot = pd.get_dummies(y)

# open #
read = open("d:/data/prac/iris.csv", "r", encoding='utf-8')
csvread = csv.reader(read)
#for row in csvread:
#    print(row)

index = ['setosa', 'versicolor', 'virginica']

x_data = []
ydata = []
next(csvread)
for row in csvread:
    data = []
    sepal_length = float(row[1])
    sepal_width = float(row[2])
    petal_length = float(row[3])
    petal_width = float(row[4])
    data = [sepal_length, sepal_width, petal_length, petal_width]
    x_data.append(data)
    for i in range(3):
        if row[5] == index[i]:
            ydata.append([i])

X = tf.placeholder(tf.float32, shape=[None, 4])
y = tf.placeholder(tf.int32, shape=[None, 1])
y_one_hot = tf.one_hot(y, 3)
Y_one_hot = tf.reshape(y_one_hot, [-1, 3]) # None이 아닌 -1

W = tf.Variable(tf.random_normal([4,10]))
b = tf.Variable(tf.random_normal([10]))
logits = tf.matmul(X, W) + b

W2 = tf.Variable(tf.random_normal([10, 10]))
b2 = tf.Variable(tf.random_normal([10]))
logits2 = tf.matmul(logits, W2) + b2

W3 = tf.Variable(tf.random_normal([10, 3]))
b3 = tf.Variable(tf.random_normal([3]))
logits3 = tf.matmul(logits2, W3) + b3
hypothesis = tf.nn.softmax(logits3)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y_one_hot, logits=logits3))
train = tf.train.AdamOptimizer(learning_rate=0.3).minimize(cost)

predict = tf.cast(tf.argmax(hypothesis, axis=1), dtype=tf.int64)
# equal -> (pred, y_one_hot)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict, tf.argmax(Y_one_hot, axis=1)), dtype=tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(3000):
    cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, y: ydata})
    if i % 100 == 0:
        print(cost_val)
pred = sess.run(predict, feed_dict={X: x_data})
acc = sess.run(accuracy, feed_dict={X: x_data, y: ydata})
print(acc)

for p, y in zip(pred, np.array(ydata).flatten()):
    print("{} prediction: {} True Y: {}".format(p==y, p, y))

sess.close()


















