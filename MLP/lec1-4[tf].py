import tensorflow as tf

input1 = tf.constant([3.0], dtype=tf.float32)
input2 = tf.constant([2.0], dtype=tf.float32)
input3 = tf.constant([5.0], dtype=tf.float32)
inter = tf.add(input2, input3)
mul = tf.multiply(input1, inter)
with tf.Session() as sess:
    res, inter_res = sess.run([mul, inter])
    print(res, inter_res)