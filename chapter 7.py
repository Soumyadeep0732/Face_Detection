#COLOR DETECTION
import cv2
import numpy as np
#Using the stacked function to use later
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
def empty(a):
    pass
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",600,300)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",26,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",154,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",146,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)
while True:
    img = cv2.imread('C:/Users/user/Pictures/lambo.png')
    img_HSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hue_min=  cv2.getTrackbarPos("Hue Min","Trackbars")
    hue_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    sat_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    sat_max  =cv2.getTrackbarPos("Sat Max", "Trackbars")
    val_min=cv2.getTrackbarPos("Val Min", "Trackbars")
    val_max=cv2.getTrackbarPos("Val Max", "Trackbars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
    lower=np.array([hue_min,sat_min,val_min])
    upper=np.array([hue_max,sat_max,val_max])
    mask=cv2.inRange(img_HSV,lower,upper)
    imgoutput=cv2.bitwise_and(img,img,mask=mask)
    imgstack=stackImages(0.5,([img,img_HSV],[mask,imgoutput]))

    #cv2.imshow("Original",img)
    #cv2.imshow("HSV",img_HSV)
    #cv2.imshow("Mask",mask)
    #cv2.imshow("Result",imgoutput)
    cv2.imshow("Stacked", imgstack)
    cv2.waitKey(1)