import cv2

img=cv2.imread("C:\\Users\\op\\Desktop\\back5.png")
b_image=cv2.blur(img,(20,20))

cv2.imshow("Blurred",b_image)
