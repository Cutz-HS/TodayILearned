### Q1: Liniear Regression ###
import tensorflow as tf
import matplotlib.pyplot as plt

tf.set_random_seed(777)

x_data = [1,2,3,4,5]
y_data = [2.1, 3.1, 4.1, 5.3, 6.2]

X = tf.placeholder(dtype=tf.float32, shape=[None])
Y = tf.placeholder(dtype=tf.float32, shape=[None])

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = W * X + b

cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)
cost_list = []
y_hat_list = []
W_list = []

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for i in range(2000):
        cost_val, y_hat, _, W_var = sess.run([cost, hypothesis, train, W],
                                      feed_dict={X: x_data, Y: y_data})
        cost_list.append(cost_val)
        y_hat_list.append(y_hat)
        W_list.append(W_var)
        if i % 100 == 0:
            print(cost_val)
            
    predict = sess.run(hypothesis, feed_dict={X: [10, 9.5]})

print("X = 9.5 --> y_hat :", predict[0])
print("X = 10 --> y_hat :", predict[1])

plt.figure()
plt.plot(x_data, y_data, 'rx')
plt.plot(x_data, y_hat_list[-1], 'b-')
plt.show()

plt.figure()
plt.plot(cost_list, W_list, 'y-')
plt.show()



