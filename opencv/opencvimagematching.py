import numpy as np 
import cv2
import sys
def draw_matches(img1,keypoints,img2,keypoints2,matches):
     rows1,cols1=img1.shape[:2]
     rows2,cols2=img2.shape[:2]

     output_img=np.zeros((max(rows1,rows2),cols1+cols2,3),dtype=np.uint8)
     output_img[:rows1,:cols1]=np.dstack([img1,img1,img1])
     output_img[:rows2,:cols2]=np.dstack([img2,img2,img2])

     for match in matches:
         img1_idx=match.queryIdx
         img2_idx=match.trainIdx
         (x1, y1) = keypoints1[img1_idx].pt
         (x2, y2) = keypoints2[img2_idx].pt

         radius=4
         colour=(0,255,0)
         thickness=1
         cv2.circle(output_img,(int(x1),int(y1)),radius,colour,thickness)
         cv2.circle(output_img, (int(x2)+cols1,int(y2)), radius, colour,
         thickness)
         cv2.line(output_img, (int(x1),int(y1)), (int(x2)+cols1,int(y2)),
         colour, thickness)
         return output_img
if __name__=='__main__':
    ig1 = cv2.imread("C:\\Users\\op\\Desktop\\pimage_orig.png") 
    ig2 = cv2.imread("C:\\Users\\op\\Desktop\\pimage.jpg")

    img1=cv2.cvtColor(ig1,cv2.COLOR_BGR2GRAY)

    img2=cv2.cvtColor(ig2,cv2.COLOR_BGR2GRAY)

    surf = cv2.xfeatures2d.SURF_create()  #initialising surf
    keypoints1, descriptors1 = surf.detectAndCompute(img1,None)   # it returns location of all those keypoint and the description of each keypoint
    keypoints2, descriptors2 = surf.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(descriptors1, descriptors2)   #matches the featues of each keypoint in case image is larger or smaller

    matches = sorted(matches, key = lambda x:x.distance)

    img3 = draw_matches(img1, keypoints1, img2, keypoints2, matches[:30])
    cv2.imshow('Matched keypoints', img3)
    cv2.waitKey()


