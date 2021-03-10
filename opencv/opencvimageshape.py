import cv2
import numpy as np

img=cv2.imread("C:\\Users\\op\\Desktop\\python.jpeg")
rows,col=img.shape[:2]
print(rows,col)
rot_matrice=cv2.getRotationMatrix2D((rows/2,col/2),30,1)
r_image=cv2.warpAffine(img,(rot_matrice),(rows,col))
cv2.imshow("rotated",r_image)
