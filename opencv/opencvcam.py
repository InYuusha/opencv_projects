import cv2
cap=cv2.VideoCapture(0)
 
if not cap.isOpened():
    raise IOError("Cannot Open Webcam")
  
while True:
    bol,frame=cap.read()    #it must be inside while to initialise frame evry time
 
    #cv2.resize(frame,None,fx=1,
    cv2.imshow("cam",frame)
    k=cv2.waitKey(33)
    if k==ord('q'):
        break

cv2.destroyAllWindows()    
    
    
