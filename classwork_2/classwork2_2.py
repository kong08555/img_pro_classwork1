import numpy as np
import cv2 as cv

# อ่านภาพจากไฟล์
img = cv.imread('classwork_2/center_spot_circle.png')

cv.imshow('Circle', img)
cv.waitKey(0)
cv.destroyAllWindows()
#หาจุดศุนย์กลางได้ แต่ยังทำให้วาดวลกลมออกมาเป็นจุดศูนย์กลางยังไม่ได้