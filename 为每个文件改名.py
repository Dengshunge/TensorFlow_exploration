import os
import shutil
import random

#为每个文件改名
path = r'C:\Users\dengshunge\Desktop\smallData\test_data'
files = ['gua_plate']
for i in range(len(files)):
    subPath = os.path.join(path,files[i])
    subFiles = list(os.listdir(subPath))
    for s in range(len(subFiles)):
        oldname = os.path.join(subPath,subFiles[s])
        newname = subPath+'\\newname2_'+str(s)+'.jpg'
        os.rename(oldname,newname)
