import numpy as np
import cv2 as cv

# Read the image in grayscale
img = cv.imread('gull-7539615_1280.jpg', 0)

# Get image dimensions
rows, cols = img.shape

# Shrink the image
img_shrinked = cv.resize(img,(250, 200),interpolation=cv.INTER_AREA
)

# Display the shrinked image
cv.imshow('Shrinked Image', img_shrinked)

# Enlarge the shrinked image
img_enlarged = cv.resize(img_shrinked,None,fx=1.5,fy=1.5,interpolation=cv.INTER_CUBIC)

# Display the enlarged image
cv.imshow('Enlarged Image', img_enlarged)

# Wait for a key press
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()