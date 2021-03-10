import cv2
import numpy as np

image=cv2.imread("C:\\Users\\op\\Desktop\\python.jpeg")
row,col=image.shape[:2]
print(image.shape)


r_matrix=cv2.getRotationMatrix2D((row/2,col/2),45,0.5)
img_rotated=cv2.warpAffine(image,(r_matrix),(row,col))
cv2.imshow('ROtated',img_rotated)

