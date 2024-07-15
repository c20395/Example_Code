#Example 7.5 YOLOv3 Detection
import numpy as np
import argparse
import cv2 as cv
import subprocess
import time
import os
from yolo_utils import infer_image, show_image
from types import SimpleNamespace

d = {'confidence':0.5,
     'threshold':0.3,
     'weights':'./yolov3-coco/yolov4-tiny.weights',
     'config':'./yolov3-coco/yolov4-tiny.cfg',
     'show_time':True}
FLAGS = SimpleNamespace(**d)
cocolabels='./yolov3-coco/coco-labels'
labels = open(cocolabels).read().strip().split('\n')
print(FLAGS)


colors = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')
net = cv.dnn.readNetFromDarknet(FLAGS.config, FLAGS.weights)

layer_names = net.getLayerNames()
layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


vfile="../../../Programming/PythonMachineLearning/ObjectDetection/Vehicle Detection/vehicle-detection-master/examples/PedalPostIncident20200821.mp4"      
vfile=0
vid = cv.VideoCapture(vfile)

while True:
    _, frame = vid.read()
    #frame = cv.resize(frame, (640,360), interpolation = cv.INTER_AREA)
    height, width = frame.shape[:2]
    frame, boxes, confidences, classids, idxs = infer_image(net, layer_names, \
			height, width, frame, colors, labels, FLAGS)
    cv.imshow('webcam', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv.destroyAllWindows()
