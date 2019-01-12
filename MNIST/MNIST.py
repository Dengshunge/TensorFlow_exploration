# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 21:30:53 2018

@author: Administrator
"""

import tensorflow as tf
import numpy as np
#import readData
from tensorflow.examples.tutorials.mnist import input_data

# 载入数据，并是labels进行one-hot编码
mnist = input_data.read_data_sets('./MNIST_data/',one_hot=True)
# 下面是训练集、测试集和验证集的images和labels
train_images = mnist.train.images
train_labels = mnist.train.labels
test_images = mnist.test.images
test_labels = mnist.test.labels
validation_images = mnist.validation.images
validation_labels = mnist.validation.labels

# 创建一个新的session
sess = tf.InteractiveSession()
# x为images
x =  tf.placeholder(tf.float32,[None,784])
# W为权重
W = tf.Variable(tf.zeros([784,10]))
# b为偏差
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,W)+b)
y_ = tf.placeholder(tf.float32,[None,10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y),reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

tf.global_variables_initializer().run()

for i in range(1000):
    batch_xs,batch_ys = mnist.train.next_batch(100)
    train_step.run({x:batch_xs,y_:batch_ys})
    
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print(accuracy.eval({x:mnist.test.images,y_:mnist.test.labels}))
y_value = y.eval({x:mnist.test.images,y_:mnist.test.labels})
b_value=b.eval()

sess.close()
