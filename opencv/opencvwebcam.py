import cv2
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,None,fx=0,fy=0.5,interpolation=cv2.INTER_AREA)
    cv2.imshow('INput',frame)
    c=cv2.waitKey(1)
    if c==ord('e'):
        break
cap.release()    
    
