# Example 9.4c

# Next put all the frames back into a video
import os
import cv2
import datetime
file_dict = {}
video = cv2.VideoCapture("work/person.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
for i in os.listdir('work/result/'):
    filename, file_extension = os.path.splitext(i)
    if file_extension != '.jpg':
        continue
    file_dict['work/result/'+i] = float(i.replace('ndarray_','').replace('.jpg',''))
file_dict = sorted(file_dict.items(),key = lambda x:x[1])
videoWriter = cv2.VideoWriter('trans.avi', cv2.VideoWriter_fourcc(*"MJPG"), fps, size)
flag = True
for i in file_dict:
    if flag:
        for j in range(34):
            videoWriter.write(cv2.imread('work/target/0.jpg'))
        flag = False
    videoWriter.write(cv2.imread(i[0]))
videoWriter.release()
cv2.destroyAllWindows()


