import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Opencv/Photos/boston.jpg')
cv.imshow("boston",img)

# 1. BGR to Gray Scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# 2. BGR to hsv  
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# 23. BGR to L A B  
lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)

# 4. BGR to rgb 
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

# 5. HSV to BGR   # same as lab
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR',hsv_bgr)

cv.waitKey(0)

# Open CV dispalay brg images . if you open bgr images in mathplot lab color may be distorted.
# 3 Math plot lab has no idea about br images
'''
#Mathplotlab opens bgr image
plt.imshow(img)
plt.show()
'''