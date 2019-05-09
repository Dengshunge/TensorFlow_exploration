# 创建HMF5文件
from tflearn.data_utils import build_hdf5_image_dataset
# 各文件目录
new_train = r"C:\Users\dengshunge\Desktop\train.txt"
new_val = "../train_test/cub200/validation.txt"
new_test = r"C:\Users\dengshunge\Desktop\test.txt"

# 注意更改image_shape，output_path为生成文件的位置
build_hdf5_image_dataset(new_val, image_shape=(200, 200), mode='file', output_path='new_val.h5', categorical_labels=True, normalize=False)
print ("Done creating new_val.h5")
build_hdf5_image_dataset(new_test, image_shape=(30, 120), mode='file', output_path='new_test.h5', categorical_labels=True, normalize=False)
print ('Done creating new_test.h5')
build_hdf5_image_dataset(new_train, image_shape=(30, 120), mode='file', output_path='new_train.h5', categorical_labels=True, normalize=False)
print ('Done creating new_train.h5')
