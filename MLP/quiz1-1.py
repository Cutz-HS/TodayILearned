### Q1: a노드를 실행, 결과가 10이 출력 ###
### Q2: z노드 실행, y는 a(3) * b(2) --> 12 출력 ###
import tensorflow as tf

## Q1 ##
a = tf.constant(10, dtype=tf.float32)
sess = tf.Session()
#print(sess.run(a))

## Q2 ##
a = tf.placeholder(dtype=tf.float32)
b = tf.placeholder(dtype=tf.float32)
y = tf.multiply(a, b)
z = tf.add(y, y)
res1 = sess.run(z, feed_dict={a:[3], b:[2]})
#print(res1)

sess.close()