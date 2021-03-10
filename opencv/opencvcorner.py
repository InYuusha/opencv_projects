import cv2
import numpy as np 

box=cv2.imread("C:\\Users\\op\\Desktop\\box1.png")

gray=cv2.cvtColor(box,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

dst=cv2.cornerHarris(gray,4,5,0.04)
dst=cv2.dilate(dst,none)
img[dst>0.01*dst.max()]=[0,0,0]
cv2.imshow("Harris Corner",img)
