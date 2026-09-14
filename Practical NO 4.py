import cv2
import numpy as np
img = cv2.imread('gull-7539615_1280.jpg', 0)
negative = 255 - img
combined = np.hstack((img, negative))
cv2.imshow('Original (Left) vs Negative (Right)', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()