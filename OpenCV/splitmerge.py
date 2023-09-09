import cv2 as cv
import numpy as np


img = cv.imread('Opencv/Photos/boston.jpg')
cv.imshow("boston",img)

# 1. display b,g,r from the img
b,g,r=cv.split(img)
cv.imshow("Blue",b)
cv.imshow("Red",r)
cv.imshow("Green",g)

print(f'img.shape {img.shape} , b.shape {b.shape} ,r.shape {r.shape} ,g.shape {g.shape}')

# 2.Merged bgr
merged = cv.merge([r,b,g])
cv.imshow('merged image', merged)

# 3.Combine Blank with B,g,r
blank=np.zeros(img.shape[:2],dtype='uint8')
blue=cv.merge([b,blank,blank])
red=cv.merge([blank,blank,r])
green=cv.merge([blank,g,blank])
cv.imshow("Blank --> Blue",blue)
cv.imshow("Blank --> Red",red)
cv.imshow("Blank --> Green",green)

cv.waitKey(0)