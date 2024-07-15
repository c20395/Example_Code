# Detect QRCode using the cv2 QRCode detector
import cv2

img = cv2.imread('qrcode001.png')
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)
# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        point1 = tuple(bbox[i][0].astype(int))
        point2 = tuple(bbox[i][2].astype(int))
        cv2.rectangle(img, point1, point2, (255, 0, 0), 2)# display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
