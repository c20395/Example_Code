import pixellib
from pixellib.semantic import semantic_segmentation
import cv2

segment_frame = semantic_segmentation()
segment_frame.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")

cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cap.read()
    outfile = str(count) + ".jpg"
    segment_frame.segmentFrameAsPascalvoc(frame, output_frame_name= outfile, overlay = True)
    image = cv2.imread(outfile)
    cv2.imshow("Semantic Segmentation",image)
    count = count + 1
    k = cv2.waitKey(1) & 0xff
    if k == 27 : 
        breakcap.release()
cv2.destroyAllWindows()
