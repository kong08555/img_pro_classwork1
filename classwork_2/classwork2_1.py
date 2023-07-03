import cv2 as cv
import numpy as np

# อ่านภาพ
img = cv.imread('classwork_2/circle Objects.png')

# แปลงสีขาวเป็นสีดำ
#img[np.where((img != [255, 255, 255]).all(axis=2))] = [0, 0, 0]

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred = cv.medianBlur(gray, 25) 

minDist = 50
param1 = 50
param2 = 43  
minRadius = 5
maxRadius = 100 

circles = cv.HoughCircles(blurred, cv.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
cv.imshow('Modified Image with Circles', img)
cv.waitKey(0)
cv.destroyAllWindows()
