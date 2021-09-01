import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
#img[:]=0,0,255
cv2.line(img,(200,200),(300,300),(0,255,255),2)
cv2.rectangle(img,(200,200),(400,400),(0,0,255),cv2.FILLED)
cv2.circle(img,(200,300),50,(0,255,250),3)
cv2.putText(img,"HALO",(300,450),cv2.FONT_ITALIC,1,(0,156,189),1)
cv2.imshow("Image",img)
cv2.waitKey(0)