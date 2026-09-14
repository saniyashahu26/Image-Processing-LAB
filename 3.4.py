import numpy as np
import cv2 as cv
img = cv.imread('gull-7539615_1280.jpg', 0)
cropped_img = img[100:300, 100:300]
cv.imshow('cropped_out.jpg', cropped_img)
cv.imwrite('cropped_out.jpg', cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()