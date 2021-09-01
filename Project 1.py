import cv2
frameWidth=640
frameHeight=480
cap= cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
def findColors(img):
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(img_HSV, lower, upper)
while True:
    success,image= cap.read()
    cv2.imshow("Video",image)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
