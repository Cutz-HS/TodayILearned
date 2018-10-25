import numpy as np
import tensorflow as tf

tf.set_random_seed(777)

data = [[828.659973, 833.450012, 908100, 828.349976, 831.659973],
        [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
        [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
        [816, 820.958984, 1008100, 815.48999, 819.23999],
        [819.359985, 823, 1188100, 818.469971, 818.97998],
        [819, 823, 1198100, 816, 820.450012],
        [811.700012, 815.25, 1098100, 809.780029, 813.669983],
        [809.51001, 816.659973, 1398100, 804.539978, 809.559998]]

def without_norm():
    global data
    data = np.array(data) # (8, 5)
    
    x = data[:,:-1].astype(np.float32) 
    y = data[:, -1].astype(np.float32)
    
    w = tf.Variable(tf.random_uniform([4,1], -1, 1))
    b = tf.Variable(tf.random_uniform([1], -1, 1))
    hypothesis = tf.matmul(x, w) + b
    
    cost = tf.reduce_mean(tf.square(hypothesis - y))
    train = tf.train.GradientDescentOptimizer(learning_rate=0.0000000000006).minimize(cost)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    
    for i in range(400):
        cost_val, _ = sess.run([cost, train])
        if i % 20 == 0:
            print(cost_val)
    sess.close()

def min_max_scaler(data):
    ''' 정규화 '''
    global min_col
    min_col = np.min(data, axis=0)
    max_col = np.max(data, axis=0)
    return np.array(data) - min_col / max_col - min_col
    
def min_max_scaler_byrow(data):
    global min_row
    min_row = np.min(data, axis=1)
    max_row = np.max(data, axis=1)
    return np.array(data).T - min_row / max_row - min_row   
    
    
print(min_max_scaler(data))
print(min_max_scaler_byrow(data))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    