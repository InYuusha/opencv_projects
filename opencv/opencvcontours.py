import cv2
import numpy as np

def get_ref_contour(img2):
    ref_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    T,thresh=cv2.threshold(ref_gray,150,255,0)

    contours=cv2.findContours(thresh,1,2)[0]


    return contours


def get_all_contours(img1):
    img_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    T,thresh=cv2.threshold(img_gray,150,255,0)

    contours=cv2.findContours(thresh,1,2)[0]
   
    return contours



if __name__=='__main__':
    img1=cv2.imread("C:\\Users\\op\\Desktop\\allcontours.png")
    img2=cv2.imread("C:\\Users\\op\\Desktop\\ref_contour.png")
    ref_image=get_ref_contour(img2)
    contours=get_all_contours(img1)
    print(contours)

    dst=0.3
    cc=contours[0]
    for contour in contours:

         acc=cv2.matchShapes(ref_image,contour,1,0.0)
         if acc<dst:
            dst=acc
            cc=contour


    arr=np.ones((600,700),dtype=np.uint8)
    white_page=255*arr
    print(type(cc))

    cv2.drawContours(img1,[cc],0,(0,255,0))   
    cv2.imshow("Matched Contour",img1)
    cv2.waitKey(0)
   