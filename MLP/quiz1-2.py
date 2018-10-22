### Q3: 그림보고 tf 설계 ###
import tensorflow as tf

input_data = [1,2,3,4,5]

x = tf.placeholder(dtype=tf.float32, shape=None)
w = tf.Variable(tf.constant(2, dtype=tf.float32, shape=None))
y = tf.multiply(w, x)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
res = sess.run(y, feed_dict={x:input_data})
print(res)