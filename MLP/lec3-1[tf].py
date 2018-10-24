import tensorflow as tf

#a = tf.placeholder(tf.int32)
#b = tf.placeholder(tf.int32)
#add = tf.add(a, b)

a = tf.Variable(3)
b = tf.Variable(4)
add = tf.add(a, b)


## a에 3, b에 4를 전달하여 출력 ##
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(add))
    
    
def show99(dan):
    x = tf.placeholder(dtype=tf.int32)
    W = tf.placeholder(dtype=tf.int32)
    res = x * W
    sess = tf.Session()
    for i in range(1, 10):
        x_val, W_val, res_val = sess.run([x, W, res], feed_dict={x: dan, W: i})
        print(x_val, " x ", W_val, " = ", res_val)
    sess.close()
    
    
show99(5)