import numpy as np  
from keras.datasets import mnist
from matplotlib import pyplot as plt
import os
import cv2
from PIL import Image 
import math

(X_train, y_train), (X_test, y_test) = mnist.load_data()

root_dir="C:/Users/tnt/Desktop/mnist/test"


folder=0
for i in range(10):
    img1=cv2.imread(root_dir+"/"+str(i)+"/"+"1.png",cv2.IMREAD_GRAYSCALE)
    img1=img1.astype(np.int)
    
    j=2
    end=False
    Euclidean=0;
    while(not end):
        img2=cv2.imread(root_dir+"/"+str(i)+"/"+str(j)+".png",cv2.IMREAD_GRAYSCALE)
        
        if(img2 is None):
            end=True
        else:
            img2=img2.astype(np.int)
            Euclidean+=math.sqrt(np.sum(np.square((img1-img2))))
            j+=1
            
    print("folder"+str(i))
    print(str(int(Euclidean)/(j-2)))