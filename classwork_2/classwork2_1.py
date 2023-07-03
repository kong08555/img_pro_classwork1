import cv2 as cv
import numpy as np

img = cv.imread('classwork_2/circle Objects.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred = cv.medianBlur(gray, 25) 

minDist = 50     #ระยะห่างขั้นต่ำระหว่างวงกลม
param1 = 50      #พารามิเตอร์ที่ใช้ในการกรองเส้นของการตรวจจับวงกลม
param2 = 43      #พารามิเตอร์ที่กำหนดระดับเชื่อมโยงระหว่างวงกลมที่ตรวจจับแล้ว
minRadius = 5    #รัศมีวงกลมขั้นต่ำที่ต้องการให้ตรวจจับ
maxRadius = 100  #รัศมีวงกลมสูงสุดที่ต้องการให้ตรวจจับ

#ตรวจจับวงกลมโดยใช้ค่าparamiter
circles = cv.HoughCircles(blurred, cv.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

#วาดวงกลมที่ตรวจพบ
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        center = (i[0], i[1])
        cv.circle(img, center, 3, (255, 0, 0), -1)
cv.imshow('Modified Image with Circles', img)
cv.imwrite('classwork_2/center_spot_circle.png',img)

cv.waitKey(0)
cv.destroyAllWindows()
