import numpy as np
import cv2 as cv

img_1 = np.zeros([300, 300], dtype=np.uint8)

start = (150, 150)
end = (3, 70)

dx = end[0] - start[0]
dy = end[1] - start[1]
slope = dy / dx if dx != 0 else np.inf
intercept = start[1] - slope * start[0]

for x in range(img_1.shape[1]):
    y = int(slope * x + intercept)
    if 0 <= y < img_1.shape[0]:
        img_1[y, x] = 255
        

cv.imwrite('classwork_1/line.jpg', img_1)
cv.imshow('line', img_1)
cv.waitKey(0)

cv.destroyAllWindows()
#this code is drawing line