import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

tf.set_random_seed(777)

x_data = [1,2,3]
y_data = [1,2,3]
m = len(x_data)
w = tf.Variable(tf.random_normal([1]))
x = tf.placeholder(dtype=tf.float32)
y = tf.placeholder(dtype=tf.float32)
hypothesis = x * w
learning_rate = 0.01
cost = tf.reduce_mean(tf.square(hypothesis-y))
grad = tf.reduce_mean((hypothesis - y) * x)
descent = w - learning_rate * grad
update = w.assign(descent)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

costList, wList = [], []
y_hat_list = []
plt.figure()

for i in range(1000):
    w_new, _, y_hat, cost_val = sess.run([descent, update, hypothesis, cost], feed_dict={x: x_data, y: y_data})
    costList.append(cost_val)
    wList.append(w_new[0])
    if i % 100 == 0:
        y_hat_list.append(y_hat)

plt.plot(wList, costList, 'r-')
#for i in y_hat_list:
#    plt.plot(x_data, i, '-')
plt.ylim(np.min(costList), np.max(costList))
plt.xlim(np.min(wList), np.max(wList))
plt.show()

sess.close()