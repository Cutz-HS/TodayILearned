import tensorflow as tf
import numpy as np

## session ##
a = tf.constant(3)
#sess = tf.Session()
#print(sess.run(a))

#with tf.Session() as sess: # session open
#    print(a.eval())
#    print(a.eval())

#a = tf.constant(5)
#b = tf.constant(5)
#c = tf.multiply(a,b) # multiply 함수
#d = tf.add(a, b)
#e = tf.add(c, d)
sess = tf.Session()
#print(sess.run([c, d, e]))

x = tf.placeholder(dtype=tf.float32, shape=None)
w = tf.Variable(tf.random_normal([3,3]), name='weight')
hypothesis = tf.matmul(x, w)
#y = tf.Variable(hypothesis, dtype=tf.float32)
sess.run(tf.global_variables_initializer())
print(sess.run(hypothesis, feed_dict={x:[[1,2,3]]}))

sess.close()