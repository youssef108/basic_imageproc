import cv2 as cv
import numpy as np
def getContours(img):
    contours,hierarchy=cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv.contourArea(cnt)
        if area > 300:
            cv.drawContours(imgcontour,cnt,-1,(0,255,0),1)
            #print(area)
            parameter=cv.arcLength(cnt,True)
            #print(parameter)
            approx=cv.approxPolyDP(cnt,0.03*parameter,True)
            print(len(approx))
            objcont=len(approx)
            x,y,w,h=cv.boundingRect(approx)
            if objcont ==3: objecttype='tri' 
            elif objcont ==4: 
                aspratio=w/float(h)
                if aspratio >0.95 and aspratio<1.05: 
                    objecttype='sqr'
                else:
                    objecttype='rec'    
            elif objcont ==6: objecttype='hex'
            elif objcont >6: objecttype='cir'
            else: objecttype='none'   
            cv.rectangle(imgcontour,(x,y),(x+w,y+h),(255,0,0),1)
            cv.putText(imgcontour,objecttype,(x+(w//2)-10,y+(h//2)-10),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)



img=cv.imread('photos\shapes.jpg')
imgG=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgB=cv.GaussianBlur(imgG,(7,7),1)
imgC=cv.Canny(imgB,50,50)
imgcontour=img.copy()
cv.imshow('img',img)
cv.imshow('gray',imgG)
cv.imshow('blur',imgB)
cv.imshow('blur',imgC)

getContours(imgC)
cv.imshow('countors',imgcontour)
cv.waitKey(0)