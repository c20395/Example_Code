# Example 12.3 TPU Test
#import tensorflow and print the version
import tensorflow as tf
print(tf.__version__)

#Display TPU info
resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
tf.config.experimental_connect_to_cluster(resolver)
# This is the TPU initialization code that has to be at the beginning.
tf.tpu.experimental.initialize_tpu_system(resolver)
print("All devices: ", tf.config.list_logical_devices('TPU'))

import time
def current_milli_time():
    return round(time.time() * 1000)

#Test Matrix calculation on TPU
t0 = current_milli_time()
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
with tf.device('/TPU:0'):
  c = tf.matmul(a, b)
print("c device: ", c.device)
print(c)
dt = current_milli_time() - t0
print("TPU time: ",dt)

#Test calculation on CPU
t0 = current_milli_time()
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
with tf.device('/CPU:0'):
  c = tf.matmul(a, b)
print("c device: ", c.device)
print(c)
dt = current_milli_time() - t0
print("CPU time: ",dt)

#Display the CPU GPU TPU information
from tensorflow.python.client import device_lib
device_lib.list_local_devices()
