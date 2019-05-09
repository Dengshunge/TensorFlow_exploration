import os
import shutil
import random

# 整理和复制文件
s1 = '黑牌'
path = r'C:\Users\dengshunge\Desktop\车牌数据集V4\车牌训练集'
rest = r'C:\Users\dengshunge\Desktop\车牌数据集V5\车牌训练集'
path = os.path.join(path, s1)
rest = os.path.join(rest, s1)
if not os.path.exists(path) or not os.path.exists(rest):
    raise Exception("文件夹不存在")

files = []
files = os.listdir(path)
random.shuffle(files)
