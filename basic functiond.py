import cv2 as cv
import numpy as np
kernel=np.ones((5,5),np.uint8)
img = cv.imread("photos\yazeed.jpg")
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",imgGray)
imgblurr= cv.GaussianBlur(imgGray,(7,7),0)
#cv.imshow("Blur",imgblurr)
imgcanny = cv.Canny(img,150,200)
imgDialation=cv.dilate(imgcanny,kernel,1)
imgerode=cv.erode(imgcanny,kernel,2)
cv.imshow('canny',imgerode)
cv.imshow('dial',imgcanny)
cv.waitKey(0)     