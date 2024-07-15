#Example 5.11 Image Stitching  
import numpy as np
import cv2 as cv
import sys
 
modes = (cv.Stitcher_PANORAMA, cv.Stitcher_SCANS)
names=['London_left.jpg','London_right.jpg']
imgs = []
for img_name in names:
    img = cv.imread(cv.samples.findFile(img_name))
    cv.imshow(img_name,img)
    if img is None:
        print("can't read image " + img_name)
        sys.exit(-1)
    imgs.append(img)

stitcher = cv.Stitcher.create(modes[0])
status, pano = stitcher.stitch(imgs)

if status != cv.Stitcher_OK:
    print("Can't stitch images, error code = %d" % status)
    sys.exit(-1)

cv.imwrite('result.jpg', pano)
cv.imshow('result', pano)
