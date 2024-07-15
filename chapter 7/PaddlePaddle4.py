# Example 7.42 PaddlePaddle background removal
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import animation
import cv2
import paddlehub as hub
from PIL import Image, ImageSequence
from IPython.display import display, HTML
import numpy as np
import imageio
import os

# 1. Define the input and output image folder
test_path = 'imgs/'
output_path = 'humanseg_output/'
# Get all the input images
test_img_path = ['01.jpg', '02.jpg']
test_img_path = [test_path + img for img in test_img_path]
# Display the first image
img = mpimg.imread(test_img_path[0])
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis('off')
plt.show()
#2. Get the Deep Learning model
# PaddleHub DeepLabv3+(deeplabv3p_xception65_humanseg)
module = hub.Module(name="deeplabv3p_xception65_humanseg")
input_dict = {"image": test_img_path}
# execute predict and print the result
results = module.segmentation(data=input_dict, visualization=True, output_dir=output_path)for result in results:
    print(result)
    out_img_path = result['save_path']
    img = mpimg.imread(out_img_path)
    plt.figure(figsize=(10,10))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
