import numpy as np  
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense
from keras.utils import np_utils  # 用來後續將 label 標籤轉為 one-hot-encoding  

# 載入 MNIST 資料庫的訓練資料，並自動分為『訓練組』及『測試組』
(X_train, y_train), (X_test, y_test) = mnist.load_data()


new_X_train=np.empty((len(X_train),28,28),dtype=np.uint8)
new_y_train=np.empty((len(y_train)),dtype=np.uint8)
j=0
for i in range(len(y_train)):
    if(y_train[i]<5):
        new_X_train[j]=X_train[i]
        new_y_train[j]=y_train[i]
        j+=1
new_X_train=np.resize(new_X_train,(j,28,28))
new_y_train=np.resize(new_y_train,(j))


new_X_test=np.empty((len(X_test),28,28),dtype=np.uint8)
new_y_test=np.empty((len(y_test)),dtype=np.uint8)
j=0
for i in range(len(y_test)):
    if(y_test[i]<5):
        new_X_test[j]=X_test[i]
        new_y_test[j]=y_test[i]
        j+=1
new_X_test=np.resize(new_X_test,(j,28,28))
new_y_test=np.resize(new_y_test,(j))

y_TrainOneHot = np_utils.to_categorical(new_y_train) 
y_TestOneHot = np_utils.to_categorical(new_y_test) 

X_train_2D = new_X_train.reshape(-1, 28*28).astype('float32')  
X_test_2D = new_X_test.reshape(-1, 28*28).astype('float32')  

x_Train_norm = X_train_2D/255
x_Test_norm = X_test_2D/255


model = Sequential()
model.add(Dense(units=5, kernel_initializer='normal', activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 

train_history = model.fit(x=x_Train_norm, y=y_TrainOneHot, validation_split=0.2, epochs=10, batch_size=800, verbose=2)  

scores = model.evaluate(x_Test_norm, y_TestOneHot)  
print()  
print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0))  

X = x_Test_norm[0:10,:]
predictions = model.predict_classes(X)
# get prediction result
print(predictions)

