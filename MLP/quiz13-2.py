# ANN: 예측 시도 ##
### Q1+: deep learning (logistic) ###

# one-hot #
y_train[y_train=='F'] = 1
y_train[y_train=='M'] = 0
y_test[y_test=='F'] = 1
y_test[y_test=='M'] = 0
y_train = np.array(y_train).reshape(len(y_train), 1)
y_test = np.array(y_test).reshape(len(y_test), 1)
x_train = np.array(x_train)
x_test = np.array(x_test)

# parameter #
learning_rate = 0.005
epochs = 600
keep_prob = tf.placeholder(dtype=tf.float32)
batch_size = 512

## tensorflow building ##
X = tf.placeholder(dtype=tf.float32, shape=[None, 37])  # shape (398, 30)
y = tf.placeholder(dtype=tf.float32, shape=[None, 1]) # shape (398, 1)

# 초기값: he #
init = tf.keras.initializers.he_normal(seed=7)
W1 = tf.Variable(init([37, 50]), name="W1")
b1 = tf.Variable(init([50]), name='b1')
logits = tf.matmul(X, W1) + b1
l1 = tf.nn.relu(logits)
L1 = tf.nn.dropout(l1, keep_prob=keep_prob)

W2 = tf.Variable(init([50, 25]), name="W2")
b2 = tf.Variable(init([25]), name='b2')
logits = tf.matmul(L1, W2) + b2
l2 = tf.nn.relu(logits)
L2 = tf.nn.dropout(l2, keep_prob=keep_prob)

W3 = tf.Variable(init([25, 1]), name="W3")
b3 = tf.Variable(init([1]), name='b3')
logits = tf.matmul(L2, W3) + b3
hypothesis = tf.nn.sigmoid(logits)

# cost #
cost = -tf.reduce_mean(y * tf.log(hypothesis) + (1 - y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

# acc #
predicted = tf.cast(hypothesis > 0.5, tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.float32))

## session ##
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(epochs):
    cost_sum = 0
    total_batch = int(len(x_train) / batch_size) # batch
    train_idx = pd.Series([i for i in range(len(x_train))])
    for j in range(total_batch):
        if j == total_batch-2:
            x_batch, y_batch = x_train[train_idx], y_train[train_idx]
        else:
            idx = np.random.choice(train_idx, size=batch_size)
            x_batch, y_batch = x_train[idx], y_train[idx]
            train_idx = train_idx.drop(idx)
        cost_val, _,= sess.run([cost, train], feed_dict={X: x_batch, y: y_batch, keep_prob: 0.5})
        cost_sum += cost_val
    if i % 200 == 0:
        print(cost_sum)
        
acc, y_hat = sess.run([accuracy, hypothesis], feed_dict={X: x_test, y: y_test, keep_prob: 1.0})
print(acc)

sess.close()






