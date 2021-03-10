import cv2
img=cv2.imread("C:\\Users\\op\\Desktop\\icons.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
t,timage=cv2.threshold(gray_img,200,255,0)    # pixel above thrashold(200(that is light colours))
                                              # will turn 255(white)
cv2.imshow("Threshold image",timage)

cv2.waitKey(0)