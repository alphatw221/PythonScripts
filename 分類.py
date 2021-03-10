import numpy as np  
from keras.datasets import mnist
from matplotlib import pyplot as plt
import os
import cv2
from PIL import Image 

(X_train, y_train), (X_test, y_test) = mnist.load_data()

root_dir="C:/Users/tnt/Desktop/mnist"

for i in range(10):
    try:
        os.makedirs(root_dir+"/train/"+str(i))
    except OSError :
        pass
    try:
        os.makedirs(root_dir+"/test/"+str(i))
    except OSError :
        pass

name=[1,1,1,1,1,1,1,1,1,1]

for i in range(len(y_train)):
    # np_img=X_train[i]
    # img=Image.fromarray(np_img)
    # img.save(root_dir+"/train/"+str(y_train[i])+"/"+str(name[int(y_train[i])])+".png")
    cv2.imwrite(root_dir+"/train/"+str(y_train[i])+"/"+str(name[int(y_train[i])])+".png",X_train[i])
    name[int(y_train[i])]+=1
    
name=[1,1,1,1,1,1,1,1,1,1]


for i in range(len(y_test)):
    # np_img=X_test[i]
    # img=Image.fromarray(np_img)
    # img.save(root_dir+"/test/"+str(y_test[i])+"/"+str(name[int(y_test[i])])+".png")
    # name[int(y_train[i])]+=1
    cv2.imwrite(root_dir+"/test/"+str(y_test[i])+"/"+str(name[int(y_test[i])])+".png",X_test[i])
    name[int(y_test[i])]+=1