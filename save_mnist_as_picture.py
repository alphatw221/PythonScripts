import numpy as np  
from keras.datasets import mnist
from matplotlib import pyplot as plt
import os
import cv2
from PIL import Image 

(X_train, y_train), (X_test, y_test) = mnist.load_data()

    
root_dir="C:/Users/tnt/Desktop/mnist"
x_train_path=root_dir+"/x_train/"
y_train_path=root_dir+"/y_train/"
x_test_path=root_dir+"/x_test/"
y_test_path=root_dir+"/y_test/"


try:
    os.mkdir(root_dir)
except OSError :
    pass

try:
    os.mkdir(x_train_path)
except OSError :
    pass

for i in range(len(y_train)):    
    np_image=X_train[i]
    img=Image.fromarray(np_image)
    img.save(x_train_path+str(i)+".png")
    
try:
    os.mkdir(x_test_path)
except OSError :
    pass

for i in range(len(y_test)):    
    np_image=X_test[i]
    img=Image.fromarray(np_image)
    img.save(x_test_path+str(i)+".png")