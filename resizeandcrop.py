import cv2 as cv
img = cv.imread("photos\yazeed.jpg")
print(img.shape)
#imgresiaze=cv.resize(img,(300,600))
cv.imshow('img',img)
imgcrop=img[0:700,0:600]
cv.imshow('im',imgcrop)
cv.waitKey(0)