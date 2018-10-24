import tensorflow as tf

w = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)

x = tf.placeholder(dtype=tf.float32)
y = tf.placeholder(dtype=tf.float32)

hypothesis = tf.multiply(x, w) + b
loss = tf.reduce_sum(tf.square(hypothesis - y))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

x_train = [1,2,3,4]
y_train = [0,-1,-2,-3]

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    _, w_val, b_val, loss_val = sess.run([train, w, b, loss], feed_dict={x: x_train, y: y_train})
    if i % 100 == 0:
        print(i, loss_val)
    
print(w_val, b_val, loss_val)