

'''CREATING A MOTION SENSOR  '''

'''        FOLLOW          '''
'''   ------------------   '''

#                    @Ddoingstuffswithpython

import numpy as np
import cv2

def get_frame(cap):
    ret,frame=cap.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    return gray_img

def frame_diff(pre_frame,cur_frame,nex_frame):

    diff1=cv2.absdiff(nex_frame,cur_frame)
    diff2=cv2.absdiff(cur_frame,pre_frame)

    return cv2.bitwise_and(diff1,diff2)    


if __name__=='__main__':
    cap=cv2.VideoCapture(0)
    pre_frame=get_frame(cap)
    cur_frame=get_frame(cap)
    nex_frame=get_frame(cap)

    while True:
         cv2.imshow("frame Diff",frame_diff(pre_frame,cur_frame,nex_frame))

         #prev_frame= cur_frame
         cur_frame=nex_frame
         nex_frame=get_frame(cap)
         
         key=cv2.waitKey(10)
         if key==ord('q'):
             break
cv2.destroyAllWindows()            
 
