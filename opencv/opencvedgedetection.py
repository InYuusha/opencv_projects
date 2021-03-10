import numpy as np
import cv2

img=cv2.imread("C:\\Users\\op\\Desktop\\back5.png",cv2.IMREAD_GRAYSCALE)
rows,col=img.shape[:2]
sobel_horizontal=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=7)
sobel_vertical=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

lap=cv2.Laplacian(img,cv2.CV_64F)

cv2.imshow("sobel_h",sobel_horizontal)
cv2.imshow("sobel_v",sobel_vertical)
cv2.imshow("lap",lap)

