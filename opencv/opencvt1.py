import cv2

image=cv2.imread("C:\\Users\\op\\Desktop\\python.jpeg")
g_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hello",g_image)
