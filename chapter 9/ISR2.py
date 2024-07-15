#Example 9.2 ISR webcam
#https://github.com/idealo/image-super-resolution
#pip install ISR

import numpy as np
from PIL import Image
from imutils.video import VideoStream
import cv2
import imutils

#pip install 'h5py<3.0.0'
#pip install h5py==2.10.0
#import h5py
#h5py.run_tests()

from ISR.models import RDN

#rdn = RDN(weights='psnr-small')
#rdn = RDN(weights='psnr-large')
rdn = RDN(weights='noise-cancel')


vs = VideoStream(src=0).start()
while True:
    frame = vs.read()
    #frame = imutils.resize(frame, width=50)
    lr_img = np.array(frame)
    sr_img = rdn.predict(lr_img)
    #sr_img =Image.fromarray(sr_img)

    cv2.imshow("Original", frame)
    cv2.imshow("ISR", sr_img)
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
