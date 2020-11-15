import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from myFunctions import get_x_train
from myFunctions import get_x_test
from myFunctions import get_y_train
from myFunctions import get_y_test

x_train = np.array(get_x_train())
x_test = np.array(get_x_test())

x_train = x_train / 255
x_test = x_test / 255

y_train = np.array(get_y_train())
y_test = np.array(get_y_test())

y = np.concatenate((y_train, y_test), axis=0)
le = LabelEncoder()
le.fit(y)
y_train = le.transform(y_train)
y_test = le.transform(y_test)

y_train = tf.keras.utils.to_categorical(y_train, 4)
y_test = tf.keras.utils.to_categorical(y_test, 4)

model = tf.keras.Sequential()
#-----------------------------conv block 1-------------------------------------
model.add(tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu', 
          input_shape=(32, 32, 3)))
model.add(tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2,2)))
#-----------------------------conv block 2-------------------------------------
model.add(tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2,2)))
model.add(tf.keras.layers.Dropout(0.25))
#------------------------fully-connected classifier----------------------------
model.add(tf.keras.layers.Flatten())	
model.add(tf.keras.layers.Dense(4096, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(4096, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(4, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', 
              metrics=['accuracy'])
model.summary()

history = model.fit(x_train, y_train, epochs=100, verbose=1, 
          validation_data=(x_test, y_test))
		
score = model.evaluate(x_test, y_test)
print("score =", score)

plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('Accuracy/Loss per Epoch')
plt.ylabel('Value')
plt.xlabel('Epoch')
plt.legend(['accuracy', 'loss'], loc='lower left')
plt.show()