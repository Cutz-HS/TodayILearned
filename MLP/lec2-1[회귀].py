### lec 2-1 ###
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(777)
tf.set_random_seed(777)

## building graph ##
td = tf.argmax([[5,1,4],
                [4,5,6]], axis=0)
td2 = tf.argmax([[5,1,4],
                [4,5,6]], axis=1)

def costtoYhat(y, yhat):
    '''
    (yhat - y) 제곱 = cost
    '''
    return tf.reduce_mean(tf.square(yhat - y))

y = np.array([1,2,3], dtype=np.float32)
yhat = np.array([2,4,6], dtype=np.float32)

num_points = 1000
vectors_set = []
for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])

x_data = np.array([x[0] for x in vectors_set]) # 뽑아오기, shape = (1000,)
y_data = np.array([x[1] for x in vectors_set]) # np.array면 훨씬 편하게 가능 --> index

x_data = x_data.reshape(len(x_data), 1)
y_data = y_data.reshape(len(y_data), 1)

X = tf.placeholder(dtype=tf.float32, shape=[None, 1])
y = tf.placeholder(dtype=tf.float32)
W = tf.Variable(tf.random_normal([1, 1]), dtype=tf.float32, name='weight')
b = tf.Variable(tf.random_normal([1]), dtype=tf.float32, name='bias')

hypothesis = W * X + b # W * X + b

cost = tf.reduce_mean(tf.square(hypothesis - y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.3)
train = optimizer.minimize(cost)


sess = tf.Session()
var = tf.global_variables_initializer()
sess.run(var)
costList = []
WList = []

plt.figure()
plt.plot(x_data, y_data, 'rx')
plt.grid(True)
        

for epoch in range(101):
    cost_var, W_var, b_var, y_hat, _ = sess.run([cost, W, b, hypothesis, train], feed_dict={X: x_data, y: y_data})
    costList.append(cost_var)
    WList.append(W_var[0,0])
    if epoch % 10 == 0:
        print(cost_var)
        plt.plot(x_data, y_hat)
        plt.legend(y_hat)
        plt.show()
        

sess.close()


# fit ##
plt.figure('a')
plt.plot(x_data, y_data, 'rx')
plt.grid(True)
plt.plot(x_data, y_hat, 'b-')
plt.title("hypo_fit")
plt.show()

# gradient descent ##
plt.figure('b')
plt.plot(WList, costList, 'y-')
plt.title("cost/W")
plt.show()
















