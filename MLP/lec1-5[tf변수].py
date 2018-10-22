### tf 변수 범위 탐색과 변수 공유 ###
import tensorflow as tf

## function ##
def my_network(input1):
    w_1 = tf.Variable(tf.random_uniform([784, 100], -1, 1), name="W_1")
    b_1 = tf.Variable(tf.zeros([100]), name="bias_1")
    output_1 = tf.matmul(input1, w_1) + b_1
    
    w_2 = tf.Variable(tf.random_uniform([100, 50], -1, 1), name="W_2")
    b_2 = tf.Variable(tf.zeros([50]), name="bias_2")
    output_2 = tf.matmul(output_1, w_2) + b_2
    
    w_3 = tf.Variable(tf.random_uniform([50, 10], -1, 1), name="W_3")
    b_3 = tf.Variable(tf.zeros([10]), name="bias_3")
    output_3 = tf.matmul(output_2, w_3) + b_3
    
    print(w_1.name, w_2.name, w_3.name)
    print(b_1.name, b_2.name, b_3.name)
    return output_3

## main ##
i_1 = tf.placeholder(tf.float32, [1000, 784], name="i_1")
#my_network(i_1)
i_2 = tf.placeholder(tf.float32, [1000, 784], name="i_2")
#my_network(i_2) ## 변수 이름이 다르다.

def layer(input2, weight_shape, bias_shape):
    '''
    initializer의 --> weight과 b의 variable 저장
    '''
    weight_init = tf.random_uniform_initializer(minval=-1, maxval=1)
    bias_init =tf.constant_initializer(value=0)
    W = tf.get_variable("W", weight_shape, initializer=weight_init)
    b = tf.get_variable("b", bias_shape, initializer=bias_init)
    return tf.matmul(input2, W) +b

def my_network2(input2):
    with tf.variable_scope("layer_1"):
        output_1 = layer(input2, [784, 100], [100])
    with tf.variable_scope("layer_2"):
        output_2 = layer(output_1, [100, 50], [50])
    with tf.variable_scope("layer_3"):
        output_3 = layer(output_2, [50, 10], [10])
    return output_3
#
#my_network2(i_1)
#my_network2(i_2)
    
with tf.variable_scope("shared_variables") as scope:
    i_1 = tf.placeholder(tf.float32, [1000, 784], name="i_1")
    i_2 = tf.placeholder(tf.float32, [1000, 784], name="i_2")
    my_network2(i_1)
    scope.reuse_variables()
    my_network(i_2)




















