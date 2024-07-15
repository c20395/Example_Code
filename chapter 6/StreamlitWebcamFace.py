#Example 6.19 Face Detection in webcam - web app with Streamlit
#pip install --upgrade protobuf
#pip install streamlit

import streamlit as st
import cv2 

cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


@st.cache(allow_output_mutation=True)
def get_cap():
    #from webcam
#    return cv2.VideoCapture(0)
    #from a video file
    return cv2.VideoCapture('Roller Coaster.mp4')

cap = get_cap()

frameST = st.empty()
st.title("Face Detection")
st.text("Built with Streamlit and OpenCV")

scale=st.sidebar.slider('Scale Factor:', 1.0, 2.0, 1.3)
mn=st.sidebar.slider('minNeighbors:', 5, 20, 5)
msize=st.sidebar.slider('minSize:', 10, 200, 30)

while True:
ret, frame = cap.read()
    # Stop the program if reached end of video
    if not ret:
        cv2.waitKey(3000)
        cap.release()
        break

    gray_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= cascade_classifier.detectMultiScale(gray_img,
                                               scaleFactor=scale,
                                               minNeighbors=mn,      
                                               minSize=(msize, msize)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(frame,'face', (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2)


    frameST.image(frame, channels="BGR")
