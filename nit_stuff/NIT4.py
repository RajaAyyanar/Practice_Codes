
from sklearn.model_selection import train_test_split
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

batch_size = 128
num_classes = 6
epochs = 2
seed = 7
numpy.random.seed(seed)

dataframe =pandas.read_csv("/home/raja/chem/final_data.csv", sep=',',header=None)
dataset = dataframe.values
X = dataset[:,1:].astype(float)
Y = dataset[:,0]

encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)
number_of_class= 6

x_train, x_test, y_train, y_test = train_test_split(X, dummy_y, test_size=0.3, random_state=0) 

model = Sequential()
model.add(Dense(55, input_dim=128, activation='relu'))
model.add(Dense(32,  activation='relu'))
model.add(Dense(20,  activation='relu'))
model.add(Dense(number_of_class, activation='softmax'))
	# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])



model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
