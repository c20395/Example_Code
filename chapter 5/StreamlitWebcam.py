#Example 5.10
#https://github.com/streamlit/streamlit/issues/511
#pip install --upgrade protobuf
#pip install streamlit

import streamlit as st
import cv2 
import numpy as np

@st.cache(allow_output_mutation=True)
def get_cap():
    return cv2.VideoCapture(0)

cap = get_cap()

frameST = st.empty()
contrast=st.sidebar.slider('Contrast')/50.0
brightness=st.sidebar.slider('Brightness')

while True:
    ret, frame = cap.read()
    #frame = np.clip(contrast * frame + brightness, 0, 255)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #contrast = 1.25
    #brightness = 50
    frame[:,:,2] = np.clip(contrast * frame[:,:,2] + brightness, 0, 255)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    
    # Stop the program if reached end of video
    if not ret:
        print("Done processing !!!")
        cv2.waitKey(3000)
        # Release device
        cap.release()
        break

    frameST.image(frame, channels="BGR")
 
