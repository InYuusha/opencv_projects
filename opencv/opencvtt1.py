import cv2
import numpy as np

cascade_f=cv2.CascadeClassifier("C:\\Users\\op\\AppData\\\\Local\\Programs\\Python\\Python37-32\\cascades\\haarcascade_frontalface_alt.xml")

cap=cv2.VideoCapture(0)

while True:
    bol,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rect=cascade_f.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in rect:
        cv2.rectangle(frame,(x,y),(w+x,h+y),(0,255,0),5)
    k=cv2.waitKey(1)
    if k==ord('q'):
       break

    cv2.imshow("cam",frame)
cv2.destroyAllWindows()    
