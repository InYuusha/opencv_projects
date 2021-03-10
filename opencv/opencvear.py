import cv2

cap=cv2.VideoCapture(0)
mouth=cv2.CascadeClassifier("C:\\Users\\op\\AppData\\Local\\Programs\\Python\\Python37-32\\cascades\\Mouth.xml")
if mouth.empty():
    raise IOError("MOuth xml not initialised")
while True:
    bol,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    mouth_rect=mouth.detectMultiScale(gray)
    for (x,y,w,h) in mouth_rect:
        
       
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    cv2.imshow("Mouth detector",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cv2.destroyAllWindows()






