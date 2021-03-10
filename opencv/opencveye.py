import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier("C:\\Users\\op\\AppData\\Local\\Programs\\Python\\Python37-32\\cascades\\haarcascade_frontalface_alt.xml")
eye_cascade=cv2.CascadeClassifier("C:\\Users\\op\\AppData\\Local\\Programs\\Python\\Python37-32\\cascades\\haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
if  face_cascade.empty():
    raise IOError("FAce cascade not initialised")
if  eye_cascade.empty():
    raise IOError("Eye Cascade Not Initialised")
while True:
    bol,frame=cap.read()
    cv2.resize(frame,None,fx=0.2,fy=0.5,interpolation=cv2.INTER_AREA)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rect=face_cascade.detectMultiScale(gray,1.3)
    for (x,y,w,h) in rect:
        gray_face=gray[y:y+h,x:x+h]
        color_face=frame[y:y+h,x:x+h]
        eye=eye_cascade.detectMultiScale(gray_face)
        for (eye_x,eye_y,eye_w,eye_h) in eye:
            center=(int(eye_x+0.5*eye_w),int(eye_y+0.5*eye_h))
            radius=int(0.3*(eye_w+eye_h))
            cv2.circle(color_face,(center),radius,(0,255,0),3)

    cv2.imshow("face detector",frame)
    k=cv2.waitKey(10)
    if k==ord('q'):
        break
cv2.destroyAllWindows()    
    
    

