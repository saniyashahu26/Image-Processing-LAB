import cv2
import numpy as np
img = cv2.imread("gull-7539615_1280.jpg")
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()
dst = cv2.bilateralFilter(img, 9, 75, 75)
combined = np.hstack((img, dst))
cv2.imshow('Original vs Bilateral Filter', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()