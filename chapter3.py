import cv2
import numpy as np
img = cv2.imread('C:/Users/user/Pictures/lambo.png')
img_resize=cv2.resize(img,(300,200))
img_cropped=img[0:200,200:400]
cv2.imshow("Image",img)
cv2.imshow("Image Cropped",img_cropped)

cv2.waitKey(0)
