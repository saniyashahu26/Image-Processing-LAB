import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('gull-7539615_1280.jpg', 0)  # Grayscale
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imshow('Original vs Equalized', res)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(img.ravel(), 256, [0, 256], color='blue')
plt.title('Original Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.subplot(1, 2, 2)
plt.hist(equ.ravel(), 256, [0, 256], color='green')
plt.title('Equalized Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()