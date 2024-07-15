# Example 7.46 depth map using two live webcams
import numpy as np
import cv2
from matplotlib import pyplot as plt

capL = cv2.VideoCapture(0)
capR = cv2.VideoCapture(1)

while capL.isOpened() and capR.isOpened():
    ok, imgL = capL.read()
    if not ok:
        break
    ok, imgR = capR.read()
    if not ok:
        break

    # stereo.compute() requires input images converted to single channel, i.e. of type CV_8UC1
    imgL=cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
imgR=cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    stereo = cv2.cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(imgL,imgR)

    disparity = (disparity - np.amin(disparity))/(np.amax(disparity)-np.amin(disparity))*255
    w,h, = imgR.shape
    img = np.zeros([w,h,3])
    img[:,:,0] = np.ones([w,h])*0/255.0
    img[:,:,1] = np.ones([w,h])*0/255.0
    img[:,:,2] = np.ones([w,h])*disparity/255.0

    cv2.imshow('Depth Map',img)
    key = cv2.waitKey(30)
    if key == 27: # press 'ESC' to quit
        break

capL.release()
capR.release()
cv2.destroyAllWindows()
