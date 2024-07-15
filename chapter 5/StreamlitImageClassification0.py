#Example 5.9
#pip install --upgrade protobuf
#pip install streamlit

import streamlit as st
import cv2 
import numpy as np
import pandas as pd
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import time
import matplotlib.pyplot as plt
import random
import os

# import the models for further classification experiments
from tensorflow.keras.applications import vgg16

@st.cache(allow_output_mutation=True)
def vgg16_predict(cam_frame, image_size):
    frame= cv2.resize(cam_frame, (image_size, image_size))
    numpy_image = img_to_array(frame)
    image_batch = np.expand_dims(numpy_image, axis=0)
    # prepare the image for the VGG16 model
    processed_image = vgg16.preprocess_input(image_batch.copy())
    predictions = model.predict(processed_image)
    label_vgg = decode_predictions(predictions)
    cv2.putText(cam_frame, "VGG16: {}, {:.2f}".format(label_vgg[0][0][1], label_vgg[0][0][2]) , (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 1)
    return cam_frame


model = vgg16.VGG16(weights='imagenet')
image_size = 224

frameST = st.empty()
#st.subheader("Image Classification")
st.title("Image Classification")
st.sidebar.markdown("# Image Classification")

file_image = st.sidebar.file_uploader("Upload your Images", type=['jpeg','jpg','png','gif'])
if file_image is None:
    st.write("No image file!")
else:
    img = Image.open(file_image)
    img = np.asarray(img)[:,:,::-1].copy()
    #imcv = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)
    st.write("Image")

    img = vgg16_predict(img, image_size)
    img = img[:,:,::-1]
    st.image(img, use_column_width=True)
    if st.button("Download"):
        im_pil = Image.fromarray(img)
        im_pil.save('output.jpg')
        st.write('Download completed')

