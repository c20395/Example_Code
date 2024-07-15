# Example 7.17 18 OpenCV multi-objects tracking
# Modified based on:
# https://stackoverflow.com/questions/54730427/multi-object-tracking-initialization-in-opencv-using-multitracker-object
# Worked for multi Object tracking
# This programe doesn't work for OpenCV > 4.5.0

import imutils
import cv2
from random import randint

trackerName = 'csrt'

OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,
    "tld": cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,
    "mosse": cv2.TrackerMOSSE_create
}

# initialize OpenCV's special multi-object tracker
trackers = cv2.MultiTracker_create()
cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()

    if frame is None:
        break

    frame = imutils.resize(frame, width=600)
    (success, boxes) = trackers.update(frame)

    # loop over the bounding boxes and draw them on the frame
    count = 1
    for box in boxes:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, str(count) , (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
        print(count)
        count = count + 1
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 's' key is selected, we are going to "select" a bounding
    # box to track
    if key == ord("s"):
        colors = []
        # select the bounding box of the object we want to track (make
        # sure you press ENTER or SPACE after selecting the ROI)
        box = cv2.selectROIs("Frame", frame, fromCenter=False,
                             showCrosshair=True)
        box = tuple(map(tuple, box)) 
        for bb in box:
            tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
            trackers.add(tracker, frame, bb)

    # if you want to reset bounding box, select the 'r' key 
    elif key == ord("r"):
        trackers.clear()
        trackers = cv2.MultiTracker_create()

        box = cv2.selectROIs("Frame", frame, fromCenter=False,
                            showCrosshair=True)
        box = tuple(map(tuple, box))
        for bb in box:
            tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
            trackers.add(tracker, frame, bb)

    elif key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
