#Example 7.10
#Modified based on:
#https://machinelearningmastery.com/how-to-perform-object-detection-in-photographs-with-mask-r-cnn-in-keras/
# example of inference with a pre-trained coco model
# Does work on TensorFlow 1.13 15/10/2020  (Very Slow)

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from mrcnn.config import Config
from mrcnn.model import MaskRCNN
from mrcnn import model as modellib
from mrcnn import visualize

from matplotlib import pyplot
from matplotlib.patches import Rectangle
import cv2
import numpy as np
import imutils
import colorsys
import random
import os

# load the class label names from disk, one label per line
#The content does not seem to be correct
#CCLASS_NAMES = open('coco_labels.txt').read().strip().split("\n")

CLASS_NAMES = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
               'bus', 'train', 'truck', 'boat', 'traffic light',
               'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
               'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
               'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
               'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
               'kite', 'baseball bat', 'baseball glove', 'skateboard',
               'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
               'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
               'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
               'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
               'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
               'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
               'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
               'teddy bear', 'hair drier', 'toothbrush']
#
# generate random (but visually distinct) colors for each class label
# (thanks to Matterport Mask R-CNN for the method!)
hsv = [(i / len(CLASS_NAMES), 1, 1.0) for i in range(len(CLASS_NAMES))]
COLORS = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
random.seed(42)
random.shuffle(COLORS)




# define the test configuration
class TestConfig(Config):
     NAME = "test"
     GPU_COUNT = 1
     IMAGES_PER_GPU = 1
     NUM_CLASSES = 1 + 80

# define the model
rcnn = MaskRCNN(mode='inference', model_dir='./', config=TestConfig())
# load coco model weights
rcnn.load_weights('mask_rcnn_coco.h5', by_name=True)

# Read video
cap = cv2.VideoCapture(0)
vf='./Vehicle Detection/vehicle-detection-master/examples/PedalPostIncident20200821.mp4'
#cap = cv2.VideoCapture(vf)
#while cap.isOpened():
#    ok, image = cap.read()   
#    if not ok:
#        break

while True:
#    image = cv2.imread("images/3ft.jpg")
    image = cv2.imread("./apple.jpeg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = imutils.resize(image, width=512)
    # perform a forward pass of the network to obtain the results
    print("[INFO] making predictions with Mask R-CNN...")
    r = rcnn.detect([image], verbose=1)[0]


    # loop over of the detected object's bounding boxes and masks
    for i in range(0, r["rois"].shape[0]):
        # extract the class ID and mask for the current detection, then
        # grab the color to visualize the mask (in BGR format)
        classID = r["class_ids"][i]
        mask = r["masks"][:, :, i]
        color = COLORS[classID][::-1]
        # visualize the pixel-wise mask of the object
        image = visualize.apply_mask(image, mask, color, alpha=0.5)


    # convert the image back to BGR so we can use OpenCV's drawing
    # functions
    mage = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # loop over the predicted scores and class labels
    for i in range(0, len(r["scores"])):
        # extract the bounding box information, class ID, label, predicted
        # probability, and visualization color
        (startY, startX, endY, endX) = r["rois"][i]
        classID = r["class_ids"][i]
        label = CLASS_NAMES[classID]
        score = r["scores"][i]
        color = [int(c) for c in np.array(COLORS[classID]) * 255]
        # draw the bounding box, class label, and score of the object
        cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
        text = "{}: {:.3f}".format(label, score)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX,
                     0.6, color, 2)
    # show the output image
    cv2.imshow('video image', image)
    key = cv2.waitKey(30)
    if key == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
