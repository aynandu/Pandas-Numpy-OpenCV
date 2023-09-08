import cv2 as cv
import numpy as np


blank= np.zeros((500,500,3),dtype='uint8')  #(Width,Height, 0r Color Channel (ratio) )
#cv.imshow("Blank",blank)

# 1.Paint the image a Certain color
blank[200:300]=0,255,0
cv.imshow("Green",blank)

# 2.Draw a Rectangle
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
#cv.imshow('Rectangle',blank)

# 3.Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,225),thickness=2)
#cv.imshow('Circle',blank)

#4.Draw line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=2)
cv.imshow('Line',blank)

#5. Draw Text
cv.putText(blank,"Hello word",(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,100,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)