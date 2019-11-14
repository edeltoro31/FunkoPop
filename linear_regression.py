import tensorflow as tf 
import csv
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = tf.placeholder(tf.float32, shape=[None])
y = tf.placeholder(tf.float32, shape=[None])
w = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

H = x * w + b

cost = tf.reduce_mean(tf.square(H - y))

opt = tf.train.GradientDescentOptimizer(learning_rate=0.00000008731)
train = opt.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

with open('own.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	x_axis = []
	y_axis = []
	for row in csv_reader:
		x_axis.append(float(row[0]))
		y_axis.append(float(row[1]))



for step in range(2000):
	_, v1, v2 = sess.run([train, w, b], feed_dict={x: x_axis, y: y_axis})
	print(v1, v2)


print(w)
print(b)