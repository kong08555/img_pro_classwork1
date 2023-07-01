import numpy as np
import cv2 as cv

img_1 = np.zeros([300, 300], dtype=np.uint8)

center_1 = (140, 100)
radius_1 = 30

center_2 = (180, 100)
radius_2 = 30

cv.circle(img_1, center_1, radius_1, 200, -1)
cv.circle(img_1,center_2,radius_2,200,-1)

cv.imwrite('classwork_2/circle.jpg', img_1)

cv.waitKey(0)
cv.destroyAllWindows()