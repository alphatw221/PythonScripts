import numpy as np  
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten, Conv2D, MaxPool2D
from keras.utils import np_utils  
import os
from matplotlib import pyplot as plt
import pickle
import pandas as pd


X_train=np.load('X_train.npy')
y_train=np.load('y_train.npy')
X_test=np.load('X_test.npy')
y_test=np.load('y_test.npy')


model = Sequential()
model.add(Conv2D(filters=32, kernel_size=3, input_shape=(1, 28, 28), activation='relu', padding='same'))
model.add(MaxPool2D(pool_size=2, data_format='channels_first'))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 


y_TrainOneHot = np_utils.to_categorical(y_train) 
y_TestOneHot = np_utils.to_categorical(y_test) 

X_train_3D = X_train.reshape(len(X_train),1,28,28).astype('float32')  
X_test_3D = X_test.reshape(len(X_test),1,28,28).astype('float32')  

x_Train_norm = X_train_3D/255
x_Test_norm = X_test_3D/255

train_history = model.fit(x=x_Train_norm, y=y_TrainOneHot, validation_split=0.2, epochs=10, batch_size=800, verbose=2)  
model.summary()

plt.plot(train_history.history['accuracy'])  
plt.plot(train_history.history['val_accuracy'])  
plt.title('C32-D256-D10')  
plt.ylabel('acc')  
plt.xlabel('Epoch')  
plt.legend(['train', 'validation'], loc='upper left')  
plt.show()  

scores = model.evaluate(x_Test_norm, y_TestOneHot)  
prediction = model.predict_classes(x_Test_norm)    #官方建議誤用
#Please use instead:* `np.argmax(model.predict(x), axis=-1)`,   if your model does multi-class classification  
# (e.g. if it uses a `softmax` last-layer activation).* `(model.predict(x) > 0.5).astype("int32")`, 
# if your model does binary classification   (e.g. if it uses a `sigmoid` last-layer activation).
obj=pd.crosstab(y_test, prediction, rownames=['label'], colnames=['predict'])


path='mnist_model/'
try:
    os.mkdir(path)
except OSError :
    pass
model.save(path+'C32-D256-D10')

with open(path+'C32-D256-D10.pyc', 'wb') as file_pi:
    pickle.dump(train_history.history, file_pi)