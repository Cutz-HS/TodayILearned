### CPU&GPU 관리 ###
import tensorflow as tf

a = tf.constant(1, dtype=tf.float32)
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
#print(sess.run(a))

with tf.device('/gpu:2'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0], shape=[2,2], name='a')
    b = tf.constant([1.0, 2.0], shape=[2, 1], name='b')
    c = tf.matmul(a, b)
    
sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))
#print(sess.run(c))