import matplotlib.pyplot as plt
import tensorflow as tf

tf.set_random_seed(999)

x = [1,2,3]
y = [1,2,3]

w = tf.placeholder(dtype=tf.float32)
hypothesis = x * w

cost = tf.reduce_mean(tf.square(hypothesis - y))
sess = tf.Session()

w_history = []
cost_history = []

for i in range(-40, 61):
    cw = i * 0.1
    cost_val = sess.run([cost], feed_dict={w:cw})
    w_history.append(cw)
    cost_history.append(cost_val)
    
sess.close()

plt.figure
plt.plot(w_history, cost_history, 'r-')
plt.show()
