import cv2
print("Package Imported")

#img= cv2.imread("C:/Users/user/Pictures/lena.png")
cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success,image= cap.read()
    cv2.imshow("Video",image)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break





