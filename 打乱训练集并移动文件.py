import os
import shutil
import random

# path是源目录，rest是需要移动到的目录，path->rest
s1 = '新能源'
path = r'C:\Users\dengshunge\Desktop\车牌数据集V4\车牌训练集'
rest = r'C:\Users\dengshunge\Desktop\车牌数据集V4\车牌测试集'
path = os.path.join(path, s1)
rest = os.path.join(rest, s1)

files = []
files = os.listdir(path)
random.shuffle(files)

# range为需要移动的文件数量
for i in range(1100):
    s = os.path.join(path, files[i])
    shutil.move(s, rest)

