# Example 12.1 GPUTest.py
# Check TensorFlow with GPU
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

# Check Keras with GPU
from keras import backend as K
print(K.tensorflow_backend._get_available_gpus())

#Check PyTorch with GPU
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name())
