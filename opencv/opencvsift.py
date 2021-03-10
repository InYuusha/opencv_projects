import cv2
import numpy as np

img=cv2.imread("C:\\Users\\op\\Desktop\\pimage.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift=cv2.xfeatures2d.SIFT_create()
keypoints=sift.detect(gray,None)
o_image=cv2.drawKeypoints(img,keypoints,gray , flags=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
cv2.imshow("SIFT",o_image)
cv2.waitKey(0)