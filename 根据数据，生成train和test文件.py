import os
import shutil
import random

# 形成train和test.txt文件
# 需要更换path和restoreFile
path = r'C:\Users\dengshunge\Desktop\smallData\train_data'
files = ['ao_plate','black_plate','blue_plate','doubleYellow_plate','gang_plate','gua_plate','jiaolian_plate','jing_plate','lingshiguan_plate','newEnergy_plate','nongyong_plate','yellow_plate']
restoreFile = r'C:\Users\dengshunge\Desktop\train.txt'
with open(restoreFile,'w') as f:
    for i in range(len(files)):
        subPath = os.path.join(path, files[i])
        subFiles = []
        subFiles = os.listdir(subPath)
        for s in subFiles:
            f.write(os.path.join(subPath,s)+' '+str(i)+'\n')
