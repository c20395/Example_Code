# Example 12.2 GPUTest2.py
#import tensorflow and print the version
import tensorflow as tf
print(tf.__version__)

#Display GPU info
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

import time
def current_milli_time():
    return round(time.time() * 1000)

#Test MNIST data on GPU
t0 = current_milli_time()
mnist=tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test/255.0
with tf.device('/GPU:0'):
  model=tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28,28)),
      tf.keras.layers.Dense(512, activation=tf.nn.relu),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10, activation=tf.nn.softmax)
  ]) 
  model.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy')
  #             metices=['accuracy'])
  model.fit(x_train, y_train, epochs=5)
  model.evaluate(x_test, y_test)
  dt = current_milli_time() - t0
  print("time: ",dt)

#Test MNIST data on CPU
t0 = current_milli_time()
with tf.device('/CPU:0'):
  model=tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(28,28)),
      tf.keras.layers.Dense(512, activation=tf.nn.relu),
      tf.keras.layers.Dropout(0.2),
      tf.keras.layers.Dense(10, activation=tf.nn.softmax)
  ]) 
  model.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy')
  model.fit(x_train, y_train, epochs=5)
  model.evaluate(x_test, y_test)
  dt = current_milli_time() - t0
  print("time: ",dt)

from tensorflow.python.client import device_lib
device_lib.list_local_devices()
