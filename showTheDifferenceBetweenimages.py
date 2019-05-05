# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:59:19 2019

@author: dengshunge
"""

"""
用于显示图像的小命令，可以根据需求进行复制
"""

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import h5py

lena = mpimg.imread(r'C:/Users/dengshunge/Desktop/fgvc-aircraft-2013b/fgvc-aircraft-2013b/data/images/1514522.jpg')

plt.figure()
plt.imshow(lena) # 显示图片

test_data = h5py.File(r'C:\Users\dengshunge\Desktop\源码\BCNN-86.4%-飞机\Bilinear-CNN-TensorFlow-master\Bilinear-CNN-TensorFlow-master\utils\new_test_224.h5', 'r')
X_test, Y_test = test_data['X'], test_data['Y']

plt.figure()
plt.imshow(X_test[0]/255)


