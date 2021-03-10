import numpy as np  
from keras.datasets import mnist
import random
from matplotlib import pyplot as plt
import math

class Img :
    def __init__(self,data=np.array([[]])):
        self.data=data
        self.work=True
        self.x_side=False
        self.y_side=False
    
    @property
    def width(self):
        return np.shape(self.data)[1]
    @property
    def heigth(self):
        return np.shape(self.data)[0]
    
    def downsample(self,data_w,data_h,x_devide,y_devide):
        if self.x_side:
            factor=math.ceil(data_w/x_devide)
            if factor==1:
                factor=2
            self.data=self.data[:,::factor]
        else:
            factor=math.ceil(data_w/(data_w-x_devide))
            if factor==1:
                factor=2
            self.data=self.data[:,::factor]
        if self.y_side:
            factor=math.ceil(data_h/y_devide)
            if factor==1:
                factor=2
            self.data=self.data[::factor,:]
        else:
            factor=math.ceil(data_h/(data_h-y_devide))
            if factor==1:
                factor=2
            self.data=self.data[::factor,:]
    
    def resize(self,x_devide,y_devide,data_w,data_h):
        if(self.x_side and self.y_side):#左上
            padding=np.zeros((self.heigth,data_w-self.width))
            self.data=np.append(self.data,padding,axis=1)
            padding=np.zeros((data_h-self.heigth,self.width))
            self.data=np.append(self.data,padding,axis=0)
        elif(self.x_side and not self.y_side):#左下
            padding=np.zeros((self.heigth,data_w-self.width))
            self.data=np.append(self.data,padding,axis=1)
            padding=np.zeros((data_h-self.heigth,self.width))
            self.data=np.append(padding,self.data,axis=0)
        elif(not self.x_side and self.y_side):#右上
            padding=np.zeros((self.heigth,data_w-self.width))
            self.data=np.append(padding,self.data,axis=1)
            padding=np.zeros((data_h-self.heigth,self.width))
            self.data=np.append(self.data,padding,axis=0)
        else:#右下
            padding=np.zeros((self.heigth,data_w-self.width))
            self.data=np.append(padding,self.data,axis=1)
            padding=np.zeros((data_h-self.heigth,self.width))
            self.data=np.append(padding,self.data,axis=0)
    
  
    
def allocate_side(img1,img2):
    if(x_devide<w_th):
        if(y_devide<h_th or data_h-y_devide<h_th):
            #doesn't work
            img1.work=False
            img2.work=False
        else:
            img1.x_side=False
            img2.x_side=False
            
            img1.y_side=bool(random.getrandbits(1))
            img2.y_side=not img1.y_side
    elif(data_w-x_devide<w_th):
        if(y_devide<h_th or data_h-y_devide<h_th):
            #doesn't work
            img1.work=False
            img2.work=False
        else:
            img1.x_side=True
            img2.x_side=True
            
            img1.y_side=bool(random.getrandbits(1))
            img2.y_side=not img1.y_side
    else:
        if(y_devide<h_th):
            img1.x_side=bool(random.getrandbits(1))
            img2.x_side=not img1.x_side
            
            img1.y_side=False
            img2.y_side=False
            
        elif(data_h-y_devide<h_th):
            img1.x_side=bool(random.getrandbits(1))
            img2.x_side=not img1.x_side
            
            img1.y_side=True
            img2.y_side=True
        else:
            img1.x_side=bool(random.getrandbits(1))
            img2.x_side=not img1.x_side
            
            img1.y_side=bool(random.getrandbits(1))
            img2.y_side=bool(random.getrandbits(1))
      
def merge(img1,img2):
    return Img(img1.data+img2.data)
    




(X_train, y_train), (X_test, y_test) = mnist.load_data()

portion=0.33

data_w=28
data_h=28

w_th=int(data_w*portion)
h_th=int(data_h*portion)

x_devide=random.randint(0,data_w)
y_devide=random.randint(0,data_h)

for i in range(10):
    img1=Img(np.array(X_train[random.randint(0, np.shape(X_train)[0])]))
    img2=Img(np.array(X_train[random.randint(0, np.shape(X_train)[0])]))
    while True:
        allocate_side(img1, img2)
        if img1.work and img2.work:
            break

    img1.downsample(data_w,data_h,x_devide,y_devide)
    img2.downsample(data_w,data_h,x_devide, y_devide)
    img1.resize(x_devide, y_devide, data_w, data_h)
    img2.resize(x_devide, y_devide, data_w, data_h)
    
    new_img=merge(img1,img2)
    plt.imshow(new_img.data)
    plt.show()
    

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        