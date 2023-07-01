import numpy as np
import cv2 as cv

img_fred = cv.imread('classwork_1/fred.jpg', cv.IMREAD_GRAYSCALE)
img_line = cv.imread('classwork_1/line.jpg', cv.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), dtype=np.uint8)

convol_img = cv.filter2D(img_fred, -1, kernel)

cv.imwrite('classwork_1/Fred_Image.jpg', img_fred)
cv.imwrite('classwork_1/Convolution_Image.jpg', convol_img)

cv.waitKey(0)

cv.destroyAllWindows()