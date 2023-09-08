import cv2 as cv
import numpy as np

img = cv.imread('Opencv/Photos/boston.jpg')
cv.imshow("boston",img)

# 1. Transilate Image
def translate(img, x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)
# -x  --> left
# -y  --> up
# x  --> Right
# y  --> bottom
translated = translate(img,100,100)
cv.imshow('Transalated', translated)

# 2.Rotation
def rotate (img , angle ,rotPoint=None):
   (height,width)=img.shape[:2]
   if rotPoint is None:
       rotPoint = (width//2,height//2) # rotate from Centre
   rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
   dimension = (width, height)
   return cv.warpAffine(img,rotMat,dimension)

rotated = rotate(img ,-45)  
cv.imshow("rotated",rotated)

# 3. Resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

# 4.flipping
flip=cv.flip(img,1)  # 0 --> fliping the img vertically over the x axis ; 1--> horizontaly  y axis  ; -1 --> both horizontally and vertically
cv.imshow('flipping',flip)

# 5. Cropped
cropped= img[200:400,300:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)