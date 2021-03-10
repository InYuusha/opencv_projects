import cv2
import numpy as np

img= cv2.imread("C:\\Users\\op\\Desktop\\pimage.jpg")


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
surf=cv2.xfeatures2d.SURF_create()
keypoints=surf.detect(gray,None)
o=cv2.drawKeypoints(img,keypoints,gray,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS) #(iamge,keypoints,o_image,methods)
p=cv2.resize(o,(0,0),fx=0.7,fy= 0.7)
cv2.imshow("sift",p)
cv2.waitKey(0)
