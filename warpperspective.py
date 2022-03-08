import cv2 as cv
import numpy as np
img =cv.imread("photos\cards.jpg")
print(img.shape)
hieght,width=350,250
pts1=np.float32([[215,29],[270,23],[224,107],[288,100]])
pts2=np.float32([[0,0],[width,0],[0,hieght],[width,hieght]])
matrix=cv.getPerspectiveTransform(pts1,pts2)
img2=cv.warpPerspective(img,matrix,(width,hieght))
cv.imshow("img",img2)
cv.waitKey(0)