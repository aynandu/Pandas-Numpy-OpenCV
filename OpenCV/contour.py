import cv2 as cv
import numpy as np

# contour - identifying the object edges
img = cv.imread('Opencv/Photos/cats.jpg')
cv.imshow("cats",img)
# gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) # increase Blur by  increasing Ksize (3,3)--> (7,7)
cv.imshow('Blur',blur)

# canny
canny=cv.Canny(img,125,175)
cv.imshow('Canny', canny)

#Threshold
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresold', thresh)

#blank
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow("Blank",blank)

#Contours
#The boundary or contour marks the outline of an object in an image. 
# So, detecting contours plays a vital role in applications for identifying and segmenting objects in an image. 
# A contour consists of the pixels in an object's boundary:
# These pixels are usually of the same color, differentiating them from the rest.
contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #use Canny img to peform contour ; no direct blur
print(f'{len(contours)} Countour(s) found !')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)