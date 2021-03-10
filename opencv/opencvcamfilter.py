import argparse
import cv2

def argument_parse():
    parser=argparse.ArgumentParser(description=" Press Between 'a','s','d' ")
    return parser

if __name__=='__main__':
    cap=cv2.VideoCapture(0)
    if  not cap.isOpened():
        raise IOError("Cannot open Cam")
    c_char=-1
    p_char=-1
        
while True:
    
    argument_parse().parse_args()
    bol,frame=cap.read()
    
    k=cv2.waitKey(1)
    if k==ord('e'):
        break
    if k>-1 and k!=p_char:
        c_char=k
    p_char=k    
    
    if c_char==ord('a'):
        output=cv2.cvtColor(frame,cv2.IMREAD_GRAYSCALE)
    elif c_char==ord('s'):
        output=cv2.cvtColor(frame,cv2.cv2.COLOR_BGR2GRAY)
    elif c_char==ord('d'):
        output=cv2.cvtColor(frame,cv2.COLOR_LBGR2Lab)
    else:
        output=frame
        
    cv2.imshow("Cam",output)
cv2.destroyAllWindows()    
        
    
    
