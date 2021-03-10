import numpy as np  
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten, Conv2D, MaxPool2D
from keras.utils import np_utils  
import os
from matplotlib import pyplot as plt
import pickle
import pandas as pd
import keras
path='mnist_model/'
X_train=np.load('X_train.npy')
y_train=np.load('y_train.npy')
X_test=np.load('X_test.npy')
y_test=np.load('y_test.npy')

y_TrainOneHot = np_utils.to_categorical(y_train) 
y_TestOneHot = np_utils.to_categorical(y_test) 

X_train_2D = X_train.reshape(len(X_train), 28*28).astype('float32')  
X_test_2D = X_test.reshape(len(X_test), 28*28).astype('float32')  

x_Train_norm = X_train_2D/255
x_Test_norm = X_test_2D/255

# model = keras.models.load_model(path+'D1000-D10.h5')
# scores = model.evaluate(x_Test_norm, y_TestOneHot)  
# prediction = model.predict_classes(x_Test_norm)    #官方建議勿用
# d10_confuse=pd.crosstab(y_test, prediction, rownames=['label'], colnames=['predict'])
with open(path+'D1000-0.5d-D1000-0.5d-D10_history.pyc', 'rb') as file_pi:
    history=pickle.load(file_pi)
plt.plot(history['accuracy'])  
plt.plot(history['val_accuracy'])  
plt.title('D1000-0.5d-D1000-0.5d-10D')  
plt.ylabel('acc')  
plt.xlabel('Epoch')  
plt.legend(['train', 'validation'], loc='upper left')  
plt.show()  