import cv2
# Import NumPy
import numpy as np
# Read the image in grayscale
img = cv2.imread('gull-7539615_1280.jpg', 0)
# Apply Histogram Equalization
equ = cv2.equalizeHist(img)
# Stack original and equalized images side by side
res = np.hstack((img, equ))
# Display the images
cv2.imshow('Original Image and Equalized Image', res)
# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()