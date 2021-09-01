import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
path='Images Attendance'
images=[]
classnames=[]
mylist=os.listdir(path)
for cls in mylist:
    currentImg=cv2.imread(f'{path}/{cls}')
    images.append(currentImg)
    classnames.append(os.path.splitext(cls)[0])

def findEncodings(images):
    encodinglist=[]
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(img)[0]
        encodinglist.append(encoding)
    return encodinglist
def markAttendance(name):
    with open('attend.csv','r+') as f:
        mydatalist=f.readlines()
        namelist=[]
        for line in mydatalist:
            entry=line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now=datetime.now()
            dtstring=now.strftime("%H:%M:%S")
            f.writelines(f'\n{name},{dtstring}')



encodelistknown=findEncodings(images)
print('Encoding Completed')
cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    imgsmall=cv2.resize(img,(0,0),None,0.25,0.25)
    imgsmall= cv2.cvtColor(imgsmall, cv2.COLOR_BGR2RGB)
    faceLocationCurr = face_recognition.face_locations(imgsmall)
    encodingcurr = face_recognition.face_encodings(imgsmall,faceLocationCurr)

    for encodeface,faceloc in zip(encodingcurr,faceLocationCurr):
        matches=face_recognition.compare_faces(encodelistknown,encodeface)
        facedist=face_recognition.face_distance(encodelistknown,encodeface)
        print(facedist)
        matchIndex=np.argmin(facedist)
        if matches[matchIndex]:
            name=classnames[matchIndex]
            print(name)
            y1,x2,y2,x1=faceloc
            y1, x2, y2, x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)


    cv2.imshow('Webcam',img)
    cv2.waitKey(1)



