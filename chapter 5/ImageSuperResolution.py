#Example 5.13 Image Super Resolution
#Modified from:
#https://www.pyimagesearch.com/2020/11/09/opencv-super-resolution-with-deep-learning/
# pip install opencv-contrib-python
from imutils.video import VideoStream
import imutils
import time
import cv2
import os

modelfile = 'LapSRN_x8.pb'
modelName = modelfile.split(os.path.sep)[-1].split("_")[0].lower()
modelScale = modelfile.split("_x")[-1]
modelScale = int(modelScale[:modelScale.find(".")])

sr = cv2.dnn_superres.DnnSuperResImpl_create()
sr.readModel(modelfile)
sr.setModel(modelName, modelScale)

vs = VideoStream(src=0).start()
time.sleep(2.0)
while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=100)

	upscaled = sr.upsample(frame)
	bicubic = cv2.resize(frame,
		(upscaled.shape[1], upscaled.shape[0]),
		interpolation=cv2.INTER_CUBIC)

	cv2.imshow("Original", frame)
	cv2.imshow("Bicubic", bicubic)
	cv2.imshow("Super Resolution", upscaled)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()
