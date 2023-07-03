import numpy as np
import cv2 as cv

# อ่านภาพจากไฟล์
img = cv.imread('classwork_2/circle.jpg', cv.IMREAD_GRAYSCALE)

contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for contour in contours:
    (x, y), radius = cv.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    cv.circle(img, center, radius, (0, 255, 0), 2)

cv.imshow('Circle', img)
cv.waitKey(0)
cv.destroyAllWindows()