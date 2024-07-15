# Example 7.6a
# https://github.com/OlafenwaMoses/ImageAI
# Only works for TensorFlow 1.X
# pip install imageai

import matplotlib.pyplot as plt
from imageai.Detection import ObjectDetection
import os
import cv2

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior

execution_path = os.getcwd()
print(execution_path)
input_image=os.path.join(execution_path , "fruits.jpeg")

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
#detector.setModelTypeAsYOLOv3()
#detector.setModelPath(os.path.join(execution_path , "yolo.h5")) # Download the model via this link https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0

detector.loadModel()
detections = detector.detectObjectsFromImage(input_image, output_image_path=os.path.join(execution_path , "imagenew.jpg"))

    
for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] , " : ", eachObject["box_points"] )
    x1= int(eachObject["box_points"][0])
    y1= int(eachObject["box_points"][1])
    x2= int(eachObject["box_points"][2])
    y2= int(eachObject["box_points"][3])
    start_point = (x1,y1)
    end_point = (x2,y2)
    image = cv2.rectangle(image, start_point, end_point, color, thickness)
    cv2.putText(image, eachObject["name"] , (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color , thickness)


# Displaying the image 
cv2.imshow(window_name, image)
