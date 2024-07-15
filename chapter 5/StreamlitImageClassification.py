#Example 5.9a
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
# imports for reproducibility
from keras import backend as K

# import the models for further classification experiments
from tensorflow.keras.applications import (
        vgg16,
        resnet50,
        mobilenet,
        inception_v3
    )

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

@st.cache(allow_output_mutation=True)
def resnet50_predict(cam_frame, image_size):
    frame= cv2.resize(cam_frame, (image_size, image_size))
    numpy_image = img_to_array(frame)
    image_batch = np.expand_dims(numpy_image, axis=0)  
    # prepare the image for the ResNet50 model
    processed_image = resnet50.preprocess_input(image_batch.copy())
    predictions = model.predict(processed_image)
    label_resnet = decode_predictions(predictions, top=3)
    cv2.putText(cam_frame, "ResNet50: {}, {:.2f}".format(label_resnet[0][0][1], label_resnet[0][0][2]) , (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 1)
    return cam_frame    

@st.cache(allow_output_mutation=True)
def mobilenet_predict(cam_frame, image_size):
    frame= cv2.resize(cam_frame, (image_size, image_size))
    numpy_image = img_to_array(frame)
    image_batch = np.expand_dims(numpy_image, axis=0)
    # prepare the image for the MobileNet model
    processed_image = mobilenet.preprocess_input(image_batch.copy())
    predictions = model.predict(processed_image)
    label_mobilenet = decode_predictions(predictions)
    cv2.putText(cam_frame, "MobileNet: {}, {:.2f}".format(label_mobilenet[0][0][1], label_mobilenet[0][0][2]) , (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 1)
    return cam_frame    
    
@st.cache(allow_output_mutation=True)
def inception_v3_predict(cam_frame, image_size):
    frame= cv2.resize(cam_frame, (image_size, image_size))
    numpy_image = img_to_array(frame)
    image_batch = np.expand_dims(numpy_image, axis=0)
    # prepare the image for the Inception model
    processed_image = inception_v3.preprocess_input(image_batch.copy())
    predictions = model.predict(processed_image)
    label_inception = decode_predictions(predictions)
    cv2.putText(cam_frame, "Inception: {}, {:.2f}".format(label_inception[0][0][1], label_inception[0][0][2]) , (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 1)
    return cam_frame    



mode = 1
#model = vgg16.VGG16(weights='imagenet')
#image_size = 224

frameST = st.empty()
#st.subheader("Image Classification")
st.title("Image Classification")
st.sidebar.markdown("# Image Classification")
option = st.sidebar.selectbox(
     'Select a Deep Learning Model:',
     ["VGG16","RESNET50","MOBILENET","INCEPTION_V3"], index=0)
st.sidebar.write('You selected:', option)
if option == "VGG16":
    K.clear_session()
    model = vgg16.VGG16(weights='imagenet')
    image_size = 224
    mode = 1
elif option == "RESNET50":
    K.clear_session()
    model = resnet50.ResNet50(weights='imagenet')
    image_size = 224
    mode = 2
elif option == "MOBILENET":
    K.clear_session()
    model = mobilenet.MobileNet(weights='imagenet')
    image_size = 224
    mode = 3
    
elif option == "INCEPTION_V3":
    K.clear_session()
    model = inception_v3.InceptionV3(weights='imagenet')
    image_size = 299
    mode = 4



file_image = st.sidebar.file_uploader("Upload your Images", type=['jpeg','jpg','png','gif'])

if file_image is None:
    st.write("No image file!")

else:
    img = Image.open(file_image)
    img = np.asarray(img)[:,:,::-1].copy()
    #imcv = cv2.cvtColor(np.asarray(im), cv2.COLOR_RGB2BGR)
    st.write("Image")

    if mode == 1:
        img = vgg16_predict(img, image_size)
    elif mode == 2:
        img = resnet50_predict(img, image_size)
    elif mode == 3:
        img = mobilenet_predict(img, image_size)
    elif mode == 4:
        img = inception_v3_predict(img, image_size)

    img = img[:,:,::-1]
    st.image(img, use_column_width=True)
    if st.button("Download"):
        im_pil = Image.fromarray(img)
        im_pil.save('output.jpg')
        st.write('Download completed')

