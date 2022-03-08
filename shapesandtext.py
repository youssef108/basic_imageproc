import cv2 as cv
import numpy as np
img = np.zeros((512,512,3),np.uint8)
img[:] = 255,0,0

cv.line(img,(0,0),(300,300),(0,0,255),2)
cv.rectangle(img,(0,0),(300,300),(0,255,0),3)
cv.circle(img,(300,300),(30),(30,100,60),4)
cv.putText(img,"text",(70,60),cv.FONT_HERSHEY_SCRIPT_COMPLEX,3,(200,200,0),2)
cv.imshow('img',img)
cv.waitKey(0)

