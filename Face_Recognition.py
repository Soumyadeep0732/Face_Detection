import cv2
import numpy as np
import face_recognition
imgEmma= face_recognition.load_image_file('C:/Users/user/Downloads/IMG_1918.jpg')
imgEmma=cv2.cvtColor(imgEmma,cv2.COLOR_BGR2RGB)
imgTest= face_recognition.load_image_file('C:/Users/user/Pictures/emtese.jpg')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLocation=face_recognition.face_locations(imgEmma)[0]
encodingEmma=face_recognition.face_encodings(imgEmma)[0]
cv2.rectangle(imgEmma,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]),(255,0,255),2)

faceLocationtest=face_recognition.face_locations(imgTest)[0]
encodingEmmaTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocationtest[3],faceLocationtest[0]),(faceLocationtest[1],faceLocationtest[2]),(255,0,255),2)

results=face_recognition.compare_faces([encodingEmma],encodingEmmaTest)
faceDist=face_recognition.face_distance([encodingEmma],encodingEmmaTest)
print(results,faceDist)

cv2.putText(imgTest,f'{results} {round(faceDist[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('Emma',imgEmma)
cv2.imshow('Emma Test',imgTest)
cv2.waitKey(0)
