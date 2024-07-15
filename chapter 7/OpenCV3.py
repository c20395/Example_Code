#Example 7.3 Color Detection
import cv2
import numpy as np

def callback(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('HSV Color')

# create trackbars for HSV color
cv2.createTrackbar('H0','HSV Color',0,179,callback)
cv2.createTrackbar('H1','HSV Color',179,179,callback)

cv2.createTrackbar('S0','HSV Color',0,255,callback)
cv2.createTrackbar('S1','HSV Color',255,255,callback)

cv2.createTrackbar('V0','HSV Color',0,255,callback)
cv2.createTrackbar('V1','HSV Color',255,255,callback)

import urllib.request as urllib
#get image by url
#resp = urllib.urlopen("https://opencv-python-tutroals.readthedocs.io/en/latest/_images/water_coins.jpg")
resp = urllib.urlopen("https://images.wisegeek.com/skin-mole.jpg")
#resp = urllib.urlopen("http://www.anti-aging-skin-care-illusions.com/images/Dry-Skin.jpg")
#resp = urllib.urlopen("https://jooinn.com/images/human-skin-4.jpg")

image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)


while(1):
    ret, frame = cap.read()
    #frame = image.copy()
    h0 = cv2.getTrackbarPos('H0', 'HSV Color')
    h1 = cv2.getTrackbarPos('H1', 'HSV Color')
    s0 = cv2.getTrackbarPos('S0', 'HSV Color')
    s1 = cv2.getTrackbarPos('S1', 'HSV Color')
    v0 = cv2.getTrackbarPos('V0', 'HSV Color')
    v1 = cv2.getTrackbarPos('V1', 'HSV Color')
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV', hsv)
    lower = np.array([h0, s0, v0])
    higher = np.array([h1, s1, v1])
    mask = cv2.inRange(hsv, lower, higher)
    frame = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('frame', frame)

    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cv2.destroyAllWindows()
cap.release()
