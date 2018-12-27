# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:07:09 2018

@author: Deng Shunge
@reference:https://blog.csdn.net/shwan_ma/article/details/77603311
"""

import numpy as np
import struct

def readLabels(path):
    with open(path,'rb') as f:
        data = f.read()
    offset = 0#设置偏移量offset
    numberOfItems = struct.unpack_from('>II',data,offset)[1]#读取先两个字节的内容，并支取第二个数据
    offset += struct.calcsize('>II')#重新计算偏移量，跳到第三个字节处
    Labels = np.zeros((numberOfItems))#创建一个大小的numberOfItems的列向量，用于返回标签值
    
    #循环读取内容，幅值给Labels
    for i in range(numberOfItems):
        Labels[i] = np.array(struct.unpack_from('>B',data,offset))
        offset += struct.calcsize('>B')#读取完后都需要加上一个字节的偏移量
        
    return Labels

def readImages(path):
    with open(path,'rb') as f:
        data = f.read()
    offset = 0
    magic,numberOfImages,rows,columns = struct.unpack_from('>IIII',data,offset)
    offset += struct.calcsize('>IIII')
    Images = np.empty((numberOfImages,rows,columns))
    image_size = rows*columns
    fmt = '>'+str(image_size)+'B'#这里变量用于控制每次读取的字节数和offset的偏移量
    
    for i in range(numberOfImages):
        Images[i] = np.array(struct.unpack_from(fmt,data,offset)).reshape((rows,columns))
        offset += struct.calcsize(fmt)
    
    return Images

def input_data(path):
    train_Images = readImages(path+r'\train-images.idx3-ubyte')
    train_Labels = readLabels(path+r'\train-labels.idx1-ubyte')
    test_Images = readImages(path+r'\t10k-images.idx3-ubyte')
    test_Labels = readLabels(path+r'\t10k-labels.idx1-ubyte')
    return train_Images,train_Labels,test_Images,test_Labels
    
if __name__=="__main__":
    #传入文件夹
    train_Images,train_Labels,test_Images,test_Labels=input_data(r'.\MNIST_DataSet')
