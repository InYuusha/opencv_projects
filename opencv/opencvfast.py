import numpy as np
import cv2

image=cv2.imread("C:\\Users\\op\\Desktop\\pimage.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
fast=cv2.FastFeatureDetector()
keypoint=fast.detect(gray,None)
o_image=cv2.drawKeypoints(image,keypoint,gray,flasgs=cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS)
cv2.imshow("Fast",o_image)
cv2.waitKey(0)