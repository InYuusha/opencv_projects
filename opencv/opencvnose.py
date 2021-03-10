import cv2

cap=cv2.VideoCapture(0)
nose=cv2.CascadeClassifier("C:\\Users\\op\\AppData\\Local\\Programs\\Python\\Python37-32\\cascades\\Nariz.xml")
if nose.empty():
    raise IOError("Nose xml not initialised")
while True:
    bol,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    nose_rect=nose.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in nose_rect:
        cv2.rectangle(frame,(x,y),(w+x,h+y),(0,255,0),5)
    cv2.imshow("Nose Detector",frame)    
    k=cv2.waitKey(1)
    if k==ord('q'):
         break
cv2.destroyAllWindows()