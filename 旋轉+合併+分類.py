import numpy as np  
from keras.datasets import mnist
from matplotlib import pyplot as plt
import os
# import cv2
# from PIL import Image 
import random
import keras
import scipy



root_dir="C:/Users/tnt/Desktop/mnist/combine/"
try:
    os.makedirs(root_dir)
except OSError :
    pass

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# new_data=np.empty(shape=(0,28,28))

# i=0
# j=1
# while(i<len(y_test)):
#     img1=scipy.ndimage.rotate(X_test[i],random.randint(-180,180),reshape=False)
#     img2=scipy.ndimage.rotate(X_test[i+1],random.randint(-180,180),reshape=False)
#     img3=scipy.ndimage.rotate(X_test[i+2],random.randint(-180,180),reshape=False)
#     img4=scipy.ndimage.rotate(X_test[i+3],random.randint(-180,180),reshape=False)
#     new_data=np.append(new_data,img1.reshape(1,28,28),axis=0)
#     new_data=np.append(new_data,img2.reshape(1,28,28),axis=0)
#     new_data=np.append(new_data,img3.reshape(1,28,28),axis=0)
#     new_data=np.append(new_data,img4.reshape(1,28,28),axis=0)
    
#     up=np.append(img1,img2,axis=1)
#     down=np.append(img3,img4,axis=1)
#     final=np.append(up,down,axis=0)
    
#     final=final[:,::2]
#     final=final[::2,:]
    
#     name=str(j)+'-'+str(y_test[i])+str(y_test[i+1])+str(y_test[i+2])+str(y_test[i+3])
#     cv2.imwrite(root_dir+name+".png",final)
    
#     i+=4
#     j+=1
    

# new_data_2D = new_data.reshape(new_data.shape[0], 28*28).astype('float32')  
# new_data_norm = new_data_2D/255
model = keras.models.load_model('C:/Users/tnt/Desktop/mnist_model/1d_model.h5')
# prediction=model.predict_classes(new_data_norm)
# correct_list=np.array([])
# i=0
# while(i<len(y_test)):
#     correct=0
#     if(prediction[i] == y_test[i] and prediction[i+1] == y_test[i+1] and prediction[i+2]==y_test[i+2] and prediction[i+3] == y_test[i+3]):
#         correct=1
#     correct_list=np.append(correct_list,correct)
#     i+=4
    
# correct_list=np.reshape(correct_list,(-1,1))
# prediction=np.reshape(prediction,(-1,4))
# result=np.append(correct_list,prediction,axis=1)

# print (result)