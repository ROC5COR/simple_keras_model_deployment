from keras.models import Sequential
from keras.layers import Dense
import numpy as np

X = np.array([[1,2,3],[2,2,3],[-2,-3,-4],[4,4,2],[-1,0,0],[3,5,6],[4,2,0]])

y = np.array([[1],[1],[0],[0],[1],[1],[0]])

model = Sequential()
model.add(Dense(32, input_shape=(3,)))
model.add(Dense(32))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
model.fit(X,y, validation_data=(X,y), epochs=1000)

model.save('vector_direction.h5')

