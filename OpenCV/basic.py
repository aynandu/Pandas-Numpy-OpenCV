import cv2 as cv

img = cv.imread('Opencv/Photos/boston.jpg')
cv.imshow('Lady',img)

# 1. Converting Gray image
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) # increase Blur by  increasing Ksize (3,3)--> (7,7)
cv.imshow('Blur',blur)

# 3. Edge Cascade - (Canny Edge detection by opencv)
canny=cv.Canny(img,125,175)
cv.imshow('Edge Detection', canny)

# 4. Dilated Images
dilated = cv.dilate(canny,(3,3),iterations=1)   # increase Blur by  increasing kenernal size (3,3)--> (7,7)
cv.imshow("Dilated",dilated)

# 5.Eroded
eroded=cv.erode(dilated,(3,3),iterations=2)
cv.imshow("Eroded",eroded)

# 6. Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)  # interpolation=cv.INTER_AREA / cv.INTER_LINEAR / cv.INTER_CUBIC
cv.imshow('Resize',resized)

# 7. Cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)