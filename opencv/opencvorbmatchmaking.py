

''' MATCHING KEYPOINTS DESCRIPTOR IN TWO SIMILAR IMAGES 
    AFTER AFFINE TRANSFORM     
                                          @doingstuffswithpython
            FOLLOW
  -----------------------------------
  ------------------------------------                    '''                                        


import numpy as np
import cv2

image_orig=cv2.imread("C:\\Users\\op\\Desktop\\book.jpg")
image=cv2.imread("C:\\Users\\op\\Desktop\\book1.png")

image1=cv2.resize(image_orig,None,fx=1.1,fy=1.3)
image2=cv2.resize(image,None,fx=1.3,fy=1.3)

img1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

orb=cv2.ORB_create()
orig_keypoints,desc1=orb.detectAndCompute(img1,None)
keypoints,desc2=orb.detectAndCompute(img2,None)

matcher=cv2.BFMatcher()
matches=matcher.match(desc1,desc2)

matches=sorted(matches,key=lambda x: x.distance)

f_image=cv2.drawMatches(image1,orig_keypoints,image2,keypoints,matches[:50],None)
done=cv2.resize(f_image,None,fx=0.8,fy=0.8)
cv2.imshow("matches",done)

cv2.waitKey(0)
