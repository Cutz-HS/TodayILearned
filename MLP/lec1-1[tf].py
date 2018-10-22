### tensorflow ###
import tensorflow as tf
import numpy as np
import pandas as pd

## tf test ##
test = [[1,2,3],
        [4,5,6],
        [7,8,9]]

sess = tf.Session()
x = tf.constant(test, dtype=tf.float32, shape=None)
W = tf.constant([2], dtype=tf.float32, shape=[1], name='weight')
y = tf.Variable(x * W, name='y')
#function = tf.global_variables_initializer()
#sess.run(function)

#print(sess.run(y))
#sess.close()

## tf practice ##
hello = tf.constant('hello')
#print(sess.run(hello))
#print(str(sess.run(hello), encoding='utf-8'))

a = tf.constant(5, dtype=tf.float32)
b = tf.constant(10, dtype=tf.float32)
c = tf.constant(2, dtype=tf.float32)
d = tf.Variable(a * b + c, dtype=tf.float32)
#d = a * b + c # tf.nod --> multi + add
fun = tf.global_variables_initializer()
sess.run(fun)

#print(sess.run(d))
sess.close()