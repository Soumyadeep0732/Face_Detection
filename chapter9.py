# FACE DETECTION
import cv2

faceCasade=cv2.CascadeClassifier('https://github.com/murtazahassan/Learn-OpenCV-in-3-hours/blob/d4d6a14c7151aa4ebe23eb2a7cc8f94db05384c3/Resources/haarcascade_frontalface_default.xml')
img= cv2.imread("C:/Users/user/Pictures/lena.png")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faceCasade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow("Result", img)
cv2.waitKey(0)