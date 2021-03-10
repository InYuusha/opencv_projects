import cv2
import numpy as np


image=cv2.imread("C:\\Users\\op\\Desktop\\python.jpeg")
row,col=image.shape[:2]
src=np.float32(([0,0],[col-1,0],[0,row-1]))
drc=np.float32(([col-1,0],[0,0],[col-1,row-1]))

               
t_matrix=cv2.getAffineTransform(src,drc,)
t_image=cv2.warpAffine(image,(t_matrix),(row,col))
cv2.imshow("Input",image)
cv2.imshow("transformed",t_image)
