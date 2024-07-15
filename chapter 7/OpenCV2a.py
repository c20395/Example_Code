#Example 7.2a
import cv2 
import numpy as np 
  
image = cv2.imread('shapes.jpeg') 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200) 
contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  
print("Number of Contours found = " + str(len(contours))) 
  
# -1 signifies drawing all contours  3: thickness
cv2.drawContours(image, contours, 2, (0, 255, 0), 3)
cv2.imshow('Contours', image) 
cv2.waitKey(0) 
