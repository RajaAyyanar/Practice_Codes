#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 12:59:53 2018

@author: raja
"""

import pandas as pd
import numpy as np

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv1D, MaxPooling1D
from keras import backend as K
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import numpy as np
from keras.utils import np_utils


batch_size = 128
num_classes = 6
epochs = 100

df= pd.read_csv("/home/raja/chem/final_data.csv", sep=',',header=None)

y= df[0]
X= df.drop([0], axis=1)

y=np.array(y)
x=np.array(X)

Y=y.copy()
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

y=dummy_y.copy()




from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, shuffle=True) 


print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')


num_classes = 6

x_train = x_train.reshape(x_train.shape[0], 32, 4).astype('float32')
x_test = x_test.reshape(x_test.shape[0], 32, 4).astype('float32') 

model = Sequential()
model.add(Conv1D(filters=12, kernel_size=5, input_shape=(32, 4)))
model.add(MaxPooling1D(pool_size=5 ))
model.add(Dropout(0.25))
model.add(Conv1D(filters=10, kernel_size=3))
model.add(MaxPooling1D(pool_size=2 ))
model.add(Flatten())
model.add(Dense(10, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(10, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(5, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])











