import cv2
import numpy as np
image=255*np.ones((600,700),dtype=np.uint8)

cv2.rectangle(image,(50,50),(200,200),(0,0,0),-1)
cv2.imshow("REct",image)
