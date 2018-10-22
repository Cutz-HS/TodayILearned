import tensorflow as tf

#x = tf.linspace(-1.0, 1.0, 10)
#sess = tf.Session()
#print(sess.run(x))
#sess.close()

a = tf.placeholder("float")
b = tf.placeholder("float")
y = tf.multiply(a, b)
z = tf.add(y, y)
#with tf.Session() as sess:
#    print(sess.run(z, feed_dict={a:4, b:4}))
    
#x = tf.constant([[1.0, 2.0, 3.0]]) # 1행 3열
#W = tf.constant([[2.0], [2.0], [2.0]])

input_data = [[1.0, 2.0, 3.0],
              [1.0, 2.0, 3.0],
              [2.0, 3.0, 4.0]]

x = tf.placeholder(dtype=tf.float32, shape=[None,3])
W = tf.Variable(tf.random_normal(shape=[3, 3]), dtype=tf.float32) # 3개
hypothesis = tf.matmul(x, W)

with tf.Session() as sess:
    init = sess.run(tf.global_variables_initializer())
    val = sess.run(hypothesis, feed_dict={x: input_data})
    print(init)
