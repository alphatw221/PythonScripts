import numpy as np  
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense
from keras.utils import np_utils  # 用來後續將 label 標籤轉為 one-hot-encoding  
import random
import os
import scipy

# 載入 MNIST 資料庫的訓練資料，並自動分為『訓練組』及『測試組』
(X_train, y_train), (X_test, y_test) = mnist.load_data()


# new_list_x=[]
# new_list_y=[]

# for i in range(len(y_train)):
#     new_list_x.append(X_train[i])
#     img1=scipy.ndimage.rotate(X_train[i],random.randint(-180,180),reshape=False)
#     new_list_x.append(img1)
#     new_list_y.append(y_train[i])
#     new_list_y.append(y_train[i])
    
# new_data_x=np.array(new_list_x).reshape(-1,28,28)
# new_data_y=np.array(new_list_y)

# np.save('X_train',new_data_x)
# np.save('y_train',new_data_y)

new_list_x=[]
new_list_y=[]
for i in range(len(y_test)):
    img1=scipy.ndimage.rotate(X_test[i],random.randint(-180,180),reshape=False)
    new_list_x.append(img1)
    new_list_y.append(y_test[i])
    
new_data_x=np.array(new_list_x).reshape(-1,28,28)
new_data_y=np.array(new_list_y)

np.save('X_test',new_data_x)
np.save('y_test',new_data_y)