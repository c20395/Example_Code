# Example 9.4a
# Read out all the frames in the video
import cv2
from tqdm import tqdm
video = cv2.VideoCapture("work/person.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("Total Frames：",frameCount)
success, frame = video.read() 
index = 0
for i in tqdm(range(int(frameCount)),desc='Progress'):
    if success:
        cv2.imwrite('work/target/'+str(index)+'.jpg', frame)
    success, frame = video.read()
    index += 1

