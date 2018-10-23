import tensorflow as tf

tf.set_random_seed(777)

x_train = [1,2,3]
y_train = [1,2,3]

X = tf.placeholder(dtype=tf.float32)
Y = tf.placeholder(dtype=tf.float32)

W = tf.Variable(tf.random_normal([1]), dtype=tf.float32, name='weight')
b = tf.Variable(tf.random_normal([1]), dtype=tf.float32, name='bias')

hypothesis = W * X + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(2000):
    cost_val, W_val, b_val, y_hat, _ = sess.run([cost, W, b, hypothesis, train],
                                                feed_dict={X: x_train, Y: y_train})
    if i % 20 == 0:
        print (i, cost_val, W_val, b_val, y_hat)

