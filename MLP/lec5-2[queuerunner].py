### queue runner ###
import tensorflow as tf

sess = tf.Session()

# 입력 데이터 텐서 생성 #
myqueue = tf.train.string_input_producer(['d:/data/prac/q_1.txt', 'd:/data/prac/q_2.txt', 'd:/data/prac/q_3.txt'], 
                                         shuffle=False) # 파일을 리스트로 str tensor

reader = tf.TextLineReader() # read
key, value = reader.read(myqueue) # dict 형식 --> value = data
record_default = [[-1], [999]]

# decode #
for i in range(20):
    sp, dist =  tf.decode_csv(value, record_defaults=record_default)

x_batch, y_batch = tf.train.batch([sp, dist], batch_size=4) # batch 생성

coord = tf.train.Coordinator() # thread를 coordinate
threads = tf.train.start_queue_runners(sess=sess, coord=coord) # thread 생성

for i in range(20):
    x, y = sess.run([x_batch, y_batch])
    print(x, y)

coord.request_stop()
coord.join(threads=threads)

sess.close()