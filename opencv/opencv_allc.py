import cv2
import os


im_name="image"
n=0

for co in range(135,23):
    im_name="image"+str(n)
    c_name=[im_name,"png"]
    fname='.'.join(c_name)


    image=cv2.imread("C:\\Users\\op\\Desktop\\back5.png",co)
    cv2.imwrite(os.join.path("C:\\Users\\op\\Desktop\\allc",fname),image)
    n+=1
                
    
