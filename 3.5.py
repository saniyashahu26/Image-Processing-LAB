import numpy as np
import cv2 as cv

# Read the image in grayscale
img = cv.imread('gull-7539615_1280.jpg', 0)

# Get image dimensions
rows, cols = img.shape

# Define the shearing matrix
M = np.float32([
    [1, 0.5, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Apply shear transformation
sheared_img = cv.warpPerspective(img,M,(int(cols * 1.5), int(rows * 1.5)))

# Display the sheared image
cv.imshow('Sheared Image', sheared_img)

# Wait for a key press
cv.waitKey(0)

# Close all OpenCV windows
cv.destroyAllWindows()