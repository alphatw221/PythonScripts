import numpy as np  
from keras.datasets import mnist
from matplotlib import pyplot as plt
import os
import cv2
from PIL import Image 
import random


root_dir="C:/Users/tnt/Desktop/mnist/combine/"
try:
    os.makedirs(root_dir)
except OSError :
    pass

(X_train, y_train), (X_test, y_test) = mnist.load_data()


i=0
j=1
while(i<len(y_train)):
    img1=X_train[i]
    img2=X_train[i+1]
    img3=X_train[i+2]
    img4=X_train[i+3]
    up=np.append(img1,img2,axis=0)
    down=np.append(img3,img4,axis=0)
    final=np.append(up,down,axis=1)
    
    final=final[:,::2]
    final=final[::2,:]
    
    cv2.imwrite(root_dir+str(j)+".png",final)
    
    i+=4
    j+=1
    