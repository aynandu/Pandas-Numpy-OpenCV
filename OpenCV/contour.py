import cv2 as cv
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
canny=cv.Canny(blur,125,175)
cv.imshow('Canny', canny)

#Threshold
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresold', thresh)

#Contours
contours,hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #use Canny img to peform contour ; no direct blur
print(f'{len(contours)} Countour(s) found !')

cv.waitKey(0)