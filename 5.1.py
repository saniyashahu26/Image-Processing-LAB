import cv2
import numpy
img = cv2.imread("gull-7539615_1280.jpg")
dst = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('Original vs Gaussian Blur', numpy.hstack((img, dst)))
cv2.waitKey(0)
cv2.destroyAllWindows()